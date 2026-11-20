---
title: "Home Assistant: automatisation caméra Sonoff vers ZBMINIR2 ne fonctionne pas avec la condition coucher du soleil"
---

# Home Assistant: automatisation caméra Sonoff vers ZBMINIR2 ne fonctionne pas avec la condition coucher du soleil

- **Catégorie :** [Jardin Connecté et Extérieurs](https://forumdomotique.com/forums/72-jardin-connect%C3%A9-et-ext%C3%A9rieurs/)
- **Sujet :** https://forumdomotique.com/forums/topic/729-home-assistant-automatisation-cam%C3%A9ra-sonoff-vers-zbminir2-ne-fonctionne-pas-avec-la-condition-coucher-du-soleil/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 31 janvier 2026 à 09:32 (Europe/Paris)
- **Dernier message de XAV59213 :** 1 février 2026 à 09:31 (Europe/Paris)

---

## Message 1 — 31 janvier 2026 à 09:32 (Europe/Paris)

- **Identifiant :** `1925`
- **Lien :** https://forumdomotique.com/forums/topic/729-home-assistant-automatisation-cam%C3%A9ra-sonoff-vers-zbminir2-ne-fonctionne-pas-avec-la-condition-coucher-du-soleil/#findComment-1925

Bonjour Philippe,

Merci pour ta description détaillée. Ton problème semble lié à la condition “après coucher du soleil” dans Home Assistant, qui peut parfois poser des soucis si la configuration n’est pas optimale ou si la formulation de la condition n’est pas adaptée. Voici quelques idées et suggestions pour dépanner et corriger ça étape par étape. Je me base sur des problèmes courants rapportés dans la communauté Home Assistant.

**1. Vérifie la configuration de la localisation et du soleil dans Home Assistant**

•  Home Assistant utilise l’intégration “Sun” pour calculer les heures de lever/coucher du soleil. Pour que ça fonctionne, assure-toi que ta localisation est correctement définie :

•  Va dans **Paramètres > Système > Général** (ou “Configuration > Général” selon la version).

•  Vérifie et édite la **localisation** : entre ta latitude, longitude (tu peux les trouver via Google Maps) et le fuseau horaire.

•  Si ces infos manquent ou sont erronées, les conditions liées au soleil ne fonctionneront pas correctement (par exemple, le coucher du soleil pourrait être calculé pour un mauvais endroit).

•  Redémarre Home Assistant après modification pour que les changements prennent effet.

•  Teste l’état du soleil : Dans l’interface HA, cherche l’entité sun.sun. Pendant la journée, elle devrait être en état “above_horizon” (au-dessus de l’horizon), et la nuit “below_horizon”. Si ce n’est pas le cas, c’est un signe de mauvais paramétrage.

**2. Adapte la condition dans ton automatisation**

•  Au lieu d’utiliser directement “après coucher du soleil” (qui peut avoir des bugs avec les offsets ou après minuit, comme rapporté dans certains cas), essaie une condition plus simple et fiable basée sur l’état du soleil :

•  Dans l’éditeur d’automatisation (YAML ou interface graphique), remplace ta condition par :

```yaml
condition:
  - condition: state
    entity_id: sun.sun
    state: below_horizon
```

Ça signifie : “exécuter seulement si le soleil est sous l’horizon” (c’est-à-dire la nuit, entre coucher et lever du soleil). C’est équivalent à ton intention et évite les problèmes de calcul d’heure spécifique.

•  Si tu veux un offset (par exemple, 30 minutes après le coucher), tu peux l’ajouter comme suit :

```yaml
condition:
  - condition: sun
    after: sunset
    after_offset: "00:30:00"
```

Mais attention : des bugs ont été signalés avec les offsets positifs après le coucher (le système peut confondre avec le lendemain). Teste sans offset d’abord.

•  Si tu édites en YAML, voici un exemple complet d’automatisation basique (adapte à tes entités) :

```yaml
alias: Allumer lumières sur détection caméra
description: ''
trigger:
  - platform: state  # Ou l'événement de détection de ta caméra Sonoff
    entity_id: binary_sensor.ta_camera_detection  # Remplace par l'entité de détection humaine/objet
    to: 'on'
condition:
  - condition: state
    entity_id: sun.sun
    state: below_horizon
action:
  - service: switch.turn_on
    entity_id: switch.ton_sonoff_zbminir2
mode: single
```

•  Note : Assure-toi que la détection de la caméra (via l’intégration Sonoff ou eWeLink) déclenche bien un événement ou un état que HA peut utiliser comme trigger.

Si ça ne résout pas, peux-tu partager le YAML exact de ton automatisation (sans infos sensibles) ?

Ça aiderait à comprendre le souci. N’hésite pas si tu as plus de détails !

---

## Message 2 — 1 février 2026 à 09:31 (Europe/Paris)

- **Identifiant :** `1943`
- **Lien :** https://forumdomotique.com/forums/topic/729-home-assistant-automatisation-cam%C3%A9ra-sonoff-vers-zbminir2-ne-fonctionne-pas-avec-la-condition-coucher-du-soleil/#findComment-1943

Super cool philou83,

**Augmente la sensibilité de détection**

Dans eWeLink, cherche l’option “Sensibilité de détection” (ou “Detection Sensitivity”). Mets-la sur “High” si ce n’est pas déjà le cas. Des utilisateurs rapportent que sur Low/Medium, la détection nocturne est trop conservative pour éviter les faux positifs (comme des insectes attirés par l’IR).

Vérifie aussi la “Zone de détection” : Dessine une zone plus large ou sans restriction pour tester.

Certains disent que les zones ne fonctionnent pas toujours bien sur ce modèle

---
