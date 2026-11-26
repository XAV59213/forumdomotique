#!/usr/bin/env python3
"""Génère un PDF A4 téléchargeable pour chaque guide, test produit et
intégration de la vitrine Forum Domotique.

Usage :
    python scripts/generer-pdf.py
    python scripts/generer-pdf.py --list
    python scripts/generer-pdf.py --only slzb,4008
    python scripts/generer-pdf.py --no-front-matter

Le contenu vient uniquement des pages sources. Rien n'est inventé.
Les adresses IP privées et les adresses MAC sont masquées.
Les brouillons et les pages noindex / sitemap: false sont ignorés.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from html import unescape
from pathlib import Path

import markdown
import yaml
from bs4 import BeautifulSoup, Comment, NavigableString, Tag
from PIL import Image as PILImage
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent
TMP_ROOT = Path("/tmp/forumdomotique-pdf")
AUTHOR = "XAV59213"
SITE_PUBLIC = "https://xav59213.github.io/forumdomotique"
GITHUB_ORG = "https://github.com/XAV59213"

BLUE = HexColor("#155799")
GREEN = HexColor("#159957")
TEXT = HexColor("#1a1a1a")
MUTED = HexColor("#4a5560")
RULE = HexColor("#d5dde3")
QUOTE_BG = HexColor("#f3f7f5")
QUOTE_BAR = HexColor("#159957")
TABLE_HEAD = HexColor("#155799")
TABLE_ROW = HexColor("#f4f7fa")
LIGHT = HexColor("#e8eef3")
CODE_BG = HexColor("#f3f5f8")

PAGE_W, PAGE_H = A4
MARGIN = 18 * mm
CONTENT_W = PAGE_W - 2 * MARGIN

# Fichier déjà publié pour le guide 4008 : on conserve le nom.
KEEP_PDF_NAMES = {
    "sujets/4008-guide-utilisateur-freebox-homexa-de-linstallation-a-lutilisation-v28824/messages.md":
        "guide-freebox-homexa-v28824.pdf",
}

KICKER = {
    "guides": "FORUM DOMOTIQUE  ·  GUIDE",
    "tests": "FORUM DOMOTIQUE  ·  TEST PRODUIT",
    "integrations": "FORUM DOMOTIQUE  ·  INTÉGRATION",
}

IP_RE = re.compile(
    r"\b(?:"
    r"10\.(?:\d{1,3}\.){2}\d{1,3}|"
    r"192\.168\.\d{1,3}\.\d{1,3}|"
    r"172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}|"
    r"169\.254\.\d{1,3}\.\d{1,3}"
    r")\b"
)
MAC_RE = re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b")
TOKEN_RE = re.compile(
    r"\b(?:eyJ[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,})\b"
)

IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".tif", ".tiff", ".svg", ".ico"}


@dataclass
class MaskHit:
    kind: str
    original: str
    replacement: str
    context: str


@dataclass
class Article:
    kind: str  # guides | tests | integrations
    source: Path
    title: str
    fm: dict
    body: str
    pdf_path: Path
    pdf_url: str
    cover_src: Path | None = None
    forum_url: str | None = None
    repo_url: str | None = None
    product: str | None = None
    brand: str | None = None
    tags: list[str] = field(default_factory=list)
    description: str | None = None
    masks: list[MaskHit] = field(default_factory=list)
    missing_images: list[str] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)
    skipped: str | None = None


def repo_rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO).as_posix()
    except ValueError:
        return str(path)


def load_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        data = {}
    return data, parts[2]


def is_noindex(fm: dict, source: Path) -> str | None:
    rel = repo_rel(source)
    if "/brouillons/" in f"/{rel}" or rel.startswith("brouillons/"):
        return "brouillon"
    robots = str(fm.get("robots") or "").lower()
    if "noindex" in robots:
        return "noindex"
    if fm.get("sitemap") is False:
        return "sitemap: false"
    if fm.get("draft") is True:
        return "draft"
    return None


def mask_text(text: str, hits: list[MaskHit]) -> str:
    def ip_sub(m: re.Match) -> str:
        ip = m.group(0)
        parts = ip.split(".")
        repl = f"{parts[0]}.{parts[1]}.x.x"
        start = max(0, m.start() - 40)
        hits.append(MaskHit("IP", ip, repl, text[start:m.end() + 40].replace("\n", " ")))
        return repl

    def mac_sub(m: re.Match) -> str:
        orig = m.group(0)
        sep = ":" if ":" in orig else "-"
        repl = sep.join(["xx"] * 6)
        start = max(0, m.start() - 40)
        hits.append(MaskHit("MAC", orig, repl, text[start:m.end() + 40].replace("\n", " ")))
        return repl

    def tok_sub(m: re.Match) -> str:
        orig = m.group(0)
        repl = "[jeton masqué]"
        start = max(0, m.start() - 20)
        hits.append(MaskHit("TOKEN", orig[:8] + "…", repl, text[start:m.end() + 10].replace("\n", " ")))
        return repl

    text = IP_RE.sub(ip_sub, text)
    text = MAC_RE.sub(mac_sub, text)
    text = TOKEN_RE.sub(tok_sub, text)
    return text


def extract_forum_url(body: str, fm: dict) -> str | None:
    m = re.search(
        r'<p class="forum-cta">\s*<a href="([^"]+)"',
        body,
    )
    if m:
        return unescape(m.group(1))
    for key in ("forum_url", "canonical_url"):
        val = fm.get(key)
        if isinstance(val, str) and val.startswith("http"):
            return val
    return None


def find_cover(fm: dict, source: Path) -> Path | None:
    image = fm.get("image")
    candidates: list[Path] = []
    if isinstance(image, str) and image.strip():
        raw = image.strip()
        if raw.startswith("/"):
            candidates.append(REPO / raw.lstrip("/"))
        else:
            candidates.append(source.parent / raw)
            candidates.append(REPO / raw)
    img_dir = source.parent / "images"
    if img_dir.is_dir():
        for pat in ("*couverture*.*", "*cover*.*", "*entete*.*", "*og*.*", "og-partage.*"):
            candidates.extend(sorted(img_dir.glob(pat)))
    seen = set()
    for c in candidates:
        try:
            c = c.resolve()
        except OSError:
            continue
        if c in seen:
            continue
        seen.add(c)
        if c.is_file() and c.suffix.lower() in IMG_EXT:
            return c
    return None


def default_pdf_filename(kind: str, source: Path, repo_name: str | None) -> str:
    rel = repo_rel(source)
    if rel in KEEP_PDF_NAMES:
        return KEEP_PDF_NAMES[rel]
    if kind == "integrations" and repo_name:
        safe = re.sub(r"[^A-Za-z0-9._-]+", "-", repo_name).strip("-")
        return f"integration-{safe}.pdf"
    parent = source.parent.name
    if source.name == "messages.md":
        m = re.match(r"^(\d+)-", parent)
        if m:
            return f"sujet-{m.group(1)}.pdf"
    return f"{parent}.pdf"


def parse_integrations() -> list[dict]:
    path = REPO / "_data" / "integrations.yml"
    data = yaml.safe_load(path.read_text()) or []
    return [it for it in data if isinstance(it, dict) and it.get("page")]


def page_to_source(page: str) -> Path | None:
    raw = page.strip().lstrip("/")
    raw = re.sub(r"\.html?$", ".md", raw)
    candidate = REPO / raw
    if candidate.is_file():
        return candidate
    if raw.endswith(".md"):
        alt = REPO / raw[:-3] / "index.md"
        if alt.is_file():
            return alt
    return None


def guides_md_sujet_sources() -> list[Path]:
    text = (REPO / "guides.md").read_text()
    found: list[Path] = []
    seen = set()
    for m in re.finditer(r"/sujets/[^'\"\s)]+/messages\.html", text):
        src = page_to_source(m.group(0))
        if src and src not in seen:
            seen.add(src)
            found.append(src)
    return found


def build_article(kind: str, source: Path, repo_name: str | None = None) -> Article:
    raw = source.read_text(encoding="utf-8")
    fm, body = load_front_matter(raw)
    title = str(fm.get("title") or source.parent.name)
    title = title.strip().strip("*").strip()
    skip = is_noindex(fm, source)
    pdf_name = default_pdf_filename(kind, source, repo_name)
    # Keep an already declared pdf: path if it points inside the article folder.
    declared = fm.get("pdf")
    if isinstance(declared, str) and declared.strip().endswith(".pdf"):
        declared_path = REPO / declared.strip().lstrip("/")
        if declared_path.parent == source.parent or declared_path.exists() or source.parent.name in declared:
            pdf_path = declared_path if declared_path.suffix == ".pdf" else source.parent / pdf_name
        else:
            pdf_path = source.parent / pdf_name
        # If the declared file is in the same folder, honour the filename.
        if declared_path.parent.resolve() == source.parent.resolve():
            pdf_path = source.parent / declared_path.name
    else:
        pdf_path = source.parent / pdf_name
    pdf_url = "/" + repo_rel(pdf_path)
    hits: list[MaskHit] = []
    masked_body = mask_text(body, hits)
    masked_title = mask_text(title, hits)
    art = Article(
        kind=kind,
        source=source,
        title=masked_title,
        fm=fm,
        body=masked_body,
        pdf_path=pdf_path,
        pdf_url=pdf_url,
        cover_src=find_cover(fm, source),
        forum_url=extract_forum_url(body, fm),
        product=(str(fm["product"]) if fm.get("product") else None),
        brand=(str(fm["brand"]) if fm.get("brand") else None),
        tags=[str(t) for t in fm.get("tags") or [] if t],
        description=str(fm["description"]).strip() if fm.get("description") else None,
        masks=hits,
        skipped=skip,
    )
    gh = fm.get("github_repo") or repo_name
    if gh:
        if str(gh).startswith("http"):
            art.repo_url = str(gh)
        else:
            art.repo_url = f"{GITHUB_ORG}/{str(gh).strip().strip('/')}"
    return art


def discover() -> list[Article]:
    articles: list[Article] = []
    seen: set[Path] = set()

    def add(kind: str, source: Path, repo_name: str | None = None) -> None:
        source = source.resolve()
        if source in seen or not source.is_file():
            return
        seen.add(source)
        articles.append(build_article(kind, source, repo_name))

    for path in sorted((REPO / "contenus" / "guides").rglob("article.md")):
        add("guides", path)
    for path in sorted((REPO / "contenus" / "tests").rglob("article.md")):
        add("tests", path)
    for path in guides_md_sujet_sources():
        add("guides", path)
    for item in parse_integrations():
        src = page_to_source(str(item["page"]))
        if src:
            add("integrations", src, repo_name=str(item.get("repo") or "") or None)
        else:
            sys.stderr.write(f"Page d'intégration introuvable : {item.get('page')}\n")
    return articles


def upsert_front_matter(path: Path, key: str, value: str) -> bool:
    """Insert or update a single YAML key. Leaves the rest of the file untouched."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    pre, fm, rest = text.split("---", 2)
    # Do not rewrite the body; only the front-matter block.
    pattern = re.compile(rf"^{re.escape(key)}:\s*.+$", re.M)
    line = f"{key}: {value}"
    if pattern.search(fm):
        current = pattern.search(fm).group(0)
        if current == line:
            return False
        fm = pattern.sub(line, fm, count=1)
    else:
        fm = fm.rstrip() + "\n" + line + "\n"
    path.write_text("---" + fm + "---" + rest, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Fonts & typography
# ---------------------------------------------------------------------------

def _first_existing(paths: list[Path]) -> Path | None:
    for p in paths:
        if p.is_file():
            return p
    return None


def register_fonts() -> None:
    names = {
        "SSP": "SourceSansPro-Regular.ttf",
        "SSP-Bold": "SourceSansPro-Bold.ttf",
        "SSP-Semibold": "SourceSansPro-Semibold.ttf",
        "SSP-It": "SourceSansPro-It.ttf",
        "SSP-BoldIt": "SourceSansPro-BoldIt.ttf",
        "SSP-Light": "SourceSansPro-Light.ttf",
        "SSP-Black": "SourceSansPro-Black.ttf",
    }
    font_dirs = [
        SCRIPT_DIR / "fonts",
        Path("/usr/share/fonts/truetype/sand-box/custom/Source Sans Pro"),
    ]
    for name, fn in names.items():
        found = _first_existing([d / fn for d in font_dirs])
        if not found:
            raise SystemExit(f"Police introuvable : {fn}")
        pdfmetrics.registerFont(TTFont(name, str(found)))
    mono = _first_existing(
        [
            SCRIPT_DIR / "fonts" / "DejaVuSansMono.ttf",
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
        ]
    )
    if not mono:
        raise SystemExit("Police mono introuvable")
    pdfmetrics.registerFont(TTFont("Mono", str(mono)))
    pdfmetrics.registerFontFamily(
        "SSP", normal="SSP", bold="SSP-Bold", italic="SSP-It", boldItalic="SSP-BoldIt"
    )


def make_styles() -> dict[str, ParagraphStyle]:
    return {
        "cover_kicker": ParagraphStyle(
            "cover_kicker", fontName="SSP-Semibold", fontSize=9.5, leading=13,
            textColor=BLUE, alignment=TA_LEFT, spaceAfter=4 * mm,
        ),
        "cover_title": ParagraphStyle(
            "cover_title", fontName="SSP-Black", fontSize=22, leading=26.5,
            textColor=TEXT, alignment=TA_LEFT, spaceAfter=4 * mm,
        ),
        "cover_author": ParagraphStyle(
            "cover_author", fontName="SSP-Semibold", fontSize=13, leading=17,
            textColor=BLUE, spaceAfter=3 * mm,
        ),
        "cover_body": ParagraphStyle(
            "cover_body", fontName="SSP", fontSize=11, leading=16,
            textColor=TEXT, spaceAfter=2.5 * mm,
        ),
        "cover_muted": ParagraphStyle(
            "cover_muted", fontName="SSP", fontSize=10, leading=14.5,
            textColor=MUTED, spaceAfter=1.5 * mm,
        ),
        "toc_title": ParagraphStyle(
            "toc_title", fontName="SSP-Bold", fontSize=18, leading=22,
            textColor=BLUE, spaceBefore=0, spaceAfter=8 * mm,
        ),
        "h2": ParagraphStyle(
            "h2", fontName="SSP-Bold", fontSize=15.5, leading=20,
            textColor=BLUE, spaceBefore=3 * mm, spaceAfter=4 * mm, keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "h3", fontName="SSP-Semibold", fontSize=12.5, leading=16.5,
            textColor=HexColor("#123a66"), spaceBefore=3 * mm, spaceAfter=3 * mm, keepWithNext=True,
        ),
        "h4": ParagraphStyle(
            "h4", fontName="SSP-Semibold", fontSize=11, leading=15,
            textColor=HexColor("#123a66"), spaceBefore=2.5 * mm, spaceAfter=2 * mm, keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "body", fontName="SSP", fontSize=10.5, leading=15.2,
            textColor=TEXT, alignment=TA_JUSTIFY, spaceAfter=3 * mm,
        ),
        "body_left": ParagraphStyle(
            "body_left", fontName="SSP", fontSize=10.5, leading=15.2,
            textColor=TEXT, alignment=TA_LEFT, spaceAfter=3 * mm,
        ),
        "li": ParagraphStyle(
            "li", fontName="SSP", fontSize=10.5, leading=15,
            textColor=TEXT, leftIndent=0, spaceAfter=1.1 * mm,
        ),
        "caption": ParagraphStyle(
            "caption", fontName="SSP-It", fontSize=9, leading=12.5,
            textColor=MUTED, alignment=TA_CENTER, spaceBefore=1.5 * mm, spaceAfter=5 * mm,
        ),
        "quote": ParagraphStyle(
            "quote", fontName="SSP", fontSize=10, leading=14.5,
            textColor=TEXT, leftIndent=2 * mm, rightIndent=2 * mm,
        ),
        "th": ParagraphStyle(
            "th", fontName="SSP-Semibold", fontSize=9, leading=12.5, textColor=white,
        ),
        "td": ParagraphStyle(
            "td", fontName="SSP", fontSize=9, leading=12.5, textColor=TEXT,
        ),
        "code": ParagraphStyle(
            "code", fontName="Mono", fontSize=7.8, leading=10.6,
            textColor=TEXT, spaceAfter=0,
        ),
        "meta": ParagraphStyle(
            "meta", fontName="SSP", fontSize=10, leading=14,
            textColor=MUTED, spaceAfter=1 * mm,
        ),
        "toc_l0": ParagraphStyle(
            "toc_l0", fontName="SSP", fontSize=12, leading=20,
            textColor=TEXT, leftIndent=0, firstLineIndent=0,
        ),
        "toc_l1": ParagraphStyle(
            "toc_l1", fontName="SSP", fontSize=10.5, leading=16,
            textColor=MUTED, leftIndent=8 * mm, firstLineIndent=0,
        ),
    }


class NumberedHeading(Paragraph):
    def __init__(self, text, style, level, key):
        super().__init__(text, style)
        self._toc_level = level
        self._toc_text = Paragraph(text, style).getPlainText()
        self._toc_key = key


class ArticleDoc(BaseDocTemplate):
    def __init__(self, path: Path, article: Article, footer_label: str, **kw):
        super().__init__(
            str(path),
            pagesize=A4,
            title=article.title,
            author=AUTHOR,
            subject=f"{article.title} — Forum Domotique",
            creator=AUTHOR,
            lang="fr",
            **kw,
        )
        self._footer_label = footer_label
        frame = Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H - 2 * MARGIN, id="normal")
        self.addPageTemplates(
            [
                PageTemplate(id="cover", frames=frame, onPage=self._draw_cover_page),
                PageTemplate(id="body", frames=frame, onPage=self._draw_body_page),
            ]
        )

    def afterFlowable(self, flowable):
        if not isinstance(flowable, NumberedHeading):
            return
        text = flowable._toc_text
        if not text:
            return
        self.notify("TOCEntry", (flowable._toc_level, text, self.page, flowable._toc_key))
        self.canv.bookmarkPage(flowable._toc_key)
        try:
            self.canv.addOutlineEntry(text[:120], flowable._toc_key, level=flowable._toc_level, closed=0)
        except Exception:
            pass

    def _draw_cover_page(self, canv, doc):
        canv.saveState()
        canv.setFillColor(BLUE)
        canv.rect(0, PAGE_H - 4.5 * mm, PAGE_W, 4.5 * mm, fill=1, stroke=0)
        canv.setFillColor(GREEN)
        canv.rect(0, 0, PAGE_W, 4.5 * mm, fill=1, stroke=0)
        canv.restoreState()

    def _draw_body_page(self, canv, doc):
        canv.saveState()
        canv.setFillColor(BLUE)
        canv.rect(0, PAGE_H - 3.2 * mm, PAGE_W, 3.2 * mm, fill=1, stroke=0)
        canv.setFillColor(GREEN)
        canv.rect(0, 0, PAGE_W, 3.2 * mm, fill=1, stroke=0)
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.3)
        canv.line(MARGIN, 12 * mm, PAGE_W - MARGIN, 12 * mm)
        canv.setFont("SSP", 8)
        canv.setFillColor(MUTED)
        label = self._footer_label
        if len(label) > 78:
            label = label[:75] + "…"
        canv.drawString(MARGIN, 7 * mm, label)
        canv.drawRightString(PAGE_W - MARGIN, 7 * mm, str(doc.page))
        canv.restoreState()


