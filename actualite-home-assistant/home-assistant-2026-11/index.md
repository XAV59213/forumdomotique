---
layout: ha-release
title: "Home Assistant 2026.11 : HACS devient le Marketplace officiel, et c’est la plus grosse version jamais publiée"
short_title: "2026.11 : HACS devient le Marketplace"
description: "Home Assistant 2026.11 (4 novembre 2026) en français : HACS devient le Marketplace officiel, exclusions dans les cibles et 38 nouvelles intégrations."

excerpt_fr: "HACS entre dans Home Assistant sous le nom de Marketplace, on peut exclure une pièce d’une cible, les sections de dashboard se remplissent seules et les noms d’entités sont repensés. La plus grosse version de l’histoire."
image: /actualite-home-assistant/home-assistant-2026-11/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.11, novembre 2026"
date: 2026-11-04
release_date: 2026-11-04
section: actualite-ha
featured: true
version: "2026.11"
month: "Novembre 2026"
official_title: "2026.11: A lot in store!"
release_url: https://www.home-assistant.io/blog/2026/11/04/release-202611/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.11/
tags: [home-assistant, mise-a-jour, 2026.11, hacs, marketplace]
seo:
  type: NewsArticle
gallery:
  - src: images/marketplace-settings.webp
    caption: "Le Marketplace apparaît dans les Paramètres, entre Apps et Tableaux de bord."
  - src: images/marketplace-project.webp
    caption: "La fiche d’un projet : téléchargements, étoiles GitHub, version de Home Assistant requise."
  - src: images/marketplace-warning.webp
    caption: "L’avertissement affiché à la première ouverture : tout est créé par la communauté."
  - src: images/marketplace-group-by.webp
    caption: "Les listes du Marketplace se regroupent par état, type ou source."
  - src: images/exclude-target-details.webp
    caption: "Exclure des éléments d’une cible : ici, le rez-de-chaussée sauf certaines entités."
  - src: images/automatic-section-picker.webp
    caption: "Choisir une section automatique, avec aperçu en direct."
  - src: images/entities-section-editor.webp
    caption: "La section automatique « Entités » : toutes les lumières du premier étage, par exemple."
  - src: images/light-tile-color.webp
    caption: "Une bande de couleur (teinte) directement sur les tuiles des lumières."
  - src: images/action-history.webp
    caption: "Le nouvel onglet Historique des actions dans Paramètres › Outils."
  - src: images/statistics-delete-range.webp
    caption: "Supprimer les statistiques sur une plage horaire seulement, avec aperçu."
  - src: images/lorawan-page.webp
    caption: "La page LoRaWAN : connexions, appareils et liens vers leurs consoles."
  - src: images/lorawan-network.webp
    caption: "La carte du réseau LoRaWAN : quelles passerelles reçoivent quels appareils."
---

C’est Frenck qui le dit : la **2026.11**, sortie le **4 novembre 2026**, est « **la plus grosse version jamais publiée, et de loin** ». Et elle contient une annonce historique pour tous ceux qui, comme moi, publient des intégrations communautaires : **HACS, le Home Assistant Community Store, est désormais intégré à Home Assistant sous le nom de Marketplace**. Ajoutez à cela les **exclusions dans les cibles**, des **sections de dashboard qui se remplissent seules**, un **nommage des entités repensé** après plus de quatre ans de travail, des caméras **Matter**, le **LoRaWAN** et **38 nouvelles intégrations**.

<div class="ha-callout info" markdown="1">
**En bref**
- 🛍️ **HACS devient le Marketplace**, intégré à Home Assistant (Paramètres › Marketplace).
- 🎯 **Exclure** une entité, un appareil, une pièce, un étage ou une étiquette d’une cible.
- 🧩 **Sections automatiques** et copier-coller de sections dans les dashboards.
- 🏷️ **Nommer une fois** : Home Assistant ajoute le contexte (appareil, pièce) là où c’est utile.
- 🔍 Outils « **Pourquoi est-ce arrivé ?** », caméras **Matter 1.5**, **LoRaWAN**, **Zigbee Green Power**, disques locaux pour les sauvegardes.
</div>

## ✨ Les nouveautés phares

### 🛍️ Bienvenue dans le Marketplace

Depuis des années, la communauté publie intégrations personnalisées, cartes, thèmes et templates via **HACS**. Avec cette version, **HACS fait partie de Home Assistant** sous le nom de **Marketplace**. Il suit le cycle de publication normal, fonctionne avec **tous les types d’installation** (y compris Home Assistant Container) et reste **entièrement gratuit**, ce qui ne changera pas.

