#!/usr/bin/env python3
"""Génère des versions d'affichage (WebP + JPEG, 640 et 1200 px) et
met à jour uniquement le balisage <img>/<picture> des articles, sans
toucher au texte, aux légendes, ni aux originaux. Les liens href/data-full
vers l'original sont conservés."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = []
ARTICLES += sorted((ROOT / "contenus" / "tests").glob("*/article.md"))
ARTICLES += sorted((ROOT / "contenus" / "guides").glob("*/article.md"))

SKIP_CLASS = re.compile(r'\bclass="[^"]*\b(card-thumb|auteur-logo)\b[^"]*"')
BANNED = re.compile(r'(?:^|/)(64|66)[-_]')
LIQUID_SRC = re.compile(
    r"""\{\{\s*'(?P<path>/[^']+)'\s*\|\s*relative_url\s*\}\}"""
)
ATTR_RE = re.compile(
    r'([^\s=]+)(?:\s*=\s*("([^"]*)"|\'([^\']*)\'|[^\s>]+))?',
    re.I,
)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
PICTURE_RE = re.compile(r"<picture\b[^>]*>[\s\S]*?</picture>", re.I)

TARGET_WIDTHS = (640, 1200)
WEBP_QUALITY = 80
JPEG_QUALITY = 82


def parse_attrs(tag: str) -> dict[str, str]:
    inner = tag.strip()
    if inner.startswith("<"):
        inner = inner[1:]
    # drop tag name
    inner = re.sub(r"^(img|source|picture)\b", "", inner, flags=re.I).strip()
    if inner.endswith("/>"):
        inner = inner[:-2].strip()
    elif inner.endswith(">"):
        inner = inner[:-1].strip()
    attrs: dict[str, str] = {}
    for m in ATTR_RE.finditer(inner):
        key = m.group(1)
        if key == "/":
            continue
        raw = m.group(2)
        if raw is None:
            attrs[key] = ""
        elif raw.startswith('"') and raw.endswith('"'):
            attrs[key] = raw[1:-1]
        elif raw.startswith("'") and raw.endswith("'"):
            attrs[key] = raw[1:-1]
        else:
            attrs[key] = raw
    return attrs


def resolve_src(src: str, article: Path) -> Path | None:
    src = (src or "").strip()
    if not src:
        return None
    m = LIQUID_SRC.search(src)
    if m:
        rel = m.group("path").lstrip("/")
        p = ROOT / rel
        return p if p.exists() else None
    if src.startswith("/"):
        p = ROOT / src.lstrip("/")
        return p if p.exists() else None
    p = (article.parent / src).resolve()
    try:
        p.relative_to(ROOT)
    except ValueError:
        return None
    return p if p.exists() else None


def affichage_dir_for(original: Path) -> Path:
    # .../images/foo.jpg -> .../images/affichage/
    if original.parent.name == "affichage":
        return original.parent
    return original.parent / "affichage"


def variant_name(original: Path, width: int, ext: str) -> str:
    return f"{original.stem}-{width}{ext}"


def make_variants(original: Path) -> dict:
    """Create 640/1200 WebP+JPEG (no upscale). Return manifest entry."""
    if BANNED.search(original.as_posix()):
        return {"skipped": "banned", "src": str(original)}

    out_dir = affichage_dir_for(original)
    out_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(original) as im:
        im = ImageOps.exif_transpose(im)
        src_w, src_h = im.size
        mode_src = im.mode
        # Work in RGB (JPEG) / keep alpha for intermediate
        has_alpha = mode_src in ("RGBA", "LA") or (
            mode_src == "P" and "transparency" in im.info
        )
        if has_alpha:
            rgba = im.convert("RGBA")
            background = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
            rgb = Image.alpha_composite(background, rgba).convert("RGB")
        else:
            rgb = im.convert("RGB")

    files = {}
    widths_made = []
    for tw in TARGET_WIDTHS:
        w = min(tw, src_w)
        if w in widths_made:
            continue
        # If 1200-target collapses to same as 640 (src_w <= 640), skip second
        h = max(1, round(src_h * (w / src_w)))
        resized = rgb.resize((w, h), Image.Resampling.LANCZOS)
        jpg_path = out_dir / variant_name(original, w, ".jpg")
        webp_path = out_dir / variant_name(original, w, ".webp")
        resized.save(
            jpg_path,
            "JPEG",
            quality=JPEG_QUALITY,
            optimize=True,
            progressive=True,
        )
        resized.save(
            webp_path,
            "WEBP",
            quality=WEBP_QUALITY,
            method=6,
        )
        files[w] = {
            "jpg": jpg_path,
            "webp": webp_path,
            "w": w,
            "h": h,
            "jpg_bytes": jpg_path.stat().st_size,
            "webp_bytes": webp_path.stat().st_size,
        }
        widths_made.append(w)

    largest = files[max(files)]
    return {
        "original": original,
        "orig_w": src_w,
        "orig_h": src_h,
        "orig_bytes": original.stat().st_size,
        "files": files,
        "display_w": largest["w"],
        "display_h": largest["h"],
    }


