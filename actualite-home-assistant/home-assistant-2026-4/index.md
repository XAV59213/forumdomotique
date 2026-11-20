---
layout: ha-release
title: "Home Assistant 2026.4 : l’infrarouge devient natif, les automatisations pensent « portes, fenêtres et mouvement »"
short_title: "2026.4 : l’infrarouge fait son retour"
description: "Home Assistant 2026.4 (1er avril 2026) en français : infrarouge natif avec les proxys ESPHome, déclencheurs et conditions multi-domaines, couleurs de fond des sections, gestion des codes des serrures Matter, nouvelle jauge et breaking changes."
excerpt_fr: "L’infrarouge devient un citoyen de première classe grâce aux proxys ESPHome, les automatisations raisonnent en portes, fenêtres et mouvement, et les serrures Matter se gèrent enfin depuis Home Assistant."
image: /actualite-home-assistant/home-assistant-2026-4/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.4, avril 2026"
date: 2026-04-01
release_date: 2026-04-01
section: actualite-ha
version: "2026.4"
month: "Avril 2026"
official_title: "2026.4: Infrared never left the chat"
release_url: https://www.home-assistant.io/blog/2026/04/01/release-20264/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.4/
tags: [home-assistant, mise-a-jour, 2026.4]
seo:
  type: NewsArticle
gallery:
  - src: images/infrared-proxy.webp
    caption: "La page d’un proxy infrarouge (Seeed XIAO IR Mate sous ESPHome) dans Home Assistant."
  - src: images/lg-tv-infrared-proxy.webp
    caption: "Un téléviseur LG piloté en infrarouge : lecteur multimédia et boutons de télécommande."
  - src: images/cross-domain-triggers.webp
    caption: "Les nouveaux déclencheurs multi-domaines : porte, fenêtre, mouvement, température…"
  - src: images/natural-automation-example.webp
    caption: "Une automatisation écrite « comme on parle » avec le déclencheur Mouvement détecté."
  - src: images/dashboard-sections-background-colors.webp
    caption: "Des couleurs de fond pour regrouper visuellement les sections d’un dashboard."
  - src: images/matter-manage-lock-credentials.webp
    caption: "Gérer les utilisateurs et les codes PIN d’une serrure Matter."
  - src: images/card-feature-light-favorite-colors.webp
    caption: "Les couleurs et positions favorites directement sur les cartes tuiles."
  - src: images/card-gauge-redesign.webp
    caption: "La carte jauge redessinée."
  - src: images/ai-conversation-thinking.webp
    caption: "« Show details » : le raisonnement et les outils utilisés par l’agent IA d’Assist."
---

Non, ce n’est pas un poisson d’avril 🐟 : la **2026.4**, sortie le **1er avril 2026**, fait de l’**infrarouge** un citoyen de première classe de Home Assistant. Frenck avoue ne pas avoir sauté de sa chaise en entendant l’idée… avant d’être convaincu. Cette version apporte aussi une **tonne de déclencheurs et conditions par usage**, désormais **multi-domaines**, des **couleurs de fond** pour les sections, la **gestion des codes des serrures Matter** et 14 nouvelles intégrations.

<div class="ha-callout info" markdown="1">
**En bref**
- 📡 **Infrarouge natif** : des proxys ESPHome pilotent téléviseurs, climatiseurs, ventilateurs…
- 🤖 Déclencheurs et conditions **multi-domaines** (porte, fenêtre, mouvement, température, batterie…) dans Labs.
- 🎨 **Couleur de fond** pour les sections de dashboard.
- 🔐 **Gestion des utilisateurs et codes PIN** des serrures Matter.
- 🗣️ « **Nettoie la cuisine** » : le nettoyage par pièce arrive à la voix.
</div>

## ✨ Les nouveautés phares

### 📡 L’infrarouge devient natif

