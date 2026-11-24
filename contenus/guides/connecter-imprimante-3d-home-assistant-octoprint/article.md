---
title: "Connecter son imprimante 3D à Home Assistant avec OctoPrint sur Raspberry Pi : mon retour d’expérience"
description: "Comment j’ai connecté mon imprimante 3D à Home Assistant avec OctoPrint sur un Raspberry Pi : isolation USB, image OctoPi, intégration officielle et notifications."
image: /contenus/guides/connecter-imprimante-3d-home-assistant-octoprint/images/entete-octoprint-og.jpg
image_alt: "Raspberry Pi posé sur le plateau d’une imprimante 3D Artillery Genius, éclairage bleu et violet, logo Home Assistant sur la tête d’impression."
cover_alt: "Raspberry Pi posé sur le plateau d’une imprimante 3D Artillery Genius, éclairage bleu et violet, logo Home Assistant sur la tête d’impression."
date: 2025-12-21
section: guides
tags:
  - domotique
  - home-assistant
  - octoprint
  - raspberry-pi
  - impression-3d
pdf: /contenus/guides/connecter-imprimante-3d-home-assistant-octoprint/connecter-imprimante-3d-home-assistant-octoprint.pdf
---

# Connecter son imprimante 3D à Home Assistant avec OctoPrint sur Raspberry Pi : mon retour d’expérience

<figure>
  <picture>
    <source type="image/webp" srcset="images/entete-octoprint.webp">
    <img src="images/entete-octoprint.jpg" alt="Raspberry Pi posé sur le plateau d’une imprimante 3D Artillery Genius, éclairage bleu et violet, logo Home Assistant sur la tête d’impression." width="1600" height="900">
  </picture>
</figure>

