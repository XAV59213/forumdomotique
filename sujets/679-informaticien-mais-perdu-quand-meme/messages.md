---
title: "Informaticien, mais perdu quand même ^^"
description: "Ravi de te voir revenir aux forums ,c’est sympa de bricoler un peu de domotique pour ajouter du confort à la maison. Ton projet de projecteur extérieur…"
image: /assets/images/og-default.png
date: 2026-01-12
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/679-informaticien-mais-perdu-quand-m%C3%AAme/">Lire et commenter sur Forum Domotique</a></p>

# Informaticien, mais perdu quand même ^^

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/679-informaticien-mais-perdu-quand-m%C3%AAme/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 12 janvier 2026 à 10:16 (Europe/Paris)
- **Dernier message de XAV59213 :** 13 janvier 2026 à 06:25 (Europe/Paris)

---

## Message 1 — 12 janvier 2026 à 10:16 (Europe/Paris)

- **Identifiant :** `1743`
- **Lien :** https://forumdomotique.com/forums/topic/679-informaticien-mais-perdu-quand-m%C3%AAme/#findComment-1743

Bonjour [@Aurel](https://forumdomotique.com/profile/1098-aurel/)

Ravi de te voir revenir aux forums ,c’est sympa de bricoler un peu de domotique pour ajouter du confort à la maison. Ton projet de projecteur extérieur avec détection de mouvement, pilotable via interrupteur et domotique, sans ajouter de fils, est un bon premier pas. C’est simple, scalable, et ça permet d’étendre ensuite à d’autres éclairages. Je vais donner mon avis, des critiques constructives, et répondre à tes questions spécifiques basées sur ce que j’ai pu vérifier.

**Avis général sur ton setup proposé**

Ton idée avec un projecteur contrôlé en parallèle par un détecteur PIR filaire classique et un relais Zigbee (comme le SONOFF ZBMINIR2) est solide. Ça permet :

•  Une détection autonome via le PIR (pas de dépendance au réseau pour l’allumage basique).

•  Un contrôle manuel via un interrupteur Zigbee intérieur (qui pilote le relais).

•  Une intégration domotique pour des automatisations futures (ex: allumage via app ou scénarios).

Avantages :

•  Pas besoin de tirer de nouveaux câbles, ce qui est parfait pour un retrofit.

•  Scalable : Tu pourras ajouter d’autres relais ou capteurs Zigbee pour étendre l’éclairage (ex: plusieurs spots synchronisés).

•  Budget-friendly pour commencer, surtout post-fêtes.

Critiques et points d’attention :

•  **Sécurité électrique** : Assure-toi que le relais Zigbee est bien dimensionné pour la puissance du projecteur (le ZBMINIR2 gère jusqu’à 10A, ce qui est ok pour la plupart des projecteurs LED extérieurs, mais vérifie la conso). Utilise un boîtier étanche pour l’extérieur et respecte les normes (terre, etc.). Si tu n’es pas à l’aise, fais appel à un électricien pour l’installation.

•  **Fiabilité du PIR filaire** : Les PIR classiques sont robustes, mais ils peuvent avoir des faux positifs (animaux, vent). Un capteur Zigbee pourrait le remplacer plus tard pour plus de flexibilité (ex: ajustements via app).

•  **Interrupteur Zigbee** : Choisis-en un compatible avec ton hub (ex: Aqara ou SONOFF). Si tu veux un look “classique”, opte pour un modèle sans fil qui se pose sur un mur existant.

•  **Extension future** : Pense à la topologie du réseau Zigbee – place des routeurs (comme des prises connectées) pour renforcer le maillage si ton jardin est grand.

Globalement, c’est un bon plan pour ne pas louper la première marche. Pas besoin d’un autre thread!

**Sur le direct binding Zigbee**

Oui, c’est possible ! Le “direct binding” (ou simplement “binding” en Zigbee) permet à des dispositifs de communiquer directement entre eux sans passer par le hub/coordinateur. C’est une feature du protocole Zigbee pour augmenter la fiabilité : si le hub ou internet plante, les liens directs restent opérationnels. Par exemple, un interrupteur peut contrôler un relais/lumière sans round-trip via le hub, ce qui rend la réponse plus rapide et résiliente.

Comment ça marche :

•  Le hub initie le binding (il “lie” les endpoints des dispositifs).

•  Une fois lié, les commandes passent en peer-to-peer.

•  C’est idéal pour ton cas : l’interrupteur Zigbee pourrait binder directement au relais, et un capteur de mouvement Zigbee pourrait binder au projecteur/relais.

•  Limitations : Pas tous les dispositifs le supportent. Ça marche bien avec des “sources” comme des remotes, boutons ou capteurs (ex: IKEA Tradfri, Philips Hue remotes, certains SONOFF). Pour les “cibles” comme des lumières ou relais, c’est variable certains Aqara ne le font pas, et certains Hue bulbs ont des limites (ex: on/off ok, mais pas couleur).

Sources claires :

•  La doc Zigbee2MQTT explique bien : Tu peux binder via MQTT (ex: lier un interrupteur à un groupe de dispositifs).

•  Des tutos sur Reddit et Medium montrent des exemples concrets, comme binder un bouton à une ampoule pour un contrôle offline.

•  Dans Home Assistant (ZHA ou Zigbee2MQTT), c’est intégré via l’interface : Tu sélectionnes “bind” sur le dispositif source vers la cible.

Pour le SONOFF ZBMINIR2 spécifiquement : Il supporte le binding, car c’est un relais standard Zigbee 3.0. Des utilisateurs l’ont testé avec Zigbee2MQTT pour binder à des interrupteurs ou capteurs.  Ça devrait marcher sans hub, une fois le binding configuré.

Si tu ajoutes des capteurs Zigbee, vérifie leur support (ex: via la liste de compatibilité de Zigbee2MQTT).

**Compatibilité avec Tahoma comme hub temporaire**

Bonne idée pour démarrer sans gros budget – la Tahoma Switch peut servir de hub Zigbee basique. Cependant :

•  Pas tous les périphériques Zigbee sont compatibles nativement avec Tahoma (Somfy est sélectif pour éviter les bugs).

•  Pour le SONOFF ZBMINIR2 : Il est compatible ! Des retours indiquent qu’il fonctionne pour l’ON/OFF.   Mais attention : Avec un interrupteur externe, seul un toggle switch (bascule) est supporté, pas un poussoir momentané (à cause de la façon dont Tahoma gère les états). Si tu utilises un interrupteur standard, ça ira.

•  Direct binding avec Tahoma : Pas nativement supporté dans l’interface Tahoma (c’est plus pour des scénarios simples). Tu devras attendre une box plus avancée comme Home Assistant pour le configurer facilement.

•  Liste officielle Somfy : Elle inclut des produits comme Izymo, mais pas explicitement SONOFF cependant, des users l’ont intégré via Zigbee générique.

Si ça coince, teste avec Zigbee2MQTT sur un PC temporaire pour valider.

**Pour la box future : Nabu Casa Home Assistant Green vs homeassitant sur Raspberry**

Les deux sont excellents pour harmoniser tout

•  **Home Assistant Green (Nabu Casa)** : Prêt à l’emploi, facile pour un débutant. Grande communauté (50k+ users Zigbee), interface intuitive, automatisations puissantes. Avantages : Mises à jour auto, addon Zigbee2MQTT ou ZHA pour binding facile. Inconvénients : Moins “français” que Jeedom, mais traductions ok. Prix ~150€. Idéal si tu veux du plug-and-play.

•  **Home Assistant sur Raspberry 3 ou 4** : Plus flexible, communauté francophone forte. (RPi + dongle ~150€).

Mon conseil : Si tu aimes bidouiller (comme tes sites web), va sur Home Assistant sur Raspberry ou vieux pc

---

## Message 2 — 13 janvier 2026 à 06:25 (Europe/Paris)

- **Identifiant :** `1769`
- **Lien :** https://forumdomotique.com/forums/topic/679-informaticien-mais-perdu-quand-m%C3%AAme/#findComment-1769

Le mieux est de commencer simple avec un vieux pc ou raspberry 3 par exemple pour home assistant

et oui pour les 2 pistes a suivre après il y a d’autres solutions avec le zigbee la smligth il ya la possibilité de tout faire depuis l os

---
