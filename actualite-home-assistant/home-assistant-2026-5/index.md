---
layout: ha-release
title: "Home Assistant 2026.5 : la radiofréquence arrive, Téléinfo lit votre Linky et un tableau Maintenance surveille vos piles"
short_title: "2026.5 : radiofréquence et Téléinfo Linky"
description: "Home Assistant 2026.5 (6 mai 2026) en français : plateforme radiofréquence (RF), ports série via ESPHome, tableau Maintenance des batteries, carte Raccourci, durées dans les déclencheurs, intégration Teleinfo pour le Linky et breaking changes."
excerpt_fr: "Volets, portails et prises RF entrent dans Home Assistant, les ports série passent par le réseau, un tableau Maintenance traque les piles faibles… et l’intégration Teleinfo lit enfin le Linky en local."
image: /actualite-home-assistant/home-assistant-2026-5/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.5, mai 2026"
date: 2026-05-06
release_date: 2026-05-06
section: actualite-ha
version: "2026.5"
month: "Mai 2026"
official_title: "2026.5: We're on the same frequency now 📡"
release_url: https://www.home-assistant.io/blog/2026/05/06/release-20265/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.5/
tags: [home-assistant, mise-a-jour, 2026.5]
seo:
  type: NewsArticle
gallery:
  - src: images/rf-config-flow.webp
    caption: "Configuration d’un appareil radiofréquence : on choisit l’émetteur RF à utiliser."
  - src: images/rf-device.webp
    caption: "Un appareil piloté en radiofréquence, avec ses commandes dans Home Assistant."
  - src: images/serial-proxy-picker.webp
    caption: "Le nouveau sélecteur de port série : ports USB locaux et ports distants ESPHome."
  - src: images/maintenance-dashboard.webp
    caption: "Le nouveau tableau Maintenance : toutes les batteries, regroupées par pièce."
  - src: images/security-activity-log.webp
    caption: "Le tableau Sécurité et sa nouvelle colonne Activité sur 24 heures."
  - src: images/shortcut-card.webp
    caption: "La carte Raccourci : naviguer, ouvrir une URL, lancer Assist ou une action."
  - src: images/media-player-features.webp
    caption: "Les nouvelles fonctionnalités des tuiles de lecteurs multimédias : source et boutons de lecture."
  - src: images/purpose-specific-trigger-duration.webp
    caption: "Le nouveau champ « pendant » (for) dans les déclencheurs par usage."
  - src: images/vacuum-more-info.webp
    caption: "La fenêtre de détails redessinée des aspirateurs, avec animations selon l’état."
  - src: images/template-autocomplete-functions.webp
    caption: "L’autocomplétion des fonctions dans l’éditeur de templates."
---

La **2026.5** est sortie le **6 mai 2026**, quelques semaines après le **State of the Open Home 2026** à Utrecht. Grande nouvelle de transparence au passage : la **feuille de route de Home Assistant est désormais publique** et ouverte aux commentaires. Côté logiciel, après l’infrarouge le mois dernier, c’est au tour de la **radiofréquence (RF)** de devenir native. Et pour nous, Français, une nouveauté attendue : l’intégration **Teleinfo** pour lire le **Linky** en local 🇫🇷.

<div class="ha-callout info" markdown="1">
**En bref**
- 📡 **Radiofréquence** : volets, guirlandes, hottes… pilotés via ESPHome ou un Broadlink RM4 Pro.
- 🔌 **Ports série via le réseau** grâce au proxy série d’ESPHome.
- 🔋 Nouveau tableau **Maintenance** pour surveiller toutes vos batteries.
- ⏱️ Les déclencheurs par usage comprennent enfin les **durées** (« ouvert depuis 2 minutes »).
- 🇫🇷 **Teleinfo** : consommation du Linky et des anciens compteurs électroniques, en local.
</div>

## ✨ Les nouveautés phares

### 📡 La radiofréquence rejoint l’infrarouge

