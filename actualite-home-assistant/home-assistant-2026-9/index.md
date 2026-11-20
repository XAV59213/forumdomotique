---
layout: ha-release
title: "Home Assistant 2026.9 : Modbus se modernise, l’Activité explique le « pourquoi » et la carte du réseau Matter arrive"
short_title: "2026.9 : Modbus, Matter et le pourquoi des choses"
description: "Home Assistant 2026.9 (2 septembre 2026) en français : Modbus configurable par intégration, nouvelle reconnaissance vocale Cloud à tester, alertes et favoris du tableau Sécurité, panneau Sources, détails « pourquoi » dans l’Activité, carte du réseau Matter, heure dorée et heure bleue, et breaking changes."
excerpt_fr: "Les appareils Modbus se choisissent enfin dans l’interface, l’Activité raconte pourquoi une lumière s’est allumée, Matter affiche sa carte réseau et le soleil gagne l’heure dorée et l’heure bleue."
image: /actualite-home-assistant/home-assistant-2026-9/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.9, septembre 2026"
date: 2026-09-02
release_date: 2026-09-02
section: actualite-ha
version: "2026.9"
month: "Septembre 2026"
official_title: "2026.9: There's room on this bus"
release_url: https://www.home-assistant.io/blog/2026/09/02/release-20269/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.9/
tags: [home-assistant, mise-a-jour, 2026.9]
seo:
  type: NewsArticle
gallery:
  - src: images/security-dashboard-favorites.webp
    caption: "L’éditeur du tableau Sécurité : entités favorites et alertes actives."
  - src: images/history-filtering.webp
    caption: "Le nouveau panneau Sources de l’Historique, pour choisir pièces, appareils ou entités."
  - src: images/activity-filtering.webp
    caption: "Le même panneau Sources pour filtrer l’Activité."
  - src: images/activity-details.webp
    caption: "Les détails d’une ligne d’Activité : ce qui a déclenché le changement, étape par étape."
  - src: images/matter-network-graph.webp
    caption: "La carte du réseau Matter, avec les routeurs Thread et les appareils."
  - src: images/tile-card-feature-light-effect.webp
    caption: "Choisir un effet lumineux directement depuis une tuile."
  - src: images/tile-card-feature-vacuum-fan-speed.webp
    caption: "La puissance d’aspiration d’un robot réglable depuis la tuile."
  - src: images/serial-panel.webp
    caption: "Le nouveau panneau Série dans Paramètres › Connectivité."
  - src: images/network-storage-space.webp
    caption: "L’espace utilisé sur chaque stockage réseau, sur la page Stockage."
  - src: images/cloud-signup.webp
    caption: "La nouvelle page d’accueil de l’inscription à Home Assistant Cloud."
---

Frenck l’avoue d’emblée : **Modbus** n’a jamais été la partie la plus glamour de Home Assistant. Il fait pourtant tourner onduleurs solaires, pompes à chaleur et compteurs… à condition d’écrire soi-même la carte des registres. La **2026.9**, sortie le **2 septembre 2026**, pose les bases d’une autre approche. Elle apporte aussi une **nouvelle reconnaissance vocale Cloud** à tester, des **alertes actives** dans le tableau Sécurité, une **Activité qui explique pourquoi** les choses arrivent et la **carte du réseau Matter**.

<div class="ha-callout info" markdown="1">
**En bref**
- 🔌 **Modbus** : des intégrations qui connaissent déjà votre appareil (Fronius pour commencer).
- 🎙️ Nouveau moteur de **reconnaissance vocale Cloud** (Soniox) à tester dans Labs, meilleur sur les accents et les langues autres que l’anglais.
- 🛡️ Tableau **Sécurité** : **alertes actives** et **favoris**.
- 🔍 Panneau **Sources** commun à l’Historique et à l’Activité, et détails « **pourquoi** » sur chaque ligne d’Activité.
- 🗺️ **Carte du réseau Matter** ; 🌅 heure dorée, heure bleue, soleil de minuit et nuit polaire.
</div>

## ✨ Les nouveautés phares

