---
title: "[TEST] Home Assistant Connect ZBT-1 : la clé Zigbee officielle pour Home Assistant"
description: "Salut ! La différence entre ZHA (Zigbee Home Automation) et Z2M (Zigbee2MQTT) réside dans leur approche, leur intégration, leur compatibilité et leur…"
image: /assets/images/og-default.png
date: 2025-05-22
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/153-test-home-assistant-connect-zbt-1-la-cl%C3%A9-zigbee-officielle-pour-home-assistant/">Lire et commenter sur Forum Domotique</a></p>

# [TEST] Home Assistant Connect ZBT-1 : la clé Zigbee officielle pour Home Assistant

- **Catégorie :** [Box & Matériel](https://forumdomotique.com/forums/97-box-mat%C3%A9riel/)
- **Sujet :** https://forumdomotique.com/forums/topic/153-test-home-assistant-connect-zbt-1-la-cl%C3%A9-zigbee-officielle-pour-home-assistant/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 22 mai 2025 à 17:08 (Europe/Paris)
- **Dernier message de XAV59213 :** 12 juin 2025 à 19:51 (Europe/Paris)

---

## Message 1 — 22 mai 2025 à 17:08 (Europe/Paris)

- **Identifiant :** `343`
- **Lien :** https://forumdomotique.com/forums/topic/153-test-home-assistant-connect-zbt-1-la-cl%C3%A9-zigbee-officielle-pour-home-assistant/#findComment-343

Salut a tous ,

Attention zha et z2mqtt

c'est pas la même affaire

Salut ! La différence entre **ZHA** (Zigbee Home Automation) et **Z2M** (Zigbee2MQTT) réside dans leur approche, leur intégration, leur compatibilité et leur flexibilité pour gérer un réseau Zigbee dans un système domotique, notamment avec **Home Assistant**. Voici un comparatif clair et concis pour t’aider à choisir :

### 1. **Définition**

- **ZHA** :

  - Intégration native de Home Assistant pour gérer les appareils Zigbee.
  - Utilise directement la bibliothèque bellows, zigpy ou équivalent pour communiquer avec une clé Zigbee (coordinateur).
- **Z2M** (Zigbee2MQTT) :

  - Solution open-source indépendante qui traduit les messages Zigbee en MQTT (Message Queuing Telemetry Transport).
  - Fonctionne comme un pont entre le réseau Zigbee et Home Assistant (ou d’autres systèmes) via un broker MQTT.

### 2. **Installation et configuration**

- **ZHA** :

  - **Plus simple** à configurer : Intégration directe dans Home Assistant (menu "Intégrations" > Ajouter > ZHA).
  - Plug-and-play si la clé Zigbee est compatible (ex. : Sonoff ZBDongle-P/E, ConBee II).
  - Pas besoin de composants externes (comme un broker MQTT).
  - Configuration via l’interface graphique de Home Assistant.
- **Z2M** :

  - **Plus complexe** à installer :

    - Nécessite un broker MQTT (ex. : Mosquitto) installé et configuré.
    - Installation de Zigbee2MQTT via Docker, Node.js, ou add-on Home Assistant.
    - Configuration via un fichier configuration.yaml ou interface web (optionnel).
  - Demande une clé Zigbee compatible (liste plus large que ZHA).
  - Plus de dépendances, mais interface web dédiée pour gérer le réseau.

### 3. **Compatibilité des appareils**

- **ZHA** :

  - Compatible avec de nombreux appareils Zigbee conformes au standard ZHA (éclairage, capteurs, prises).
  - Supporte bien les grandes marques (Philips Hue, IKEA Tradfri, Aqara).
  - **Limitation** : Moins flexible pour les appareils non standards ou propriétaires, car dépend de la bibliothèque zigpy.
  - La liste des appareils supportés dépend des mises à jour de zigpy.
- **Z2M** :

  - **Meilleure compatibilité** : Supporte plus de 2600 appareils (en 2025), y compris des dispositifs non standards ou exotiques.
  - Communauté très active qui ajoute rapidement de nouveaux appareils via des "quirks" ou définitions personnalisées.
  - Permet des ajustements manuels (ex. : exposer des fonctionnalités spécifiques via MQTT).
  - Exemple : Certains capteurs Aqara ou Tuya fonctionnent mieux avec Z2M.

### 4. **Flexibilité et fonctionnalités**

- **ZHA** :

  - Intégré nativement, donc fluide dans Home Assistant (pas de latence due à MQTT).
  - Gestion des appareils directement dans l’interface HA (groupes, scènes, automatisations).
  - Supporte les mises à jour OTA (over-the-air) pour certains appareils (ex. : IKEA, Philips).
  - **Limitation** : Moins de contrôle granulaire sur le réseau Zigbee (ex. : difficile de forcer un appareil à utiliser un routeur spécifique).
  - Pas d’interface réseau dédiée (visualisation basique dans HA).
- **Z2M** :

  - Interface web dédiée pour visualiser et gérer le réseau (carte du maillage, LQI, routage).
  - Contrôle précis : Forcer des routes, ajuster la puissance des clés (ex. : 20 dBm sur Sonoff ZBDongle-P), exposer des attributs spécifiques.
  - Supporte les mises à jour OTA pour une large gamme d’appareils.
  - Compatible avec d’autres plateformes (Jeedom, Domoticz, Node-RED) grâce à MQTT.
  - **Inconvénient** : Légère latence possible (due à MQTT) et dépendance au broker MQTT.

### 5. **Performance et stabilité**

- **ZHA** :

  - Très stable pour les setups simples et les appareils standards.
  - Moins de risques de pannes liées à des dépendances externes.
  - Peut être limité pour les grands réseaux (>50 appareils) en termes de gestion du maillage.
- **Z2M** :

  - Très robuste pour les grands réseaux (testé avec >200 appareils).
  - Meilleure gestion du maillage grâce à l’interface et aux outils de diagnostic.
  - Stabilité dépend du broker MQTT et de la configuration réseau (si MQTT tombe, Z2M perd la connexion avec HA).

### 6. **Communauté et maintenance**

- **ZHA** :

  - Maintenu par l’équipe Home Assistant et les contributeurs de zigpy.
  - Moins de documentation communautaire spécifique, mais intégré dans les guides HA.
  - Évolue avec Home Assistant, donc mises à jour fréquentes.
- **Z2M** :

  - Projet communautaire très actif avec une documentation détaillée ([zigbee2mqtt.io](https://www.zigbee2mqtt.io/)).
  - Support rapide pour nouveaux appareils via GitHub.
  - Évolutions fréquentes, mais nécessite de suivre les mises à jour manuellement (sauf via add-on).

### 7. **Cas d’usage**

- **Choisis ZHA si** :

  - Tu veux une solution **simple**, rapide à configurer, et intégrée à Home Assistant.
  - Tu as un petit réseau (<50 appareils) avec des marques standards (Philips, IKEA).
  - Tu n’as pas envie de gérer un broker MQTT ou une interface séparée.
- **Choisis Z2M si** :

  - Tu as un grand réseau ou des appareils non standards/exotiques (ex. : Tuya, Xiaomi).
  - Tu veux une **visualisation avancée** du réseau Zigbee et un contrôle granulaire.
  - Tu utilises plusieurs plateformes domotiques (pas seulement Home Assistant).
  - Tu es à l’aise avec une configuration plus technique.

### Exemple avec ta clé Sonoff

- **ZHA** : Branche ta clé Sonoff ZBDongle-P/E, configure ZHA dans Home Assistant, et appaire directement les appareils. Simple, mais moins d’options pour optimiser la portée ou gérer des appareils complexes.
- **Z2M** : Installe Mosquitto, configure Z2M avec ta clé, et utilise l’interface web pour voir le maillage. Plus de travail initial, mais tu peux passer ta clé en mode routeur (comme demandé avant) ou ajuster la puissance.

### En résumé

| **Critère** | **ZHA** | **Z2M** |
| --- | --- | --- |
| **Facilité** | Très simple, natif HA | Plus complexe (MQTT requis) |
| **Compatibilité** | Bonne, mais limitée aux standards | Excellente, >2600 appareils |
| **Flexibilité** | Basique, intégré à HA | Avancée, interface web, multi-plateforme |
| **Performance** | Stable, petits réseaux | Robuste, grands réseaux |
| **Communauté** | Intégrée à HA, moins de docs | Très active, docs détaillées |

### Conseil

- Si tu débutes ou veux du plug-and-play, commence avec **ZHA**.
- Si tu as des appareils spécifiques (ex. : Aqara, Tuya) ou veux optimiser un grand réseau (avec ta clé Sonoff en mode routeur), passe à **Z2M**.

---

## Message 2 — 12 juin 2025 à 19:51 (Europe/Paris)

- **Identifiant :** `446`
- **Lien :** https://forumdomotique.com/forums/topic/153-test-home-assistant-connect-zbt-1-la-cl%C3%A9-zigbee-officielle-pour-home-assistant/#findComment-446

Si tu peux flasher <https://www.hacf.fr/zigbee2mqtt-config/#:~:text=Pour%20flasher%20la%20cl%C3%A9%20Skyconnect,Zigbee%20et%20emp%C3%AAcher%20le%20flashage>. <https://github.com/mercenaruss/zigstar_addons> J ai jamais tester je suis en dongle

---
