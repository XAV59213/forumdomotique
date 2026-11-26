---
layout: ha-dev
title: 'Bêta Home Assistant 2026.1 : six bêtas entre deux réveillons pour le dashboard Home et les déclencheurs « par usage »'
short_title: 'Bêta 2026.1 : le dashboard Home passe au mobile'
description: 'La bêta de Home Assistant 2026.1 (29 décembre 2025 – 7 janvier 2026) en français : nouveautés en test, correctifs entre les six bêtas, Tibber en OAuth.'
excerpt_fr: 'Ouverte le 29 décembre 2025, la bêta 2026.1 teste le dashboard Home sur mobile et les déclencheurs par usage de Labs. En six bêtas : Tibber passe en OAuth, et les journaux Ring arrêtent de déborder.'
image: /actualite-ha-dev/home-assistant-2026-1-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.1, janvier 2026'
date: 2025-12-29
section: actualite-ha-dev
cycle: 2026-1
version: '2026.1'
month: Janvier 2026
release_url: https://www.home-assistant.io/blog/2026/01/07/release-20261/
official_title: '2026.1: Home is where the dashboard is 🥂'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.1/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.1'
seo:
  type: NewsArticle
---
La toute première bêta de 2026 est arrivée… en 2025 : la **2026.1.0b0** a été publiée le **29 décembre 2025** au soir, en pleines fêtes. Six bêtas plus tard, le **7 janvier 2026**, elle devenait la version stable. Sur le canal bêta, c’est un cycle calme. Les nouveautés étaient déjà là dès la b0, et les bêtas suivantes ont surtout servi à **corriger les intégrations**.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : dashboard Home adapté au mobile, page « Appareils », nouveaux déclencheurs par usage dans Labs, section Protocoles dans les Paramètres.
- 🔁 **Pendant la bêta** : Tibber passe à OAuth (b3), plusieurs correctifs Reolink, Tuya et Hikvision, une contrainte sur aiomqtt pour supprimer un appel bloquant (b5).
- ⚠️ **À vérifier** : les changements cassants documentés pour Coolmaster, Tailscale, UniFi Protect, Telegram bot et VeSync.
</div>

## 🧪 Ce qui était en test

D’après les notes de la version finale, la bêta embarquait :

- le **dashboard Home** qui affiche ses résumés (lumières, climat, sécurité, énergie) en haut de l’écran sur mobile, avec une nouvelle page **Appareils** pour ceux qui ne sont rattachés à aucune pièce ;
- dans **Labs**, des déclencheurs « par usage » pour les boutons, le climat, la présence, les humidificateurs, les lumières, les serrures, les scènes, les sirènes et les mises à jour ;
- une **section dédiée aux protocoles** (Matter, Zigbee, Z-Wave, Thread…) dans les Paramètres ;
- **8 nouvelles intégrations**, dont Watts Vision + et Fressnapf Tracker.

Le détail de chaque nouveauté est expliqué dans l’article de la version stable.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (30 décembre).** Une série de petites modifications ajoute un **type d’intégration** (appareil, service ou hub) à plusieurs intégrations : Netgear, NuHeat, Permobil, PoolDose, PoolSense, PS4 [#159816](https://github.com/home-assistant/core/pull/159816). Portainer corrige les statistiques des conteneurs arrêtés [#159964](https://github.com/home-assistant/core/pull/159964), et KNX ses références de traduction [#159959](https://github.com/home-assistant/core/pull/159959).

**b2 (31 décembre).** Correctif du déchargement de Netgear LTE [#160008](https://github.com/home-assistant/core/pull/160008) et d’un problème de concurrence (*thread safety*) dans Hikvision [#160027](https://github.com/home-assistant/core/pull/160027). Les images de la boutique Xbox passent en https [#160015](https://github.com/home-assistant/core/pull/160015).

**b3 (5 janvier), la plus fournie.** **Tibber passe à OAuth** [#156690](https://github.com/home-assistant/core/pull/156690). Si vous l’utilisez, c’est le changement à surveiller après la mise à jour. Tractive ajoute la prise en charge de l’API *health_overview* [#157960](https://github.com/home-assistant/core/pull/157960). Reolink corrige l’échelle de luminosité [#160106](https://github.com/home-assistant/core/pull/160106), et Tuya la couleur de ses lumières [#160280](https://github.com/home-assistant/core/pull/160280). La liste de courses attend désormais la fin de ses écritures [#157420](https://github.com/home-assistant/core/pull/157420), et le cloud vérifie la connexion avant d’enregistrer une URL de *cloudhook* [#160284](https://github.com/home-assistant/core/pull/160284).

**b4 (6 janvier).** Classe d’état des compteurs de pluie Ecowitt [#158204](https://github.com/home-assistant/core/pull/158204), unité d’un capteur Tibber [#160319](https://github.com/home-assistant/core/pull/160319), correspondance plus stricte des appareils Hue BLE [#160321](https://github.com/home-assistant/core/pull/160321).

**b5 (7 janvier, le jour de la sortie).** Ring arrête d’inonder les journaux pour les comptes sans abonnement [#158012](https://github.com/home-assistant/core/pull/158012). Le schéma de Telegram est corrigé [#160367](https://github.com/home-assistant/core/pull/160367), Bravia TV gagne le SSL [#160373](https://github.com/home-assistant/core/pull/160373), et une version minimale d’aiomqtt (2.5.0) est imposée pour corriger un appel bloquant [#160410](https://github.com/home-assistant/core/pull/160410).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour **Coolmaster, Tailscale, UniFi Protect, Telegram bot et VeSync**. Si vous utilisez l’une de ces intégrations, lisez la rubrique « Breaking changes » de l’article stable avant de mettre à jour.

## 🧭 Pour le canal bêta

Le cycle a été coupé par le Nouvel An : entre la b2 (31 décembre) et la b3 (5 janvier), aucune bêta n’a été publiée pendant cinq jours. Si vous testez pendant les fêtes, gardez une **sauvegarde récente** sous la main : en cas de souci, les correctifs peuvent mettre plusieurs jours à arriver.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Un démarrage d’année tranquille sur le canal bêta. Pour moi, le changement le plus important est le passage de Tibber à OAuth, parce que c’est le genre de modification qui peut demander une action de votre part. Le reste, ce sont des finitions bienvenues.
</div>

Vous testez les bêtas vous aussi ? Racontez-moi vos retours sur le forum.

<p class="ha-signature">— XAV59213</p>
