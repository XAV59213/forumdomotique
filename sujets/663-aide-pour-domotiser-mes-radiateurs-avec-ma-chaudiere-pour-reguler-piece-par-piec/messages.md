---
title: "Aide pour domotiser mes radiateurs avec ma chaudière pour réguler pièce par pièce sans se brancher directement à la chaudière (TRV Sonoff et Vitodens 100-W OpenTherm)"
description: "Je ne suis pas un pro du chauffage (et pour des raisons de sécurité, je te conseille vivement de ne pas bricoler seul si tu n'es pas qualifié), mais voici…"
image: /assets/images/og-default.png
date: 2026-01-10
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/663-aide-pour-domotiser-mes-radiateurs-avec-ma-chaudi%C3%A8re-pour-r%C3%A9guler-pi%C3%A8ce-par-pi%C3%A8ce-sans-se-brancher-directement-%C3%A0-la-chaudi%C3%A8re-trv-sonoff-et-vitodens-100-w-opentherm/">Lire et commenter sur Forum Domotique</a></p>

# Aide pour domotiser mes radiateurs avec ma chaudière pour réguler pièce par pièce sans se brancher directement à la chaudière (TRV Sonoff et Vitodens 100-W OpenTherm)

- **Catégorie :** [Chauffage et Climatisation](https://forumdomotique.com/forums/70-chauffage-et-climatisation/)
- **Sujet :** https://forumdomotique.com/forums/topic/663-aide-pour-domotiser-mes-radiateurs-avec-ma-chaudi%C3%A8re-pour-r%C3%A9guler-pi%C3%A8ce-par-pi%C3%A8ce-sans-se-brancher-directement-%C3%A0-la-chaudi%C3%A8re-trv-sonoff-et-vitodens-100-w-opentherm/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 10 janvier 2026 à 16:46 (Europe/Paris)

---

## Message 1 — 10 janvier 2026 à 16:46 (Europe/Paris)

- **Identifiant :** `1715`
- **Lien :** https://forumdomotique.com/forums/topic/663-aide-pour-domotiser-mes-radiateurs-avec-ma-chaudi%C3%A8re-pour-r%C3%A9guler-pi%C3%A8ce-par-pi%C3%A8ce-sans-se-brancher-directement-%C3%A0-la-chaudi%C3%A8re-trv-sonoff-et-vitodens-100-w-opentherm/#findComment-1715

Salut [@Juliemoss](https://forumdomotique.com/profile/1052-juliemoss/) ,

Je ne suis pas un pro du chauffage (et pour des raisons de sécurité, je te conseille vivement de ne pas bricoler seul si tu n'es pas qualifié), mais voici un guide clair basé sur les docs officielles Viessmann et des retours d'utilisateurs. **Contacte toujours un chauffagiste certifié Viessmann pour l'intervention – ça évite les pannes ou la perte de garantie.**

### Pourquoi reprogrammer en contact sec ?

- Le mode "contact sec" (ou dry contact) permet à la chaudière de recevoir des signaux électriques simples (sans tension) d'un module externe, comme un thermostat ou une sonde. Ça remplace les modes plus anciens (comme on/off basique) pour une modulation fine.
- Amélioration : Meilleure régulation de la température, moins de cycles courts (qui gaspillent du gaz), et compatibilité avec des outils modernes pour économiser jusqu'à 10-20 % sur la facture.

### Étapes pour reprogrammer et ajouter un module contact sec

1. **Préparation (à faire par toi ou le pro)** :

   - Vérifie ton modèle exact (ex. : B1HA, B1HE, etc.) sur la plaque signalétique de la chaudière.
   - Télécharge le manuel spécifique sur le site Viessmann ([viessmann.fr](https://viessmann.fr) ou [viessmann.com](https://viessmann.com)). Cherche "Vitodens 100-W [ton modèle] – Instructions de service" (souvent en PDF gratuit). Par exemple, pour la Vitodens 100-W B1HA, c'est dispo ici : [lien vers manuel FR](https://www.viessmann.fr/heizung/content/dam/public-brands/fr/pdfs/doc/b1ha/vitodens_100-b1ha_oi_fr.pdf?referrer=grok.com).
   - Assure-toi que la chaudière est éteinte (coupure générale) avant toute manip.
2. **Accès au mode paramétrage (par le chauffagiste)** :

   - Allume la chaudière et accède au menu "Réglages" ou "Paramètres" via l'écran numérique (boutons flèches haut/bas). Pour la Vitodens 100-W, c'est souvent en mode "technicien" (code d'accès requis, comme 100 ou spécifique au modèle – dans le manuel, cherche "Code service" ou "Engineering mode").
   - Navigue vers les options de régulation : Cherche "Mode de commande" ou "Type de contact" (parfois sous "A1" pour entrée analogique ou "K1" pour contact).
   - Sélectionne "Contact sec" (dry contact) ou "Potentiomètre distant" si c'est pour un module variable. Confirme et sauvegarde (le paramètre clignote souvent).
   - Temps estimé : 10-15 min, mais le pro testera après pour éviter les erreurs.
3. **Installation du module contact sec** :

   - Choisis un module compatible Viessmann (ex. : Vitotrol ou un relais dry contact comme le ZK 01153). Ou un thermostat tiers (Tado OpenTherm si ta chaudière le supporte – vérifie en mode EU).
   - Branche-le sur les bornes dédiées (souvent X1 ou X2 sur la carte électronique – voir schéma dans le manuel, page ~50-60).
   - Test : Remets sous tension, vérifie que le module envoie bien le signal (LED ou app du thermostat).
4. **Autres améliorations rapides pour ta Vitodens 100-W** :

   - **Réglages optimaux** : Température chauffage max 70-75°C (pour condensation max), ECS à 50-55°C. Active la "fonction confort" pour ECS instantanée si tu as une combi.
   - **Entretien** : Nettoie le filtre à condensats tous les 3 mois, et fais une visite annuelle (brûleur, échangeur).
   - **Économies** : Ajoute une sonde extérieure (si pas déjà) pour modulation auto. Ou passe en OpenTherm si compatible (demande au pro – ça booste l'efficacité).
   - **Coût estimé** : Reprogrammation + module : 100-300 € (main-d'œuvre incluse).

---
