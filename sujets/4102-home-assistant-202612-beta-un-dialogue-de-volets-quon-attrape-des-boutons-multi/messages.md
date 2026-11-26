---
title: "Home Assistant 2026.12 (bêta) : un dialogue de volets qu’on attrape, des boutons multi-appuis et Home Assistant Link"
description: "La bêta Home Assistant 2026.12 : un dialogue de volets qu’on attrape, des boutons multi-appuis, Home Assistant Link, et les volets Freebox dans l’intégration officielle."
image: /actualite-ha-dev/home-assistant-2026-12-beta/images/cover.png
cover_alt: "Couverture : la bêta de Home Assistant 2026.12, décembre 2026"
date: 2026-11-26
canonical_url: https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/
sitemap: false
---

<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/4102-home-assistant-202612-b%C3%AAta-un-dialogue-de-volets-quon-attrape-des-boutons-multi-appuis-et-home-assistant-link/">Lire et commenter sur Forum Domotique</a></p>

<div class="ha-callout info" markdown="1">
**Article détaillé.** Cette actualité est aussi publiée dans la rubrique Actualité HA développement : [Bêta Home Assistant 2026.12 : un dialogue de volets qu’on attrape, des boutons multi-appuis et Home Assistant Link]({{ '/actualite-ha-dev/home-assistant-2026-12-beta/' | relative_url }}).
</div>

# Home Assistant 2026.12 (bêta) : un dialogue de volets qu’on attrape, des boutons multi-appuis et Home Assistant Link

![Couverture de l’article sur la bêta Home Assistant 2026.12. Couverture : XAV59213](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/cover.png)

La bêta de la dernière version de l’année est en cours. La **2026.12.0b0** a été publiée le **25 novembre 2026** au soir, suivie de la **b1** et de la **b2** le **26 novembre**. Les notes officielles, encore en cours de rédaction, annoncent la version stable et sa *release party* pour le **2 décembre 2026**, à 21 h (heure de Paris). Rien n’est figé : certaines fonctionnalités peuvent encore changer, ou ne pas arriver dans la version finale. L’intégration Bambu Lab, d’abord annoncée, a d’ailleurs été retirée dès la b1.

## ✨ Les nouveautés principales

- 🪟 **Volets** : un nouveau dialogue dessine votre volet, store, rideau ou porte de garage, et se commande en l’attrapant. On peut enregistrer des positions favorites, et les volets ouverts s’affichent en bleu sur les tuiles.

![Le nouveau dialogue des volets : le dessin du volet sert de commande. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/cover-more-info.webp)

- 🔘 **Boutons** : le déclencheur « Bouton appuyé » gère aussi les télécommandes et interrupteurs, avec double, triple ou quadruple appui, plus un appui long (éventuellement répété) et le relâchement. C’est une première étape : Universal Devices ISY/IoX gère l’ensemble, Lutron Caséta et OpenDisplay une partie seulement. Les automatisations existantes ne changent pas.
- 🗣️ **Voix nouvelle génération**, à activer dans Labs : un second modèle confirme le mot d’activation (Okay Nabu, Hey Jarvis, Hey Mycroft), ce qui réduit les faux déclenchements et permet d’enchaîner le mot et la commande. Les minuteurs vocaux d’un satellite ESPHome apparaissent dans une nouvelle entité Liste de minuteurs. La Voice Preview Edition a besoin de son firmware bêta.

![Les minuteurs vocaux d’un satellite, avec compte à rebours, dans la nouvelle entité Liste de minuteurs. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/timer-list-dialog.webp)

- ⚡ **Tableau Énergie** : les batteries domestiques peuvent être mesurées par sens de circulation (réseau, solaire, maison) au lieu d’être estimées. Paramètres › Énergie signale aussi les compteurs d’énergie, de gaz et d’eau oubliés.

![Tableau Énergie : la batterie domestique mesurée par sens de circulation. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/energy-batteries.webp)

![Paramètres › Énergie propose les compteurs oubliés à ajouter au tableau. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/energy-suggestions.webp)

- 📹 **Lecteur de caméra** unifié, identique partout, avec zoom, image dans l’image et un badge indiquant le mode de transmission.

