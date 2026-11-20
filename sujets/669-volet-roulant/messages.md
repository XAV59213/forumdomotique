---
title: "Volet roulant"
---

{% raw %}
# Volet roulant

- **Catégorie :** [Smart Life / Tuya Smart](https://forumdomotique.com/forums/88-smart-life-tuya-smart/)
- **Sujet :** https://forumdomotique.com/forums/topic/669-volet-roulant/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 10 janvier 2026 à 16:22 (Europe/Paris)

---

## Message 1 — 10 janvier 2026 à 16:22 (Europe/Paris)

- **Identifiant :** `1713`
- **Lien :** https://forumdomotique.com/forums/topic/669-volet-roulant/#findComment-1713

Salut [@Tounet](https://forumdomotique.com/profile/1079-tounet/) ,

Sur home assistant ?

**Oui, c'est tout à fait possible et même assez classique** en Home Assistant pour simuler une présence quand on est absent (anti-intrusion).

Il existe plusieurs façons de faire, voici les 2 approches les plus utilisées et les plus simples en 2025/2026 :

### Méthode recommandée n°1 : Trigger time_pattern + delay aléatoire (la plus simple)

```yaml
automation:
  - alias: "Volets - Ouverture aléatoire matin"
    trigger:
      - platform: time_pattern
        hours: "/1"           # toutes les heures
        minutes: "0"          # → toutes les heures pile
        seconds: "0"

    condition:
      - condition: time
        after: "07:30:00"     # début de la plage possible
        before: "09:30:00"    # fin de la plage possible

    action:
      - delay: 
          minutes: "{{ range(0, 61) | random }}"   # 0 à 60 min aléatoire

      - service: cover.open_cover
        target:
          entity_id: cover.votre_volet_salon   # ← à changer !

      - stop: "Ouverture déjà faite aujourd'hui"   # évite plusieurs ouvertures
        if: 
          - "{{ is_state('cover.votre_volet_salon', 'open') }}"

  # ──────────────────────────────────────────────────────────────

  - alias: "Volets - Fermeture aléatoire soir"
    trigger:
      - platform: time_pattern
        hours: "/1"
        minutes: "0"
        seconds: "0"

    condition:
      - condition: time
        after: "17:45:00"
        before: "21:30:00"

    action:
      - delay: 
          minutes: "{{ range(0, 61) | random }}"

      - service: cover.close_cover
        target:
          entity_id: cover.votre_volet_salon

      - stop: "Fermeture déjà faite"
        if: 
          - "{{ is_state('cover.votre_volet_salon', 'closed') }}"
```

### Méthode n°2 : Une seule automation par volet avec trigger time + offset aléatoire (plus propre)

```yaml
automation:
  - alias: "Volet Salon - Ouverture plage 8h-9h30"
    trigger:
      - platform: time
        at: "08:00:00"     # heure de départ

    action:
      - delay:
          minutes: "{{ range(0, 91) | random }}"   # jusqu'à +1h30 max

      - service: cover.open_cover
        target:
          entity_id: cover.salon

  - alias: "Volet Salon - Fermeture plage 18h-21h"
    trigger:
      - platform: time
        at: "18:00:00"

    action:
      - delay:
          minutes: "{{ range(0, 181) | random }}"  # jusqu'à +3h

      - service: cover.close_cover
        target:
          entity_id: cover.salon
```

### Variante encore plus naturelle (la préférée de beaucoup)

Utiliser **deux triggers** (début et fin de plage) + un **random entre 0 et 100%** pour décider si on agit ou pas :

```yaml
- alias: "Volet aléatoire style présence"
  trigger:
    - platform: time
      at: "08:15:00"
    - platform: time
      at: "20:45:00"

  condition: []   # ou mettre une condition absence si tu veux

  action:
    - variables:
        chance: "{{ range(0,101) | random }}"

    - choose:
        - conditions: "{{ chance <= 65 }}"   # 65% de chances d'ouvrir/fermer
          sequence:
            - service: cover.open_cover    # ou close_cover selon le moment
              target:
                entity_id: cover.votre_volet

        - conditions: "{{ chance >= 35 and chance <= 50 }}"   # petite chance de faire l'inverse
          sequence:
            - service: cover.close_cover
```

Bref, tu as le choix ! La méthode 1 (time_pattern + delay random) reste la plus répandue et la plus fiable pour simuler une présence.

Bon paramétrage et surtout... bonne simulation de présence 😉

---
{% endraw %}
