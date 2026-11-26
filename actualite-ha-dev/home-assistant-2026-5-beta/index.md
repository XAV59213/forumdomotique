---
layout: ha-dev
title: 'Bêta Home Assistant 2026.5 : la radiofréquence arrive, et les automatisations apprennent à ignorer les entités incompatibles'
short_title: 'Bêta 2026.5 : radiofréquence et durées'
description: 'La bêta de Home Assistant 2026.5 (29 avril – 6 mai 2026) en français : radiofréquence, Téléinfo, durées dans les conditions, déclencheurs média et correctifs.'
excerpt_fr: La bêta 2026.5 teste la radiofréquence, le port série via le réseau et Téléinfo pour le Linky. Pendant la bêta, les conditions gagnent les durées, les lecteurs multimédia leurs déclencheurs de volume, et l’émetteur infrarouge Broadlink arrive.
image: /actualite-ha-dev/home-assistant-2026-5-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.5, mai 2026'
date: 2026-04-29
section: actualite-ha-dev
cycle: 2026-5
version: '2026.5'
month: Mai 2026
release_url: https://www.home-assistant.io/blog/2026/05/06/release-20265/
official_title: '2026.5: We''re on the same frequency now 📡'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.5/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.5'
seo:
  type: NewsArticle
---
Ouverte le **29 avril 2026**, la bêta 2026.5 a d’abord laissé passer cinq jours sans nouvelle version. La **b1** n’est arrivée que le **4 mai**, avec 42 changements d’un coup. Trois autres ont suivi, puis la stable est sortie le **6 mai**. Pour nous, utilisateurs français, c’est le cycle de **Téléinfo** pour lire le Linky en local.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : radiofréquence (ESPHome ou Broadlink RM4 Pro), port série via le réseau, tableau Maintenance des batteries, durées dans les déclencheurs par usage, Téléinfo.
- 🔁 **Pendant la bêta** : émetteur infrarouge Broadlink (b1), durées dans toutes les conditions d’entité (b1), déclencheurs et conditions de volume et de sourdine pour les lecteurs multimédia (b2-b3), entités incompatibles exclues des automatisations (b3-b4).
- ⚠️ **À vérifier** : déclencheurs et conditions par usage, Gardena Bluetooth, pilight, Ring, Supervisor et Webhook.
</div>

## 🧪 Ce qui était en test

- La **radiofréquence** : volets, guirlandes, hottes… pilotés via ESPHome ou un Broadlink RM4 Pro.
- Les **ports série via le réseau** grâce au proxy série d’ESPHome.
- Un nouveau tableau **Maintenance** pour surveiller toutes les batteries.
- Des déclencheurs par usage qui comprennent les **durées** (« ouvert depuis 2 minutes »).
- **Téléinfo** : la consommation du Linky et des anciens compteurs électroniques, en local.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (4 mai).** **Broadlink gagne l’émission infrarouge** [#168889](https://github.com/home-assistant/core/pull/168889), dans la continuité de l’infrarouge natif de la 2026.4. Les **durées** sont prises en charge dans toutes les conditions d’entité [#169532](https://github.com/home-assistant/core/pull/169532), avec un schéma corrigé pour l’option « pendant » (*for*) [#169539](https://github.com/home-assistant/core/pull/169539). ZHA réinterroge l’appareil lors d’une reconfiguration [#169483](https://github.com/home-assistant/core/pull/169483). La détection du capteur de température du processeur est corrigée sur les anciennes FRITZ!Box [#169620](https://github.com/home-assistant/core/pull/169620), et les noms de configuration du nettoyage par zone changent pour les aspirateurs template [#169599](https://github.com/home-assistant/core/pull/169599).

**b2 (5 mai).** Nouveau déclencheur `media_player.muted` [#156736](https://github.com/home-assistant/core/pull/156736). Le rechargement des templates est amélioré [#169480](https://github.com/home-assistant/core/pull/169480). Le capteur template *uptime* [#169743](https://github.com/home-assistant/core/pull/169743) et la validation de Nord Pool [#169751](https://github.com/home-assistant/core/pull/169751) sont corrigés.

**b3 (6 mai).** Une série complète pour les **lecteurs multimédia** : `media_player.unmuted` [#169797](https://github.com/home-assistant/core/pull/169797), déclencheurs de volume [#169885](https://github.com/home-assistant/core/pull/169885), conditions de sourdine [#169892](https://github.com/home-assistant/core/pull/169892) et de volume [#169897](https://github.com/home-assistant/core/pull/169897). Le déclencheur `timer.time_remaining` arrive [#169763](https://github.com/home-assistant/core/pull/169763). Les ventilateurs Matter exposent la vitesse [#169696](https://github.com/home-assistant/core/pull/169696). Les automatisations d’humidité et de température **excluent les entités incompatibles** [#169898](https://github.com/home-assistant/core/pull/169898) [#169901](https://github.com/home-assistant/core/pull/169901).

**b4 (6 mai, deux heures avant la stable).** La même exclusion s’étend au climat, aux chauffe-eau et aux humidificateurs [#169903](https://github.com/home-assistant/core/pull/169903) [#169904](https://github.com/home-assistant/core/pull/169904) [#169905](https://github.com/home-assistant/core/pull/169905). Les scripts et conditions créés par les entités template sont aussi correctement déchargés [#169366](https://github.com/home-assistant/core/pull/169366).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour les **déclencheurs et conditions par usage**, **Gardena Bluetooth, pilight, Ring, Supervisor et Webhook**.

## 👩‍💻 Côté développeurs

- [Dépréciation de l’ancienne API de plateforme *device tracker*](https://contributors.home-assistant.io/blog/2026/04/20/legacy-device-tracker-deprecation/)
- [Identifiants d’entité avec un domaine qui ne correspond pas : dépréciés](https://contributors.home-assistant.io/blog/2026/04/07/entity-id-mismatched-domain-deprecated/)
- [Mises à jour des composants du frontend pour la 2026.5](https://contributors.home-assistant.io/blog/2026/05/04/frontend-component-updates-2026.5/) et [groupes de contexte du frontend](https://contributors.home-assistant.io/blog/2026/05/04/frontend-context-groups-decorators/)
- [Construction des apps avec Docker BuildKit](https://contributors.home-assistant.io/blog/2026/04/02/builder-migration/)
- [Nouvelle plateforme d’entités radiofréquence](https://contributors.home-assistant.io/blog/2026/04/24/radio-frequency-entity-platform/)
- [Enregistrer des stratégies de dashboard personnalisées](https://contributors.home-assistant.io/blog/2026/04/21/registering-custom-dashboard-strategies/)
- [De pyserial à serialx](https://contributors.home-assistant.io/blog/2026/04/27/pyserial-to-serialx/)
- [Type d’événement standard pour les sonnettes](https://contributors.home-assistant.io/blog/2026/04/15/doorbell-standard-event-type/)

## 🧭 Pour le canal bêta

Les déclencheurs par usage ont encore beaucoup bougé pendant cette bêta, et ils figurent dans la liste des changements cassants. Si vous avez créé des automatisations avec eux pendant la phase Labs, **ouvrez-les après la mise à jour** pour vérifier qu’elles sont toujours valides.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Pour un utilisateur français, Téléinfo est la vedette de ce cycle. Côté bêta, j’ai surtout retenu le travail sur l’exclusion des entités incompatibles : c’est invisible, mais ça rend les déclencheurs par pièce beaucoup plus fiables.
</div>

Vous lisez votre Linky avec Téléinfo ? Venez en parler sur le forum.

<p class="ha-signature">— XAV59213</p>
