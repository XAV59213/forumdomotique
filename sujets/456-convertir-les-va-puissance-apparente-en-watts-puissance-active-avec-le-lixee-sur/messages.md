---
title: "Convertir les VA (Puissance apparente) en Watts (Puissance active) avec le Lixee sur Home Assistant"
---

{% raw %}
# Convertir les VA (Puissance apparente) en Watts (Puissance active) avec le Lixee sur Home Assistant

- **Catégorie :** [Projets et Personnalisations](https://forumdomotique.com/forums/12-projets-et-personnalisations/)
- **Sujet :** https://forumdomotique.com/forums/topic/456-convertir-les-va-puissance-apparente-en-watts-puissance-active-avec-le-lixee-sur-home-assistant/
- **Auteur du premier message du sujet :** XAV59213
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 21 octobre 2025 à 15:45 (Europe/Paris)

---

## Message 1 — 21 octobre 2025 à 15:45 (Europe/Paris)

- **Identifiant :** `1077`
- **Lien :** https://forumdomotique.com/forums/topic/456-convertir-les-va-puissance-apparente-en-watts-puissance-active-avec-le-lixee-sur-home-assistant/#findComment-1077

Le module **Lixee** (via le capteur sensor.linky_papp) te donne la **puissance apparente en VA**.

Mais dans les dashboards Énergie, on veut des **Watts (puissance active)**.

Voici comment créer un **capteur template** qui estime les Watts à partir des VA, **directement dans l’interface (UI)**.

> **Note** : On applique un facteur de **0.9** (cos φ ≈ 0.9), typique pour un logement résidentiel. Tu peux ajuster selon ton installation.

---

## 📌 **Étape 1 : Accéder aux Aides (Helpers)**

1. Va dans **Paramètres** → **Appareils et services**

![Capture d’écran du 2025-10-21 15-15-02.png](images/Capturedcrandu2025-10-2115-15-02.png)![Capture d’écran du 2025-10-21 15-15-14.png](images/Capturedcrandu2025-10-2115-15-14.png)

2. Clique sur l’onglet **Entrée** (en haut à droite)

![Capture d’écran du 2025-10-21 15-16-03.png](images/Capturedcrandu2025-10-2115-16-03.png)

3. Clique sur **+ Créer une Entrée**

![Capture d’écran du 2025-10-21 15-16-26.png](images/Capturedcrandu2025-10-2115-16-26.png)

---

## 📌 **Étape 2 : Choisir le type de capteur**

1. Sélectionne **Modèle (Template)**

![Capture d’écran du 2025-10-21 15-16-45.png](images/Capturedcrandu2025-10-2115-16-45.png)

1. Puis **Capteur (Sensor)**

![Capture d’écran du 2025-10-21 15-16-58.png](images/Capturedcrandu2025-10-2115-16-58.png)

---

## 📌 **Étape 3 : Configurer le capteur**

Remplis les champs comme suit :

> | Champ | Valeur |
> | --- | --- |
> | **Nom** | `Puissance active Linky` |
> | **Icône** | `mdi:lightning-bolt` *(optionnel)* |
> | **Classe d’appareil** | `Puissance` (Power) |
> | **Classe d’état** | `Mesure` (Measurement) |
> | **Unité de mesure** | `W` |
> | **Modèle de valeur d’état** | ```yaml {% set papp = states('sensor.linky_papp') | float(default=0) %} {{ (papp * 0.9) | round(0) if papp > 0 else 0 }} ``` |

Et ajoute le code dans état:

```yaml
{% set papp = states('sensor.linky_papp') | float(default=0) %}
{{ (papp * 0.9) | round(0) if papp > 0 else 0 }}
```

![Capture d’écran du 2025-10-21 15-39-09.png](images/Capturedcrandu2025-10-2115-39-09.png)

## 🎉 **Et voilà !**

Tu as maintenant un capteur **prêt pour le dashboard Énergie** de Home Assistant. N’oublie pas de l’ajouter dans ta vue Énergie pour suivre ta conso en Watts !

![Capture d’écran du 2025-10-21 15-43-55.png](images/Capturedcrandu2025-10-2115-43-55.png)

Tu veux la version YAML ? Ajoute ça dans configuration.yaml ou via Fichier de configuration :

```yaml
template:
  - sensor:
      - name: "Puissance active Linky approx"
        unit_of_measurement: "W"
        device_class: power
        state_class: measurement
        icon: mdi:lightning-bolt
        state: >
          {{ (states('sensor.linky_papp') | float(0) * 0.9) | round(0) }}
```

Besoin d’aide ? Pose ta question dans les commentaires !

---
{% endraw %}
