---
title: "Comment démonter la clé Sonoff PMG24 et la mettre en mode appairage Zigbee ?"
description: "Je ferai un tutoriel plus approfondi pour passer les clés USB en mode routeur J’en ai actuellement une à l’extérieur pour étendre mon réseau à l’extérieur…"
image: /assets/images/og-default.png
date: 2026-02-01
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/732-comment-d%C3%A9monter-la-cl%C3%A9-sonoff-pmg24-et-la-mettre-en-mode-appairage-zigbee/">Lire et commenter sur Forum Domotique</a></p>

# Comment démonter la clé Sonoff PMG24 et la mettre en mode appairage Zigbee ?

- **Catégorie :** [Sonoff](https://forumdomotique.com/forums/55-sonoff/)
- **Sujet :** https://forumdomotique.com/forums/topic/732-comment-d%C3%A9monter-la-cl%C3%A9-sonoff-pmg24-et-la-mettre-en-mode-appairage-zigbee/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 1 février 2026 à 09:52 (Europe/Paris)

---

## Message 1 — 1 février 2026 à 09:52 (Europe/Paris)

- **Identifiant :** `1944`
- **Lien :** https://forumdomotique.com/forums/topic/732-comment-d%C3%A9monter-la-cl%C3%A9-sonoff-pmg24-et-la-mettre-en-mode-appairage-zigbee/#findComment-1944

Bonjour Corent02,

Je ferai un tutoriel plus approfondi pour passer les clés USB en mode routeur.

J’en ai actuellement une à l’extérieur pour étendre mon réseau à l’extérieur côté garage qui est à plus de 20 mètres.

Voici les étapes :

Pour remettre ta clé Sonoff Dongle Plus MG24 (modèle PMG24) en mode appairage sans avoir à la démonter, tu peux reflasher le firmware routeur via l’outil web officiel de Sonoff. Ça réinitialisera les paramètres réseau et la mettra automatiquement en mode appairage.

Voici les étapes :

1.  Branche la clé sur un port USB de ton ordinateur (utilise de préférence un câble d’extension pour éviter les interférences).

2.  Ouvre un navigateur web (comme Chrome ou Edge, car l’outil utilise WebSerial).

3.  Va sur le site du flasher : <https://dongle.sonoff.tech/sonoff-dongle-flasher/>

Voici le firmware 7.5.0 que tu dois utiliser : <https://raw.githubusercontent.com/iHost-Open-Source-Project/hassio-ihost-sonoff-dongle-flasher/main/firmware-build/donglepmg24_mg24_zigbeerouter_stable_7.5.0_115200.gbl>

4.  Clique sur “Connect” pour détecter la clé. L’outil devrait la reconnaître et entrer en mode bootloader automatiquement (sans besoin de bouton physique, grâce à la conception du circuit).

5.  Sélectionne le firmware “Zigbee Router” (la version la plus récente).

6.  Clique sur “Flash” pour lancer le processus.

Une fois le flash terminé, la clé redémarrera et entrera en mode appairage automatiquement. Tu pourras alors l’appairer avec ton coordinateur SMLIGHT MR4U (active le mode “permit join” sur ton réseau Zigbee).

Si l’outil ne détecte pas la clé, essaie un autre port USB ou un autre ordinateur. Assure-toi qu’aucun autre logiciel (comme un terminal série) n’utilise le port.

Si ça ne fonctionne pas, il pourrait être nécessaire d’ouvrir le boîtier malgré tout (en forçant doucement le capuchon en plastique ou la coque en aluminium avec un outil plat, mais attention à ne pas endommager le PCB). Mais l’outil web devrait suffire, car il est conçu pour ça sur ce modèle.

---
