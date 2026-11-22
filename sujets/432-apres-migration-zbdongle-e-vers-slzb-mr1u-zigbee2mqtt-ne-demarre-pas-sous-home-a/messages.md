---
title: "Après migration ZBdongle-E vers SLZB-MR1U Zigbee2MQTT ne démarre pas sous Home Assistant"
description: "Le SLZB-MR2 utilise une puce Texas Instruments CC2652P (Z-Stack 3.x). Mais Zigbee2MQTT essaie de communiquer avec une CC2530/CC2531 (Z-Stack 1.2) →…"
image: /assets/images/vignettes-themes/zigbee.jpg

date: 2025-10-21
cover_alt: "Vignette de rubrique Zigbee — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/432-apr%C3%A8s-migration-zbdongle-e-vers-slzb-mr1u-zigbee2mqtt-ne-d%C3%A9marre-pas-sous-home-assistant/">Lire et commenter sur Forum Domotique</a></p>

# Après migration ZBdongle-E vers SLZB-MR1U Zigbee2MQTT ne démarre pas sous Home Assistant

- **Catégorie :** [Home Assistant](https://forumdomotique.com/forums/7-home-assistant/)
- **Sujet :** https://forumdomotique.com/forums/topic/432-apr%C3%A8s-migration-zbdongle-e-vers-slzb-mr1u-zigbee2mqtt-ne-d%C3%A9marre-pas-sous-home-assistant/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 21 octobre 2025 à 17:49 (Europe/Paris)

---

## Message 1 — 21 octobre 2025 à 17:49 (Europe/Paris)

- **Identifiant :** `1080`
- **Lien :** https://forumdomotique.com/forums/topic/432-apr%C3%A8s-migration-zbdongle-e-vers-slzb-mr1u-zigbee2mqtt-ne-d%C3%A9marre-pas-sous-home-assistant/#findComment-1080

Salut [@Zignet](https://forumdomotique.com/profile/500-zignet/)

Erreur principale :

```plaintext
Error: Failed to connect to the adapter (Error: SRSP - SYS - ping after 6000ms)
```

Et juste avant :

```plaintext
zh:zstack:znp: Writing CC2530/CC2531 skip bootloader payload
zh:zstack:znp: Skip bootloader for CC2652/CC1352
```

## Problème identifié : **Mauvais firmware ou mauvaise puce détectée**

Le **SLZB-MR2** utilise une puce **Texas Instruments CC2652P** (Z-Stack 3.x). Mais Zigbee2MQTT essaie de **communiquer avec une CC2530/CC2531** (Z-Stack 1.2) → **incompatible**.

---

## Cause probable :

Le **dongle est en mode USB** (ou firmware mal configuré) → Zigbee2MQTT voit une **vieille puce** au lieu du **CC2652P**.

Même si tu es en Ethernet, **le firmware du dongle doit être en mode Z-Stack 3.x** (pas 1.2).

---

## Solution pas à pas (à faire **obligatoirement**)

### 1. **Accède à l’interface web du SLZB-MR2**

- Ouvre ton navigateur : <http://IP-DU-DONGLE> ou <http://slzb-mr2.local>

### 2. **Vérifie et change le mode Zigbee**

Va dans l’onglet **Zigbee** ou **Coordinator** :

| Paramètre | Valeur à mettre |  |
| --- | --- | --- |
| **Coordinator type** | Z-Stack 3.x **(pas 1.2 !)** |  |
| **Firmware** | CC2652P ou zstack |  |
| **Baudrate** | 115200 |  |
| **Port TCP** | 6638 |  |

### 3. **Vérifie que le dongle est bien en Ethernet**

Onglet **Network** :

- Mode : **Ethernet** (pas USB)
- IP fixe ou DHCP → note l’IP

---

### 4. **Configuration.yaml Zigbee2MQTT (correcte)**

```yaml
serial:
  port: tcp://192.168.30.24:6638   # ← Remplace par TON IP
  adapter: zstack                 # ← Obligatoire, en minuscules
```

### 5. **Redémarre Zigbee2MQTT**

Dans les logs, tu dois voir :

```plaintext
zh:zstack:cc: CC2652P detected
Zigbee2MQTT started!
```

***Si ça fonctionne pas dit le moi !***

***Le firmware est probablement corrompu.***

P.S. : J'ai aussi vu une erreur concernant un conflit de réseau.

```plaintext
Error: network commissioning timed out - most likely network with the same panId or extendedPanId already exists nearby
```

C’est un timeout pendant la création du réseau Zigbee. Les codes montrent :

- bdbComissioningNotifcation avec status:8 → "NOT_ON_A_NETWORK" (échec, pas de réseau formé).
- stateChangeInd passe à 8 (DEV_COORD_STARTING) puis à 0 (DEV_HOLD), ce qui indique un blocage.
- Dans un essai, ECONNRESET ou ping timeout → problème de connexion TCP.

Cause principale : **Conflit avec un autre réseau Zigbee proche** (même panID 6754 ou extendedPanID [221,221,221,221,221,221,221,221]). Ça arrive souvent si tu as un ancien réseau, un autre coordinator, ou un voisin avec du Zigbee (ex: Philips Hue, IKEA).

Autres points :

- Port TCP : Tes logs montrent 7638, mais le défaut pour SLZB-MR2 en Zigbee est **6638**. Vérifie dans l’interface web du dongle (onglet Zigbee) — si c’est 7638, c’est peut-être pour Thread/Matter. Change pour 6638 si besoin.

---
