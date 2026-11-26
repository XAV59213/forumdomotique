---
layout: ha-dev
title: 'Bêta Home Assistant 2026.12 : un dialogue de volets qu’on attrape, des boutons multi-appuis et Home Assistant Link'
short_title: 'Bêta 2026.12 : volets dessinés et boutons multi-appuis'
description: 'La bêta de Home Assistant 2026.12 en cours en français : dialogue des volets redessiné, boutons multi-appuis, voix nouvelle génération, Freebox et Météo-France.'
excerpt_fr: 'Bêta en cours : le dialogue des volets dessine votre volet, les boutons gèrent double appui et appui long, la voix nouvelle génération arrive dans Labs, et Cloud devient Link. Pour nous : volets Freebox et alerte Météo-France à vérifier.'
image: /actualite-ha-dev/home-assistant-2026-12-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.12, décembre 2026'
date: 2026-11-25
section: actualite-ha-dev
cycle: 2026-12
version: '2026.12'
month: Décembre 2026
planned_fr: 2 décembre 2026
release_url: https://rc.home-assistant.io/blog/2026/11/25/release-202612/
official_title: '2026.12 Beta: Under cover 🪟'
changelog_url: https://rc.home-assistant.io/changelogs/core-2026.12/
gallery:
- src: images/cover-more-info.webp
  caption: 'Le nouveau dialogue des volets : le dessin du volet sert de commande.'
- src: images/timer-list-dialog.webp
  caption: Les minuteurs vocaux d’un satellite, avec compte à rebours, dans la nouvelle entité Liste de minuteurs.
- src: images/camera-player.webp
  caption: Le lecteur de caméra de Home Assistant, identique sur tous les navigateurs et dans les applications.
- src: images/energy-batteries.webp
  caption: 'Tableau Énergie : la batterie domestique mesurée par sens de circulation.'
- src: images/energy-suggestions.webp
  caption: Paramètres › Énergie propose les compteurs oubliés à ajouter au tableau.
- src: images/add-device-or-integration.webp
  caption: Le dialogue unique « Ajouter un appareil ou une intégration ».
- src: images/startup-details.webp
  caption: Suivre le démarrage de Home Assistant en direct, intégration par intégration.
- src: images/integration-health.webp
  caption: 'L’élément « Santé » d’une intégration : entités, réparations, erreurs du journal.'
- src: images/database-usage.webp
  caption: 'La carte Base de données de la page Stockage : quelles tables et quelles entités prennent de la place.'
- src: images/link-settings.webp
  caption: Home Assistant Cloud devient Home Assistant Link dans les Paramètres.
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.12'
seo:
  type: NewsArticle
---
La bêta de la dernière version de l’année est en cours. La **2026.12.0b0** a été publiée le **25 novembre 2026** au soir, suivie de la **b1** et de la **b2** le **26 novembre**. Les notes officielles, encore en cours de rédaction, annoncent la version stable et sa *release party* pour le **2 décembre 2026**, à 21 h (heure de Paris). Rien n’est figé : certaines fonctionnalités peuvent encore changer, ou ne pas arriver dans la version finale. L’intégration Bambu Lab, d’abord annoncée, a d’ailleurs été retirée dès la b1.

## ✨ Les nouveautés principales

