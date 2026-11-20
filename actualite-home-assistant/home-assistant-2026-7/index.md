---
layout: ha-release
title: "Home Assistant 2026.7 : les déclencheurs « par usage » sortent de Labs et deviennent la norme"
short_title: "2026.7 : des automatisations qui parlent votre langue"
description: "Home Assistant 2026.7 (1er juillet 2026) en français : déclencheurs et conditions par usage activés pour tous, automatisations par pièce, journal Activité en frise chronologique, bouton Tout mettre à jour, panneaux infrarouge et radiofréquence, firmware Raspberry Pi et breaking changes."
excerpt_fr: "Huit mois de travail aboutissent : on décrit ce que la maison doit faire, par pièce, sans pièges techniques. Le journal Activité devient une frise et un bouton « Update all » met tout à jour d’un geste."
image: /actualite-home-assistant/home-assistant-2026-7/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.7, juillet 2026"
date: 2026-07-01
release_date: 2026-07-01
section: actualite-ha
version: "2026.7"
month: "Juillet 2026"
official_title: "2026.7: Automations that speak your language"
release_url: https://www.home-assistant.io/blog/2026/07/01/release-20267/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.7/
tags: [home-assistant, mise-a-jour, 2026.7]
seo:
  type: NewsArticle
gallery:
  - src: images/automation-purpose-specific-trigger.webp
    caption: "Les déclencheurs par usage, désormais proposés à tout le monde dans l’éditeur d’automatisations."
  - src: images/automation-area-target.webp
    caption: "Une automatisation construite autour du mouvement dans une pièce, et non d’un seul capteur."
  - src: images/automation-event-trigger.webp
    caption: "Réagir directement à une entité évènement, sans les pièges d’un déclencheur d’état."
  - src: images/documentation.webp
    caption: "Chaque déclencheur, condition et action a désormais sa propre page de documentation."
  - src: images/activity-timeline.webp
    caption: "Le journal Activité transformé en frise chronologique, groupée par jour."
  - src: images/update-all-grouped.webp
    caption: "La page Mises à jour regroupée par familles, avec un bouton « Update all » par carte."
  - src: images/infrared-rf-panels.webp
    caption: "Les nouveaux panneaux Infrarouge et Radiofréquence dans les Paramètres."
  - src: images/zha-device-management.webp
    caption: "La gestion d’un appareil Zigbee (ZHA) sur une page complète, avec onglets."
  - src: images/rpi-firmware-update.webp
    caption: "La mise à jour du firmware Raspberry Pi proposée dans Paramètres › Mises à jour."
---

C’est l’aboutissement d’environ **huit mois de travail** : avec la **2026.7**, sortie le **1er juillet 2026**, les **déclencheurs et conditions par usage sortent de Labs et deviennent la norme pour tout le monde** 🎉. Frenck résume l’objectif poursuivi depuis des années : **plus de puissance, moins de complexité**. On ne part plus des rouages de Home Assistant (quelle entité, quel état ?) mais de ce que l’on veut : *« Quand la chambre descend sous 18 °C, allume le chauffage. »* Et bonne nouvelle : **rien ne casse**, vos automatisations existantes continuent de fonctionner.

<div class="ha-callout info" markdown="1">
**En bref**
- 🤖 Déclencheurs et conditions **par usage** activés pour tous, pensés **par pièce**.
- 📜 Le journal **Activité** (ex-logbook) devient une frise chronologique claire.
- ⬆️ **Update all** : les mises à jour regroupées par familles, installées d’un geste.
- 📡 Panneaux dédiés **infrarouge** et **radiofréquence** ; gestion **ZHA** repensée.
- 🍓 Mise à jour du **firmware Raspberry Pi** depuis Home Assistant.
</div>

## ✨ Les nouveautés phares

### 🤖 Créer une automatisation devient naturel

Les blocs testés depuis la 2025.12 dans Labs sont désormais proposés **par défaut** dans l’éditeur. Ce n’est pas qu’un habillage plus sympathique, explique l’équipe, et voici pourquoi.

