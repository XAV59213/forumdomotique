---
layout: ha-release
title: "Home Assistant 2026.8 : adieu le « :8123 », bonjour les Outils pour tous et le déclencheur Lune"
short_title: "2026.8 : plus accessible que jamais"
description: "Home Assistant 2026.8 (5 août 2026) en français : adresse sans :8123 pour les nouvelles installations, réglages du serveur web dans l’interface, fin du vocabulaire « avancé », Developer Tools devient Tools, Cloud repensé, identifiants d’entité personnalisables, déclencheur Lune et breaking changes."
excerpt_fr: "Une version placée sous le signe de l’accessibilité : plus de :8123 à retenir pour les nouvelles installations, plus de « mode expert », un Cloud guidé pas à pas… et un déclencheur sur les phases de la Lune."
image: /actualite-home-assistant/home-assistant-2026-8/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.8, août 2026"
date: 2026-08-05
release_date: 2026-08-05
section: actualite-ha
version: "2026.8"
month: "Août 2026"
official_title: "2026.8: Approachable by design"
release_url: https://www.home-assistant.io/blog/2026/08/05/release-20268/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.8/
tags: [home-assistant, mise-a-jour, 2026.8]
seo:
  type: NewsArticle
gallery:
  - src: images/web-server-settings.webp
    caption: "Les réglages du serveur web dans l’interface : port, interface réseau d’écoute et proxys de confiance."
  - src: images/web-server-revert.webp
    caption: "Après un changement de port, Home Assistant demande confirmation et revient en arrière si besoin."
  - src: images/cloud_page_top.webp
    caption: "La page Home Assistant Cloud repensée : chaque service a son espace."
  - src: images/cloud_page_bottom.webp
    caption: "Le bas de la page Cloud, avec la configuration guidée."
  - src: images/entity-id-rename.gif
    caption: "Renommer un identifiant d’entité et choisir l’ordre de ses éléments (animation)."
  - src: images/favorite-cards.webp
    caption: "Marquer ses cartes préférées dans l’onglet « By Card » du sélecteur."
  - src: images/zwave-access-control.webp
    caption: "Le nouvel onglet Access Control de Z-Wave JS UI : utilisateurs, identifiants et historique."
---

Frenck en vacances bien méritées, c’est **Ashley Abbott** (responsable de programme technique à l’Open Home Foundation) qui présente la **2026.8**, sortie le **5 août 2026**, avec Bram. Le fil rouge est assumé : **rendre Home Assistant utilisable sans être technicien**, sans rien sacrifier en puissance. Au menu : la fin du « :8123 » pour les nouvelles installations, la disparition du vocabulaire « avancé », un Cloud plus simple à découvrir… et, pour les amateurs de ciel, un **déclencheur sur les phases de la Lune** 🌙.

<div class="ha-callout info" markdown="1">
**En bref**
- 🌐 Nouvelles installations Home Assistant OS : **plus de numéro de port** à ajouter à l’adresse.
- ⚙️ Port, interface d’écoute et proxys de confiance réglables **depuis l’interface**.
- 🧰 **Developer Tools** devient simplement **Tools** ; « avancé » et « expert » disparaissent (environ 43 endroits).
- ☁️ Page **Home Assistant Cloud** repensée avec configuration guidée.
- 🏷️ **Identifiants d’entité** renommables et ordonnables à votre façon.
</div>

## ✨ Les nouveautés phares

### 🌐 Adieu le « :8123 »

Depuis toujours, joindre Home Assistant voulait dire penser à ajouter **`:8123`** à l’adresse. Les **nouvelles installations de Home Assistant OS** utilisent désormais une adresse web normale, **sans numéro à la fin** : on accède à sa maison comme à n’importe quel site.

✅ **Vous avez déjà une installation ? Rien ne change**, et il n’y a rien à faire.

**Changer le port vous-même, pas à pas :**
1. Ouvrez les **réglages du serveur web** dans l’interface (port, interface réseau d’écoute, proxys de confiance).
2. Modifiez le port et validez.
3. Home Assistant applique la nouvelle configuration puis **demande de confirmer** : sans confirmation, il revient automatiquement à l’ancienne. Impossible de rester bloqué dehors.

{% include ha-figure.html src="images/web-server-settings.webp" caption="Les réglages du serveur web, désormais dans l’interface." %}

⚠️ Pensez ensuite à mettre à jour ce qui utilise l’ancienne adresse : favoris, applications et services connectés. Si vous configuriez le serveur web en **YAML**, vos réglages sont **importés automatiquement** dans l’interface au premier démarrage (une réparation vous le signale) ; rien ne casse.

### 🧰 Moins d’« avancé », plus d’accessible

Des mots comme *advanced* ou *expert* laissaient entendre que certaines fonctions n’étaient « pas pour vous ». Ils ont été retirés à **environ 43 endroits** (application, documentation, applis mobiles) : les fonctions n’ont pas changé, leur description dit simplement ce qu’elles font. Dans le même esprit, **Developer Tools devient Tools**.

### ☁️ Home Assistant Cloud plus facile à explorer

La page **Home Assistant Cloud** (Nabu Casa) devient une vue d’ensemble claire : accès à distance, sauvegardes, assistants vocaux, application… chaque service a son espace. Surtout, une **configuration guidée** accompagne pas à pas ceux qui débutent.

