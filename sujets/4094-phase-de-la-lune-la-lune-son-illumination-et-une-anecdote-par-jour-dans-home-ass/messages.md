---
title: "🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant"
description: "Après Saints du Jour et Jour Férié, voici une nouvelle petite intégration « culture et calendrier » pour Home Assistant : Phase de la Lune 🌙. Elle calcule…"
image: /sujets/4094-phase-de-la-lune-la-lune-son-illumination-et-une-anecdote-par-jour-dans-home-ass/images/og-partage.jpg
date: 2026-11-20
github_repo: phase_lune
pdf: /sujets/4094-phase-de-la-lune-la-lune-son-illumination-et-une-anecdote-par-jour-dans-home-ass/integration-phase_lune.pdf
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/4094-%F0%9F%8C%99-phase-de-la-lune-la-lune-son-illumination-et-une-anecdote-par-jour-dans-home-assistant/">Lire et commenter sur Forum Domotique</a> · <a href="https://github.com/XAV59213/phase_lune">Dépôt HACS : Phase de la Lune</a></p>


<section class="carousel photo-carousel" data-carousel data-lightbox aria-roledescription="carrousel" aria-label="Photos de l’article (4)" tabindex="0">
<div class="carousel-track" data-track>
<figure class="photo-slide" data-slide>
  <a href="images/card-preview.jpg" data-full="images/card-preview.jpg" data-alt="Photo 1 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant" aria-label="Agrandir la photo 1 : Photo 1 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant">
    <img src="images/card-preview.jpg" alt="Photo 1 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant" loading="eager">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/device-sensors.jpg" data-full="images/device-sensors.jpg" data-alt="Photo 2 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant" aria-label="Agrandir la photo 2 : Photo 2 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant">
    <img src="images/device-sensors.jpg" alt="Photo 2 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/config-country.jpg" data-full="images/config-country.jpg" data-alt="Photo 3 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant" aria-label="Agrandir la photo 3 : Photo 3 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant">
    <img src="images/config-country.jpg" alt="Photo 3 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/full_moon.png" data-full="images/full_moon.png" data-alt="Photo 4 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant" aria-label="Agrandir la photo 4 : Photo 4 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant">
    <img src="images/full_moon.png" alt="Photo 4 — 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant" loading="lazy">
  </a>
</figure>
</div>
<button type="button" class="carousel-nav" data-prev aria-label="Photo précédente">‹</button>
<button type="button" class="carousel-nav" data-next aria-label="Photo suivante">›</button>
<div class="carousel-dots" data-dots></div>
<div class="carousel-live" data-live aria-live="polite"></div>
<p class="carousel-hint">Faites défiler les photos, ou ouvrez-les pour les agrandir (si JavaScript est activé).</p>
</section>

# 🌙 Phase de la Lune – La lune, son illumination et une anecdote par jour dans Home Assistant

Bonjour à tous 👋

Après Saints du Jour et Jour Férié, voici une nouvelle petite intégration « culture et calendrier » pour Home Assistant : **Phase de la Lune** 🌙. Elle calcule chaque jour la phase de la lune, son pourcentage d’illumination, et l’accompagne d’un petit texte poétique et d’une **anecdote du jour**.

