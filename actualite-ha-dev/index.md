---
title: "Actualité HA développement : les bêtas de Home Assistant 2026 expliquées en français"
description: "Chaque cycle bêta de Home Assistant depuis janvier 2026 suivi en français par XAV59213 : nouveautés en test, correctifs entre bêtas et changements cassants."
image: /actualite-ha-dev/home-assistant-2026-12-beta/images/cover.png
cover_alt: "Couverture : Actualité HA développement, la bêta de Home Assistant 2026.12"
date: 2026-11-26
permalink: /actualite-ha-dev/
---

# Actualité HA développement

<p class="section-lead">Je suis sur le <strong>canal de développement</strong> de Home Assistant : j’installe les versions de test avant tout le monde. Cette rubrique suit chaque <strong>cycle bêta mensuel</strong> depuis janvier 2026 : ce qui arrive en test, ce qui est corrigé (ou retiré) d’une bêta à l’autre, les <strong>changements cassants annoncés</strong> et ce qui change pour les développeurs d’intégrations. Toutes les informations viennent des sources officielles (GitHub, notes de la bêta, blog des contributeurs), citées et liées dans chaque article.</p>

{% assign cycles = site.pages | where: "section", "actualite-ha-dev" | sort: "date" | reverse %}

{% include ha-dev-hero.html items=cycles label="Les derniers cycles bêta de Home Assistant" %}

## Tous les cycles bêta de 2026

{% include ha-dev-cards.html items=cycles label="Tous les cycles bêta" %}

## Stable, bêta ou dev : quel canal choisir ?

<div class="hd-channels">
<div class="hd-channel is-stable" markdown="1">
### 🟦 Stable
La version mensuelle, publiée en général le premier mercredi du mois, puis ses correctives (.1, .2…). C’est le bon choix pour une maison qui doit simplement fonctionner. Elle est suivie dans [Actualité HA]({{ '/actualite-home-assistant/' | relative_url }}).
</div>
<div class="hd-channel is-beta" markdown="1">
### 🟧 Bêta
Environ une semaine avant chaque version, Home Assistant publie une **b0** puis une série de bêtas (b1, b2…) qui corrigent ce que les testeurs remontent. Pour la rejoindre : **Paramètres › Système › Mises à jour**, menu ⋮, **Rejoindre la bêta**, ou `ha supervisor options --channel beta`.
</div>
<div class="hd-channel is-dev" markdown="1">
### 🟥 Dev
La branche de développement, au plus près du code. La documentation officielle prévient qu’elle est « probablement instable » et peut aller jusqu’à la **perte de données**. Commande : `ha supervisor options --channel dev`, puis `ha supervisor reload` et `ha core update --backup`.
</div>
</div>

<p class="ha-note hd-note">💡 Sur la bêta comme sur dev : <strong>sauvegarde complète avant chaque mise à jour</strong> (l’option <code>--backup</code> crée une sauvegarde partielle pour revenir en arrière), et signalez les problèmes en précisant <strong>le numéro exact de la bêta</strong> sur <a href="https://github.com/home-assistant/core/issues">GitHub</a>. Le salon <em>#beta</em> du <a href="https://www.home-assistant.io/join-chat">Discord officiel</a> rassemble testeurs et développeurs. Source : <a href="https://www.home-assistant.io/common-tasks/os/#running-a-beta-version">documentation Home Assistant OS</a>.</p>
