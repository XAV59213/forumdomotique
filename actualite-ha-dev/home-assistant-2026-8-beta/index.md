---
layout: ha-dev
title: 'Bêta Home Assistant 2026.8 : adieu le « :8123 », et le registre des appareils réparé en pleine bêta'
short_title: 'Bêta 2026.8 : plus de :8123, registre réparé'
description: 'La bêta de Home Assistant 2026.8 (29 juillet – 5 août 2026) en français : port 80 sur HAOS, Tools pour tous, migration HTTP corrigée, registre des appareils.'
excerpt_fr: La bêta 2026.8 teste les installations sans « :8123 » et les réglages du serveur web dans l’interface. La b2 protège la migration de la configuration HTTP en YAML. Les b4 et b5 corrigent ensuite des dizaines d’intégrations touchées par le nouveau registre des appareils.
image: /actualite-ha-dev/home-assistant-2026-8-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.8, août 2026'
date: 2026-07-29
section: actualite-ha-dev
cycle: 2026-8
version: '2026.8'
month: Août 2026
release_url: https://www.home-assistant.io/blog/2026/08/05/release-20268/
official_title: '2026.8: Approachable by design'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.8/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.8'
seo:
  type: NewsArticle
---
Avec **228 changements** répartis sur six bêtas, du **29 juillet** au **5 août 2026**, la 2026.8 est l’un des cycles bêta les plus chargés de l’année. Deux sujets le dominent : la **configuration du serveur web** qui passe dans l’interface (et la fin du « :8123 » pour les nouvelles installations Home Assistant OS), et une vaste réparation du **registre des appareils**.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : plus de numéro de port pour les nouvelles installations Home Assistant OS, port, interface et proxys de confiance réglables dans l’interface, Developer Tools renommé **Tools**, page Cloud repensée, identifiants d’entité renommables.
- 🔁 **Pendant la bêta** : la migration de la configuration HTTP en YAML est sécurisée (b1-b2), et plus d’une centaine de changements portent sur le rattachement des appareils (*via_device*, b3 à b6). Les automatisations des boutons Hue fonctionnent de nouveau après un redémarrage (b5).
- ⚠️ **À vérifier** : AirNow, Gardena Bluetooth, Edifier Infrared, Ohme, Paperless-ngx, robots aspirateurs, ScreenLogic, UniFi Protect et Volvo On Call.
</div>

## 🧪 Ce qui était en test

- Les nouvelles installations Home Assistant OS **sans numéro de port** à ajouter à l’adresse.
- Le port, l’interface d’écoute et les proxys de confiance réglables **depuis l’interface**.
- **Developer Tools** devient simplement **Tools**, et les modes « avancé » et « expert » disparaissent.
- La page **Home Assistant Cloud** repensée, avec une configuration guidée.
- Des **identifiants d’entité** que l’on peut renommer et ordonner à sa façon.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 et b2 (30 juillet) : la migration HTTP.** Pour ceux qui ont une section `http:` en YAML, c’est le point clé du cycle. La réparation de migration indique la bonne version de Home Assistant [#177566](https://github.com/home-assistant/core/pull/177566). Aucune configuration HTTP n’est préparée s’il n’y a pas de YAML à migrer [#177622](https://github.com/home-assistant/core/pull/177622). Surtout, **le nouveau port par défaut (80) n’est pas utilisé pendant la migration** [#177638](https://github.com/home-assistant/core/pull/177638), et la configuration HTTP ne peut pas être modifiée tant que Home Assistant n’a pas fini de démarrer [#177640](https://github.com/home-assistant/core/pull/177640). La b1 arrête aussi de rattacher à un appareil les entités YAML de plusieurs helpers : statistiques d’historique, dérivée, intégrale, statistiques, seuil, tendance, indicateur de moisissure, hygrostat et thermostat génériques, compteur de consommation [#177594](https://github.com/home-assistant/core/pull/177594) [#177603](https://github.com/home-assistant/core/pull/177603). UniFi Protect exige désormais la version 7.1 [#177620](https://github.com/home-assistant/core/pull/177620).

**b3 à b6 (31 juillet – 5 août) : le registre des appareils.** Le blog des contributeurs a annoncé que chaque appareil serait limité à **une seule entrée de configuration**. En parallèle, les bêtas apportent plus d’une centaine de changements sur le rattachement des appareils. Près de 60 intégrations corrigent un problème d’ordre de création qui pouvait mal rattacher un appareil à son appareil parent (*via_device race*) : Hue, Matter, Reolink, Synology DSM, Overkiz, Tessie, TP-Link… La **Freebox** en fait partie [#177716](https://github.com/home-assistant/core/pull/177716). D’autres, comme Shelly, Z-Wave JS ou ZHA, sont adaptées au nouveau champ `via_device_id` [#177759](https://github.com/home-assistant/core/pull/177759) [#177861](https://github.com/home-assistant/core/pull/177861) [#178168](https://github.com/home-assistant/core/pull/178168). La b5 compte à elle seule **100 changements**.

**Autres correctifs notables.** Les capteurs de mouvement Hue MotionAware signalent de nouveau le mouvement [#177643](https://github.com/home-assistant/core/pull/177643), et les automatisations des boutons Hue fonctionnent après un redémarrage [#177427](https://github.com/home-assistant/core/pull/177427). L’adoption depuis le dashboard ESPHome ne coupe plus l’accès de Home Assistant aux appareils provisionnés [#178039](https://github.com/home-assistant/core/pull/178039). Une ancienne clé de chiffrement ne masque plus la bonne dans le formulaire ESPHome [#178047](https://github.com/home-assistant/core/pull/178047). Enfin, la recréation d’un conteneur Portainer est réservée aux administrateurs [#177301](https://github.com/home-assistant/core/pull/177301).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour **AirNow, Gardena Bluetooth, Edifier Infrared, Ohme, Paperless-ngx, les robots aspirateurs, ScreenLogic, UniFi Protect et Volvo On Call**.

## 👩‍💻 Côté développeurs

- [Un appareil est limité à une seule entrée de configuration et au plus une sous-entrée](https://contributors.home-assistant.io/blog/2026/07/21/device-registry-single-config-entry/)
- [La politique IA de l’Open Home Foundation](https://contributors.home-assistant.io/blog/2026/07/20/ai-policy/)
- [Les sources multimédia deviennent consultables par recherche](https://contributors.home-assistant.io/blog/2026/07/03/media-source-search/)
- [La modernisation de Modbus](https://contributors.home-assistant.io/blog/2026/07/05/modernizing-modbus/)
- [Types d’événements standard pour les boutons](https://contributors.home-assistant.io/blog/2026/07/22/button-standard-event-types/)

## 🧭 Pour le canal bêta

Si vous accédez à Home Assistant par un proxy inverse, ou si vous avez une section `http:` dans `configuration.yaml`, **ne restez pas sur la b0 ou la b1** de ce cycle. Les protections de la migration sont arrivées en b2. Et si vous développez une intégration, la liste des correctifs *via_device* vous montre comment adapter votre code.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Ce cycle montre tout le travail invisible derrière une version. On parle du « :8123 » qui disparaît, mais plus d’une centaine de changements ont été faits en une semaine pour le nouveau registre des appareils. J’ai vérifié pour la Freebox : elle fait partie du lot.
</div>

Vous avez changé de port pendant cette bêta ? Dites-moi comment ça s’est passé sur le forum.

<p class="ha-signature">— XAV59213</p>
