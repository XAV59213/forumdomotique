---
layout: ha-dev
title: 'Bêta Home Assistant 2026.12 : un dialogue de volets qu’on attrape, des boutons multi-appuis et Home Assistant Link'
short_title: 'Bêta 2026.12 : volets dessinés et boutons multi-appuis'
description: 'La bêta de Home Assistant 2026.12 en cours en français : dialogue des volets redessiné, boutons multi-appuis, voix nouvelle génération, Freebox et Météo-France.'
excerpt_fr: 'Bêta en cours : le dialogue des volets dessine votre volet, les boutons gèrent double appui et appui long, la voix nouvelle génération arrive dans Labs, et Cloud devient Link. Pour nous : volets Freebox et alerte Météo-France à vérifier.'
image: /actualite-ha-dev/home-assistant-2026-12-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.12, décembre 2026'
date: 2026-11-25
section: actualite-ha-dev
cycle: 2026-12
version: '2026.12'
month: Décembre 2026
planned_fr: 2 décembre 2026
release_url: https://rc.home-assistant.io/blog/2026/11/25/release-202612/
official_title: '2026.12 Beta: Under cover 🪟'
forum_url: https://forumdomotique.com/forums/topic/4102-home-assistant-202612-b%C3%AAta-un-dialogue-de-volets-quon-attrape-des-boutons-multi-appuis-et-home-assistant-link/
gallery:
- src: images/cover-more-info.webp
  caption: 'Le nouveau dialogue des volets : le dessin du volet sert de commande.'
- src: images/timer-list-dialog.webp
  caption: Les minuteurs vocaux d’un satellite, avec compte à rebours, dans la nouvelle entité Liste de minuteurs.
- src: images/camera-player.webp
  caption: Le lecteur de caméra de Home Assistant, identique sur tous les navigateurs et dans les applications.
- src: images/energy-batteries.webp
  caption: 'Tableau Énergie : la batterie domestique mesurée par sens de circulation.'
- src: images/energy-suggestions.webp
  caption: Paramètres › Énergie propose les compteurs oubliés à ajouter au tableau.
- src: images/add-device-or-integration.webp
  caption: Le dialogue unique « Ajouter un appareil ou une intégration ».
- src: images/startup-details.webp
  caption: Suivre le démarrage de Home Assistant en direct, intégration par intégration.
- src: images/integration-health.webp
  caption: 'L’élément « Santé » d’une intégration : entités, réparations, erreurs du journal.'
- src: images/database-usage.webp
  caption: 'La carte Base de données de la page Stockage : quelles tables et quelles entités prennent de la place.'
- src: images/link-settings.webp
  caption: Home Assistant Cloud devient Home Assistant Link dans les Paramètres.
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.12'
seo:
  type: NewsArticle
---
La bêta de la dernière version de l’année est en cours. La **2026.12.0b0** a été publiée le **25 novembre 2026** au soir, suivie de la **b1** et de la **b2** le **26 novembre**. Les notes de la bêta annoncent la sortie et sa *release party* pour le **2 décembre 2026**. Rien n’est figé : comme le rappellent ces notes, certaines fonctionnalités **peuvent ne pas arriver** dans la version finale, et une intégration annoncée a d’ailleurs déjà été retirée.

<div class="ha-callout info" markdown="1">
**En bref**
- 🪟 **Volets** : un nouveau dialogue qui dessine votre volet et se commande en l’attrapant, des positions favorites, et des volets qui s’affichent en bleu quand ils sont ouverts.
- 🔘 **Boutons** : double, triple ou quadruple appui, appui long qui se répète, relâchement, pour toutes les marques qui suivent la nouvelle norme.
- 🗣️ **Voix nouvelle génération** dans Labs, minuteurs vocaux visibles dans Home Assistant, lecteur de caméra unifié, batteries **mesurées** dans le tableau Énergie.
- 🔗 **Home Assistant Cloud devient Home Assistant Link**, sans rien à faire de votre côté.
- 🇫🇷 Pour nous : les **volets roulants Freebox** arrivent, et l’**état de l’alerte Météo-France** change (à vérifier dans vos automatisations).
</div>

