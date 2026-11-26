---
layout: ha-dev
title: 'Bêta Home Assistant 2026.2 : Overview, Apps et recherche rapide, avec un retour en arrière une heure avant la sortie'
short_title: 'Bêta 2026.2 : Overview, Apps et recherche rapide'
description: 'La bêta de Home Assistant 2026.2 (28 janvier – 4 février 2026) en français : Overview, Apps, recherche rapide, correctifs des six bêtas et changements cassants.'
excerpt_fr: La bêta 2026.2 teste le dashboard Overview, les add-ons renommés Apps et la recherche rapide. Pendant la bêta, les dashboards YAML sont corrigés, et une mise à jour des intents est annulée une heure avant la sortie.
image: /actualite-ha-dev/home-assistant-2026-2-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.2, février 2026'
date: 2026-01-28
section: actualite-ha-dev
cycle: 2026-2
version: '2026.2'
month: Février 2026
release_url: https://www.home-assistant.io/blog/2026/02/04/release-20262/
official_title: '2026.2: Home, sweet overview'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.2/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.2'
seo:
  type: NewsArticle
---
La bêta **2026.2.0b0** a été publiée le **28 janvier 2026** au soir. Le **4 février**, elle était devenue la version stable, après six bêtas, dont **trois le dernier jour**. Elle teste un gros changement visible : le dashboard Home devient **Overview**, et les **add-ons deviennent des Apps**.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : Overview par défaut, base de données d’appareils (Labs, en opt-in), add-ons renommés Apps, recherche rapide (Ctrl+K / ⌘+K), carte Distribution.
- 🔁 **Pendant la bêta** : migration des dashboards YAML corrigée (b1), entités d’options Home Connect restaurées (b2), Anthropic passe par défaut à Haiku 4.5 (b3), mise à jour des intents annulée dans la b5.
- ⚠️ **À vérifier** : Group, Sentry, Tractive, Tuya et VeSync.
</div>

## 🧪 Ce qui était en test

- Le dashboard Home devient **Overview**, la vue par défaut des nouvelles installations.
- Une **base de données d’appareils** à partager de façon anonyme et volontaire, à activer dans Labs.
- Les **add-ons** prennent le nom d’**Apps**.
- La **recherche rapide** (Ctrl+K ou ⌘+K) pour naviguer, lancer une commande ou trouver une entité.
- Une nouvelle **carte Distribution** et les premières **conditions par usage** dans Labs.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (30 janvier).** C’est le correctif clé pour ceux qui gèrent leurs dashboards en YAML : le chemin *lovelace* est de nouveau accepté et la **migration des dashboards YAML** est réparée [#161816](https://github.com/home-assistant/core/pull/161816). La validation des actions d’*intent_script* est corrigée [#158266](https://github.com/home-assistant/core/pull/158266), tout comme les unités ambiguës de la puissance et de l’énergie réactives [#161810](https://github.com/home-assistant/core/pull/161810) et la correspondance entre états et actions HVAC de Control4 [#161916](https://github.com/home-assistant/core/pull/161916).

**b2 (2 février).** Les **entités d’options de programme Home Connect** reviennent [#156401](https://github.com/home-assistant/core/pull/156401). Les capteurs de date passent à « inconnu » quand la lecture échoue, au lieu de planter [#161952](https://github.com/home-assistant/core/pull/161952). Le *parse_mode* des actions Telegram est corrigé [#162006](https://github.com/home-assistant/core/pull/162006), et un texte « en savoir plus » est ajouté pour Analytics dans Labs [#162094](https://github.com/home-assistant/core/pull/162094).

**b3 (3 février).** Anthropic passe par défaut au modèle **Haiku 4.5** [#162093](https://github.com/home-assistant/core/pull/162093). Des capteurs de notification invalides sont retirés d’Alexa Devices [#160422](https://github.com/home-assistant/core/pull/160422), et le texte d’Analytics dans Labs est retouché [#162151](https://github.com/home-assistant/core/pull/162151).

**b4 (4 février).** Jellyfin gagne les commandes du client natif [#161982](https://github.com/home-assistant/core/pull/161982), et Anthropic signale les modèles obsolètes par une réparation [#162162](https://github.com/home-assistant/core/pull/162162). La bibliothèque auth0-python est bloquée sous la version 5.0 [#162203](https://github.com/home-assistant/core/pull/162203).

**b5 (4 février, moins d’une heure avant la stable).** La mise à jour des **intents** (les phrases comprises par Assist) est **annulée** [#162226](https://github.com/home-assistant/core/pull/162226). Fressnapf Tracker filtre les traceurs invalides [#161670](https://github.com/home-assistant/core/pull/161670), et evohome met de nouveau à jour ses consignes programmées [#162043](https://github.com/home-assistant/core/pull/162043).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour **Group, Sentry, Tractive, Tuya et VeSync**.

## 👩‍💻 Côté développeurs

Les notes de la version renvoient vers deux billets du blog des contributeurs :
- [prek remplace pre-commit](https://contributors.home-assistant.io/blog/2026/01/13/replace-pre-commit-with-prek/) pour les vérifications avant commit ;
- [pyserial-asyncio ne bloque plus la boucle d’événements](https://contributors.home-assistant.io/blog/2026/01/05/pyserial-asyncio-fast/).

## 🧭 Pour le canal bêta

L’annulation des intents dans la b5 montre bien le rôle de la bêta : une modification peut disparaître au tout dernier moment. Si vous testez Assist en français, vérifiez vos phrases habituelles après chaque bêta.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Pour moi, le point clé de ce cycle est la correction de la migration des dashboards YAML dès la b1. Si vous gérez vos dashboards en YAML, ne faites pas l’impasse sur cette bêta-là.
</div>

Vous avez testé Overview pendant la bêta ? Dites-moi sur le forum ce que vous en pensez.

<p class="ha-signature">— XAV59213</p>
