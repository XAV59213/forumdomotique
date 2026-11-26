---
layout: ha-dev
title: 'Bêta Home Assistant 2026.11 : le Marketplace prend forme pendant la bêta, et les intégrations déclarent leur connectivité'
short_title: 'Bêta 2026.11 : HACS devient le Marketplace'
description: 'La bêta de Home Assistant 2026.11 (28 octobre – 4 novembre 2026) en français : Marketplace (ex-HACS), exclusions de cibles, noms d’entités, correctifs des sept bêtas.'
excerpt_fr: 'La bêta de la plus grosse version de l’histoire : HACS devient le Marketplace, les cibles acceptent des exclusions et les noms d’entités sont repensés. Pendant la bêta, le Marketplace gagne son titre et un serveur miroir pour les utilisateurs en Chine, et les intégrations déclarent leur connectivité.'
image: /actualite-ha-dev/home-assistant-2026-11-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.11, novembre 2026'
date: 2026-10-28
section: actualite-ha-dev
cycle: 2026-11
version: '2026.11'
month: Novembre 2026
release_url: https://www.home-assistant.io/blog/2026/11/04/release-202611/
official_title: '2026.11: A lot in store!'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.11/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.11'
seo:
  type: NewsArticle
---
La **2026.11.0b0** a été publiée le **28 octobre 2026**, et la version stable, « la plus grosse jamais publiée » selon ses notes, le **4 novembre**, après six bêtas correctives. Pour ceux qui publient des intégrations communautaires, comme moi, c’est **le** cycle à suivre : HACS entre dans Home Assistant sous le nom de **Marketplace**.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : le Marketplace (ex-HACS), des exclusions dans les cibles, des sections de dashboard automatiques, des noms d’entités repensés (« nommer une fois »), les outils « Pourquoi est-ce arrivé ? », les caméras Matter 1.5, LoRaWAN, Zigbee Green Power et les disques locaux pour les sauvegardes.
- 🔁 **Pendant la bêta** : le champ des outils IA devient une liste de cases à cocher (b1), les identifiants tronqués ne finissent plus par « _ » (b2), une métadonnée de connectivité est ajoutée aux intégrations (b3), le Marketplace reçoit un titre, une icône et un serveur miroir pour les utilisateurs en Chine (b3-b5).
- ⚠️ **À vérifier** : plus de quarante entrées, dont les noms d’entités, Matter, MQTT, Z-Wave, ZHA, Philips Hue, Tuya et l’authentification.
</div>

## 🧪 Ce qui était en test

