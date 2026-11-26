---
layout: ha-dev
title: 'Bêta Home Assistant 2026.9 : dix bêtas pour Modbus, la reconnaissance vocale Soniox et la carte du réseau Matter'
short_title: 'Bêta 2026.9 : Modbus, Soniox et Matter'
description: 'La bêta de Home Assistant 2026.9 (26 août – 2 septembre 2026) en français : Modbus, Soniox dans Labs, tableau Sécurité, carte Matter et dix bêtas de correctifs.'
excerpt_fr: 'Dix bêtas pour la 2026.9 : Modbus se modernise, la reconnaissance vocale Cloud Soniox arrive dans Labs, et le réseau Matter a sa carte. Pendant la bêta, les services de serrure Z-Wave sont réservés aux administrateurs et la Freebox gagne une nouvelle tentative de connexion.'
image: /actualite-ha-dev/home-assistant-2026-9-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.9, septembre 2026'
date: 2026-08-26
section: actualite-ha-dev
cycle: 2026-9
version: '2026.9'
month: Septembre 2026
release_url: https://www.home-assistant.io/blog/2026/09/02/release-20269/
official_title: '2026.9: There''s room on this bus'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.9/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.9'
seo:
  type: NewsArticle
---
De la **2026.9.0b0** (26 août 2026) à la **b9** (2 septembre, quatre heures avant la version finale), ce cycle compte **dix bêtas**. Le 2 septembre, trois bêtas sont publiées en un peu plus de deux heures, avant la sortie de la version stable en fin de journée.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : Modbus avec des intégrations qui connaissent déjà l’appareil (Fronius pour commencer), reconnaissance vocale Cloud Soniox dans Labs, tableau Sécurité avec alertes actives et favoris, panneau Sources commun à l’Historique et à l’Activité, carte du réseau Matter, heure dorée et heure bleue.
- 🔁 **Pendant la bêta** : numpy ramené à la version 2.3.2 (b2), services de serrure Z-Wave réservés aux administrateurs (b2), Shelly en sécurité renforcée (b5), images Home Connect annulées (b6), nouvelle intégration de tuiles de carte OpenStreetMap (b6).
- ⚠️ **À vérifier** : KNX, API LLM, Persistent Notification, UniFi Protect, Update, Vacuum et Z-Wave JS.
</div>

## 🧪 Ce qui était en test

- **Modbus** : des intégrations qui connaissent déjà votre appareil, en commençant par Fronius.
- Un nouveau moteur de **reconnaissance vocale Cloud** (Soniox) à tester dans Labs.
- Le tableau **Sécurité** avec ses **alertes actives** et ses **favoris**.
- Un panneau **Sources** commun à l’Historique et à l’Activité, et le détail du « **pourquoi** » sur chaque ligne d’Activité.
- La **carte du réseau Matter**, ainsi que l’heure dorée, l’heure bleue, le soleil de minuit et la nuit polaire.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (27 août).** On peut enregistrer la configuration HTTP sans proxys de confiance [#180357](https://github.com/home-assistant/core/pull/180357). Le transport SSE du serveur MCP ne crée plus de contexte SSL bloquant [#180367](https://github.com/home-assistant/core/pull/180367), et la limite de puissance Fronius est nommée d’après le côté sur lequel elle agit [#180364](https://github.com/home-assistant/core/pull/180364).

**b2 (28 août, 50 changements).** **numpy revient à la version 2.3.2** [#180411](https://github.com/home-assistant/core/pull/180411). Les **services de serrure Z-Wave restants sont réservés aux administrateurs** [#180512](https://github.com/home-assistant/core/pull/180512), et le PIN des serrures Matter peut être un template [#180482](https://github.com/home-assistant/core/pull/180482). Se déconnecter du cloud supprime son entrée de configuration [#180472](https://github.com/home-assistant/core/pull/180472). Modbus respecte les états de vérification des bobines [#180490](https://github.com/home-assistant/core/pull/180490). La **Freebox réessaie de se configurer** quand le routeur est injoignable [#180544](https://github.com/home-assistant/core/pull/180544). Une confirmation est demandée avant de supprimer un point de montage en échec depuis la réparation [#180414](https://github.com/home-assistant/core/pull/180414).

**b3 et b4 (29 août).** KNX valide les données de ses entités créées dans l’interface avant de les configurer [#180067](https://github.com/home-assistant/core/pull/180067). Plex se remet d’un changement de certificat plex.direct [#180446](https://github.com/home-assistant/core/pull/180446). Le serveur MCP demande un jeton de rafraîchissement aux serveurs d’autorisation [#180604](https://github.com/home-assistant/core/pull/180604).

**b5 (31 août).** Les **Shelly en sécurité renforcée** (*enhanced_security*) sont pris en charge en HTTP [#180438](https://github.com/home-assistant/core/pull/180438). Le capteur « fin d’attente » de Sofar, limité à un compte à rebours actif dans la b4 [#180605](https://github.com/home-assistant/core/pull/180605), est finalement **supprimé** [#180899](https://github.com/home-assistant/core/pull/180899).

**b6 (1er septembre).** Une **intégration de tuiles de carte** sert de proxy au fond de carte OpenStreetMap [#180441](https://github.com/home-assistant/core/pull/180441). Les **images de Home Connect sont annulées** [#180933](https://github.com/home-assistant/core/pull/180933). Dans l’image Container, le dossier de configuration sort du `sys.path` [#180967](https://github.com/home-assistant/core/pull/180967). Le titre de la reconnaissance vocale dans Labs est clarifié [#180927](https://github.com/home-assistant/core/pull/180927).

**b7 à b9 (2 septembre).** La reconnaissance vocale lit le flux audio par morceaux pour éviter une erreur *LineTooLong* [#180831](https://github.com/home-assistant/core/pull/180831). Xbox ne supprime plus les appareils hors ligne [#181045](https://github.com/home-assistant/core/pull/181045). La b8 met seulement à jour le frontend [#181072](https://github.com/home-assistant/core/pull/181072), et la b9 ignore les appareils fixes des add-ons quand elle attribue les ports série [#181074](https://github.com/home-assistant/core/pull/181074).

## ⚠️ Changements cassants annoncés

Les notes finales documentent notamment des changements pour **KNX, les API LLM, Persistent Notification, UniFi Protect, Update, Vacuum et Z-Wave JS**.

## 👩‍💻 Côté développeurs

- [L’intégration Configurator est dépréciée](https://contributors.home-assistant.io/blog/2026/08/31/deprecate-configurator/)
- [Changements de l’API WebSocket du registre des appareils](https://contributors.home-assistant.io/blog/2026/08/19/device-registry-websocket-api-changes/)
- [Nouvelles dépréciations, helpers et validations du registre des appareils](https://contributors.home-assistant.io/blog/2026/08/24/device-registry-follow-up-changes/)

## 🧭 Pour le canal bêta

Si vous testez la reconnaissance vocale de Labs, installez au moins la **b7** : elle corrige la lecture du flux audio envoyé à la reconnaissance vocale. Si vous avez des serrures Z-Wave pilotées par un compte non administrateur, vérifiez vos automatisations dès la b2.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Pour un utilisateur Freebox comme moi, la nouvelle tentative de connexion quand le routeur ne répond pas est un petit correctif qui change la vie après une coupure. Et la restriction des serrures Z-Wave aux administrateurs va dans le bon sens.
</div>

Vous testez la reconnaissance vocale Soniox ? Comparez vos résultats sur le forum.

<p class="ha-signature">— XAV59213</p>
