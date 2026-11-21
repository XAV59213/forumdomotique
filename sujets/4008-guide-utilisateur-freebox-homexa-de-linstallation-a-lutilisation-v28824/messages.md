---
title: "Guide utilisateur Freebox Homexa — de l’installation à l’utilisation (v28.8.24)"
description: "Suite à la mise à jour 28.8.24 , guide complet : de l’installation HACS jusqu’à l’usage quotidien Dépôt : github.com/XAV59213/freebox homexa Intégration…"
image: /assets/images/og-default.png
date: 2026-09-27
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/4008-guide-utilisateur-freebox-homexa-de-linstallation-%C3%A0-lutilisation-v28824/">Lire et commenter sur Forum Domotique</a> · <a href="https://github.com/XAV59213/freebox_homexa">Dépôt HACS : Freebox Homexa</a></p>

# Guide utilisateur Freebox Homexa — de l’installation à l’utilisation (v28.8.24)

<!-- source : https://litter.catbox.moe/hx4wox.jpg — fichier d’origine introuvable (hébergeur temporaire, lien mort). -->
<p class="media-fallback">L’illustration d’origine n’est plus disponible. Voir le <a href="https://github.com/XAV59213/freebox_homexa/blob/main/docs/guide-utilisateur.md">guide utilisateur dans le dépôt Freebox Homexa</a>.</p>

Suite à la mise à jour **28.8.24**, guide complet : de l’installation HACS jusqu’à l’usage quotidien.

