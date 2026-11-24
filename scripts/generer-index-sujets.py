#!/usr/bin/env python3
"""Crée un index.md de redirection dans chaque dossier sujets/<slug>/.

L'URL courte /sujets/<slug>/ répond ainsi 200 et envoie vers messages.html,
sans dupliquer le texte du sujet et sans l'inscrire dans le sitemap.

Usage :
    python scripts/generer-index-sujets.py
    python scripts/generer-index-sujets.py --check
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SUJETS = ROOT / "sujets"

HEADER_COMMENT = (
    "# Redirection de l'URL du dossier vers messages.html.\n"
    "# Généré par scripts/generer-index-sujets.py — ne pas y copier le texte du sujet.\n"
)


def read_title(messages_md: Path) -> str:
    text = messages_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return messages_md.parent.name
    end = text.find("\n---", 3)
    if end == -1:
        return messages_md.parent.name
    fm = yaml.safe_load(text[3:end]) or {}
    title = fm.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    return messages_md.parent.name


def yaml_scalar(value) -> str:
    # Dump via un dict pour éviter le marqueur de fin de document « ... »
    # que PyYAML ajoute après un scalaire nu, ce qui casserait le front matter.
    dumped = yaml.safe_dump(
        {"v": value},
        allow_unicode=True,
        default_flow_style=False,
        width=10**9,
        sort_keys=False,
    )
    if not dumped.startswith("v:"):
        raise ValueError(f"Échec de sérialisation YAML : {dumped!r}")
    return dumped[len("v:"):].strip()


def render_index(slug: str, title: str) -> str:
    return (
        "---\n"
        f"{HEADER_COMMENT}"
        "layout: redirect\n"
        f"title: {yaml_scalar(title)}\n"
        f"redirect_to: /sujets/{slug}/messages.html\n"
        "sitemap: false\n"
        "robots: noindex, follow\n"
        "---\n"
    )


def iter_subjects() -> list[Path]:
    if not SUJETS.is_dir():
        return []
    found = []
    for folder in sorted(SUJETS.iterdir()):
        if folder.is_dir() and (folder / "messages.md").is_file():
            found.append(folder)
    return found


def sync(check_only: bool = False) -> int:
    written = 0
    unchanged = 0
    for folder in iter_subjects():
        slug = folder.name
        content = render_index(slug, read_title(folder / "messages.md"))
        dest = folder / "index.md"
        current = dest.read_text(encoding="utf-8") if dest.is_file() else None
        if current == content:
            unchanged += 1
            continue
        written += 1
        if not check_only:
            dest.write_text(content, encoding="utf-8")
    total = written + unchanged
    action = "à mettre à jour" if check_only else "écrits ou mis à jour"
    print(f"{total} sujets : {written} {action}, {unchanged} déjà à jour.")
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Ne rien écrire : quitte avec le code 1 s'il manque des index ou s'ils diffèrent.",
    )
    args = parser.parse_args()
    changed = sync(check_only=args.check)
    if args.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
