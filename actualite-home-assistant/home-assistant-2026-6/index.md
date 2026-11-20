---
layout: ha-release
title: "Home Assistant 2026.6 : un sélecteur de cartes qui part de vos appareils et un éditeur d’automatisations qui teste en direct"
short_title: "2026.6 : choisissez un appareil, pas une carte"
description: "Home Assistant 2026.6 (3 juin 2026) en français : nouveau sélecteur de cartes « par entité », infrarouge en réception, conditions testées en direct, notes dans les automatisations, prévisions météo sur les tuiles, codes des serrures Z-Wave, page Apps repensée et breaking changes."
excerpt_fr: "On ajoute une carte en partant de l’appareil, l’éditeur d’automatisations montre en direct quelles conditions passent, l’infrarouge apprend à écouter et les serrures Z-Wave se gèrent comme les Matter."
image: /actualite-home-assistant/home-assistant-2026-6/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.6, juin 2026"
date: 2026-06-03
release_date: 2026-06-03
section: actualite-ha
version: "2026.6"
month: "Juin 2026"
official_title: "2026.6: Pick a card, any card"
release_url: https://www.home-assistant.io/blog/2026/06/03/release-20266/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.6/
tags: [home-assistant, mise-a-jour, 2026.6]
seo:
  type: NewsArticle
gallery:
  - src: images/new-card-picker.webp
    caption: "Le nouveau sélecteur de cartes : l’arborescence de la maison à gauche, des aperçus en direct à droite."
  - src: images/automation-condition-live-test.webp
    caption: "Chaque condition affiche en direct si elle est remplie (badge vert) ou non (badge rouge)."
  - src: images/target-row-count.webp
    caption: "Le nombre d’entités ciblées s’affiche à côté de chaque pièce, étage, appareil ou étiquette."
  - src: images/automation-item-note.webp
    caption: "Une note attachée à un déclencheur pour expliquer pourquoi il existe."
  - src: images/tile-weather-forecast.webp
    caption: "Les prévisions de température et de précipitations directement sur la tuile météo."
  - src: images/tile-media-player.webp
    caption: "La tuile de lecteur multimédia avec muet, aléatoire, répétition et volume."
  - src: images/zwave-credential-management.webp
    caption: "Gestion des accès d’une serrure Z-Wave depuis la page de l’appareil."
  - src: images/apps-panel-refresh.webp
    caption: "La page Apps repensée : une carte par App installée, avec son état."
  - src: images/battery-state-of-charge.webp
    caption: "Le niveau de charge de la batterie domestique affiché dans le tableau Énergie."
  - src: images/yaml-linting.webp
    caption: "Les erreurs de syntaxe YAML soulignées directement dans les éditeurs."
---

« Je ne suis *pas* quelqu’un de dashboards » : c’est Frenck qui le dit, et c’est pourtant le **nouveau sélecteur de cartes** qui est son coup de cœur de la **2026.6**, sortie le **3 juin 2026**. Au lieu de demander « quel type de carte ? », Home Assistant demande désormais « **quel élément de votre maison voulez-vous afficher ?** ». Autour de cette idée, l’éditeur d’automatisations s’enrichit d’indicateurs en direct, l’infrarouge devient bidirectionnel et les serrures Z-Wave rattrapent les Matter.

<div class="ha-callout info" markdown="1">
**En bref**
- 🃏 Nouveau sélecteur de cartes **« par entité »** avec aperçus en direct.
- 📡 L’infrarouge sait maintenant **recevoir** (télécommande d’origine).
- ✅ Conditions **testées en direct**, nombre d’entités ciblées, **notes** sur chaque étape.
- 🌦️ Prévisions météo et télécommande complète sur les **tuiles**.
- 🔐 Gestion des **utilisateurs et codes** des serrures Z-Wave.
</div>

## ✨ Les nouveautés phares

### 🃏 Ajouter une carte en partant de l’appareil

L’ancienne fenêtre d’ajout s’ouvrait sur un mur de types de cartes au nom technique (tuile, entités, glance…). Les études utilisateurs le confirmaient : on ouvre l’éditeur avec un **appareil** ou une **entité** en tête. La fenêtre s’ouvre donc sur un nouvel onglet **By entity**.