# ---------------------------------------------------------------------------
# Inline / HTML helpers
# ---------------------------------------------------------------------------

def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def strip_unsupported(s: str) -> str:
    """Retire les emoji et symboles que Source Sans Pro ne sait pas dessiner."""
    out = []
    for ch in s:
        o = ord(ch)
        if o >= 0x1F300 or o in {0x200D, 0xFE0F}:
            continue
        cat = unicodedata.category(ch)
        if cat == "So" and o > 0xFF:
            continue
        out.append(ch)
    return "".join(out)


def slug_key(text: str, prefix: str) -> str:
    s = unicodedata.normalize("NFKD", text)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower() or "titre"
    return f"{prefix}-{s[:60]}"


def inner_xml(el: Tag) -> str:
    return "".join(str(c) for c in el.children)


def html_to_rl(html: str) -> str:
    """Convert a fragment of HTML to a ReportLab-safe paragraph string."""
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")

    def conv(node) -> str:
        if isinstance(node, NavigableString):
            return esc(strip_unsupported(str(node)))
        if not isinstance(node, Tag):
            return ""
        name = node.name.lower()
        if name in {"script", "style"}:
            return ""
        if name == "br":
            return "<br/>"
        if name in {"strong", "b"}:
            return f"<b>{''.join(conv(c) for c in node.children)}</b>"
        if name in {"em", "i"}:
            return f"<i>{''.join(conv(c) for c in node.children)}</i>"
        if name == "u":
            return f"<u>{''.join(conv(c) for c in node.children)}</u>"
        if name == "code":
            return (
                f'<font face="Mono" size="8.5" color="#155799">'
                f"{''.join(conv(c) for c in node.children)}</font>"
            )
        if name == "a":
            href = (node.get("href") or "").strip()
            label = "".join(conv(c) for c in node.children).strip()
            if not label:
                # Lien qui ne contient qu'une image : l'image est émise à part.
                return ""
            if href.startswith("mailto:"):
                return label
            if href and not href.startswith(("#", "javascript:")):
                return f'<link href="{esc(href)}" color="#155799"><u>{label}</u></link>'
            return label
        if name in {"p", "div", "span", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6",
                    "figcaption", "figure", "section", "article", "blockquote"}:
            return "".join(conv(c) for c in node.children)
        if name == "img":
            return ""
        return "".join(conv(c) for c in node.children)

    text = "".join(conv(c) for c in soup.contents)
    text = re.sub(r"(?:<br/>\s*){3,}", "<br/><br/>", text)
    text = re.sub(r"\s+", " ", text)
    # Restore intended line breaks that we just flattened? Keep <br/> already emitted
    text = text.replace(" <br/>", "<br/>").replace("<br/> ", "<br/>")
    return text.strip()