Elle fait déjà partie de la **bibliothèque officielle de HACS**. La version actuelle est la [**1.3.3**](https://github.com/XAV59213/phase_lune/releases/tag/1.3.3).

👉 **Le plus simple :** cliquez sur ce bouton. Un clic ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

![Ouvrir dans HACS](images/hacs_repository.svg)
<!-- source : https://my.home-assistant.io/badges/hacs_repository.svg -->

![La carte Phase de la Lune](images/card-preview.jpg)
<!-- source : https://raw.githubusercontent.com/XAV59213/phase_lune/main/docs/images/card-preview.jpg -->

### 🤔 À quoi ça sert, concrètement ?

Certains jardinent avec la lune, d’autres aiment simplement savoir si ce soir ce sera pleine lune pour sortir la tête dehors, et beaucoup trouvent juste qu’une jolie lune donne du cachet à une tablette murale. C’est un peu pour tout ce monde-là que j’ai écrit cette intégration.

Le calcul se fait **entièrement en local**, sans compte, sans API et sans connexion Internet. Il s’appuie sur les formules astronomiques de Jean Meeus, et je l’ai vérifié sur **249 instants officiels** de l’observatoire naval américain (USNO) : l’écart est d’environ deux minutes. Largement suffisant pour savoir quand sortir le télescope 😄

Une fois installée, l’intégration crée un appareil **Phase de la Lune** avec **4 capteurs** :

- 🌓 la **phase en français** (« Premier quartier », « Gibbeuse croissante »…)
- 🖼️ la **phase « image »**, qui sert à afficher la bonne illustration parmi les 8 fournies
- 💡 l’**illumination**, en pourcentage
- 📖 l’**anecdote du jour** : 365 anecdotes différentes, une pour chaque jour de l’année (science, exploration, mythologie, folklore…)

![Les capteurs créés](images/device-sensors.jpg)
<!-- source : https://raw.githubusercontent.com/XAV59213/phase_lune/main/docs/images/device-sensors.jpg -->

### 🌍 Et si on habite dans l’hémisphère sud ?

À l’installation, on choisit son **pays** (la France par défaut). La phase est la même partout sur Terre, mais vue de l’hémisphère sud, la lune est « à l’envers » : l’image est alors inversée automatiquement, croissant et décroissant échangés. Le pays peut être changé plus tard dans les options.

![Le choix du pays](images/config-country.jpg)
<!-- source : https://raw.githubusercontent.com/XAV59213/phase_lune/main/docs/images/config-country.jpg -->

### ✨ Les grandes étapes depuis la première version

L’intégration est jeune (1.0.0 fin octobre 2026), mais elle a déjà bien avancé :

- 🎨 **Une carte Lovelace livrée avec l’intégration**, avec éditeur visuel : grande image de la lune, phase, texte poétique et anecdote
- 🖼️ Les **8 images de phases sont incluses** : plus rien à copier dans le dossier `www`
- 📖 **365 anecdotes uniques**, en français et en anglais
- 🌍 Le **choix du pays** et la gestion de l’hémisphère sud
- 💡 Un capteur d’**illumination** et un capteur d’**anecdote** dédiés
- 🎯 Un calcul plus précis, vérifié sur les données USNO (1.3.2)
- ✅ L’entrée dans la **bibliothèque HACS par défaut**

### 🛠️ Installation pas à pas (bibliothèque officielle HACS)

*Pour ceux qui débutent : HACS, c’est un peu le « magasin d’applications » communautaire de Home Assistant. Il permet d’installer et de mettre à jour en quelques clics des intégrations qui ne sont pas fournies d’origine. S’il n’est pas encore installé chez vous, le guide officiel est ici :* [*https://hacs.xyz/docs/use/*](https://hacs.xyz/docs/use/)

L’intégration fait partie de la **bibliothèque HACS par défaut** : plus besoin d’ajouter un dépôt personnalisé.

**Le plus rapide :** un clic sur ce bouton ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

![Ouvrir dans HACS](images/hacs_repository.svg)
<!-- source : https://my.home-assistant.io/badges/hacs_repository.svg -->

**Ou à la main :**

1. Dans Home Assistant, ouvrez **HACS** dans le menu de gauche
2. Tapez **Phase de la Lune** dans la barre de recherche
3. Ouvrez la fiche, puis cliquez sur **Télécharger**
4. Redémarrez Home Assistant (**Paramètres > Système > bouton ⏻ en haut à droite > Redémarrer**)
5. Allez dans **Paramètres > Appareils et services > + Ajouter une intégration**, et cherchez **Phase de la Lune**

⚠️ Petite subtilité qui piège souvent au début : HACS ne fait que **télécharger les fichiers**. Ce sont les étapes 4 et 5 qui créent réellement l’intégration et ses entités. Si vous ne voyez qu’une entité `update.…` après l’installation, c’est normal : c’est HACS qui surveille les mises à jour, il reste juste l’étape 5.

L’assistant ne pose qu’une seule question : votre **pays** (France par défaut). Il faut Home Assistant **2024.12** ou plus récent.

Raccourci pour l’étape 5 : <https://my.home-assistant.io/redirect/config_flow_start/?domain=phase_lune>

### 🎨 Ajouter la carte

1. Ouvrez votre tableau de bord en mode **Modifier**
2. **Ajouter une carte**, puis cherchez **« Phase de la Lune »**
3. Réglez le titre, la langue (français ou anglais) et ce que vous voulez afficher

En YAML :

```plaintext
type: custom:phase-lune-card
title: Phase de la Lune
language: fr
show_illumination: true
show_anecdote: true
```

L’entité n’est pas obligatoire : la carte retrouve toute seule les capteurs de l’intégration.

### ⚠️ Bon à savoir

- Pleine lune, nouvelle lune et quartiers sont affichés dans une fenêtre d’environ une demi-journée autour de l’instant exact, comme l’intégration Lune officielle de Home Assistant
- Le calcul est prévu pour les années **1950 à 2050** environ
- Les illustrations des phases viennent du projet de **papo-o** (communauté Home Assistant), merci à lui

![Pleine lune](images/full_moon.png)
<!-- source : https://raw.githubusercontent.com/XAV59213/phase_lune/main/media/moon_phases/full_moon.png -->

### 🔗 Liens

- Dépôt GitHub : <https://github.com/XAV59213/phase_lune>
- Dernière version (1.3.3) : <https://github.com/XAV59213/phase_lune/releases/tag/1.3.3>
- Signaler un bug ou proposer une idée : <https://github.com/XAV59213/phase_lune/issues>

Vos retours, idées et remontées de bugs sont les bienvenus, ici ou sur GitHub 😉

Bonne domotique ! 🏠  
Xavier (XAV59213)