def to_url(original: Path, variant: Path, src_attr: str) -> str:
    """Build a URL in the same style as the original src attribute."""
    if LIQUID_SRC.search(src_attr):
        rel = "/" + variant.relative_to(ROOT).as_posix()
        return "{{ '" + rel + "' | relative_url }}"
    if src_attr.startswith("/"):
        return "/" + variant.relative_to(ROOT).as_posix()
    # relative to article (usually images/foo.jpg -> images/affichage/foo-1200.jpg)
    # Compute path relative to the original's parent of 'images'
    # Safer: relative from the same directory the original src was relative to.
    # If src is images/foo.jpg, variant is images/affichage/foo-1200.jpg
    orig_src = src_attr.split("?")[0]
    orig_name = Path(orig_src).name
    prefix = orig_src[: -len(orig_name)] if orig_src.endswith(orig_name) else ""
    # prefix is e.g. "images/"
    return f"{prefix}affichage/{variant.name}"


def srcset_for(info: dict, kind: str, src_attr: str) -> str:
    parts = []
    for w in sorted(info["files"]):
        f = info["files"][w]
        url = to_url(info["original"], f[kind], src_attr)
        parts.append(f"{url} {w}w")
    return ", ".join(parts)


def build_picture(
    info: dict,
    src_attr: str,
    alt: str,
    loading: str,
    fetchpriority: bool,
    sizes: str,
    extra_img_attrs: dict[str, str],
) -> str:
    webp_ss = srcset_for(info, "webp", src_attr)
    jpg_ss = srcset_for(info, "jpg", src_attr)
    largest = info["files"][max(info["files"])]
    jpg_src = to_url(info["original"], largest["jpg"], src_attr)
    w = info["display_w"]
    h = info["display_h"]

    img_bits = [
        f'src="{jpg_src}"',
        f'srcset="{jpg_ss}"',
        f'sizes="{sizes}"',
        f'alt="{alt}"',
        f'width="{w}"',
        f'height="{h}"',
        f'loading="{loading}"',
        'decoding="async"',
    ]
    if fetchpriority:
        img_bits.append('fetchpriority="high"')
    # preserve class/style/id if any
    for k in ("class", "style", "id"):
        if k in extra_img_attrs and extra_img_attrs[k]:
            img_bits.append(f'{k}="{extra_img_attrs[k]}"')

    source_ss = webp_ss
    return (
        "<picture>\n"
        f'  <source type="image/webp" srcset="{source_ss}" sizes="{sizes}">\n'
        f'  <img {" ".join(img_bits)}>\n'
        "</picture>"
    )


def should_skip_img(tag: str) -> bool:
    if SKIP_CLASS.search(tag):
        return True
    attrs = parse_attrs(tag)
    src = attrs.get("src", "")
    if BANNED.search(src):
        return True
    return False


def is_already_affichage(src: str) -> bool:
    return "/affichage/" in src or src.startswith("affichage/")


def cover_sizes(src: str, tag_context: str) -> str:
    if "cover" in src.lower() or "hero" in src.lower() or "bistrot-cover" in tag_context:
        return "(max-width: 42em) 100vw, 1200px"
    return "(max-width: 42em) 92vw, 800px"