Téléviseurs, climatiseurs, ventilateurs, barres de son… des millions d’appareils encore pilotés par une petite télécommande infrarouge. Home Assistant reprend la recette qui a si bien marché pour le Bluetooth : des **proxys** ESPHome peu coûteux, placés où il faut dans la maison, qui émettent les commandes IR. Une nouvelle plateforme **Infrared** sert de socle commun aux intégrations.

{% include ha-figure.html src="images/infrared-proxy.webp" caption="Un proxy infrarouge (Seeed Studio XIAO IR Mate) vu dans Home Assistant." %}

La première intégration à en profiter est **LG Infrared** : elle crée un **lecteur multimédia** (alimentation, volume, chaînes, lecture) et des **boutons** pour un téléviseur LG.

**Pour démarrer, pas à pas :**
1. Procurez-vous un émetteur compatible : le plus simple est le **Seeed Studio XIAO IR Mate**.
2. Ouvrez la page **ESPHome Ready-Made Projects**, branchez l’appareil à l’ordinateur et flashez-le **depuis le navigateur**.
3. Ajoutez-le à Home Assistant (découverte ESPHome), puis ajoutez l’intégration de votre appareil (par exemple **LG Infrared**) en choisissant ce proxy.

🌱 **Pourquoi c’est important ?** C’est une affaire de **durabilité** chère à l’Open Home Foundation : inutile de jeter un appareil parfaitement fonctionnel parce qu’il n’est pas « smart ».

### 🤖 Des automatisations qui pensent en portes, fenêtres et mouvement (Labs)

Jusqu’ici, chaque déclencheur était lié à un domaine technique (*binary_sensor*, *cover*…). Or, on pense en **portes, fenêtres, mouvement ou température**. La 2026.4 introduit des déclencheurs et conditions **multi-domaines** : un seul bloc « porte ouverte » fonctionne, que l’info vienne d’un capteur d’ouverture ou d’un volet motorisé.

{% include ha-figure.html src="images/natural-automation-example.webp" caption="« Quand du mouvement est détecté » : une automatisation lisible par toute la famille." %}

Nouveautés multi-domaines (déclencheur « quand » + condition « si ») :
- **Porte, porte de garage, portail, fenêtre** : ouverture/fermeture.
- **Mouvement** et **présence (occupancy)** : détecté / plus détecté.
- **Température, humidité, luminosité, puissance** : variation ou franchissement d’un seuil.
- **Batterie** : faible, en charge, franchissement d’un seuil.
- **Qualité de l’air** : CO, CO₂, fumée…

Et beaucoup de domaines existants s’enrichissent : compteur, volets (tous types), évènements, programmes horaires (*schedule*), listes de tâches, vannes, chauffe-eau, télécommandes… Le tout cible aussi des **pièces, étages et étiquettes**. L’équipe le dit : la fonctionnalité est **presque complète**. À tester dans **Paramètres › Système › Labs**.

### 🎨 Des couleurs de fond pour les sections

Les sections d’un dashboard peuvent avoir une **couleur de fond** : idéal pour regrouper des cartes, faire ressortir une zone ou personnaliser son tableau.

{% include ha-figure.html src="images/dashboard-sections-background-colors.webp" caption="Quatre sections, avec ou sans fond coloré." %}

**Comment faire :** ouvrez les paramètres de la section, activez **Background**, puis choisissez une couleur prédéfinie ou un code hexadécimal. Les sections voisines sans fond s’alignent automatiquement.

### 🔐 Gérer les codes de sa serrure Matter

Si vous avez une **serrure Matter**, la page de l’appareil propose **Manage lock** : liste des utilisateurs, ajout, modification, suppression, **codes PIN** et type d’accès. Derrière, de nouvelles **actions Matter** permettent aussi de tout automatiser (par exemple, créer ou supprimer le code d’un invité).

{% include ha-figure.html src="images/matter-manage-lock-add-user.webp" caption="Ajout d’un utilisateur : nom, code PIN et type d’accès." %}

### ⭐ Favoris, jauge et hauteur automatique