## 🧪 Ce qui est en test

### 🪟 Un dialogue de volets qu’on attrape

Le dialogue commun à tous les volets (stores, volets, rideaux, portes de garage, portails) est **redessiné de zéro**. Il affiche maintenant un **dessin du volet** adapté à son type, et ce dessin sert de commande : un appui envoie le volet à la position choisie, un glisser le déplace depuis sa position actuelle. En dessous se trouvent des boutons Ouvrir, Stop et Fermer. Les volets avec inclinaison ont un sélecteur position/inclinaison, et l’on peut enregistrer ses **positions favorites**. Les volets ouverts s’affichent en **bleu** sur les tuiles, et les icônes sont rafraîchies (les stores bannes ont enfin la leur).

{% include ha-figure.html src="images/cover-more-info.webp" caption="Le nouveau dialogue des volets : le dessin du volet est la commande." %}

### 🔘 Des boutons qui en font plus

Le déclencheur **Bouton appuyé** fonctionne désormais aussi avec les télécommandes et interrupteurs muraux, avec un **nombre d’appuis** : double, triple ou quadruple. Deux nouveaux déclencheurs arrivent : **Bouton maintenu**, qui peut se répéter à intervalle tant que le bouton est maintenu (pour faire varier une lumière pas à pas), et **Fin du maintien**, au relâchement. Une condition **Le bouton est maintenu** les accompagne. C’est une première étape : pour l’instant, Universal Devices ISY/IoX gère tout, Lutron Caséta et OpenDisplay en partie. Les automatisations existantes ne changent pas tant qu’on n’utilise pas ces options.

### 🗣️ Voix nouvelle génération (Labs) et minuteurs vocaux

Quand un satellite vocal se réveille, Home Assistant envoie le bout d’audio à un **modèle de mot d’activation bien plus gros**, qui confirme que vous avez vraiment dit le mot d’activation. Résultat : plus besoin d’attendre le bip (« Okay Nabu, allume les lumières » d’une traite), et moins de commandes coupées. Cette fonction s’active dans **Paramètres › Système › Labs** (« Next-generation voice »). Elle vérifie pour l’instant Okay Nabu, Hey Jarvis et Hey Mycroft. La Voice Preview Edition a besoin de son **firmware bêta**.

Les minuteurs lancés à la voix sur les satellites ESPHome rejoignent une nouvelle entité **Liste de minuteurs**, avec une carte qui affiche le compte à rebours et permet de démarrer, prolonger, mettre en pause ou annuler un minuteur.

### 📹 Un lecteur de caméra identique partout

Le dialogue des caméras a maintenant son propre lecteur. On peut **zoomer** (au pincement, au double clic ou avec Ctrl/Cmd et la molette), passer en **image dans l’image**, y compris pour les caméras MJPEG, et voir par un badge le mode de transmission utilisé (WebRTC, HLS ou MJPEG). L’écran reste allumé tant que la caméra est ouverte.

### ⚡ Un tableau Énergie plus juste

- **Batteries mesurées** : si votre batterie le permet, vous déclarez l’énergie par sens de circulation (depuis le réseau, depuis le solaire, vers la maison, vers le réseau) au lieu d’une estimation. Sa capacité utile peut venir d’un capteur.
- **Compteurs oubliés** : Paramètres › Énergie liste les compteurs d’énergie, de gaz et d’eau qui ne sont pas encore dans le tableau.
- Les réglages s’ouvrent en pleine page, les sources de même type peuvent être regroupées, les appareils au gaz s’ajoutent individuellement, et le graphique d’électricité affiche le coût net de la période.

### 🔗 Home Assistant Cloud devient Home Assistant Link

Le changement annoncé en octobre est officiel : même service, nouveau nom et nouvelle icône. Les sauvegardes cloud s’appellent désormais **sauvegardes hors site**. Il n’y a **rien à faire** : l’intégration garde le domaine `cloud`, et votre YAML ne change pas. Les notes en profitent pour rappeler que Home Assistant appartient à l’Open Home Foundation, une fondation à but non lucratif, et que Nabu Casa en est un partenaire commercial.

