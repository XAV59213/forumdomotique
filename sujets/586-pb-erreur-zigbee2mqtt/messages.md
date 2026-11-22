---
title: "Pb erreur Zigbee2MQTT"
description: "Tu as deux réseaux Zigbee qui utilisent exactement les mêmes paramètres (par exemple ZHA + Zigbee2MQTT, ou deux instances Zigbee2MQTT) Du coup…"
image: /assets/images/vignettes-themes/zigbee.jpg

date: 2025-12-05
cover_alt: "Vignette de rubrique Zigbee — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/586-pb-erreur-zigbee2mqtt/">Lire et commenter sur Forum Domotique</a></p>

# Pb erreur Zigbee2MQTT

- **Catégorie :** [MQTT](https://forumdomotique.com/forums/63-mqtt/)
- **Sujet :** https://forumdomotique.com/forums/topic/586-pb-erreur-zigbee2mqtt/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 5
- **Premier message de XAV59213 :** 5 décembre 2025 à 06:59 (Europe/Paris)
- **Dernier message de XAV59213 :** 21 décembre 2025 à 16:07 (Europe/Paris)

---

## Message 1 — 5 décembre 2025 à 06:59 (Europe/Paris)

- **Identifiant :** `1480`
- **Lien :** https://forumdomotique.com/forums/topic/586-pb-erreur-zigbee2mqtt/#findComment-1480

Salut [@TUTU12](https://forumdomotique.com/profile/797-tutu12/) ,

Tu as deux réseaux Zigbee qui utilisent exactement les mêmes paramètres (par exemple ZHA + Zigbee2MQTT, ou deux instances Zigbee2MQTT).

Du coup, Zigbee2MQTT essaie de former ou de rejoindre un réseau Zigbee, mais il détecte qu’un autre réseau avec le même PAN ID et/ou le même Extended PAN ID existe déjà à proximité. Les deux coordinateurs se gênent et aucun des deux ne parvient à créer un réseau stable

Pour tester le bon fonctionnement, suis ce test.

Respecte bien les étapes.

<https://forumdomotique.com/tests/dongles-passerelles/test-slzb-mr4u-coordinateur-zigbee-thread-matter/?do=embed>

---

## Message 2 — 11 décembre 2025 à 19:54 (Europe/Paris)

- **Identifiant :** `1517`
- **Lien :** https://forumdomotique.com/forums/topic/586-pb-erreur-zigbee2mqtt/#findComment-1517

Salut [@TUTU12](https://forumdomotique.com/profile/797-tutu12/) ,

Tu peux m’envoyer :

• Les logs complets de ton Zigbee2MQTT (dans l’add-on → z2mqtt → onglet Log). Le top, c’est de passer en mode debug quelques minutes, de reproduire le bug et de tout copier-coller ici.

• Ton fichier configuration.yaml de Zigbee2MQTT (il est dans /share/zigbee2mqtt/ normalement)

• Et tu tournes avec combien d’instances Zigbee2MQTT en même temps ? Une seule ou plusieurs ?

Avec ça je pourrai t’aider direct

Pour information Zigbee2MQTT c’est la version standard Zigbee2MQTTedge ça la version dev mais ça doit fonctionner le principal c’est de ne pas démarrer le module avant d’avoir configurer le topic il ne doit pas être identique à ta première instance avoir ajouté l ip + port différent et mettre un canal différent pour éviter les conflits logiquement après le démarrage ça doit te demander de valider la configuration tu contrôles si c’est ok et tu valide

---

## Message 3 — 20 décembre 2025 à 12:30 (Europe/Paris)

- **Identifiant :** `1580`
- **Lien :** https://forumdomotique.com/forums/topic/586-pb-erreur-zigbee2mqtt/#findComment-1580

**Salut TUT12,**

Voilà, c'est tout nouveau sur le forum : l'assistance à distance !

J'espère que tu as apprécié l'intervention et que tu es content du résultat.

Je sais que tu es occupé à appairer tes appareils, mais pourras-tu éditer ton premier message (le sujet principal) en ajoutant **[Résolu]** au début du titre, suivi de « via aide à distance XAV59213 » ?

Ça permettra de clôturer officiellement ta demande.

Un petit message de remerciement après la clôture serait sympa aussi ! 😊

Merci et à bientôt sur le forum !

---

## Message 4 — 20 décembre 2025 à 15:23 (Europe/Paris)

- **Identifiant :** `1583`
- **Lien :** https://forumdomotique.com/forums/topic/586-pb-erreur-zigbee2mqtt/#findComment-1583

Merci 🥰

---

## Message 5 — 21 décembre 2025 à 16:07 (Europe/Paris)

- **Identifiant :** `1593`
- **Lien :** https://forumdomotique.com/forums/topic/586-pb-erreur-zigbee2mqtt/#findComment-1593

Salut TUTU12,

En fait, il y avait deux instances de Zigbee2MQTT qui tournaient en parallèle, plus un ZHA actif sur le même dongle. Ça créait un conflit et empêchait ton instance de démarrer.

Ce que j’ai fait, c’est recréer une instance propre avec un canal différent. J’ai aussi modifié le topic Zigbee2MQTT pour éviter tout conflit avec les anciennes installations que tu avais faites.

Je viens d’envoyer un message à Jack pour clôturer ton poste.

---
