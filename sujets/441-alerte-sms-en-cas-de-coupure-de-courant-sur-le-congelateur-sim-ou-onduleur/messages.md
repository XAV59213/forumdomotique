---
title: "Alerte SMS en cas de coupure de courant sur le congélateur: SIM ou onduleur ?"
description: "D'abord, oui, tu es au bon endroit pour ce genre de question technique. Ton besoin est clair : alerter ton client par SMS en cas de coupure de courant…"
image: /assets/images/og-default.png
date: 2025-10-11
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/441-alerte-sms-en-cas-de-coupure-de-courant-sur-le-cong%C3%A9lateur-sim-ou-onduleur/">Lire et commenter sur Forum Domotique</a></p>

# Alerte SMS en cas de coupure de courant sur le congélateur: SIM ou onduleur ?

- **Catégorie :** [Tutoriels, Guides & Astuces des Membres](https://forumdomotique.com/forums/87-tutoriels-guides-astuces-des-membres/)
- **Sujet :** https://forumdomotique.com/forums/topic/441-alerte-sms-en-cas-de-coupure-de-courant-sur-le-cong%C3%A9lateur-sim-ou-onduleur/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 11 octobre 2025 à 16:37 (Europe/Paris)

---

## Message 1 — 11 octobre 2025 à 16:37 (Europe/Paris)

- **Identifiant :** `1036`
- **Lien :** https://forumdomotique.com/forums/topic/441-alerte-sms-en-cas-de-coupure-de-courant-sur-le-cong%C3%A9lateur-sim-ou-onduleur/#findComment-1036

> **Il y a 18 heures, Gatsso a dit :**
> Bonjour a tous je ne sais pas si je suis sur le bon forum pour ma question.
>
> Je recherche pour un de mes clients un moyen ou un système de l alerter par SMS en cas de coupure de courant totale ou partielle surtout sur la rampe du disjoncteur qui alimente le congel
>
> c est dans une résidence secondaire.
>
> en cherchant un peu j ai trouvé un appareil de marque Eighosee GA01P je crois que ça fonctionne avec une carte Sim , alors que moi j étais parti sur l idée de mettre un petit onduleur (pour éviter un abonnement de carte) avec la box internet branché dessus ,mais par manque de compétence je m arrête là.
>
> Avez vous un moyen simple que je puisse proposer ?
>
> Merci a tous.
>
> [GA01P](https://www.amazon.fr/T%C3%A9l%C3%A9commande-Intelligente-d%C3%A9lectricit%C3%A9-Plastique-S%C3%A9curit%C3%A9/dp/B0BQ7BV5M2)

Salut [@Gatsso](https://forumdomotique.com/profile/516-gatsso/) !

D'abord, oui, tu es au bon endroit pour ce genre de question technique. Ton besoin est clair : alerter ton client par SMS en cas de coupure de courant (totale ou partielle, surtout sur le circuit du congélateur) dans une résidence secondaire.

C'est un classique pour éviter les catastrophes avec les aliments !

L'appareil que tu as trouvé, le **GA01P** (je pense que c'est de la marque EiGensee ou similaire, un boîtier GSM d'alarme pour pannes de courant), super piste simple et dédiée.

Il fonctionne effectivement avec une carte SIM (pas besoin d'abonnement data, juste un forfait SMS basique genre 1-2 €/mois). Il détecte la perte de tension sur le secteur, a une batterie de backup pour envoyer l'alerte même en cas de coupure, et peut notifier jusqu'à 6 numéros par SMS/appel.

Tu le branches directement sur la rampe du disjoncteur du congélateur (ou via une prise adaptée), et hop, alerte en cas de chute de puissance. Pas de compétences en bricolage avancées requises – c'est plug-and-play.

Seul bémol : il faut une SIM, et il est un peu basique (pas de monitoring tempé en plus).

Si tu veux éviter la SIM et rester sur ton idée d'onduleur + box internet (pour une connexion WiFi stable), c'est faisable et plus flexible. Voici une proposition simple et évolutive que tu pourrais pitcher à ton client :

### Solution DIY accessible : Raspberry Pi + Home Assistant

- **Matériel de base (budget ~100-150 € une fois)** :

  - Un **Raspberry Pi 3 ou 4** (petit ordi à 40-60 €, ultra-fiable pour du monitoring distant).
  - Une **prise connectée intelligente** (genre Shelly ou TP-Link HS110, ~20 €) branchée sur le circuit du congélateur. Elle mesure la conso électrique en temps réel – si elle tombe à zéro, c'est une coupure !
  - Une **sonde de température** (DS18B20 ou via une prise compatible, ~10 €) pour surveiller l'intérieur du congélateur (alerte si > -1°C, comme tu dis).
  - Un petit **onduleur** (UPS genre APC ou un mini à 20-30 €) pour alimenter le Pi et la box internet 1-2h en cas de panne, le temps d'envoyer l'alerte.
- **Logiciel gratuit et puissant : Home Assistant (HA)** :

  - Installe HA sur le Pi (super simple via une carte SD, tutoriels en 30 min).
  - Intègre la prise connectée et la sonde directement dans HA (via WiFi/Zigbee).
  - Sur ta maison principale (ou un serveur cloud gratuit comme Nabu Casa, ~5 €/an), tu syncs tout via l'app HA. Tu auras un dashboard avec conso électrique, température, et historique.
  - Pour l'alerte SMS : Ajoute l'intégration **Twilio** ou **OVH SMS** ou gratuit avec l'api freebox

    <https://forumdomotique.com/forums/topic/110-%F0%9F%93%A8-free-mobile-sms-xa-int%C3%A9gration-home-assistant/?do=embed>
  - exemple dans HA (gratuit pour quelques SMS/mois, ou ~0,05 €/SMS). Règle des automatisations genre : "Si conso < 5W pendant 5 min OU temp > -1°C, envoie SMS 'Attention : coupure congélateur !'".
  - Bonus pour la robustesse : Installe **Uptime Kuma** (gratuit sur le même Pi ou en extension) pour "pinguer" le HA de la résidence secondaire toutes les 5 min. Si pas de réponse, alerte auto par SMS.

**Avantages** : Tout est monitoré (pas juste la coupure, mais aussi la température)

---