### 🔍 Mieux comprendre ce que fait Home Assistant

- Un dialogue unique, **Ajouter un appareil ou une intégration**, qui commence par ce qui a été découvert et permet de parcourir par catégorie ou par marque.
- Le **démarrage en direct** : combien d’intégrations sont prêtes, lesquelles se configurent et depuis combien de temps, lesquelles ont échoué.
- Un élément **Santé** dans le menu de chaque intégration : entités disponibles, réparations ouvertes, erreurs récentes, temps de configuration.
- Une carte **Base de données** dans Paramètres › Système › Stockage, qui montre quelles tables et quelles entités prennent de la place. La page Stockage est maintenant disponible sur tous les types d’installation, y compris Container.
- L’assistant IA peut aider à **configurer et ranger** la maison : ajouter des intégrations, organiser les pièces, lire les automatisations, l’énergie et l’historique. Ces outils sont réservés aux administrateurs, et le serveur MCP peut n’exposer que des outils en lecture seule.

### 🧩 Intégrations

Les notes de la bêta annoncent **16 nouvelles intégrations**, dont Electrolux (développée par Electrolux, pour AEG et Frigidaire aussi), E3/DC, Powersensor, Intesis Modbus, Tile BLE (traceurs Tile en local), Trimlight, plusieurs intégrations **infrarouges** (BenQ, Croma, Daikin, Fujitsu, NAD, Sony) et la Liste de minuteurs.

Parmi les améliorations, deux nous concernent directement. La **Freebox** peut désormais **piloter les volets roulants** appairés à une Freebox Delta ou Freebox Home, et affiche le trafic de ses ports LAN. **Overkiz** pilote les fours et gère les sèche-serviettes Atlantic à niveaux de chauffe.

