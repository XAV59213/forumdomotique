---
title: "smart switch  4ch"
description: "D’abord, merci pour ta question, et oui, tu es au bon endroit pour discuter de ça on va essayer de trouver une solution pour ton setup avec Google Home et…"
image: /assets/images/og-default.png
date: 2025-11-19
---
{% raw %}
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/506-smart-switch-4ch/">Lire et commenter sur Forum Domotique</a></p>

# smart switch  4ch

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/506-smart-switch-4ch/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 19 novembre 2025 à 09:44 (Europe/Paris)
- **Dernier message de XAV59213 :** 19 novembre 2025 à 18:59 (Europe/Paris)

---

## Message 1 — 19 novembre 2025 à 09:44 (Europe/Paris)

- **Identifiant :** `1263`
- **Lien :** https://forumdomotique.com/forums/topic/506-smart-switch-4ch/#findComment-1263

Bonjour [@titi25520](https://forumdomotique.com/profile/216-titi25520/) et bienvenue

D’abord, merci pour ta question, et oui, tu es au bon endroit pour discuter de ça on va essayer de trouver une solution pour ton setup avec Google Home et tes smart switches (je suppose que ce sont des interrupteurs intelligents compatibles comme ceux de Tuya, Sonoff ou similaires, reliés à Google Home).

Ton objectif est clair : quand tu dis “allume la lampe 1” (par exemple), Google Home allume celle-là et éteint automatiquement toutes les autres, pour qu’il n’y en ait qu’une allumée à la fois. C’est une automatisation sympa pour un mode “sélectif”.

**Solution avec Google Home seul (via les Routines)**

Google Home permet de créer des “Routines” qui sont déclenchées par une commande vocale personnalisée. Tu peux en faire une pour chaque lampe, où la commande allume la lampe cible et éteint les autres. C’est natif, pas besoin d’app tierce, mais si tu as beaucoup de lampes, ça veut dire créer plusieurs routines (une par lampe). Voici comment faire étape par étape :

1.  Ouvre l’application **Google Home** sur ton téléphone (Android ou iOS).

2.  Va dans l’onglet **Automatisations** (ou “Routines” selon la version de l’app – c’est sous l’icône de la maison ou dans les paramètres).

3.  Appuie sur **Ajouter** ou **+** pour créer une nouvelle routine, et choisis **Routine personnelle** (car c’est pour toi).

4.  Donne un nom à la routine, par exemple “Allumer Lampe 1”.

5.  Ajoute un **déclencheur (starter)** :

•  Sélectionne “Quand je dis à Google Assistant”.

•  Entre la commande vocale exacte, comme “allume la lampe 1” (ou ce que tu utilises habituellement). Tu peux ajouter des variantes comme “active la lampe 1” pour plus de flexibilité.

6.  Ajoute les **actions** :

•  Première action : Allume la lampe cible (sélectionne ton smart switch/relais nommé “lampe 1” et choisis “Allumer”).

•  Ensuite, pour chaque autre lampe : Sélectionne l’appareil (ex. “lampe 2”, “lampe 3”, etc.) et choisis “Éteindre”.

•  Répète pour toutes les autres lampes. Malheureusement, il n’y a pas d’option automatique pour “éteindre toutes les autres” en un clic, donc tu dois les lister une par une .

7.  Enregistre la routine en appuyant sur **Sauvegarder**.

Répète ces étapes pour chaque lampe (ex. une routine pour “allume la lampe 2” qui allume lampe 2 et éteint les 1, 3, etc.).

**Teste ça** : Dis “OK Google, allume la lampe 1” – ça devrait exécuter la routine au lieu de juste allumer la lampe seule. Si la commande vocale est trop proche de la commande native de Google, ça pourrait interférer, donc essaie des phrases uniques comme “mode lampe 1”.

**Limites** : Si tu as des dizaines de lampes, c’est un peu lourd à gérer. Les routines dépendent d’une connexion internet stable, et Google Home n’est pas super flexible pour des logiques conditionnelles avancées (comme détecter si les autres sont allumées).

**Alternative plus simple : Utiliser Home Assistant**

Si tu veux une solution plus puissante et centralisée, je te recommande **Home Assistant** (c’est gratuit et open-source). C’est un hub domotique qui s’intègre parfaitement avec Google Home et tes smart switches. Tu peux créer une seule automatisation qui écoute toutes les commandes et gère la logique “une seule allumée”.

•  **Pourquoi c’est mieux ?** : Une automatisation unique qui vérifie l’état des lampes et éteint les autres automatiquement, sans routines multiples.

•  **Comment commencer** :

1.  Avoir Home Assistant

2.  Intègre tes smart switches (la plupart sont compatibles via integrations comme Tuya ou MQTT).

3.  Intègre Google Home/Assistant pour que les commandes vocales passent par Home Assistant.

4.  Crée une automatisation dans Home Assistant :

•  Déclencheur : Quand une lampe est allumée (via événement ou état).

•  Condition : Vérifie si c’est via commande vocale ou manuelle.

•  Action : Éteindre toutes les autres lampes du groupe.

Exemple basique en YAML (le langage de Home Assistant) :

```yaml
automation:
  - alias: Une seule lampe allumée
    trigger:
      - platform: state
        entity_id: switch.lampe_1, switch.lampe_2, switch.lampe_3  # Liste tes entités
        to: 'on'
    action:
      - service: homeassistant.turn_off
        entity_id: 
          - switch.lampe_1
          - switch.lampe_2
          - switch.lampe_3
        data:
          exclude: "{{ trigger.entity_id }}"  # Éteint tout sauf celle qui vient d'être allumée
```

Ça gère tout en une fois ! Si tu n’as pas Home Assistant, c’est facile à installer, et tu peux garder Google Home pour les commandes vocales.

Si tu me donnes plus de détails sur tes smart switches (marque/modèle) ou si tu as déjà Home Assistant, je peux affiner les conseils.

N’hésite pas? 😊

---

## Message 2 — 19 novembre 2025 à 18:59 (Europe/Paris)

- **Identifiant :** `1271`
- **Lien :** https://forumdomotique.com/forums/topic/506-smart-switch-4ch/#findComment-1271

Salut [@titi25520](https://forumdomotique.com/profile/216-titi25520/),

Tout dépend de ton budget, mais en gros, tu as 4 possibilités principales pour installer et utiliser Home Assistant (HA) comme hub central compatible avec tes smart switches. Je vais te détailler chacune pour que tu puisses choisir sans te planter. HA est gratuit et open-source, donc l’investissement est surtout sur le hardware.

#### 1. Acheter le hub officiel : Home Assistant Green

• C’est la solution la plus simple et “plug-and-play”. C’est un petit boîtier pré-installé avec HA, fabriqué par l’équipe officielle (Nabu Casa).

[@Jack](https://forumdomotique.com/profile/1-jack/) a fait le test

<https://forumdomotique.com/tests/box-domotiques/home-assistant-green-test/?do=embed>

• Avantages : Facile à installer (branche-le et configure via l’app), fiable, avec des mises à jour automatiques. Il supporte Zigbee et Z-Wave nativement (avec un dongle optionnel).

• Inconvénients : Coûte environ 100-150 € (vérifie les prix actuels sur le site officiel).

• Où l’acheter : Sur le site de Home Assistant ([home-assistant.io](https://home-assistant.io)) ou des revendeurs comme [Domadoo](https://www.domadoo.fr/fr/produits-compatibles-home-assistant/7046-nabu-casa-box-domotique-home-assistant-green-0860011789703.html).C’est idéal si tu veux zéro prise de tête.

#### 2. Installer sur un PC (ou un mini-PC comme un NUC)

• Utilise un ordinateur que tu as déjà (même un vieux) ou achète un mini-PC bon marché (genre Intel NUC ou équivalent pour 100-200 €).

• Comment faire : Télécharge Home Assistant OS (HAOS) sur une clé USB, installe-le comme un système d’exploitation. Tu peux aussi l’installer en container (Docker) si tu as déjà un OS comme Linux/Windows.

• Avantages : Puissant pour gérer beaucoup d’appareils, scalable, et gratuit si tu réutilises du matos.

• Inconvénients : Consomme plus d’énergie qu’un petit hub, et nécessite un peu de config initiale.

• Budget : 0 € si tu as un PC, sinon 50-300 € pour du hardware dédié.

#### 3. Installer sur un Raspberry Pi

• La solution la plus populaire et DIY. Prends un Raspberry Pi 4 ou 5 (le 5 est plus performant pour HA).

J’ai fait un tuto sur le Raspberry

Va directement à la section : **Installation du Logiciel (Home Assistant en 10 min**

<https://forumdomotique.com/forums/topic/402-cr%C3%A9er-sa-box-domotique-parfaite-de-limpression-3d-%C3%A0-la-configuration-home-assistant/?do=embed&comment=892&embedComment=892&embedDo=findComment#comment-892>

• Comment faire : Télécharge l’image HAOS pour Raspberry Pi, grave-la sur une carte microSD, et boot. Ajoute un boîtier et une alim.

• Avantages : Compact, économe en énergie, communauté énorme avec tutos partout. Parfait pour débuter.

• Inconvénients : Moins puissant qu’un PC pour des setups complexes, et les stocks de Pi peuvent varier.

• Budget : Environ 50-100 € pour un Pi 4/5 + accessoires. Achète sur [Raspberrypi.com](https://Raspberrypi.com) ou Amazon.

#### 4. Installer sur une Freebox (en VM)

Je peux te faire un tuto si besoin

• Si tu as une Freebox Delta ou Ultra (les modèles qui supportent les VM), tu peux installer HA directement en machine virtuelle dessus.

• Comment faire : Via l’interface Freebox, crée une VM, télécharge l’image HAOS (format qcow2 ou similaire), et alloue des ressources (CPU/RAM/stockage). Il y a des guides officiels sur le forum Free ou la doc HA.

• Avantages : Pas besoin d’acheter du hardware supplémentaire, intégré à ton réseau existant, et gratuit.

• Inconvénients : Limité aux abonnés Free avec une box compatible, et performances dépendent de la box (pas idéal pour des setups lourds).

• Budget : 0 € si tu as déjà la Freebox.

Si besoin d’aide pour les configurations et l’installation n’hésite pas ✌️

---
{% endraw %}
