---
title: "Conseil domotique"
description: "Pour domotiser vos volets roulants sur Home Assistant avec une installation mixte (Somfy radio, Nice radio, et Nice filaire avec interrupteur), il faut…"
image: /assets/images/og-default.png
date: 2025-06-08
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/197-conseil-domotique/">Lire et commenter sur Forum Domotique</a></p>

# Conseil domotique

- **Catégorie :** [Bien débuter en domotique](https://forumdomotique.com/forums/99-bien-d%C3%A9buter-en-domotique/)
- **Sujet :** https://forumdomotique.com/forums/topic/197-conseil-domotique/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 8 juin 2025 à 10:30 (Europe/Paris)

---

## Message 1 — 8 juin 2025 à 10:30 (Europe/Paris)

- **Identifiant :** `420`
- **Lien :** https://forumdomotique.com/forums/topic/197-conseil-domotique/#findComment-420

> **il y a 30 minutes, francki a dit :**
> Bonjour à tous,je souhaite domotiser mes volets roulants, et je n ai aucune idée de la manière dont je dois m y prendre,j ai du Somfy radio sur mes baie vitrée,du nice radio sur mes fenêtres et du nice interrupteur a l étage.
>
> Merci pour vos conseils

Salut [@francki](https://forumdomotique.com/profile/186-francki/)

Pour domotiser vos volets roulants sur Home Assistant avec une installation mixte (Somfy radio, Nice radio, et Nice filaire avec interrupteur), il faut prendre en compte les protocoles de communication (Somfy RTS ou IO, Nice radio, et filaire) et leur compatibilité avec Home Assistant. Voici des solutions adaptées à chaque type de volet, avec des recommandations pour centraliser leur contrôle.

### 1. **Somfy Radio (RTS ou IO sur les baies vitrées)**

Somfy utilise principalement deux protocoles radio : **RTS** (plus ancien, unidirectionnel) ou **IO-homecontrol** (bidirectionnel, avec retour d'état). Voici comment procéder :

- **Identifier le protocole** : Vérifiez si vos volets Somfy sont en RTS ou IO. Cela peut être indiqué sur la télécommande ou dans la documentation. Les télécommandes IO ont souvent un bouton "My" et un retour d'état visible.
- **Solution pour Somfy RTS** :

  - **Matériel** : Utilisez un **RFXtrx433E** (transcepteur 433 MHz) connecté à Home Assistant. Ce module est compatible avec le protocole RTS de Somfy. Prix : ~100-120€.
  - **Installation** :

    1. Branchez le RFXtrx433E à votre serveur Home Assistant (via USB).
    2. Configurez l'intégration RFXtrx dans Home Assistant (via l'interface ou fichier YAML).
    3. Associez chaque volet en appuyant sur le bouton "Prog" de la télécommande Somfy pour l'appairer avec le RFXtrx.
  - **Avantages** : Solution économique, compatible avec la plupart des volets RTS. Permet de contrôler les volets via Home Assistant (montée, descente, stop).
  - **Limites** : Pas de retour d'état (vous ne savez pas si le volet est ouvert ou fermé).
- **Solution pour Somfy IO** :

  - **Matériel** : La box **Somfy TaHoma Switch** (~200€) est la solution officielle pour IO-homecontrol. Elle se connecte à Home Assistant via l'intégration officielle Somfy.
  - **Installation** :

    1. Configurez la TaHoma Switch via l'application Somfy (Tahoma app).
    2. Ajoutez vos volets IO dans l'application.
    3. Installez l'intégration Somfy dans Home Assistant (via HACS ou manuellement).
    4. Connectez Home Assistant à la TaHoma Switch avec vos identifiants Somfy.
  - **Avantages** : Retour d'état précis (position exacte des volets), scénarios avancés (ex. : ouvrir à 30 % si température > 25°C).
  - **Limites** : Coût plus élevé. Dépendance au cloud Somfy (bien que l'intégration locale soit possible avec certaines versions).
- **Alternative avancée pour IO** : Si vous voulez éviter la TaHoma, un module **Velux KLF-200** (~200€) peut contrôler les volets IO (Somfy et Velux partagent IO-homecontrol). Nécessite des compétences techniques pour l'intégration via Home Assistant (souvent via MQTT ou Z-Wave).

### 2. **Nice Radio (fenêtres)**

Les volets Nice radio utilisent généralement un protocole radio propriétaire sur 433 MHz. La compatibilité avec Home Assistant dépend du modèle exact.

- **Solution 1 : RFXtrx433E** :

  - **Matériel** : Le même RFXtrx433E utilisé pour Somfy RTS peut parfois fonctionner avec certains moteurs Nice radio, car ils utilisent des fréquences similaires (433 MHz).
  - **Installation** :

    1. Testez la compatibilité en essayant d'appairer une télécommande Nice avec le RFXtrx (bouton d'association sur la télécommande).
    2. Configurez les volets dans Home Assistant comme des "covers".
  - **Avantages** : Réutilisation du même matériel que pour Somfy RTS, donc économique si compatible.
  - **Limites** : La compatibilité n'est pas garantie pour tous les moteurs Nice. Pas de retour d'état.
- **Solution 2 : Box Nice ou passerelle tierce** :

  - **Matériel** : Nice propose des hubs comme le **Nice Yubii Home** ou des passerelles radio (ex. : Nice IT4WIFI). Vérifiez la compatibilité avec vos volets.
  - **Installation** :

    1. Configurez la passerelle Nice via l'application officielle.
    2. Intégrez-la à Home Assistant via une intégration tierce (souvent via MQTT ou API, car Nice n'a pas d'intégration native).
  - **Avantages** : Solution officielle, potentiellement plus stable pour Nice.
  - **Limites** : Coût élevé (~150-250€). Intégration dans Home Assistant parfois complexe.
- **Solution 3 : Modules universels** :

  - Si le RFXtrx ne fonctionne pas, envisagez des modules comme **Broadlink RM4 Pro** (~40€), qui clonent les signaux radio des télécommandes Nice.
  - **Installation** : Apprenez les commandes de la télécommande Nice au Broadlink via son application, puis intégrez-le à Home Assistant via l'intégration Broadlink.
  - **Avantages** : Bon marché, flexible.
  - **Limites** : Configuration manuelle, pas de retour d'état.

### 3. **Nice Filaire avec Interrupteur (étage)**

Les volets Nice filaires sont contrôlés par des interrupteurs muraux (montée/descente). Pour les domotiser, il faut ajouter un module connecté derrière l'interrupteur.

- **Solution 1 : Modules Zigbee/Wi-Fi** :

  - **Matériel** : Utilisez des modules comme **Shelly 2.5** (~25€ par volet) ou **Tuya Zigbee Volet Roulant** (~20€). Assurez-vous que l'interrupteur a un fil neutre (souvent absent dans les installations anciennes).
  - **Installation** :

    1. Coupez l'alimentation électrique.
    2. Installez le module Shelly/Tuya derrière l'interrupteur (suivez le schéma de câblage : phase, neutre, fils de montée/descente).
    3. Associez le module à Home Assistant via Zigbee (nécessite un hub Zigbee comme Conbee II ou Zigbee2MQTT) ou Wi-Fi.
    4. Configurez le module comme un "cover" dans Home Assistant.
  - **Avantages** : Maintient la compatibilité avec l'interrupteur manuel. Shelly est très fiable et bien intégré à Home Assistant. Retour d'état possible avec Shelly.
  - **Limites** : Nécessite un neutre. Installation électrique requise (faites appel à un électricien si vous n'êtes pas à l'aise).
- **Solution 2 : Micro-modules Somfy RTS** :

  - **Matériel** : Si vous souhaitez uniformiser avec les volets Somfy, un **micro-module Somfy RTS** (~90€ par volet) peut transformer un volet filaire en radio RTS.
  - **Installation** :

    1. Installez le micro-module derrière l'interrupteur.
    2. Associez-le au RFXtrx433E (comme pour les volets Somfy RTS).
  - **Avantages** : Uniformise la gestion avec les volets Somfy RTS. Contrôle via le même RFXtrx.
  - **Limites** : Plus cher que Shelly/Tuya. Pas de retour d'état.

### 4. **Centralisation et Scénarios dans Home Assistant**

Une fois les volets intégrés à Home Assistant, vous pouvez :

- **Grouper les volets** : Créez des groupes dans Home Assistant pour contrôler tous les volets ensemble (ex. : "tous les volets du rez-de-chaussée").
- **Créer des scénarios** :

  - Exemple 1 : "Ouvrir tous les volets à 7h, sauf s'il fait >25°C."
  - Exemple 2 : "Fermer les volets à la tombée de la nuit (basé sur le capteur de luminosité ou l'heure du coucher du soleil)."
  - Utilisez Node-RED ou les automatisations natives pour des scénarios complexes.
- **Contrôle vocal** : Intégrez Home Assistant à Google Home ou Alexa pour des commandes vocales.
- **Simulation de présence** : Programmez des ouvertures/fermetures aléatoires pour simuler une présence en vacances.

### 5. **Recommandations Générales**

- **Budget minimal** :

  - RFXtrx433E (~120€) pour Somfy RTS et potentiellement Nice radio.
  - Shelly 2.5 (~25€ par volet) pour les volets filaires Nice.
  - Total : ~120€ + 25€ par volet filaire.
- **Solution robuste** :

  - Somfy TaHoma Switch (~200€) pour Somfy IO.
  - Nice Yubii Home (~200€) pour Nice radio.
  - Shelly 2.5 pour volets filaires.
  - Total : ~400€ + 25€ par volet filaire.
- **Compatibilité** : Vérifiez les protocoles exacts (RTS/IO pour Somfy, modèle de Nice radio). Si possible, partagez les références des moteurs/télécommandes pour des conseils précis.
- **Installation électrique** : Pour les volets filaires, assurez-vous d'avoir un neutre. Sinon, envisagez des modules alimentés par batterie (rares et plus chers).
- **Évolutivité** : Privilégiez Zigbee ou Z-Wave pour les modules filaires (Shelly, Tuya) pour une meilleure intégration future avec d'autres appareils.

### 6. **Étapes pour commencer**

1. **Diagnostiquez vos volets** :

   - Confirmez si les Somfy sont RTS ou IO (regardez la télécommande ou contactez Somfy avec la référence).
   - Vérifiez le modèle des Nice radio (télécommande ou moteur).
   - Pour les Nice filaires, vérifiez la présence d'un neutre dans les boîtes d'encastrement.
2. **Achetez le matériel** :

   - RFXtrx433E pour tester Somfy RTS et Nice radio.
   - Un module Shelly 2.5 pour tester un volet filaire.
3. **Testez et configurez** :

   - Intégrez un premier volet dans Home Assistant.
   - Si ça fonctionne, étendez aux autres.
4. **Ajoutez des scénarios** : Une fois tous les volets intégrés, configurez des automatisations.

---