def plain(html: str) -> str:
    return BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)


# ---------------------------------------------------------------------------
# Body preprocessing
# ---------------------------------------------------------------------------

def preprocess_body(article: Article) -> str:
    body = article.body
    body = re.sub(r"\{%\s*raw\s*%\}", "", body)
    body = re.sub(r"\{%\s*endraw\s*%\}", "", body)
    body = re.sub(r"\{%\s*include product-meta\.html\s*%\}", '<div class="pdf-product-meta"></div>', body)
    body = re.sub(r"\{%.*?%\}", "", body, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    # Hide comments / don sections already stripped in the layout
    body = re.split(r'<section class="article-comments"', body, maxsplit=1)[0]
    body = re.split(r'<h2 id="commentaires-de-xav59213', body, maxsplit=1)[0]
    # Drop the forum CTA (links appear on the cover)
    body = re.sub(r'<p class="forum-cta">.*?</p>', "", body, flags=re.S)
    # If a top photo-carousel is followed by the same images inline, drop the carousel
    # so photos stay next to the text that describes them.
    def strip_redundant_carousel(m: re.Match) -> str:
        block = m.group(0)
        rest = body[m.end():]
        srcs = re.findall(r'(?:src|href)="(images/[^"]+)"', block)
        if srcs and any(src in rest for src in srcs):
            return ""
        return block

    body = re.sub(
        r'<section class="carousel[^"]*"[^>]*>.*?</section>',
        strip_redundant_carousel,
        body,
        flags=re.S,
    )
    # Image markdown liée, parfois écrite sur deux lignes : [![alt](img)\nlabel](url)
    body = re.sub(
        r"\[!\[([^\]]*)\]\(([^)]+)\)\s*\n+\s*([^\]]+)\]\(([^)]+)\)",
        r"[![\1](\2)](\4)\n[\3](\4)",
        body,
    )
    return body.strip()


def first_intro(html: str, title: str, description: str | None) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for p in soup.find_all("p"):
        if p.find("img"):
            continue
        text = p.get_text(" ", strip=True)
        if len(text) < 40:
            continue
        if text.rstrip(" *") == title.rstrip(" *"):
            continue
        return html_to_rl(inner_xml(p))
    if description:
        return esc(description)
    return ""


# ---------------------------------------------------------------------------
# Images
# ---------------------------------------------------------------------------

def resolve_image(src: str, article: Article) -> Path | None:
    if not src:
        return None
    src = unescape(src.split("?")[0].split("#")[0].strip())
    if src.startswith("data:"):
        return None
    if src.startswith(("http://", "https://")):
        # only local site paths we can map
        for prefix in (
            "https://xav59213.github.io/forumdomotique/",
            "http://xav59213.github.io/forumdomotique/",
        ):
            if src.startswith(prefix):
                src = "/" + src[len(prefix):]
                break
        else:
            return None
    if src.startswith("/"):
        cand = REPO / src.lstrip("/")
    else:
        cand = article.source.parent / src
    if cand.is_file() and cand.suffix.lower() in IMG_EXT:
        return cand
    return None


def rasterize_for_pil(src: Path, tmp: Path) -> Path:
    """Return a raster path Pillow can open (SVG via CairoSVG)."""
    suffix = src.suffix.lower()
    if suffix != ".svg":
        return src
    dest = tmp / (hashlib.sha1(str(src).encode()).hexdigest()[:16] + "-svg.png")
    if dest.exists() and dest.stat().st_mtime >= src.stat().st_mtime:
        return dest
    try:
        import cairosvg
    except ImportError as exc:
        raise RuntimeError("CairoSVG est requis pour rasteriser les SVG") from exc
    dest.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(url=str(src), write_to=str(dest), output_width=1200)
    return dest


def opt_image(src: Path, tmp: Path, max_side: int, quality: int) -> Path:
    key = hashlib.sha1(f"{src}:{max_side}:{quality}:{src.stat().st_mtime_ns}".encode()).hexdigest()[:16]
    dest = tmp / f"{key}.jpg"
    if dest.exists():
        return dest
    src = rasterize_for_pil(src, tmp)
    im = PILImage.open(src)
    if im.mode in {"RGBA", "LA", "P"}:
        bg = PILImage.new("RGB", im.size, (255, 255, 255))
        if im.mode == "P":
            im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[-1] if im.mode in {"RGBA", "LA"} else None)
        im = bg
    else:
        im = im.convert("RGB")
    w, h = im.size
    scale = min(1.0, max_side / max(w, h))
    if scale < 1.0:
        im = im.resize((int(w * scale), int(h * scale)), PILImage.Resampling.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, "JPEG", quality=quality, optimize=True, progressive=True, subsampling=0)
    return dest