Ce contenu reprend le [sujet publié sur Forum Domotique le 21 décembre 2025](https://forumdomotique.com/forums/topic/620-connecter-son-imprimante-3d-%C3%A0-home-assistant-avec-octoprint-sur-raspberry-pi-mon-retour-dexp%C3%A9rience/).

<div class="ha-callout info" markdown="1">
Archive du sujet 620 sur ce site : [Connecter son imprimante 3D à Home Assistant avec OctoPrint]({{ '/sujets/620-connecter-son-imprimante-3d-a-home-assistant-avec-octoprint-sur-raspberry-pi-mon/messages.html' | relative_url }}).
</div>

<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/620-connecter-son-imprimante-3d-%C3%A0-home-assistant-avec-octoprint-sur-raspberry-pi-mon-retour-dexp%C3%A9rience/">Lire et commenter sur Forum Domotique</a></p>

## Sommaire

1. [Un retour d’expérience](#un-retour-dexperience)
2. [Le matériel](#le-materiel)
3. [Isoler la ligne 5V du câble USB](#isoler-la-ligne-5v-du-cable-usb)
4. [Installer OctoPi](#installer-octopi)
5. [Au quotidien avec OctoPrint](#au-quotidien-avec-octoprint)
6. [L’intégration avec Home Assistant](#lintegration-avec-home-assistant)
7. [Une automatisation de fin d’impression](#une-automatisation-de-fin-dimpression)
8. [Ce que j’en retiens](#ce-que-jen-retiens)

## 1. Un retour d’expérience {#un-retour-dexperience}

Depuis que j’ai plongé plus sérieusement dans l’impression 3D il y a quelques mois, avec une Artilery Genuis qui trône dans mon atelier, je cherchais une façon simple et fiable de surveiller mes impressions à distance sans avoir à rester collé devant la machine.

L’idée d’intégrer tout ça à **Home Assistant**, ma plateforme domotique centrale qui gère déjà lumières, thermostats et caméras dans la maison, m’a tout de suite séduit.

C’est là qu’**OctoPrint** entre en jeu, ce logiciel open source qui transforme un **Raspberry Pi** en serveur dédié pour l’imprimante.

J’ai monté ce setup il y a quelques mois maintenant, et franchement, ça a changé ma manière de lancer des impressions longues sans stress.

Pas de révolution miracle, juste une solution pratique qui fonctionne au quotidien et qui s’intègre parfaitement dans l’écosystème Home Assistant.

## 2. Le matériel {#le-materiel}

Pour le matériel, rien de bien compliqué ni d’onéreux.

J’ai utilisé un **Raspberry Pi 4** que j’avais sous la main, avec une alimentation dédiée et une carte microSD de 32 Go, mais un Pi 3 ou même un Zero 2 W fait largement l’affaire pour ce genre d’usage.

L’imprimante est connectée via un câble USB classique, et j’ai ajouté une petite webcam basique pour la surveillance vidéo.

Tout tient dans un boîtier discret fixé près de l’imprimante, alimenté indépendamment pour éviter les surprises.

Ce qui m’a agréablement surpris, c’est la compacité du montage : une fois installé, on oublie presque le Pi, il fait juste son boulot en silence sans chauffer excessivement, même pendant des impressions de plusieurs heures.

![Imprimante 3D Artillery dans une enceinte Caymon, en cours d’impression, éclairage bleu](images/imprimante-enceinte-caymon.jpg)

*L’imprimante dans son enceinte, près de laquelle est fixé le Raspberry Pi.*

![Tête d’impression et alimentation du Raspberry Pi dans l’enceinte](images/imprimante-tete-et-pi.jpg)

*Vue intérieure : tête d’impression, plateau, et alimentation du Pi dans l’enceinte.*

## 3. Isoler la ligne 5V du câble USB {#isoler-la-ligne-5v-du-cable-usb}

La mise en route commence par une étape cruciale que beaucoup négligent au départ, et que j’ai moi-même apprise à mes dépens lors d’un premier essai raté : isoler correctement la ligne 5V du câble USB pour éviter le retour de courant de l’imprimante vers le Pi.

Beaucoup d’imprimantes 3D, comme les Ender et genuis, envoient du 5V via le port USB même quand elles sont allumées, ce qui peut causer des instabilités, des redémarrages intempestifs du Pi ou pire, endommager la carte à long terme.

J’ai opté pour la méthode simple et réversible avec du ruban isolant sur la broche correspondante du connecteur USB côté Pi, mais couper le fil rouge à l’intérieur du câble fonctionne aussi très bien si on est à l’aise avec un cutter et du ruban électrique.

Ça prend cinq minutes, et croyez-moi, ça évite bien des galères par la suite.

![Broche 5V d’un connecteur USB isolée avec du ruban](images/usb-broche-5v-isolee.jpg)

*Côté Pi : la broche 5V du connecteur USB est isolée avec du ruban.*

![Schéma des broches USB Standard A et Standard B](images/usb-schema-broches.jpg)

*Repère des broches USB : la ligne 5V correspond au « + » (broche 1).*

## 4. Installer OctoPi {#installer-octopi}

Une fois cette précaution prise, l’installation d’OctoPrint se fait presque toute seule grâce à l’image **OctoPi**, qui est prête à l’emploi.

Je l’ai flashée sur la carte SD avec Raspberry Pi Imager, en configurant le Wi-Fi directement dans les options pour que le Pi se connecte au réseau domestique dès le premier démarrage.

![Raspberry Pi Imager : menu Système d’exploitation, rubrique 3D printing](images/imager-menu-impression-3d.jpg)

*Raspberry Pi Imager : on ouvre la rubrique « 3D printing ».*

![Raspberry Pi Imager : choix d’OctoPi parmi les systèmes pour imprimante 3D](images/imager-octopi.jpg)

*Dans cette liste, on choisit OctoPi.*

![Raspberry Pi Imager : OctoPi (stable), OctoPi 1.1.0 avec OctoPrint 1.11.5](images/imager-octopi-stable.jpg)

*OctoPi (stable), prêt à être flashé sur la carte SD.*

Le port série se détecte généralement automatiquement, et un baud rate en auto fait le reste.

J’ai eu un petit moment de doute quand la connexion n’était pas immédiate, mais un redémarrage de l’imprimante et du Pi a tout résolu.

À l’allumage, on accède à l’interface web via octopi.local, on suit l’assistant pour créer un compte sécurisé et connecter l’imprimante.

Depuis, la liaison est stable, même en Wi-Fi, sans latence notable pour les commandes basiques.

## 5. Au quotidien avec OctoPrint {#au-quotidien-avec-octoprint}

Au quotidien, OctoPrint devient vite indispensable.

L’interface est claire, avec un suivi en temps réel de la température du nozzle et du bed, de la progression de l’impression et même d’une webcam si on en branche une.

J’aime particulièrement pouvoir uploader un G-code depuis n’importe quel ordinateur ou téléphone, lancer une impression et la surveiller de loin.

Les plugins ajoutent des fonctionnalités utiles, comme des alertes en cas de problème ou des timelapses automatiques à la fin.

La réactivité est bonne, les commandes comme pause ou arrêt répondent instantanément, et la stabilité est au rendez-vous tant que le réseau Wi-Fi est correct.

Pour les impressions longues la nuit, c’est un vrai confort de pouvoir vérifier d’un œil sur le téléphone que tout va bien sans se lever.

![Interface OctoPrint pendant une impression : températures, avancement, fichiers et webcam](images/octoprint-interface.jpg)

*L’interface OctoPrint : températures, avancement, fichiers et vue webcam.*

## 6. L’intégration avec Home Assistant {#lintegration-avec-home-assistant}

Mais le vrai plus pour moi, c’est l’intégration avec **Home Assistant**.

![Ajout de l’intégration officielle OctoPrint dans Home Assistant](images/ha-ajout-octoprint.jpg)

*Dans Home Assistant, on ajoute l’intégration officielle OctoPrint.*

Une fois OctoPrint en place, ajouter l’intégration officielle est enfantin : dans les réglages de Home Assistant, on cherche OctoPrint, on entre l’adresse IP du Pi et la clé API générée dans OctoPrint, et voilà.

L’auto-découverte fonctionne souvent du premier coup si les deux sont sur le même réseau. Immédiatement, on récupère une foule d’entités utiles : capteurs de température, pourcentage d’avancement, état de l’impression, et même des boutons pour contrôler pause, reprise ou arrêt.

![Appareil OctoPrint dans Home Assistant : informations, contrôles, capteurs et activité](images/ha-appareil-octoprint.jpg)

*L’appareil OctoPrint dans Home Assistant : capteurs, contrôles et activité.*

J’ai créé un dashboard dédié avec une vue caméra, les températures en gros et un graphique de progression, ce qui rend le suivi hyper intuitif depuis l’application Home Assistant sur mon téléphone.

![Dashboard Home Assistant dédié à l’imprimante 3D Artillery Genius](images/ha-dashboard-imprimante.jpg)

*Le dashboard dédié : état de l’impression, températures, commandes et vue caméra.*

J’ai aussi installé la carte via HACS : <https://github.com/xZetsubou/ha-threedy-card>

![Recherche de la carte threedy dans HACS](images/hacs-threedy-card.jpg)

*La carte threedy, à installer depuis HACS.*

![Aperçu de la carte threedy pour imprimante 3D dans Home Assistant](images/threedy-card-apercu.jpg)

*Aperçu de la carte threedy dans Home Assistant.*

Ce qui simplifie vraiment la vie, c’est de pouvoir coupler ça à des automatisations : par exemple, une notification SMS quand l’impression est terminée, ou allumer une lumière spécifique dans l’atelier en cas d’erreur détectée.

## 7. Une automatisation de fin d’impression {#une-automatisation-de-fin-dimpression}

```yaml
alias: "Impression terminée "
description: ""
triggers:
  - device_id: e0fc02c08be906cef3ab379c74f10219
    domain: button
    entity_id: aa7a79614c181af12daad30fac0c2f78
    type: pressed
    trigger: device
conditions: []
actions:
  - action: notify.send_message
    metadata: {}
    data:
      message: "Impression terminée "
    target:
      entity_id: notify.papa
mode: single
```

## 8. Ce que j’en retiens {#ce-que-jen-retiens}

Ce setup a de vrais points forts qui en font une solution durable.

D’abord, la fiabilité une fois l’isolation USB bien faite, plus de crashes aléatoires qui m’avaient agacé au début.

Ensuite, la flexibilité : tout est open source, gratuit, et s’intègre sans accroc à Home Assistant sans passer par des clouds tiers.

La consommation électrique reste modeste, et le Pi dédié à OctoPrint ne perturbe pas les autres tâches domotiques.

Côté pistes d’amélioration, je dirais que l’interface OctoPrint pourrait être un peu plus moderne sur mobile, même si ça fait le job, et qu’il faut veiller à une bonne ventilation du Pi lors d’usages intensifs.

Aussi, pour les débutants en Raspberry Pi, la partie isolation USB peut sembler intimidante, mais avec les tutos de la communauté, ça passe crème.

Au final, après plusieurs mois d’utilisation régulière, je garde ce montage sans hésiter.

Il m’a apporté exactement ce que j’attendais : un contrôle distant serein de mon imprimante 3D, intégré à Home Assistant pour une vue unifiée de la maison.

C’est parfait pour les passionnés de domotique qui ont déjà une imprimante 3D et veulent aller plus loin sans complications inutiles.

Si vous hésitez encore, lancez-vous, la communauté autour d’OctoPrint et Home Assistant est active et prête à aider en cas de besoin.

Pour ma part, c’est devenu un élément fixe de mon atelier connecté.
