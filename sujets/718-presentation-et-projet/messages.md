---
title: "Présentation et projet"
---

# Présentation et projet

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/718-pr%C3%A9sentation-et-projet/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 2 février 2026 à 10:48 (Europe/Paris)
- **Dernier message de XAV59213 :** 3 février 2026 à 13:34 (Europe/Paris)

---

## Message 1 — 2 février 2026 à 10:48 (Europe/Paris)

- **Identifiant :** `1964`
- **Lien :** https://forumdomotique.com/forums/topic/718-pr%C3%A9sentation-et-projet/#findComment-1964

Bonjour Pierre (et l’autre Pierre 😄),

Bienvenue sur le forum ! Ton problème est **très courant** quand on fait tourner **Home Assistant dans une machine virtuelle** sur un Synology (via **Virtual Machine Manager ou proxmox**).

Le dongle **Sonoff Zigbee 3.0 USB Dongle Plus** (ou Lite / MG21 / ZBDongle-E selon le nom exact) n’apparaît pas dans **Paramètres → Système → Matériel** (ni dans « Mes appareils et services ») parce qu’il n’est tout simplement **pas passé à la VM**.

Voici les points les plus probables et les solutions à tester, dans l’ordre :

### 1. Vérifie le **passthrough USB** dans Virtual Machine Manager

C’est la cause n°1 dans 90 % des cas similaires.

- Va dans **Virtual Machine Manager** sur ton Synology
- Sélectionne ta VM Home Assistant → **Action** → **Modifier** (ou Éditer)
- Va dans l’onglet **Autres** (ou « Others » selon la langue)
- Cherche la section **Périphériques USB** ou **USB Device Passthrough**
- Vérifie si ton dongle Sonoff apparaît dans la liste des périphériques USB disponibles

  - Si **non** → le dongle n’est pas détecté par DSM → passe directement au point 3
  - Si **oui** → coche-le / ajoute-le à la VM → Appliquer → redémarre la VM

Une fois le passthrough activé, tu devrais voir apparaître dans Home Assistant :

**Paramètres → Système → Matériel → Tous les matériels** un périphérique du type /dev/ttyUSB0 ou /dev/ttyACM0 (ou /dev/serial/by-id/...)

### 2. Si le dongle apparaît dans VMM mais pas dans HA

- Redémarre complètement la VM (pas juste HA)
- Parfois il faut **débrancher / rebrancher** le dongle **après** le démarrage de la VM
- Vérifie aussi dans HA si le port série est bien visible (le Sonoff E est souvent /dev/ttyACM0 avec les versions récentes)

### 3. Si le dongle n’apparaît **pas du tout** dans VMM (le cas le plus fréquent avec DSM 7.2+)

Synology a fortement restreint / modifié la gestion USB série depuis DSM 7 pour des raisons de sécurité.

Solutions courantes :

**a) Tester un autre port USB** Essaie un port à l’arrière (souvent plus fiable que celui de devant).

**b) Utiliser un câble USB d’extension** Beaucoup de dongles Zigbee sont capricieux avec les ports directs → un câble d’1 m avec blindage aide souvent.

**c) Vérifier la détection bas niveau sur le NAS** Tu peux ouvrir un terminal SSH sur le Synology et taper :

```bash
lsusb
dmesg | grep usb
```

Si le dongle n’apparaît même pas là → problème matériel / port / câble / DSM qui bloque.

**d) Alternative très recommandée** : installer **Zigbee2MQTT** dans un conteneur Docker séparé

Beaucoup de personnes ayant exactement ton setup (HA en VM + dongle Sonoff) finissent par :

- Garder HA en VM (sans Zigbee dedans)
- Installer **Zigbee2MQTT** en Docker sur le NAS directement
- Passer le dongle au conteneur Zigbee2MQTT (via /dev/ttyUSBx ou /dev/ttyACMx)
- Connecter Z2M à HA via MQTT

C’est plus stable sur Synology et évite les galères de passthrough USB vers la VM.

### 4. Dernière option (la plus radicale mais souvent la plus fiable)

Installer **Home Assistant OS** directement dans la VM (pas Home Assistant Core / Supervised dans une VM Linux). HAOS gère très bien les dongles USB quand le passthrough fonctionne.

Tu télécharges l’image **.ova** pour VMware depuis le site officiel HA, et tu l’importes dans VMM.

### En résumé rapide pour toi :

1. Vérifie **d’abord** si le dongle est visible dans **VMM → Modifier VM → Autres → USB**
2. Si non → teste port / câble / lsusb en SSH
3. Si oui → coche-le, redémarre la VM, et regarde dans **Matériel** de HA
4. Si toujours rien → envisage Zigbee2MQTT en Docker (très populaire sur Syno)

N’hésite pas à nous dire ce que tu vois dans VMM et/ou dans lsusb, ça aidera à affiner !

Bon courage et à bientôt sur le forum 😊

---

## Message 2 — 3 février 2026 à 13:34 (Europe/Paris)

- **Identifiant :** `1980`
- **Lien :** https://forumdomotique.com/forums/topic/718-pr%C3%A9sentation-et-projet/#findComment-1980

Salut [@Pierre31470](https://forumdomotique.com/profile/1253-pierre31470/) ,

Ravi d’entendre que tout fonctionne maintenant et que ton dongle est reconnu la magie de la domotique opère enfin !

😄 Un grand merci pour ton retour

Et n oublie pas de clôturer ton poste🕺

---
