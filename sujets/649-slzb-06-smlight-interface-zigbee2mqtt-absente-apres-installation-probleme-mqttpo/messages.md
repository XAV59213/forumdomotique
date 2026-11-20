---
title: "SLZB-06 SMLight: interface Zigbee2MQTT absente après installation, problème MQTT/port série"
---

# SLZB-06 SMLight: interface Zigbee2MQTT absente après installation, problème MQTT/port série

- **Catégorie :** [Dépannage et Support Technique](https://forumdomotique.com/forums/19-d%C3%A9pannage-et-support-technique/)
- **Sujet :** https://forumdomotique.com/forums/topic/649-slzb-06-smlight-interface-zigbee2mqtt-absente-apr%C3%A8s-installation-probl%C3%A8me-mqttport-s%C3%A9rie/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 3 janvier 2026 à 11:07 (Europe/Paris)

---

## Message 1 — 3 janvier 2026 à 11:07 (Europe/Paris)

- **Identifiant :** `1667`
- **Lien :** https://forumdomotique.com/forums/topic/649-slzb-06-smlight-interface-zigbee2mqtt-absente-apr%C3%A8s-installation-probl%C3%A8me-mqttport-s%C3%A9rie/#findComment-1667

Salut [@vipa](https://forumdomotique.com/profile/1012-vipa/)

Voici un petit récapitulatif clair des problèmes observés dans vos logs Zigbee2MQTT :

1.  **Problème MQTT (au début)**

•  Erreur : getaddrinfo ENOTFOUND core-mosquitto

•  Signification : Zigbee2MQTT ne trouvait pas le broker MQTT (Mosquitto).

•  Statut : Ce problème semble résolu depuis, car une tentative a réussi à se connecter.

2.  **Problème principal actuel : communication avec le coordinateur SLZB-06**

•  Erreur : SRSP - SYS - ping after 6000ms

•  Signification : Zigbee2MQTT arrive à ouvrir la connexion TCP vers le SLZB-06 (slzb-06.local:6638), mais le coordinateur ne répond pas au premier « ping » (timeout de 6 secondes).

•  Conséquence : Zigbee2MQTT ne peut pas démarrer correctement et s’arrête.

3.  **Problèmes secondaires**

•  Erreur Node.js « write after end » : juste une conséquence des arrêts brutaux, pas la cause.

•  Version Zigbee2MQTT très ancienne (2.7.2) et firmware radio du SLZB-06 daté (20221226) → stabilité moindre.

**En résumé** :

Le cœur du problème actuel est que le SLZB-06 ne répond plus correctement à Zigbee2MQTT, probablement à cause d’un gel, d’un problème réseau temporaire, d’un firmware obsolète ou d’une résolution de nom .local instable.

La solution la plus efficace : redémarrer/mettre à jour le firmware du SLZB-06 et passer à une IP fixe dans la configuration.

<https://forumdomotique.com/tests/dongles-passerelles/test-slzb-mr4u-coordinateur-zigbee-thread-matter/?do=embed>

---
