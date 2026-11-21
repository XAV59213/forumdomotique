---
title: "Mes créations"
description: "Mes projets fabriqués de A à Z : impression 3D, capteurs, montage, configuration Home Assistant."
image: /creations/portail-coulissant-ditec-cs122e-home-assistant/images/portail-couverture.jpg
date: 2026-11-21
permalink: /creations/
---

# Mes créations <span class="az-badge">A à Z</span>

<p class="section-lead">Voici mes projets fabriqués de A à Z : impression 3D, capteurs, montage, configuration Home Assistant. Ce ne sont pas des guides repris d’ailleurs : je les ai conçus, assemblés et mis en service moi-même, et je raconte le parcours complet, du premier prototype jusqu’à l’installation qui tourne.</p>

{% assign creations = site.pages | where: "section", "creations" | sort: "date" | reverse %}
{% assign creations_feat = creations | where: "featured", true %}
{% if creations_feat.size > 0 %}
  {% assign crea_une = creations_feat | first %}
{% else %}
  {% assign crea_une = creations | first %}
{% endif %}
{% include featured-une.html une=crea_une label="Création à la une" button="Voir la création" %}

{% assign creations_rest = creations | where_exp: "p", "p.url != crea_une.url" %}
{% if creations_rest.size > 0 %}
## Autres créations

{% include item-cards.html items=creations_rest label="Autres créations" %}
{% endif %}
