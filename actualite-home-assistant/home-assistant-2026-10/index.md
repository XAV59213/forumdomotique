---
layout: ha-release
title: "Home Assistant 2026.10 : une carte toute neuve, la condition « Déclenché par » enfin simple et l’IA connectée en un clic"
short_title: "2026.10 : vous êtes ici 📍"
description: "Home Assistant 2026.10 (7 octobre 2026) en français : Cloud bientôt renommé Link, carte OpenStreetMap et profil utilisateur réorganisé."

excerpt_fr: "Les cartes passent aux tuiles vectorielles d’OpenStreetMap, la condition « Triggered by » se coche sans identifiants, l’IA se branche en un clic via MCP… et Home Assistant Cloud annonce son nouveau nom : Link."
image: /actualite-home-assistant/home-assistant-2026-10/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.10, octobre 2026"
date: 2026-10-07
release_date: 2026-10-07
section: actualite-ha
version: "2026.10"
month: "Octobre 2026"
official_title: "2026.10: You are here 📍"
release_url: https://www.home-assistant.io/blog/2026/10/07/release-202610/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.10/
tags: [home-assistant, mise-a-jour, 2026.10]
seo:
  type: NewsArticle
gallery:
  - src: images/map-markers.webp
    caption: "La nouvelle carte : marqueurs redessinés, avec la photo des personnes et les zones."
  - src: images/map-activity.webp
    caption: "Le panneau de vue d’ensemble du tableau Carte : activité récente d’une personne."
  - src: images/map-zone-editor.webp
    caption: "L’éditeur de zones utilise la même nouvelle carte."
  - src: images/profile-page.webp
    caption: "La page de profil réorganisée : compte, thème, apparence, localisation, sécurité."
  - src: images/automation-triggered-by.webp
    caption: "La condition « Triggered by » : on coche les déclencheurs numérotés, sans inventer d’identifiant."
  - src: images/visibility-conditions.webp
    caption: "L’onglet Visibilité indique si la carte est visible maintenant et quelles conditions passent."
  - src: images/modbus-panel.webp
    caption: "Le nouveau panneau Modbus liste toutes les connexions, série et réseau."
  - src: images/ai-settings-mcp.webp
    caption: "La carte Model Context Protocol de la page IA, avec les URL à copier."
  - src: images/timer-tile-features.webp
    caption: "Des boutons de minuteur et des durées prédéfinies directement sur les tuiles."
---

« **Vous êtes ici** » 📍 : la **2026.10**, sortie le **7 octobre 2026**, met la **carte** à l’honneur après un incident discret mais spectaculaire du mois précédent. Frenck, lui, a un autre coup de cœur : la condition **Triggered by**, « la meilleure fonction d’automatisation que vous n’avez jamais utilisée », devient enfin simple. On y trouve aussi un **profil utilisateur** rangé, l’**IA connectée en un clic** grâce au protocole MCP, et une annonce de taille : **Home Assistant Cloud va devenir Home Assistant Link**.

<div class="ha-callout info" markdown="1">
**En bref**
- ☁️ Home Assistant **Cloud** sera renommé **Link** (prévu pour la version de décembre).
- 🗺️ Nouvelle **carte vectorielle** OpenStreetMap, nette à tous les zooms, avec vue d’ensemble.
- 👤 **Profil** réorganisé ; chaque utilisateur peut modifier son nom et sa photo.
- 🤖 Condition **Triggered by** sans identifiants à inventer.
- 🧠 Serveur **MCP** activable en un clic ; nouveau panneau **Modbus**.
</div>

## ✨ Les nouveautés phares

### ☁️ Le Cloud devient Link

Home Assistant Cloud sera renommé **Home Assistant Link** : même service, nouveau nom. L’équipe explique en avoir assez de voir les géants de la tech rendre des appareils dépendants du cloud, puis inutilisables. Le service de Nabu Casa n’a jamais enfermé personne ni exploité de données : un nom différent s’imposait. **Le changement est prévu pour la version de décembre.** Au passage, l’accès à distance accélère : serveurs migrés sur du *bare metal*, couverture élargie, et un **test de latence au démarrage** qui choisit le meilleur serveur.

