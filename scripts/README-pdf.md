# Génération des PDF de la vitrine

Script : `scripts/generer-pdf.py`

Il produit un PDF A4 (couverture, sommaire cliquable s’il y a des titres,
auteur XAV59213, liens vers le sujet du forum et le dépôt) pour :

- chaque article `section: guides` et `section: tests` ;
- les guides du forum listés dans `guides.md` (sauf pages `noindex` /
  `sitemap: false`, par exemple le sujet 618, doublon du guide SMB) ;
- chaque intégration de `_data/integrations.yml`, à partir de sa page
  `page:`.

Les brouillons et le contenu `noindex` sont ignorés. Les adresses IP
privées et les adresses MAC sont masquées dans le PDF.

## Lancer en local

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements-pdf.txt
.venv/bin/python scripts/generer-pdf.py
```

Options utiles : `--list`, `--only slzb,4008`, `--no-front-matter`.

Le script écrit le fichier PDF à côté de l’article et ajoute (ou met à
jour) la clé de front matter `pdf:`. Le corps des posts archivés n’est
pas modifié.

Le bouton « Télécharger en PDF » est ajouté par `_includes/pdf-download.html`
dans le layout, juste au-dessus du bandeau « Lire et commenter ». S’il
existe déjà un lien vers le même fichier dans le texte (guide 4008), le
bouton n’est pas doublé.

## GitHub Action

Le flux `.github/workflows/generer-pdf.yml` peut être lancé à la main
(`workflow_dispatch`) et se déclenche aussi quand un article ou le
script change. Il commet les PDF avec le marqueur `[pdf]` pour éviter
une boucle.