- **HACS devient le Marketplace**, intégré à Home Assistant (Paramètres › Marketplace).
- **Exclure** une entité, un appareil, une pièce, un étage ou une étiquette d’une cible.
- Des **sections automatiques** et le copier-coller de sections dans les dashboards.
- **Nommer une fois** : Home Assistant ajoute le contexte (appareil, pièce) là où c’est utile.
- Les outils « **Pourquoi est-ce arrivé ?** », les caméras **Matter 1.5**, **LoRaWAN**, **Zigbee Green Power** et les disques locaux pour les sauvegardes.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (29 octobre).** Le choix des **outils IA** s’affiche sous forme de cases à cocher [#189320](https://github.com/home-assistant/core/pull/189320). L’historique des journaux d’une intégration est lu depuis le journal du Supervisor [#189404](https://github.com/home-assistant/core/pull/189404). srptools est bloqué sous la version 2 pour réparer Apple TV [#189349](https://github.com/home-assistant/core/pull/189349). La Marzocco demande d’accepter sa politique de confidentialité [#189414](https://github.com/home-assistant/core/pull/189414), et le serveur MCP utilise l’origine de la requête pour ses icônes [#189460](https://github.com/home-assistant/core/pull/189460).

**b2 (31 octobre).** Le nouveau nommage est retouché : un **identifiant d’entité tronqué ne se termine plus par un tiret bas** [#189403](https://github.com/home-assistant/core/pull/189403). Les clés ZBT-2 et ZBT-1 apparaissent quand elles passent par un proxy série ESPHome [#189450](https://github.com/home-assistant/core/pull/189450). Les domaines personnalisés du cloud sont préférés pour construire l’URL [#189471](https://github.com/home-assistant/core/pull/189471), et les connexions Modbus partagées sont fermées à l’arrêt [#189514](https://github.com/home-assistant/core/pull/189514).

**b3 (2 novembre, 54 changements).** Le **panneau Marketplace** reçoit un titre et une icône [#189511](https://github.com/home-assistant/core/pull/189511). Surtout, une série ajoute aux intégrations une **métadonnée de connectivité**, protocole par protocole : Bluetooth, cloud, Zigbee, Z-Wave, Matter, MQTT, KNX, LoRaWAN, infrarouge, radiofréquence, réseau local… [#189894](https://github.com/home-assistant/core/pull/189894) [#189916](https://github.com/home-assistant/core/pull/189916). Les vitesses « silencieuse » et « par défaut » des volets Velux sont dépréciées [#189438](https://github.com/home-assistant/core/pull/189438), et Flic Button reçoit plusieurs correctifs d’appairage [#190005](https://github.com/home-assistant/core/pull/190005).

**b4 (3 novembre).** Les délais d’attente de la **Freebox** sont signalés comme « connexion impossible » [#190079](https://github.com/home-assistant/core/pull/190079). Une durée de dérogation evohome qui chevauche le changement d’heure est corrigée [#190109](https://github.com/home-assistant/core/pull/190109).

**b5 et b6 (4 novembre).** Une commande WebSocket **explique les exclusions d’une cible** [#190119](https://github.com/home-assistant/core/pull/190119). Le **Marketplace** gagne un **serveur miroir pour les utilisateurs en Chine** [#190251](https://github.com/home-assistant/core/pull/190251). Les commandes différées s’exécutent sous l’identité de l’utilisateur qui a lancé le minuteur [#190287](https://github.com/home-assistant/core/pull/190287). Tedee bénéficie d’un délai de grâce avant de redemander l’authentification [#190338](https://github.com/home-assistant/core/pull/190338), et l’ancienne intégration Flic est marquée « legacy » [#190364](https://github.com/home-assistant/core/pull/190364).

## ⚠️ Changements cassants annoncés

La liste des notes finales est la plus longue de l’année, avec **plus de quarante entrées**. On y trouve notamment les **noms d’entités**, l’**authentification**, **Matter**, **MQTT**, **Philips Hue**, **Tuya**, **Z-Wave**, **ZHA**, **UniFi Protect** et les **dépendances Python**. Le changement de nommage peut modifier des noms affichés sur vos dashboards.

## 👩‍💻 Côté développeurs

Les notes de la version renvoient vers une vingtaine de billets du blog des contributeurs, parmi lesquels les suivants. On peut y ajouter [les cibles peuvent exclure des entités](https://contributors.home-assistant.io/blog/2026/10/21/target-exclude/), publié pendant le cycle.
- [Les appareils enfants (*child devices*)](https://contributors.home-assistant.io/blog/2026/10/22/child-devices/)
- [DeviceInfo devient une dataclass](https://contributors.home-assistant.io/blog/2026/10/13/device-info-class/)
- [Les intégrations ont désormais des catégories](https://contributors.home-assistant.io/blog/2026/10/20/integration-categories/)
- [Une console Python dans Home Assistant](https://contributors.home-assistant.io/blog/2026/10/17/debug-console/)
- [L’audio bidirectionnel pour les caméras](https://contributors.home-assistant.io/blog/2026/10/24/camera-two-way-audio/)
- [Toujours fournir un step_id aux résultats de formulaire](https://contributors.home-assistant.io/blog/2026/10/23/flow-results-require-step-id/)
- [Un nouveau site pour tous les contributeurs](https://contributors.home-assistant.io/blog/2026/10/16/a-new-home-for-every-contributor/) : le blog des développeurs devient celui des contributeurs.

## 🧭 Pour le canal bêta

Si vous publiez une intégration sur HACS, testez votre dépôt dans le **Marketplace de la bêta** avant la sortie, et lisez le billet sur les [catégories d’intégrations](https://contributors.home-assistant.io/blog/2026/10/20/integration-categories/). Côté utilisateur, comparez vos dashboards avant et après : le nouveau nommage peut modifier des noms affichés.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

C’est le cycle bêta que j’attendais le plus en tant que développeur d’intégrations. Voir le Marketplace se peaufiner d’une bêta à l’autre, avec son titre, son icône et même un serveur miroir pour les utilisateurs en Chine, montre que l’équipe l’a vraiment pensé pour tout le monde.
</div>

Vos intégrations HACS s’affichent bien dans le Marketplace ? Comparons nos retours sur le forum.

<p class="ha-signature">— XAV59213</p>
