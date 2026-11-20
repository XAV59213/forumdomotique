---
title: "Présentation de la Gestion de Code dans Home Assistant"
description: "Home Assistant est une plateforme puissante pour l'automatisation domestique. Pour maintenir une configuration claire et modulaire, j'organise mon code en…"
image: /assets/images/og-default.png
date: 2025-04-26
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/67-pr%C3%A9sentation-de-la-gestion-de-code-dans-home-assistant/">Lire et commenter sur Forum Domotique</a></p>

# Présentation de la Gestion de Code dans Home Assistant

- **Catégorie :** [Tutoriels, Guides & Astuces des Membres](https://forumdomotique.com/forums/87-tutoriels-guides-astuces-des-membres/)
- **Sujet :** https://forumdomotique.com/forums/topic/67-pr%C3%A9sentation-de-la-gestion-de-code-dans-home-assistant/
- **Auteur du premier message du sujet :** XAV59213
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 26 avril 2025 à 10:34 (Europe/Paris)

---

## Message 1 — 26 avril 2025 à 10:34 (Europe/Paris)

- **Identifiant :** `118`
- **Lien :** https://forumdomotique.com/forums/topic/67-pr%C3%A9sentation-de-la-gestion-de-code-dans-home-assistant/#findComment-118

## 1. Introduction

Home Assistant est une plateforme puissante pour l'automatisation domestique. Pour maintenir une configuration claire et modulaire, j'organise mon code en plusieurs fichiers YAML inclus dans le fichier principal configuration.yaml. Cette approche améliore la lisibilité, la maintenance et la scalabilité.

## 2. Structure du Fichier Principal (configuration.yaml)

Le fichier configuration.yaml sert de point d'entrée et inclut toutes les configurations nécessaires via des fichiers externes. Voici un aperçu de sa structure :

```plaintext
homeassistant:
  packages: !include_dir_named packages
# Charge les intégrations par défaut
default_config:

# Configuration des panneaux personnalisés pour la barre latérale
panel_custom: !include panel_custom.yaml

# Automatisations, scripts et scènes
automation: !include automations.yaml
script: !include scripts.yaml
scene: !include scenes.yaml

# Intégrations spécifiques
freebox_player: !include freebox_player.yaml
wake_on_lan: !include wake_on_lan.yaml
lovelace: !include lovelace.yaml
notify: !include notify.yaml

# Entités et capteurs
switch: !include switch.yaml
climate: !include climate.yaml
powercalc: !include powercalc.yaml
binary_sensor: !include binary_sensor.yaml
sensor: !include sensor.yaml
template: !include template.yaml

# Configurations avancées
ffmpeg: !include ffmpeg.yaml
frontend: !include frontend.yaml
http: !include http.yaml
```

### Explication :

- **packages** : Inclut des fichiers de configuration pour des intégrations complexes (par exemple, des intégrations tierces).
- **default_config** : Charge les intégrations de base de Home Assistant.
- **Fichiers inclus** : Chaque fichier YAML gère une catégorie spécifique (ex. : climate.yaml pour les thermostats, switch.yaml pour les interrupteurs).
- **Organisation** : Les fichiers sont séparés par type d’entité ou fonctionnalité, facilitant la recherche et la modification.

## 3. Exemple de Fichier : climate.yaml

Le fichier climate.yaml contient la configuration des entités de type climate, utilisées pour contrôler les thermostats ou climatiseurs. Voici un exemple de structure pour climate.yaml :

```plaintext
# climate.yaml
climate:
  - platform: generic_thermostat
    name: Thermostat Salon
    heater: switch.salon_heater
    target_sensor: sensor.salon_temperature
    min_temp: 15
    max_temp: 30
    target_temp: 20
    ac_mode: false
    cold_tolerance: 0.3
    hot_tolerance: 0.3
    initial_hvac_mode: "heat"

  - platform: generic_thermostat
    name: Thermostat Chambre
    heater: switch.chambre_heater
    target_sensor: sensor.chambre_temperature
    min_temp: 15
    max_temp: 28
    target_temp: 19
    ac_mode: false
    cold_tolerance: 0.5
    hot_tolerance: 0.5
    initial_hvac_mode: "heat"
```

### Explication :

- **Plateforme** : Utilise generic_thermostat pour créer un thermostat virtuel basé sur un interrupteur (heater) et un capteur de température (target_sensor).
- **Paramètres** :

- name : Nom de l’entité dans Home Assistant.
- min_temp/max_temp : Plage de température autorisée.
- target_temp : Température cible par défaut.
- cold_tolerance/hot_tolerance : Marges de tolérance pour éviter des cycles trop fréquents.
- initial_hvac_mode : Mode initial (ici, chauffage).

## 4. Avantages de Cette Organisation

- **Modularité** : Chaque fichier gère un aspect spécifique, facilitant les modifications.
- **Clarté** : La séparation par type d’entité réduit les erreurs.
- **Réutilisabilité** : Les fichiers comme climate.yaml peuvent être facilement adaptés pour de nouveaux appareils.
- **Maintenance** : Les mises à jour ou ajouts se font dans des fichiers dédiés, sans toucher au fichier principal.

## 5. Étapes pour Ajouter une Nouvelle Entité

1. Identifier le type d’entité (ex. : climate pour un thermostat).
2. Créer ou modifier le fichier correspondant (ex. : climate.yaml).
3. Ajouter la configuration spécifique (comme ci-dessus pour generic_thermostat).
4. Vérifier la configuration dans Home Assistant (via l’outil de validation).
5. Redémarrer Home Assistant pour appliquer les changements.

## 6. Exemple d’Intégration dans Lovelace

Pour afficher les entités climate dans l’interface utilisateur, j’utilise une carte dans lovelace.yaml :

```plaintext
# lovelace.yaml (extrait)
views:
  - title: Maison
    cards:
      - type: thermostat
        entity: climate.thermostat_salon
      - type: thermostat
        entity: climate.thermostat_chambre
```

Cela crée une interface utilisateur intuitive pour contrôler les thermostats.

## 7. Conclusion

En structurant ma configuration Home Assistant avec des fichiers YAML séparés, je maintiens un système clair, évolutif et facile à gérer. Le fichier climate.yaml illustre comment configurer des entités spécifiques, tandis que configuration.yaml centralise toutes les inclusions. Cette méthode est idéale pour les installations complexes avec de nombreuses intégrations.

---
