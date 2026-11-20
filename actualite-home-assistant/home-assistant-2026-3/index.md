---
layout: ha-release
title: "Home Assistant 2026.3 : aspirateurs par pièce, « Continuer en cas d’erreur » et mot d’activation sur Android"
short_title: "2026.3 : le grand nettoyage"
description: "Home Assistant 2026.3 (4 mars 2026) en français : nettoyage par pièce pour les robots aspirateurs, option Continuer en cas d’erreur dans l’éditeur, wake word local sur Android, tableau Énergie amélioré, Python 3.14 et breaking changes."
excerpt_fr: "Une version « grand nettoyage » : envoyez votre robot dans une pièce précise, laissez une automatisation continuer malgré une erreur, et réveillez Assist à la voix sur Android, en local."
image: /actualite-home-assistant/home-assistant-2026-3/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.3, mars 2026"
date: 2026-03-04
release_date: 2026-03-04
section: actualite-ha
version: "2026.3"
month: "Mars 2026"
official_title: "2026.3: A clean sweep"
release_url: https://www.home-assistant.io/blog/2026/03/04/release-20263/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.3/
tags: [home-assistant, mise-a-jour, 2026.3]
seo:
  type: NewsArticle
gallery:
  - src: images/vacuum-area-mapping.webp
    caption: "Associer les segments de l’aspirateur aux pièces de Home Assistant."
  - src: images/automation-continue-on-error.webp
    caption: "L’option « Continue on error » dans le menu d’une action de l’éditeur visuel."
  - src: images/energy-badges.webp
    caption: "Les badges de la vue « Now » du tableau Énergie : puissance, débit de gaz et d’eau en temps réel."
  - src: images/energy-tabs.webp
    caption: "Les réglages Énergie séparés en trois onglets : Électricité, Gaz et Eau."
---

Après une 2026.2 massive, la **2026.3** (sortie le **4 mars 2026**) prend un rythme plus posé. Frenck l’assume : l’équipe a mis de côté les grandes annonces pour **relire, polir et intégrer un nombre impressionnant de contributions communautaires**. Résultat : une avalanche de nouvelles intégrations, de corrections et de montées en qualité… et quelques pépites très concrètes au quotidien.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧹 **Nettoyage par pièce** pour les robots aspirateurs, avec vos propres pièces Home Assistant.
- 🛟 **Continue on error** enfin disponible dans l’éditeur visuel.
- 🎙️ **Mot d’activation local** dans l’application Android (expérimental).
- ⚡ Tableau **Énergie** : badges temps réel, Sankey pour l’eau, onglets Électricité / Gaz / Eau.
- 🐍 Home Assistant tourne désormais sous **Python 3.14**.
</div>

## ✨ Les nouveautés phares

### 🧹 Envoyez votre aspirateur nettoyer une pièce précise

La star de cette version : l’action **clean area** (« nettoyer une zone »). Elle envoie votre robot nettoyer **une ou plusieurs pièces** à la demande. Le gros atout : elle utilise **vos pièces Home Assistant**, pas des identifiants obscurs propres au fabricant.

{% include ha-figure.html src="images/vacuum-area-mapping.webp" caption="La boîte de dialogue « Map vacuum segments to areas » : chaque segment détecté par le robot est relié à une pièce." %}

**Mise en place, pas à pas :**
1. Ouvrez l’entité de votre aspirateur (s’il prend en charge le nettoyage par zone).
2. Cliquez sur l’icône **paramètres** (roue dentée).
3. Dans la section **Map vacuum segments to areas**, associez chaque segment détecté par le robot à une pièce de Home Assistant.
4. Utilisez ensuite l’action « nettoyer une zone » dans une automatisation, un script ou un bouton de dashboard.

Si la carte du robot change (nouvelle cartographie dans l’appli du fabricant…), Home Assistant le détecte et crée une **réparation** pour vous inviter à mettre à jour l’association. Et comme tout repose sur les pièces natives, la voie est ouverte pour un futur « nettoie la cuisine » à la voix (il arrivera dès la 2026.4).

### 🛟 « Continue on error » dans l’éditeur visuel

Une option très attendue : **Continue on error**, accessible depuis le menu **⋮** de chaque action. Jusqu’ici, elle n’existait qu’en YAML (Frenck rappelle l’avoir écrite il y a des années !). Un indicateur visuel apparaît sur la ligne de l’action concernée.

{% include ha-figure.html src="images/automation-continue-on-error.webp" caption="Activer « Continue on error » sur une action : la suite de l’automatisation s’exécute même si elle échoue." %}

**Exemple concret :** une automatisation envoie trois notifications. Si l’une échoue (téléphone hors ligne, service indisponible), les deux autres partent quand même.

### 🎙️ Votre téléphone Android devient un satellite vocal (expérimental)

L’application **Companion Android** sait détecter un **mot d’activation directement sur le téléphone**, même verrouillé. Elle s’appuie sur **microWakeWord**, le moteur léger de la Home Assistant Voice Preview Edition : **tout est traité localement**, aucun son n’est envoyé dans le cloud. Trois mots au choix : *Okay Nabu*, *Hey Jarvis* et *Hey Mycroft*.

