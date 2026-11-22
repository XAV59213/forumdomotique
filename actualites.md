---
title: "Actualités"
description: "Actualités Home Assistant rédigées par XAV59213 sur Forum Domotique : mises à jour, nouveautés et points remarquables de chaque version."
image: /assets/images/og-default.png
date: 2026-11-20
permalink: /actualites/
# URLs Jekyll (sans baseurl) à mettre en avant, dans l’ordre :
# la première devient « à la une », les suivantes « À lire aussi ».
# Liste vide : l’actualité la plus récente s’affiche automatiquement.
une_urls:
  - /sujets/536-zigbee-40-revolution-iot-adieu-les-pannes-bonjour-la-magie-connectee/messages.html
  - /sujets/676-le-drame-invisible-quand-ton-wi-fi-tue-ton-zigbee-en-silence/messages.html
---

# Actualités

<p class="section-lead">Les notes de version et actualités Home Assistant publiées sur Forum Domotique, ainsi que les publications mises en avant. L’<strong>actualité à la une</strong> est la plus récente, sauf si une ou plusieurs publications sont mises en avant.</p>

<p class="ha-note">📰 Retrouvez aussi chaque version 2026 expliquée en détail dans la section <a href="{{ '/actualite-home-assistant/' | relative_url }}">Actualité Home Assistant</a>.</p>

{% assign news_legacy = site.pages | where: "section", "actualites" | where_exp: "item", "item.canonical_url == nil" %}
{% assign news_ha = site.pages | where: "section", "actualite-ha" %}
{% assign news = news_legacy | concat: news_ha | sort: "date" | reverse %}
{% assign news_une = news | first %}
{% assign pinned_pages = nil %}
{% if page.une_urls %}
  {% for u in page.une_urls %}
    {% if u != "" %}
      {% assign found = site.pages | where: "url", u %}
      {% if found.size > 0 %}
        {% if pinned_pages %}
          {% assign pinned_pages = pinned_pages | concat: found %}
        {% else %}
          {% assign pinned_pages = found %}
        {% endif %}
      {% endif %}
    {% endif %}
  {% endfor %}
{% endif %}
{% if pinned_pages and pinned_pages.size > 0 %}
  {% assign news_une = pinned_pages | first %}
  {% assign pins_to_add = nil %}
  {% for p in pinned_pages %}
    {% assign already = news | where: "url", p.url %}
    {% if already.size == 0 %}
      {% assign found = site.pages | where: "url", p.url %}
      {% if pins_to_add %}
        {% assign pins_to_add = pins_to_add | concat: found %}
      {% else %}
        {% assign pins_to_add = found %}
      {% endif %}
    {% endif %}
  {% endfor %}
  {% if pins_to_add %}
    {% assign news = pins_to_add | concat: news %}
  {% endif %}
{% endif %}
{% include featured-une.html une=news_une label="Actualité à la une" button="Lire l’actualité" %}
{% if pinned_pages %}
  {% for p in pinned_pages %}
    {% unless forloop.first %}
      {% include featured-une.html une=p label="À lire aussi" button="Lire l’article" class="featured-also" %}
    {% endunless %}
  {% endfor %}
{% endif %}

## Dernières actualités

{% include item-cards.html items=news label="Dernières actualités" filters=true %}