Volets et rideaux motorisés, portails, ventilateurs de plafond, interrupteurs sans fil, prises RF, sonnettes, guirlandes… beaucoup d’appareils RF n’avaient aucune porte d’entrée propre vers la maison connectée. La nouvelle plateforme **Radio frequency** suit exactement le modèle de l’infrarouge : une entité représente un **émetteur RF**, que des intégrations spécifiques utilisent.

{% include ha-figure.html src="images/rf-config-flow.webp" caption="On choisit l’émetteur radiofréquence lors de l’ajout d’un appareil." %}

Deux émetteurs sont pris en charge dès le départ :
- **ESPHome**, avec un émetteur sub-GHz compatible ;
- **Broadlink**, avec le **RM4 Pro** (seul modèle de la gamme concerné).

Et deux premières intégrations d’appareils : **Honeywell String Lights** (guirlandes) et **Novy Cooker Hood** (lumière et extraction des hottes Novy, souvent installées au plafond).

🌱 Même philosophie que l’infrarouge : plutôt que de jeter un volet roulant « bête » qui fonctionne, on l’intègre.

### 🔌 Des ports série… par le réseau

Compteur avec port **P1**, ampli **RS-232**… beaucoup d’appareils parlent en série. Avec le **proxy série** d’ESPHome, un port série branché sur un ESP devient utilisable par Home Assistant **comme s’il était branché sur le serveur**.

{% include ha-figure.html src="images/serial-proxy-picker.webp" caption="Le sélecteur de port série liste les ports USB locaux et les ports distants ESPHome." %}

Sous le capot, tout Home Assistant passe à **serialx**, un pilote série moderne et asynchrone qui remplace `pyserial`. ⚠️ Soyons francs, comme l’équipe : ce n’est **pas encore du « en un clic »**. Il faut construire son propre appareil ESPHome avec le composant `serial_proxy` configuré sur le bon UART. C’est la fondation, la simplicité viendra ensuite.

### 🔋 Le tableau Maintenance : fini les piles mortes surprises

Le capteur de mouvement du couloir qui ne déclenche plus la lumière… parce que sa pile est vide depuis des jours. Le nouveau tableau intégré **Maintenance** (une contribution de @Brookke) **découvre automatiquement toutes les entités batterie** les regroupe **par pièce** et met en évidence celles qui faiblissent, pour savoir d’un coup d’œil quelle pile changer.

{% include ha-figure.html src="images/maintenance-dashboard.webp" caption="Le tableau Maintenance regroupe vos batteries par pièce et signale les plus faibles." %}

Le tableau **Sécurité** gagne aussi une colonne **Activité** : un journal en direct des dernières 24 heures (caméras, serrures, alarmes, ouvertures, allées et venues).

### 🎛️ La carte Raccourci et des tuiles multimédia plus riches

Nouvelle carte **Raccourci** (*shortcut*) : elle ressemble à une tuile, mais déclenche une action quand on la touche :
- **naviguer** vers un tableau, une vue, une pièce ou un appareil ;
- **ouvrir une URL** (box, NAS, documentation) ;
- **lancer Assist** ;
- **exécuter une action** (éteindre toutes les lumières en partant 🌙).

Elle reprend automatiquement le titre, l’icône et la couleur de la destination, et existe aussi en **badge**. Les tuiles de **lecteurs multimédias** gagnent un sélecteur de **source** et un choix (et un ordre) libre des **boutons de lecture**.

### ⏱️ Les automatisations comprennent « pendant un moment » (Labs)

La demande n°1 des testeurs : les **durées**. Un champ **for** (« pendant ») arrive sur la plupart des déclencheurs par usage (mouvement, présence, portes, fenêtres, lumières, climat, volets…) et sur **toutes** les conditions d’entité.

{% include ha-figure.html src="images/purpose-specific-trigger-duration.webp" caption="Le champ de durée d’un déclencheur par usage." %}

Exemples cités par l’équipe :
- « Quand la porte d’entrée est ouverte **depuis plus de 2 minutes** » → rappel de la fermer 🔔 ;
- « Quand aucun mouvement n’a été détecté dans le bureau **depuis 15 minutes** » → extinction des lumières 💡 ;
- « Si la fenêtre de la chambre est fermée **depuis au moins une heure** » → démarrer le purificateur.

