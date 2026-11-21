---
title: "Actualité Home Assistant : toutes les mises à jour 2026 expliquées en français"
description: "Chaque version mensuelle de Home Assistant expliquée en français par XAV59213 : nouveautés, intégrations, breaking changes et conseils de mise à jour."

image: /actualite-home-assistant/home-assistant-2026-11/images/cover.png
date: 2026-11-20
permalink: /actualite-home-assistant/
---

# Actualité Home Assistant

<p class="section-lead">Chaque mois, Home Assistant publie une nouvelle version. Ici, chacune est <strong>expliquée en français</strong> : ce qui change vraiment, comment s’en servir pas à pas, les nouvelles intégrations et les <strong>points à vérifier avant de mettre à jour</strong>. Toutes les informations proviennent des notes de version officielles, citées et liées dans chaque article.</p>

{% assign releases = site.pages | where: "section", "actualite-ha" | sort: "date" | reverse %}

{% include ha-hero.html items=releases label="Les dernières versions de Home Assistant" %}

## Toutes les versions de 2026

{% include ha-cards.html items=releases label="Toutes les versions" %}

<p class="ha-note">💡 Avant chaque mise à jour : faites une <strong>sauvegarde complète</strong> (Paramètres › Système › Sauvegardes) et lisez la rubrique « Breaking changes » de l’article. Les versions correctives (.1, .2…) sortent généralement chaque semaine du mois : attendre la première d’entre elles est souvent un bon réflexe.</p>
