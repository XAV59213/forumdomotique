---
layout: ha-release
title: "Home Assistant 2026.1 : le dashboard Home s’adapte au mobile et les automatisations parlent votre langue"
short_title: "2026.1 : le dashboard Home passe au mobile"
description: "Home Assistant 2026.1 (7 janvier 2026) en français : dashboard Home repensé sur mobile, page Appareils, nouveaux déclencheurs « métier » dans Labs, protocoles mis en avant, 8 nouvelles intégrations et breaking changes."
excerpt_fr: "Une version de rentrée plus calme mais utile : résumés en haut du dashboard Home sur mobile, page « Appareils » pour les orphelins, et une pluie de déclencheurs lisibles dans Labs."
image: /actualite-home-assistant/home-assistant-2026-1/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.1, janvier 2026"
date: 2026-01-07
release_date: 2026-01-07
section: actualite-ha
version: "2026.1"
month: "Janvier 2026"
official_title: "2026.1: Home is where the dashboard is 🥂"
release_url: https://www.home-assistant.io/blog/2026/01/07/release-20261/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.1/
tags: [home-assistant, mise-a-jour, 2026.1]
seo:
  type: NewsArticle
gallery:
  - src: images/home-dashboard-mobile.webp
    caption: "Sur mobile, le dashboard Home affiche désormais les résumés (lumières, climat, sécurité, énergie…) directement en haut."
  - src: images/home-dashboard-devices.webp
    caption: "La nouvelle page « Appareils » du dashboard Home regroupe les appareils qui ne sont rattachés à aucune pièce."
  - src: images/purpose-specific-triggers.webp
    caption: "Les déclencheurs « par usage » (Labs) : on choisit « Quand une lumière s’allume » plutôt qu’un changement d’état technique."
  - src: images/target_summary_automation_editor.webp
    caption: "L’éditeur d’automatisations résume la cible (pièce, étage, étiquette) pour comprendre l’automatisation d’un coup d’œil."
  - src: images/protocol-dashboards.webp
    caption: "Les protocoles (Matter, Zigbee, Z-Wave, Thread, Bluetooth, KNX…) remontent dans la page Paramètres."
  - src: images/energy-dashboard-period-selector.webp
    caption: "Le sélecteur de période du tableau Énergie reste collé en bas de l’écran."
---

👋 **Bonne année à toutes et à tous !** Home Assistant ouvre 2026 avec la version **2026.1**, sortie le **7 janvier 2026**. Franck Nijhof (Frenck) l’annonce lui-même : c’est une version volontairement plus légère, contributeurs et mainteneurs ayant eux aussi profité des fêtes. Plus légère, mais pas vide : le dashboard **Home** continue sa mue (surtout sur smartphone), les **déclencheurs « par usage »** gagnent une dizaine de familles, et les **protocoles** (Zigbee, Z-Wave, Thread…) deviennent enfin faciles à trouver.

<div class="ha-callout info" markdown="1">
**En bref**
- 📱 Dashboard Home : résumés en haut de l’écran sur mobile + page « Appareils » pour les appareils sans pièce.
- 🤖 Labs : nouveaux déclencheurs bouton, climat, présence, humidificateur, lumière, serrure, scène, sirène et mise à jour.
- 🧭 Paramètres : une section dédiée aux protocoles, juste après les réglages principaux.
- 🧩 8 nouvelles intégrations, dont Watts Vision + (chauffage) et Fressnapf Tracker (animaux).
</div>

## ✨ Les nouveautés phares

### 📱 Le dashboard Home, pensé pour le smartphone

🏠 Le dashboard **Home**, apparu avec la 2025.9, poursuit son évolution. Sur **mobile**, les cartes de résumé (lumières, climat, sécurité, lecteurs multimédias, météo, énergie) s’affichent **directement en haut de la vue**, suivies de vos favoris et de vos pièces. Elles remplacent l’ancienne navigation par onglets.

{% include ha-figure.html src="images/home-dashboard-mobile.webp" caption="Le dashboard Home sur mobile : les résumés sont accessibles sans toucher un seul onglet." %}

