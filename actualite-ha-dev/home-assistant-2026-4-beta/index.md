---
layout: ha-dev
title: 'Bêta Home Assistant 2026.4 : onze bêtas, un record, pour l’infrarouge natif et les déclencheurs multi-domaines'
short_title: 'Bêta 2026.4 : onze bêtas pour l’infrarouge'
description: "La bêta de Home Assistant 2026.4 (25 mars – 1er avril 2026) : infrarouge natif, déclencheurs et conditions multi-domaines, Dropbox retiré, onze bêtas."
excerpt_fr: 'Onze bêtas en une semaine : la 2026.4 a été la plus remaniée de l’année. Les déclencheurs et conditions par usage s’enrichissent presque chaque jour, le support des aspirateurs MQTT est annulé, et l’intégration Dropbox est retirée juste avant la sortie.'
image: /actualite-ha-dev/home-assistant-2026-4-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.4, avril 2026'
date: 2026-03-25
section: actualite-ha-dev
cycle: 2026-4
version: '2026.4'
month: Avril 2026
release_url: https://www.home-assistant.io/blog/2026/04/01/release-20264/
official_title: '2026.4: Infrared never left the chat'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.4/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.4'
seo:
  type: NewsArticle
---
**Onze bêtas**, de la **2026.4.0b0** (25 mars 2026) à la **b10** (1er avril, deux heures avant la version finale) : c’est le cycle le plus agité de 2026. Cette agitation s’explique : la bêta servait à construire, presque au jour le jour, la famille des **déclencheurs et conditions multi-domaines** (porte, fenêtre, mouvement, batterie, vanne, minuteur, calendrier…), en même temps que l’**infrarouge natif**.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : infrarouge natif par des proxys ESPHome, déclencheurs et conditions multi-domaines dans Labs, couleur de fond des sections, utilisateurs et codes PIN des serrures Matter, nettoyage par pièce à la voix.
- 🔁 **Pendant la bêta** : des dizaines de déclencheurs et conditions ajoutés (b1 à b8), les entités *number* retirées puis rétablies comme seuils (b3), le support des aspirateurs MQTT annulé (b5), Dropbox retiré (b9).
- ⚠️ **À vérifier** : JVC Projector, Litter-Robot, Motion Blinds, MQTT, pyLoad, Roth Touchline, Tuya et Z-Wave.
</div>

## 🧪 Ce qui était en test