{% include ha-figure.html src="images/automation-purpose-specific-trigger.webp" caption="On choisit « Température passe sous… » plutôt qu’un déclencheur d’état numérique sur un attribut." %}

**1. On part de l’intention.** Plus besoin de penser « déclencheur d’état numérique », « attribut » ou « unité » : on décrit le moment qui compte.

**2. On raisonne par pièce.** Les nouveaux blocs ciblent des **pièces, étages ou étiquettes**. *« Quand du mouvement est détecté dehors, allume les lumières dehors »* : la même automatisation fonctionne avec un capteur… ou cinq, et intègre automatiquement ceux que vous ajouterez demain.

{% include ha-figure.html src="images/automation-area-target.webp" caption="Une automatisation autour du mouvement dans une pièce plutôt que d’un capteur précis." %}

**3. Les intégrations peuvent ajouter leurs propres déclencheurs.** Un capteur vous donne le prix de l’électricité ; l’intégration, elle, peut vous dire **quand le prix est le plus bas aujourd’hui**.

**4. Fini les pièges techniques.** Plus besoin de se soucier des états `unknown` ou `unavailable` : chaque bloc les gère comme il faut. Et un déclencheur d’**entité évènement** se déclenche bien à chaque évènement, même identique au précédent (là où un déclencheur d’état pouvait rester muet).

**Et le YAML ?** Il reste là : les déclencheurs génériques, conditions, templates et le YAML fonctionnent comme avant, et les nouveaux blocs se lisent bien en YAML. Chaque déclencheur, condition et action a d’ailleurs maintenant **sa propre page de documentation**.

**Pour essayer :** ouvrez **Paramètres › Automatisations et scènes › Créer une automatisation**, puis commencez par ce que vous voulez qu’il se passe.

### 📜 Le journal Activité devient une frise

L’**Activité** (que beaucoup appellent encore *logbook*) est reconstruite de zéro en **frise chronologique** : l’heure à gauche, une pastille colorée avec l’icône de l’entité, le texte à côté, le tout **groupé par jour**.

{% include ha-figure.html src="images/activity-timeline.webp" caption="La nouvelle frise de l’Activité." %}

- Le texte d’état reprend **les mêmes mots que le reste de l’application**.
- La **cause** est affichée : l’avatar de la personne, le déclencheur de l’automatisation, l’intégration.
- Dans les vues compactes (fenêtre de détails, pages appareil et pièce, cartes), un clic sur l’heure bascule entre heure exacte et heure relative.

### ⬆️ « Update all » : fini le mur de mises à jour

La page **Paramètres › Mises à jour** regroupe désormais les mises à jour en cartes : **Home Assistant** (Core, OS, Supervisor) en haut, une carte par intégration ayant plusieurs mises à jour (vos sept ESPHome ensemble !), les **Intégrations** restantes, les **Apps**, et les mises à jour **ignorées** à part. Un bouton **Update all** par carte s’occupe du reste, sans cases à cocher.

{% include ha-figure.html src="images/update-all-grouped.webp" caption="Les mises à jour regroupées et le bouton « Update all »." %}

### 📡 Infrarouge, radiofréquence et Zigbee mieux rangés

- Des **panneaux dédiés à l’infrarouge et à la radiofréquence** apparaissent dans les Paramètres.
- La gestion d’un appareil **ZHA** (clusters, liaisons, signature, voisins) quitte sa petite fenêtre pour une **page complète à onglets**, avec un résumé de l’appareil en haut.

### 🍓 Le firmware du Raspberry Pi depuis Home Assistant

Environ **un tiers des installations** tournent sur Raspberry Pi. Une entité de mise à jour propose désormais le **firmware** du Pi (corrections, compatibilité NVMe, thermique, surtout sur Pi 5 et CM5). À savoir :
- il faut **Home Assistant OS 18 ou plus** ;
- sur **Pi 4**, uniquement si la carte démarre sur **carte SD** ;
- la Home Assistant Yellow avec Compute Module 4 n’est pas prise en charge (quand la mise à jour est impossible, l’entité n’apparaît tout simplement pas) ;
- un **redémarrage** est demandé à la fin.

