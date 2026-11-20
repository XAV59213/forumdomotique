---
title: "Fini les pannes de piles sur Home Assistant ! Le système PARFAIT"
description: "Tu peux laisser to: vide si tu veux supprimer le mot \"Batterie\" Sur le code que tu a partagé il y a encore Pile présent"
image: /assets/images/og-default.png
date: 2025-10-21
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/339-fini-les-pannes-de-piles-sur-home-assistant-le-syst%C3%A8me-parfait/">Lire et commenter sur Forum Domotique</a></p>

# Fini les pannes de piles sur Home Assistant ! Le système PARFAIT

- **Catégorie :** [Dépannage et Support Technique](https://forumdomotique.com/forums/19-d%C3%A9pannage-et-support-technique/)
- **Sujet :** https://forumdomotique.com/forums/topic/339-fini-les-pannes-de-piles-sur-home-assistant-le-syst%C3%A8me-parfait/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 21 octobre 2025 à 16:52 (Europe/Paris)
- **Dernier message de XAV59213 :** 19 novembre 2025 à 08:29 (Europe/Paris)

---

## Message 1 — 21 octobre 2025 à 16:52 (Europe/Paris)

- **Identifiant :** `1078`
- **Lien :** https://forumdomotique.com/forums/topic/339-fini-les-pannes-de-piles-sur-home-assistant-le-syst%C3%A8me-parfait/#findComment-1078

Bonjour [@DELEPLANQUE](https://forumdomotique.com/profile/326-deleplanque/)

Voici le code bien structurer :

```yaml
type: custom:battery-state-card
secondary_info: "{last_changed}"

filter:
  include:
    - name: attributes.device_class
      value: battery
  exclude:
    - name: entity_id
      value: sensor.one_bernard*
    - name: entity_id
      value: sensor.bah_w09_battery_level
    - name: entity_id
      value: sensor.sonoff_zbminil2_batterie
    - name: entity_id
      value: sensor.sonoff_zbminil2_batterie_2
    - name: entity_id
      value: sensor.sonoff_snzb_02d_batterie
    - name: entity_id
      value: sensor.sonoff_zbminil2_batterie_3
    - name: entity_id
      value: sensor.lumiere_exterieure_buanderie_batterie

sort:
  by: state

bulk_rename:
  - from: Batterie
    to: Pile
```

Tu peux laisser to: vide si tu veux supprimer le mot "Batterie".

By et From n'a pas de majuscule

---

## Message 2 — 19 novembre 2025 à 08:29 (Europe/Paris)

- **Identifiant :** `1260`
- **Lien :** https://forumdomotique.com/forums/topic/339-fini-les-pannes-de-piles-sur-home-assistant-le-syst%C3%A8me-parfait/#findComment-1260

Salut [@DELEPLANQUE](https://forumdomotique.com/profile/326-deleplanque/) ,

Sur le code que tu a partagé il y a encore Pile présent

```yaml
to: Pile
```

Retire Pile

```yaml
to: 
```

---