def fitted_image(path: Path, max_w: float, max_h: float, src_orig: Path | None = None) -> Image:
    # Prefer the already-rasterized file; originals like SVG cannot be opened by Pillow.
    src = path
    if src_orig is not None and src_orig.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".tif", ".tiff", ".ico"}:
        src = src_orig
    with PILImage.open(src) as im:
        iw, ih = im.size
    if iw <= 0 or ih <= 0:
        raise ValueError("image vide")
    ratio = min(max_w / iw, max_h / ih)
    return Image(str(path), width=iw * ratio, height=ih * ratio, kind="proportional")


# ---------------------------------------------------------------------------
# Flowables
# ---------------------------------------------------------------------------

def quote_block(inner_html: str, styles) -> Table:
    inner = Paragraph(html_to_rl(inner_html) or "&nbsp;", styles["quote"])
    t = Table([[inner]], colWidths=[CONTENT_W - 4 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), QUOTE_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 6 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, QUOTE_BAR),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    t.spaceAfter = 4 * mm
    t.spaceBefore = 1 * mm
    return t


def simple_table(el: Tag, styles) -> Table | None:
    rows = el.find_all("tr")
    if not rows:
        return None
    data = []
    has_head = False
    for i, tr in enumerate(rows):
        cells = tr.find_all(["th", "td"])
        if not cells:
            continue
        if i == 0 and all(c.name == "th" for c in cells):
            has_head = True
            style = styles["th"]
        else:
            style = styles["td"]
        data.append([Paragraph(html_to_rl(inner_xml(c)) or "&nbsp;", style) for c in cells])
    if not data:
        return None
    ncols = max(len(r) for r in data)
    for r in data:
        while len(r) < ncols:
            r.append(Paragraph("&nbsp;", styles["td"]))
    col_w = CONTENT_W / ncols
    t = Table(data, colWidths=[col_w] * ncols, repeatRows=1 if has_head else 0)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 1.6 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.6 * mm),
        ("GRID", (0, 0), (-1, -1), 0.3, LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.6, BLUE),
        ("ROWBACKGROUNDS", (0, 1 if has_head else 0), (-1, -1), [white, TABLE_ROW]),
    ]
    if has_head:
        cmds.insert(0, ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEAD))
    t.setStyle(TableStyle(cmds))
    t.spaceBefore = 2 * mm
    t.spaceAfter = 5 * mm
    return t


