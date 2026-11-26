---
title: "Comment renommer proprement ses instances Zigbee2MQTT dans le menu latéral de Home Assistant (et arrêter d’avoir dix fois « Zigbee2MQTT » qui se battent en duel)"
description: "Plusieurs instances Zigbee2MQTT portent le même nom dans le menu de Home Assistant : comment les renommer proprement, avec Ingress, pour s’y retrouver."
image: /contenus/coin-bistrot/renommer-instances-zigbee2mqtt/images/cover-renommer-z2m-og.jpg
cover_alt: "Comptoir de bistrot, un café, une clé USB Zigbee et une tablette dont le menu affiche clairement Z2M Salon, Z2M Étage, Z2M Jardin et Z2M Grange."
date: 2025-11-23
section: coin-bistrot
tags:
  - home-assistant
  - zigbee2mqtt
  - astuces
---

# Comment renommer proprement ses instances Zigbee2MQTT dans le menu latéral de Home Assistant (et arrêter d’avoir dix fois « Zigbee2MQTT » qui se battent en duel)

<figure class="bistrot-cover">
  <picture>
    <source type="image/webp" srcset="{{ '/contenus/coin-bistrot/renommer-instances-zigbee2mqtt/images/cover-renommer-z2m.webp' | relative_url }}">
    <img src="{{ '/contenus/coin-bistrot/renommer-instances-zigbee2mqtt/images/cover-renommer-z2m.jpg' | relative_url }}" alt="Comptoir de bistrot, un café, une clé USB Zigbee et une tablette dont le menu affiche clairement Z2M Salon, Z2M Étage, Z2M Jardin et Z2M Grange." width="1600" height="900">
  </picture>
  <figcaption>Le rêve, au comptoir : un coup d’œil au menu, et on sait enfin quelle instance Zigbee2MQTT ouvre quoi.</figcaption>
</figure>