- 🪟 **Volets** : un nouveau dialogue dessine votre volet, store, rideau ou porte de garage, et se commande en l’attrapant. On peut enregistrer des positions favorites, et les volets ouverts s’affichent en bleu sur les tuiles.
- 🔘 **Boutons** : le déclencheur « Bouton appuyé » gère aussi les télécommandes et interrupteurs, avec double, triple ou quadruple appui, plus un appui long (éventuellement répété) et le relâchement. C’est une première étape : Universal Devices ISY/IoX gère l’ensemble, Lutron Caséta et OpenDisplay une partie seulement. Les automatisations existantes ne changent pas.
- 🗣️ **Voix nouvelle génération**, à activer dans Labs : un second modèle confirme le mot d’activation (Okay Nabu, Hey Jarvis, Hey Mycroft), ce qui réduit les faux déclenchements et permet d’enchaîner le mot et la commande. Les minuteurs vocaux d’un satellite ESPHome apparaissent dans une nouvelle entité Liste de minuteurs. La Voice Preview Edition a besoin de son firmware bêta.
- ⚡ **Tableau Énergie** : les batteries domestiques peuvent être mesurées par sens de circulation (réseau, solaire, maison) au lieu d’être estimées. Paramètres › Énergie signale aussi les compteurs d’énergie, de gaz et d’eau oubliés.
- 📹 **Lecteur de caméra** unifié, identique partout, avec zoom, image dans l’image et un badge indiquant le mode de transmission.
- 🔗 **Home Assistant Cloud devient Home Assistant Link**, sans rien à faire de votre côté : même service, nouveau nom. Les sauvegardes cloud s’appellent désormais sauvegardes hors site. L’intégration conserve le domaine `cloud`.
- 🔍 On ajoute désormais un appareil depuis un dialogue unique, on peut suivre le démarrage intégration par intégration, consulter la **santé** d’une intégration et voir, sur la page Stockage, quelles tables et quelles entités occupent la base de données.
- 🧩 Les notes annoncent **16 nouvelles intégrations**, parmi lesquelles Electrolux (aussi pour AEG et Frigidaire), E3/DC, Powersensor, Tile BLE, Intesis Modbus, Trimlight et plusieurs commandes infrarouges. **Bambu Lab a été retirée dès la b1.** Parmi les améliorations, l’intégration **Freebox** officielle peut désormais piloter les **volets roulants** appairés à une Freebox Delta ou Freebox Home, et affiche le trafic de ses ports LAN. Deux intégrations sont retirées : **Crownstone** (service cloud fermé) et **Fitbit** (l’API Web a été arrêtée par Google le 2 novembre 2026).

## ⚠️ Changements cassants

Les notes en dressent une longue liste. Voici ceux qui méritent le plus d’attention :

- **Météo-France** : l’état du capteur d’alerte, jusqu’ici toujours en français (`Vert`, `Jaune`, `Orange`, `Rouge`), devient `green`, `yellow`, `orange` ou `red`, et s’affiche dans votre langue dans l’interface. Il faut mettre à jour les automatisations, scripts et templates qui testent cet état.
- **Matter** et **Zigbee (ZHA)** : les prises multiples et les interrupteurs multi-canaux deviennent des appareils enfants. Les identifiants d’entité restent les mêmes, mais les noms affichés (`friendly_name`) changent. Les volets Matter de type volet roulant prennent la classe *shutter*.
- **Z-Wave** : plusieurs modules de volets prennent la classe de ce qu’ils pilotent (volet, store, portail…) au lieu de *window*. Il faut aussi **zwave-js-server 3.12.0** ou plus (app Z-Wave JS en version 1.11.0 au minimum).
- L’app communautaire **Home Assistant Matter Hub** doit être en version **2.1.0** ou plus, sinon elle n’est plus ouvrable depuis la barre latérale.

Pour les intégrations personnalisées, un flux de configuration qui renvoie un type de résultat en texte simple (`"form"`, `"abort"`) au lieu de l’énumération `FlowResultType` échoue désormais avec une erreur `TypeError`. Les notes de la bêta et le blog des contributeurs ne signalent rien de spécifique à mes intégrations HACS (freebox_homexa, freesmsxa, jourferier, chauffage, phase_lune, saintdujour, piscinexa, date_countdown et starship_tracker) : je les vérifierai comme d’habitude avant la version stable.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Sur le papier, cette dernière bêta de l’année est réjouissante : des volets enfin pensés comme des volets, des boutons qui gèrent le double appui, et, de notre côté, des **volets Freebox** pilotables. Je garderai surtout un œil sur le changement de l’alerte Météo-France, qui peut casser une automatisation si on ne le voit pas venir.
</div>

<p class="ha-signature">— XAV59213</p>
