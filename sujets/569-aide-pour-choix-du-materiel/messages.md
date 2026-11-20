---
title: "Aide pour choix du matériel."
---

# Aide pour choix du matériel.

- **Catégorie :** [Box & Matériel](https://forumdomotique.com/forums/97-box-mat%C3%A9riel/)
- **Sujet :** https://forumdomotique.com/forums/topic/569-aide-pour-choix-du-mat%C3%A9riel/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 30 novembre 2025 à 16:34 (Europe/Paris)

---

## Message 1 — 30 novembre 2025 à 16:34 (Europe/Paris)

- **Identifiant :** `1406`
- **Lien :** https://forumdomotique.com/forums/topic/569-aide-pour-choix-du-mat%C3%A9riel/#findComment-1406

Bonjour [@yvanbricard64](https://forumdomotique.com/profile/759-yvanbricard64/) et bienvenue dans l’univers Home Assistant et dans le forum !

Ton projet est hyper classique et tout à fait réalisable, beaucoup d’entre nous sont passés par là 😊

Pour résumer tes besoins :

- Portail assez éloigné de la box → besoin d’une bonne couverture Zigbee/Z-Wave ou d’une solution filaire
- Volets roulants, chauffage, VMC, portail, future piscine → tu vas avoir besoin d’un réseau radio fiable + éventuellement quelques modules Shelly/ESPs/SONOFF

### 1. PC reconditionné Dell OptiPlex 3050 (ou 3060/3070/5060 etc.)

Excellente idée ! Ces petits Dell micro sont parfaits pour HA :

- Consomment très peu (≈10-15 W), silencieux, fiables, et tu trouves des modèles avec i5 6e/7e gen + 8/16 Go RAM + SSD à moins de 150 €. Tu installes Proxmox dessus si tu veux, ou directement Home Assistant OS → top.

### 2. Le gros point sensible : la distance jusqu’au portail

C’est LE point clé de ton installation.

Options possibles, du plus simple au plus costaud :

| Solution | Portée approx | Avantages | Inconvénients | Prix approx |
| --- | --- | --- | --- | --- |
| Zigbee + 1 répéteur prise | 15-30 m en champ libre | Pas cher, répéteurs alimentés renforcent le mesh | Portée très aléatoire selon murs et terrain | 50-80 € |
| Zigbee + 2-3 répéteurs | jusqu’à 50-60 m (parfois +) | Mesh très solide | Pas garanti à 100 % sur grande distance | 80-120 € |
| Z-Wave série 700/800 | souvent meilleure que Zigbee | Plus stable, meilleure pénétration des murs | Plus cher, moins de modules spécifiques portail | 80-150 € |
| Shelly / ESP32 en WiFi + point d’accès extérieur | dépend de la couverture WiFi | Très fiable et rapide si bon WiFi | Besoin d’une alimentation 220 V près du portail | 50-100 € |
| Câble Ethernet (RJ45) jusqu’au portail ou abri proche | illimitée | La solution la plus fiable et évolutive (zéro latence) | Travaux (goulotte, terrassement ou goulotte) | 50-200 € selon distance |

### La question que tout le monde va te poser :

Quelle est la distance approximative entre ta box Internet et ton portail ? Et est-ce qu’il y a un garage, un local technique, une prise 220 V ou une goulotte déjà existante à mi-chemin OU puisart de raccordement ?

### Recommandation la plus courante dans ton cas (distance importante) :

#### Pourquoi la ligne « Relais direct sur RJ45 » est souvent LA meilleure pour ton cas précis

Tu tires un seul câble Ethernet blindé extérieur (Cat6 STP) + éventuellement un câble d’alimentation 220 V (ou tu utilises du PoE). À l’arrivée tu mets dans un petit boîtier étanche IP66 :

- soit un **Sonoff ZBDongle-E** (version Ethernet)** → ~55 €
- soit un **TubeZB Ethernet** ou **ZigStar UZG-01 Ethernet** → ~60-70 €
- soit un Raspberry Pi 4/Zéro 2 W + stick Zigbee/Z-Wave alimenté en PoE → ~80-100 €
- soit directement un **Shelly Pro 4PM** ou **Shelly Plus Pro** en LAN pour piloter le portail en filaire
- soit un sonoff contact se no/nc

Résultat : ton réseau Zigbee démarre directement au portail → tous les appareils du jardin (portail, arrosage, lumières extérieures, future piscine) seront à 100 % fiables, même à 80-100 m de la maison.

C’est actuellement la solution la plus adoptée par ceux qui ont un portail très éloigné et qui veulent une installation propre et évolutive.

Avec ça tu n’auras jamais de problème de portée, même si tu ajoutes 50 appareils plus tard.

un exemple pour déporté ton zigbee:

<https://forumdomotique.com/tests/dongles-passerelles/test-slzb-mr4u-coordinateur-zigbee-thread-matter/?do=embed>

### Dongles conseillés aujourd’hui (novembre 2025)

- Zigbee : Sonoff Zigbee 3.0 USB Dongle Plus-E (version Ethernet existe aussi !) ou SkyConnect ou TubeZB EFR32
- Z-Wave : Zooz 800 Series ou Aeotec Z-Stick 7/Gen7 (série 700/800 obligatoire pour la portée longue)

N’hésite pas à nous dire :

- la distance approximative box → portail
- si tu as déjà une tranchée ou une goulotte
- si tu es OK pour tirer un câble

On pourra te donner la solution idéale à 100 % 😉

ps: Il y a énormément de possibilités que je peux te proposer. Peux-tu nous en dire plus sur ton projet ? Es-tu plutôt orienté Zigbee, Matter, KNX, Legrand, Sonoff, etc. ? Ces informations nous permettront de t’orienter au mieux.

---
