---
title: "Actualités"
description: "Actualités Home Assistant rédigées par XAV59213 sur Forum Domotique : mises à jour, nouveautés et points remarquables de chaque version."
image: /assets/images/og-default.png
date: 2026-11-20
permalink: /actualites/
---

{% include site-nav.html %}

# Actualités

<p class="section-lead">Les notes de version et actualités Home Assistant publiées sur Forum Domotique. L’<strong>actualité à la une</strong> est la plus récente, sauf si un article porte <code>featured: true</code> dans son entête.</p>

{% assign news = site.pages | where: "section", "actualites" | sort: "date" | reverse %}
{% assign news_feat = news | where: "featured", true %}
{% if news_feat.size > 0 %}
  {% assign news_une = news_feat | first %}
{% else %}
  {% assign news_une = news | first %}
{% endif %}
{% include featured-une.html une=news_une label="Actualité à la une" button="Lire l’actualité" %}

## Dernières actualités

{% assign news_rest = news | where_exp: "p", "p.url != news_une.url" %}
{% include item-cards.html items=news_rest label="Dernières actualités" filters=true %}
