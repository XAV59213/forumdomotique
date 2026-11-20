---
title: "Eleve NUL novice en domotique."
description: "Félicitations te voilà dans le monde de la domotique ! Pas de souci, je vais t’expliquer pas à pas comment mettre en route ton hub Zigbee Tuya filaire…"
image: /assets/images/og-default.png
date: 2025-12-31
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/644-eleve-nul-novice-en-domotique/">Lire et commenter sur Forum Domotique</a></p>

# Eleve NUL novice en domotique.

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/644-eleve-nul-novice-en-domotique/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 31 décembre 2025 à 16:32 (Europe/Paris)
- **Dernier message de XAV59213 :** 24 janvier 2026 à 11:32 (Europe/Paris)

---

## Message 1 — 31 décembre 2025 à 16:32 (Europe/Paris)

- **Identifiant :** `1650`
- **Lien :** https://forumdomotique.com/forums/topic/644-eleve-nul-novice-en-domotique/#findComment-1650

Bonjour [@eleve NUL](https://forumdomotique.com/profile/990-eleve-nul/) !

Félicitations te voilà dans le monde de la domotique !

Pas de souci, je vais t’expliquer pas à pas comment mettre en route ton **hub Zigbee Tuya filaire** (Ethernet), ton **mini capteur de température** et ton **relais commutateur** (switch relay Zigbee). Comme tu es débutant, on va y aller doucement. Tout ça fonctionne avec l’application gratuite **Smart Life** (ou Tuya Smart, c’est la même chose) sur ton Samsung Galaxy S24.

Ton hub est filaire (Ethernet), donc plus stable que les versions WiFi. Il se connecte directement à ta Livebox Fibre via un câble réseau RJ45.

**Étape 1 : Préparation matérielle**

•  Branche le hub Tuya Zigbee :

•  Alimente-le (généralement avec un câble USB fourni, branche sur une prise USB ou adaptateur 5V).

•  Connecte un câble Ethernet de ton hub à un port libre sur ta Livebox Fibre.

•  Les voyants devraient s’allumer. Si un voyant clignote lentement ou rapidement, c’est normal (mode appairage).

**Étape 2 : Télécharge l’application**

•  Sur ton Galaxy S24, va sur le Google Play Store.

•  Cherche “**Smart Life**” (l’icône est bleue avec une maison).

•  Télécharge et installe l’app (c’est gratuit, par Tuya).

•  Ouvre l’app et crée un compte (avec ton email ou numéro de téléphone). Confirme par le code reçu.

**Étape 3 : Ajouter le hub Zigbee à l’app**

1.  Dans l’app Smart Life, appuie sur le “+” en haut à droite (Ajouter un appareil).

2.  Va dans la catégorie “**Gateway Control**” ou “**Passerelle**” (à gauche).

3.  Sélectionne “**Gateway (Zigbee)**” ou “**Zigbee Hub**” (il y a souvent une version “Wired” ou “Filaire/Ethernet”).

4.  L’app te demande de confirmer que le hub est alimenté et connecté en Ethernet.

•  Si le voyant ne clignote pas, appuie longtemps sur le bouton reset du hub (généralement 5-10 secondes) jusqu’à ce qu’un voyant clignote rapidement.

5.  L’app détecte automatiquement le hub (grâce au câble Ethernet, c’est rapide).

6.  Suis les instructions : ça configure le hub.

7.  Une fois ajouté, le hub apparaît dans la liste des appareils (nom comme “Zigbee Gateway”).

**Étape 4 : Ajouter les appareils Zigbee (capteur température et relais)**

Une fois le hub ajouté :

1.  Ouvre la page du hub dans l’app (appuie dessus).

2.  Appuie sur “**Add Subdevice**” ou “**Ajouter un sous-appareil**” ou “**Add Devices**”.

3.  Pour chaque appareil (capteur et relais) :

•  Mets-le en mode appairage : appuie longtemps sur le bouton reset (souvent 5-10 secondes) jusqu’à ce que le voyant clignote rapidement.

•  (Pour le capteur température : il a généralement un petit bouton sur le côté ou derrière.)

•  (Pour le relais commutateur : même chose, bouton reset.)

4.  L’app recherche et ajoute l’appareil automatiquement (ça prend 30-60 secondes).

5.  Donne un nom à chaque (ex: “Capteur Salon”, “Relais Lampe”).

6.  Répète pour l’autre appareil.

**Étape 5 : Tester**

•  Dans l’app, tu vois le capteur : il affiche la température en temps réel.

•  Pour le relais : tu peux l’allumer/éteindre manuellement dans l’app.

•  Tu peux créer des automatisations simples, par exemple : si température < 18°C, allumer le relais (pour chauffer quelque chose).

**Astuces pour débutant**

•  Si ça ne détecte pas : rapproche les appareils du hub pendant l’appairage (Zigbee porte ~10-20m, mais murs réduisent).

•  Mise à jour : l’app te proposera des mises à jour pour le hub et appareils.

•  Compatible Alexa/Google si tu veux commande vocale plus tard.

Si tu bloques à une étape (ex: voyant ne clignote pas, ou app ne trouve pas le hub), dis-moi exactement ce qui se passe (photo du hub si possible !), je t’aiderai plus précisément.

Ça va être super une fois en route ! 🎄 Amuse-toi bien avec tes nouveaux gadgets domotiques. 😊

---

## Message 2 — 24 janvier 2026 à 11:32 (Europe/Paris)

- **Identifiant :** `1872`
- **Lien :** https://forumdomotique.com/forums/topic/644-eleve-nul-novice-en-domotique/#findComment-1872

Oui ton schéma est correct il faut bien respecter le 20 ampères avant ton module

Si tu a un contrat heures creuses et heures pleines il te faudra faire des automatismes pour les créneaux horaires

> **il y a 16 minutes, XAV59213 a dit :**
> Oui ton schéma est correct il faut bien respecter le 20 ampères avant ton module
>
> Si tu a un contrat heures creuses et heures pleines il te faudra faire un automatismes pour les créneaux horaires

Voici un exemple :

```yaml
- id: 'activer_heures_creuses'
  alias: Activer heures creuses
  description: 'Active le helper pendant les heures creuses (12h-14h et 21h-6h)'
  trigger:
  - platform: time
    at: '12:00:00'
  - platform: time
    at: '21:00:00'
  condition: []
  action:
  - service: input_boolean.turn_on
    target:
      entity_id: input_boolean.heures_creuses
    data: {}
  mode: single

- id: 'desactiver_heures_creuses'
  alias: Désactiver heures creuses
  description: 'Désactive le helper pendant les heures pleines'
  trigger:
  - platform: time
    at: '14:00:00'
  - platform: time
    at: '06:00:00'
  condition: []
  action:
  - service: input_boolean.turn_off
    target:
      entity_id: input_boolean.heures_creuses
    data: {}
  mode: single

- id: 'controler_cumulus_heures_creuses'
  alias: Contrôler cumulus en heures creuses
  description: 'Active le cumulus seulement en heures creuses via le helper'
  trigger:
  - platform: state
    entity_id: input_boolean.heures_creuses
  condition: []
  action:
  - choose:
    - conditions:
      - condition: state
        entity_id: input_boolean.heures_creuses
        state: 'on'
      sequence:
      - service: switch.turn_on
        target:
          entity_id: switch.cumulus  # Remplace par ton entity_id réel (ex. : switch.chauffe_eau)
        data: {}
    - conditions:
      - condition: state
        entity_id: input_boolean.heures_creuses
        state: 'off'
      sequence:
      - service: switch.turn_off
        target:
          entity_id: switch.cumulus  # Remplace par ton entity_id réel (ex. : switch.chauffe_eau)
        data: {}
  mode: single
```

---
