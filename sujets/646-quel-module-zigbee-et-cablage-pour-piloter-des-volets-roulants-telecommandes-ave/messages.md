---
title: "Quel module Zigbee et câblage pour piloter des volets roulants télécommandés avec Home Assistant"
description: "Vos volets roulants sont commandés par télécommande radio (probablement RF, comme Somfy ou similaire), donc ils sont radio et non filaires. Il n’est pas…"
image: /assets/images/vignettes-themes/zigbee.jpg

date: 2026-01-03
cover_alt: "Vignette de rubrique Zigbee — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/646-quel-module-zigbee-et-c%C3%A2blage-pour-piloter-des-volets-roulants-t%C3%A9l%C3%A9command%C3%A9s-avec-home-assistant/">Lire et commenter sur Forum Domotique</a></p>

# Quel module Zigbee et câblage pour piloter des volets roulants télécommandés avec Home Assistant

- **Catégorie :** [Confort et Ambiance](https://forumdomotique.com/forums/67-confort-et-ambiance/)
- **Sujet :** https://forumdomotique.com/forums/topic/646-quel-module-zigbee-et-c%C3%A2blage-pour-piloter-des-volets-roulants-t%C3%A9l%C3%A9command%C3%A9s-avec-home-assistant/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 3 janvier 2026 à 11:51 (Europe/Paris)
- **Dernier message de XAV59213 :** 18 janvier 2026 à 12:31 (Europe/Paris)

---

## Message 1 — 3 janvier 2026 à 11:51 (Europe/Paris)

- **Identifiant :** `1671`
- **Lien :** https://forumdomotique.com/forums/topic/646-quel-module-zigbee-et-c%C3%A2blage-pour-piloter-des-volets-roulants-t%C3%A9l%C3%A9command%C3%A9s-avec-home-assistant/#findComment-1671

Bonjour [@kris57](https://forumdomotique.com/profile/950-kris57/) ,

Vos volets roulants sont commandés par télécommande radio (probablement RF, comme Somfy ou similaire), donc ils sont **radio** et non filaires. Il n’est pas possible d’ajouter un simple module Zigbee derrière un interrupteur, car il n’y a généralement pas d’interrupteur filaire classique.

Pour les piloter à distance via Home Assistant (HA), les options Zigbee sont limitées, car la plupart des modules Zigbee sont conçus pour des volets **filaires** (moteur câblé avec phase montée/descente).

**Options possibles**

Voici quelques solutions adaptées :

1.  **Ajouter un récepteur RF Zigbee compatible avec votre marque**

•  Si vos volets sont Somfy (très courant), le mieux est un **bridge Somfy Connectivity Kit** ou **Somfy TaHoma Switch**, qui intègre les volets radio Somfy à HA via une intégration officielle ou Overkiz. Ce n’est pas purement Zigbee, mais ça fonctionne très bien à distance.

•  Pour d’autres marques (ex. : Bubendorff, Profalux), vérifiez s’il existe un bridge compatible.

2.  **Remplacer la télécommande par une télécommande Zigbee universelle**

•  Une **télécommande Zigbee pour volets** (comme certains modèles Zemismart ou Tuya Zigbee remote pour shutters) peut parfois apprendre les codes RF, mais c’est rare et pas fiable pour toutes les marques. Pas recommandé comme solution principale.

3.  **Passer à une solution non Zigbee (mais excellente pour HA)**

•  Un module **Broadlink RM4 Pro** ou **RM Mini** (WiFi/IR+RF) peut apprendre les codes de votre télécommande existante et les reproduire. Très simple à intégrer dans HA (intégration Broadlink), et ça permet un contrôle à distance parfait sans modifier les volets.

•  Ou un **Bond Bridge** (spécialisé dans les volets RF), compatible HA.

4.  **Si vous voulez rester en Zigbee pur**

•  Il n’existe pas (à ma connaissance en 2026) de module Zigbee qui se branche directement sur un moteur radio pour le rendre Zigbee. Les modules populaires comme NOUS B4Z, NodOn SIN-4-RS-20, MOES MS-108ZR, ou Sonoff MINI-ZBRBS sont pour volets **filaires** (à encastrer derrière un interrupteur filaire).

**Recommandation**

Si vos volets sont Somfy → Somfy TaHoma ou Connectivity Kit + intégration HA.

Sinon → Broadlink RM4 Pro (peu cher, fiable, contrôle à distance total, et conserve votre télécommande locale).

Si vous me précisez la marque de vos volets et de la télécommande (Somfy, Bubendorff, etc.), je pourrai affiner le conseil !

---

## Message 2 — 18 janvier 2026 à 12:31 (Europe/Paris)

- **Identifiant :** `1815`
- **Lien :** https://forumdomotique.com/forums/topic/646-quel-module-zigbee-et-c%C3%A2blage-pour-piloter-des-volets-roulants-t%C3%A9l%C3%A9command%C3%A9s-avec-home-assistant/#findComment-1815

Salut [@kris57](https://forumdomotique.com/profile/950-kris57/)

Désolé d'entendre que le Broadlink RM4 Pro n'a pas fonctionné pour vos télécommandes Somfy (modèle 74300, qui utilise le protocole RTS à 433 MHz). C'est un problème courant avec les rolling codes de Somfy, qui changent à chaque commande et compliquent l'apprentissage par des dispositifs comme Broadlink. Il existe plusieurs alternatives fiables pour intégrer vos 4 volets roulants Schuco/Somfy à Home Assistant (HA), en visant un contrôle à distance via HA et MQTT si possible, sans multiplier les apps. Je vais lister les options les plus adaptées en 2026, basées sur des solutions éprouvées.

### 1. **Bond Bridge (recommandé comme alternative simple au Broadlink)**

- **Description** : C'est un hub RF/WiFi spécialisé dans les volets et stores RF comme Somfy RTS <https://www.amazon.com/stores/Bond/page/1F4CF490-6E81-4C3A-AB95-835E1B000A91>.
- Il apprend les codes de votre télécommande et les reproduit, mais gère mieux les rolling codes que Broadlink grâce à une émulation spécifique pour Somfy. Il se connecte directement à HA via l'intégration officielle "Bond" (disponible dans HA core). Vous pouvez contrôler les volets à distance via l'app Bond ou HA, et il supporte MQTT via des automations personnalisées si besoin.
- **Montage** :

  - Achetez un Bond Bridge (environ 100-150 €).
  - Installez-le près des volets (portée RF jusqu'à 30-50 m).
  - Via l'app Bond, apprenez les commandes de votre télécommande Somfy (up/down/stop/my position).
  - Ajoutez l'intégration Bond dans HA (via Configuration > Intégrations > Ajouter > Bond). Il créera des entités "cover" pour chaque volet.
  - Pour le contrôle à distance : Utilisez le service cloud de HA (Nabu Casa) ou configurez un VPN/MQTT broker pour accéder à HA depuis l'extérieur.
- **Avantages** : Facile à installer, conserve la télécommande locale, compatible Alexa/Google si voulu. Pas de cloud obligatoire pour HA.
- **Inconvénients** : Pas purement Zigbee (c'est WiFi/RF), et coûte un peu plus que Broadlink.
- **Si ça ne marche pas** : Bond est testé avec Somfy RTS, mais vérifiez la compatibilité exacte pour le modèle 74300 sur leur site.

### 2. **ESPSomfy RTS (solution DIY locale et économique, via MQTT)**

- **Description** : Un projet open-source basé sur un ESP32 + module transceiver CC1101 (433 MHz)<https://github.com/rstrouse/ESPSomfy-RTS>. Il émule une télécommande Somfy RTS virtuelle, gère les rolling codes nativement, et s'intègre parfaitement à HA via MQTT ou une intégration HACS dédiée. Vous pouvez contrôler jusqu'à 32 volets avec un seul dispositif. C'est idéal pour votre setup, car c'est 100% local et MQTT-friendly.
- **Montage** :

  - Matériel : ESP32 (5-10 €) + CC1101 (5 €) + alimentation USB. Tutoriel complet sur GitHub pour le câblage (simple, pas de soudure complexe).
  - Flashez le firmware ESPSomfy sur l'ESP32 via ESPHome ou directement.
  - Programmez chaque volet : Utilisez votre télécommande Somfy pour appairer les volets à l'ESP (comme une nouvelle télécommande virtuelle).
  - Intégrez à HA : Ajoutez l'intégration "ESPSomfy-RTS-HA" via HACS, ou utilisez MQTT (l'ESP publie des topics pour up/down/position). Créez des entités cover dans HA.
  - Contrôle à distance : Via MQTT broker (comme Mosquitto dans HA) et un accès distant sécurisé à HA.
- **Avantages** : Bon marché (total <20 €), local (pas de cloud), supporte positions précises et favoris. Communauté active en 2026.
- **Inconvénients** : Nécessite un peu de bricolage (mais tutoriels vidéo disponibles). Pas Zigbee, mais RF pur.

### 3. **RFXtrx433 (solution hardware dédiée, sans cloud)**

- **Description** : Un transceiver USB RF (433 MHz) qui supporte nativement Somfy RTS <https://www.domadoo.fr/fr/obsoletes/62-rfxcom-interface-rfxtrx433-usb-avec-recepteur-et-emetteur-43392mhz.html?srsltid=AfmBOoobrIQREYEhWvhhqYB-L_Hv_3oH_7YrB7mcy0H_jmIHtEQAYWW->.
- Il s'intègre directement à HA via l'intégration "RFXtrx", et gère les rolling codes en émulant les commandes. Portée excellente (jusqu'à 100 m), et supporte plusieurs volets.
- **Montage** :

  - Achetez un RFXtrx433E ou XL (environ 100 €).
  - Branchez-le via USB à votre serveur HA (Raspberry Pi ou autre).
  - Dans HA, ajoutez l'intégration RFXtrx > Activez "Ajout automatique".
  - Programmez : Utilisez votre télécommande Somfy pour envoyer des signaux ; RFXtrx les capture et crée des entités cover. (Ou utilisez RFXmngr pour configurer manuellement.)
  - Contrôle à distance : Via HA distant.
- **Avantages** : Fiable, supporte d'autres protocoles RF si besoin, intégration native HA.
- **Inconvénients** : Pas Zigbee, et nécessite un PC/serveur HA toujours allumé.

### 4. **Somfy TaHoma Switch (solution officielle, si vous acceptez un bridge dédié)**

- **Description** : Le hub officiel Somfy pour RTS [https://www.amazon.fr/So](https://www.amazon.fr/Somfy-1870755-connectivit%C3%A9-l%C3%A9clairage-smartphone/dp/B094YLCZFR/ref=sr_1_4?adgrpid=137663041375&dib=eyJ2IjoiMSJ9.XfnVcmy6DBVUEjRuKmC8PFllJDtsyZ2Ct5Iv3iTVh21smY7zGVxgPSUOQ2vmPlgqsE_DcWS1lVO_1CPc8x6LInKQ5a-xNVuJl1ePAlKj4nkElwlMs1Dx7js4ljTCH38zcJhcT8LQWqbCFRVKeCLU1rCPOeC6jPUNM7uakyqqg-y2A-XeHOpuwcso8xjNP8DtateNgyaeQyUip55ZB3D7qtMzULd1SyD5igPth6TAdhz5BlT1EOyr4FMPCkiEdMxh9dCeCaGvk_oOSn0dn8iLXRA13UK1suDoBKzhCVR4V4c.B897iS5fiom3S92MdZjCxiwZ7je1koBuEDk5fnBcRGc&dib_tag=se&hvadid=605387702155&hvdev=c&hvexpln=0&hvlocphy=9109104&hvnetw=g&hvocijid=14912068594618437827--&hvqmt=e&hvrand=14912068594618437827&hvtargid=kwd-1679916789101&hydadcr=15307_2293066&keywords=somfy%2Btahoma%2Bswitch%2Bbox&mcid=deeeb55b92253e88a7d64b540c280356&qid=1768735741&sr=8-4&th=1). Il connecte vos volets via RF, et s'intègre à HA via "Overkiz" (anciennement TaHoma). Contrôle à distance via l'app Somfy ou HA.
- **Montage** : Appairez vos volets au TaHoma, puis ajoutez Overkiz dans HA. Utilisez MQTT pour des automations avancées si voulu.
- **Avantages** : Officiel, fiable, supporte mises à jour.
- **Inconvénients** : Ajoute un système (app Somfy), et utilise du cloud (mais HA peut être local).

Pour le Zigbee pur : Malheureusement, il n'y a pas de module Zigbee direct pour Somfy RTS (qui est RF 433 MHz). Les modules Zigbee comme NOUS ou MOES sont pour volets filaires, pas radio. Si vos volets étaient Somfy Zigbee (nouveaux modèles), ce serait simple, mais ce n'est pas le cas.

---