def bullet_list(items_html: list[str], styles, numbered: bool = False):
    flow = []
    for it in items_html:
        txt = html_to_rl(it)
        if not txt:
            continue
        flow.append(ListItem(Paragraph(txt, styles["li"]), leftIndent=8))
    if not flow:
        return None
    if numbered:
        return ListFlowable(
            flow, bulletType="1", start="1", leftIndent=18,
            bulletFontName="SSP-Bold", bulletFontSize=10.5, bulletColor=BLUE,
            spaceBefore=1 * mm, spaceAfter=3.5 * mm,
        )
    return ListFlowable(
        flow, bulletType="bullet", start="•", leftIndent=16,
        bulletFontName="SSP", bulletFontSize=11, bulletColor=GREEN,
        spaceBefore=1 * mm, spaceAfter=3.5 * mm,
    )


def _code_table(html: str, styles, *, first: bool, last: bool) -> Table:
    inner = Paragraph(html, styles["code"])
    t = Table([[inner]], colWidths=[CONTENT_W])
    # A split block keeps a continuous look: no double gap, lighter edges mid-block.
    top = 2.5 * mm if first else 1 * mm
    bottom = 2.5 * mm if last else 1 * mm
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), top),
        ("BOTTOMPADDING", (0, 0), (-1, -1), bottom),
        ("BOX", (0, 0), (-1, -1), 0.4, LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    t.spaceBefore = 1.5 * mm if first else 0
    t.spaceAfter = 4 * mm if last else 0
    return t


def code_block(text: str, styles) -> list[Table]:
    """Rendu d'un bloc de code, découpé si plus haut qu'une page."""
    cleaned = text.replace("\t", "    ").rstrip() + "\n"
    lines = cleaned.split("\n")
    leading = styles["code"].leading or 10.6
    padding = 5 * mm
    # Le cadre de page fait un peu moins que PAGE_H - 2*MARGIN ; on garde une marge.
    max_h = PAGE_H - 2 * MARGIN - 18 * mm
    max_lines = max(8, int((max_h - padding) / leading) - 1)
    chunks: list[str] = []
    current: list[str] = []
    for line in lines:
        if len(current) >= max_lines:
            chunks.append("\n".join(current) + "\n")
            current = []
        current.append(line)
    if current:
        chunks.append("\n".join(current) + "\n")
    tables = []
    n = len(chunks)
    for i, chunk in enumerate(chunks):
        html = esc(chunk).replace("\n", "<br/>")
        tables.append(_code_table(html, styles, first=(i == 0), last=(i == n - 1)))
    return tables


def product_meta_block(article: Article, styles):
    bits = []
    if article.product:
        bits.append(f"<b>Produit</b>  {esc(article.product)}")
    if article.brand:
        bits.append(f"<b>Marque</b>  {esc(article.brand)}")
    if article.tags:
        bits.append(f"<b>Catégories</b>  {esc(', '.join(article.tags))}")
    shop_parts = []
    shop_heading = str(article.fm.get("shop_heading") or "Voir sur la boutique").strip()
    raw_links = article.fm.get("shop_links") or []
    if isinstance(raw_links, list):
        for link in raw_links:
            if not isinstance(link, dict):
                continue
            label = str(link.get("label") or "").strip()
            url = str(link.get("url") or "").strip()
            if label and url:
                shop_parts.append(
                    f'<link href="{esc(url)}" color="#0d5c38"><u>{esc(label)}</u></link>'
                )
    if not bits and not shop_parts:
        return None
    rows = []
    if bits:
        rows.append([Paragraph("    ·    ".join(bits), styles["meta"])])
    if shop_parts:
        rows.append([
            Paragraph(
                f"<b>{esc(shop_heading)}</b><br/>" + "    ·    ".join(shop_parts),
                styles["meta"],
            )
        ])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#f6faf7")),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("BOX", (0, 0), (-1, -1), 0.3, HexColor("#dce8e0")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    t.spaceAfter = 5 * mm
    return t


class ConvertContext:
    def __init__(self, article: Article, styles, tmp: Path, quality: int, max_side: int):
        self.article = article
        self.styles = styles
        self.tmp = tmp
        self.quality = quality
        self.max_side = max_side
        self.heading_keys: set[str] = set()
        self.heading_index = 0
        self.seen_images: set[Path] = set()
        self.headings: list[tuple[int, str]] = []

    def heading_key(self, text: str) -> str:
        self.heading_index += 1
        base = slug_key(text, f"h{self.heading_index}")
        key = base
        n = 2
        while key in self.heading_keys:
            key = f"{base}-{n}"
            n += 1
        self.heading_keys.add(key)
        return key

    def figure(self, src: str, caption: str | None):
        path = resolve_image(src, self.article)
        if path is None:
            # Favicons and remote-only badges: not treated as content images.
            name = (src or "").rsplit("/", 1)[-1].lower()
            if name.startswith("favicon."):
                return []
            self.article.missing_images.append(src)
            return []
        path = path.resolve()
        # Skip the cover if it is repeated as the first body image
        if self.article.cover_src and path == self.article.cover_src.resolve() and not self.seen_images:
            self.seen_images.add(path)
            return []
        if path in self.seen_images:
            return []
        self.seen_images.add(path)
        try:
            opt = opt_image(path, self.tmp, self.max_side, self.quality)
            max_h = 110 * mm
            lname = path.name.lower()
            if any(tok in lname for tok in ("logo", "hacs_repository", "favicon", "badge")):
                max_h = 18 * mm
            img = fitted_image(opt, CONTENT_W, max_h, src_orig=path)
        except Exception as exc:
            self.article.issues.append(f"image illisible ({src}): {exc}")
            return []
        img.hAlign = "CENTER"
        items = [img]
        cap = (caption or "").strip()
        if cap:
            # Skip generic "Photo N — Title" carousel captions; keep meaningful alts
            if re.match(r"^Photo\s+\d+\s+[—–-]", cap) and self.article.title[:40] in cap:
                cap = ""
            elif cap.lower().startswith("couverture"):
                cap = ""
            elif re.search(r"\.(jpe?g|png|webp|gif|svg)$", cap, re.I) or cap == path.name:
                cap = ""
        if cap:
            items.append(Paragraph(esc(cap), self.styles["caption"]))
        else:
            img.spaceAfter = 5 * mm
        return [KeepTogether(items)]


def convert_element(el, ctx: ConvertContext):
    styles = ctx.styles
    if isinstance(el, Comment):
        return
    if isinstance(el, NavigableString):
        text = str(el).strip()
        if text:
            yield Paragraph(esc(text), styles["body"])
        return
    if not isinstance(el, Tag):
        return
    name = el.name.lower()
    classes = " ".join(el.get("class") or [])

    if name in {"script", "style", "noscript", "svg", "iframe", "video", "audio"}:
        # Keep a clickable source URL when one exists (do not invent a capture).
        src = el.get("src") or el.get("href")
        if src and str(src).startswith("http"):
            yield Paragraph(
                f'Support : <link href="{esc(src)}" color="#155799"><u>{esc(src)}</u></link>',
                styles["cover_muted"],
            )
        return
    if name == "hr":
        yield HRFlowable(width="100%", thickness=0.5, color=RULE, spaceBefore=2 * mm, spaceAfter=3 * mm)
        return
    if name == "br":
        yield Spacer(1, 1.5 * mm)
        return
    if name in {"h1", "h2", "h3", "h4"}:
        text = html_to_rl(inner_xml(el))
        plain_t = plain(inner_xml(el))
        if not plain_t:
            return
        # Skip a leading title that repeats the cover title
        if name == "h1" and plain_t.strip(" *") == ctx.article.title.strip(" *"):
            return
        level = {"h1": 0, "h2": 0, "h3": 1, "h4": 1}[name]
        style = {"h1": styles["h2"], "h2": styles["h2"], "h3": styles["h3"], "h4": styles["h4"]}[name]
        key = ctx.heading_key(plain_t)
        ctx.headings.append((level, plain_t))
        yield NumberedHeading(text, style, level, key)
        return
    if name == "pre":
        code = el.get_text()
        yield from code_block(code, styles)
        return
    if name == "blockquote":
        yield quote_block(inner_xml(el), styles)
        return
    if name == "table":
        t = simple_table(el, styles)
        if t:
            yield t
        return
    if name in {"ul", "ol"}:
        # Nested lists: flatten one level of li text (nested ul kept as inner HTML)
        items = []
        for li in el.find_all("li", recursive=False):
            items.append(inner_xml(li))
        fl = bullet_list(items, styles, numbered=(name == "ol"))
        if fl:
            yield fl
        return
    if name == "img":
        cap = el.get("alt") or ""
        yield from ctx.figure(el.get("src") or "", cap)
        return
    if name == "figure":
        img = el.find("img")
        cap_el = el.find("figcaption")
        cap = cap_el.get_text(" ", strip=True) if cap_el else (img.get("alt") if img else "")
        if img:
            yield from ctx.figure(img.get("src") or "", cap)
        # Any leftover text
        return
    if name == "p":
        imgs = el.find_all("img")
        text = html_to_rl(inner_xml(el))
        # Image-only paragraph
        if imgs and not plain(inner_xml(el)):
            for img in imgs:
                yield from ctx.figure(img.get("src") or "", img.get("alt") or "")
            return
        if text:
            yield Paragraph(text, styles["body"])
        for img in imgs:
            yield from ctx.figure(img.get("src") or "", img.get("alt") or "")
        return
    if name in {"div", "section", "article", "main", "aside", "span", "center"}:
        if "PRODUCT_META" in (el.string or "") or (el.get("id") == "product-meta"):
            return
        for child in el.children:
            yield from convert_element(child, ctx)
        return
    # Fallback: recurse
    if el.contents:
        for child in el.children:
            yield from convert_element(child, ctx)


def body_to_html(markdown_text: str) -> str:
    return markdown.markdown(
        markdown_text,
        extensions=["extra", "sane_lists", "smarty"],
        output_format="html",
    )


# ---------------------------------------------------------------------------
# Build one PDF
# ---------------------------------------------------------------------------

def footer_label(article: Article) -> str:
    short = article.title
    if len(short) > 55:
        short = short[:52].rstrip() + "…"
    return f"XAV59213  ·  {short}"


def cover_flowables(article: Article, styles, ctx: ConvertContext, intro: str):
    story = []
    if article.cover_src and article.cover_src.is_file():
        try:
            opt = opt_image(article.cover_src, ctx.tmp, max_side=1600, quality=max(ctx.quality, 80))
            banner = fitted_image(opt, CONTENT_W, 108 * mm, src_orig=article.cover_src)
            banner.hAlign = "CENTER"
            story.append(banner)
            story.append(Spacer(1, 6 * mm))
            ctx.seen_images.add(article.cover_src.resolve())
        except Exception as exc:
            article.issues.append(f"couverture illisible : {exc}")
    story.append(Paragraph(KICKER.get(article.kind, "FORUM DOMOTIQUE"), styles["cover_kicker"]))
    story.append(Paragraph(esc(article.title), styles["cover_title"]))
    story.append(Paragraph("Auteur&nbsp;: XAV59213", styles["cover_author"]))
    if intro:
        story.append(Paragraph(intro, styles["cover_body"]))
    # Keep an existing independence mention on the cover when the article has one.
    plain_body = re.sub(r"<[^>]+>", " ", article.body)
    plain_body = re.sub(r"[*_`]+", "", plain_body)
    m = re.search(r"Projet indépendant[^\n<.]*(?:\.|$)", plain_body, re.I)
    if m:
        sentence = re.sub(r"\s+", " ", m.group(0)).strip()
        if sentence and sentence.lower() not in (intro or "").lower():
            story.append(Paragraph(f"<b>{esc(sentence)}</b>", styles["cover_body"]))
    story.append(Spacer(1, 2 * mm))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4 * mm))
    if article.repo_url:
        label = article.repo_url.replace("https://", "").replace("http://", "")
        story.append(Paragraph(
            f'Dépôt : <link href="{esc(article.repo_url)}" color="#155799"><u>{esc(label)}</u></link>',
            styles["cover_muted"],
        ))
    if article.forum_url:
        story.append(Paragraph(
            f'Sujet sur Forum Domotique : <link href="{esc(article.forum_url)}" color="#155799"><u>Lire et commenter</u></link>',
            styles["cover_muted"],
        ))
    page_url = SITE_PUBLIC + "/" + repo_rel(article.source.parent) + "/"
    story.append(Paragraph(
        f'Page de la vitrine : <link href="{esc(page_url)}" color="#155799"><u>{esc(page_url)}</u></link>',
        styles["cover_muted"],
    ))
    return story


