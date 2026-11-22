---
title: "Moderniser vieux radiateur électrique"
description: "Oui, tu as parfaitement compris le principe, et bravo pour ton avancée ! Sur tes Thermor Amadeus de début 2000, il y a bien un fil pilote 6 ordres (c’est…"
image: /assets/images/vignettes-themes/chauffage.jpg

date: 2025-12-03
cover_alt: "Vignette de rubrique Chauffage — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/579-moderniser-vieux-radiateur-%C3%A9lectrique/">Lire et commenter sur Forum Domotique</a></p>

# Moderniser vieux radiateur électrique

- **Catégorie :** [Chauffage et Climatisation](https://forumdomotique.com/forums/70-chauffage-et-climatisation/)
- **Sujet :** https://forumdomotique.com/forums/topic/579-moderniser-vieux-radiateur-%C3%A9lectrique/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 3 décembre 2025 à 15:52 (Europe/Paris)

---

## Message 1 — 3 décembre 2025 à 15:52 (Europe/Paris)

- **Identifiant :** `1462`
- **Lien :** https://forumdomotique.com/forums/topic/579-moderniser-vieux-radiateur-%C3%A9lectrique/#findComment-1462

Salut [@Patex](https://forumdomotique.com/profile/781-patex/)

Oui, tu as parfaitement compris le principe, et bravo pour ton avancée !

Sur tes Thermor Amadeus de début 2000, **il y a bien un fil pilote 6 ordres** (c’est le standard à cette époque chez Thermor). Donc quand tu mettras les molettes à fond (position 7 ou « ★ » selon le modèle), le radiateur **obéira exclusivement aux ordres envoyés par le fil pilote** du module Nodon (ou équivalent).

Les ordres que tu pourras envoyer très facilement depuis Home Assistant avec le Nodon SIN-4-FP-21 :

| Ordre fil pilote | Effet sur le radiateur Amadeus | Commande Nodon utile dans HA |
| --- | --- | --- |
| Confort | Chauffage à la température de consigne (la molette n’a plus d’effet) | Confort |
| Éco (-3,5 °C) | Baisse de 3,5 °C par rapport à Confort | Eco |
| Hors-gel (≈ 7-10 °C) | Maintien hors-gel | Frost protection |
| Arrêt | Radiateur complètement éteint (même si molette à fond) | Off |
| Confort -1 °C | Confort moins 1 °C | Comfort -1 |
| Confort -2 °C | Confort moins 2 °C | Comfort -2 |

Donc oui, même avec tes vieux Amadeus, tu récupères toute la finesse du fil pilote 6 ordres, exactement comme sur un radiateur récent.

Pour l’instant moi je bricoles avec des scripts et automations j ai pas encore passé le cap et pas encore tester **Versatile Thermostat**→ de ce je vois l'intégration est bien suivi c’est très bien pour débuter, mais dès que tu passeras au **Versatile Thermostat** , tu vas gagner un temps fou et une régulation beaucoup plus douce et économe.

Petit tips quand tu feras le pas : Dans Versatile Thermostat, tu peux même mapper les ordres fil pilote comme tu veux. Exemple très efficace pour des vieux inertiels comme les Amadeus :

- Confort → Confort
- Éco → Confort -2 °C (au lieu de -3,5 °C classique, c’est souvent plus confortable et suffisant)
- Hors-gel → Hors-gel
- Arrêt → Off

---
