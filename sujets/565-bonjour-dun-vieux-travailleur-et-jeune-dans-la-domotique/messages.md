---
title: "Bonjour, d'un vieux travailleur, et jeune dans la domotique"
description: "Je vois que tu es en train de te lancer dans Home Assistant (HA) et le Zigbee, et que tu te sens un peu submergé par toutes les options. Pas de panique…"
image: /assets/images/og-default.png
date: 2025-11-30
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/565-bonjour-dun-vieux-travailleur-et-jeune-dans-la-domotique/">Lire et commenter sur Forum Domotique</a></p>

# Bonjour, d'un vieux travailleur, et jeune dans la domotique

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/565-bonjour-dun-vieux-travailleur-et-jeune-dans-la-domotique/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 30 novembre 2025 à 10:24 (Europe/Paris)

---

## Message 1 — 30 novembre 2025 à 10:24 (Europe/Paris)

- **Identifiant :** `1399`
- **Lien :** https://forumdomotique.com/forums/topic/565-bonjour-dun-vieux-travailleur-et-jeune-dans-la-domotique/#findComment-1399

Bonjour [@jlfa](https://forumdomotique.com/profile/769-jlfa/) et bienvenue !

Je vois que tu es en train de te lancer dans Home Assistant (HA) et le Zigbee, et que tu te sens un peu submergé par toutes les options. Pas de panique, c’est normal au début HA est super puissant, mais il y a beaucoup de choix. Je vais essayer de te répondre de manière simple et structurée, en me basant sur tes questions. Je vais me concentrer sur l’essentiel pour t’aider à démarrer sans te noyer dans les détails techniques.

**1. Compatibilité de tes modules Yokis Zigbee avec Home Assistant**

D’après mes recherches, les modules Yokis (surtout la gamme “UP” qui est compatible Zigbee 3.0) fonctionnent bien avec Home Assistant via l’intégration ZHA (Zigbee Home Automation), qui est native dans HA.  Certains utilisateurs les intègrent sans problème, et il y a même des produits Yokis listés comme compatibles avec HA (par exemple, des interrupteurs Zigbee).  Si tes modules sont bien en Zigbee, ils devraient s’appairer directement une fois que tu auras un coordinateur Zigbee configuré (j’explique ça plus bas).

Si tu as des modèles précis (par exemple, des références comme “Yokis UP”), vérifie sur le forum HA ou dans la doc ZHA pour confirmer. Mais globalement, c’est positif pas besoin de regretter tes achats !

**2. Home Assistant OS : Indispensable ?**

Oui, HA OS est une bonne base, surtout pour les débutants. C’est le système d’exploitation optimisé pour HA, qui rend tout plus simple (mises à jour automatiques, intégrations faciles). Tu peux l’installer sur différents supports, mais si tu vises la simplicité, c’est parfait.

**3. Choix du support (hardware) : HA Green vs. Mini PC vs. Vieux PC**

Tu as raison de viser quelque chose de compact et économe. Voici un comparatif rapide :

**Home Assistant Green** : C’est le choix le plus simple pour les débutants. C’est un petit boîtier prêt à l’emploi (plug-and-play) vendu par les créateurs de HA (Nabu Casa). Tu le branches, tu suis l’assistant d’installation via un navigateur web, et c’est parti en quelques minutes. Pas besoin de formater un disque ou d’installer un OS manuellement. Il est économe en énergie (environ 5-10W), silencieux, et évolutif (tu peux ajouter des extensions comme un dongle Zigbee). Prix autour de 100-150€, et il est conçu pour durer. Si tu veux éviter les complications, c’est idéal surtout si tu n’es pas à l’aise avec l’informatique.

**Mini PC** (comme un Intel NUC ou un Beelink) : C’est plus puissant et flexible (tu peux ajouter du stockage, de la RAM, etc.), ce qui est génial si tu veux faire tourner d’autres trucs en plus de HA (comme des conteneurs Docker pour des add-ons avancés). Mais l’installation est un peu plus compliquée : tu dois télécharger HA OS, créer une clé USB bootable (avec un outil comme Rufus ou Balena Etcher), brancher le mini PC, et installer l’OS depuis zéro. Ça prend 30-60 minutes, et il faut être un minimum à l’aise avec les BIOS/UEFI. Côté énergie, c’est un peu plus gourmand (10-20W en idle), mais toujours mieux qu’un vieux PC. Si tu aimes bricoler et que tu veux de la puissance pour l’avenir (par exemple, pour de l’IA ou beaucoup d’automations), c’est top. Pourquoi plus compliqué que le Green ? Parce que le Green est pré-installé, tandis que là, tu fais tout toi-même.

**Vieux PC** : Évite si possible, comme tu dis. Ils sont encombrants, bruyants, et consomment beaucoup (50W+ même au repos). Mais si tu en as un qui traîne, tu peux tester HA dessus pour voir si ça te plaît avant d’acheter du neuf. Installe HA OS comme sur un mini PC.

**Mon conseil** : Commence par le HA Green pour la simplicité. C’est évolutif (tu peux migrer vers un mini PC plus tard si besoin), et ça te permettra de te concentrer sur tes modules plutôt que sur l’installation. Si tu as un budget serré, un mini PC d’occasion peut être une alternative, mais vérifie qu’il supporte HA OS (processeur 64-bit, au moins 4Go RAM, SSD recommandé).

**4. C’est quoi les “dongles” ?**

Dans le contexte de Home Assistant et Zigbee, un “dongle” c’est simplement une petite clé USB qui sert de “coordinateur” pour ton réseau Zigbee. C’est comme une antenne qui permet à HA de communiquer avec tes modules Zigbee (comme tes Yokis). Sans ça, HA ne peut pas contrôler les appareils Zigbee.

Exemples populaires :

•  Sonoff Zigbee 3.0 USB Dongle (pas cher, environ 10-20€, et super compatible avec HA via ZHA ou Zigbee2MQTT).

•  Conbee II ou III (un peu plus cher, mais fiable).

Tu le branches directement sur ton HA Green ou mini PC, et tu le configures dans HA. C’est indispensable si tu veux du Zigbee. Choisis-en un compatible avec ZHA pour la simplicité (la doc HA en liste plein).

**Prochains pas pour toi**

**Achats prioritaires** :

•  Un HA Green (ou mini PC si tu préfères).

•  Un dongle Zigbee (Sonoff pour commencer).

•  Pas besoin d’autre chose pour tester tes Yokis.

**Installation basique** : Une fois le hardware en main, suis le guide officiel de HA (sur home-assistant.io). Commence par installer HA, ajouter l’intégration ZHA, brancher le dongle, et appairer tes modules Yokis (généralement en appuyant longtemps sur un bouton du module).

**Sécurité** : Une fois installé, active le HTTPS, change les mots de passe par défaut, et utilise un VPN si tu accèdes à HA depuis l’extérieur. Mais ne t’inquiète pas tout de suite – HA est sécurisé de base.

Si tu as des questions plus précises (modèles exacts de Yokis, liens pour acheter, etc.), dis-moi ! Prends ton temps, expérimente étape par étape, et tu vas adorer. Bonne chance, et amuse-toi bien avec la domotique ! 😊

---