**Pourquoi c’est utile ?** Tout ce qui compte est visible sans tap supplémentaire : on ouvre l’application, on voit d’un coup d’œil s’il reste une lumière allumée ou si la maison est sécurisée. Sur ordinateur, rien ne change : les résumés restent dans la barre latérale, sous l’intitulé **For you**.

### 🗂️ Une page « Appareils » pour les orphelins

Vous avez retiré un appareil d’une pièce et il a « disparu » ? Une nouvelle page **Appareils** apparaît dans le dashboard Home et liste **tous les appareils non affectés à une pièce**. Vous pouvez les retrouver et les piloter sans fouiller dans les paramètres.

👉 **Comment en profiter :** ouvrez le dashboard Home, puis la page **Appareils**. Profitez-en pour ranger vos appareils dans les bonnes pièces : c’est ce qui fait fonctionner les résumés et les futures automatisations par pièce.

### 🤖 Des déclencheurs qui parlent votre langue (Labs)

Introduits en 2025.12, les **déclencheurs et conditions « par usage »** (*purpose-specific triggers and conditions*) remplacent la logique technique (« l’état de l’entité passe de *off* à *on* ») par des formulations naturelles comme « **Quand une lumière s’allume** » ou « **Si le climat chauffe** ». La 2026.1 en ajoute beaucoup :

- **Bouton** : quand une entité bouton est pressée.
- **Climat** : changement de mode HVAC, de consigne, franchissement d’un seuil de consigne, variation de température ou d’humidité.
- **Suivi d’appareil** : arrivée ou départ de la maison (premier arrivé, dernier parti, ou tout changement).
- **Humidificateur** : marche/arrêt, humidification, séchage, seuils d’humidité.
- **Lumière** : variation de luminosité ou franchissement d’un seuil.
- **Serrure** : verrouillée, déverrouillée, ouverte ou **bloquée**.
- **Scène**, **sirène** et **mise à jour disponible**.

{% include ha-figure.html src="images/target_summary_automation_editor.webp" caption="La cible (pièce, étage ou étiquette) est désormais résumée dans le flux de l’automatisation." %}

Comme ces déclencheurs ciblent une **pièce, un étage ou une étiquette** (et pas seulement une entité), l’affichage de la cible a été repensé pour comprendre l’intention d’une automatisation d’un seul regard.

**Pour l’essayer, pas à pas :**
1. Ouvrez **Paramètres › Système › Labs**.
2. Activez les **déclencheurs et conditions par usage**.
3. Créez une automatisation : la liste des déclencheurs propose maintenant ces nouvelles familles.

### 🧭 Les protocoles enfin mis en avant

Beaucoup d’utilisateurs ignoraient que Home Assistant dispose de tableaux dédiés à **Zigbee, Z-Wave, Matter, Thread, Bluetooth, KNX ou Insteon**. La page **Paramètres** leur réserve désormais une section, placée juste après les réglages principaux. Les entrées n’apparaissent que si l’intégration correspondante est configurée : vous ne voyez que ce qui vous concerne.

{% include ha-figure.html src="images/protocol-dashboards.webp" caption="La nouvelle section Protocoles de la page Paramètres." %}

## 🧩 Nouvelles intégrations

✅ Huit nouveautés dans cette version :

- **AirPatrol** : pilotage des climatiseurs via les boîtiers Wi-Fi AirPatrol.
- **eGauge** : compteurs d’énergie eGauge, souvent associés au solaire.
- **Fluss+** : le bouton connecté Fluss+.
- **Fish Audio** : synthèse vocale (TTS) au rendu naturel.
- **Fressnapf Tracker** : localisation et activité de vos animaux via les traceurs GPS Fressnapf.
- **HomeLink** : déclencher des routines depuis les boutons HomeLink de votre voiture.
- **Watts Vision +** : pilotage du chauffage Watts Vision +, zone par zone.
- **WebRTC** : intégration interne qui fournit le streaming WebRTC des caméras.

