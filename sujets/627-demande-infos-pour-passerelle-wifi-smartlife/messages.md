---
title: "Demande infos pour passerelle wifi smartlife"
---

# Demande infos pour passerelle wifi smartlife

- **Catégorie :** [Smart Life / Tuya Smart](https://forumdomotique.com/forums/88-smart-life-tuya-smart/)
- **Sujet :** https://forumdomotique.com/forums/topic/627-demande-infos-pour-passerelle-wifi-smartlife/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 3
- **Premier message de XAV59213 :** 23 décembre 2025 à 14:06 (Europe/Paris)
- **Dernier message de XAV59213 :** 18 janvier 2026 à 11:52 (Europe/Paris)

---

## Message 1 — 23 décembre 2025 à 14:06 (Europe/Paris)

- **Identifiant :** `1609`
- **Lien :** https://forumdomotique.com/forums/topic/627-demande-infos-pour-passerelle-wifi-smartlife/#findComment-1609

Salut [@jpci](https://forumdomotique.com/profile/918-jpci/) ,

Il existe des petits hubs Zigbee pas trop chers.

J’en utilise un en ce moment pour mes interrupteurs tactiles avec rétro-éclairage :

<https://www.domadoo.fr/fr/domotique/6324-moes-box-domotique-zigbee-tuya-smart-life-ethernet.html>

---

## Message 2 — 24 décembre 2025 à 12:19 (Europe/Paris)

- **Identifiant :** `1614`
- **Lien :** https://forumdomotique.com/forums/topic/627-demande-infos-pour-passerelle-wifi-smartlife/#findComment-1614

Salut [@jpci](https://forumdomotique.com/profile/918-jpci/)

Oui, tu peux ajouter le hub sans problème ! Les hubs Zigbee (ou multimodes Zigbee/Bluetooth) compatibles avec les apps **Smart Life** ou **Tuya Smart** sont nombreux et fonctionnent parfaitement pour gérer jusqu'à un maximum d'appareils (souvent 50 à 128 selon le modèle).

Ces hubs servent justement à connecter et contrôler les appareils Zigbee (ampoules, interrupteurs, capteurs, etc.) via l'app Smart Life ou Tuya Smart, même si certains appareils WiFi fonctionnent déjà sans hub.

### Comment ajouter un hub :

1. Télécharge l'app **Smart Life** (recommandée, elle est plus complète et mieux supportée que Tuya Smart pour la plupart des utilisateurs).
2. Branche le hub (la plupart sont alimentés par USB ou filaire).
3. Dans l'app, clique sur "+" (ajouter un appareil) → cherche "Hub" ou "Passerelle" → sélectionne "Zigbee Gateway" ou similaire.
4. Suis les instructions (le hub clignote généralement pour le mode appairage).

Une fois ajouté, tu pourras y connecter tous tes appareils compatibles Tuya/Smart Life comme ta prise (y compris les Zigbee).

---

## Message 3 — 18 janvier 2026 à 11:52 (Europe/Paris)

- **Identifiant :** `1812`
- **Lien :** https://forumdomotique.com/forums/topic/627-demande-infos-pour-passerelle-wifi-smartlife/#findComment-1812

Bonjour [@jpci](https://forumdomotique.com/profile/918-jpci/) ,

Désolé d'entendre que tu rencontres des difficultés avec la passerelle Moes. Je vais essayer de t'expliquer ce qui se passe et te proposer des solutions adaptées, en me basant sur les specs du produit et des retours similaires.

### Pourquoi ça ne marche pas ?

- Tes prises connectées (comme celle que tu as partagée) sont **uniquement WiFi** (2.4 GHz), ce qui signifie qu'elles se connectent directement à ton routeur WiFi via l'app Smart Life/Tuya. Elles n'utilisent pas le protocole Zigbee.
- La passerelle Moes que tu as achetée (le modèle Ethernet Zigbee Tuya) est une **passerelle Zigbee** : elle sert à connecter des appareils Zigbee (comme des ampoules, capteurs ou interrupteurs compatibles Zigbee) à l'app Smart Life. Quand tu ajoutes un "sous-appareil" dans l'app, elle cherche des dispositifs Zigbee à proximité (d'où le mode appairage avec clignotement), pas des WiFi.
- Résultat : Tes plugs WiFi ne peuvent pas être "connectés" directement à cette passerelle comme sous-appareils. La compatibilité mentionnée pour les produits WiFi Tuya signifie juste que tu peux contrôler **à la fois** des appareils WiFi (ajoutés directement) et Zigbee (via la passerelle) dans la même app Smart Life. Mais ça n'offload pas tes connexions WiFi vers la passerelle – tes plugs WiFi continueront à utiliser ton routeur WiFi.

En gros, la passerelle ne résout pas ton problème de limite WiFi sur la box, car elle n'absorbe pas les connexions WiFi. Elle est utile seulement si tu passes à des appareils Zigbee, qui communiquent via la passerelle (connectée en Ethernet) au lieu d'utiliser le WiFi.

### Comment ajouter tes plugs existants ?

- Dans l'app Smart Life, n'essaie pas d'ajouter tes plugs comme "sous-appareils" de la passerelle. Ajoute-les **directement** comme des appareils WiFi normaux :

  1. Clique sur "+" pour ajouter un appareil.
  2. Sélectionne "Prise électrique" ou similaire (pas sous la catégorie passerelle).
  3. Mets la prise en mode appairage (généralement en maintenant le bouton jusqu'à ce qu'elle clignote).
  4. L'app la trouvera via ton WiFi (pas via la passerelle).
- Si l'app détecte déjà la passerelle, c'est bon – elle sert pour les futurs appareils Zigbee.

### Solutions pour ton problème principal (trop d'appareils WiFi sur la box)

Ton souci vient de la limite de connexions simultanées sur ton routeur (souvent 20-50 max pour les box basiques des FAI). Voici des options concrètes :

1. **Migrer vers des appareils Zigbee** :

   - Puisque tu as déjà la passerelle Moes (qui supporte jusqu'à 300 appareils Zigbee), remplace progressivement tes plugs WiFi par des versions Zigbee compatibles Tuya/Smart Life. Exemples :

     - Prises Zigbee Tuya sur Amazon ou Domadoo (cherche "prise Zigbee Tuya" – environ 10-15€ pièce).
     - Avantage : Les appareils Zigbee se connectent à la passerelle (via radio Zigbee, pas WiFi), ce qui libère ton WiFi. La passerelle gère tout via Ethernet, et tu contrôles via l'app.
     - Pour appairer : Dans l'app, va dans la passerelle > Ajouter sous-appareil > Sélectionne le type (ex. prise) > Mets l'appareil Zigbee en mode appairage.
2. **Améliorer ton réseau WiFi** :

   - **Change de routeur/box** : Opte pour un modèle qui gère plus de connexions, comme un routeur mesh (ex. TP-Link Deco, Google Nest Wifi, ou Netgear Orbi). Les systèmes mesh AX (WiFi 6) peuvent gérer 50-100+ appareils sur 2.4 GHz sans problème. Vérifie les specs : cherche "nombre de clients max".
   - **Ajoute un point d'accès (AP) dédié pour l'IoT** : Branche un AP WiFi 2.4 GHz séparé (ex. TP-Link EAP ou un vieux routeur en mode AP) sur ton routeur principal. Crée un SSID dédié pour tes appareils smart (ex. "IoT_2.4"). Ça répartit la charge.
   - **Sépare les bandes WiFi** : Dans les paramètres de ton routeur, crée des SSIDs séparés pour 2.4 GHz (pour IoT) et 5 GHz (pour ordinateurs/téléphones). Ça évite la surcharge sur une seule bande.
   - **Vérifie l'airtime fairness** : Certains routeurs ont une option "Airtime Fairness" qui peut causer des problèmes avec les IoT lents. Désactive-la si disponible.

---