def build_pdf(article: Article, quality: int = 78, max_side: int = 1400) -> Path:
    styles = make_styles()
    tmp = TMP_ROOT / hashlib.sha1(repo_rel(article.source).encode()).hexdigest()[:12]
    tmp.mkdir(parents=True, exist_ok=True)
    ctx = ConvertContext(article, styles, tmp, quality=quality, max_side=max_side)

    prepared = preprocess_body(article)
    html = body_to_html(prepared)
    # Product meta marker
    soup = BeautifulSoup(html, "html.parser")
    intro = first_intro(html, article.title, article.description)

    doc = ArticleDoc(article.pdf_path, article, footer_label(article))
    story = []
    story.append(NextPageTemplate("cover"))
    story.extend(cover_flowables(article, styles, ctx, intro))

    body_story = []
    meta = product_meta_block(article, styles)
    # If the article used the product-meta include, honour it at the start of the body
    if ('class="pdf-product-meta"' in prepared or "pdf-product-meta" in prepared) and meta:
        body_story.append(meta)

    # Walk top-level elements
    # markdown wraps nothing; soup may have a list of tags
    roots = list(soup.contents)
    for el in roots:
        if isinstance(el, NavigableString) and not str(el).strip():
            continue
        body_story.extend(list(convert_element(el, ctx)))

    if ctx.headings:
        story.append(NextPageTemplate("body"))
        story.append(PageBreak())
        story.append(Paragraph("Sommaire", styles["toc_title"]))
        toc = TableOfContents()
        toc.levelStyles = [styles["toc_l0"], styles["toc_l1"]]
        story.append(toc)
        story.append(PageBreak())
    else:
        story.append(NextPageTemplate("body"))
        story.append(PageBreak())

    story.extend(body_story)

    article.pdf_path.parent.mkdir(parents=True, exist_ok=True)
    # Two-pass build for TOC page numbers when needed
    if ctx.headings:
        doc.multiBuild(story)
    else:
        doc.build(story)
    return article.pdf_path


