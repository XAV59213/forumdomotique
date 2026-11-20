---
title: "Installation basique"
description: "Voici les solutions réalistes pour ton besoin : suivre la température intérieure à distance en 4G (sans WiFi/box allumée) et piloter la pompe de…"
image: /assets/images/og-default.png
date: 2026-01-10
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/673-installation-basique/">Lire et commenter sur Forum Domotique</a></p>

# Installation basique

- **Catégorie :** [Café Domotique](https://forumdomotique.com/forums/85-caf%C3%A9-domotique/)
- **Sujet :** https://forumdomotique.com/forums/topic/673-installation-basique/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 10 janvier 2026 à 16:34 (Europe/Paris)

---

## Message 1 — 10 janvier 2026 à 16:34 (Europe/Paris)

- **Identifiant :** `1714`
- **Lien :** https://forumdomotique.com/forums/topic/673-installation-basique/#findComment-1714

Voici les solutions réalistes pour ton besoin : **suivre la température intérieure à distance en 4G** (sans WiFi/box allumée) et **piloter la pompe de circulation** (via une prise) pendant 3 mois d’absence, tout en essayant de minimiser la consommation électrique permanente.

**il faut quasi obligatoirement laisser quelque chose allumé en permanence** (prise 4G + capteur ou module autonome). Mais on peut très fortement réduire cette consommation résiduelle (souvent entre 1 et 4 W en veille).

### Solutions les plus adaptées en 2026 (classées par simplicité / efficacité)

1. **La solution la plus simple et la plus fiable (la plus utilisée pour ce cas précis)** **Prise SimPal T420 (ou équivalent actuel 4G LTE type T420/T430)**

   <https://www.amazon.fr/Intelligente-Contr%C3%B4lable-Temp%C3%A9rature-Programmable-T%C3%A9l%C3%A9commande/dp/B0063G87NW/ref=asc_df_B0063G87NW?mcid=d39c1cb5e32a3b6f9df91dcee42957e3&tag=googshopfr-21&linkCode=df0&hvadid=701623790546&hvpos=&hvnetw=g&hvrand=8528204119146652098&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9109104&hvtargid=pla-435304181973&psc=1&hvocijid=8528204119146652098-B0063G87NW-&hvexpln=0>

   - Alimentation 230V classique
   - Carte SIM 4G (Free 2€, Red by SFR 5Go 5€, etc.)
   - Capteur température intégré (±1–2°C environ)
   - Pilotage total par SMS (ou app si version récente)
   - Fonction thermostat intégrée : allume/éteint automatiquement la prise selon seuils température (ex : >18°C → off / <12°C → on)
   - Alerte SMS si température <8°C ou >25°C (gel ou surchauffe)
   - Alerte coupure courant (pratique)

   Consommation ≈ **1,5–3 W** en permanence (très acceptable pour 3 mois). Prix actuel ≈ 70–110 € selon revendeur.

   → Tu branches directement ta pompe de circulation sur cette prise → thermostat déporté parfait pour gel + économie.
2. **Solution autonome basse consommation (la plus économe en électricité)** Capteur NB-IoT + prise intelligente 4G commandée à distance

   Exemple de combo très efficace en 2025-2026 :

   - Capteur température NB-IoT Efento / ou similaire (batterie 5–10 ans !) → très faible conso réseau (Narrowband IoT)
   - Plateforme cloud qui peut envoyer des ordres vers une prise 4G (SimPal, 4G Smart Plug avec API ou IFTTT-like)

   Consommation totale système : **< 1 W** possible en moyenne (le capteur lui-même consomme quasi rien). Inconvénient : plus cher + configuration un peu plus technique (mais très fiable une fois en place).
3. **Solution intermédiaire très répandue** **UBIBOT GS1 4G** (ou son successeur en 2026)

   - Température + humidité
   - Écran LCD
   - 4G + WiFi (mais tu peux n’utiliser que 4G)
   - Alimentation USB ou 230V (possibilité panneau solaire 5V + batterie pour ~0 W réseau)
   - Application + alertes + historique
   - Pilotage prise séparée via scénario cloud (ex : si T < 10°C → allumer telle prise 4G)

   Consommation ≈ **2–4 W** (un peu plus que SimPal mais plus complet).

### Comparaison rapide conso & simplicité

| Solution | Conso permanente | Pilotage prise auto | Prix approx. | Simplicité | Fiabilité 3 mois absence |
| --- | --- | --- | --- | --- | --- |
| SimPal T420 (ou équiv.) | 1,5–3 W | Oui (thermostat intégré) | 70–110 € | ★★★★★ | ★★★★★ |
| UBIBOT GS1 4G | 2–5 W | Via scénario cloud | 120–180 € | ★★★★ | ★★★★ |
| NB-IoT capteur + prise 4G | < 1–2 W | Oui (via cloud) | 150–300 € | ★★ | ★★★★★ |
| Juste capteur + SMS manuel | 0,5–2 W | Manuel | 80–150 € | ★★★ | ★★★ |

### Mon conseil perso (ce que je ferais à ta place)

Prends directement une **prise SimPal T420** (ou le modèle 2026 équivalent, la gamme existe toujours) :

- Tu la branches sur une prise normale
- Tu mets une nano-SIM pas chère
- Tu configures 2–3 seuils par SMS :

  - Si T < 8–10°C → allumer la pompe
  - Si T > 16–18°C → éteindre
  - Alerte SMS si T < 5°C (grand danger gel)

→ Consommation ridicule (~2 W × 24 h × 90 jours ≈ 4,3 kWh pour 3 mois → 1–1,5 € sur facture EDF) → Pas besoin de box, pas de WiFi, ultra fiable → Tu reçois la température quand tu veux par SMS

Tu peux même demander à un proche de venir vérifier 1 fois dans les 3 mois si jamais tu stresses.

Tu veux que je te cherche les liens d’achat ou modèles équivalents les plus récents en 2026 ? 😊

---
