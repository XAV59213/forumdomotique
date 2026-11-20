---
title: "Présentation nouvel inscrit"
---

# Présentation nouvel inscrit

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/462-pr%C3%A9sentation-nouvel-inscrit/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 20 décembre 2025 à 13:10 (Europe/Paris)

---

## Message 1 — 20 décembre 2025 à 13:10 (Europe/Paris)

- **Identifiant :** `1581`
- **Lien :** https://forumdomotique.com/forums/topic/462-pr%C3%A9sentation-nouvel-inscrit/#findComment-1581

Bonjour Eric,

Bienvenue sur le forum et bravo pour ton message très clair !

Habitant le Nord, je connais bien ce climat qui nous laisse effectivement du temps pour bricoler la domotique quand il pleut 😉 Tu as choisi **LA** meilleure solution pour débuter : **Home Assistant Green**. C’est simple, évolutif et tu ne seras jamais bloqué plus tard.

Voici une liste précise et sereine de ce qu’il te faut acheter pour réaliser **tout** ce que tu veux dès le premier jour, sans rien racheter ensuite. Je te mets des liens français (Amazon.fr ou Domadoo, livraison rapide, SAV facile) .

1. **La base (obligatoire)** ✓ Home Assistant Green → [https://www.domadoo.fr/fr/box-domotique/7046-nabu-casa-home-assistant-green-smart-home-hub.html](https://www.domadoo.fr/fr/box-domotique/7046-nabu-casa-home-assistant-green-smart-home-hub.html?referrer=grok.com) (ou version anglaise si besoin)
2. **La clé Zigbee (indispensable pour tous tes capteurs et volets)** ✓ Sonoff Zigbee 3.0 USB Dongle Plus V2 (version “E”) → [https://www.domadoo.fr/fr/interface/6315-sonoff-dongle-zigbee-30-usb-compatible-home-assistant.html](https://www.domadoo.fr/fr/interface/6315-sonoff-dongle-zigbee-30-usb-compatible-home-assistant.html?referrer=grok.com) Tu la branches simplement sur le Green, tu installes l’intégration ZHA ou Zigbee2MQTT en 2 clics et c’est parti.
3. **Détection de présence + éclairage (très fiable, fonctionne même dans le noir)** ✓ 2 × Aqara Capteur de présence FP2 (détecte jusqu’à 6 m, découpe en 30 zones max) → [https://www.amazon.fr/Aqara-Capteur-Présence-Détection-Multi-Personnes/dp/B0BXWZMQJ3](https://www.amazon.fr/Aqara-Capteur-Pr%C3%A9sence-D%C3%A9tection-Multi-Personnes/dp/B0BXWZMQJ3?referrer=grok.com) Commence par 2 (salon + couloir), tu en rajouteras plus tard si besoin. Avec ça, lumières qui s’allument/s’éteignent automatiquement = magique !
4. **Sonnette + notification jardin** ✓ Sonnette vidéo Reolink 5MP PoE (sonnette + caméra + carillon inclus) → Recherche “Reolink Video Doorbell PoE” sur Amazon.fr ou site Reolink Tu la câbles en PoE (ou avec les 2 fils de ton ancienne sonnette si tu utilises l’adaptateur). Tu reçois la notification sur ton téléphone même au fond du jardin, tu parles à la personne, et tu peux créer une petite musique dans les pièces avec tes enceintes Alexa.
5. **Volets roulants Somfy RTS (BSO motorisé + Velux RTS)** Pour les moteurs Somfy RTS ou io, il n’existe pas de “stick Zigbee” direct à coller derrière le moteur. Les solutions Zigbee courantes sont des modules encastrés comme NodOn ou Sunricher (mais pas spécifiques Somfy). Alternative recommandée : utilise un dongle/overlays RTS séparé ou passe par Zigbee2MQTT avec des modules compatibles. Si tu veux rester simple, regarde les modules volets Zigbee génériques sur Domadoo (ex : [https://www.domadoo.fr/fr/peripheriques/5245-sunricher-module-volet-roulant-zigbee-30.html](https://www.domadoo.fr/fr/peripheriques/5245-sunricher-module-volet-roulant-zigbee-30.html?referrer=grok.com)). Ton BSO Somfy RTS et ton Velux RTS seront pilotables dans Home Assistant avec la bonne intégration.
6. **Volets roulants filaires (ceux avec interrupteur classique)** ✓ Module Zigbee derrière interrupteur pour volets (recommandé : Zemismart ou équivalent) → Recherche “Zemismart Zigbee 3.0 module volet roulant filaire” sur Domadoo ou Amazon Alternative fiable : NodOn SIN-4-RS-20 ou Sunricher → [https://www.domadoo.fr/fr/peripheriques/5690-nodon-module-volet-roulant-zigbee.html](https://www.domadoo.fr/fr/peripheriques/5690-nodon-module-volet-roulant-zigbee.html?referrer=grok.com) Tu le caches derrière ton interrupteur existant (couper le courant, 10 min par volet). Tu gardes les interrupteurs physiques + commande Alexa + automatisations.
7. **Chauffe-serviette Acova** ✓ Module fil pilote Zigbee NodOn SIN-4-FP-21 → Recherche sur Domadoo ou Amazon.fr Tu le places dans la boîte de dérivation du chauffe-serviette (ou derrière l’interrupteur). Tu pourras dire « Alexa, chauffe les serviettes » 20 min avant la douche, ou programmer 30 min chaque matin.
8. **Commande vocale Alexa** Tu as déjà des enceintes Alexa ? Parfait ! Home Assistant s’intègre nativement avec Alexa : toutes tes lumières, volets, chauffe-serviette apparaîtront automatiquement dans l’app Alexa après une rapide configuration.

**Tes premiers pas (15 minutes un dimanche après-midi)**

1. Brancher le Green → suivre le guide en français.
2. Brancher la clé Sonoff → ajouter ZHA ou Zigbee2MQTT.
3. Appairer ton premier capteur Aqara.
4. Créer ta première automation : « Quand présence détectée → allume la lumière ».
5. Dire « Alexa, découvre les appareils » → tu commandes déjà à la voix !

Voilà, une base solide ! Après, il y a tellement de modules qui existent et plein de façons différentes de faire (exemple : chez moi, tous les Somfy se gèrent via ma Freebox avec HomeConnect).

N’hésite pas à revenir ici avec des photos quand tu reçois le matériel, toute la communauté t’aidera pour chaque étape. Tu vas adorer voir tes lumières s’allumer toutes seules et recevoir la sonnette sur ton téléphone en buvant le café dans le jardin !

Excellent dimanche à toi dans le Morbihan, et à très vite pour la suite !

---
