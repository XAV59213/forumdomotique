---
title: "Coin bistrot de la domotique"
description: "Un coin convivial pour parler domotique : le lexique Home Assistant, l’histoire de l’interrupteur maudit, un retour sur les dashboards Mushroom Cards, et l’astuce pour renommer ses instances Zigbee2MQTT, à lire comme autour d’un café."
image: /contenus/coin-bistrot/lexique-home-assistant/images/cover-coin-bistrot-og.jpg
cover_alt: "Comptoir de bistrot chaleureux, une tablette affiche un tableau de bord de maison connectée à côté d’un café et d’objets connectés."
date: 2026-11-24
permalink: /coin-bistrot-de-la-domotique/
---

# Coin bistrot de la domotique

<p class="section-lead">Bienvenue au comptoir. Ici, on parle domotique comme autour d’un café : le vocabulaire, les protocoles, les outils, sans prise de tête. Le <strong>sujet à la une</strong> est le plus récent, sauf choix contraire dans l’entête de l’article.</p>

{% assign bistrot = site.pages | where: "section", "coin-bistrot" | sort: "date" | reverse %}
{% assign bistrot_feat = bistrot | where: "featured", true %}
{% if bistrot_feat.size > 0 %}
  {% assign bistrot_une = bistrot_feat | first %}
{% else %}
  {% assign bistrot_une = bistrot | first %}
{% endif %}
{% include featured-une.html une=bistrot_une label="À la une du bistrot" button="Lire l’article" %}

## Derniers sujets du bistrot

{% include item-cards.html items=bistrot label="Coin bistrot de la domotique" carousel=true %}