## 🧩 Nouvelles intégrations

✅ Dix ajouts :

- **Aqvify** (puits et cuves, platine), **Chef iQ** (sondes de cuisson Bluetooth), **Dropbox** (sauvegardes ; la connexion passe par le service de liaison de compte de Home Assistant Cloud, sans abonnement requis), **Edifier Infrared**, **energieleser**, **Envertech EVT800** (micro-onduleur solaire), **Greencell** (bornes VE via MQTT), **Helty Flow** (VMC), **KlikAanKlikUit** (prises 433 MHz) et **MELCloud Home** (climatisation Mitsubishi Electric).
- Intégrations virtuelles : **Avosdim** (via Motionblinds), **BWT** (via SEKO PoolDose), **Nexen**, **Gitter**.

**SAJ Solar Inverter**, **SMTP**, **Swisscom Internet-Box** et **UniFi AP** passent par l’interface. Grand ménage de printemps… en juillet : une vingtaine d’intégrations cassées ou abandonnées sont retirées (Clementine, MS Teams, Mycroft, Microsoft Face, Watson TTS…).

## 🔧 Améliorations notables

- 🇫🇷 **Overkiz** prend en charge **Rexel Energeasy Connect**, en cloud et en local.
- **Tesla Powerwall 3**, **Tedee** (connectivité), **Wallbox**, **SMTP** (entités de notification), **Alexa Devices**, **SwitchBot**…
- **Format d’heure** au choix dans l’interface (exact, relatif court ou long) pour les entités horodatées.
- Modifier la durée d’un **minuteur en cours**, frontend plus rapide (graphiques énergie, historique, statistiques), templates jusqu’à **40 % plus rapides**, traces plus claires, capteurs Matter d’humidité du sol, classe « projecteur » pour les lecteurs multimédias.

## ⚠️ Breaking changes à surveiller

- **Déclencheurs par usage renommés** (si vous les utilisiez dans Labs, notamment en YAML) : `battery.low` → `battery.became_low`, `battery.not_low` → `battery.no_longer_low`, `vacuum.docked` → `vacuum.returned_to_dock`, `lawn_mower.docked` → `lawn_mower.returned_to_dock`, `schedule.turned_on/off` → `schedule.block_started/ended`, `timer.time_remaining` → `timer.remaining_time_reached`, `update.update_became_available` → `update.became_available`. Conditions : `climate.target_*` → `climate.is_target_*`.
- **Zones** : le nombre de personnes et l’attribut `persons` se calculent à partir de l’attribut `in_zones` des personnes.
- **Personnes** : plus de coordonnées GPS de la maison quand la localisation vient d’un scanner de présence.
- **Z-Wave JS** : serveur Z-Wave JS à mettre à jour.
- **iCloud**, **StarLine**, **Tractive** : attribut `battery_level` supprimé des suivis d’appareils ; **Reolink Duo** : un sous-appareil par objectif ; **Rabbit Air**, **BSB-LAN**, **Tesla Fleet**, **Teslemetry**, **Zeroconf** : ajustements.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.7**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-7" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète.**
2. Si vous utilisez **Z-Wave JS** hors App officielle, mettez d’abord le serveur à jour.
3. Si vous aviez testé les blocs Labs en YAML, appliquez les renommages ci-dessus.
4. Après la mise à jour, testez le bouton **Update all**… sur une carte à la fois si vous êtes prudent.

<div class="ha-avis" markdown="1">
### 💬 Mon avis

C’est sans doute **la version la plus importante de l’année pour les débutants**. Penser « par pièce » plutôt que « par capteur » change tout : une automatisation bien écrite aujourd’hui fonctionnera encore quand vous ajouterez des appareils demain. Le fait que les intégrations puissent ajouter leurs propres déclencheurs ouvre aussi de belles perspectives pour nous, développeurs d’intégrations HACS. Gros coup de cœur pour la nouvelle frise Activité, enfin lisible.
</div>

Vous avez converti vos vieilles automatisations ? Partagez vos avant/après sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— XAV59213</p>
