---
layout: ha-dev
title: 'Bêta Home Assistant 2026.7 : grand ménage, onze intégrations retirées pendant la bêta'
short_title: 'Bêta 2026.7 : les déclencheurs par usage pour tous'
description: "La bêta de Home Assistant 2026.7 (24 juin – 1er juillet 2026) : déclencheurs par usage pour tous, journal Activité, Update all et intégrations retirées."
excerpt_fr: La bêta 2026.7 fait sortir de Labs les déclencheurs par usage, et le journal devient une frise Activité. Pendant la bêta, onze vieilles intégrations sont retirées, de Mycroft à Microsoft Face.
image: /actualite-ha-dev/home-assistant-2026-7-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.7, juillet 2026'
date: 2026-06-24
section: actualite-ha-dev
cycle: 2026-7
version: '2026.7'
month: Juillet 2026
release_url: https://www.home-assistant.io/blog/2026/07/01/release-20267/
official_title: '2026.7: Automations that speak your language'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.7/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.7'
seo:
  type: NewsArticle
---
La **2026.7.0b0** a été publiée le **24 juin 2026**, et la version stable le **1er juillet**, après quatre bêtas correctives. C’est un tournant : les **déclencheurs et conditions par usage** quittent Labs et deviennent la norme. Pendant la bêta, Home Assistant en profite aussi pour faire un grand ménage parmi ses vieilles intégrations.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : déclencheurs et conditions par usage pour tous, pensés par pièce. Aussi : journal Activité en frise chronologique, « Update all », panneaux infrarouge et radiofréquence, gestion ZHA repensée, firmware du Raspberry Pi.
- 🔁 **Pendant la bêta** : onze intégrations retirées (b2 à b4), erreurs des conditions d’automatisation mieux gérées (b2), conditions solaires basées sur l’heure de l’événement (b4).
- ⚠️ **À vérifier** : déclencheurs par usage, BSB-LAN, iCloud, Person, Rabbit Air, Reolink, StarLine, Tesla Fleet, Teslemetry, Tractive, Zeroconf, Zone et Z-Wave JS.
</div>

## 🧪 Ce qui était en test

- Les déclencheurs et conditions **par usage** activés pour tous, pensés **par pièce**.
- Le journal **Activité** (ex-*logbook*) transformé en frise chronologique.
- **Update all** : les mises à jour regroupées par familles et installées d’un geste.
- Des panneaux dédiés à l’**infrarouge** et à la **radiofréquence**, et une gestion **ZHA** repensée.
- La mise à jour du **firmware du Raspberry Pi** depuis Home Assistant.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (24 juin au soir).** Dropbox récupère le paramètre d’autorisation et la portée OAuth qui lui manquaient [#174587](https://github.com/home-assistant/core/pull/174587).

**b2 (27 juin, 44 changements).** Le grand ménage commence : **ThermoWorks Smoke** [#174845](https://github.com/home-assistant/core/pull/174845), **Mycroft** [#174849](https://github.com/home-assistant/core/pull/174849), **Greenwave Reality** [#174929](https://github.com/home-assistant/core/pull/174929), **Dovado** [#174933](https://github.com/home-assistant/core/pull/174933), **Logentries** [#174939](https://github.com/home-assistant/core/pull/174939) et **ATEN Rack PDU** [#174940](https://github.com/home-assistant/core/pull/174940) sont retirés. Côté automatisations, les erreurs d’évaluation des conditions sont désormais interceptées [#174799](https://github.com/home-assistant/core/pull/174799), et une exception de l’ancienne condition solaire est corrigée [#174811](https://github.com/home-assistant/core/pull/174811). Le recorder gagne une commande WebSocket pour lire les options d’enregistrement d’une entité [#174134](https://github.com/home-assistant/core/pull/174134). Renault ajoute un mode de recharge déléguée [#174687](https://github.com/home-assistant/core/pull/174687), et AEMET ne rafraîchit plus la météo que toutes les 20 minutes [#174803](https://github.com/home-assistant/core/pull/174803).

**b3 (30 juin).** Retrait de **BlinkStick** [#174961](https://github.com/home-assistant/core/pull/174961), **Watson TTS** [#174967](https://github.com/home-assistant/core/pull/174967), **Clementine Music Player** [#174970](https://github.com/home-assistant/core/pull/174970) et **Microsoft Face** [#174977](https://github.com/home-assistant/core/pull/174977).

**b4 (1er juillet).** **Gitter** est retiré et remplacé par une intégration virtuelle gérée par Matrix [#175044](https://github.com/home-assistant/core/pull/175044). Le journal expose certains attributs d’état [#174808](https://github.com/home-assistant/core/pull/174808). Les déclencheurs numériques signalent leurs erreurs [#175093](https://github.com/home-assistant/core/pull/175093). Les conditions « soleil levé / couché » utilisent l’heure de l’événement [#175240](https://github.com/home-assistant/core/pull/175240). Le message de dépréciation du comportement des déclencheurs est clarifié [#175263](https://github.com/home-assistant/core/pull/175263).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour les **déclencheurs et conditions par usage**, **BSB-LAN, iCloud, Person, Rabbit Air, Reolink, StarLine, Tesla Fleet, Teslemetry, Tractive, Zeroconf, Zone et Z-Wave JS**.

## 👩‍💻 Côté développeurs

- [Changements des modèles d’entités *device tracker*](https://contributors.home-assistant.io/blog/2026/06/15/device-tracker-changes/)
- [Mises à jour des composants du frontend pour la 2026.7](https://contributors.home-assistant.io/blog/2026/06/23/frontend-component-updates-2026.7/)
- [Nouvelles énumérations d’unités](https://contributors.home-assistant.io/blog/2026/06/30/new-unit-enumerators/)
- [Dépréciation de l’option *home_assistant_start* d’async_initialize_triggers](https://contributors.home-assistant.io/blog/2026/06/30/async-initialize-triggers-home-assistant-start-deprecated/)

## 🧭 Pour le canal bêta

Avant d’installer une bêta, parcourez la liste des intégrations retirées pendant le cycle : elles peuvent tomber en cours de cycle. Ici, elles sont toutes tombées entre la b2 et la b4. Si vous en utilisiez une, l’intégration ne se chargera plus après la mise à jour.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Voir les déclencheurs par usage devenir la norme après des mois dans Labs, c’est l’aboutissement de tout ce qu’on a suivi depuis la 2026.1. Le ménage dans les vieilles intégrations allège Home Assistant, mais il vaut la peine de vérifier sa propre installation avant chaque mise à jour.
</div>

Vous avez migré vos automatisations vers les déclencheurs par usage ? Racontez-moi sur le forum.

<p class="ha-signature">— XAV59213</p>
