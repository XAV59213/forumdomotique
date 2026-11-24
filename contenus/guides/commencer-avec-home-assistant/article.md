---
title: "Commencer avec Home Assistant"
description: "Un parcours pour bien démarrer avec Home Assistant en 2026 : installer, relier ses premiers objets, automatiser, et s’appuyer sur les guides, le lexique et les intégrations déjà présents sur ce site."
image: /contenus/guides/commencer-avec-home-assistant/images/cover-commencer-home-assistant-og.jpg
cover_alt: "Sur une table en bois, un petit boîtier blanc, une tasse de café, des clés et un câble réseau, près d’une plante, dans un salon lumineux."
date: 2026-11-24
section: guides
featured: true
tags:
  - home-assistant
  - débuter
  - marketplace
---

# Commencer avec Home Assistant

<figure class="bistrot-cover">
  <picture>
    <source type="image/webp" srcset="{{ '/contenus/guides/commencer-avec-home-assistant/images/cover-commencer-home-assistant.webp' | relative_url }}">
    <img src="{{ '/contenus/guides/commencer-avec-home-assistant/images/cover-commencer-home-assistant.jpg' | relative_url }}" alt="Sur une table en bois, un petit boîtier blanc, une tasse de café, des clés et un câble réseau, près d’une plante, dans un salon lumineux." width="1600" height="900">
  </picture>
  <figcaption>On installe d’abord des bases solides. Le reste, on l’ajoute à son rythme, autour d’un café.</figcaption>
</figure>

<p class="ha-note">Cette page s’inspire du guide <a href="https://forumdomotique.com/guides-tutoriels/home-assistant/bien-debuter-home-assistant/">Bien débuter avec Home Assistant</a>, publié sur Forum Domotique par Jack. Je l’ai réécrit entièrement avec mes mots, mis à jour pour Home Assistant 2026.11, et j’y ai ajouté des liens vers les contenus de ce site. Jack en reste l’auteur d’origine : merci à lui, et au forum, pour ce point de départ.</p>

## C’est quoi Home Assistant ? {#cest-quoi-home-assistant}

Home Assistant, c’est un logiciel de domotique **libre et open source**. Tu l’installes chez toi, sur une petite machine qui reste allumée, et c’est lui qui relie tes objets connectés : lumières, capteurs, chauffage, box, serrure, et bien d’autres, même quand ils ne sont pas de la même marque.

Tu peux ensuite les voir et les piloter depuis un seul tableau de bord, sur l’ordinateur ou le téléphone. Et surtout, tu peux lui apprendre des automatisations : « quand le soleil se couche, allume le salon », « si je quitte la maison, coupe cette prise ». La maison commence alors à travailler un peu toute seule.

Un point qui compte beaucoup pour moi : tout ça peut vivre **en local**. Tes données restent d’abord chez toi, et une bonne partie de la maison continue de fonctionner même si Internet est coupé. Tu n’es pas obligé de passer par le nuage de chaque fabricant pour allumer une lampe.

Ce n’est pas réservé aux informaticiens. L’interface est en français, et on peut aller très loin sans écrire une ligne de code. Le reste, on l’ajoute à son rythme.

<aside class="debuter-demo" aria-labelledby="debuter-demo-titre">
  <figure class="debuter-demo-media">
    <picture>
      <source type="image/webp" srcset="{{ '/contenus/guides/commencer-avec-home-assistant/images/debuter-demo-home-assistant.webp' | relative_url }}">
      <img src="{{ '/contenus/guides/commencer-avec-home-assistant/images/debuter-demo-home-assistant.jpg' | relative_url }}" alt="Une tablette posée sur une table en bois affiche un tableau de bord stylisé de la maison, avec un bouton vert « Essayer la démo »." width="1600" height="900">
    </picture>
  </figure>
  <div class="debuter-demo-copy">
    <h2 id="debuter-demo-titre">Découvre-le sans rien installer</h2>
    <p>Avant même de choisir une machine, tu peux te balader dans l’interface. Le site <a href="https://testhomeassistant.fr/">Test Home Assistant</a>, proposé par Maison et Domotique, met à disposition une <strong>démo gratuite</strong>, sans installation. Ils l’annoncent sur leur page d’accueil par « Testez Home Assistant en 3 secondes », et précisent qu’elle est réinitialisée chaque nuit à 03:30.</p>
    <p>Les identifiants ci-dessous sont ceux qu’ils affichent publiquement sur <a href="https://testhomeassistant.fr/">testhomeassistant.fr</a>. C’est leur démo, pas un service de ce site.</p>
    <p class="debuter-demo-creds">Utilisateur : <code>demo</code><br>Mot de passe : <code>maisonetdomotique</code></p>
    <a class="hero-btn" href="https://testhomeassistant.fr/">Essayer la démo</a>
  </div>
