---
title: "Tests produits"
description: "Tests et avis de XAV59213 sur des produits domotiques : serrure Nuki Smart Lock Pro 5e génération, tondeuse Navimow, serrure Aqara U200, coordinateur SMLight SLZB-MR4U, et d’autres à venir."
image: /assets/images/og-default.png
date: 2026-11-20
permalink: /tests-produits/
---

# Tests produits

<p class="section-lead">Retours d’usage, photos à l’appui, pour choisir un matériel compatible Home Assistant. Chaque test indique le <strong>produit</strong>, la <strong>marque</strong>, un carrousel de photos, et un lien vers l’article d’origine sur Forum Domotique.</p>

<p class="section-lead">Le <strong>test à la une</strong> est le plus récent, sauf choix contraire dans l’entête de l’article.</p>

{% include prochains-tests.html lead="Voici ce que je prépare, avant de publier le test complet." %}

{% assign tests = site.pages | where: "section", "tests" | sort: "date" | reverse %}
{% assign tests_feat = tests | where: "featured", true %}
{% if tests_feat.size > 0 %}
  {% assign test_une = tests_feat | first %}
{% else %}
  {% assign test_une = tests | first %}
{% endif %}
{% include featured-une.html une=test_une label="Test à la une" button="Lire le test" %}

## Derniers tests

{% include item-cards.html items=tests label="Derniers tests" filters=true %}
