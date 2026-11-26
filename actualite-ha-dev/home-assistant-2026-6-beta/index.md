---
layout: ha-dev
title: 'Bêta Home Assistant 2026.6 : 82 correctifs d’un coup, MQTT 5 et des zones qui deviennent des déclencheurs'
short_title: 'Bêta 2026.6 : MQTT 5 et déclencheurs de zone'
description: 'La bêta de Home Assistant 2026.6 (27 mai – 3 juin 2026) en français : sélecteur de cartes, conditions testées en direct, MQTT 5, déclencheurs de zone.'
excerpt_fr: La bêta 2026.6 teste le nouveau sélecteur de cartes et les conditions vérifiées en direct. La b1 apporte 82 correctifs, dont la migration silencieuse vers MQTT 5, puis les déclencheurs et conditions de zone arrivent juste avant la sortie.
image: /actualite-ha-dev/home-assistant-2026-6-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.6, juin 2026'
date: 2026-05-27
section: actualite-ha-dev
cycle: 2026-6
version: '2026.6'
month: Juin 2026
release_url: https://www.home-assistant.io/blog/2026/06/03/release-20266/
official_title: '2026.6: Pick a card, any card'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.6/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.6'
seo:
  type: NewsArticle
---
La **2026.6.0b0** a été publiée le **27 mai 2026**, puis la **b1** le **1er juin** avec **82 changements**, le plus gros lot d’une seule bêta du premier semestre. La version finale est sortie le **3 juin**. Ce cycle compte surtout pour ceux qui utilisent **MQTT** et les **zones**.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : sélecteur de cartes « par entité » avec aperçus en direct, réception infrarouge, conditions testées en direct et notes sur chaque étape, météo et télécommande sur les tuiles, utilisateurs et codes des serrures Z-Wave.
- 🔁 **Pendant la bêta** : passage automatique à MQTT 5 si le broker le permet (b1), délai maximal de nouvelle tentative porté à 10 minutes (b1), messages Bluetooth « pourquoi l’appareil est introuvable » (b2), déclencheurs et conditions de zone (b3).
- ⚠️ **À vérifier** : Bluetooth, Certificate Expiry, ESPHome, HDMI-CEC, IronOS, ONVIF, Shelly, SmartThings, entités template, Tuya et Velux.
</div>

## 🧪 Ce qui était en test

