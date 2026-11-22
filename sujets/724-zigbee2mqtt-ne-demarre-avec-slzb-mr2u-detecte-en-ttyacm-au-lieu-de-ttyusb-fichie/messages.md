---
title: "Zigbee2MQTT ne démarre avec SLZB-MR2U détecté en ttyACM au lieu de ttyUSB, fichier introuvable"
description: "Puisque ton dongle est un SLZB-MR2U (version USB multi-radio similaire au MR4U du tuto que j ai partagé, mais sans Ethernet/PoE natif), je vais adapter ma…"
image: /assets/images/vignettes-themes/zigbee.jpg

date: 2026-01-30
cover_alt: "Vignette de rubrique Zigbee — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/724-zigbee2mqtt-ne-d%C3%A9marre-avec-slzb-mr2u-d%C3%A9tect%C3%A9-en-ttyacm-au-lieu-de-ttyusb-fichier-introuvable/">Lire et commenter sur Forum Domotique</a></p>

# Zigbee2MQTT ne démarre avec SLZB-MR2U détecté en ttyACM au lieu de ttyUSB, fichier introuvable

- **Catégorie :** [Dépannage et Support Technique](https://forumdomotique.com/forums/19-d%C3%A9pannage-et-support-technique/)
- **Sujet :** https://forumdomotique.com/forums/topic/724-zigbee2mqtt-ne-d%C3%A9marre-avec-slzb-mr2u-d%C3%A9tect%C3%A9-en-ttyacm-au-lieu-de-ttyusb-fichier-introuvable/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 30 janvier 2026 à 08:09 (Europe/Paris)
- **Dernier message de XAV59213 :** 15 février 2026 à 22:03 (Europe/Paris)

---

## Message 1 — 30 janvier 2026 à 08:09 (Europe/Paris)

- **Identifiant :** `1908`
- **Lien :** https://forumdomotique.com/forums/topic/724-zigbee2mqtt-ne-d%C3%A9marre-avec-slzb-mr2u-d%C3%A9tect%C3%A9-en-ttyacm-au-lieu-de-ttyusb-fichier-introuvable/#findComment-1908

Salut !

Puisque ton dongle est un SLZB-MR2U (version USB multi-radio similaire au MR4U du tuto que j ai partagé, mais sans Ethernet/PoE natif), je vais adapter ma réponse pour t’orienter au mieux

Pour l’ USB, on utilise les ports serial directs (/dev/ttyACM*) au lieu de TCP/IP. L’erreur “No such file or directory” vient souvent d’un chemin by-id mal résolu dans le container de l’add-on (problème courant avec HA), ou d’un port occupé/ non accessible.

Voici comment procéder pas à pas, en suivant l’esprit du tuto mais adapté à ton SLZB-MR2U. Assume que tu es sur HA OS récent (2025+), avec Mosquitto déjà installé.

**1. Préparation du dongle**

•  Branche-le directement sur ton host HA.

•  Vérifie dans HA > Paramètres > Système > Matériel > Tout le matériel que les deux ports sont visibles : /dev/ttyACM0 (if00, probablement EFR32MG21 pour Ember/Thread) et /dev/ttyACM1 (if02, probablement CC2652P pour Z-Stack/Zigbee).

•  Si tu peux accéder à l’interface web du dongle (via USB, il émule parfois un réseau RNDIS avec IP comme 192.168.42.1 ou 192.168.168.1 – vérifie dans tes interfaces réseau sur le host), mets à jour le firmware à la dernière version (v3.0+ si disponible). Sinon, flashe via l’outil SMLight (dispo sur leur site). Mets-le en mode “Zigbee Coordinator” pour la radio que tu veux utiliser.

**2. Installation de l’intégration SMLIGHT SLZB (optionnel mais recommandé)**

•  Dans HA, va dans Paramètres > Appareils & Services > Ajouter une intégration > Cherche “SMLIGHT SLZB”.

•  Si auto-détecté (en USB, ça peut marcher si RNDIS actif), suis les instructions. Sinon, ajoute manuellement avec l’IP RNDIS si disponible (username/password par défaut souvent admin/admin).

•  Ça te permettra de monitorer le dongle (firmware, temp, mode), et d’éviter des conflits avec les radios. Pour multi-radio comme le tien, ça crée des entities séparées pour chaque radio.

**3. Ajout du dépôt Zigbee2MQTT**

•  Si c’est ta première instance : Utilise l’add-on officiel Zigbee2MQTT.

**4. Configuration de Zigbee2MQTT**

Passe en mode YAML et adapte comme suit. Choisis la radio selon ce que tu veux (Zigbee sur CC2652P souvent recommandé pour portée +20dBm).

•  **Pour la radio if00 (EFR32MG21, ttyACM0) – Idéal pour Thread/Matter ou Zigbee alternatif** :

```yaml
data_path: /config/zigbee2mqtt  # Ou -edge si seconde instance
socat:
  enabled: false
mqtt:
  server: mqtt://core-mosquitto  # Ton broker MQTT
  user: ton_user
  password: ton_pass
serial:
  port: /dev/ttyACM0  # Essaie ça d'abord au lieu du by-id pour bypasser l'erreur
  # Ou /dev/serial/by-id/usb-SMLIGHT_SMLIGHT_SLZB-MR2U_SLZB-MR2U236163-if00 si ça marche après redémarrage
  adapter: ember
  baudrate: 115200
  rtscts: true
```

•  **Pour la radio if02 (CC2652P, ttyACM1) – Idéal pour Zigbee principal** :

```yaml
data_path: /config/zigbee2mqtt  # Ou -edge
socat:
  enabled: false
mqtt:
  server: mqtt://core-mosquitto
  user: ton_user
  password: ton_pass
serial:
  port: /dev/ttyACM1  # Direct au lieu du by-id
  # Ou /dev/serial/by-id/usb-SMLIGHT_SMLIGHT_SLZB-MR2U_SLZB-MR2U236163-if02
  adapter: zstack
  baudrate: 115200
  rtscts: false
```

•  Sauvegarde, puis lance l’add-on. Vérifie les logs pour voir si ça connecte (cherche “Starting Zigbee2MQTT” sans erreur).

**5. Lancement et vérification**

•  Si erreur persiste : Redémarre ton host HA (pas juste l’add-on). Ça rafraîchit les mappings /dev.

•  Vérifie que ZHA n’est pas actif (désinstalle-le si oui, car il peut occuper un port).

•  Dans Zigbee2MQTT UI (accède via HA ou port 8080), active “Permit Join”, et appaire un device pour tester.

•  Change le canal Zigbee (ex: 25) pour éviter interférences.

N’hésite pas à m’envoyer les logs de z2mqtt une fois terminée

---

## Message 2 — 15 février 2026 à 22:03 (Europe/Paris)

- **Identifiant :** `2031`
- **Lien :** https://forumdomotique.com/forums/topic/724-zigbee2mqtt-ne-d%C3%A9marre-avec-slzb-mr2u-d%C3%A9tect%C3%A9-en-ttyacm-au-lieu-de-ttyusb-fichier-introuvable/#findComment-2031

Salut [@Engrobel](https://forumdomotique.com/profile/1262-engrobel/)

les warnings que tu mentionnes sont courants et non bloquants

Si tu veux vérifier que tout roule côté OTBR :

•  Va dans **Paramètres > Appareils & services > Thread > Configurer**. Tu devrais voir ton réseau Thread listé (quelque chose comme ha-thread-xxxx). S’il n’apparaît pas, redémarre l’addon OTBR et rafraîchis.

•  Assure-toi que l’IPv6 est activé sur ton HA : **Paramètres > Système > Réseau > IPv6** sur “Automatique”.

•  Logs supplémentaires : Si tu as d’autres erreurs après un redémarrage, partage-les, mais là, c’est clean.

**Intégrer le Bilresa IKEA en Matter-over-Thread**

Le Bilresa est une télécommande 2 boutons compatible Matter-over-Thread (pas Wi-Fi). L’appairage se fait via le code QR ou numérique sur l’emballage/appareil, mais il faut d’abord **synchroniser les credentials Thread de ton OTBR vers ton téléphone** pour que le pairing marche. Sans ça, le device ne peut pas rejoindre le réseau Thread. C’est souvent là que ça coince.

**Étapes pour l’appairage**

1.  **Mettre le Bilresa en mode pairing** :

•  Retire l’onglet isolant de la pile (si neuf).

•  Appuie 4 fois rapidement sur le bouton système (le gros bouton au milieu) pour activer le mode Matter. La LED devrait clignoter (ou pulser). Tiens-le près de ton SLZB-MR2U (le border router) pendant le pairing – max 1-2m.

•  Note le code QR ou le code numérique à 11/21 chiffres sur la batterie ou l’emballage (c’est ton “setup code”).

2.  **Synchroniser les credentials Thread vers ton téléphone** (obligatoire !) :

•  Utilise l’app Companion HA sur ton phone (iOS ou Android).

•  **Pour Android** : Va dans **Paramètres > App Companion > Dépannage > Synchroniser les credentials Thread**.

•  **Pour iOS** : Dans HA, va **Paramètres > Appareils & services > Thread > Configurer > Envoyer les credentials au téléphone**.

•  Une fois sync, sélectionne ton réseau Thread comme “réseau préféré” dans l’app (ça évite les conflits avec d’autres réseaux Thread existants sur ton phone).

3.  **Ajouter le device via l’app Companion HA** :

•  Ouvre l’app HA sur ton phone (Bluetooth activé, phone près du Bilresa et du SLZB).

•  Va **Paramètres > Appareils & services > Ajouter un appareil > Ajouter un appareil Matter**.

•  Choisis “Non, c’est nouveau”.

•  Scanne le QR code ou entre le code numérique manuellement.

•  Suis les prompts : Ça passe par Bluetooth pour envoyer les creds réseau, puis le device rejoint Thread via ton OTBR.

•  Temps estimé : 30-60 secondes si tout va bien ; si ça spinne plus de 2 min, annule et réessaie (proximité phone/BR/device critique).

---
