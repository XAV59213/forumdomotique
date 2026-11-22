---
title: "Refoss M06, remettre une pince à 0 sur HA"
description: "Pour remettre le compteur à zéro sur le circuit actuel (la recharge de votre véhicule électrique) après avoir déplacé la pince, la solution la plus fiable…"
image: /assets/images/vignettes-themes/home-assistant.jpg

date: 2026-01-15
cover_alt: "Vignette de rubrique Home Assistant — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/689-refoss-m06-remettre-une-pince-%C3%A0-0-sur-ha/">Lire et commenter sur Forum Domotique</a></p>

# Refoss M06, remettre une pince à 0 sur HA

- **Catégorie :** [Home Assistant](https://forumdomotique.com/forums/7-home-assistant/)
- **Sujet :** https://forumdomotique.com/forums/topic/689-refoss-m06-remettre-une-pince-%C3%A0-0-sur-ha/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 15 janvier 2026 à 11:38 (Europe/Paris)
- **Dernier message de XAV59213 :** 15 janvier 2026 à 12:48 (Europe/Paris)

---

## Message 1 — 15 janvier 2026 à 11:38 (Europe/Paris)

- **Identifiant :** `1794`
- **Lien :** https://forumdomotique.com/forums/topic/689-refoss-m06-remettre-une-pince-%C3%A0-0-sur-ha/#findComment-1794

Salut [@BatschRoland](https://forumdomotique.com/profile/563-batschroland/)

Pour remettre le compteur à zéro sur le circuit actuel (la recharge de votre véhicule électrique) après avoir déplacé la pince, la solution la plus fiable est de **réinitialiser l’appareil en usine** :

1.  Appuyez longuement sur le bouton physique du Refoss EM06 pendant **5 à 10 secondes** (jusqu’à ce que le voyant LED clignote ou change de couleur, souvent en rouge).  
Cela efface toutes les données de consommation accumulées sur tous les canaux.

2.  Une fois l’appareil réinitialisé, ouvrez l’application Refoss (ou Meross, car les deux marques sont liées) et **réajoutez l’appareil** comme lors de la première configuration (via Wi-Fi ou Bluetooth).

Après cela, le compteur repartira à zéro pour le circuit connecté actuellement. Comme vous n’utilisez qu’une seule pince pour ce circuit, cela ne posera pas de problème pour les autres canaux (ils resteront à zéro ou sans mesure).

---

## Message 2 — 15 janvier 2026 à 12:48 (Europe/Paris)

- **Identifiant :** `1796`
- **Lien :** https://forumdomotique.com/forums/topic/689-refoss-m06-remettre-une-pince-%C3%A0-0-sur-ha/#findComment-1796

Malheureusement, d’après les informations disponibles sur le Refoss EM06 (ou modèles similaires comme l’EM06P), il n’existe pas d’option officielle pour réinitialiser le compteur d’énergie d’un seul canal sans affecter les autres

---