{% include ha-figure.html src="images/new-card-picker.webp" caption="À gauche, la maison (étages, pièces, appareils) ; à droite, des aperçus de cartes adaptées à l’entité choisie." %}

**Comment ça marche :**
1. Passez le dashboard en édition et cliquez sur **Ajouter une carte**.
2. Dans l’onglet **By entity**, parcourez vos étages et pièces, puis choisissez une entité.
3. À droite, des **aperçus réels, avec vos données**, s’affichent : pour une lumière, tuile simple, tuile avec curseur de luminosité, température de couleur, couleurs favorites… ; pour un volet, ouverture/fermeture, position, inclinaison ; pour un capteur numérique, une tuile avec courbe de tendance ; pour un calendrier, la carte dédiée.
4. Cliquez sur celle qui vous plaît. L’ancien onglet **By card** reste disponible, ainsi que **Browse all cards**.

Les cartes personnalisées peuvent rejoindre la fête dans une section **Community** (leurs auteurs ajoutent une fonction `getEntitySuggestion`). Sur mobile, le choix se fait en deux étapes.

### 📡 L’infrarouge écoute aussi

Il y a deux versions, Home Assistant pouvait **envoyer** des commandes infrarouges, sans savoir ce que faisait la télécommande d’origine. La plateforme Infrared gagne une **entité évènement de réception** : si quelqu’un utilise la télécommande du téléviseur, Home Assistant le voit et garde un état cohérent. À terme, de futures intégrations pourront aller plus loin, par exemple transformer une télécommande IR inutilisée en télécommande pour Home Assistant. La promesse d’un infrarouge bidirectionnel est tenue.

### ✅ L’éditeur d’automatisations teste en direct

- **Indicateur en direct sur chaque condition** : coche verte si elle est remplie, cercle rouge sinon, état neutre si elle est incomplète, erreur explicite si la configuration est invalide. Le badge se met à jour au fil des changements dans la maison et pendant que vous éditez la condition.
- **Nombre d’entités ciblées** à côté de chaque étage, pièce, appareil et étiquette : « douze lumières, c’est bien ça ».
- **Notes** sur chaque déclencheur, condition et action, pour expliquer *pourquoi* une étape existe. Elles suivent l’automatisation lorsqu’on la duplique, l’exporte ou la partage en blueprint.

{% include ha-figure.html src="images/automation-condition-live-test.webp" caption="Le badge sur l’icône d’une condition indique en temps réel si elle passe." %}

Dans Labs, les remplaçants promis en 2026.5 arrivent : **4 déclencheurs et 4 conditions de zone** (une personne ou un suivi d’appareil *entre* ou *quitte* une zone, est *dans* une zone ou non, zone occupée ou non), compatibles avec la durée **for** et valables pour **n’importe quelle zone** (travail, école…).

### 🌦️ Des tuiles météo et multimédia bien plus riches

- **Prévision des températures** (barres min/max colorées) et **prévision des précipitations** (quantité ou probabilité) directement sur la tuile météo, avec la meilleure résolution disponible (jour, demi-journée, heure).
- La tuile **lecteur multimédia** devient une vraie télécommande : bouton **Muet**, **Aléatoire**, **Répétition**, **Volume +/−**, et un **filtre** sur les listes de sources et de modes sonores.

{% include ha-figure.html src="images/tile-weather-forecast.webp" caption="Les prévisions s’affichent directement sur la tuile météo." %}

### 🔐 Les serrures Z-Wave se gèrent comme les Matter

Depuis la page de la serrure, menu **⋮ › Manage access** : vue d’ensemble des utilisateurs et de leurs identifiants, ajout, modification, suppression. Atout Z-Wave : **codes PIN et mots de passe** sont pris en charge si la serrure le permet. Toutes les opérations existent aussi sous forme d’**actions** pour vos automatisations.

### 📦 Une page Apps plus accueillante

Chaque App installée (anciennement add-on) apparaît sous forme de **carte** avec icône, nom, description et état (en marche, arrêtée, mise à jour disponible), avec de petites **étiquettes** pour s’y retrouver.

## 🧩 Nouvelles intégrations

✅ Seize ajouts, dont trois qui parleront aux Français :