Cette astuce reprend le [sujet publié sur Forum Domotique le 23 novembre 2025](https://forumdomotique.com/forums/topic/509-comment-renommer-proprement-ses-instances-zigbee2mqtt-dans-le-menu-lat%C3%A9ral-de-home-assistant-et-arr%C3%AAter-davoir-dix-fois-%C2%AB-zigbee2mqtt-%C2%BB-qui-se-battent-en-duel/).

<div class="ha-callout info" markdown="1">
Archive du sujet 509 sur ce site : [Comment renommer proprement ses instances Zigbee2MQTT dans le menu latéral de Home Assistant]({{ '/sujets/509-comment-renommer-proprement-ses-instances-zigbee2mqtt-dans-le-menu-lateral-de-ho/messages.html' | relative_url }}).
</div>

<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/509-comment-renommer-proprement-ses-instances-zigbee2mqtt-dans-le-menu-lat%C3%A9ral-de-home-assistant-et-arr%C3%AAter-davoir-dix-fois-%C2%AB-zigbee2mqtt-%C2%BB-qui-se-battent-en-duel/">Lire et commenter sur Forum Domotique</a></p>

Cela fait maintenant plusieurs années que je tourne avec plusieurs instances Zigbee2MQTT sous Home Assistant. Au début, une seule suffisait largement, puis le réseau a grandi, les extensions Zigbee se sont multipliées, les pannes de clé USB aussi, et je me suis retrouvé avec trois, puis quatre instances différentes : une pour le salon et le rez-de-chaussée, une pour l’étage, une pour l’extérieur et la dépendance, et même une petite dernière dédiée aux appareils un peu capricieux qui préfèrent vivre leur vie à part.

## Le menu latéral qui se bat en duel

Tout allait bien jusqu’au jour où j’ai regardé mon menu latéral et que j’ai eu l’impression de relire dix fois la même ligne : Zigbee2MQTT, Zigbee2MQTT, Zigbee2MQTT… Impossible de savoir en un coup d’œil laquelle ouvrait quoi. Clic droit, nouvel onglet, attendre que la page charge, ah oui c’est celle de l’étage… Fastidieux.

J’ai cherché pendant des mois la solution propre, celle qui ne consiste pas à bidouiller le nom de l’add-on dans Supervisor (ça ne change rien dans le menu) ni à prier pour qu’une option magique apparaisse un jour dans les paramètres officiels. Et puis je suis tombé sur **HACS Ingress**, une petite intégration toute simple qui règle le problème en deux minutes et, surtout, de façon parfaitement propre et stable.

<figure class="ha-figure">
  <img src="{{ '/contenus/coin-bistrot/renommer-instances-zigbee2mqtt/images/menu-lateral-z2m-renomme.png' | relative_url }}" alt="Dans le menu latéral de Home Assistant, quatre entrées bien distinctes : Z2M dev, Z2M Grange, Zigbee2MQTT et Zigbee2MQTT Edge." width="311" height="155">
  <figcaption>Le résultat, une fois les entrées renommées : on distingue enfin le dev, la grange, l’instance principale et celle en version Edge.</figcaption>
</figure>

## D’où vient Ingress, et pourquoi c’est parfait pour ça

Avant de plonger dans les étapes, deux mots sur ce qu’est Ingress. À la base, c’est le système qu’utilise Home Assistant OS pour créer les accès sécurisés aux interfaces des add-ons depuis l’interface principale (le petit iframe qui s’ouvre quand tu cliques sur « Ouvrir l’interface web » d’un add-on). Chaque add-on exposé possède un **slug** unique, un bout de code du genre `a1b2c3d4e5f`, qui permet d’y accéder via l’URL `/api/hassio_ingress/a1b2c3d4e5f`.

L’intégration [HACS Ingress](https://github.com/lovelylain/hass_ingress), développée par lovelylain, fait une chose toute bête mais géniale : elle te permet de créer tes propres entrées dans le menu latéral qui pointent vers ces URL internes, avec le nom et l’icône que tu veux. Résultat : tu peux enfin appeler ton instance « Z2M Salon », « Zigbee Étage », « Réseau Extérieur » ou même « Les relous qui tombent tout le temps » si l’envie te prend. Et surtout, tu gardes exactement la même interface Zigbee2MQTT que tu avais avant, sans aucune perte de fonctionnalité.

<div class="ha-callout" markdown="1">
**À jour pour Home Assistant 2026.11.** Depuis cette version, la boutique communautaire s’appelle **Marketplace** : c’est elle qui reprend ce que tu connaissais sous le nom de **HACS**. Les add-ons, de leur côté, s’appellent désormais des **applications**. Le fond de l’astuce ne change pas : l’intégration Ingress, le slug de chaque instance et le petit bloc à ajouter dans `configuration.yaml` restent la bonne méthode. Seuls les noms dans les menus ont bougé.
</div>

## L’installation, en quelques minutes

Si tu as déjà HACS d’installé (et à ce stade, je pense que tout le monde l’a — ou le Marketplace, depuis Home Assistant 2026.11), l’ajout se fait en moins de cinq minutes. Voici comment je procède, tel que je l’ai fait à l’époque via HACS :

1. Tu vas dans **HACS**, puis **Intégrations**.
2. Tu cliques sur les trois petits points en haut à droite, puis **Dépôts personnalisés**.
3. Tu colles l’adresse <https://github.com/lovelylain/hass_ingress>, tu valides en choisissant la catégorie **Integration**, et tu valides encore.
4. Ensuite tu descends dans **Explorer et télécharger des dépôts**, tu tapes « Ingress », tu télécharges, tu acceptes le redémarrage quand on te le propose, et c’est fini.

Rien de plus classique, exactement comme quand tu ajoutes MQTT Explorer ou Node-RED. Aujourd’hui, tu feras le même geste depuis le **Marketplace**, en ajoutant au besoin le dépôt de l’intégration.

Petit aparté : j’ai installé ça il y a maintenant plus d’un an et je n’ai jamais eu le moindre souci de mise à jour ou de compatibilité, même en passant sur les dernières versions de Home Assistant 2025.x. C’est du solide.

## Trouver le slug de chaque instance

Avant de toucher au `configuration.yaml`, il faut récupérer le fameux slug de chaque instance. Il y a plusieurs façons simples de le faire.

1. **La plus rapide, sur ordinateur.** Tu passes la souris sur l’entrée Zigbee2MQTT dans le menu latéral, tu fais clic droit, « Inspecter » (ou Ctrl+Maj+I), et dans le code tu vois directement l’URL complète avec le slug après `/api/hassio_ingress/`. Ça ressemble à ça : `45df7312_zigbee2mqtt_edge`. Tu notes cette partie, c’est ton slug.
2. **Sur tablette ou téléphone**, c’est un peu plus chiant mais faisable : tu ouvres l’interface Zigbee2MQTT, tu partages le lien vers toi-même par mail ou Telegram, et tu récupères l’URL complète comme ça.
3. **La méthode ultra propre.** Tu vas dans **Paramètres**, puis **Add-ons** (désormais les **applications**, depuis Home Assistant 2026.11). Tu cliques sur ton instance Zigbee2MQTT, onglet **Info**, tout en bas. Le slug est affiché clairement à la ligne **Ingress URL**. Sur cette même page, le **nom d’hôte** reprend souvent le même identifiant, par exemple `45df7312-zigbee2mqtt`.

<figure class="ha-figure">
  <img src="{{ '/contenus/coin-bistrot/renommer-instances-zigbee2mqtt/images/addon-info-zigbee2mqtt.png' | relative_url }}" alt="Page Info du module complémentaire Zigbee2MQTT dans Home Assistant : le nom d’hôte 45df7312-zigbee2mqtt apparaît à droite, et le menu latéral montre déjà les entrées Z2M dev et Z2M Grange." width="1200" height="725">
  <figcaption>L’onglet Info de l’instance : le nom d’hôte (ici l’identifiant public de l’add-on officiel Zigbee2MQTT) aide à retrouver le slug. Dans le menu, Z2M dev et Z2M Grange sont déjà en place.</figcaption>
</figure>

## La configuration qui change la vie, en quelques lignes

Une fois que tu as tous tes slugs sous la main, tu ouvres ton bon vieux `configuration.yaml` (moi je passe par Studio Code Server, mais File Editor ou Samba, ça marche aussi) et tu ajoutes ça tout en bas :

```yaml
ingress:
  zigbee2mqtt:          # clé sans tiret
    work_mode: hassio
    title: Z2M Grange
    icon: mdi:zigbee
    url: 45df7312_zigbee2mqtt

  zigbee2mqtt_edge:     # ← tiret remplacé par underscore
    work_mode: hassio
    title: Z2M dev
    icon: mdi:zigbee
    url: 45df7312_zigbee2mqtt_edge   # l’URL du slug de l’add-on, elle, peut contenir un tiret
```

Tu adaptes évidemment les slugs et les noms. Tu peux mettre l’icône que tu veux ; perso, j’aime bien garder une logique par étage ou par zone pour m’y retrouver encore plus vite.

<div class="ha-callout info" markdown="1">
**Le détail qui évite de se tromper.** La **clé** YAML (`zigbee2mqtt_edge`) ne doit pas contenir de tiret : on le remplace par un underscore. En revanche, le **slug** dans `url:` peut tout à fait en contenir un. Tu sauvegardes, tu vas dans **Outils de développement**, puis **Redémarrer**, et magie : tes nouvelles entrées apparaissent immédiatement dans le menu latéral, parfaitement intégrées, avec le petit cadre bleu quand tu es dessus, exactement comme les entrées natives.
</div>

## Au quotidien, ça change quoi ?

Depuis que je les ai renommées, je gagne un temps fou. Quand je cherche pourquoi la lampe de la chambre des enfants ne répond plus, je clique directement sur « Z2M Étage » au lieu de faire trois essais pour tomber sur la bonne instance. Quand je veux vérifier la batterie des capteurs de fuite d’eau du garage, un clic sur « Z2M Jardin & Dépendance » et je suis dessus. C’est tout bête, mais quand tu as 200 appareils et quatre réseaux Zigbee qui cohabitent, ce genre de petite amélioration fait vraiment la différence.

Et surtout, les anciennes entrées « Zigbee2MQTT » toutes grises sont toujours là si jamais j’en ai besoin (par exemple pour un diagnostic rapide), mais je ne les utilise presque plus. Je peux même les masquer complètement avec un petit package sidebar si je veux faire le ménage.

## Pour que ça reste propre longtemps

Quelques petites astuces que j’ai apprises à l’usage :

- Si tu crées une nouvelle instance Zigbee2MQTT plus tard, le slug sera généré automatiquement et tu n’auras plus qu’à l’ajouter dans la section `ingress`, deux minutes chrono.
- Les mises à jour de Zigbee2MQTT ou de Home Assistant n’ont jamais cassé mes entrées personnalisées jusqu’à présent.
- Si un jour tu supprimes complètement une instance, pense à nettoyer la ligne correspondante dans `configuration.yaml`, sinon tu auras un petit fantôme dans le menu (mais ça ne casse rien).

## Points forts, et le petit regret

Ce qui est génial avec cette solution, c’est qu’elle ne touche à rien d’officiel : pas de patch douteux, pas de modification du core, pas de risque de tout casser à la prochaine mise à jour. C’est juste Home Assistant qui fait ce qu’il sait déjà faire, mais en mieux.

Le seul petit regret que j’ai, c’est que ça nécessite quand même une édition manuelle du `configuration.yaml`. J’aimerais bien qu’un jour on ait un petit éditeur graphique directement dans l’interface Ingress pour ajouter ou supprimer les entrées sans toucher au YAML, mais honnêtement, vu le temps que ça me fait gagner tous les jours, je ne vais pas faire la fine bouche.

## À faire les yeux fermés

Si comme moi tu vis avec plusieurs instances Zigbee2MQTT et que tu en as marre de jouer à la roulette russe dans le menu latéral, installe Ingress et renomme-moi tout ça. C’est propre, c’est stable, c’est exactement dans l’esprit Home Assistant : on bricole un peu au début, et ensuite on vit heureux.

Depuis que je l’ai fait, je me demande même comment j’ai pu vivre aussi longtemps avec dix fois le même nom. Si tu hésites encore, viens me dire dans les commentaires combien d’instances tu as, je parie que tu vas franchir le pas dans la journée.

Et toi, tu as déjà essayé ? Ou tu as une autre méthode propre pour distinguer tes réseaux ? La section commentaires est là pour ça.
