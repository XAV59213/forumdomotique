---
title: "Guides"
description: "Guides et tutoriels de XAV59213 pour Home Assistant : installation Zigbee, Matter, sauvegardes, et pas à pas publiés sur Forum Domotique."
image: /assets/images/og-default.png
date: 2026-11-20
permalink: /guides/
---

# Guides

<p class="section-lead">Des pas à pas pour installer, configurer et sauvegarder sa maison connectée. Le <strong>guide à la une</strong> est le plus récent, sauf choix contraire dans l’entête de l’article.</p>

{% assign guides = site.pages | where: "section", "guides" | sort: "date" | reverse %}
{% assign guides_feat = guides | where: "featured", true %}
{% if guides_feat.size > 0 %}
  {% assign guide_une = guides_feat | first %}
{% else %}
  {% assign guide_une = guides | first %}
{% endif %}
{% include featured-une.html une=guide_une label="Guide à la une" button="Lire le guide" %}

## Derniers guides

{% include item-cards.html items=guides label="Derniers guides" filters=true %}

## Autres guides publiés sur le forum

Quelques tutoriels rédigés directement dans un sujet du forum (en plus des guides ci-dessus) :

- [Guide utilisateur Freebox Homexa]({{ '/sujets/4008-guide-utilisateur-freebox-homexa-de-linstallation-a-lutilisation-v28824/messages.html' | relative_url }})
- [OctoPrint : connecter une imprimante 3D à Home Assistant]({{ '/sujets/620-connecter-son-imprimante-3d-a-home-assistant-avec-octoprint-sur-raspberry-pi-mon/messages.html' | relative_url }})
- [Ajouter la musique du disque Freebox à Music Assistant]({{ '/sujets/618-comment-ajouter-la-musique-stockee-sur-le-disque-dur-de-votre-freebox-a-music-as/messages.html' | relative_url }})

Voir aussi les [actualités]({{ '/actualites/' | relative_url }}).
