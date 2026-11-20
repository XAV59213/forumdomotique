---
title: "CHOIX BOX DOMOTIQUE"
description: "Merci pour ton message détaillé ! Je vais te conseiller sur une box domotique multiprotocole qui corresponde à tes besoins : une interface graphique…"
image: /assets/images/og-default.png
date: 2025-11-27
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/543-choix-box-domotique/">Lire et commenter sur Forum Domotique</a></p>

# CHOIX BOX DOMOTIQUE

- **Catégorie :** [Choisir sa box domotique](https://forumdomotique.com/forums/100-choisir-sa-box-domotique/)
- **Sujet :** https://forumdomotique.com/forums/topic/543-choix-box-domotique/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 27 novembre 2025 à 13:16 (Europe/Paris)

---

## Message 1 — 27 novembre 2025 à 13:16 (Europe/Paris)

- **Identifiant :** `1357`
- **Lien :** https://forumdomotique.com/forums/topic/543-choix-box-domotique/#findComment-1357

Bonjour Bruno,

Merci pour ton message détaillé ! Je vais te conseiller sur une box domotique multiprotocole qui corresponde à tes besoins : une interface graphique intuitive, une bonne application iPhone (plus avancée que celle de Jeedom que tu trouves sommaire), et une compatibilité avec tes protocoles actuels (KNX, Z-Wave, WiFi, RF 433 MHz). Tu prévois aussi d’ajouter une station météo et un assistant vocal, et tu mentionnes l’intérêt pour HomeKit. Je me base sur des options populaires et bien supportées en 2025, en tenant compte de la facilité d’accès et de l’évolutivité.

**Mes recommandations principales**

Après analyse des options disponibles, je te conseille deux box qui se distinguent pour leur polyvalence et leur facilité d’utilisation. Elles supportent tous tes protocoles via des intégrations natives ou simples à ajouter, et ont d’excellentes apps mobiles. Je priorise celles qui sont “plug-and-play” autant que possible, tout en étant puissantes.

1.  **Home Assistant (HA) – Ma recommandation n°1, surtout si tu veux de la personnalisation et HomeKit**

•  **Pourquoi ça correspond ?**

•  **Protocoles supportés** :

•  KNX : Intégration native excellente pour contrôler tes lumières, volets, prises et panels tactiles.

•  Z-Wave : Support complet pour tes modules Fibaro (et bien plus).

•  RF 433 MHz : Via l’intégration RTL433 ou similaire, pour ton relais de lumière piscine (facile à intégrer si compatible ; sinon, remplace par un module Z-Wave ou Zigbee).

•  WiFi : Nombreuses intégrations pour des commutateurs comme Tangoo (via Tuya ou API générique si compatible ; sinon, remplace par un Shelly ou équivalent WiFi domotique).

•  **Ajouts futurs** :

•  Station météo : Support pour de nombreux modèles (Ecowitt, Ambient Weather, Netatmo, etc.) via intégrations dédiées.

•  Assistant vocal : Compatible avec Google Assistant, Amazon Alexa, et Siri (via HomeKit). Tu peux même utiliser HA Voice pour du contrôle local sans cloud.

•  **Interface et app iPhone** : L’interface web est très personnalisable avec des dashboards graphiques (Lovelace UI) – bien plus avancée que Jeedom. L’app iOS officielle (Home Assistant Companion) est excellente : notifications push, widgets, géolocalisation, et intégration Siri. Les retours en 2025 la décrivent comme fluide et complète, avec des mises à jour régulières.

•  **HomeKit** : Oui ! HA peut exposer tes devices à HomeKit via un bridge intégré, ce qui permet de tout contrôler depuis l’app Maison d’Apple. Idéal si tu es dans l’écosystème Apple.

•  **Facilité d’accès** : C’est open-source et gratuit, mais nécessite un peu de configuration initiale (pas plus compliquée que Jeedom). Tu peux l’installer sur un Raspberry Pi, un mini-PC, ou même une box prête à l’emploi comme le Home Assistant Green ou Yellow (environ 100-200€). Communauté énorme pour l’aide.

•  **Prix** : Logiciel gratuit ; hardware de base ~150€.

•  **Inconvénients** : Plus technique au départ si tu veux des automatisations complexes, mais pour une utilisation basique, c’est accessible.

•  **Où commencer** : Télécharge l’app iOS et teste une démo sur <https://testhomeassistant.fr> [@CedricMD](https://forumdomotique.com/profile/7-cedricmd/) a mis à disposition un home assistant test pour découvrir home assistant.

2.  **[Homey Pro](https://forumdomotique.com/tests/box-domotiques/homey-pro-box-domotique-avis-test-complet/) – Une alternative plus “prête à l’emploi” si tu veux moins de configuration**

•  **Pourquoi ça correspond ?**

•  **Protocoles supportés** :

•  KNX : Support via intégrations communautaires (apps tierces, confirmées par des utilisateurs en 2025).

•  Z-Wave : Natif et robuste pour tes Fibaro.

•  RF 433 MHz : Natif (attention : désactivé dans certains pays comme les US, mais OK en Europe).

•  WiFi : Oui, pour des devices comme Tangoo (via apps spécifiques si compatible ; sinon, remplace).

•  **Ajouts futurs** :

•  Station météo : Intégrations pour Netatmo, Weather Underground, etc.

•  Assistant vocal : Compatible avec Google Assistant, Alexa, et Siri (via Siri Shortcuts dans l’app). Pas de HomeKit natif, mais possible via Matter/Thread pour certains devices.

•  **Interface et app iPhone** : Interface graphique simple et visuelle avec des “Flows” pour les automatisations. L’app iOS est très bien notée (disponible sur l’App Store) : intuitive, avec dashboards, widgets, et intégration Siri. Les reviews 2025 la louent pour sa simplicité par rapport à Jeedom – pas de menus compliqués, tout est fluide.

•  **HomeKit** : Pas natif, mais compatible via Matter pour exposer des devices à l’app Maison. Si HomeKit est prioritaire, HA est mieux.

•  **Facilité d’accès** : Très user-friendly, plug-and-play. La box est compacte et gère tout localement (pas de cloud obligatoire).

•  **Prix** : Environ 300-400€ pour la [Homey Pro](https://forumdomotique.com/tests/box-domotiques/homey-pro-box-domotique-avis-test-complet/) (modèle 2023 ou Mini pour 2025).

•  **Inconvénients** : Moins personnalisable que HA, et certaines intégrations avancées nécessitent des apps payantes.

•  **Où commencer** : Visite [homey.app](https://homey.app) pour voir les compatibilités.

**Autres options à considérer rapidement**

•  **Apple Home (avec HomePod/Apple TV comme hub)** : Si tu veux tout en HomeKit natif, c’est simple avec une super app iPhone (Maison). Mais pour tes protocoles non-HomeKit (KNX, Z-Wave, RF), il faut des bridges comme Thinka (pour KNX et Z-Wave, ~300€). Pas idéal pour multiprotocole sans ajouts, et moins flexible pour la piscine/RF.

•  **SmartThings (Aeotec ou Samsung)** : Bon pour Z-Wave et WiFi, app iOS correcte, mais support KNX et RF limité (besoin de bridges). HomeKit via Matter, mais pas aussi complet.

•  **Éviter Jeedom** : Comme tu l’as dit, l’app est basique, et il y a mieux pour l’interface.

**Conseils généraux**

•  **Pour la piscine** : Vérifie la compatibilité Tangoo/relais RF avec la box choisie (souvent via API ou intégrations). Si non, opte pour des modules Shelly (WiFi) ou Z-Wave – faciles à changer et compatibles avec HA/Homey.

•  **Teste avant d’acheter** : Beaucoup de ces systèmes ont des communautés (Reddit, forums HA/Homey) où tu peux poser des questions spécifiques à ton setup.

•  **Sécurité et local** : Privilégie les box qui fonctionnent localement (comme HA et Homey) pour éviter les dépendances cloud.

•  Si tu as un écosystème Apple fort, HA avec HomeKit bridge est parfait.

Si tu me donnes plus de détails (budget, niveau technique, ou préférence pour HomeKit), je peux affiner ! Qu’en penses-tu ?

---
