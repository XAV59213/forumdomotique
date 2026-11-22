---
title: "decouverte de la domotique et de son monde"
description: "Le RFXCOM peut prendre en charge ton problème, mais l’installation est un peu périlleuse. Il y a quelques tutoriels disponibles, mais pas beaucoup Je l’ai…"
image: /assets/images/vignettes-themes/presentation.jpg

date: 2025-12-04
cover_alt: "Vignette de rubrique Présentation / Communauté — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/582-decouverte-de-la-domotique-et-de-son-monde/">Lire et commenter sur Forum Domotique</a></p>

# decouverte de la domotique et de son monde

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/582-decouverte-de-la-domotique-et-de-son-monde/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 4 décembre 2025 à 10:54 (Europe/Paris)

---

## Message 1 — 4 décembre 2025 à 10:54 (Europe/Paris)

- **Identifiant :** `1477`
- **Lien :** https://forumdomotique.com/forums/topic/582-decouverte-de-la-domotique-et-de-son-monde/#findComment-1477

Salut [@Ellywick](https://forumdomotique.com/profile/131-ellywick/),

Le RFXCOM peut prendre en charge ton problème, mais l’installation est un peu périlleuse. Il y a quelques tutoriels disponibles, mais pas beaucoup.

j’ai acheté sur domadoo:

<https://www.domadoo.fr/fr/145_rfxcom?srsltid=AfmBOopWcKLqfo3nBFMQQCosjPPMKvip3qNew_MPBijHUWL1oUSer8tz>

Je l’ai mis en place pour ma porte de garage, où j’ai installé un relais Comelit. En gros, voici les étapes :

1.  Branche ton RFXCOM sur ton PC et passe-le en mode apprentissage et install <http://rfxcom.com/epages/78165469.mobile/en_GB/?ObjectPath=/Shops/78165469/Categories/Downloads>

2.  Récupère les codes de ta télécommande (chaque bouton génère un code unique, donc note-les tous pour une configuration complète).

3.  Une fois les codes récupérés, rebranche le RFXCOM en USB sur ton Home Assistant.

4.  Installe l’intégration RFXCOM dans Home Assistant.

5.  Ajoute l’appareil en indiquant son nom et les codes correspondants.

C’est un peu long, mais une fois configuré, ça fonctionne très bien !

**Fréquences & protocoles supportés par RFXCOM**

```plaintext
Frequences et protocoles supportes par RFXCOM (RFXtrx433E / XL / etc.)

╔═══════════╦════════════════════════════════════════════════════════════════════════╗
║ Fréquence ║                           Protocoles supportés                         ║
╠═══════════╬════════════════════════════════════════════════════════════════════════╣
║ 310 MHz   ║ X10 lighting (RX/TX)                                                   ║
║           ║ X10 security (RX/TX)                                                   ║
╠═══════════╬════════════════════════════════════════════════════════════════════════╣
║ 315 MHz   ║ Aoke relay, PT2262 / EV1527 (Lighting4), Keeloq (non chiffré)          ║
║           ║ Visonic CodeSecure (non chiffré), Visonic PowerCode                    ║
╠═══════════╬════════════════════════════════════════════════════════════════════════╣
║ 433.92    ║ → Éclairage : X10, ARC, HomeEasy EU/UK, KlikAanKlikUit, LightwaveRF,   ║
║ MHz       ║   NEXA, Chacon, Blyss, Intertechno, Energenie, Livolo, MDremote, etc.  ║
║           ║ → Volets/rideaux : Somfy RTS (RFY), Hasta, RollerTrol, Forest, Brel,   ║
║           ║   Dooya, Louvolite, YOODA, Quotidom, Nobily, etc.                      ║
║           ║ → Météo : Oregon Scientific (tous), La Crosse, Alecto, Fine Offset,    ║
║           ║   Hideki, Rubicson, TFA, Cresta, Viking, etc.                          ║
║           ║ → Sécurité : Visonic, Meiantech, Kerui, Chuango, Atlantic, X10 sec.    ║
║           ║ → Autres : Byron SX/DX, OWL CME163/CMR200, Mertik, Conrad RSL, etc.    ║
╠═══════════╬════════════════════════════════════════════════════════════════════════╣
║ 868 MHz   ║ Alecto WS5500/ACH2010, Fine Offset WH2900/Ecowitt, Davis Vantage EU    ║
║           ║ Honeywell ActivLink, Itho CVE/ECO, Orcon, Edisio, FS20, Gaposa         ║
║           ║ Keeloq & Visonic (non chiffrés)                                        ║
║           ║ (Attention : un seul protocole RX activable à la fois sur 868 MHz)     ║
╚═══════════╩════════════════════════════════════════════════════════════════════════╝

Note : la liste complète dépasse les 120 protocoles selon le firmware. 
Pour la liste exhaustive à jour → https://www.rfxcom.com/epages/78165430.sf/fr_FR/?ObjectPath=/Shops/78165430/Categories/Downloads
```

Si tu pars sur cette solution, je préparerai un tutoriel pour expliquer l’utilisation du RFXCOM.

---
