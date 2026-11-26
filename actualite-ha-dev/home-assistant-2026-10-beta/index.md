---
layout: ha-dev
title: 'Bêta Home Assistant 2026.10 : cinq bêtas le jour de la sortie, et une série de correctifs pour la Freebox'
short_title: 'Bêta 2026.10 : nouvelle carte et cinq bêtas en un jour'
description: 'La bêta de Home Assistant 2026.10 (30 septembre – 7 octobre 2026) en français : nouvelle carte, condition Triggered by, MCP en un clic, correctifs Freebox.'
excerpt_fr: La bêta 2026.10 teste la nouvelle carte vectorielle, la condition « Triggered by » et le serveur MCP en un clic. Le 7 octobre, cinq bêtas sortent avant la version finale, dont trois correctifs pour la Freebox.
image: /actualite-ha-dev/home-assistant-2026-10-beta/images/cover.png
cover_alt: 'Couverture : la bêta de Home Assistant 2026.10, octobre 2026'
date: 2026-09-30
section: actualite-ha-dev
cycle: 2026-10
version: '2026.10'
month: Octobre 2026
release_url: https://www.home-assistant.io/blog/2026/10/07/release-202610/
official_title: '2026.10: You are here 📍'
changelog_url: https://www.home-assistant.io/changelogs/core-2026.10/
contributors_url: https://contributors.home-assistant.io/blog/
tags:
- home-assistant
- beta
- canal-dev
- '2026.10'
seo:
  type: NewsArticle
---
La **2026.10.0b0** a été publiée le **30 septembre 2026**. Comme en mai, la b1 s’est fait attendre jusqu’au **5 octobre**, avec 67 changements. La suite a été très rapide : entre minuit et 17 h 30 le **7 octobre**, le jour de la sortie, **cinq bêtas** (b3 à b7) se sont succédé. Pour les utilisateurs Freebox, la b4 est celle qui compte.

<div class="ha-callout info" markdown="1">
**En bref**
- 🧪 **En test** : nouvelle carte vectorielle OpenStreetMap, profil réorganisé, condition « Triggered by » sans identifiants, serveur MCP activable en un clic, panneau Modbus. Home Assistant Cloud annonce son nouveau nom, Link, pour décembre.
- 🔁 **Pendant la bêta** : fuite de connexion au Supervisor corrigée (b1), conditions suivies réévaluées à chaque changement d’état (b3), trois correctifs Freebox (b4), conversion des flux H.265 rétablie (b3).
- ⚠️ **À vérifier** : plus de vingt intégrations ou fonctions, dont l’authentification, MQTT, Synology DSM, Telegram bot, UniFi Network, Proxmox VE et les conditions d’état.
</div>

## 🧪 Ce qui était en test

- Home Assistant **Cloud** sera renommé **Link** (prévu pour la version de décembre).
- Une nouvelle **carte vectorielle** OpenStreetMap, nette à tous les zooms, avec une vue d’ensemble.
- Un **profil** réorganisé : chaque utilisateur peut modifier son nom et sa photo.
- La condition **Triggered by**, sans identifiants à inventer.
- Le **serveur MCP** activable en un clic, et un nouveau panneau **Modbus**.

## 🔁 Ce qui a bougé d’une bêta à l’autre

