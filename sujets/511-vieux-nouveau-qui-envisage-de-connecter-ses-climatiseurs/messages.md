---
title: "vieux nouveau qui envisage de connecter ses climatiseurs"
description: "À 80 ans et avec une maîtrise en informatique de gestion, vous êtes clairement un pionnier dans le domaine respect ! Je vais essayer de vous aider avec…"
image: /assets/images/vignettes-themes/presentation.jpg

date: 2025-11-25
cover_alt: "Vignette de rubrique Présentation / Communauté — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/511-vieux-nouveau-qui-envisage-de-connecter-ses-climatiseurs/">Lire et commenter sur Forum Domotique</a></p>

# vieux nouveau qui envisage de connecter ses climatiseurs

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/511-vieux-nouveau-qui-envisage-de-connecter-ses-climatiseurs/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 25 novembre 2025 à 18:44 (Europe/Paris)

---

## Message 1 — 25 novembre 2025 à 18:44 (Europe/Paris)

- **Identifiant :** `1319`
- **Lien :** https://forumdomotique.com/forums/topic/511-vieux-nouveau-qui-envisage-de-connecter-ses-climatiseurs/#findComment-1319

Bonjour Alain,

Tout d’abord, bienvenue sur le forum !

À 80 ans et avec une maîtrise en informatique de gestion, vous êtes clairement un pionnier dans le domaine respect !

Je vais essayer de vous aider avec vos climatiseurs équipés des modules SLWF-01 Pro. D’après ce que j’ai compris, vous avez 5 clim (probablement de la famille Midea ou compatibles, comme Idea, Neoclima, Electrolux, etc.), et vous voulez les piloter via Home Assistant : d’abord en local, puis à distance.

Les modules SLWF-01 Pro sont conçus précisément pour ça. Ils sont basés sur ESP8266 et pré-flashés avec ESPHome, ce qui les rend compatibles nativement avec Home Assistant pour un contrôle local (sans cloud). Ils remplacent ou s’ajoutent au port WiFi de vos clim pour permettre une intégration intelligente. Voici un guide étape par étape, simple et clair, basé sur des expériences partagées par d’autres utilisateurs (sur Reddit, forums HA, etc.). Je suppose que les modules sont déjà installés physiquement dans vos clim ; si ce n’est pas le cas, consultez la doc du fabricant (SMLight) pour le branchement.

**1. Préparation : Installer Home Assistant**

•  Si vous n’avez pas encore Home Assistant (HA), commencez par l’installer. Comme vous êtes un vieux routard de l’informatique, je vous recommande une installation sur un Raspberry Pi (modèle 4 ou 5 pour la performance) ou un mini-PC (comme un vieux PC recyclé).

