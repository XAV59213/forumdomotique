---
title: "Nouveau sur le forum"
---

# Nouveau sur le forum

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/581-nouveau-sur-le-forum/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 3 décembre 2025 à 18:57 (Europe/Paris)

---

## Message 1 — 3 décembre 2025 à 18:57 (Europe/Paris)

- **Identifiant :** `1467`
- **Lien :** https://forumdomotique.com/forums/topic/581-nouveau-sur-le-forum/#findComment-1467

Bienvenue sur le forum [@Bergphi](https://forumdomotique.com/profile/787-bergphi/) !

Ton setup a l’air sympa et bien parti, avec un mélange de marques qui fonctionne déjà pas mal. Pour ton problème de boucle avec la caméra Tuya et le projecteur (où l’extinction déclenche une nouvelle détection)

les changements de luminosité trompent souvent les capteurs de mouvement des caméras.

En gros tu doit adapter cette automatisation:

```yaml
automation:
  - id: 'automatisation_projecteur_sur_detection'
    alias: Allumer projecteur sur détection et éteindre après 2 min
    description: Allume le projecteur sur détection de mouvement, attend 2 min, éteint, et ignore les fausses détections pendant 10 sec.
    trigger:
      - platform: state
        entity_id: binary_sensor.ta_camera_motion  # Remplace par ton entité de détection
        from: 'off'
        to: 'on'
    condition:
      - condition: state
        entity_id: switch.ton_projecteur  # Remplace par ton entité de projecteur
        state: 'off'  # Seulement si déjà éteint, pour éviter des relances inutiles
    action:
      - service: switch.turn_on  # Ou light.turn_on si c'est une light
        target:
          entity_id: switch.ton_projecteur
      - delay:
          minutes: 2
      - service: switch.turn_off  # Ou light.turn_off
        target:
          entity_id: switch.ton_projecteur
      - delay:
          seconds: 10  # Délai pour ignorer la fausse détection causée par l'extinction
    mode: single  # Important : ignore les nouveaux triggers pendant l'exécution
```

---