- Le sélecteur de cartes **« par entité »**, avec aperçus en direct.
- L’infrarouge qui sait aussi **recevoir** (la télécommande d’origine).
- Les conditions **testées en direct**, le nombre d’entités ciblées et des **notes** sur chaque étape.
- Les prévisions météo et une télécommande complète sur les **tuiles**.
- La gestion des **utilisateurs et codes** des serrures Z-Wave.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (1er juin, 82 changements).**
- **MQTT** : le choix du protocole passe dans les options principales [#172482](https://github.com/home-assistant/core/pull/172482). Home Assistant **migre sans rien dire vers MQTT 5** si le broker le prend en charge, et crée sinon une réparation [#172500](https://github.com/home-assistant/core/pull/172500). Le message de la réparation sur l’ancien protocole est clarifié [#172404](https://github.com/home-assistant/core/pull/172404).
- **Sécurité des sauvegardes** : les envois de sauvegarde dont le nom interne n’est pas sûr sont rejetés [#172368](https://github.com/home-assistant/core/pull/172368).
- **Démarrage** : quand une intégration n’est pas prête, le délai maximal entre deux tentatives passe de 80 secondes à **10 minutes** [#172487](https://github.com/home-assistant/core/pull/172487). Le proxy BLE de Matter ne bloque plus le démarrage [#172456](https://github.com/home-assistant/core/pull/172456).
- **Intégrations** : un plantage de Hue est corrigé (division par zéro) [#172442](https://github.com/home-assistant/core/pull/172442), Volvo ne plante plus sur ses serrures [#172465](https://github.com/home-assistant/core/pull/172465), et Tado [#172486](https://github.com/home-assistant/core/pull/172486) et OctoPrint [#172495](https://github.com/home-assistant/core/pull/172495) sont réparés. Le Supervisor est mis à jour dès la configuration initiale [#171129](https://github.com/home-assistant/core/pull/171129).

**b2 (1er juin au soir).** Une série d’intégrations Bluetooth **expliquent pourquoi un appareil est introuvable** : Airthings BLE, Yale Access Bluetooth, INKBIRD, LED BLE, eQ-3, LD2410, Snooz… [#172758](https://github.com/home-assistant/core/pull/172758) [#172770](https://github.com/home-assistant/core/pull/172770). Le proxy BLE de Matter filtre les annonces rejouées et périmées [#172773](https://github.com/home-assistant/core/pull/172773).

**b3 et b4 (3 juin).** Les **zones deviennent des déclencheurs** : entrée et sortie de zone [#172412](https://github.com/home-assistant/core/pull/172412), présence détectée ou disparue [#172438](https://github.com/home-assistant/core/pull/172438). Les conditions « dans la zone / hors de la zone » [#172810](https://github.com/home-assistant/core/pull/172810) et d’occupation [#172896](https://github.com/home-assistant/core/pull/172896) suivent. L’action *choose* accepte une note facultative sur chaque option [#172837](https://github.com/home-assistant/core/pull/172837). Les options renommées du comportement des déclencheurs restent compatibles avec l’ancien nom [#172822](https://github.com/home-assistant/core/pull/172822). Enfin, le test d’une condition depuis l’interface n’écrit plus d’erreur dans les journaux [#172897](https://github.com/home-assistant/core/pull/172897).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour **Bluetooth, Certificate Expiry, ESPHome, HDMI-CEC, IronOS, ONVIF, Shelly, SmartThings, les entités template, Tuya et Velux**.

## 👩‍💻 Côté développeurs

- [BrowseMediaSource : le domaine devient obligatoire](https://contributors.home-assistant.io/blog/2026/05/20/browse-media-source-root-class/)
- [Changements des API de conditions et de scripts](https://contributors.home-assistant.io/blog/2026/05/13/condition-script-api-changes/)
- [Suggestions de cartes personnalisées dans le sélecteur](https://contributors.home-assistant.io/blog/2026/05/27/custom-card-suggestions/)
- [Dépréciation de l’écouteur d’entrée de configuration combiné aux méthodes de rechargement](https://contributors.home-assistant.io/blog/2026/05/07/config-entry-listener-together-with-reloading-methods/)
- [Dépréciation du mode avancé dans les formulaires de configuration](https://contributors.home-assistant.io/blog/2026/05/26/advanced-mode-config-flow-deprecation/)
- [Formater les noms d’entités dans les cartes personnalisées](https://contributors.home-assistant.io/blog/2026/05/11/format-entity-name-helper/)
- [Mises à jour des composants du frontend pour la 2026.6](https://contributors.home-assistant.io/blog/2026/05/27/frontend-component-updates-2026.6/)
- [Changements de l’API de publication MQTT](https://contributors.home-assistant.io/blog/2026/05/11/mqtt-publish-api-changes/) et [durée d’expiration des messages](https://contributors.home-assistant.io/blog/2026/05/11/mqtt-publish-api-message-expiry-interval/)

## 🧭 Pour le canal bêta

Si votre broker MQTT est récent, la b1 vous fait passer à MQTT 5 sans rien vous demander. Après la mise à jour, jetez un œil aux **réparations** : c’est là qu’apparaît un éventuel souci de protocole. Les déclencheurs de zone, eux, sont arrivés le jour de la sortie : ils n’ont été testés que quelques heures en bêta.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

J’aime beaucoup les messages Bluetooth « pourquoi l’appareil est introuvable ». C’est exactement le genre de détail qui évite des heures de recherche. Et les déclencheurs de zone étaient très attendus pour les automatisations de présence.
</div>

Vous êtes passé à MQTT 5 ? Partagez votre configuration de broker sur le forum.

<p class="ha-signature">— XAV59213</p>