- 🇫🇷 **Data Grand Lyon** : les données ouvertes de la Métropole de Lyon (prochains passages des transports TCL…), lancée en **platine**.
- 🇫🇷 **OVHcloud AI Endpoints** : un agent conversationnel s’appuyant sur les modèles hébergés par OVHcloud.
- 🏊 **Vistapool** : les contrôleurs de piscine de marque **Hayward** (AquaRite, Vistapool…).

Et aussi : **AiDot**, **CentriConnect/MyPropane**, **Cielo Home**, **Guntamatic** (chaudières bois/granulés), **LG TV via Serial**, **Marantz Infrared**, **Samsung Infrared**, **Mitsubishi Comfort**, **Ouman EH-800**, **PAJ GPS**, **PTDevices**, **Xthings Cloud** et **Yoto**.

**Elgato Avea**, **openSenseMap** et **OPNsense** passent en configuration par l’interface ; l’ancienne intégration **Konnected** est retirée.

## 🔧 Améliorations notables

- **Matter** : mise en service plus simple, prise en charge des **sirènes** ; **OpenThread Border Router 1.4** sort de bêta.
- **Reolink** : les caméras sur batterie se connectent **sans Home Hub ni NVR** (selon les modèles) ; **Sonos** : recherche ; **Alexa Devices** : les Echo deviennent des lecteurs multimédias.
- **Tableau Énergie** : niveau de charge de la batterie domestique et **noms personnalisés** pour le réseau, le solaire, la batterie, le gaz et l’eau.
- **Liens rapides** entre appareils, pièces, automatisations et scripts ; création d’une automatisation pré-remplie depuis une entité ou un appareil.
- **Vérification YAML en direct** dans les éditeurs (deux-points oubliés, guillemets, indentation…).
- **Mode avancé supprimé** : le bouton du profil disparaît, toutes les fonctions qu’il cachait sont accessibles à tous.
- La **clé de chiffrement des sauvegardes** est mise en avant pour qu’on ne l’oublie pas ; colonne **Firmware** dans la liste des appareils.

## ⚠️ Breaking changes à surveiller

- **Templates (YAML)** : l’**ancienne syntaxe par plateforme** (`platform: template` sous `sensor:`, `binary_sensor:`, `cover:`, `fan:`, `light:`, `lock:`, `switch:`, `vacuum:`, `weather:`, `alarm_control_panel:`) est **supprimée**. Dépréciée depuis la 2025.12, elle arrive au terme de ses six mois de sursis : migrez vers la syntaxe moderne `template:` (un guide pas à pas est proposé dans la documentation). C’est le changement le plus important de la version.
- **Bluetooth / ESPHome / Shelly** : le mode de scan par défaut passe à **Auto** (actif ou passif selon le besoin).
- **Labs** : options de comportement des déclencheurs renommées : `any` devient `each` et `last` devient `all` (rouvrez vos automatisations concernées).
- **HDMI-CEC** : `turn_off` envoie la commande de veille standard ; **SmartThings** : attribut `source` normalisé ; **Tuya** : l’unité fournie par l’API prime ; **ONVIF**, **IronOS**, **Certificate Expiry**, **Velux** : ajustements.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.6**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-6" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète** obligatoire.
2. Ouvrez `configuration.yaml` (et vos fichiers inclus) et cherchez `platform: template`. S’il y en a, **migrez avant de mettre à jour**, sinon ces entités disparaîtront.
3. Notez votre **clé de chiffrement de sauvegarde** dans un gestionnaire de mots de passe.

<div class="ha-avis" markdown="1">
### 💬 L’avis de Xavier

Le sélecteur de cartes « par entité » est exactement ce qu’il fallait pour les débutants : on part de *sa* lampe, pas d’un jargon. Les indicateurs en direct sur les conditions vont faire gagner un temps fou en dépannage. Attention en revanche à la fin de l’ancienne syntaxe des templates : c’est le genre de changement qui casse une installation ancienne en silence. Et clin d’œil aux piscinistes : l’arrivée de **Vistapool** confirme que la piscine connectée a toute sa place dans Home Assistant.
</div>

Avez-vous déjà migré vos anciens templates ? Entraidons-nous sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— Xavier (XAV59213)</p>
