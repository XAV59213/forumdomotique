---
title: "Rechercher sur le site"
description: "Recherchez parmi les guides, les tests, les intégrations, les actualités, le Coin bistrot, les créations et les sujets archivés de XAV59213."
image: /assets/images/og-default.png
permalink: /recherche/
---

# Rechercher sur le site

<p class="section-lead">Tapez un mot, puis affinez par rubrique si vous le souhaitez. La recherche se fait directement dans votre navigateur, à partir d’un index du site : aucun service externe, aucun compte.</p>

<div
  class="recherche-page"
  id="recherche-page"
  data-index="{{ '/recherche-index.json' | relative_url }}"
  data-page="{{ '/recherche/' | relative_url }}"
>
  <form class="recherche-form" role="search" action="{{ '/recherche/' | relative_url }}" method="get">
    <label class="recherche-label" for="recherche-q">Votre recherche</label>
    <div class="recherche-field">
      <input
        type="search"
        id="recherche-q"
        name="q"
        placeholder="Essayer « freebox », « zigbee » ou « mushroom »…"
        autocomplete="off"
        enterkeyhint="search"
        spellcheck="false"
      >
      <button type="submit" class="recherche-submit">Rechercher</button>
    </div>
  </form>
  <div class="recherche-filters" id="recherche-filters" hidden role="group" aria-label="Filtrer par rubrique"></div>
  <p class="recherche-count" id="recherche-count" aria-live="polite"></p>
  <div class="feature-grid recherche-grid" id="recherche-results"></div>
  <noscript>
    <p>La recherche instantanée a besoin de JavaScript. Vous pouvez parcourir les <a href="{{ '/guides/' | relative_url }}">guides</a>, les <a href="{{ '/tests-produits/' | relative_url }}">tests</a>, les <a href="{{ '/mes-integrations/' | relative_url }}">intégrations</a>, le <a href="{{ '/coin-bistrot-de-la-domotique/' | relative_url }}">Coin bistrot</a>, les <a href="{{ '/creations/' | relative_url }}">créations</a> et <a href="{{ '/tous-les-sujets.html' | relative_url }}">tous les sujets</a>.</p>
  </noscript>
</div>