- L’**infrarouge natif** : des proxys ESPHome pilotent téléviseurs, climatiseurs, ventilateurs…
- Des déclencheurs et conditions **multi-domaines** (porte, fenêtre, mouvement, température, batterie…) dans Labs.
- Une **couleur de fond** pour les sections de dashboard.
- La **gestion des utilisateurs et codes PIN** des serrures Matter.
- Le **nettoyage par pièce** commandé à la voix (« Nettoie la cuisine »).

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 et b2 (26 mars).** Une longue série harmonise les **noms des actions** : cloud, script, vanne, humidificateur, automatisation, compteur, groupe, journal, dashboard, météo… [#166516](https://github.com/home-assistant/core/pull/166516) [#166525](https://github.com/home-assistant/core/pull/166525). On voit aussi arriver les déclencheurs `water_heater.operation_mode_changed` [#166450](https://github.com/home-assistant/core/pull/166450) et `humidifier.mode_changed` [#166241](https://github.com/home-assistant/core/pull/166241), les **déclencheurs de batterie** [#166258](https://github.com/home-assistant/core/pull/166258) et la **progression de l’envoi** des sauvegardes Google Drive [#166549](https://github.com/home-assistant/core/pull/166549). La réparation qui signalait les anciens capteurs d’état de porte Z-Wave est **annulée** [#166583](https://github.com/home-assistant/core/pull/166583).

**b3 (26 mars).** Les entités *number* sont retirées des déclencheurs et conditions de batterie, d’humidité, de luminosité, d’humidité du sol et de puissance [#166593](https://github.com/home-assistant/core/pull/166593) [#166597](https://github.com/home-assistant/core/pull/166597). Elles reviennent aussitôt, mais **comme seuils** pour la batterie et l’humidité du sol [#166607](https://github.com/home-assistant/core/pull/166607) [#166608](https://github.com/home-assistant/core/pull/166608). De nouvelles conditions arrivent : `light.is_brightness` [#166601](https://github.com/home-assistant/core/pull/166601), `climate.is_hvac_mode` [#166570](https://github.com/home-assistant/core/pull/166570) et `humidifier.is_mode` [#166610](https://github.com/home-assistant/core/pull/166610). L’intégration **TP-Link LTE** est supprimée [#166615](https://github.com/home-assistant/core/pull/166615).

**b4 (27 mars).** Conditions sur les entités *select* [#166612](https://github.com/home-assistant/core/pull/166612), météo prise en compte dans les conditions d’humidité [#166599](https://github.com/home-assistant/core/pull/166599). Les entités repassent à l’**ancien nommage** (*legacy naming*) [#166696](https://github.com/home-assistant/core/pull/166696).

**b5 (30 mars).** Le **support des segments d’aspirateur via MQTT est annulé** [#166761](https://github.com/home-assistant/core/pull/166761). Une douzaine d’intégrations OAuth (Google Mail, Google Sheets, Automower, Neato…) gèrent maintenant l’indisponibilité de leur implémentation OAuth [#166650](https://github.com/home-assistant/core/pull/166650).

**b6 à b8 (31 mars).** Les **conditions et déclencheurs de vanne** arrivent (`valve.opened` et `valve.closed`) [#166634](https://github.com/home-assistant/core/pull/166634) [#165160](https://github.com/home-assistant/core/pull/165160). Z-Wave sépare l’état « Ouverture » en capteurs Ouvert/Fermé et Basculé [#166635](https://github.com/home-assistant/core/pull/166635). Puis viennent les conditions de **minuteur** [#166641](https://github.com/home-assistant/core/pull/166641), de **calendrier** [#166643](https://github.com/home-assistant/core/pull/166643) et de **compteur** [#166879](https://github.com/home-assistant/core/pull/166879). Les plateformes de déclencheurs et de conditions ne sont plus chargées qu’à leur première utilisation [#166911](https://github.com/home-assistant/core/pull/166911) [#166939](https://github.com/home-assistant/core/pull/166939).

**b9 et b10 (1er avril).** L’intégration **Dropbox est retirée** de la version [#166986](https://github.com/home-assistant/core/pull/166986). L’intégration BMW est réduite à une intégration vide qui affiche seulement un avis de réparation [#166983](https://github.com/home-assistant/core/pull/166983), et les sauvegardes reçues ne sont plus stockées que dans le dossier temporaire [#166982](https://github.com/home-assistant/core/pull/166982).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour **JVC Projector, Litter-Robot, Motion Blinds, MQTT, pyLoad, Roth Touchline, Tuya et Z-Wave**.

## 👩‍💻 Côté développeurs

- [Les agents de sauvegarde peuvent indiquer la progression de l’envoi](https://contributors.home-assistant.io/blog/2026/03/11/backup-upload-progress/)
- [Mises à jour des composants du frontend pour la 2026.4](https://contributors.home-assistant.io/blog/2026/03/25/frontend-component-updates-2026.4/)
- [Chargement à la demande des données partagées du frontend (*lazy context*)](https://contributors.home-assistant.io/blog/2026/03/25/frontend-lazy-context/) et [nouvelle façon de gérer les boîtes de dialogue](https://contributors.home-assistant.io/blog/2026/03/25/frontend-dialogs/)
- [Nouvelle plateforme d’entités infrarouges](https://contributors.home-assistant.io/blog/2026/03/30/infrared-entity-platform/)

## 🧭 Pour le canal bêta

Ce cycle montre que les fonctionnalités de **Labs changent pendant la bêta**. Une automatisation construite avec un déclencheur par usage le lundi pouvait voir son schéma bouger le jeudi, comme avec les entités *number* retirées puis rétablies dans la même journée. Sur le canal bêta, attendez la dernière bêta avant de migrer vos automatisations importantes vers ces nouveautés.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Onze bêtas, c’est beaucoup, mais c’est surtout le signe d’un vrai travail de construction en public. Le retrait de Dropbox et l’annulation du support des aspirateurs MQTT rappellent une règle simple : tant que la version finale n’est pas sortie, rien n’est acquis.
</div>

Vous utilisez déjà l’infrarouge natif ? Montrez-moi votre installation sur le forum.

<p class="ha-signature">— XAV59213</p>
