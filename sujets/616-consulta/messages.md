---
title: "CONSULTA"
---

# CONSULTA

- **Catégorie :** [Café Domotique](https://forumdomotique.com/forums/85-caf%C3%A9-domotique/)
- **Sujet :** https://forumdomotique.com/forums/topic/616-consulta/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 21 décembre 2025 à 09:31 (Europe/Paris)

---

## Message 1 — 21 décembre 2025 à 09:31 (Europe/Paris)

- **Identifiant :** `1586`
- **Lien :** https://forumdomotique.com/forums/topic/616-consulta/#findComment-1586

Bonjour [@Apareja](https://forumdomotique.com/profile/908-apareja/)

Merci pour les détails sur votre installation. Je comprends bien le problème : votre barrière infrarouge déclenche la sirène localement, mais vous n’avez aucune notification sur votre téléphone quand vous êtes absent, car le système n’est pas connecté.

Votre idée avec le Sonoff RE5V1C (relais à contact sec 5V) est bonne, mais le branchement actuel (en série sur le fil positif de la sirène) permet seulement de couper/activer la sirène manuellement via l’app eWeLink. Ça ne détecte pas automatiquement le déclenchement de l’alarme, car le relais agit comme un interrupteur commandé, pas comme un capteur d’état.

**Solution recommandée : Brancher le RE5V1C en parallèle sur la sortie alarme de la barrière**

La plupart des barrières infrarouges “pour alarme” (même les modèles basiques sans Wi-Fi ni alarme intégrée) disposent d’une **sortie relais à contact sec** (NO/NC/COM) sur le récepteur. Cette sortie change d’état quand le faisceau est coupé (alarme déclenchée).

•  Vérifiez sur votre barrière (souvent des bornes marquées ALARM, NO, NC, COM ou similaires).

•  Si c’est le cas : connectez les bornes du contact sec du Sonoff RE5V1C directement sur cette sortie relais de la barrière (par exemple, COM et NO).

•  Configurez le Sonoff en mode “inching” (impulsion) ou “self-locking” selon le comportement (self-locking si l’état reste “alarme” tant que le faisceau est coupé).

•  Dans eWeLink, activez les notifications push : vous recevrez une alerte instantanée sur votre téléphone dès que l’alarme se déclenche.

Avantages :

•  La sirène continue de fonctionner normalement (pas de coupure).

•  Vous avez un retour d’état réel du déclenchement.

•  Simple, pas cher, et compatible avec votre programmation horaire existante.

Si votre barrière n’a pas de sortie relais (certains modèles très basiques n’ont que l’alimentation de la sirène), alors il faut détecter via la sirène :

**Solution alternative : Détecter le déclenchement via la sirène**

•  Branchez le contact sec du RE5V1C **en parallèle** (pas en série) sur les fils de la sirène.

•  Alimentez le RE5V1C en 5V séparé (USB ou alimentation dédiée).

•  Quand la sirène s’active (tension apparaît sur ses fils), le contact sec du Sonoff se ferme/ouvre → il change d’état et envoie une notification via eWeLink.

Ça fonctionne bien si la sirène est en 12V ou 24V (courant typique). Testez pour voir si le changement d’état est détecté correctement.

**Fins de course sur le portail**

Si votre portail est battant ou coulissant et motorisé, ajouter **deux fins de course** (un pour position ouverte, un pour fermée) permet de détecter si quelqu’un force ou laisse le portail ouvert.

•  Utilisez des contacts magnétiques (capteurs d’ouverture comme les Sonoff DW2 ou équivalents Zigbee/WiFi).

•  Connectez-les à un autre module Sonoff (ou le même si multi-canaux) pour avoir des notifications “portail ouvert” ou “intrusion via portail”.

•  C’est particulièrement utile avec une barrière IR, car ça couvre les cas où quelqu’un escalade ou force directement le portail sans couper le faisceau IR.

Si vous avez un schéma plus précis de votre barrière ou des photos des bornes, je peux affiner les conseils

---
