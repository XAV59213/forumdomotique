---
title: "Aide câblage relais Ajax contact sec pour porte de garage, double appui et choix NO/NC"
description: "Borne 4 et Borne 2 pour valider la fonction bouton poussoir de ta porte tu le fait 2 fois ça va descendre et remonter ta porte Ça simule un appui sur le…"
image: /sujets/481-aide-cablage-relais-ajax-contact-sec-pour-porte-de-garage-double-appui-et-choix/images/og-partage.jpg

date: 2025-11-04
cover_alt: "Schéma de raccordement d’un connecteur de portail, bornes 1 à 6 (contacts et alimentation)"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/481-aide-c%C3%A2blage-relais-ajax-contact-sec-pour-porte-de-garage-double-appui-et-choix-nonc/">Lire et commenter sur Forum Domotique</a></p>

# Aide câblage relais Ajax contact sec pour porte de garage, double appui et choix NO/NC

- **Catégorie :** [Garage et Véhicules Électriques](https://forumdomotique.com/forums/76-garage-et-v%C3%A9hicules-%C3%A9lectriques/)
- **Sujet :** https://forumdomotique.com/forums/topic/481-aide-c%C3%A2blage-relais-ajax-contact-sec-pour-porte-de-garage-double-appui-et-choix-nonc/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 4 novembre 2025 à 15:35 (Europe/Paris)

---

## Message 1 — 4 novembre 2025 à 15:35 (Europe/Paris)

- **Identifiant :** `1149`
- **Lien :** https://forumdomotique.com/forums/topic/481-aide-c%C3%A2blage-relais-ajax-contact-sec-pour-porte-de-garage-double-appui-et-choix-nonc/#findComment-1149

Salut [@Marcl78](https://forumdomotique.com/profile/613-marcl78/)

#### Test avec un shunt ta motorisation

**Borne 4 et Borne 2 pour valider la fonction bouton poussoir de ta porte tu le fait 2 fois ça va descendre et remonter ta porte**

Ça simule un **appui sur le bouton poussoir (PB)** → **impulsion courte entre le NO et le commun** → la porte **ouvre si fermée, ferme si ouverte** (toggle).

→ **C’est la borne 2 (PB NO) + borne 4 (PE commun)** qui nous intéresse.

#### RACCORDEMENT FINAL (Ajax Relay → Moteur)

| Ajax Relay | → | Moteur porte de garage |
| --- | --- | --- |
| **PS IN +** | → | **Borne 5 : +24V logiquement tu peux aller a 24v avec ce module** |
| **PS IN –** | → | **Borne 4 : GND** |
| **COM (contact relais)** | → | **Borne 4 : PE (commun)GND** |
| **NO (contact relais)** | → | **Borne 2 : PB (NO)** |

Ne touche pas aux bornes 1 et 3 (porte piéton). Ne connecte rien sur NC du relais (inutilisé ici).

## Configuration OBLIGATOIRE dans l’app Ajax

1. Ouvre **Ajax App** → **Appareils** → **Relay Jeweller** → **Paramètres**
2. **Mode de fonctionnement** → **Impulsion (Pulse)**
3. **Durée d’impulsion** → **1 seconde** (testé sur 99 % des moteurs)
4. **État du contact** → **Normally Open (NO)**
5. **Nom** → ex. : *Porte Garage*
6. **Sauvegarde**

## Test final

1. Appuie **UNE FOIS** sur le relais dans l’app → → Le relais clique → contact fermé 1s → moteur démarre → porte bouge.
2. Appuie une **deuxième fois** → porte s’arrête ou inverse (selon position).

> **Plus besoin d’appuyer 2 fois !** Une seule pression = une action complète.

N’hésite pas à passer voir [@CedricMD](https://forumdomotique.com/profile/7-cedricmd/) il a testé l’alarme et pourra te renseigner :

<https://www.maison-et-domotique.com/130864-test-alarme-ajax-hub-2/>

---
