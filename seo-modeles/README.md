# Modèles de vérification (Search Console et Bing)

Ces fichiers ne sont **pas publiés** sur le site (dossier exclu dans `_config.yml`).
Ils servent uniquement de modèle, le temps que Xavier récupère ses codes de vérification.

Voir aussi `/workspace/forum/visibilite-propositions.md` pour le mode d’emploi complet.

## Google Search Console — fichier HTML

1. Dans Search Console, ajouter la propriété `https://xav59213.github.io/forumdomotique/`.
2. Choisir la méthode « Fichier HTML ».
3. Google propose un fichier du type `googleXXXXXXXX.html`.
4. Copier ce fichier à la **racine** du dépôt (au même niveau que `_config.yml`), commiter et pousser sur `main`.
5. Attendre le déploiement de GitHub Pages, puis cliquer sur « Vérifier ».

Modèle : `google-site-verification.exemple.html`.

## Google Search Console — balise meta

Alternative : coller le code dans `_config.yml` :

```yaml
webmaster_verifications:
  google: "COLLEZ_ICI_LE_CODE_GOOGLE"
```

`jekyll-seo-tag` ajoutera alors la balise `<meta name="google-site-verification" …>` sur toutes les pages.

## Bing Webmaster

```yaml
webmaster_verifications:
  bing: "COLLEZ_ICI_LE_CODE_BING"
```