def shrink_if_needed(article: Article, max_bytes: int = 5 * 1024 * 1024) -> None:
    path = article.pdf_path
    if not path.is_file():
        return
    size = path.stat().st_size
    if size <= max_bytes:
        return
    # Retry with lighter images
    for quality, side in ((68, 1200), (60, 1000), (52, 900)):
        article.issues.append(
            f"PDF au-dessus de 5 Mo ({size / 1e6:.2f} Mo) : nouvelle passe qualité={quality}, côté={side}"
        )
        # reset per-image bookkeeping for a clean rebuild
        build_pdf(article, quality=quality, max_side=side)
        size = path.stat().st_size
        if size <= max_bytes:
            return
    article.issues.append(f"PDF encore au-dessus de 5 Mo après compression ({size / 1e6:.2f} Mo)")


def matched(article: Article, needles: list[str]) -> bool:
    if not needles:
        return True
    blob = " ".join([
        repo_rel(article.source),
        article.title,
        article.pdf_path.name,
        article.kind,
        (article.fm.get("github_repo") or ""),
    ]).lower()
    return any(n.lower() in blob for n in needles)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Génère les PDF de la vitrine Forum Domotique.")
    parser.add_argument("--list", action="store_true", help="Lister les articles sans générer")
    parser.add_argument("--only", default="", help="Filtrer (sous-chaînes séparées par des virgules)")
    parser.add_argument("--no-front-matter", action="store_true", help="Ne pas écrire la clé pdf: dans le front matter")
    parser.add_argument("--repo", type=Path, default=None, help="Racine du dépôt (défaut : parent du script)")
    args = parser.parse_args(argv)

    global REPO
    if args.repo:
        REPO = args.repo.resolve()

    needles = [s.strip() for s in args.only.split(",") if s.strip()]
    articles = [a for a in discover() if matched(a, needles)]

    if args.list:
        for a in articles:
            flag = f"  [SKIP {a.skipped}]" if a.skipped else ""
            print(f"{a.kind:13} {repo_rel(a.source)} -> {repo_rel(a.pdf_path)}{flag}")
        print(f"{len(articles)} article(s)")
        return 0

    register_fonts()
    generated = []
    skipped = []
    for a in articles:
        if a.skipped:
            skipped.append(a)
            print(f"SKIP {a.kind:13} {repo_rel(a.source)} ({a.skipped})")
            continue
        print(f"PDF  {a.kind:13} {repo_rel(a.source)} -> {a.pdf_path.name} …", flush=True)
        try:
            build_pdf(a)
            shrink_if_needed(a)
        except Exception as exc:
            a.issues.append(f"échec de génération : {exc}")
            print(f"  ERREUR : {exc}")
            skipped.append(a)
            continue
        size = a.pdf_path.stat().st_size if a.pdf_path.is_file() else 0
        print(f"  OK  {size / 1e6:.2f} Mo")
        if not args.no_front_matter:
            upsert_front_matter(a.source, "pdf", a.pdf_url)
        generated.append(a)

    # Summary
    print("\n===== Rapport =====")
    by = {}
    total = 0
    for a in generated:
        by.setdefault(a.kind, []).append(a)
        total += a.pdf_path.stat().st_size if a.pdf_path.is_file() else 0
    for kind in ("guides", "tests", "integrations"):
        items = by.get(kind, [])
        sub = sum(i.pdf_path.stat().st_size for i in items)
        print(f"{kind:13} {len(items)} PDF  {sub / 1e6:.2f} Mo")
    print(f"{'total':13} {len(generated)} PDF  {total / 1e6:.2f} Mo")
    print(f"ignorés       {len(skipped)}")
    for a in generated + skipped:
        if a.masks:
            uniq = []
            seen = set()
            for h in a.masks:
                if (h.kind, h.original) in seen:
                    continue
                seen.add((h.kind, h.original))
                uniq.append(h)
            print(f"  masqué dans {repo_rel(a.source)} :")
            for h in uniq:
                print(f"    {h.kind} {h.original} → {h.replacement}  ({h.context[:80]})")
        if a.missing_images:
            print(f"  images manquantes ({repo_rel(a.source)}) :")
            for s in dict.fromkeys(a.missing_images):
                print(f"    {s}")
        if a.issues:
            print(f"  problèmes ({repo_rel(a.source)}) :")
            for s in a.issues:
                print(f"    {s}")
    return 0 if generated or args.list else 1


if __name__ == "__main__":
    sys.exit(main())