{% include ha-figure.html src="images/cloud_page_top.webp" caption="La nouvelle page Cloud, organisée par service." %}

### 🏷️ Vos identifiants d’entité, à votre façon

Après des essais de génération automatique à partir de la pièce, qui ne convenaient pas à tout le monde, Home Assistant vous laisse la main : vous pouvez **renommer un identifiant d’entité** vous-même et **choisir l’ordre de ses éléments**, pour suivre la convention de nommage qui vous parle.

### 🔧 Une gestion des appareils plus propre

Quand un même appareil physique était configuré via **deux intégrations**, Home Assistant les fusionnait en un seul appareil, et certaines infos uniques (modèle, numéro de série) entraient en conflit. Désormais, **chaque intégration garde sa propre fiche** ; les appareils fusionnés sont séparés automatiquement à la mise à jour, et vos automatisations et scripts continuent de fonctionner.

### 🌙 La Lune et les vibrations entrent dans les automatisations

- **Lune** : un déclencheur quand la Lune **entre dans une nouvelle phase** (pleine lune, nouvelle lune ou tout changement) et des conditions sur la phase en cours. Ambiance lumineuse, rappel… ou simple clin d’œil.
- **Vibration** : des conditions viennent compléter les déclencheurs existants.

## 🧩 Nouvelles intégrations

✅ Quinze ajouts, dont :

- 🏊 **NeoPool** : contrôleurs de piscine NeoPool (Sugar Valley, vendus notamment sous les marques Hidrolife, Aquarite et Oxilife), **en local via Modbus TCP** : chimie de l’eau, filtration, électrolyse. Lancée en **argent**.
- **Midea** : climatiseurs et purificateurs utilisant le protocole Midea.
- **llama.cpp** et **LiteLLM** : agents conversationnels sur serveur local ou proxy compatible OpenAI.
- **Google Health** (données Google Health / Fitbit), **Harbor Sleep** (babyphone), **Gatus** (supervision), **Karakeep** (favoris auto-hébergés).
- **Dyson Infrared**, **LED Infrared**, **Harman Luxury Audio**, **Lyngdorf**, **GeoSphere Austria Warnings**, **Fuelprices.dk**, **ScorpionTrack**.

**AquaLogic** et **OpenWrt (luci)** se configurent dans l’interface. **Permobil** et **Volvo On Call** sont retirés.

## 🔧 Améliorations notables

- 🇫🇷 **Overkiz** : capteurs fenêtre/inclinaison, réglages *boost* et durée de séchage des **sèche-serviettes électriques Atlantic**, et prise en charge du **Somfy Thermostat PRO**.
- **Shelly** : mode **Enhanced Security** (HTTPS uniquement, firmware 2.0) ; **Reolink** : pré-sirène ; **MQTT** : plateforme infrarouge ; **KNX**, **Enphase Envoy**, **MELCloud**, **Roborock Q10**…
- **Tableau Énergie** : capacité par batterie pour un niveau de charge combiné **pondéré**.
- **Recherche dans le navigateur multimédia** (Immich trouve les photos par leur contenu), **cartes favorites** dans le sélecteur, éditeur de templates plus spacieux.
- **Z-Wave JS 1.6.0** : nouvel onglet **Access Control** (plusieurs identifiants par utilisateur, PIN + empreinte, historique).
- Assist depuis la recherche rapide, date sur la carte horloge, export CSV de l’Activité, classe d’appareil **radon**, templates encore plus rapides.

## ⚠️ Breaking changes à surveiller

- **Aspirateurs** : la propriété dépréciée `battery_level` disparaît (LG ThinQ, Neato, Romy, Shark IQ, SwitchBot Cloud, Template, TP-Link, Xiaomi Miio).
- **UniFi Protect** : version **7.1** minimum, appareils AI Port et scores de détection retirés.
- **Paperless-ngx** : serveur plus récent requis ; **Ohme** : capteur d’énergie supprimé ; **Edifier Infrared** : codes corrigés pour R2000DB/R2730DB.
- **AirNow**, **Gardena Bluetooth**, **ScreenLogic** : ajustements.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.8**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-8" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète.**
2. Installation existante : **ne changez pas de port** sans avoir listé ce qui pointe vers `:8123` (applis mobiles, reverse proxy, intégrations tierces).
3. Si vous utilisiez `battery_level` d’un aspirateur dans un template, basculez sur l’entité batterie dédiée.

<div class="ha-avis" markdown="1">
### 💬 Mon avis

Une version qui ne fait pas de bruit mais qui compte : retirer le « :8123 » et les mots « avancé » ou « expert », c’est enlever des barrières pour tous ceux qui hésitent à se lancer. Côté France, les améliorations **Overkiz** pour les sèche-serviettes Atlantic et le thermostat Somfy sont bienvenues. Et en tant qu’auteur de l’intégration **Phase de la Lune**, je ne peux que saluer l’arrivée d’un déclencheur lunaire natif 🌕 : les deux approches se complètent très bien.
</div>

Vous avez profité de la nouvelle adresse sans port ? Dites-le nous sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— XAV59213</p>
