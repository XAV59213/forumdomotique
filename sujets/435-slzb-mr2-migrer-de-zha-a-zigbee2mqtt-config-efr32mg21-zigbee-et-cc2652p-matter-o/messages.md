---
title: "SLZB-MR2 : migrer de ZHA à Zigbee2MQTT, config EFR32MG21 Zigbee et CC2652P Matter-over-Thread, conseils firmwares"
description: "L’erreur « Matter-over-Thread en mode Ethernet nécessite une connexion stable » signifie que ton réseau Ethernet est trop instable ou saturé (gros…"
image: /assets/images/og-default.png
date: 2025-10-21
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/435-slzb-mr2-migrer-de-zha-%C3%A0-zigbee2mqtt-config-efr32mg21-zigbee-et-cc2652p-matter-over-thread-conseils-firmwares/">Lire et commenter sur Forum Domotique</a></p>

# SLZB-MR2 : migrer de ZHA à Zigbee2MQTT, config EFR32MG21 Zigbee et CC2652P Matter-over-Thread, conseils firmwares

- **Catégorie :** [Installation et Configuration](https://forumdomotique.com/forums/8-installation-et-configuration/)
- **Sujet :** https://forumdomotique.com/forums/topic/435-slzb-mr2-migrer-de-zha-%C3%A0-zigbee2mqtt-config-efr32mg21-zigbee-et-cc2652p-matter-over-thread-conseils-firmwares/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 21 octobre 2025 à 18:30 (Europe/Paris)

---

## Message 1 — 21 octobre 2025 à 18:30 (Europe/Paris)

- **Identifiant :** `1083`
- **Lien :** https://forumdomotique.com/forums/topic/435-slzb-mr2-migrer-de-zha-%C3%A0-zigbee2mqtt-config-efr32mg21-zigbee-et-cc2652p-matter-over-thread-conseils-firmwares/#findComment-1083

Salut [@Chrisk59](https://forumdomotique.com/profile/507-chrisk59/) !

L’erreur **« Matter-over-Thread en mode Ethernet nécessite une connexion stable »** signifie que **ton réseau Ethernet est trop instable ou saturé** (gros fichiers, streaming, etc.).

**Solution rapide :** Branche ton border router avec un **bon câble Cat5e/6 directement sur le routeur principal** et **évite les gros transferts en même temps**.

---