### 🗺️ Une carte toute neuve

En septembre, le fournisseur de cartes utilisé par Home Assistant a commencé à afficher « API key required » sur ses images, **cassant toutes les cartes d’un coup**. Plutôt que de chercher un autre service gratuit, l’équipe est passée aux **tuiles vectorielles de la fondation OpenStreetMap**. La nouvelle intégration **Map tiles** récupère et met en cache les tuiles via votre Home Assistant : votre navigateur ne contacte **pas directement** de serveur de tuiles externe, et les zones récemment vues restent disponibles en cas de coupure internet.

{% include ha-figure.html src="images/map-markers.webp" caption="Des marqueurs redessinés : les personnes avec leur photo, les zones avec leurs icônes et couleurs." %}

- **Net à tous les zooms** : la carte est dessinée en vectoriel par votre appareil.
- **Marqueurs redessinés** pour les personnes, zones et appareils.
- **Vue d’ensemble** du tableau Carte à trois onglets (**People**, **Devices**, **Zones**), à côté de la carte sur ordinateur, en panneau à tirer sur mobile.
- L’**éditeur de zones** (**Paramètres › Pièces, étiquettes et zones**) utilise la même carte ; les zones sont triées par ordre alphabétique, Maison en tête.

### 👤 Un profil enfin rangé

La page **Profil** était devenue un fourre-tout. Elle adopte la navigation des Paramètres : une carte de compte en haut, puis **Thème**, **Apparence** (dashboard par défaut, ordre de la barre latérale), **Localisation** (langue, fuseau, formats), **Ce navigateur** / **Cette application** et **Sécurité** (mot de passe, double authentification, jetons). Rien n’a été supprimé. Nouveauté : **chaque utilisateur**, administrateur ou non, a un bouton **Edit profile** pour changer **son nom et sa photo** (avec recadrage).

### 🤖 « Triggered by » : la fonction cachée devient évidente

Beaucoup d’automatisations vont par paires : l’une allume la lumière du couloir au mouvement, l’autre l’éteint quand le mouvement s’arrête. On pouvait les fusionner depuis des années avec des **identifiants de déclencheurs** et la condition **Triggered by**… à condition de les inventer et de les retaper sans faute.

{% include ha-figure.html src="images/automation-triggered-by.webp" caption="Les déclencheurs sont numérotés ; dans la condition, on coche simplement ceux qui doivent correspondre." %}

**Fusionner deux automatisations, pas à pas :**
1. Dans une même automatisation, ajoutez deux déclencheurs : **Mouvement détecté** (n°1) et **Mouvement terminé** (n°2).
2. Ajoutez une action **Choisir** (*choose*) avec deux options.
3. Dans la première option, ajoutez la condition **Triggered by** et cochez le déclencheur n°1, puis l’action « allumer la lumière ».
4. Dans la seconde, cochez le déclencheur n°2, puis « éteindre la lumière ».

Home Assistant gère les identifiants en coulisses et nettoie derrière lui quand vous supprimez un déclencheur. Vos identifiants YAML existants continuent de fonctionner. L’éditeur signale aussi une condition qui pointe vers un déclencheur disparu.

### 🧠 Connecter son IA en un clic

Home Assistant peut servir de **serveur MCP** (Model Context Protocol) pour que des applications d’IA comme **Claude**, **ChatGPT** ou **Cursor** dialoguent avec la maison. La page **Paramètres › Système › AI tasks** devient **AI** et gagne une carte **Model Context Protocol** : un clic pour activer le serveur, et les **URL à copier** dans votre appli. Par défaut, seuls les **comptes administrateurs** peuvent se connecter. Dans l’autre sens, les Apps qui exposent leur propre serveur MCP sont découvertes automatiquement, et l’IA choisit mieux la musique à jouer.

### 🎛️ Visibilité, Modbus, noms et minuteurs

