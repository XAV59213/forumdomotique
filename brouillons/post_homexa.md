---
title: "post_homexa"
description: "🎉 Freebox Homexa arrive dans HACS par défaut ! (+ les nouveautés jusqu'à la 28.8.74) Petite nouvelle qui me fait super plaisir : Freebox Homexa est…"
image: /assets/images/og-default.png
date: 2026-11-20
sitemap: false
robots: noindex, nofollow
---
**🎉 Freebox Homexa arrive dans HACS par défaut ! (+ les nouveautés jusqu'à la 28.8.74)**

Bonjour à tous,

Petite nouvelle qui me fait super plaisir : **Freebox Homexa est maintenant disponible directement dans la bibliothèque HACS** 🥳
Après une revue complète par frenck (l'équipe HACS / Home Assistant), le projet a été validé et intégré au store par défaut le 2 novembre 2026. Un grand merci à lui pour tous ses retours détaillés, ils ont vraiment fait progresser l'intégration.

### 📦 Installation : encore plus simple

Plus besoin d'ajouter le dépôt personnalisé ! Il suffit de :
1. Ouvrir **HACS** dans Home Assistant
2. Chercher **« Freebox Homexa »**
3. Télécharger, redémarrer, puis ajouter l'intégration

Ou en un clic : 👉 https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=freebox_homexa&category=integration

Si vous l'aviez déjà installée en dépôt personnalisé, pas de panique : tout continue de fonctionner comme avant.

### 🃏 Une carte Freebox Homexa enfin réglable

La carte **freebox-homexa-card** a eu droit à un vrai coup de neuf :
- un éditeur visuel natif Home Assistant, avec de vrais sélecteurs d'entités
- **plusieurs volets** (mais aussi plusieurs alarmes, détecteurs PIR, Players, capteurs RSSI) : une tuile par entité, chacune avec ses boutons
- des **sections masquables** (alarme, volets, PIR, Player, RSSI) et un titre facultatif
- la carte se pré-remplit toute seule avec vos entités Freebox à l'ajout

Vos cartes existantes s'affichent exactement comme avant, pas besoin de les refaire.

### 📺 Guide TV TNT : plus fluide

- les libellés des interrupteurs de l'éditeur de la carte **homexa-tnt-card** étaient passés à la trappe avec les dernières versions de HA : ils sont de retour
- la mise à jour horaire du guide XMLTV (~78 Mo) ne bloque plus Home Assistant. Sur un HA Green, ça pouvait figer le système une dizaine de secondes (et faire tousser ZHA…). C'est réglé, et ça consomme moins de mémoire

Merci au passage à **cyclope205** : la carte TNT est adaptée de son super projet *Programme TNT FR* 🙏

### 📞 Nouveau : la carte « Homexa Appels »

Une nouvelle carte **custom:homexa-calls-card** pour afficher le journal d'appels de la Freebox, avec un joli rendu :
- une ligne par appel avec une icône colorée (manqué / reçu / émis), le nom, l'heure, « Aujourd'hui » / « Hier », la durée
- un point rouge sur les non lus et un badge « N manqués »
- un éditeur visuel : nombre d'appels (1 à 30), types affichés, numéro et durée en option

Elle s'appuie sur le nouveau capteur **« Derniers appels Freebox »**, dont l'état donne le nombre d'appels non lus.

🔒 **Côté vie privée** (suite à la revue HACS) : les noms et numéros ne sont plus stockés dans les attributs des capteurs. La carte récupère l'historique via une commande WebSocket sécurisée, réservée aux utilisateurs qui ont le droit de voir le capteur.
⚠️ Les attributs du capteur « Appels manqués Freebox » ont aussi été retirés (son état ne change pas). Si vous aviez une carte Markdown ou une automatisation qui lisait ces attributs, passez à la carte **Homexa Appels**.

### 🛡️ Respect des autres intégrations

Homexa ne touche plus **jamais** aux appareils des autres intégrations (Shelly, ESPHome…), même quand ils partagent la même adresse MAC : pas de renommage, pas de déplacement, pas de suppression. C'est testé, et la même protection arrive aussi sur la fusion des répéteurs dans la prochaine version.

### 🔗 Les liens

- Dépôt GitHub : https://github.com/XAV59213/freebox_homexa
- Release 28.8.74 : https://github.com/XAV59213/freebox_homexa/releases/tag/28.8.74
- Ouvrir dans HACS : https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=freebox_homexa&category=integration

Comme toujours, vos retours, idées et remontées de bugs sont les bienvenus, ici ou sur GitHub 😉
Rappel : Freebox Homexa est un projet communautaire indépendant, il n'est ni affilié ni soutenu par Free / Iliad. Il utilise uniquement l'API officielle Freebox OS.

Merci à tous et bonne domotique ! 🏠
XAV59213
