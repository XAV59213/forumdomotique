---
title: "Partenariats & presse"
description: "Partenariats et presse de XAV59213 : tests de matériel de maison connectée en conditions réelles, et comment me proposer un produit à tester."
image: /assets/images/og-partenariats-presse.png
date: 2026-11-21
permalink: /partenariats-presse/
---

# Partenariats & presse

<p class="section-lead">Moi c’est <strong>XAV59213</strong>. Cette page s’adresse aux marques, aux attachés de presse et à celles et ceux qui souhaitent me proposer un produit à tester. Vous y trouverez ce que je teste, comment je travaille, et comment me contacter, sans formulaire caché ni adresse électronique publique.</p>

## Qui je suis

Je teste du matériel de domotique et de maison connectée, et je développe des intégrations Home Assistant, disponibles dans HACS ou en dépôt personnalisé. Je publie mes tests, mes guides et mes créations sur cette vitrine, et sur Forum Domotique.

{% include audience-bloc.html %}

## Ce que je teste

Je m’intéresse aux produits qui s’intègrent à une maison connectée, en particulier avec Home Assistant :

<ul class="press-topics">
  <li>Domotique et maison connectée</li>
  <li>Home Assistant</li>
  <li>Zigbee, Matter et Thread</li>
  <li>Solaire</li>
  <li>Jardin et piscine connectés</li>
  <li>Robots de tonte</li>
</ul>

Cette liste n’est pas exhaustive : un produit peut aussi entrer dans le cadre d’un test s’il enrichit vraiment une installation connectée.

## Ma méthode

<ul class="press-method">
  <li>Je teste longtemps, en conditions réelles, dans mon installation.</li>
  <li>Je m’attarde sur l’intégration dans Home Assistant : l’installation, l’usage au quotidien et les limites éventuelles.</li>
  <li>Mon avis reste honnête, qu’il soit positif ou réservé.</li>
  <li>Quand un produit m’est confié dans le cadre d’un partenariat, je le mentionne clairement dans l’article.</li>
</ul>

## Tests déjà publiés

<p class="section-lead">Voici les tests produits déjà en ligne sur le site. Cette liste se met à jour toute seule à chaque nouvel article.</p>

{% assign tests = site.pages | where: "section", "tests" | sort: "date" | reverse %}
{% include item-cards.html items=tests label="Tests déjà publiés" %}

<p class="press-more"><a href="{{ '/tests-produits/' | relative_url }}">Voir tous les tests produits</a></p>

{% include prochains-tests.html title="Tests à venir" lead="Les tests en préparation, avant la publication de l’article complet." %}

## Réutilisation des articles

Les articles de cette vitrine peuvent être repris par Forum Domotique, ainsi que par les fabricants ou les fournisseurs des marques des produits testés, à condition d’en citer la source. Le détail se trouve sur la page <a href="{{ '/droits-et-autorisations/' | relative_url }}">Droits et autorisations</a>.

## Mes intégrations

{% assign integ_count = site.data.integrations.size %}
En plus des tests, je développe <strong>{{ integ_count }} intégrations</strong> Home Assistant. Vous les trouverez, avec les dépôts GitHub et les badges HACS, sur la page <a href="{{ '/mes-integrations/' | relative_url }}">Mes intégrations</a>.

## Me proposer un produit

Pour me proposer un produit à tester, ouvrez une demande sur le dépôt GitHub de cette vitrine, ou écrivez-moi via mon profil Forum Domotique. Je ne publie ni adresse électronique, ni numéro de téléphone.

<p class="press-cta">
  <a class="btn-demand" href="https://github.com/XAV59213/forumdomotique/issues/new?template=proposition-test.yml">Proposer un produit à tester</a>
  <a class="press-profile" href="https://forumdomotique.com/profile/106-xav59213/">Profil Forum Domotique</a>
</p>

<p class="press-forum">Vous cherchez les partenariats du forum lui-même ? <a href="https://forumdomotique.com/partenariats-presse/">Partenariats Forum Domotique</a></p>
