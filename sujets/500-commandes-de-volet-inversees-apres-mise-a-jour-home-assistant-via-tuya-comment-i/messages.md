---
title: "Commandes de volet inversées après mise à jour Home Assistant via Tuya, comment inverser les flèches ↑ et ↓ du tableau de bord ?"
---

{% raw %}
# Commandes de volet inversées après mise à jour Home Assistant via Tuya, comment inverser les flèches ↑ et ↓ du tableau de bord ?

- **Catégorie :** [Dépannage et Support Technique](https://forumdomotique.com/forums/19-d%C3%A9pannage-et-support-technique/)
- **Sujet :** https://forumdomotique.com/forums/topic/500-commandes-de-volet-invers%C3%A9es-apr%C3%A8s-mise-%C3%A0-jour-home-assistant-via-tuya-comment-inverser-les-fl%C3%A8ches-%E2%86%91-et-%E2%86%93-du-tableau-de-bord/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 4
- **Premier message de XAV59213 :** 18 novembre 2025 à 12:37 (Europe/Paris)
- **Dernier message de XAV59213 :** 12 décembre 2025 à 17:32 (Europe/Paris)

---

## Message 1 — 18 novembre 2025 à 12:37 (Europe/Paris)

- **Identifiant :** `1250`
- **Lien :** https://forumdomotique.com/forums/topic/500-commandes-de-volet-invers%C3%A9es-apr%C3%A8s-mise-%C3%A0-jour-home-assistant-via-tuya-comment-inverser-les-fl%C3%A8ches-%E2%86%91-et-%E2%86%93-du-tableau-de-bord/#findComment-1250

Salut [@BièreNard](https://forumdomotique.com/profile/8-bi%C3%A8renard/),

Le problème semble assez courant avec l’intégration Tuya dans Home Assistant, surtout après des mises à jour qui peuvent introduire des changements dans la gestion des entités “cover” (volets roulants). D’après ce que j’ai pu vérifier, plusieurs utilisateurs ont rapporté des inversions similaires de positions ou de commandes pour les volets Tuya, souvent liées à des mises à jour du core HA ou de l’intégration

Inverser uniquement les symboles ↑ et ↓ sur le tableau de bord (sans toucher au comportement sous-jacent) est possible mais compliqué : cela nécessiterait du CSS personnalisé via des thèmes Lovelace ou des mods comme card-mod, ce qui n’est pas trivial et pourrait casser lors de mises à jour. Au lieu de cela, une meilleure approche de contournement est de créer une entité “cover” template qui inverse complètement le comportement du volet original (position, état, et commandes open/close).

Cela corrigera les icônes sur le dashboard (les flèches suivront la logique inversée), et tu pourra ajuster les automatisations en conséquence pour revenir à une logique normale si needed.

Voici comment procéder :

1. Ajoute la configuration dans ta configuration.yaml (ou dans un fichier inclus via !include).

Assure-toi que l’intégration template est activée (elle l’est par défaut si tu a default_config:).

Exemple YAML pour un volet Tuya inversé (remplace cover.votre_volet_tuya par l’ID réel de ton entité volet, visible dans les outils de développement HA) :

```yaml
template:
  - cover:
      - name: "Volet Inversé"
        device_class: shutter  # Pour un volet roulant
        state: >-
          {{ 'open' if is_state('cover.votre_volet_tuya', 'closed') else 'closed' }}
        position: >-
          {{ 100 - state_attr('cover.votre_volet_tuya', 'current_position') | default(0) | int }}
        open_cover:
          - service: cover.close_cover
            target:
              entity_id: cover.votre_volet_tuya
        close_cover:
          - service: cover.open_cover
            target:
              entity_id: cover.votre_volet_tuya
        stop_cover:
          - service: cover.stop_cover
            target:
              entity_id: cover.votre_volet_tuya
        set_cover_position:
          - service: cover.set_cover_position
            target:
              entity_id: cover.votre_volet_tuya
            data:
              position: "{{ 100 - position }}"
```

•  **Explications** :

•  state : Inverse l’état (ouvert → fermé, et vice versa).

•  position : Inverse la position (ex. : 80% devient 20%).

•  open_cover : Appelle la commande “fermer” de l’original pour “ouvrir” le template (et inversement pour close_cover).

•  set_cover_position : Inverse la position demandée avant de l’envoyer.  
Redémarre HA ou recharge les templates pour que l’entité apparaisse.

---

## Message 2 — 18 novembre 2025 à 20:43 (Europe/Paris)

- **Identifiant :** `1255`
- **Lien :** https://forumdomotique.com/forums/topic/500-commandes-de-volet-invers%C3%A9es-apr%C3%A8s-mise-%C3%A0-jour-home-assistant-via-tuya-comment-inverser-les-fl%C3%A8ches-%E2%86%91-et-%E2%86%93-du-tableau-de-bord/#findComment-1255

Salut [@BièreNard](https://forumdomotique.com/profile/8-bi%C3%A8renard/),

Teste ce code, il manquait l’ID, ça devrait fonctionner.

```yaml
# Loads default set of integrations. Do not remove.
default_config:

template:
  - cover:
      - unique_id: volet_rue_inverse_template  # Ajouté pour l'ID unique
        name: "Volet Inversé"
        device_class: shutter # Pour un volet roulant
        state: >-
          {{ 'open' if is_state('cover.volet_rue', 'closed') else 'closed' }}
        position: >-
          {{ 100 - state_attr('cover.volet_rue', 'current_position') | default(0) | int }}
        open_cover:
          - service: cover.close_cover
            target:
              entity_id: cover.volet_rue
        close_cover:
          - service: cover.open_cover
            target:
              entity_id: cover.volet_rue
        stop_cover:
          - service: cover.stop_cover
            target:
              entity_id: cover.volet_rue
        set_cover_position:
          - service: cover.set_cover_position
            target:
              entity_id: cover.volet_rue
            data:
              position: "{{ 100 - position }}"

# Load frontend themes from the themes folder
frontend:
  themes: !include_dir_merge_named themes

automation: !include automations.yaml
script: !include scripts.yaml
scene: !include scenes.yaml
```

---

## Message 3 — 19 novembre 2025 à 06:19 (Europe/Paris)

- **Identifiant :** `1257`
- **Lien :** https://forumdomotique.com/forums/topic/500-commandes-de-volet-invers%C3%A9es-apr%C3%A8s-mise-%C3%A0-jour-home-assistant-via-tuya-comment-inverser-les-fl%C3%A8ches-%E2%86%91-et-%E2%86%93-du-tableau-de-bord/#findComment-1257

C’est toujours un plaisir d’aider😎

---

## Message 4 — 12 décembre 2025 à 17:32 (Europe/Paris)

- **Identifiant :** `1520`
- **Lien :** https://forumdomotique.com/forums/topic/500-commandes-de-volet-invers%C3%A9es-apr%C3%A8s-mise-%C3%A0-jour-home-assistant-via-tuya-comment-inverser-les-fl%C3%A8ches-%E2%86%91-et-%E2%86%93-du-tableau-de-bord/#findComment-1520

Salut [@BièreNard](https://forumdomotique.com/profile/8-bi%C3%A8renard/)

Peux tu tester cette version

```yaml
template:
  - cover:
      - name: "Volet Inversé"
        unique_id: cover_volet_inversed  # optionnel mais recommandé
        device_class: shutter
        icon: mdi:roller-shade

        # État inversé
        state: >
          {% if is_state('cover.votre_volet_tuya', 'closed') %}
            open
          {% elif is_state('cover.votre_volet_tuya', 'open') %}
            closed
          {% else %}
            {{ states('cover.votre_volet_tuya') }}
          {% endif %}

        # Position inversée (0 → 100, 100 → 0)
        position: >
          {% set pos = state_attr('cover.votre_volet_tuya', 'current_position') | default(0) | int %}
          {{ 100 - pos }}

        # Tilt (facultatif, si ton volet gère l'inclinaison des lamelles)
        tilt: >
          {{ state_attr('cover.votre_volet_tuya', 'current_tilt_position') | default(50) | int }}

        # === ACTIONS CORRIGÉES avec "action:" au lieu de "service:" ===
        open_cover:
          - action: cover.close_cover
            target:
              entity_id: cover.votre_volet_tuya

        close_cover:
          - action: cover.open_cover
            target:
              entity_id: cover.votre_volet_tuya

        stop_cover:
          - action: cover.stop_cover
            target:
              entity_id: cover.votre_volet_tuya

        set_cover_position:
          - action: cover.set_cover_position
            target:
              entity_id: cover.votre_volet_tuya
            data:
              position: >-
                {{ 100 - position }}

        # Si ton volet gère les lamelles (tilt)
        set_cover_tilt_position:
          - action: cover.set_cover_tilt_position
            target:
              entity_id: cover.votre_volet_tuya
            data:
              tilt_position: "{{ tilt_position }}"
```

---
{% endraw %}
