---
title: "topic196 original"
description: "TITLE: 📆 [Intégration] Date Countdown – Suivi d’événements personnels dans Home Assistant Date Countdown est une intégration personnalisée pour Home…"
image: /assets/images/og-default.png
date: 2026-11-20
sitemap: false
robots: noindex, nofollow
---
{% raw %}
TITLE: 📆 [Intégration] Date Countdown – Suivi d’événements personnels dans Home Assistant

📆 Date Countdown

Date Countdown est une intégration personnalisée pour Home Assistant qui permet de suivre les jours restants avant des événements personnels tels que : anniversaires, anniversaires de mariage, promotions, mémoriaux ou événements spéciaux.

🧠 Pourquoi cette intégration ?

Je voulais initialement utiliser le calendrier intégré de Home Assistant pour suivre mes événements importants. Cependant, celui-ci ne permet pas d’associer des classes ou types spécifiques à chaque événement (comme un anniversaire, un décès ou une promotion). Il m’a donc paru plus utile de créer une intégration dédiée avec une logique adaptée à chaque type d’événement.

Entièrement configurable via l’interface graphique, aucun YAML requis. Les capteurs sont automatiquement créés pour une utilisation dans vos dashboards Lovelace, automatisations, notifications ou alertes.

✨ Fonctionnalités

✅ Interface graphique pour ajouter, modifier ou supprimer des événements

📅 Types d’événements :
- 🎂 Anniversaire
- 💍 Anniversaire de mariage (avec intitulés des noces)
- 🕯️ Mémorial (âge qu’aurait eu la personne, années depuis le décès)
- 🏆 Promotion
- 🌟 Événement spécial

⚙️ Capteurs automatiques :
- État = nombre de jours restants
- Attributs : type, date, prénom, années, intitulé des noces, etc.

🎨 Icônes dynamiques selon le type
🇫🇷 Interface et traduction en français
🔔 Prêt pour Lovelace, automatisations, TTS, notifications

🧱 Prérequis
- Home Assistant >= 2024.6.0
- HACS installé

⚙️ Installation via HACS
1. Ouvrez HACS > Intégrations
2. Cliquez sur ⋮ > Dépôt personnalisé
3. Ajoutez ce dépôt : https://github.com/XAV59213/date-countdown
4. Type : Intégration
5. Installez Date Countdown
6. Redémarrez Home Assistant
7. Allez dans Paramètres > Appareils & Services > Ajouter une intégration
8. Recherchez Date Countdown

🔧 Configuration
➕ Ajouter un événement
- Type : sélectionnez parmi les 5 types disponibles
- Nom (obligatoire), Prénom (optionnel)
- Date : JJ/MM/AAAA
- Pour les mémoriaux : date de décès (optionnelle)

🔁 Modifier ou supprimer
- Dans l’intégration : ⋮ > Options
- Choisissez l’action souhaitée : ajouter, modifier ou supprimer un événement en cour de codage pour l'instant il faut juste ajouter une entrée

🛰️ Capteurs générés
Format :

sensor.<type>_<nom>_<date>

Exemple :

sensor.memorial_jean_01011950:
  state: 15
  attributes:
    friendly_name: "Jean - Mémorial"
    first_name: "Jean"
    event_type: "memorial"
    event_date: "01/01/1950"
    years: 76
    death_date: "15/06/2000"
    age_if_alive: 75
    years_since_death: 25

🖼️ Exemple Lovelace (mémoriaux à venir)
type: markdown
content: |
  ##  Mémoriaux à venir
  {% set ns = namespace(events=[]) %}
  {% for entity in states.sensor if entity.entity_id.endswith('memorial') %}
    {% if (entity.state | int(0)) > 0 %}
      {% set ns.events = ns.events + [entity] %}
    {% endif %}
  {% endfor %}
  {% for e in ns.events | sort(attribute='state') | slice(2) %}
  - **{{ state_attr(e.entity_id, 'friendly_name') }}** : {{ e.state }} jours
    - Âge au prochain anniversaire : {{ state_attr(e.entity_id, 'years') }} ans
    - Âge s’il était en vie : {{ state_attr(e.entity_id, 'age_if_alive') }}
    {% if state_attr(e.entity_id, 'death_date') %}
    - Décès : {{ state_attr(e.entity_id, 'death_date') }} ({{ state_attr(e.entity_id, 'years_since_death') }} ans)
    {% endif %}
  {% endfor %}

🔔 Exemple d’automatisation
automation:
  - alias: "Rappel mémorial 7 jours avant"
    trigger:
      platform: numeric_state
      entity_id: sensor.memorial_jean_01011950
      value: 7
    action:
      service: notify.notify
      data:
        message: >
           Dans 7 jours : anniversaire de {{ state_attr('sensor.memorial_jean_01011950', 'friendly_name') }}.
          Âge s’il était en vie : {{ state_attr('sensor.memorial_jean_01011950', 'age_if_alive') }} ans.

🛠️ Dépannage
Les capteurs n’apparaissent pas ?
- Vérifiez que les dates sont bien au format JJ/MM/AAAA
- Redémarrez Home Assistant après ajout ou suppression d’événements

Problème avec les mémoriaux ?
- death_date : format JJ/MM/AAAA
- Vérifiez les attributs dans Développeur > États

Activer les logs de debug
logger:
  default: info
  logs:
    custom_components.date_countdown: debug

📁 Structure technique
Table Fichier / Rôle :
__init__.py : Initialisation du composant
config_flow.py : Flux de configuration UI
sensor.py : Création et mise à jour des capteurs
const.py : Types, formats, intitulés, noces
translations/fr.json : Traduction en français
manifest.json : Métadonnées HACS

👨‍💻 Crédits
Auteur : @XAV59213
Licence : MIT
Dépôt : https://github.com/XAV59213/date_countdown

📢 Support
💬 Pour toute question, bug ou suggestion :
➡️ Créer une issue sur GitHub (https://github.com/XAV59213/date-countdown/issues)

Modifié 7 juin 2025 par XAV59213

[Image in original: //cdn.forumdomotique.com/monthly_2025_06/Capturedcrandu2025-06-0718-23-28.png.4b1a6b676f20ca5951215c474910dde4.png]
{% endraw %}
