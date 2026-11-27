---
title: "Quel interrupteur Zigbee ou Z-Wave pour piloter mon portail électrique via Home Assistant ?"
description: "Quel interrupteur Zigbee ou Z-Wave pour piloter mon portail électrique via Home Assistant ? — sujet dans Garage et Véhicules Électriques — réponse de XAV59213 le 27 novembre 2026"
image: /assets/images/vignettes-themes/zigbee.jpg

date: 2026-11-27
seo:
  title: "Quel interrupteur Zigbee ou Z-Wave pour piloter mon portail électrique via Home Assistant ? (sujet 995) | XAV59213"
cover_alt: "Vignette de rubrique Zigbee — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/995-quel-interrupteur-zigbee-ou-z-wave-pour-piloter-mon-portail-%C3%A9lectrique-via-home-assistant/">Lire et commenter sur Forum Domotique</a></p>

# Quel interrupteur Zigbee ou Z-Wave pour piloter mon portail électrique via Home Assistant ?

- **Catégorie :** [Garage et Véhicules Électriques](https://forumdomotique.com/forums/76-garage-et-v%C3%A9hicules-%C3%A9lectriques/)
- **Sujet :** https://forumdomotique.com/forums/topic/995-quel-interrupteur-zigbee-ou-z-wave-pour-piloter-mon-portail-%C3%A9lectrique-via-home-assistant/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 27 novembre 2026 à 18:33 (Europe/Paris)

---

## Question d’origine (résumé)

Le 31 juillet 2026, un autre membre a demandé quel interrupteur Zigbee ou Z-Wave utiliser pour piloter son portail électrique depuis Home Assistant. Il s’agit d’un portail à deux battants, avec un moteur par battant et une porte piétonne intégrée, aujourd’hui commandé par une tablette Philips Welcome Eye ou une télécommande. La tablette ne lui semble pas compatible avec Home Assistant. Il a aussi publié une photo de son coffret (non reprise ici).

---

## Message 1 — 27 novembre 2026 à 18:33 (Europe/Paris)

- **Identifiant :** `5598`
- **Lien :** https://forumdomotique.com/forums/topic/995-quel-interrupteur-zigbee-ou-z-wave-pour-piloter-mon-portail-%C3%A9lectrique-via-home-assistant/#findComment-5598

Bonjour Dran,

Je tombe un peu tard sur ton sujet, mais au cas où cela puisse encore t’aider. J’ai récemment motorisé mon portail coulissant Ditec CS122E et je le pilote depuis Home Assistant. Le principe peut se transposer à un portail à battants, même si le coffret n’est pas le même.

Chez moi, la carte d’origine n’était plus là : j’ai posé une carte universelle BLX-2 / FY-ODM-08C, des photocellules de sécurité, et un module Zigbee à contact sec Sonoff MINI-ZBD. Il est alimenté en 12 V depuis la carte, et son contact COM / NO va sur l’entrée ONE (cycle ouverture / arrêt / fermeture). Il remonte dans Home Assistant via Zigbee2MQTT. Important : le contact doit faire une impulsion courte (0,5 s chez moi), et non rester fermé.

Tu n’as pas forcément besoin de changer de carte. Identifie dans ta documentation l’entrée bouton-poussoir qui ouvre déjà le portail, celle de ta tablette Philips Welcome Eye ou de ta télécommande, puis relie-y un module de ce type en parallèle. Sans le schéma de ton coffret, je ne peux pas te dire quelle borne utiliser. Tu pourras ensuite le commander depuis Home Assistant, tout en gardant tes commandes actuelles.

J’ai tout détaillé ici : https://xav59213.github.io/forumdomotique/creations/portail-coulissant-ditec-cs122e-home-assistant/

— XAV59213

---
