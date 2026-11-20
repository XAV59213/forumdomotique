---
title: "Modèle pour Vos Demandes d'Aide sur Home Assistant"
description: "Merci de remplir ce modèle (2-4 min maxi) ! Ça change énormément la rapidité et la qualité des réponses Avec ces infos on voit tout de suite…"
image: /sujets/730-modele-pour-vos-demandes-daide-sur-home-assistant/images/2caebf6b-03da-4291-8154-b32f2da42c67.jpg
date: 2026-01-31
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/730-mod%C3%A8le-pour-vos-demandes-daide-sur-home-assistant/">Lire et commenter sur Forum Domotique</a></p>

# Modèle pour Vos Demandes d'Aide sur Home Assistant

- **Catégorie :** [Dépannage et Support Technique](https://forumdomotique.com/forums/19-d%C3%A9pannage-et-support-technique/)
- **Sujet :** https://forumdomotique.com/forums/topic/730-mod%C3%A8le-pour-vos-demandes-daide-sur-home-assistant/
- **Auteur du premier message du sujet :** XAV59213
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 31 janvier 2026 à 10:55 (Europe/Paris)

---

## Message 1 — 31 janvier 2026 à 10:55 (Europe/Paris)

- **Identifiant :** `1928`
- **Lien :** https://forumdomotique.com/forums/topic/730-mod%C3%A8le-pour-vos-demandes-daide-sur-home-assistant/#findComment-1928

##### Salut la communauté !

**Merci de remplir ce modèle (2-4 min maxi) !** Ça change **énormément** la rapidité et la qualité des réponses.

Avec ces infos on voit tout de suite l’architecture → moins de questions aller-retour → solution plus rapide pour tout le monde.

Merci d’avance ! 🙏

Si un point ne concerne pas ton cas → mets **N/A**, **–** ou **rien**.

![2caebf6b-03da-4291-8154-b32f2da42c67.jpg](images/2caebf6b-03da-4291-8154-b32f2da42c67.jpg)
<!-- source : https://cdn.forumdomotique.com/monthly_2026_01/2caebf6b-03da-4291-8154-b32f2da42c67.jpg.4c55277a8b03955cac2dabf3fcea17a5.jpg -->

#### Titre conseillé pour le post (à adapter selon vos cas) :

#### [Pi5 8Go + ZHA] Capteur Aqara température/humidité jamais découvert

#### ou

#### [Matter + Thread] Lampe IKEA ne s’allume plus la nuit via automation

#### **1. Le problème en 3 phrases maxi**

##### (sois le plus concret possible – c’est la partie la plus importante)

.

.

.

#### **2. Ton serveur Home Assistant**

- Modèle machine : ………………………………… (ex. Raspberry Pi 5 8 Go, Beelink mini PC, HA Green, VM Proxmox…)
- Stockage principal : ………………………………… (SSD NVMe 256 Go, microSD 128 Go, eMMC…)
- Alimentation utilisée : ………………………………… (officielle Raspberry 27 W, chargeur 5V/3A lambda, PoE…)

#### **3. Installation logicielle**

- Type d’installation HA : … HAOS / Supervised / Container (Docker) / Core
- Version Home Assistant : … (regarde tout en bas à gauche dans l’interface)
- Version HAOS / système hôte (si connu) : … (ex. HAOS 14.x, Debian 12 bookworm…)
- Add-ons & intégrations les plus importantes : … (ZHA, Zigbee2MQTT, Matter / Thread, Mosquitto, Frigate, Node-RED, HACS, Samba, ESPHome…)

#### **4. Réseau & protocoles**

- Connexion du serveur HA : WiFi / Ethernet Gigabit / Ethernet 2.5G / …
- Protocoles domotiques actifs : … (Zigbee 3.0, Thread/Matter, Z-Wave, WiFi 2.4 GHz, Bluetooth, IP local, Tuya local…)
- Contrôleur(s) / dongle(s) principal(aux) : … (ex. Sonoff ZBDongle-E, SkyConnect original, Tube’s POE Coordinator, ConBee III, Goobay Matter dongle…)

#### **5. Appareil(s) qui pose(nt) problème**

- Type : … (capteur température, ampoule couleur, prise intelligente, store motorisé, serrure, caméra…)
- Marque + **modèle exact** (très important) : … (ex. Aqara WSDCGQ11LM, IKEA TRÅDFRI E27 806lm, Tuya Zemismart roller…)
- Protocole principal : … (Zigbee 3.0, Matter over Thread, WiFi Tuya/SmartLife, Bluetooth, 433 MHz…)
- Nombre d’appareils **identiques** avec le même souci : …
- État actuel dans HA : … (jamais découvert / découvert mais indisponible / entité existe mais état inconnu / valeur aberrante / clignote mais pas d’action…)

#### **6. Chaîne de communication (topologie)**

(exemple texte simple ou lien image) RPi 5 → USB Sonoff ZBDongle-E → ZHA → Aqara capteur température ou HA Green → Ethernet → Border Router Thread intégré → Lampe Matter Eve Energy

#### **7. Ce que j’ai déjà testé (très utile !)**

- …
- …
- …

#### **8. Logs / erreurs / comportement précis** / automatisation

##### Copie les lignes **importantes** (Configuration → Logs ou journalctl -u home-assistant@homeassistant -n 200) → Masquer votre IP, tokens, noms sensibles

avec xxx ou …

Exemple recherché :

```plaintext
2026-01-30 14:23:12.456 ERROR (MainThread) [zha] Failed to fetch data for device ...
```

#### **9. But final souhaité** (ce que tu veux **vraiment** obtenir) Exemples :

- « Afficher la température + humidité sur le dashboard + alerte Telegram si T° < 17 °C »
- « Allumer la lampe salon à 30 % seulement entre 22h et 6h si présence détectée ET luminosité < 40 lux »
- « Pouvoir piloter le store depuis Google Home sans délai »

#### **10. Contexte & niveau (optionnel mais précieux)**

- Niveau Home Assistant : Débutant / Intermédiaire / Avancé / « je bidouille du yaml depuis 4 ans »
- Ancienneté HA : … mois / … années
- Contraintes importantes : budget très limité / locataire (pas de perçage) / refus flash custom firmware / installation 100 % local / enfants en bas âge / …

##### Merci beaucoup pour ces précisions !

##### Avec ça, la communauté peut t’aider efficacement dès les premières réponses. 🚀

---