{% include ha-figure.html src="images/marketplace-settings.webp" caption="Le Marketplace, directement dans les Paramètres." %}

**Installer une intégration communautaire, pas à pas :**
1. Ouvrez **Paramètres › Marketplace** (rien à installer, il est fourni avec Home Assistant ; il faut être administrateur).
2. À la première ouverture, lisez l’avertissement et cochez **I understand the risks and agree** : tout ce qui s’y trouve est créé par la communauté, sans être testé, audité ni supporté par le projet Home Assistant.
3. Cherchez le projet, consultez sa fiche (nombre de téléchargements, étoiles GitHub, version de Home Assistant requise).
4. Cliquez sur **Install** : vous arrivez **directement dans l’assistant de configuration, sans redémarrage**. (Les *mises à jour* demandent encore un redémarrage, qu’une réparation propose de faire pour vous.)

{% include ha-figure.html src="images/marketplace-project.webp" caption="La fiche d’un projet (ici Spook), installé et prêt à être configuré." %}

**Ce qui change par rapport à HACS :**
- **Pas besoin de compte GitHub** pour installer ou mettre à jour.
- Chaque projet installé a son **entité de mise à jour** : les mises à jour apparaissent dans **Paramètres › Mises à jour**, à côté de celles de Home Assistant.
- Regroupement par état, type ou source ; filtre « catalogue communautaire » / « dépôts personnalisés » ; désinstallation multiple ; les mises à jour ignorées ne restent plus en haut de la liste ; recherche et filtres conservés dans l’URL (pratique pour partager un lien).

**Dépôts personnalisés :** un projet absent du catalogue s’ajoute avec **Add from link** et l’URL du dépôt. Cela nécessite une **connexion GitHub**, par connexion d’appareil (*device sign-in*) : vous validez sur GitHub sans saisir votre mot de passe dans Home Assistant, et l’accès est limité aux informations publiques.

**Vous utilisez déjà HACS ? Rien à faire.** Home Assistant le migre au premier démarrage : tout ce que vous avez installé reste installé et continue de recevoir ses mises à jour, vos dépôts personnalisés et entités de mise à jour sont conservés, et **les liens qui pointaient vers HACS ouvrent désormais le Marketplace**. En revanche, l’installateur HACS s’arrête à la 2026.11 : une installation séparée de HACS n’est plus possible, et l’ancien HACS ne recevra plus de nouvelles versions.

🙏 Un grand merci à **@ludeeus**, fondateur de HACS, qui l’a confié à l’Open Home Foundation il y a environ un an et demi, ainsi qu’aux mainteneurs et développeurs qui ont bâti cet écosystème.

### 🎯 Exclure des éléments d’une cible

« Allume toutes les lumières du rez-de-chaussée, **sauf celle de la cuisine** » : c’est désormais possible. On peut **exclure des entités, appareils, pièces, étages ou étiquettes** d’une cible, dans les déclencheurs, conditions et actions, pour les automatisations comme pour les scripts.

{% include ha-figure.html src="images/exclude-target-details.webp" caption="Les détails d’une cible avec des cases à cocher pour inclure ou exclure." %}

Chaque exclusion est listée sous la cible concernée avec le nombre d’entités retirées ; une exclusion sans effet est rangée à part. Et elle reste « intelligente » : Home Assistant la recalcule à chaque exécution. L’éditeur gagne aussi : **remplacer une étape**, **« Is not »** dans le déclencheur d’état, éléments **récemment utilisés**, **Personnes** dans le sélecteur de cibles, retour de **Edit ID**, et **Annuler** après un couper.

### 🧩 Des sections de dashboard qui se remplissent seules

- **Copier, couper et coller** une section, y compris vers une autre vue ou un autre dashboard.
- À la création d’une section, choisissez **manuelle**, **automatique** ou **celle que vous venez de copier**. Sections automatiques : **Common controls** (entités les plus utilisées), **Device** (les entités d’un appareil, avec son nom, sa pièce et sa batterie) et **Entities** (toutes les entités d’un type, par exemple toutes les lumières du rez-de-chaussée : une nouvelle lumière y apparaît d’elle-même).
- Depuis la page d’un appareil : **Add to… › Add to a dashboard**.
- **Convert to manual section** pour reprendre la main.

{% include ha-figure.html src="images/automatic-section-picker.webp" caption="Le choix d’une section automatique, avec aperçu." %}

Nouveautés de cartes : carte **Date**, badge **Alert**, éditeur visuel pour la carte **Alert**, consigne de thermostat par boutons ou curseur, et une **bande de couleur** sur les tuiles des lumières.