- **Visibilité des cartes** : mêmes conditions que dans l’éditeur d’automatisations (Template, Soleil, Zone, Appareil…), et l’onglet indique si la carte est visible **maintenant** et quelles conditions passent.
- **Panneau Modbus** (**Paramètres › Connectivité**) : toutes les connexions Modbus, ports série et passerelles réseau.
- **Use device name** : une entité peut porter simplement le nom de son appareil (un détecteur de fumée, par exemple).
- **Minuteurs** : boutons démarrer/pause/annuler et **durées prédéfinies** directement sur les tuiles (préréglages gérés via **Edit presets** dans la fenêtre du minuteur).

## 🧩 Nouvelles intégrations

✅ Quinze ajouts, dont :

- **SolarEdge Modbus** (lancée en **platine**) et **KACO Modbus** : onduleurs solaires en local, dans la lignée de la modernisation de Modbus.
- **my-PV** (AC•THOR, AC ELWA 2 : le surplus solaire en eau chaude), **Sunsynk**, **Bitvis Power Hub**, **Theben Conexa** (passerelle de compteur).
- **Gree Infrared**, **OSRAM Infrared**, **Persang Infrared** ; **Threema** (messages chiffrés de bout en bout) ; **Willow** (plantes), **Vitesy**, **INDI Allsky**, **Axle Energy**, **Zonneplan**.
- Virtuelles : **Austroflamm**, **EcoSpar**, **HAAS+SOHN** et **HETA** (via Fumis), **O General**, **Onida**, **Steinway & Lyngdorf**.

**Discogs**, **Rejseplanen** et **Volkszaehler** passent par l’interface. Huit intégrations sont retirées, dont **SolarEdge Local**, **Sigfox** et **Travis-CI**.

## 🔧 Améliorations notables

- Le **dashboard Home** affiche aussi les **alertes actives** ; nouveau curseur pour les *select* sur les tuiles ; décharge de chaque batterie visible dans le tableau Énergie.
- **Templates** : entités **climat** en template (fabriquer son propre thermostat), délai on/off pour les capteurs binaires template depuis l’interface, fonction `timedelta_string`.
- **Philips Hue** (zones MotionAware), **Matter**, **Tuya**, **Reolink**, **Roborock** (temps réel), **Music Assistant** (annonces parlées), **Z-Wave** (nouvelles conditions), **ESPHome**…
- Classe **bris de vitre** pour les capteurs binaires, mode de ventilation par la voix, gestionnaires de mots de passe de nouveau compatibles avec la page de connexion.

## ⚠️ Breaking changes à surveiller

- **Authentification** : le **mode « legacy »** du fournisseur d’authentification Home Assistant est supprimé.
- **Conditions d’état** : combiner `for` avec un attribut, une liste d’états ou l’état d’une autre entité **échoue désormais à la validation**. La **2026.10.2** a ensuite de nouveau autorisé une **liste d’états** avec une durée.
- **MQTT** : `mqtt.publish` et `mqtt.dump` exigent un **compte administrateur** (comme `synology_dsm.reboot` et `synology_dsm.shutdown`).
- **Telegram bot** : `directory_path` de `download_file` doit figurer dans `allowlist_external_dirs`.
- **Proxmox VE** : l’uptime devient un horodatage ; **Mealie** 3.2 minimum ; **easyEnergy**, **EnergyZero**, **EnergyFlip**, **OpenEVSE**, **IoTaWatt**, **Sofar**, **UniFi Network**, **Xbox** : ajustements.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.10**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-10" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète.**
2. Si vous utilisez encore le **mode legacy** d’authentification ou des conditions d’état avec `for` + attribut, corrigez-les **avant** la mise à jour (sinon l’automatisation sera refusée).
3. Vérifiez que les comptes qui publient en MQTT via des scripts sont bien administrateurs.

<div class="ha-avis" markdown="1">
### 💬 Mon avis

La nouvelle carte est une très belle réponse à un vrai problème : passer à OpenStreetMap en vectoriel, avec un cache local, c’est plus beau **et** plus respectueux de la vie privée. Mais la vraie pépite, c’est **Triggered by** : diviser par deux le nombre d’automatisations rend une installation beaucoup plus facile à maintenir. Quant au serveur MCP en un clic, il ouvre la porte à des usages IA intéressants… à manier avec prudence et des droits bien choisis.
</div>

Vous fusionnez déjà vos automatisations avec « Triggered by » ? Partagez vos exemples sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— XAV59213</p>