S’y ajoute l’intégration virtuelle **Levoit** (gérée par VeSync). **Hikvision** et **VIVOTEK** se configurent désormais depuis l’interface.

## 🔧 Améliorations notables

- **Matter** : trois capteurs de diagnostic pour la détection à distance des thermostats ; volume réglable sur les enceintes Matter.
- **SmartThings** : capteurs de qualité d’air PM1/PM2,5/PM10, suivi du filtre de hotte, vitesse de ventilation des hottes.
- **FRITZ!SmartHome** : interrupteurs pour activer/désactiver les routines FRITZ!.
- **Ping** : nouveau capteur de perte de paquets (désactivé par défaut).
- **KNX** : bien plus d’entités configurables depuis l’interface (date, heure, capteur, scène, texte, ventilateur…).
- **Pooldose** : grosse mise à niveau pour les piscines (niveaux, consignes de dosage, mode de fonctionnement).
- **ESPHome** : prise en charge des **réponses d’actions** (ESPHome 2025.12) : un appareil peut renvoyer des données structurées (JSON) à Home Assistant, par exemple sa force de signal Wi-Fi ou sa version de firmware.
- **Tableau Énergie** : le sélecteur de période reste collé en bas de l’écran, bien pratique pour comparer les jours sans remonter la page.
- Nouvelle unité **gallons par jour** pour suivre une cuve de fioul, et option pour réactiver le fichier de log dupliqué (module Terminal & SSH 9.22.0 ou plus requis).

🏆 Côté qualité : **KNX** et **UniFi Protect** atteignent le niveau **platine** ; **SFR Box** passe **argent** — une bonne nouvelle pour les abonnés SFR.

## ⚠️ Breaking changes à surveiller

À vérifier si vous utilisez l’une de ces intégrations :

- **Coolmaster** : le mode de ventilation `med` devient `medium`.
- **Tailscale** : le capteur « Supports hairpinning » est supprimé (l’API ne le fournit plus).
- **UniFi Protect** : les valeurs des entités *select* passent en *snake_case* (`Always` → `always`, `AutoNoLEDsOn` → `auto_no_leds_on`…). Mettez à jour vos automatisations et templates.
- **Telegram bot** : les paramètres inconnus ne sont plus tolérés dans les actions.
- **VeSync** : le mode `advancedSleep` devient `advanced_sleep`.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.1**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-1" %}

## 💾 Conseil de mise à jour

1. Faites une **sauvegarde complète** : **Paramètres › Système › Sauvegardes**.
2. Vérifiez la liste des breaking changes ci-dessus.
3. Installez la mise à jour depuis **Paramètres › Système › Mises à jour**. Visez au minimum la **2026.1.2**, qui corrige deux failles de sécurité.

## 📋 Résumé des nouveautés

| Fonctionnalité | Ce que ça change | Pour qui ? |
| --- | --- | --- |
| Dashboard Home mobile | Résumés en haut de l’écran | Toute la famille |
| Page Appareils | Retrouver les appareils sans pièce | Ceux qui réorganisent |
| Déclencheurs par usage (Labs) | 9 nouvelles familles | Créateurs d’automatisations |
| Section Protocoles | Zigbee, Z-Wave, Thread… faciles d’accès | Tout le monde |
| Réponses d’actions ESPHome | Échanges bidirectionnels | Bricoleurs ESPHome |

<div class="ha-avis" markdown="1">
### 💬 Mon avis

Une version de transition, mais qui va dans le bon sens : Home Assistant se rend plus **accessible au reste du foyer** (le dashboard Home sur mobile) et plus **lisible pour celui qui automatise** (les déclencheurs par usage). La page Appareils est le genre de petit détail qui pousse à ranger sa maison… et c’est indispensable pour tirer parti des automatisations par pièce qui arrivent. Si vous ne l’avez pas encore fait, c’est le bon moment pour essayer Labs.
</div>

Et vous, vous avez testé les nouveaux déclencheurs ? Venez en parler sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— XAV59213</p>
