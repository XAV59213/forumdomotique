---
layout: ha-dev
title: 'Bêta Home Assistant 2026.3 : les aspirateurs par pièce rodés en direct, et le mode de récupération apprend à restaurer'
short_title: 'Bêta 2026.3 : aspirateurs par pièce et mode de récupération'
description: 'La bêta de Home Assistant 2026.3 (25 février – 4 mars 2026) en français : nettoyage par pièce, Python 3.14, correctifs des cinq bêtas, mode de récupération.'
excerpt_fr: 'La bêta 2026.3 met à l’épreuve le nettoyage par pièce des aspirateurs, « Continuer en cas d’erreur » et Python 3.14. Pendant la bêta : la réparation des aspirateurs est revue, et le mode de récupération gagne les sauvegardes.'
image: /actualite-ha-dev/home-assistant-2026-3-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.3, mars 2026'
date: 2026-02-25
section: actualite-ha-dev
cycle: 2026-3
version: '2026.3'
month: Mars 2026
release_url: https://www.home-assistant.io/blog/2026/03/04/release-20263/
official_title: '2026.3: A clean sweep'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.3/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.3'
seo:
  type: NewsArticle
---
La bêta **2026.3.0b0** a été publiée le **25 février 2026**, et la version stable est sortie le **4 mars**, après cinq bêtas. C’est un cycle très « robot aspirateur » : le **nettoyage par pièce** a été ajusté d’une bêta à l’autre. Un autre changement, plus discret, compte beaucoup pour les testeurs : le **mode de récupération** en cas de retour à une version antérieure.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : nettoyage par pièce pour les aspirateurs, « Continue on error » dans l’éditeur visuel, mot d’activation local sur Android, badges et onglets du tableau Énergie, Python 3.14.
- 🔁 **Pendant la bêta** : la réparation des aspirateurs est retirée puis remplacée par une erreur explicite (b2), Overseerr devient Seerr, mode de récupération en cas de retour arrière des registres (b3).
- ⚠️ **À vérifier** : BSB-Lan, image Container, LIFX, lumières, Satel Integra, Snapcast, StarLine, Tado, Template et Z-Wave.
</div>

## 🧪 Ce qui était en test

- Le **nettoyage par pièce** pour les robots aspirateurs, avec les pièces de Home Assistant.
- L’option **Continue on error** enfin disponible dans l’éditeur visuel.
- Un **mot d’activation local** dans l’application Android (expérimental).
- Le tableau **Énergie** : badges en temps réel, diagramme Sankey pour l’eau, onglets Électricité, Gaz et Eau.
- Home Assistant passe à **Python 3.14**.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (26 février).** Matter corrige le contrôle d’état du nettoyage par zone [#164108](https://github.com/home-assistant/core/pull/164108). Le mot « add-ons » est remplacé par « apps » dans les messages de sauvegarde [#164129](https://github.com/home-assistant/core/pull/164129), et « Z-Wave Supervisor app » devient « Z-Wave JS app » [#164147](https://github.com/home-assistant/core/pull/164147). Portainer ne mélange plus les piles (*stacks*) et les conteneurs [#164135](https://github.com/home-assistant/core/pull/164135).

**b2 (2 mars, 38 changements).** La réparation « correspondance des pièces non configurée » des aspirateurs est **retirée** [#164259](https://github.com/home-assistant/core/pull/164259). Elle est remplacée par une **erreur levée** quand cette correspondance manque [#164595](https://github.com/home-assistant/core/pull/164595). Matter évite un plantage sur des informations de zone nulles [#164411](https://github.com/home-assistant/core/pull/164411). **Overseerr devient Seerr** [#164060](https://github.com/home-assistant/core/pull/164060). Les entités de mise à jour ZHA refonctionnent après un rechargement [#164290](https://github.com/home-assistant/core/pull/164290). Le stockage SFTP refuse les chemins relatifs [#164408](https://github.com/home-assistant/core/pull/164408), et Satel Integra exige un code utilisateur pour basculer ses interrupteurs [#164483](https://github.com/home-assistant/core/pull/164483). Les sauvegardes WebDAV volumineuses sont également corrigées [#164563](https://github.com/home-assistant/core/pull/164563).

**b3 (4 mars).** C’est le correctif qui compte pour les testeurs : Home Assistant démarre en **mode de récupération** si les registres ont changé de version majeure et que vous revenez à une version plus ancienne [#164340](https://github.com/home-assistant/core/pull/164340). L’intégration **Sauvegarde** est en plus disponible dans ce mode [#164734](https://github.com/home-assistant/core/pull/164734). On corrige aussi une boucle infinie du satellite Assist ESPHome [#163097](https://github.com/home-assistant/core/pull/163097), et une réparation apparaît après l’import de la configuration YAML d’InfluxDB [#164145](https://github.com/home-assistant/core/pull/164145).

**b4 (4 mars, deux heures avant la stable).** Thermostats QuickApp de Fibaro [#164344](https://github.com/home-assistant/core/pull/164344) et aperçu de la variable `this` dans les entités template créées depuis l’interface [#164740](https://github.com/home-assistant/core/pull/164740).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour **BSB-Lan, l’image Container, LIFX, les lumières, Satel Integra, Snapcast, StarLine, Tado, Template et Z-Wave**.

## 👩‍💻 Côté développeurs

- [async_listen est déprécié dans Labs](https://contributors.home-assistant.io/blog/2026/02/16/labs-async-listen-deprecation/)
- [Changements dans la gestion des erreurs du helper OAuth 2.0](https://contributors.home-assistant.io/blog/2026/02/19/oauth-token-request-error-handling/)
- [Les intégrations personnalisées peuvent fournir leurs propres logos](https://contributors.home-assistant.io/blog/2026/02/24/brands-proxy-api/)
- [Reconfiguration possible pour le helper webhook](https://contributors.home-assistant.io/blog/2026/02/18/reconfiguration-support-for-webhook-helper/)
- [Suppression des fonctions de lumière obsolètes](https://contributors.home-assistant.io/blog/2026/02/23/remove-deprecate-light-features/)

## 🧭 Pour le canal bêta

Revenir de la bêta à la stable n’est pas anodin. Avec ce cycle, Home Assistant détecte un retour en arrière des registres et démarre en mode de récupération, avec la restauration de sauvegarde à portée de main. Faites donc une **sauvegarde complète avant d’installer une bêta**, c’est elle qui vous permettra de revenir en arrière proprement.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Le nettoyage par pièce a bien profité de la bêta : on voit ses réglages bouger de la b1 à la b3. Pour moi, la vraie bonne nouvelle reste quand même la sauvegarde dans le mode de récupération. C’est exactement le filet de sécurité qu’on veut quand on vit sur le canal bêta.
</div>

Votre aspirateur a-t-il bien reconnu vos pièces ? Partagez votre expérience sur le forum.

<p class="ha-signature">— XAV59213</p>