**b1 (5 octobre, 67 changements).** Quitter la page du journal d’une app ne laisse plus de **connexion ouverte au Supervisor** [#183772](https://github.com/home-assistant/core/pull/183772). Une erreur 500 au lieu d’un 401 est corrigée quand la recherche DNS inverse échoue [#182919](https://github.com/home-assistant/core/pull/182919). Le contrôle *only_supervisor* vérifie le bon utilisateur [#184041](https://github.com/home-assistant/core/pull/184041), et les métadonnées de découverte OAuth sont corrigées pour les clients publics [#184254](https://github.com/home-assistant/core/pull/184254). ESPHome suit le changement d’identifiant de réseau Z-Wave [#183886](https://github.com/home-assistant/core/pull/183886).

**b2 (6 octobre).** Le recorder détecte correctement les préversions de PostgreSQL [#183146](https://github.com/home-assistant/core/pull/183146). Les thermostats en lecture seule sont signalés comme tels à Google Assistant [#183820](https://github.com/home-assistant/core/pull/183820).

**b3 (7 octobre, 0 h 47).** Les **conditions suivies sont réévaluées à chaque changement d’état** [#184335](https://github.com/home-assistant/core/pull/184335). Le calcul de moyenne des statistiques n’est plus quadratique [#184522](https://github.com/home-assistant/core/pull/184522). Les flux et enregistrements **H.265** sont de nouveau encapsulés en *hvc1* [#184537](https://github.com/home-assistant/core/pull/184537). WLED reçoit une série de correctifs (découverte, mises à jour du firmware, capteurs de courant) [#184411](https://github.com/home-assistant/core/pull/184411) [#184415](https://github.com/home-assistant/core/pull/184415).

**b4 (7 octobre, 7 h 53) : la bêta Freebox.** L’identifiant et le mot de passe sont correctement encodés dans l’URL du flux des **caméras Freebox** [#184572](https://github.com/home-assistant/core/pull/184572). La version du firmware des nœuds Freebox Home est transmise comme texte [#184577](https://github.com/home-assistant/core/pull/184577), et les **erreurs de la mise à jour périodique** sont gérées [#184578](https://github.com/home-assistant/core/pull/184578). La même bêta sépare les messages diffusés en continu de l’assistant dans l’entrée de la synthèse vocale [#184535](https://github.com/home-assistant/core/pull/184535). Les entrées OAuth du serveur MCP n’ont plus d’identifiant unique [#184594](https://github.com/home-assistant/core/pull/184594).

**b5 à b7 (7 octobre).** Hue ne plante plus quand des appareils partagent une adresse MAC Zigbee [#184672](https://github.com/home-assistant/core/pull/184672). Renault reçoit une réparation pour les changements de compte Kamereon [#184661](https://github.com/home-assistant/core/pull/184661). La configuration d’une app gérée n’écrase plus les options existantes [#182441](https://github.com/home-assistant/core/pull/182441). Shelly abandonne proprement la configuration d’un appareil non pris en charge [#184668](https://github.com/home-assistant/core/pull/184668).

## ⚠️ Changements cassants annoncés

Les notes finales listent **plus de vingt entrées**, notamment l’**authentification**, **MQTT**, **Synology DSM**, **Telegram bot**, **UniFi Network**, **Proxmox VE**, **Teslemetry**, **Xbox** et les **conditions d’état**. C’est l’une des listes les plus longues de l’année : à lire avant la mise à jour.

## 👩‍💻 Côté développeurs

- [La dépréciation de DeviceEntry.config_entries est désormais appliquée](https://contributors.home-assistant.io/blog/2026/09/15/device-entry-config-entries-deprecation/)
- [modbus.get_hub déprécié au profit d’async_get_unit](https://contributors.home-assistant.io/blog/2026/09/02/modbus-get-hub-deprecation/)
- [Les outils LLM renvoient un ToolResult et déclarent leur intégration](https://contributors.home-assistant.io/blog/2026/09/26/llm-tool-result/)
- [Nouveaux sélecteurs de classe d’appareil et de classe d’état](https://contributors.home-assistant.io/blog/2026/09/04/device-and-state-class-selectors/)
- [Action d’arrêt et activité « au repos » pour les tondeuses](https://contributors.home-assistant.io/blog/2026/09/11/lawn-mower-stop-action-idle-activity/)
- [Gestion des erreurs OAuth2 centralisée dans le helper](https://contributors.home-assistant.io/blog/2026/09/07/oauth2-central-error-handling/)
- [Probatio, le moteur de validation](https://contributors.home-assistant.io/blog/2026/09/30/probatio-validation-engine/)
- [Motifs d’abandon communs traduits de façon centrale](https://contributors.home-assistant.io/blog/2026/09/28/central-config-flow-abort-reasons/)
- [Exceptions d’entrée de configuration dans les migrations](https://contributors.home-assistant.io/blog/2026/09/17/use-config-entry-exc-in-migration/)

## 🧭 Pour le canal bêta

Quand cinq bêtas sortent le même jour, les derniers correctifs n’ont été testés que quelques heures avant la stable. Sur le canal bêta, c’est justement le moment d’être attentif : installez la dernière bêta, puis **attendez la première corrective** (2026.10.1) si votre installation est sensible.

<div class="ha-avis" markdown="1">
**💬 Mon avis**

Trois correctifs Freebox dans une seule bêta, dont un pour les caméras : pour un utilisateur Freebox comme moi, c’est la bêta du cycle. Et les cinq bêtas du 7 octobre montrent bien que la journée de sortie est aussi une journée de tests.
</div>

Vous utilisez les caméras Freebox dans Home Assistant ? Parlons-en sur le forum.

<p class="ha-signature">— XAV59213</p>
