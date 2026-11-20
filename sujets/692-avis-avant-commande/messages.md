---
title: "Avis avant commande ?"
---

# Avis avant commande ?

- **Catégorie :** [Bien débuter en domotique](https://forumdomotique.com/forums/99-bien-d%C3%A9buter-en-domotique/)
- **Sujet :** https://forumdomotique.com/forums/topic/692-avis-avant-commande/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 18 janvier 2026 à 12:04 (Europe/Paris)
- **Dernier message de XAV59213 :** 31 janvier 2026 à 09:56 (Europe/Paris)

---

## Message 1 — 18 janvier 2026 à 12:04 (Europe/Paris)

- **Identifiant :** `1813`
- **Lien :** https://forumdomotique.com/forums/topic/692-avis-avant-commande/#findComment-1813

Bonjour [@Player211](https://forumdomotique.com/profile/1145-player211/) ,

Merci pour ton message détaillé et bravo pour ton projet !

C'est effectivement le bon moment pour câbler une maison en pensant domotique dès le départ, ça évite beaucoup de galères après.

Concernant ton choix d'**interrupteurs Schneider Wiser Ovalis (réf. S320567W)** pour les volets roulants :

### Compatibilité avec SmartThings

Malheureusement, **ça ne va pas être simple ni fiable** avec un hub SmartThings (que ce soit l'ancien V3, l'Aeotec, ou autre).

- Ces interrupteurs sont en **Zigbee** (probablement Zigbee 3.0), mais Schneider Wiser utilise souvent des implémentations un peu "propriétaires" ou des clusters pas totalement standards.
- Dans la communauté SmartThings, très peu de retours positifs sur les interrupteurs muraux Wiser Ovalis/Odace récents (quelques vieux modèles plugs ou boutons marchent parfois avec driver custom, mais les volets roulants posent souvent problème : pairing capricieux, fonctionnalités partielles, pas de calibration de temps de montée/descente, etc.).
- Tu risques de devoir bricoler des drivers communautaires (pas toujours maintenus) et d'avoir une expérience décevante.

Bref : **SmartThings n'est pas le meilleur choix si tu veux utiliser ces interrupteurs précis.**

### Ma recommandation pour ton cas

Vu que tu refais toute l'électricité, que tu veux beaucoup de matériel Schneider (ou compatible esthétique), et que tu es motivé pour apprendre, je te conseille très fortement de partir sur **Home Assistant** plutôt que SmartThings.

**Pourquoi Home Assistant est beaucoup plus adapté ici ?**

- Les interrupteurs Wiser Ovalis volets (S320567W) + la plupart des autres produits Wiser Zigbee récents marchent **très bien** avec :

  - **ZHA** (l'intégration native Zigbee de Home Assistant) → simple et suffisant pour la majorité des gens
  - **Zigbee2MQTT** (plus puissant, plus de possibilités de configuration fine) → ma reco perso pour les Schneider
- Tu pourras calibrer les temps de montée/descente des volets (ce que beaucoup de gens ne peuvent pas faire en direct avec ZHA seul, mais que Zigbee2MQTT permet souvent).
- Tu gardes un contrôle **100% local**, très stable, et tu peux ajouter quasiment n'importe quelle marque plus tard (Aqara, Sonoff, Ikea, Tuya, Philips, etc.).
- Tu peux aussi utiliser **Home Assistant** avec l'app mobile très correcte (ou même Companion app) et l'intégrer avec Google/Alexa si tu veux vraiment une expérience "style SmartThings".

### Alternative "tout SmartThings" si tu tiens vraiment à cette app

Dans ce cas, il vaut mieux regarder :

- Les modules **fibaro FGR-223** / **Qubino** / **Z-Wave** pour les volets (plus cher mais compatibilité officielle excellente)
- Ou les micromodules **behind-switch** Zigbee de marques mieux supportées (Tuya rebrandés, Aqara, etc.)
- Mais tu perds l'esthétique Schneider Ovalis que tu sembles apprécier.

Si tu te lances dans Home Assistant, la communauté française est très active (plein de tutos en français) et tu vas apprendre énormément, surtout vu ta motivation !

N'hésite pas si tu veux des conseils plus précis sur le choix de la clé Zigbee ou la config des volets Schneider, je peux t'aider.

Bon courage pour le chantier électrique, c'est un gros projet mais tellement satisfaisant quand c'est fini ! 💪

---

## Message 2 — 31 janvier 2026 à 09:56 (Europe/Paris)

- **Identifiant :** `1926`
- **Lien :** https://forumdomotique.com/forums/topic/692-avis-avant-commande/#findComment-1926

Bonjour @Player211,

Super choix pour Home Assistant !

Pour le hub, opte pour le HA Green si tu veux du prêt-à-l’emploi avec Zigbee intégré simple et efficace. Sinon, un Raspberry Pi 4ou 5 avec un Sonoff Dongle Plus-E pour plus de flexibilité.

Tes interrupteurs Schneider s’intègrent bien : commence par ZHA pour la facilité, ou passe à Zigbee2MQTT pour calibrer précisément les volets.

Pour le réseau Zigbee, tes volets filaires serviront de relais mesh, ce qui devrait couvrir une maison de plain-pied sans souci. Si besoin, ajoute quelques prises connectées comme Sonoff ou Aqara pour booster les zones faibles.

Côté interrupteurs sans fil, c’est idéal pour éviter les travaux : des modèles à pile comme l’Aqara Mini Switch (15€) ou Philips Hue Dimmer (20€), ou sans pile (kinetic) comme les Moes Zigbee (20-30€). Colle-les où tu veux et lie-les via automatisations dans HA.

Pour les lumières, pas forcé d’utiliser des ampoules connectées installe plutôt des micromodules Zigbee (Qubino ou Fibaro, ~30€) derrière tes interrupteurs existants, ou passe aux ampoules Zigbee qui font aussi relais.

Paire d’abord tes volets pour tester, et rejoins la communauté HA française pour des tutos. Bonne continuation, ça va être top ! 💡

---