![Le lecteur de caméra de Home Assistant, identique sur tous les navigateurs et dans les applications. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/camera-player.webp)

- 🔗 **Home Assistant Cloud devient Home Assistant Link**, sans rien à faire de votre côté : même service, nouveau nom. Les sauvegardes cloud s’appellent désormais sauvegardes hors site. L’intégration conserve le domaine `cloud`.

![Home Assistant Cloud devient Home Assistant Link dans les Paramètres. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/link-settings.webp)

- 🔍 On ajoute désormais un appareil depuis un dialogue unique, on peut suivre le démarrage intégration par intégration, consulter la **santé** d’une intégration et voir, sur la page Stockage, quelles tables et quelles entités occupent la base de données.

![Le dialogue unique « Ajouter un appareil ou une intégration ». © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/add-device-or-integration.webp)

![Suivre le démarrage de Home Assistant en direct, intégration par intégration. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/startup-details.webp)

![L’élément « Santé » d’une intégration : entités, réparations, erreurs du journal. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/integration-health.webp)

![La carte Base de données de la page Stockage : quelles tables et quelles entités prennent de la place. © Home Assistant / Nabu Casa](https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/images/database-usage.webp)

- 🧩 Les notes annoncent **16 nouvelles intégrations**, parmi lesquelles Electrolux (aussi pour AEG et Frigidaire), E3/DC, Powersensor, Tile BLE, Intesis Modbus, Trimlight et plusieurs commandes infrarouges. **Bambu Lab a été retirée dès la b1.** Parmi les améliorations, l’intégration **Freebox** officielle peut désormais piloter les **volets roulants** appairés à une Freebox Delta ou Freebox Home, et affiche le trafic de ses ports LAN. Deux intégrations sont retirées : **Crownstone** (service cloud fermé) et **Fitbit** (l’API Web a été arrêtée par Google le 2 novembre 2026).

## ⚠️ Changements cassants

Les notes en dressent une longue liste. Voici ceux qui méritent le plus d’attention :

- **Météo-France** : l’état du capteur d’alerte, jusqu’ici toujours en français (`Vert`, `Jaune`, `Orange`, `Rouge`), devient `green`, `yellow`, `orange` ou `red`, et s’affiche dans votre langue dans l’interface. Il faut mettre à jour les automatisations, scripts et templates qui testent cet état.
- **Matter** et **Zigbee (ZHA)** : les prises multiples et les interrupteurs multi-canaux deviennent des appareils enfants. Les identifiants d’entité restent les mêmes, mais les noms affichés (`friendly_name`) changent. Les volets Matter de type volet roulant prennent la classe *shutter*.
- **Z-Wave** : plusieurs modules de volets prennent la classe de ce qu’ils pilotent (volet, store, portail…) au lieu de *window*. Il faut aussi **zwave-js-server 3.12.0** ou plus (app Z-Wave JS en version 1.11.0 au minimum).
- L’app communautaire **Home Assistant Matter Hub** doit être en version **2.1.0** ou plus, sinon elle n’est plus ouvrable depuis la barre latérale.

Pour les intégrations personnalisées, un flux de configuration qui renvoie un type de résultat en texte simple (`"form"`, `"abort"`) au lieu de l’énumération `FlowResultType` échoue désormais avec une erreur `TypeError`. Les notes de la bêta et le blog des contributeurs ne signalent rien de spécifique à mes intégrations HACS (freebox_homexa, freesmsxa, jourferier, chauffage, phase_lune, saintdujour, piscinexa, date_countdown et starship_tracker) : je les vérifierai comme d’habitude avant la version stable.

> **💬 Mon avis**
>
> Sur le papier, cette dernière bêta de l’année est réjouissante : des volets enfin pensés comme des volets, des boutons qui gèrent le double appui, et, de notre côté, des **volets Freebox** pilotables. Je garderai surtout un œil sur le changement de l’alerte Météo-France, qui peut casser une automatisation si on ne le voit pas venir.

— XAV59213

L’article, avec les sources officielles, est aussi sur la vitrine : https://xav59213.github.io/forumdomotique/actualite-ha-dev/home-assistant-2026-12-beta/