### 🔌 Modbus, version moderne

Jusqu’ici, l’intégration **Modbus** (YAML) obligeait chacun à comprendre le protocole de son appareil. Elle reste disponible, mais une nouvelle voie s’ouvre : des **intégrations qui savent déjà comment parle un appareil**, que l’on choisit dans l’interface comme n’importe quelle autre. Premier exemple : **Fronius** gagne une prise en charge optionnelle de **Modbus TCP (SunSpec)**, avec des données par chaîne de panneaux (courant, tension, puissance, énergie cumulée). Côté nouvelles intégrations, **Sofar Inverter Modbus** relie aussi les onduleurs Sofar en Modbus TCP. Sous le capot, cette nouvelle approche repose sur une bibliothèque de connexion dédiée et sur **tmodbus**, une bibliothèque Modbus moderne.

### 🎙️ Testez la nouvelle reconnaissance vocale du Cloud

Nabu Casa teste un nouveau moteur de **reconnaissance vocale** pour Home Assistant Cloud, basé sur le fournisseur **Soniox**. Il progresse nettement sur les trois écueils classiques : **accents, bruit de fond et langues autres que l’anglais** (bonne nouvelle pour nous !). Mêmes garanties de confidentialité : pas de journalisation ni de stockage.

**Pour l’essayer :** abonné Cloud, ouvrez **Paramètres › Système › Labs** et activez le nouveau traitement vocal. Pas encore abonné ? Un essai de 31 jours est proposé.

Autres progrès Cloud : la **vraie adresse IP** des tentatives de connexion passant par le Cloud est désormais visible (fini les « 127.0.0.1 invalid login attempt »), ce qui permet aussi de **bannir une IP** ; et l’inscription commence par une page plus claire (**Start your free trial** / **Sign in**).

### 🛡️ Alertes actives et favoris pour le tableau Sécurité

- La section **Active alerts** n’apparaît que lorsque quelque chose demande votre attention (porte restée ouverte, détecteur de fumée qui sonne…). Vous choisissez les entités surveillées.
- La section **Favorites** épingle les entités que vous consultez le plus (portes, serrures, capteurs importants).

{% include ha-figure.html src="images/security-dashboard-favorites.webp" caption="Favoris et alertes actives se règlent dans le même éditeur du tableau Sécurité." %}

### 🔍 Historique et Activité : un panneau Sources… et le « pourquoi »

**Historique** et **Activité** partagent un panneau **Sources** à gauche pour choisir pièces, appareils ou entités. Le sélecteur de dates devient une pilule avec flèches précédent/suivant.

Surtout, **un clic sur une ligne d’Activité ouvre ses détails** : ce qui a tout déclenché (une personne, un changement d’état, un horaire, une intégration…), puis l’enchaînement jusqu’au changement observé.

{% include ha-figure.html src="images/activity-details.webp" caption="Pourquoi cette lumière s’est-elle allumée ? La réponse, de haut en bas." %}

### 🗺️ Le réseau Matter enfin visible

Comme pour Zigbee (ZHA), Z-Wave et Bluetooth, le panneau **Matter** a un bouton **Show map** qui affiche le graphe du réseau (Home Assistant, routeurs Thread, appareils). Si votre serveur Matter est trop ancien, la page vous le dit au lieu d’échouer en silence.

{% include ha-figure.html src="images/matter-network-graph.webp" caption="La carte du réseau Matter / Thread." %}

### 🌅 Heure dorée, heure bleue et soleil polaire

La refonte des automatisations solaires se termine : après les déclencheurs dédiés de la 2026.7 (lever, coucher, midi et minuit solaires, aube, crépuscule, élévation), l’intégration **Sun** ajoute **quatre conditions et huit déclencheurs** pour l’**heure dorée**, l’**heure bleue**, le **soleil de minuit** et la **nuit polaire**. Idéal pour une ambiance lumineuse qui suit vraiment la lumière du jour.

### 🎛️ Nouvelles fonctionnalités de tuiles