- Les **couleurs favorites** des lumières s’affichent comme fonctionnalité des cartes tuile et lumière ; même principe pour les **positions favorites** des volets et vannes, et on peut **copier ses favoris** vers d’autres entités.
- La **carte jauge** est redessinée, plus moderne, sans rien perdre (mode aiguille, segments de sévérité).
- Option **Auto height** dans l’éditeur de disposition des cartes (les cartes de titre deviennent par défaut moins hautes).

### 🧠 Voir ce que « pense » l’IA d’Assist

Avec un agent conversationnel basé sur un LLM, chaque réponse a une section **Show details** : raisonnement, outils appelés, arguments et résultats. Pour l’instant, sur l’interface web de bureau uniquement.

## 🧩 Nouvelles intégrations

✅ Quatorze ajouts, dont :

- **Infrared** (plateforme) et **LG Infrared** (téléviseurs LG via IR).
- **UniFi Access** : contrôle d’accès Ubiquiti en local.
- **WiiM** : streamers audio ; **Solarman** : équipements solaires en local.
- **Qube Heat Pump** (Modbus TCP), **Fresh-r** (ventilation), **OpenDisplay** (écrans e-paper BLE), **TRMNL** (écrans e-ink, lancé directement en **platine**).
- **Autoskope**, **LoJack** (suivi de véhicules), **Casper Glow**, **Chess.com** et **Lichess**.

**Leviton Decora Wi-Fi** et **Orvibo** passent en configuration par l’interface. **BMW Connected Drive / Mini**, **Duke Energy** et **Tfiac** sont retirés.

## 🔧 Améliorations notables

- **Voix : « nettoie la cuisine »** : le nettoyage par pièce de la 2026.3 fonctionne désormais avec Assist.
- **Sauvegardes** : progression de l’envoi visible pour chaque emplacement.
- **Carte Markdown** : actions au tap, appui long et double tap ; **éditeur de la carte Map** complet.
- Templates : nouvelles fonctions `state_attr_translated` et `entity_name`.
- **Recherche** dans les graphes réseau ZHA, Z-Wave et Bluetooth.
- **SmartThings** (énorme vague d’améliorations), **Roborock Q10**, **Renault** (limites de charge), **Schlage** (codes d’accès), **Proxmox VE**, **Kostal Plenticore**…

### 🛡️ Avis de sécurité publiés

Trois failles corrigées précédemment ont été divulguées, dont une **critique (CVSS 9.7)** : des points d’accès d’Apps exposés sans authentification sur le réseau local en mode réseau hôte (**CVE-2026-34205**, corrigée dans le **Supervisor 2026.03.2**). Raison de plus pour garder Supervisor et Core à jour.

## ⚠️ Breaking changes à surveiller

- **MQTT** : l’option `object_id` est supprimée après six mois de dépréciation.
- **Z-Wave** : le panneau « Installer » disparaît.
- **Tuya** : suppression des anciens interrupteurs utilisés pour les vannes.
- **JVC Projector** : *Picture Mode* et *HDR Processing* passent de `sensor` à `select`.
- **Motion Blinds**, **Roth Touchline**, **Litter-Robot**, **pyLoad** : ajustements mineurs.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.4**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-4" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète** avant de commencer.
2. Utilisateurs **MQTT** en YAML : cherchez `object_id` et remplacez-le (voir la documentation MQTT).
3. Vérifiez que le **Supervisor** est bien à jour (faille critique corrigée en 2026.03.2).

<div class="ha-avis" markdown="1">
### 💬 Mon avis

L’infrarouge, c’est la bonne idée qui n’a l’air de rien : combien de climatiseurs mobiles et de vieux téléviseurs dorment chez nous ? Avec un proxy à quelques euros, ils entrent dans la domotique **en local**. Côté automatisations, les blocs multi-domaines rendent enfin les scénarios lisibles par tout le foyer. Et pour les propriétaires de serrures Matter, la gestion des codes depuis Home Assistant est un vrai plus.
</div>

Vous avez déjà flashé un proxy infrarouge ? Racontez-nous sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— XAV59213</p>