Nouveaux blocs aussi pour les **mises à jour**, les **lecteurs multimédias** (muet, volume…), les **minuteurs** (démarré, en pause, terminé…), les **listes de tâches** et un déclencheur universel **sonnette** (*doorbell rang*).

## 🧩 Nouvelles intégrations

✅ Douze ajouts, dont :

- 🇫🇷 **Teleinfo** : lecture des données des compteurs **Linky** et des anciens compteurs électroniques via la sortie **TIC** (Télé-Information Client), avec un adaptateur USB Teleinfo. Index, puissance apparente, intensité instantanée et tarif, **en local**. Lancée au niveau **argent**.
- **Fumis** : poêles et chaudières à granulés équipés du module Fumis WiRCU (vendus sous les marques Austroflamm, EcoSpar, HAAS+SOHN ou Heta), lancée en **platine**.
- **Eurotronic Comet Blue** : têtes thermostatiques Bluetooth.
- **Duco** (ventilation, platine), **Victron GX** (énergie, platine), **EARN-E P1**, **Denon RS-232**, **OMIE** (prix de l’électricité ibériques), **Kiosker**, **Honeywell String Lights**, **Novy Cooker Hood** et la plateforme **Radio frequency**.

**PJLink** et **Pico TTS** passent en configuration par l’interface ; **LANnouncer** est retiré.

## 🔧 Améliorations notables

- **Notifications de l’appli mobile = entités** : on peut grouper téléphones et tablettes avec un groupe classique et notifier tout le monde d’un coup, sans YAML.
- **Fenêtres de détails** des **aspirateurs** et **tondeuses** redessinées, avec animations et une vue **Clean by area**.
- **Documentation des templates** entièrement réécrite (14 pages d’apprentissage, 2 tutoriels, plus de 200 fonctions documentées) et **autocomplétion** dans l’éditeur de code (fonctions, entités, appareils, pièces, étages, étiquettes).
- Conditions de visibilité des cartes basées sur **la propre entité de la carte** ou sur un **attribut** ; recherche dans la page d’une intégration ; rechargement des `shell_command` sans redémarrer.
- **MQTT** : entités heure, date et date-heure ; **Matter** : capteurs de radon ; **Broadlink** : émetteur infrarouge ; **Sonos**, **Apple TV**, **Music Assistant**, **Shelly**, **WLED**…

## ⚠️ Breaking changes à surveiller

- **Déclencheurs par usage (Labs)** : les blocs *entered home*, *left home*, *is home* et *is not home* sont **retirés** des personnes et suivis d’appareils. En attendant leurs remplaçants multi-domaines, repassez sur un déclencheur/condition d’état classique (état = `home`).
- **Supervisor** : les actions `hassio.*` (par ex. `hassio.addon_start`, `hassio.backup_partial`) **lèvent désormais une erreur** en cas d’échec et stoppent l’automatisation. Ajoutez `continue_on_error: true` si besoin.
- **Ring** : l’évènement de sonnette s’appelle `ring` (et non plus `ding`).
- **pilight** désactivé ; **Webhook** : `local_only` doit être un vrai booléen ; **Gardena Bluetooth** : « fin d’arrosage » devient un capteur horodaté.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.5**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-5" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète** (Paramètres › Système › Sauvegardes).
2. Si vous lancez des sauvegardes ou des Apps par automatisation (`hassio.*`), vérifiez le comportement en cas d’erreur.
3. Si vous testiez les blocs « arrivée/départ de la maison » de Labs, remplacez-les avant la mise à jour.

<div class="ha-avis" markdown="1">
### 💬 L’avis de Xavier

Pour un domoticien français, **Teleinfo** est la nouveauté du mois : lire son Linky en local, sans cloud, directement dans le cœur de Home Assistant, c’est un vrai pas en avant pour le suivi de consommation. La radiofréquence ouvre la porte à nos volets et portails RF, et le tableau Maintenance évitera bien des pannes « mystères ». Le proxy série demande encore des mains de bricoleur, mais la base est posée.
</div>

Vous lisez déjà votre Linky dans Home Assistant ? Comparez vos montages sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— Xavier (XAV59213)</p>