**Effet lumineux** pour les lumières, **puissance d’aspiration** pour les robots, et **humidité cible** étendue aux thermostats. En position **Inline**, toutes les fonctionnalités s’affichent désormais (et plus seulement la première).

### ♿ Des graphiques accessibles

Les graphiques deviennent navigables au **clavier** et lisibles par les **lecteurs d’écran** : les flèches parcourent les points, une zone annonce la date et la valeur, et une **tonalité** monte et descend avec les données (graphiques en lignes et barres, y compris la répartition par appareil du tableau Énergie).

## 🧩 Nouvelles intégrations

✅ Treize ajouts, dont :

- **Sofar Inverter Modbus** (onduleurs solaires, Modbus TCP) ; **Besen**, **NexBlue** et **Silla Prism** (bornes de recharge).
- **ISEO Argo BLE** (serrures, courantes sur les portes blindées en Italie et en Suisse), **Hot Spring** (spas, platine), **Flow-it** (ventilation).
- **Collection image** (une image aléatoire tirée d’un dossier multimédia), **LibreNMS**, **Ridder HortiMaX Pro** (serres), **Samsung TV via ExLink**, **Specialized Turbo** (vélos électriques), **Tonewinner**.
- Quinze **intégrations virtuelles** gérées par Midea, dont **Ariston**, **Carrier**, **Comfee**, **Olimpia Splendid** et **Toshiba Lifestyle**.

**Flexit**, **Netio** et **Remember The Milk** passent par l’interface ; **VLC** est retiré.

## 🔧 Améliorations notables

- Nouvelle page **Paramètres › Connectivité** qui regroupe Matter, Zigbee, Z-Wave, KNX, MQTT, Thread, Bluetooth, Série, Infrarouge, Radiofréquence… avec des panneaux **Série** et **MQTT** dédiés.
- Page **Stockage** : barre d’occupation de chaque partage réseau.
- **Shelly** : caméras ; **Reolink**, **Roborock**, **Tado** (choix du circuit de chauffage), **LG webOS** (écran éteint, son allumé), **Home Connect**, **Google Gemini**…
- **Templates** : attributs personnalisés sur de nombreuses plateformes, `conditions` par entité déclenchée ; actions de volets avec **vitesse** ; la boîte de redémarrage liste les automatisations en cours ; arrière-plan de dashboard réglable dans l’interface.

## ⚠️ Breaking changes à surveiller

- **Mises à jour** : installer, ignorer ou réafficher une mise à jour exige un **compte administrateur**. Les automatisations ne sont pas concernées, mais un script lancé par un non-admin échouera.
- **Outils LLM** : les noms sont préfixés par le domaine (`GetLiveContext` → `homeassistant__GetLiveContext`, `HassTurnOn` → `intent__HassTurnOn`). Mettez à jour vos prompts personnalisés.
- **Notifications persistantes** : une mise à jour déclenche `update_type: updated` (et non plus `added`).
- **KNX** : les *exposes* n’envoient plus la première valeur au bus ; **UniFi Protect** 7.2.105 minimum ; **Z-Wave JS** : actions de gestion des utilisateurs de serrure modifiées ; **Vacuum** : `battery_level` supprimé de l’entité de base ; **Flexit Nordic** : interrupteur cheminée supprimé.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.9**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-9" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète.**
2. Si un membre non-admin du foyer déclenche un script qui installe des mises à jour, revoyez ce script.
3. Si vous avez écrit un prompt LLM qui cite des outils par leur nom, ajoutez les nouveaux préfixes.

<div class="ha-avis" markdown="1">
### 💬 Mon avis

Deux nouveautés me semblent particulièrement utiles au quotidien : les **détails « pourquoi »** de l’Activité (fini les enquêtes pour comprendre une lumière qui s’allume seule) et la **carte du réseau Matter**, indispensable pour diagnostiquer un réseau Thread. Pour les francophones, la nouvelle reconnaissance vocale Cloud mérite clairement un test, puisqu’elle cible justement les langues autres que l’anglais.
</div>

Vous avez testé la nouvelle reconnaissance vocale ? Donnez votre avis sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— XAV59213</p>