### 🏷️ Nommer une fois, Home Assistant ajoute le contexte

Après plus de quatre ans de discussions (« comment nommez-vous vos appareils ? »), le nommage est repensé : vous nommez une entité « **Température** » ; Home Assistant sait qu’elle appartient au « **Thermostat** » de la « **Chambre** » et affiche par défaut « Thermostat Température », une carte pouvant ajouter la pièce (« Chambre Thermostat Température »). Le même nom, structuré de la même façon, partout.

À savoir :
- Renommer une entité ne renomme **que** l’entité ; pour changer le nom de l’appareil, renommez l’appareil.
- Vos **noms personnalisés sont conservés** ; si un nom affiché change, l’ancien reste un **alias** pour la voix.
- **Les identifiants d’entité ne changent pas** : automatisations et scripts continuent de fonctionner.
- Templates : l’attribut `friendly_name` est appelé à être déprécié ; préférez `entity_name()`, `device_name()` et `area_name()`.
- ⚠️ C’est un changement **non rétrocompatible** : certains noms paraîtront différents, surtout sur vos dashboards.

### 🔍 « Pourquoi est-ce arrivé ? »

- Filtre **Triggered by** dans l’**Activité** (ce qu’a fait une personne, une automatisation…).
- Une trace suit désormais le **script appelé** par une automatisation.
- **Logs en direct par intégration** quand le débogage est actif, et filtre par intégration dans **Paramètres › Système › Journaux**.
- **Supprimer une mauvaise mesure** : dans **Paramètres › Outils › Statistiques**, effacez seulement une **plage horaire** (avec aperçu), sans perdre tout l’historique.
- **Zoom** par simple glisser sur les graphiques.
- Nouvel onglet **Action history** dans **Paramètres › Outils** : chaque action appelée, sa cible, sa cause, son utilisateur et ses données (copiables en YAML).

{% include ha-figure.html src="images/statistics-delete-range.webp" caption="Supprimer les statistiques d’une seule plage horaire." %}

### 📹 Caméras Matter et audio bidirectionnel

L’intégration **Matter** prend en charge les **caméras Matter 1.5** (vidéo en direct et instantanés), à condition d’avoir un serveur Matter assez récent. Nouvelle fonction **Labs** : l’**audio bidirectionnel** ajoute un bouton « parler » au flux en direct (caméras Matter et **Reolink** pour commencer). Le navigateur exigeant une connexion sécurisée pour le micro, cela fonctionne pour l’instant en **HTTPS**.

### 💾 Sauvegardes et médias sur disque local

Outre le stockage réseau, on peut ajouter un **disque interne ou USB** : **Paramètres › Système › Stockage › Add storage › Local disk**. Le disque est reconnu par son identifiant de système de fichiers (il survit aux redémarrages) et une réparation prévient s’il est débranché. La restauration ne fait plus de copie temporaire complète, ce qui économise espace et temps.

### 📶 LoRaWAN et Zigbee Green Power

- **LoRaWAN** : le protocole longue portée et basse consommation des capteurs au fond du jardin. Connectez votre serveur **ChirpStack** ou **The Things Network**, et Home Assistant propose l’intégration de l’appareil (par exemple **SenseCAP**). Une page **Paramètres › Connectivité › LoRaWAN** montre connexions, appareils et carte du réseau.
- **Zigbee Green Power** dans ZHA : les interrupteurs **sans pile** (alimentés par la pression du doigt), comme les fameux *Friends of Hue*, sont enfin pris en charge.

### ⚡ De la puissance à l’énergie en une étape

Un appareil qui ne remonte qu’une **puissance en watts** ? En l’ajoutant au tableau **Énergie**, Home Assistant propose de **créer automatiquement le capteur d’énergie** correspondant (idem pour un débit de gaz ou d’eau).

## 🧩 Nouvelles intégrations

✅ **38 nouvelles intégrations**, un record. Parmi elles :

- **Marketplace** (le nouveau HACS), **LoRaWAN**, **ChirpStack**, **The Things Network**, **SenseCAP**.
- **Flic** (boutons Flic 2, Duo et Twist en Bluetooth, sans compte), **HP Printer** (encre et état, en local), **AnyList**, **Seafile**, **Foreca** (météo), **Škoda** (Škoda Connect).
- Énergie : **BLUETTI Modbus**, **KACO RS485**, **Solyx Energy Cloud**, **ENGIE Belgium**, **Hydro-Québec Peak Events** (les *événements de pointe*, pour nos amis québécois 🇨🇦), **ecosmart**.
- Confort : **aerosmart**, **Helty Flow Cloud**, **HAVEN IAQ**, **Hase iQ** (poêles à bois), **SmartyPlants**.
- Infrarouge : **Philips Infrared**, **SilverCrest Infrared**, **Alpha Bidet Infrared** ; et aussi **Bosch Smart Camera**, **Grandstream Home**, **Marantz RS-232**, **OKOK Scale**, **Spin EV Charger**, **SteamVR Base Station**, **Debug console** (pour développeurs)…

