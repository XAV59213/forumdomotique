---
title: "soucis d'étalonnage avec Z2M et MQTT"
description: "https://www.productinfo.schneider-electric.com/wiser home/mureva-evlink wiser home device-user-guide/French/Mureva%20EVLink Socket Wiser Home…"
image: /assets/images/vignettes-themes/zigbee.jpg

date: 2025-07-04
cover_alt: "Vignette de rubrique Zigbee — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/245-soucis-d%C3%A9talonnage-avec-z2m-et-mqtt/">Lire et commenter sur Forum Domotique</a></p>

# soucis d'étalonnage avec Z2M et MQTT

- **Catégorie :** [Intégrations et Add-ons](https://forumdomotique.com/forums/11-int%C3%A9grations-et-add-ons/)
- **Sujet :** https://forumdomotique.com/forums/topic/245-soucis-d%C3%A9talonnage-avec-z2m-et-mqtt/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 3
- **Premier message de XAV59213 :** 4 juillet 2025 à 17:25 (Europe/Paris)
- **Dernier message de XAV59213 :** 5 juillet 2025 à 13:50 (Europe/Paris)

---

## Message 1 — 4 juillet 2025 à 17:25 (Europe/Paris)

- **Identifiant :** `535`
- **Lien :** https://forumdomotique.com/forums/topic/245-soucis-d%C3%A9talonnage-avec-z2m-et-mqtt/#findComment-535

> **il y a une heure, enthalpie a dit :**
> et question subsidiaire, y at'il un moyen de remettre à zéro les valeurs ?

salut [@enthalpie](https://forumdomotique.com/profile/196-enthalpie/)

Oui voici la procédure

[https://www.productinfo.schneider-electric.com/wiser_home/mureva-evlink_wiser_home_device-user-guide/French/Mureva%20EVLink_Socket_Wiser_Home_Device%20user%20guide_fr_DD00535952.xml/$/Resettingthedevice_Murev_EV_WHREF_fr_DD00535942](https://www.productinfo.schneider-electric.com/wiser_home/mureva-evlink_wiser_home_device-user-guide/French/Mureva%20EVLink_Socket_Wiser_Home_Device%20user%20guide_fr_DD00535952.xml/%24/Resettingthedevice_Murev_EV_WHREF_fr_DD00535942)

---

## Message 2 — 5 juillet 2025 à 13:45 (Europe/Paris)

- **Identifiant :** `542`
- **Lien :** https://forumdomotique.com/forums/topic/245-soucis-d%C3%A9talonnage-avec-z2m-et-mqtt/#findComment-542

> **Il y a 17 heures, enthalpie a dit :**
> 3`z2m: Failed to configure 'mureva EV link', attempt 4 (Error: ZCL command 0x70ac08fffe421106/6 haElectricalMeasurement.read(["acPowerDivisor","acPowerMultiplier"], {"timeout":10000,"disableResponse":false,"disableRecovery":false,"disableDefaultResponse":true,"direction":0,"reservedBits":0,"writeUndiv":false}) failed (Status 'UNSUPPORTED_ATTRIBUTE') at Endpoint.checkStatus (/app/node_modules/.pnpm/[email protected]/node_modules/zigbee-herdsman/src/controller/model/endpoint.ts:363:28) at Endpoint.zclCommand (/app/node_modules/.pnpm/[email protected]/node_modules/zigbee-herdsman/src/controller/model/endpoint.ts:987:26) at Endpoint.read (/app/node_modules/.pnpm/[email protected]/node_modules/zigbee-herdsman/src/controller/model/endpoint.ts:459:29) at result.configure (/app/node_modules/.pnpm/[email protected]/node_modules/zigbee-herdsman-converters/src/lib/modernExtend.ts:2065:37) at Object.configure (/app/node_modules/.pnpm/[email protected]/node_modules/zigbee-herdsman-converters/src/index.ts:363:21) at Configure.configure (/app/lib/extension/configure.ts:123:13) at Configure.onMQTTMessage (/app/lib/extension/configure.ts:46:25) at EventEmitter.wrappedCallback (/app/lib/eventBus.ts:252:17))`

Cela signifie que l’appareil **Mureva EVlink** ne prend **pas en charge** les attributs Zigbee demandés (`acPowerDivisor`, `acPowerMultiplier`) sur le cluster `haElectricalMeasurement`. il doit manquer un upgrade sur la prise ouvre une issue sur z2mqtt <https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/issues>

---

## Message 3 — 5 juillet 2025 à 13:50 (Europe/Paris)

- **Identifiant :** `543`
- **Lien :** https://forumdomotique.com/forums/topic/245-soucis-d%C3%A9talonnage-avec-z2m-et-mqtt/#findComment-543

Cela signifie que Zigbee2MQTT essaie de **lire la puissance instantanée**, mais l'appareil ne **supporte pas cet attribut**. Cela peut arriver :

- Si l’appareil ne fournit pas cette donnée via Zigbee.
- Si le **cluster ou l’attribut n’est pas exposé sur l’endpoint 6**.
- Si le **device expose la puissance autrement** (autre cluster, autre nom, ou via un payload MQTT personnalisé). a tu ajouter une integration qui renome et calcul la puissance comme powercalc ?

---
