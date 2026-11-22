---
title: "SMLight SLZB-06Mg26U ne démarre pas avec Zigbee2MQTT sur Home Assistant (erreur zigbee-herdsman)"
description: "Le problème que tu rencontre semble provenir d’une incompatibilité entre le fichier de sauvegarde du coordinateur Zigbee2MQTT et la nouvelle stack…"
image: /assets/images/vignettes-themes/zigbee.jpg

date: 2026-01-30
cover_alt: "Vignette de rubrique Zigbee — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/726-smlight-slzb-06mg26u-ne-d%C3%A9marre-pas-avec-zigbee2mqtt-sur-home-assistant-erreur-zigbee-herdsman/">Lire et commenter sur Forum Domotique</a></p>

# SMLight SLZB-06Mg26U ne démarre pas avec Zigbee2MQTT sur Home Assistant (erreur zigbee-herdsman)

- **Catégorie :** [Autres marques de matériel domotique](https://forumdomotique.com/forums/59-autres-marques-de-mat%C3%A9riel-domotique/)
- **Sujet :** https://forumdomotique.com/forums/topic/726-smlight-slzb-06mg26u-ne-d%C3%A9marre-pas-avec-zigbee2mqtt-sur-home-assistant-erreur-zigbee-herdsman/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 3
- **Premier message de XAV59213 :** 30 janvier 2026 à 11:28 (Europe/Paris)
- **Dernier message de XAV59213 :** 31 janvier 2026 à 09:19 (Europe/Paris)

---

## Message 1 — 30 janvier 2026 à 11:28 (Europe/Paris)

- **Identifiant :** `1911`
- **Lien :** https://forumdomotique.com/forums/topic/726-smlight-slzb-06mg26u-ne-d%C3%A9marre-pas-avec-zigbee2mqtt-sur-home-assistant-erreur-zigbee-herdsman/#findComment-1911

Salut Laurent59,

Le problème que tu rencontre semble provenir d’une incompatibilité entre le fichier de sauvegarde du coordinateur Zigbee2MQTT et la nouvelle stack EmberZNet utilisée par votre SLZB-06M.

Cela arrive souvent lors du passage d’un coordinateur basé sur Z-Stack (comme le SONOFF, probablement TI) à un basé sur EmberZNet (comme le SMLight SLZB-06M).

**Solution recommandée :**

1.  Accédez au répertoire de données de Zigbee2MQTT via Samba, SSH ou l’explorateur de fichiers de Home Assistant (le chemin est /config/zigbee2mqtt dans votre configuration).

2.  Localisez le fichier coordinator_backup.json (ou coordinator-backup.json selon les versions).

3.  Supprimez-le ou renommez-le (par exemple, en coordinator_backup_old.json) pour éviter que Zigbee2MQTT ne l’utilise.

4.  Redémarrez Zigbee2MQTT.

Cela forcera la création d’une nouvelle sauvegarde compatible avec EmberZNet. Notez que cela pourrait nécessiter de re-pairer certains (ou tous) vos appareils Zigbee, car la migration entre stacks différentes n’est pas toujours fluide et n’est pas officiellement supportée. Cependant, dans certains cas, les appareils rejoignent le réseau sans problème

---

## Message 2 — 31 janvier 2026 à 06:58 (Europe/Paris)

- **Identifiant :** `1920`
- **Lien :** https://forumdomotique.com/forums/topic/726-smlight-slzb-06mg26u-ne-d%C3%A9marre-pas-avec-zigbee2mqtt-sur-home-assistant-erreur-zigbee-herdsman/#findComment-1920

Salut Laurent59,

On avance !!!

l’adresse mqtt://localhost:1883 ne fonctionne souvent pas correctement en raison de la conteneurisation. À la place, utilisez mqtt://core-mosquitto:1883 (ou mqtt://a0d7b954-mosquitto:1883

Et regarde aussi cette erreur base topic dans ta configuration

la ligne base_topic: "base_topic: zigbee2mqtt" qui semble mal formée – elle devrait être simplement base_topic: zigbee2mqtt (sans les guillemets ni le doublon).

Redémarre Zigbee2MQTT, puis Home Assistant

---

## Message 3 — 31 janvier 2026 à 09:19 (Europe/Paris)

- **Identifiant :** `1924`
- **Lien :** https://forumdomotique.com/forums/topic/726-smlight-slzb-06mg26u-ne-d%C3%A9marre-pas-avec-zigbee2mqtt-sur-home-assistant-erreur-zigbee-herdsman/#findComment-1924

Super, ravi que ça ait fonctionné ! 👏

C’était un plaisir d’aider, et ça arrive souvent avec les configs MQTT dans Home Assistant le broker interne comme core-mosquitto est la clé pour éviter les boucles localhost.

Bonne chance pour le ré-appairage des capteurs et relais, ça devrait être rapide maintenant que le coordinateur est up.

Si tu rencontres d’autres soucis (Zigbee, ZHA ou autre), n’hésite pas à demander.

Ah, et pour le code postal : c’est noté🕺✌️

N’oublie pas de clôturer le post 🤩

---