def rewrite_article(article: Path, cache: dict) -> dict:
    text = article.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        fm, body = parts[1], parts[2]
        prefix = "---" + fm + "---"
    else:
        prefix, body = "", text

    stats = {
        "article": str(article.relative_to(ROOT)),
        "replaced": 0,
        "skipped": 0,
        "first": None,
        "bytes_orig": 0,
        "bytes_display_webp_1200": 0,
        "images": [],
    }

    first_done = {"v": False}

    # Replace <picture> blocks first, then remaining bare <img>
    def handle_picture(m: re.Match) -> str:
        block = m.group(0)
        img_m = IMG_RE.search(block)
        if not img_m:
            return block
        tag = img_m.group(0)
        if should_skip_img(tag):
            stats["skipped"] += 1
            return block
        return replace_img(tag, context=block, wrap_if_bare=False) or block

    def replace_img(tag: str, context: str, wrap_if_bare: bool) -> str | None:
        attrs = parse_attrs(tag)
        src = attrs.get("src", "")
        if should_skip_img(tag) or is_already_affichage(src):
            stats["skipped"] += 1
            return None
        original = resolve_src(src, article)
        if original is None:
            stats["skipped"] += 1
            return None
        if BANNED.search(original.as_posix()) or BANNED.search(original.name):
            stats["skipped"] += 1
            return None
        key = str(original)
        if key not in cache:
            cache[key] = make_variants(original)
        info = cache[key]
        if "skipped" in info:
            stats["skipped"] += 1
            return None

        is_first = not first_done["v"]
        first_done["v"] = True
        if is_first:
            stats["first"] = original.name
        loading = "eager" if is_first else "lazy"

        alt = attrs.get("alt", "")
        extra = {k: attrs[k] for k in ("class", "style", "id") if k in attrs}
        sizes = cover_sizes(src, context)
        picture = build_picture(
            info, src, alt, loading, is_first, sizes, extra
        )

        stats["replaced"] += 1
        if original not in [Path(i["original"]) for i in stats["images"]]:
            largest_w = max(info["files"])
            entry = {
                "original": original.name,
                "orig_bytes": info["orig_bytes"],
                "orig_wh": f"{info['orig_w']}x{info['orig_h']}",
                "variants": {
                    str(w): {
                        "jpg": f["jpg_bytes"],
                        "webp": f["webp_bytes"],
                        "wh": f"{f['w']}x{f['h']}",
                    }
                    for w, f in info["files"].items()
                },
            }
            stats["images"].append(entry)
            stats["bytes_orig"] += info["orig_bytes"]
            stats["bytes_display_webp_1200"] += info["files"][largest_w]["webp_bytes"]

        return picture

    def handle_img(m: re.Match) -> str:
        tag = m.group(0)
        # skip if this img is inside a picture we already rewrote? After picture
        # replace, remaining imgs should be bare. But this regex is on already
        # rewritten body — imgs inside new pictures would be rematched if we
        # run IMG_RE on the new body. We'll run pictures first, then bare imgs
        # with a skip if parent is picture. Here the function is applied via
        # a manual walk to avoid replacing inside pictures.
        return tag

    new_body = PICTURE_RE.sub(handle_picture, body)

    # Replace bare imgs not inside <picture>
    out = []
    pos = 0
    for m in IMG_RE.finditer(new_body):
        start, end = m.span()
        out.append(new_body[pos:start])
        # is this img inside a picture?
        before = new_body[:start]
        last_open = before.rfind("<picture")
        last_close = before.rfind("</picture>")
        if last_open > last_close:
            out.append(m.group(0))
        else:
            replaced = replace_img(m.group(0), new_body[max(0, start - 200):end + 20], True)
            out.append(replaced if replaced is not None else m.group(0))
        pos = end
    out.append(new_body[pos:])
    new_body = "".join(out)

    article.write_text(prefix + new_body, encoding="utf-8")
    return stats


def text_without_media(s: str) -> str:
    """Strip img/picture/source/a-around-images? Keep figcaptions and prose."""
    s = PICTURE_RE.sub("", s)
    s = IMG_RE.sub("", s)
    # drop empty <a ...></a> that only wrapped images? Don't strip all anchors
    # because some may have text. Only collapse whitespace differences later.
    return s


def main() -> int:
    cache: dict = {}
    reports = []
    for article in ARTICLES:
        raw = article.read_text(encoding="utf-8")
        body = raw.split("---", 2)[2] if raw.startswith("---") else raw
        if not IMG_RE.search(body):
            continue
        # skip if only card-thumbs? still run, skips those
        before_text = text_without_media(body)
        stats = rewrite_article(article, cache)
        after = article.read_text(encoding="utf-8")
        after_body = after.split("---", 2)[2] if after.startswith("---") else after
        after_text = text_without_media(after_body)
        if before_text != after_text:
            # Allow differences only in whitespace around removed tags
            def norm(t: str) -> str:
                t = re.sub(r"[ \t]+\n", "\n", t)
                t = re.sub(r"\n{3,}", "\n\n", t)
                return t
            if norm(before_text) != norm(after_text):
                print("WARNING: text changed in", article, file=sys.stderr)
                # show a small diff
                import difflib
                diff = list(difflib.unified_diff(
                    norm(before_text).splitlines(),
                    norm(after_text).splitlines(),
                    lineterm="",
                    n=1,
                ))
                print("\n".join(diff[:80]), file=sys.stderr)
        reports.append(stats)
        print(
            f"{stats['replaced']:3d} imgs  "
            f"{stats['bytes_orig']/1024:8.0f} KiB orig  "
            f"{stats['bytes_display_webp_1200']/1024:7.0f} KiB display  "
            f"{stats['article']}  first={stats['first']}"
        )

    # 64/66 safety
    for article in ARTICLES:
        t = article.read_text(encoding="utf-8")
        if BANNED.search(t):
            print("ERROR: banned 64/66 reference in", article, file=sys.stderr)
            return 2

    out = ROOT.parent / "visuels-seo" / "photos-affichage-rapport.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    # make json serializable
    serial = []
    for r in reports:
        serial.append({k: v for k, v in r.items() if k != "images"} | {"images": r["images"]})
    out.write_text(json.dumps(serial, indent=2, ensure_ascii=False), encoding="utf-8")
    print("rapport:", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