**Projet indépendant, non affilié à Free.**  
Dépôt : [github.com/XAV59213/freebox_homexa](https://github.com/XAV59213/freebox_homexa)  
Sujet d’origine : [Présentation du projet](https://forumdomotique.com/forums/topic/101-pr%C3%A9sentation-du-projet-freebox_homexa/)  
<!-- source : https://litter.catbox.moe/ugx9jt.pdf — fichier d’origine introuvable (hébergeur temporaire, lien mort). -->
PDF : le fichier d’origine n’est plus disponible ; le guide à jour se trouve dans le [dépôt Freebox Homexa](https://github.com/XAV59213/freebox_homexa/blob/main/docs/guide-utilisateur.md).

**Sommaire**

1. C’est quoi Homexa ?
2. Prérequis
3. Installation HACS
4. Appairage (Server / Delta Devialet)
5. Dans Home Assistant
6. Services utiles
7. Dépannage

---

## 1. C’est quoi Homexa ?

Intégration custom Home Assistant qui regroupe Server, pack Home, répéteurs, LAN/Wi-Fi et Player.

- **Freebox Server** — état, réseau, Wi-Fi, débits
- **Freebox Home** — interrupteurs, caméras, volets, PIR, contacts
- **Alarme** — Présent / Absent / Désarmé (comme l’app Free)
- **Clients LAN / Wi-Fi** — device_tracker + RSSI (dBm)
- **Répéteurs F-RP01A** — capteur En ligne + clients
- **Player** — Devialet, Mini 4K, Pop : volume, sources, télécommande

> **HDMI sur le Player** = sortie TV en CEC (One Touch Play). Ça réveille la TV. Ça ne change pas l’entrée HDMI 1/2/3.

---

## 2. Prérequis

- Home Assistant **2026.8.0+**
- HACS
- Freebox OS (Révolution, Mini 4K, Delta, Pop, Ultra)
- « Permettre les nouvelles demandes d’associations » coché dans Freebox OS
- Être devant la box : l’appairage se valide **sur l’écran / la façade**

> **Astuce forum** — poll Home à 5 s + intégration officielle Freebox encore active = API saturée. Désactive l’officielle.

---

## 3. Installation HACS

1. HACS → trois points → **Dépôts personnalisés**
2. URL : `https://github.com/XAV59213/freebox_homexa`
3. Catégorie : **Integration**
4. Installer **Freebox Homexa** puis redémarrer HA

Mise à jour : HACS → Freebox Homexa → Mettre à jour → reboot HA.

---

## 4. Appairage — deux modèles, deux formats

Paramètres → Appareils et services → Ajouter une intégration → **Freebox Homexa**.  
Host : `mafreebox.freebox.fr` / IP LAN / `xxx.fbxos.fr`. Pas de token dans configuration.yaml.

### Server / Révolution — écran + flèches

Popup HA « Lier le routeur Freebox ». Clique **Valider**, puis sur le Server la **flèche droite = Oui**.

<!-- source : https://litter.catbox.moe/7jykrx.png — fichier d’origine introuvable (hébergeur temporaire, lien mort). -->
<p class="media-fallback">L’illustration d’origine n’est plus disponible. Voir le <a href="https://github.com/XAV59213/freebox_homexa/blob/main/docs/guide-utilisateur.md">guide utilisateur dans le dépôt Freebox Homexa</a>.</p>

*Écran Server : Autoriser l’application ? Non < > Oui.*

### Delta / Devialet — façade tactile

Sur la façade Devialet, choisir **oui** avec les **boutons tactiles clignotants** (ce n’est pas le même geste que les flèches du Server).

<!-- source : https://litter.catbox.moe/jd2672.png — fichier d’origine introuvable (hébergeur temporaire, lien mort). -->
<p class="media-fallback">L’illustration d’origine n’est plus disponible. Voir le <a href="https://github.com/XAV59213/freebox_homexa/blob/main/docs/guide-utilisateur.md">guide utilisateur dans le dépôt Freebox Homexa</a>.</p>

*Façade Delta / Devialet : message AUTORIZ + boutons tactiles.*

Ensuite dans Freebox OS → Applications : droits **Home, Player, LAN, Wi-Fi**.

**Options (Configurer)**

- Suivre les clients LAN → device_tracker
- Capteurs RSSI Wi-Fi → dBm
- Device Homexa par client → à décocher si doublons HA 2026.8
- Intervalle Home → 5 / 10 / 15 / 20 / 25 / 30 s
- Code télécommande Player → 8 chiffres (Réglages → Système → Informations)

---

## 5. Dans Home Assistant

<!-- source : https://litter.catbox.moe/msv8d9.jpg — fichier d’origine introuvable (hébergeur temporaire, lien mort). -->
<p class="media-fallback">L’illustration d’origine n’est plus disponible. Voir le <a href="https://github.com/XAV59213/freebox_homexa/blob/main/docs/guide-utilisateur.md">guide utilisateur dans le dépôt Freebox Homexa</a>.</p>

**Alarme — mapping app Free**

| App Free | Home Assistant |
| --- | --- |
| Présent | armed_home |
| Absent | armed_away |
| Désarmé | disarmed |
| Armement | arming |
| Sirène | triggered |

PIN masqué dans les attributs. PIR / contacts = binary_sensor. Volets = cover. F-RP01A = En ligne + clients.

Player : volume, mute, play/pause. Sources : TV, HDMI CEC, YouTube, Netflix, Disney+, Prime.  
Remote : power, tv, ok, flèches, vol_inc / vol_dec, mute, play, 0–9.

---

## 6. Services utiles

- `freebox_homexa.reboot` — redémarre le Server
- `freebox_homexa.reload` — rediscover Home
- `freebox_homexa.remote` — touche Player
- `freebox_homexa.tv_guide` / `play_channel` — guide / chaîne TNT

Exemples concrets :

- Téléphone `not_home` 10 min → `alarm_arm_away`. Retour → désarmer ou Présent. Réserve l’IP DHCP.
- PIR on + nuit → lumière. Poll 5–10 s si l’officielle est off.
- `media_player.select_source` YouTube / Netflix. HDMI CEC = réveil TV seulement.
- Groupe cover pour les volets après sunset.

---

## 7. Dépannage

| Symptôme | Piste |
| --- | --- |
| Intégration morte | HA 2026.8.0+ |
| bad_json alarme | Homexa 28.8.2+ |
| 2 boutons d’alarme seulement | Passer en 28.8+ |
| Répéteur invisible | Reboot HA |
| Player absent | Droit Player + reboot |
| Remote muet | Code 8 chiffres |
| HDMI ≠ entrée TV | Normal : CEC uniquement |
| Pas de RSSI | Client Ethernet ou droit LAN manquant |
| Doublons devices | Décocher device par client |
| PIR à la traîne | Officielle off + poll 5/10 s |

Logs : Paramètres → Système → Journaux, filtre `freebox_homexa`.

Licence MIT. Vos retours (modèle de box, Player, nombre de répéteurs) font avancer la suite.