</aside>

On me demande souvent par où commencer ensuite, chez soi. Home Assistant a une réputation de monstre un peu intimidant, et je comprends : le vocabulaire est dense, les chemins d’installation sont nombreux, et on a vite l’impression qu’il faut tout savoir avant d’allumer la machine.

Ce n’est pas vrai. On peut démarrer simplement, en local, et faire grandir son installation ensuite. Voici l’ordre dans lequel je te conseille d’avancer, avec, à chaque étape, les articles déjà en ligne sur ce site.

## Au programme

- [C’est quoi Home Assistant ?](#cest-quoi-home-assistant)
- [Découvre-le sans rien installer](#debuter-demo-titre)
- [Pourquoi Home Assistant](#pourquoi-home-assistant)
- [Est-ce fait pour toi ?](#est-ce-fait-pour-toi)
- [Installer sur de bonnes bases](#installer-sur-de-bonnes-bases)
- [Tes premiers pas dans l’interface](#tes-premiers-pas-dans-linterface)
- [Relier tes premiers objets](#relier-tes-premiers-objets)
- [Quel protocole choisir](#quel-protocole-choisir)
- [Tes premières automatisations](#tes-premières-automatisations)
- [Fiabiliser dès le début](#fiabiliser-dès-le-début)
- [Donner une vraie tête à ton installation](#donner-une-vraie-tête-à-ton-installation)
- [Garder les choses lisibles](#garder-les-choses-lisibles)
- [Tu n’es pas tout seul](#tu-nes-pas-tout-seul)

## Pourquoi Home Assistant

Home Assistant, c’est le chef d’orchestre de la maison connectée. Il parle à tes lumières, tes capteurs, ta box, parfois même à l’imprimante 3D ou à un portail, et il le fait d’abord **chez toi**. Les commandes ne dépendent pas d’un nuage lointain pour allumer une lampe dans le salon. Si Internet tombe, une bonne partie de la maison continue de vivre.

C’est aussi un projet libre, qui évolue tous les mois. Au début, il demandait de mettre les mains dans le code. Aujourd’hui, une grande partie se règle dans l’interface, en français, sans écrire une ligne. Le YAML reste là pour plus tard, si tu en as envie. Pas avant.

Et surtout, il grandit avec toi. On commence par deux ou trois objets. On ajoute une automatisation, un coordinateur Zigbee, un joli dashboard. Un jour, on se retrouve à suivre la lune, les jours fériés ou les lancements Starship, simplement parce que c’est possible. Mais ça, ce n’est pas le programme du premier soir.

Si les mots te semblent déjà un peu flous, commence par [le lexique Home Assistant]({{ '/contenus/coin-bistrot/lexique-home-assistant/article.html' | relative_url }}) du Coin bistrot. J’y explique le vocabulaire comme autour d’un café, y compris le **Marketplace** et les **applications**, qui ont remplacé ce qu’on appelait HACS et les add-ons.

## Est-ce fait pour toi ?

Oui, si tu as envie de centraliser tes objets sans dépendre uniquement des applications de chaque marque. Oui, si tu aimes comprendre ce qui se passe dans la maison. Non, tu n’as pas besoin d’être informaticien.

Il te faut un peu de curiosité, une machine qui restera allumée, et la patience de avancer par petites étapes. Les coincements font partie du voyage : on lit, on pose une question, on recommence. J’en ai connu plus d’un, y compris avec un simple interrupteur.

Ce que je te déconseille, c’est de tout vouloir le premier week-end : vingt protocoles, trois tableaux de bord et une dizaine d’automatisations d’un coup. Pose d’abord les fondations.

## Installer sur de bonnes bases

Le projet officiel recommande **Home Assistant Operating System** (HA OS). C’est la voie que je te conseille aussi pour démarrer. Tu as le Supervisor, les mises à jour en un clic, et le magasin d’**applications** (l’ancien nom, c’était add-ons). Les autres modes — un simple conteneur Docker, ou une installation plus technique — existent, mais ils demandent que tu gères davantage toi-même, et tu n’as pas les applications.

Pour le matériel, plusieurs chemins sont possibles. Aucun n’est « le seul bon » :

- Le matériel officiel, comme le Home Assistant Green, est pensé pour être simple à mettre en route. Le Yellow s’adresse à ceux qui veulent un socle plus évolutif, avec de la radio à bord selon les versions.
- Un Raspberry Pi reste un grand classique. Si tu aimes mettre les mains dans le boîtier, j’ai raconté [comment j’ai fabriqué ma box, de l’impression 3D à Home Assistant]({{ '/creations/box-domotique-impression-3d-home-assistant/' | relative_url }}).
- Un mini-PC, discret et un peu plus à l’aise en réserve de puissance, est une belle option si tu veux quelque chose de durable.
- Si tu as déjà un homelab (un NAS, une machine sous Proxmox…), tu peux virtualiser HA OS. C’est pratique, à condition d’être à l’aise avec cet environnement.

Dans tous les cas, installe sur un stockage fiable : une carte SD usée est une mauvaise surprise. Un SSD, quand c’est possible, te donnera l’esprit plus tranquille. Et prévois dès le premier jour un endroit pour tes [sauvegardes]({{ '/contenus/guides/sauvegarde-home-assistant-backup-cloud/article.html' | relative_url }}) : on en reparle plus bas, mais autant le savoir tout de suite.

## Tes premiers pas dans l’interface

Quand la machine a démarré, ouvre un navigateur sur le même réseau et va sur `http://homeassistant.local:8123`. Si ce nom ne répond pas, l’adresse IP locale de la machine fera le même travail.

L’assistant de démarrage te demande un compte, la langue, le fuseau, l’emplacement de la maison (utile pour le soleil et la météo), puis il propose souvent des appareils déjà vus sur le réseau. Tu n’es pas obligé de tout valider d’un trait : tu pourras y revenir.

Tu arrives ensuite sur le tableau de bord. Au début, il se remplit un peu tout seul. Ce n’est pas encore « chez toi », et c’est normal. On le personnalisera plus tard.

Pense aussi à l’application officielle, **Home Assistant Companion**, sur téléphone. Elle affiche la même maison dans ta poche, envoie tes notifications, et peut partager la position ou les capteurs du téléphone. Pour beaucoup d’automatisations du type « quand je rentre », elle devient vite indispensable.

## Relier tes premiers objets

Une **intégration**, c’est le pont entre Home Assistant et un appareil, une marque ou un service. Certaines sont officielles, d’autres viennent de la communauté. Depuis Home Assistant 2026.11, tu trouves ces dernières dans **Réglages → Marketplace**, sans rien installer au préalable. Ce n’est plus HACS, même si tu verras encore ce nom un peu partout, y compris dans d’anciens articles.

Le Marketplace, ce n’est pas le magasin d’applications. Les applications (File editor, MQTT, Zigbee2MQTT, Matter Server…) s’installent à part, sur HA OS uniquement, via **Réglages → Applications → Installer une application**. J’y reviens dans [le lexique]({{ '/contenus/coin-bistrot/lexique-home-assistant/article.html' | relative_url }}) et dans [mes notes sur la version 2026.11]({{ '/actualite-home-assistant/home-assistant-2026-11/' | relative_url }}).

Pour ajouter un appareil, le plus simple est souvent **Réglages → Appareils et services**, puis d’ajouter une intégration, ou de suivre une découverte automatique. Commence par ce que tu as déjà : des ampoules Wi-Fi, une box, une prise, un capteur. Un objet qui réagit tout de suite, ça donne confiance.

Si tu as une Freebox, j’ai écrit un [guide utilisateur de Freebox Homexa]({{ '/contenus/guides/guide-utilisateur-freebox-homexa/article.html' | relative_url }}), de l’installation à l’usage de tous les jours. Mes autres ponts vers la maison se trouvent dans [Mes intégrations]({{ '/mes-integrations/' | relative_url }}) : chauffage au fil pilote, SMS Free, jours fériés, et d’autres encore. Tu les installes depuis le Marketplace.

## Quel protocole choisir

Tous les objets ne parlent pas la même langue.

Le **Wi-Fi** est pratique pour débuter : pas de dongle, souvent une application du fabricant, et Home Assistant s’y branche ensuite. L’inconvénient, c’est qu’il partage le réseau de la maison, et que trop d’objets Wi-Fi finissent par le charger.

Le **Zigbee** est, pour beaucoup d’entre nous, le plus confortable une fois le premier coordinateur en place : peu gourmand, très répandu, et pensé pour le local. Tu as alors deux grandes familles logicielles. **ZHA** est intégré à Home Assistant, direct et suffisant pour beaucoup d’installations. **Zigbee2MQTT** tourne à côté, souvent comme une application, et relie le réseau par MQTT. Il est très apprécié, notamment pour la large liste d’appareils qu’il connaît. Si tu pars sur cette voie, mon astuce pour [renommer proprement tes instances Zigbee2MQTT]({{ '/contenus/coin-bistrot/renommer-instances-zigbee2mqtt/article.html' | relative_url }}) dans le menu te évitera d’avoir dix fois le même nom qui se battent en duel.

**Z-Wave** reste solide, un peu plus typé « historique européen », avec son propre dongle.

**Matter** et **Thread** arrivent de plus en plus, avec l’idée qu’un objet d’une marque parle le même langage qu’un autre, en local. J’en parle concrètement dans mon [test de la serrure Aqara U200]({{ '/contenus/tests/test-avis-aqara-u200-serrure-connectee-matter-thread/article.html' | relative_url }}), et côté radio dans le [guide]({{ '/contenus/guides/guide-du-smlight-slzb-mr4u-installation-multi-radio-dedie-a-lopen-border-router-pour-matte/article.html' | relative_url }}) et le [test du SMLight SLZB-MR4U]({{ '/contenus/tests/test-slzb-mr4u-coordinateur-zigbee-thread-matter/article.html' | relative_url }}), un coordinateur Zigbee et Thread que j’ai utilisé chez moi.

Le Bluetooth et le 433 MHz ont encore leur place pour certains capteurs, mais je ne te les mets pas en premier pour une installation neuve.

Si tu hésites, un coordinateur Zigbee (ou un modèle capable de Zigbee et de Thread) et quelques objets simples suffisent à apprendre. J’ai aussi un [guide pour le Sonoff ZBMINIL2]({{ '/contenus/guides/installer-sonoff-zbminil2-home-assistant-zigbee-sans-neutre/article.html' | relative_url }}), un micromodule Zigbee sans neutre, quand tu veux domotiser un éclairage existant.

## Tes premières automatisations

Une automatisation, c’est une phrase : **quand** ceci se produit, **si** telle condition est vraie, **alors** fais cela. Le soleil se couche, j’allume le salon. Je quitte la maison, je coupe une prise. Une fenêtre reste ouverte et la pluie arrive, je reçois une notification.

Pour en créer une : **Réglages → Automatisations et scènes**, puis une automatisation vide. Tu choisis un déclencheur, éventuellement une condition, puis une action. Tout passe par l’interface. Tu peux tester tout de suite, et corriger sans drame.

Trois idées pour se faire la main, sans rien de sorcier :

1. Allumer une lumière au coucher du soleil.
2. Éteindre certaines prises quand tout le monde est parti.
3. Envoyer une notification si une fenêtre est ouverte alors que la météo annonce de la pluie.

Le YAML viendra plus tard, si tu veux versionner tes recettes ou aller plus loin. Ce n’est pas un prérequis.

## Fiabiliser dès le début

Une belle installation que l’on ne peut pas restaurer, ce n’est qu’une belle installation… jusqu’au jour où. Mets en place des sauvegardes tout de suite, chez toi, et si possible une copie ailleurs. J’ai détaillé le sujet dans le [guide des sauvegardes Home Assistant]({{ '/contenus/guides/sauvegarde-home-assistant-backup-cloud/article.html' | relative_url }}) : copies locales, Google Drive et cloud.

Pour les mises à jour, mon réflexe est simple : je lis les notes, je sauvegarde, et je ne me précipite pas toujours le jour J. Les versions mensuelles de Home Assistant sont racontées en français dans la rubrique [Actualité Home Assistant]({{ '/actualite-home-assistant/' | relative_url }}). Un coup d’œil aux changements qui cassent quelque chose évite bien des matins difficiles.

L’accès depuis l’extérieur est un autre sujet à traiter posément. Le service officiel Home Assistant Cloud (Nabu Casa) est le chemin le plus simple pour beaucoup. Un VPN, ou d’autres tunnels, conviennent si tu es à l’aise avec la technique. L’important est de ne pas exposer ton interface n’importe comment sur Internet.

## Donner une vraie tête à ton installation

Le dashboard par défaut suffit pour vérifier que tout répond. Ensuite, on a envie que ce soit *chez soi* : des pièces, des raccourcis, une lumière clairement nommée, un coup d’œil le matin.

Pour ça, je te renvoie à mon retour sur [Mushroom Cards]({{ '/contenus/coin-bistrot/faire-ses-premiers-dashboards-mushroom-cards/article.html' | relative_url }}). C’est devenu mon quotidien pour les tableaux de bord, et l’installation passe maintenant par le Marketplace, plus par l’ancien HACS.

Justement, le Marketplace (toujours dans **Réglages**) est aussi l’endroit où tu ajoutes des cartes communautaires, des thèmes, des modèles. Comme tout ce qui vient de la communauté, tu regardes l’auteur et les retours avant d’installer. Tes applications, elles, restent dans le magasin d’applications.

## Garder les choses lisibles

Prends de bonnes habitudes tôt, elles te feront gagner des heures plus tard.

Donne des noms clairs à tes entités, avec la pièce dedans : `lumiere_salon` se retrouve autrement mieux qu’un nom tout juste sorti de la boîte. Range tes appareils dans des pièces. Si tu as plusieurs instances de Zigbee2MQTT, [renomme-les dans le menu]({{ '/contenus/coin-bistrot/renommer-instances-zigbee2mqtt/article.html' | relative_url }}) pour t’y retrouver.

Les automatisations aussi aiment les titres parlants : « Coucher de soleil, allumer le salon » se débogue mieux que « Automatisation 14 ».

## Tu n’es pas tout seul

Home Assistant se découvre bien mieux en compagnie. [Forum Domotique](https://forumdomotique.com/) est là pour les questions, même les plus simples. Sur ce site, tu as le [Coin bistrot]({{ '/coin-bistrot-de-la-domotique/' | relative_url }}), les [guides]({{ '/guides/' | relative_url }}), les [tests]({{ '/tests-produits/' | relative_url }}), [mes créations]({{ '/creations/' | relative_url }}) et [mes intégrations]({{ '/mes-integrations/' | relative_url }}).

Voici le parcours que je te propose, dans l’ordre, une fois cette page lue :

<div class="feature-grid">
  <a class="feature-card" href="{{ '/contenus/coin-bistrot/lexique-home-assistant/article.html' | relative_url }}">
    <img class="card-thumb" src="{{ '/contenus/coin-bistrot/lexique-home-assistant/images/cover-coin-bistrot-og.jpg' | relative_url }}" alt="Couverture du lexique Home Assistant" loading="lazy" width="280" height="140">
    <div class="tag tag-bistrot">1. Le vocabulaire</div>
    <h3>Le lexique Home Assistant</h3>
    <p>Les mots utiles, y compris Marketplace et applications, expliqués simplement.</p>
  </a>
  <a class="feature-card" href="{{ '/contenus/guides/sauvegarde-home-assistant-backup-cloud/article.html' | relative_url }}">
    <img class="card-thumb" src="{{ '/contenus/guides/sauvegarde-home-assistant-backup-cloud/images/cover-sauvegarde.png' | relative_url }}" alt="Couverture du guide des sauvegardes Home Assistant" loading="lazy" width="280" height="140">
    <div class="tag">2. Les bases solides</div>
    <h3>Sauvegarder Home Assistant</h3>
    <p>Les copies locales et le cloud, pour pouvoir restaurer le jour où il le faudra.</p>
  </a>
  <a class="feature-card" href="{{ '/contenus/coin-bistrot/faire-ses-premiers-dashboards-mushroom-cards/article.html' | relative_url }}">
    <img class="card-thumb" src="{{ '/contenus/coin-bistrot/faire-ses-premiers-dashboards-mushroom-cards/images/cover-mushroom-cards-og.jpg' | relative_url }}" alt="Couverture de l’article sur les dashboards Mushroom Cards" loading="lazy" width="280" height="140">
    <div class="tag tag-bistrot">3. Le tableau de bord</div>
    <h3>Premiers dashboards avec Mushroom</h3>
    <p>Mon retour après plusieurs mois, et l’installation désormais via le Marketplace.</p>
  </a>
  <a class="feature-card" href="{{ '/contenus/coin-bistrot/renommer-instances-zigbee2mqtt/article.html' | relative_url }}">
    <img class="card-thumb" src="{{ '/contenus/coin-bistrot/renommer-instances-zigbee2mqtt/images/cover-renommer-z2m-og.jpg' | relative_url }}" alt="Couverture de l’astuce pour renommer Zigbee2MQTT" loading="lazy" width="280" height="140">
    <div class="tag tag-bistrot">4. Zigbee, au propre</div>
    <h3>Renommer ses instances Zigbee2MQTT</h3>
    <p>Une petite astuce de menu, très utile dès que l’on a plus d’une instance.</p>
  </a>
  <a class="feature-card" href="{{ '/mes-integrations/' | relative_url }}">
    <img class="card-thumb" src="{{ '/sujets/4074-freebox-homexa-est-dans-hacs-par-defaut-et-pas-mal-de-nouveautes/images/IMG_7808.png' | relative_url }}" alt="Aperçu de l’intégration Freebox Homexa" loading="lazy" width="280" height="140">
    <div class="tag">5. Mes intégrations</div>
    <h3>Les ponts que je développe</h3>
    <p>Freebox Homexa, chauffage fil pilote, SMS, jours fériés… à installer depuis le Marketplace.</p>
  </a>
  <a class="feature-card" href="{{ '/actualite-home-assistant/home-assistant-2026-11/' | relative_url }}">
    <img class="card-thumb" src="{{ '/actualite-home-assistant/home-assistant-2026-11/images/cover.png' | relative_url }}" alt="Couverture des notes de version Home Assistant 2026.11" loading="lazy" width="280" height="140">
    <div class="tag">6. Rester à jour</div>
    <h3>Home Assistant 2026.11</h3>
    <p>La version où HACS devient le Marketplace officiel, expliquée en français.</p>
  </a>
</div>

Tu n’as pas à tout lire d’une traite. Prends le lexique, installe proprement, sauvegarde, relie un premier objet, puis une première automatisation. Le reste viendra tout seul, comme la seconde tasse de café.

Et encore merci à Jack, et à [son guide sur Forum Domotique](https://forumdomotique.com/guides-tutoriels/home-assistant/bien-debuter-home-assistant/), qui m’a servi de base pour poser ce parcours.