**Bitcoin**, **Folder**, **Keyboard Remote**, **OpenWrt (ubus)** et **Sky Hub** passent par l’interface. **Flipr** est retiré, l’entreprise ayant été liquidée (une version minimale subsiste pour afficher des alertes de configuration).

## 🔧 Améliorations notables

- **ESPHome** : partage d’un port série ; **Tuya** : sèche-serviettes et bien d’autres ; **UniFi Protect** : Alarm Hub ; **ZHA** : chaque groupe a son propre appareil ; **Bosch SHC** : alarme intrusion pilotable ; **Amazon Alexa** : flux caméra sur Echo Show.
- Infrarouge et radiofréquence : plateforme IR pour **Shelly**, **réception RF**, climat pour **LG** et **Gree Infrared**.
- Triggers et conditions **radon**, exposition de nombreuses entités à la fois à Assist, **Ctrl/Cmd + Maj + Y** pour basculer en YAML, **groupes de calendriers**, l’IA peut **lire le journal système** pour aider au dépannage, templates de chauffe-eau et de lecteurs multimédias.

## ⚠️ Breaking changes à surveiller

La liste est longue (version record oblige). Les plus importants :

- **Noms d’entités** : composés désormais du nom de l’entité et de son contexte (voir plus haut). Vérifiez vos dashboards.
- **Authentification** : si vous accédez à Home Assistant via une **IP non locale** (IP publique, IPv6 globale, adresse **Tailscale** `100.64.0.0/10`), l’adresse du navigateur doit correspondre exactement (schéma, hôte, port) à celle vue par Home Assistant, sinon « Invalid client id ». Un reverse proxy déclaré comme *trusted proxy* continue de fonctionner.
- **Soleil et calendrier** : le signe de l’`offset` décide désormais (négatif = avant, positif = après). Vérifiez vos déclencheurs YAML.
- **Dépendances Python** : plus d’installation dans le dossier `deps` de la configuration (Core seul).
- **ZHA** : si vous ciblez l’**appareil coordinateur** pour piloter vos groupes, ciblez désormais les entités ou nouveaux appareils de groupe.
- **Z-Wave** : serveur zwave-js-server à mettre à jour ; entités des sous-points de terminaison déplacées sur des appareils enfants.
- **Frontend** : Chrome 67, Safari 15.4 ou Firefox 98 minimum.
- **Telegram** : l’ancienne plateforme `notify` (`platform: telegram`) est supprimée.
- **MQTT** : les entités sans `unique_id` n’utilisent plus leur configuration `device` ; **Matter**, **Tuya**, **Xiaomi BLE/Home**, **Ring**, **UniFi Protect**, **Uptime Kuma** (2.0 minimum)… : voir les notes officielles.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.11**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-11" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète** (indispensable pour une version de cette taille).
2. Lisez la liste des breaking changes officielle, en particulier si vous utilisez **Tailscale ou une IP publique**, **ZHA avec groupes**, **Z-Wave** ou des déclencheurs **sun** avec `offset`.
3. Mettez à jour directement en **2026.11.3**.
4. Ouvrez ensuite **Paramètres › Marketplace** : vos projets HACS doivent tous y figurer. Vérifiez vos dashboards, où les nouveaux noms d’entités sont les plus visibles.

<div class="ha-avis" markdown="1">
### 💬 Mon avis

En tant que développeur d’intégrations distribuées via HACS (Freebox Homexa, Chauffage fil pilote, Jour Férié…), je vois l’arrivée du **Marketplace** comme une reconnaissance énorme pour tout l’écosystème communautaire. Installer une intégration **sans redémarrer** et sans compte GitHub, c’est ce qui manquait aux débutants. Les exclusions dans les cibles et les sections automatiques sont du même niveau : moins de bricolage, plus de logique. Seul conseil : prenez le temps de lire les breaking changes, cette version touche à beaucoup de choses.
</div>

Vous êtes passé au Marketplace ? Racontez votre migration sur [Forum Domotique](https://forumdomotique.com/) !

<p class="ha-signature">— XAV59213</p>