Deux intégrations sont retirées : **Crownstone**, dont le service cloud a fermé, et **Fitbit**, car Google a arrêté l’API Web Fitbit le 2 novembre 2026. Il faut passer à Google Health.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (26 novembre, 9 h 54, 39 changements).** L’intégration **Bambu Lab**, pourtant annoncée dans les notes de la bêta, est **retirée** (*revert*) [#194580](https://github.com/home-assistant/core/pull/194580). MQTT peut charger ses **certificats depuis des fichiers** et signale par une réparation les problèmes d’expiration du certificat client [#190476](https://github.com/home-assistant/core/pull/190476) [#194585](https://github.com/home-assistant/core/pull/194585). La **rétention des sauvegardes** ne s’applique plus qu’aux emplacements activés [#192788](https://github.com/home-assistant/core/pull/192788). La croissance du cache des conditions de script après le rendu des templates est corrigée [#182183](https://github.com/home-assistant/core/pull/182183), tout comme le redémarrage du thermostat générique après son délai maximal [#187264](https://github.com/home-assistant/core/pull/187264). Les stores Velux reçoivent leurs positions d’inclinaison [#194419](https://github.com/home-assistant/core/pull/194419), et KNX vérifie le trousseau de clés importé lors d’une reconfiguration [#194201](https://github.com/home-assistant/core/pull/194201).

**b2 (26 novembre, 18 h 25, 18 changements).** Les volets MQTT gagnent les **angles et positions d’inclinaison** [#194600](https://github.com/home-assistant/core/pull/194600). **Météo-France** atteint le niveau **or** de l’échelle de qualité [#194410](https://github.com/home-assistant/core/pull/194410). Overkiz ne se recharge plus quand une passerelle redémarrée réannonce ses appareils [#193278](https://github.com/home-assistant/core/pull/193278), et abandonne la découverte Zeroconf sans code PIN de passerelle [#194723](https://github.com/home-assistant/core/pull/194723). Une automatisation YAML avec une clé nulle ne bloque plus le chargement [#194740](https://github.com/home-assistant/core/pull/194740). Toutes les pages de la liste des agendas Google sont chargées [#194791](https://github.com/home-assistant/core/pull/194791), et les échecs de mise à jour du firmware SMLIGHT sont signalés [#193741](https://github.com/home-assistant/core/pull/193741).

## ⚠️ Changements cassants annoncés

La liste est longue (plus de trente entrées). Voici celles qui méritent le plus d’attention :

- **Météo-France** : l’état du capteur d’alerte était toujours en français (Vert, Jaune, Orange, Rouge). Il devient **green, yellow, orange ou red**, et s’affiche dans votre langue dans l’interface. **Mettez à jour vos automatisations, scripts et templates** qui testent cet état.
- **Matter** : les prises multiples nommées par l’appareil deviennent des **appareils enfants**. Les identifiants d’entité ne changent pas, mais le `friendly_name` oui. Les volets Matter de type volet roulant prennent la classe *shutter*.
- **Zigbee (ZHA)** : même logique d’appareils enfants pour les interrupteurs multi-canaux, les multiprises et les doubles variateurs. Les identifiants restent les mêmes, mais les noms affichés changent.
- **Z-Wave** : plusieurs modules de volets prennent la classe de ce qu’ils pilotent (volet, store, portail…) au lieu de *window*. Il faut aussi au minimum **zwave-js-server 3.12.0**, soit l’app Z-Wave JS en version 1.11.0 ou plus.
- **Supervisor** : la commande WebSocket `supervisor/api` est réservée aux administrateurs. L’app communautaire Home Assistant Matter Hub doit être en **version 2.1.0** ou plus.
- **Recorder et SQL** : un `%` suivi de deux chiffres hexadécimaux dans le nom de la base de données ou le chemin SQLite est désormais décodé. Écrivez `%25` pour garder un `%`.
- **AccuWeather** (attributs en minuscules), **AprilAire** (migration d’adresse MAC impossible à annuler), **SmartThings** (plus de connexion par Home Assistant Cloud pour les nouvelles installations), **System Bridge** (actions réservées aux administrateurs), **Tuya** (unités vides supprimées, ce qui peut interrompre des statistiques).

## 👩‍💻 Côté développeurs

Les notes de la bêta signalent 12 billets du blog des contributeurs, notamment :
- [Les apps perdent quatre capacités Linux par défaut](https://contributors.home-assistant.io/blog/2026/11/06/apps-fewer-default-capabilities/)
- [Les volets peuvent décrire leur position d’inclinaison](https://contributors.home-assistant.io/blog/2026/11/25/cover-tilt-position/)
- [Les cartes de dashboard peuvent être livrées en ZIP](https://contributors.home-assistant.io/blog/2026/11/24/dashboard-cards-zip-files/)
- [Laisser une partie du README hors du Marketplace](https://contributors.home-assistant.io/blog/2026/11/25/leave-readme-sections-out-of-the-marketplace/)
- [Types d’événements standard des boutons revus](https://contributors.home-assistant.io/blog/2026/11/09/button-event-types-revised/)
- [L’accès de type dictionnaire aux informations d’appareil est déprécié](https://contributors.home-assistant.io/blog/2026/11/19/device-info-mapping/)
- [Le plugin multicast est en cours de dépréciation](https://contributors.home-assistant.io/blog/2026/11/17/multicast-plugin-deprecation/)
- [Mises à jour des composants du frontend pour la 2026.12](https://contributors.home-assistant.io/blog/2026/11/25/frontend-component-updates-2026.12/)

Pour les intégrations personnalisées, un formulaire qui renvoie un type de résultat sous forme de texte simple (`"form"`, `"abort"`) au lieu de l’énumération `FlowResultType` **échoue désormais** avec une erreur `TypeError`.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Sur le papier, cette bêta est faite pour moi : des volets mieux pensés, des **volets Freebox** enfin pilotables, et des boutons qui gèrent le double appui et l’appui long. Je garde un œil sur le changement de l’alerte Météo-France, qui peut casser des automatisations si on ne l’anticipe pas. Je compléterai cet article au fil des prochaines bêtas.
</div>

Vous êtes sur la bêta 2026.12 ? Partagez vos retours sur le forum, en indiquant le numéro de bêta.

<p class="ha-signature">— XAV59213</p>