**Activation :** sur le téléphone, **Paramètres › Companion App › Assist for Android**, puis activez **Enable wake word detection**. Si un autre satellite est à proximité, seul le plus rapide répond.

🔋 **À savoir :** l’écoute permanente consomme de la batterie. L’équipe conseille de l’activer par automatisation uniquement quand c’est utile (par exemple quand le téléphone est connecté au Wi-Fi de la maison).

### ⚡ Un tableau Énergie plus lisible

- La vue **Now** gagne des **badges** de puissance, de débit de gaz et de débit d’eau en temps réel, ainsi qu’un **diagramme de Sankey pour l’eau**.
- Le deuxième onglet s’appelle désormais **Electricity** (et non plus *Energy*) ; les réglages sont séparés en **Électricité**, **Gaz** et **Eau**.
- Les infobulles des graphiques indiquent le **jour de la semaine**.

{% include ha-figure.html src="images/energy-badges.webp" caption="Les nouveaux badges temps réel de la vue « Now »." %}

## 🧩 Nouvelles intégrations

✅ Dix-sept ajouts, parmi lesquels :

- 🇫🇷 **MyNeomitis** : radiateurs, sèche-serviettes et planchers chauffants **Axenco MyNeomitis**, une marque bien présente en France.
- **OneDrive for Business** et **IDrive e2** : de nouveaux emplacements de sauvegarde.
- **Homevolt**, **Indevolt**, **Zinvolt** : batteries domestiques (en local pour les deux premières).
- **Powerfox Local** : le Poweropti en local, sans cloud.
- **Liebherr** : réfrigérateurs et congélateurs connectés.
- **Trane Local** : thermostats Trane/American Standard en local.
- **Hegel**, **Ghost**, **Hypontech Cloud**, **IntelliClima**, **MTA New York**, **Redgtech**, **System Nexa 2**, **Teltonika**…

**InfluxDB**, **Ness Alarm** et **Splunk** se configurent désormais depuis l’interface.

## 🔧 Améliorations notables

- **Matter** : alarmes de **monoxyde de carbone** et capteurs de **COV totaux**.
- **Reolink** : boutons PTZ diagonaux ; **UniFi Protect** : PTZ et presets.
- **SmartThings** : fours Samsung à double cavité ; **Roborock** : machines à laver/sécher Zeo.
- **Alexa Devices** : moniteur de qualité d’air Amazon.
- **KNX** : entités nombre configurables depuis l’interface.
- Assist sait **retirer un élément d’une liste de tâches** ; la carte statistiques propose la période **Année** ; les vues en sections acceptent un **pied de page** (carte collée en bas de l’écran) ; les pages Matter, Z-Wave, Zigbee et Bluetooth sont réorganisées.
- 🏆 Neuf intégrations passent **platine** (dont WLED, Immich, Portainer, Watts Vision +).

### 🐍 Python 3.14

Home Assistant tourne désormais sous **Python 3.14** : interpréteur plus rapide et démarrage amélioré. **Rien à faire** sur les installations officielles, la migration est automatique.

## ⚠️ Breaking changes à surveiller

- **Lumières** : `color_temp` (en mireds) n’est plus accepté pour régler la température de couleur. Utilisez `color_temp_kelvin`. Les attributs d’état `color_temp`, `kelvin`, `min_mireds` et `max_mireds` disparaissent aussi (remplacés par `color_temp_kelvin`, `min_color_temp_kelvin` et `max_color_temp_kelvin`) : attention à vos templates ! Même chose pour `lifx.effect_pulse`.
- **Images Docker** : compressées en `zstd` au lieu de `gzip` (vérifiez vos outils si vous gérez un registre).
- **Tado** : le suivi des téléphones (device tracker) est supprimé.
- **Snapcast** : les lecteurs des groupes sont supprimés.
- **Template fans** : état `unavailable` si le template d’état contient une erreur de syntaxe.
- **Z-Wave** : vitesses des ventilateurs corrigées en pourcentage ; **BSB-Lan** : mode `on` → `performance` ; **Satel Integra** et **StarLine** : changements mineurs.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.3**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-3" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète** (Paramètres › Système › Sauvegardes).
2. Cherchez `color_temp:` dans vos automatisations, scripts et scènes YAML : c’est le changement qui touchera le plus de monde.
3. Mettez à jour, puis rendez-vous dans les réglages de votre robot aspirateur pour l’associer à vos pièces.

<div class="ha-avis" markdown="1">
### 💬 L’avis de Xavier

Pas de révolution, mais des fonctions qu’on utilise **tous les jours** : le nettoyage par pièce change la vie de ceux qui ont un robot, et « Continue on error » rend les automatisations plus robustes sans écrire une ligne de YAML. Côté France, l’arrivée de MyNeomitis est une bonne nouvelle pour le chauffage électrique. Seul vrai point de vigilance : le passage obligatoire aux kelvins.
</div>

Votre robot connaît-il déjà vos pièces ? Partagez votre configuration sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— Xavier (XAV59213)</p>
