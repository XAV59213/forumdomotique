---
title: "SONOFF ZBMINIL2 ZigBee"
---

# SONOFF ZBMINIL2 ZigBee

- **Catégorie :** [Sonoff](https://forumdomotique.com/forums/55-sonoff/)
- **Sujet :** https://forumdomotique.com/forums/topic/121-sonoff-zbminil2-zigbee/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 22 mai 2025 à 16:49 (Europe/Paris)
- **Dernier message de XAV59213 :** 25 mai 2025 à 09:43 (Europe/Paris)

---

## Message 1 — 22 mai 2025 à 16:49 (Europe/Paris)

- **Identifiant :** `342`
- **Lien :** https://forumdomotique.com/forums/topic/121-sonoff-zbminil2-zigbee/#findComment-342

Salut [Dam](https://forumdomotique.com/profile/157-dam/)

Oui et Non

il existe une multitude de protocole comme tu la indiquer ton SONOFF ZBMINIL2 ZigBee passe par du ZigBee

il te faudra un serveur ZigBee comme dans home assistant ou du z2mqtt

dans tous les les cas il te faudra une base exemple smart life

il te faut le contrôleur une Gateway <https://www.amazon.fr/ZigBee-Bluetooth-Gateway-Bridge-T%C3%A9l%C3%A9commande/dp/B0BDYF1Y1J/ref=sr_1_3?crid=2UK5PXXGVYDP9&dib=eyJ2IjoiMSJ9.nO4hLeem2kYYe6kMhYchYK319SFSESQMjykOowhLxPxbJ9FdxAIfOIlnOA31HNIc6pxalFqkVai5uuxWCb7BjlVJh49gxV19D6yfj944nwxqFB4YTJVUIvuOCiHE8c9rYrS_uJBE6C9YajY_aGbi882sBxI5SjiVpl2mNfOW-gNNkZGS3mDKPz3WgHq1m5dha0caq30FhJQ0RWCXYsBU5AvDc66Itw0o1jkd6PDp-p-vC51N6QBSRootlU0eUcvE_9Di5OplxtgEKZT5CGt9mmDd6MSZDgJMYOdqmhAEWAM.WDEGtE4VgaDMO07IfqZfmR8tSUwyElmdB2rBsri3WnM&dib_tag=se&keywords=box%2Btuya%2Bzigbee&qid=1747925206&sprefix=box%2Btuya%2Caps%2C96&sr=8-3&th=1>

En domotique, plusieurs protocoles sont utilisés pour permettre la communication entre les appareils connectés (capteurs, éclairages, thermostats, etc.). Voici une liste des principaux protocoles en 2025, avec leurs caractéristiques clés :

### 1. **Wi-Fi**

- **Description** : Protocole réseau standard (IEEE 802.11) utilisé pour connecter des appareils à Internet ou en local.
- **Avantages** :

  - Large compatibilité (ampoules, caméras, prises intelligentes).
  - Haut débit, idéal pour le streaming ou les appareils gourmands (ex. : caméras 4K).
- **Inconvénients** :

  - Consommation énergétique élevée, moins adapté aux capteurs à pile.
  - Saturation possible si trop d’appareils sur le réseau.
- **Exemples** : Philips Hue (avec hub), caméras Ring, prises TP-Link.

### 2. **Zigbee**

- **Description** : Protocole sans fil basse consommation (IEEE 802.15.4) fonctionnant sur la bande 2.4 GHz.
- **Avantages** :

  - Faible consommation, idéal pour capteurs et appareils à pile (ex. : détecteurs de mouvement).
  - Réseau maillé (mesh) : chaque appareil relaie le signal, augmentant la portée.
  - Grande interopérabilité avec une hub (ex. : Zigbee2MQTT).
- **Inconvénients** :

  - Nécessite souvent un hub (ex. : Philips Hue Bridge, Aqara Hub).
  - Débit limité, non adapté pour le streaming.
- **Exemples** : Philips Hue, Aqara, IKEA Tradfri.

### 3. **Z-Wave**

- **Description** : Protocole sans fil basse consommation utilisant des fréquences sub-GHz (ex. : 868 MHz en Europe).
- **Avantages** :

  - Faible consommation, longue portée (jusqu’à 100 m en champ libre).
  - Réseau maillé, robuste et sécurisé.
  - Moins d’interférences que le Wi-Fi/Zigbee (fréquence différente).
- **Inconvénients** :

  - Moins de compatibilité que Zigbee (écosystème plus fermé).
  - Nécessite un hub (ex. : Homey, Fibaro).
- **Exemples** : Fibaro, Aeotec, Qubino.

### 4. **Bluetooth (BLE - Bluetooth Low Energy)**

- **Description** : Protocole sans fil à courte portée, souvent utilisé pour des appareils simples.
- **Avantages** :

  - Faible consommation, idéal pour capteurs ou petits appareils.
  - Pas besoin de hub si contrôle direct via smartphone.
- **Inconvénients** :

  - Portée limitée (~10-20 m).
  - Pas de réseau maillé natif (sauf avec extensions comme Bluetooth Mesh).
- **Exemples** : Certaines ampoules (ex. : Wiz), capteurs de température.

### 5. **Matter**

- **Description** : Protocole unifié lancé en 2022, fonctionnant sur Wi-Fi, Thread ou Ethernet, visant à standardiser la domotique.
- **Avantages** :

  - Interopérabilité entre écosystèmes (Google Home, Apple HomeKit, Amazon Alexa).
  - Sécurité renforcée et configuration simplifiée.
  - Supporte le réseau maillé via Thread.
- **Inconvénients** :

  - Adoption encore en cours en 2025, pas tous les appareils compatibles.
  - Parfois besoin d’un hub Matter (ex. : HomePod, Google Nest).
- **Exemples** : Appareils Eve, Nanoleaf, nouveaux produits Philips Hue.

### 6. **Thread**

- **Description** : Protocole sans fil basse consommation basé sur IPv6, conçu pour la domotique et souvent associé à Matter.
- **Avantages** :

  - Réseau maillé, faible latence, faible consommation.
  - Intégration native avec Matter.
- **Inconvénients** :

  - Nécessite un routeur Thread (ex. : Apple HomePod Mini, Google Nest Hub).
  - Écosystème encore en développement.
- **Exemples** : Eve Energy, Nanoleaf Essentials.

### 7. **KNX**

- **Description** : Protocole filaire (ou sans fil avec KNX-RF) pour l’automatisation des bâtiments, utilisé dans les installations professionnelles.
- **Avantages** :

  - Très robuste, adapté aux grandes installations (maisons, bureaux).
  - Grande variété d’appareils (éclairage, volets, climatisation).
- **Inconvénients** :

  - Coût élevé, installation complexe (souvent par des pros).
  - Moins courant dans les setups domestiques simples.
- **Exemples** : Gira, Schneider Electric, Jung.

### 8. **EnOcean**

- **Description** : Protocole sans fil sans pile, utilisant l’énergie ambiante (mouvement, lumière, chaleur).
- **Avantages** :

  - Pas de piles, idéal pour capteurs autonomes (ex. : interrupteurs).
  - Faible maintenance.
- **Inconvénients** :

  - Portée et débit limités.
  - Écosystème restreint.
- **Exemples** : Interrupteurs EnOcean, capteurs de fenêtre.

### 9. **LoRaWAN**

- **Description** : Protocole longue portée et basse consommation pour l’IoT, utilisé dans la domotique pour des applications spécifiques.
- **Avantages** :

  - Portée très longue (jusqu’à plusieurs km).
  - Idéal pour capteurs distants (ex. : agriculture, smart home extérieure).
- **Inconvénients** :

  - Débit très faible, non adapté pour des données volumineuses.
  - Nécessite une passerelle LoRa.
- **Exemples** : Capteurs environnementaux, gestion de parcs.

### 10. **Protocoles propriétaires**

- **Description** : Certains fabricants utilisent des protocoles spécifiques (ex. : Somfy RTS, Tuya).
- **Avantages** :

  - Optimisés pour leurs appareils.
  - Simples à configurer dans leur écosystème.
- **Inconvénients** :

  - Compatibilité limitée avec d’autres marques.
  - Dépendance au fabricant.
- **Exemples** : Somfy (volets roulants), Tuya (appareils low-cost).

### Conseils pour choisir :

- **Usage domestique simple** : Wi-Fi ou Bluetooth pour la facilité, Matter pour l’interopérabilité.
- **Maison connectée avancée** : Zigbee ou Z-Wave pour un réseau maillé robuste, avec un hub.
- **Grande installation** : KNX pour une solution professionnelle, ou LoRaWAN pour des capteurs distants.
- **Écosystème unifié** : Privilégiez Matter/Thread pour une compatibilité future.
- **Budget** : Zigbee et Tuya offrent des solutions abordables, tandis que KNX et EnOcean sont plus coûteux.

---

## Message 2 — 25 mai 2025 à 09:43 (Europe/Paris)

- **Identifiant :** `355`
- **Lien :** https://forumdomotique.com/forums/topic/121-sonoff-zbminil2-zigbee/#findComment-355

Bonjour Dam,

Pour débuter avec un système domotique économique,

je vous conseille d’utiliser un vieux PC équipé d’une clé USB Zigbee (environ 20-30€).

Avec un logiciel comme Home Assistant, vous pouvez créer un réseau maillé Zigbee robuste.

Les modules Zigbee (comme Aqara, Xiaomi ou Tuya) sont très abordables (5-15€ par module) et compatibles.

C’est une solution flexible et puissante pour un budget réduit.

### **Prérequis**

1. **Un vieux PC** :

   - Minimum : 2 Go de RAM, processeur 32/64 bits (même un vieux Intel Core 2 Duo ou équivalent convient).
   - Disque dur ou SSD avec au moins 32 Go d’espace libre.
   - Système d’exploitation : Windows, Linux ou macOS pour l’installation initiale (on installera un système dédié ensuite).
2. **Clé USB Zigbee** :

   - Exemples : **ConBee II**, **Sonoff Zigbee 3.0 USB Dongle**, **Texas Instruments CC2531** (environ 20-40€).
   - Vérifiez la compatibilité avec ZHA sur le site officiel de Home Assistant.
3. **Connexion réseau** : Ethernet ou Wi-Fi stable pour le PC.
4. **Clé USB ou disque externe** : Pour créer le support d’installation.
5. **Modules Zigbee** : Capteurs, ampoules, prises (ex. : Aqara, Xiaomi, Tuya) pour plus tard.

---

### **Étapes d’installation**

#### **1. Télécharger Home Assistant**

- Rendez-vous sur le site officiel : [home-assistant.io](https://home-assistant.io).
- Choisissez l’option **Home Assistant OS** (recommandé pour un vieux PC, car c’est un système dédié).
- Téléchargez l’image pour **PC générique (x86-64)** (fichier .img ou .qcow2).

#### **2. Créer un support d’installation**

- **Sur un autre ordinateur** :

  - Téléchargez un outil pour écrire l’image, comme **Balena Etcher** ([etcher.io](https://etcher.io)).
  - Insérez une clé USB (minimum 4 Go).
  - Ouvrez Balena Etcher, sélectionnez l’image Home Assistant téléchargée, choisissez la clé USB, puis cliquez sur **Flash**.
- Une fois terminé, la clé USB est prête.

#### **3. Installer Home Assistant OS sur le vieux PC**

- Branchez la clé USB sur le vieux PC.
- **Démarrez sur la clé USB** :

  - Éteignez le PC, puis redémarrez-le.
  - Accédez au menu de démarrage (souvent en appuyant sur **F12**, **F2**, **DEL** ou **ESC** au démarrage, selon la marque du PC).
  - Sélectionnez la clé USB comme périphérique de démarrage.
- L’installation de Home Assistant OS commence automatiquement :

  - Suivez les instructions à l’écran (généralement, il suffit de confirmer l’installation sur le disque dur).
  - Le processus formate le disque et installe le système (5-10 minutes).
- Une fois terminé, retirez la clé USB et redémarrez le PC.

#### **4. Configurer Home Assistant**

- **Accéder à l’interface** :

  - Sur un autre appareil (PC, smartphone) connecté au même réseau, ouvrez un navigateur et entrez : <http://homeassistant.local:8123>.
  - Si cela ne fonctionne pas, trouvez l’adresse IP du vieux PC (via votre routeur ou un scan réseau) et entrez http://[IP]:8123.
- **Première configuration** :

  - Créez un compte utilisateur (nom, mot de passe).
  - Configurez les paramètres de base (fuseau horaire, langue, etc.).
  - Home Assistant est maintenant opérationnel !

#### **5. Installer et configurer ZHA**

- **Brancher la clé Zigbee** :

  - Insérez la clé USB Zigbee dans un port USB du vieux PC.
- **Ajouter ZHA dans Home Assistant** :

  - Connectez-vous à l’interface Home Assistant.
  - Allez dans **Paramètres** > **Appareils et services** > **Ajouter une intégration**.
  - Recherchez **ZHA** et sélectionnez-le.
  - Home Assistant détecte automatiquement la clé Zigbee (ex. : /dev/ttyUSB0 ou nom similaire).
  - Confirmez et laissez ZHA s’initialiser (cela crée le réseau maillé Zigbee).
- **Vérifier la compatibilité** :

  - Si la clé ne fonctionne pas, vérifiez qu’elle est reconnue (voir **Paramètres** > **Système** > **Matériel**).
  - Certaines clés (ex. : CC2531) nécessitent un firmware mis à jour. Consultez la documentation ZHA ou le fabricant.

#### **6. Ajouter des appareils Zigbee**

- **Mettre un appareil en mode appairage** :

  - Pour chaque module Zigbee (ex. : capteur Aqara, prise Tuya), suivez les instructions du fabricant (souvent, appuyer longtemps sur un bouton ou allumer/éteindre plusieurs fois).
- **Appairer dans ZHA** :

  - Dans Home Assistant, allez dans **Paramètres** > **Appareils et services** > **ZHA** > **Ajouter des appareils**.
  - ZHA recherche les appareils en mode appairage.
  - Une fois détecté, l’appareil apparaît dans la liste (ex. : capteur de mouvement, ampoule).
- **Configurer les appareils** :

  - Attribuez un nom (ex. : “Capteur salon”).
  - Créez des automatisations (ex. : allumer une lampe si mouvement détecté).

#### **7. Optimiser le réseau maillé**

- **Réseau maillé Zigbee** :

  - Les appareils Zigbee (comme les prises ou ampoules) agissent comme **répéteurs** pour étendre la portée du réseau.
  - Placez des répéteurs stratégiquement (ex. : prises Zigbee à mi-chemin entre le PC et les capteurs éloignés).
- **Conseils** :

  - Évitez les interférences Wi-Fi (utilisez un canal Zigbee différent du Wi-Fi, configurable dans ZHA).
  - Ajoutez au moins 2-3 répéteurs pour un réseau robuste.

---
