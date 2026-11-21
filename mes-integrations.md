---
title: "Mes intégrations GitHub / HACS"
description: "Les intégrations Home Assistant de XAV59213 : Freebox Homexa, chauffage fil pilote, SMS Free, jours fériés, piscine et d’autres dépôts HACS."

image: /assets/images/og-default.png
date: 2026-11-20
permalink: /mes-integrations/
---

# Mes intégrations GitHub / HACS

<p class="section-lead">Ici se trouvent uniquement les <strong>dépôts et présentations d’intégrations</strong> que je développe (XAV59213). Les tests produits, les guides et les réponses dans les sujets d’autres membres sont dans des rubriques à part.</p>

<div class="feature-grid">
{% for item in site.data.integrations %}
  <article class="feature-card">
    {% if item.image %}
    <img class="card-thumb" src="{{ item.image | relative_url }}" alt="{{ item.name }}" loading="lazy" width="280" height="140">
    {% endif %}
    <div class="tag">{% if item.official %}HACS officiel{% else %}Dépôt HACS personnalisé{% endif %}</div>
    <h3>{% if item.page %}<a href="{{ item.page | relative_url }}">{{ item.name }}</a>{% else %}{{ item.name }}{% endif %}</h3>
    <p>{{ item.blurb }}</p>
    <p class="repo-actions">
      <a href="https://github.com/XAV59213/{{ item.repo }}">Dépôt GitHub</a>
      <a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&amp;repository={{ item.repo }}&amp;category=integration"><img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Ouvrir le dépôt {{ item.name }} dans HACS"></a>
    </p>
    {% include github-star.html repo=item.repo compact=true %}
    {% if item.related %}
    <ul class="integration-related">
      {% for r in item.related %}
      <li><a href="{{ r.url | relative_url }}">{{ r.title }}</a></li>
      {% endfor %}
    </ul>
    {% endif %}
  </article>
{% endfor %}
</div>

Tous les projets : [github.com/XAV59213](https://github.com/XAV59213).