•  Téléchargez l’image HA OS depuis le site officiel : [home-assistant.io](https://home-assistant.io).

•  Flashez-la sur une carte SD (avec Balena Etcher ou similaire) et démarrez.

•  Une fois HA lancé, accédez à l’interface web via <http://homeassistant.local:8123> (ou l’IP de votre machine).

•  Créez un compte utilisateur.

**2. Configurer les modules SLWF-01 Pro**

•  Chaque module doit être configuré individuellement (pour vos 5 clim).

•  Branchez le module dans la clim et allumez-la. Le module créera un point d’accès WiFi (AP) temporaire pour la configuration.

•  Le nom du réseau WiFi est souvent quelque chose comme “SLWF-XXXX” (les credentials sont indiqués sur l’emballage ou la doc du module – typiquement SSID : “SLWF-01”, mot de passe : “12345678” ou similaire ; vérifiez sur le site SMLight ou Amazon).

•  Connectez-vous à cet AP depuis un ordinateur ou smartphone.

•  Ouvrez un navigateur et allez à l’adresse IP du module (souvent 192.168.4.1 ou indiquée dans la doc).

•  Configurez le module pour qu’il se connecte à votre réseau WiFi domestique (SSID et mot de passe de votre box).

•  Une fois connecté, le module redémarrera et sera visible sur votre réseau local.

**Note :** Si vous avez des problèmes de détection, assurez-vous que votre réseau est en 2.4 GHz (les ESP8266 ne supportent pas le 5 GHz).

**3. Intégration en local avec Home Assistant**

•  Dans HA, installez l’intégration ESPHome si ce n’est pas déjà fait :

•  Allez dans **Paramètres > Appareils & Services > Ajouter une intégration > Recherchez “ESPHome”**.

•  Installez-la (c’est gratuit et local).

•  ESPHome devrait détecter automatiquement chaque module SLWF-01 Pro sur votre réseau (via mDNS).

•  Cliquez sur “Ajouter” pour chaque appareil détecté.

•  Il apparaîtra comme une entité “Climate” (climatisation) dans HA.

•  Testez : Dans l’interface HA, allez dans **Aperçu** ou créez un tableau de bord. Vous devriez pouvoir allumer/éteindre, régler la température, le mode (froid, chaud, ventilateur), la vitesse du ventilo, etc. Tout ça en local, sans internet.

**Astuces d’utilisateurs :**

•  Si vous voulez la fonction “Follow Me” (pour utiliser un capteur externe de température, car le capteur interne des clim Midea est souvent imprécis), il faut parfois souder un fil sur la carte du module pour simuler la télécommande IR. C’est optionnel, mais recommandé si vous automatisez via HA. Des tutos existent sur Reddit (recherchez “SLWF-01 Pro follow me soldering”).

•  Pour tweaker la config (ex. : ajouter un capteur externe), installez l’addon “ESPHome” dans HA (via **Paramètres > Add-ons > Boutique d’addons > Recherchez ESPHome**). Vous pourrez “adopter” les configs des modules et les modifier en YAML si besoin. Mais pour un usage basique, ce n’est pas nécessaire – ils sont préconfigurés.

**Pour vos 5 clim :** Répétez pour chaque module. Donnez-leur des noms clairs dans HA (ex. : “Clim Salon”, “Clim Chambre 1”, etc.).

**4. Contrôle à distance**

•  Une fois le local OK, passez au distant.

•  Option simple (payante, mais facile) : Abonnez-vous à Home Assistant Cloud (Nabu Casa) pour ~6€/mois. Ça configure tout automatiquement : accès distant sécurisé via app mobile ou web, sans bidouiller les ports de votre box.

•  Dans HA : **Paramètres > Home Assistant Cloud > S’inscrire**.

•  Option gratuite (plus technique) :

•  Utilisez DuckDNS pour un domaine dynamique (addon gratuit dans HA).

•  Configurez un certificat SSL avec Let’s Encrypt (via addon Nginx ou similaire).

•  Ouvrez le port 8123 sur votre box (redirection vers l’IP de HA), mais attention à la sécurité – utilisez un VPN si possible.

•  Installez l’app HA sur iOS/Android pour l’accès mobile.

•  Testez : Depuis dehors (via 4G), connectez-vous à HA et contrôlez vos clim.

**Problèmes courants et solutions**

•  **Module non détecté :** Vérifiez le WiFi (2.4 GHz), redémarrez HA et le module. Logs ESPHome dans HA pour debug.

•  **Stabilité :** Certains utilisateurs disent que le firmware d’origine est moyen ; si bugs, re-flashez avec un YAML custom ESPHome (ex. via GitHub comme adamgranted/SLWF-01_Della pour les modèles compatibles). Mais pour la plupart, ça marche out-of-the-box.

•  **Compatibilité :** Confirmez que vos clim sont bien de la famille Midea (le module est optimisé pour ça). Si non, testez un par un.

•  Si vous avez des erreurs, regardez les logs dans HA (**Paramètres > Journaux système**).

Si vous avez plus de détails sur la marque de vos clim (Midea ? Della ? Autre ?), ou des erreurs spécifiques, je peux affiner. D’autres ont réussi avec ce setup, et comme vous êtes informaticien, ça devrait rouler !

---
