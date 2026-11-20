---
title: "Relier Home Assistant au chauffage Daikin via passerelle Modbus, BACnet ou KNX"
---

# Relier Home Assistant au chauffage Daikin via passerelle Modbus, BACnet ou KNX

- **Catégorie :** [Autres Protocoles Domotiques](https://forumdomotique.com/forums/65-autres-protocoles-domotiques/)
- **Sujet :** https://forumdomotique.com/forums/topic/482-relier-home-assistant-au-chauffage-daikin-via-passerelle-modbus-bacnet-ou-knx/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 4 novembre 2025 à 16:14 (Europe/Paris)

---

## Message 1 — 4 novembre 2025 à 16:14 (Europe/Paris)

- **Identifiant :** `1152`
- **Lien :** https://forumdomotique.com/forums/topic/482-relier-home-assistant-au-chauffage-daikin-via-passerelle-modbus-bacnet-ou-knx/#findComment-1152

> **il y a 11 minutes, CDRN a dit :**
> Bonjour,
>
> Je vous présent ma situation afin d'obtenir de l'aide dans le développement de solution domotique. Dans mon cadre professionnel, nous allons déménager dans des nouveaux locaux qui sont en cours de rénovation. J'ai réussi à négocier pour ajouter un peu de domotique pour faire des tests. J'envisage notamment d'avoir une box (soit Rasperry ou Home Assistant green) sous Zigbee (via Home Assistant) afin de piloter l'éclairage.
>
> En complément, des nouveaux caissons de chauffage vont être installés de la marque DAIKIN et l'entreprise qui les installe me confirme qu'il est possible d'ajouter des passerelles fonctionnant sous l'un des protocole suivant : Modbus, Bacnet ou KNX. Mon objectif serait de piloter le chauffage à distance en fonction de la présence de personne et ou de l’ouverture de fenêtre.
>
> C'est à partir de là que mes jeunes compétences en domotique sont bloquées car je ne vois pas comment communiquer entre ma box (via Home Assistant) et le caisson de chauffage ?
>
> Mes recherches internet, me poussent vers un équipement supplémentaire sur ma box afin de communiquer avec la passerelle qui sera sur le caisson de chauffage ? et également avec quel protocole Modbus, Bacnet ou KNX ?
>
> Merci de vos conseils, en espérant avoir été assez clair dans mes explications.

Salut [@CDRN](https://forumdomotique.com/profile/617-cdrn/) et bienvenue !

Parmi les trois protocoles, **KNX est de loin le plus adapté pour ton objectif** (pilotage à distance basé sur présence ou ouverture de fenêtre). Voici pourquoi :

- **Intégration native et mature dans Home Assistant** : HA a une intégration KNX officielle et hyper robuste (dispo directement dans les intégrations). Tu pourras exposer les capteurs de présence/ouverture de fenêtre (via Zigbee) comme des entités HA, et les lier facilement à des automatisations qui envoient des commandes au chauffage Daikin via KNX. Pas besoin de bidouiller des scripts complexes.
- Si tu as besoin de ressources :

  - Doc HA pour KNX : [home-assistant.io/integrations/knx](https://home-assistant.io/integrations/knx)

### Conseil matos pour ta box HA

**Je te conseille un Raspberry Pi 5 en SSD NVMe** (via un HAT PCIe genre Pimoroni ou Geekworm) : c’est ultra réactif, fiable, et ça supporte sans broncher KNX + Zigbee + plusieurs automatisations lourdes.

Le Green est sympa mais un poil limité en perf pour un usage pro/test intensif.

**Exemple de backup en cas de coupure opérateur** : Ajoute un module 4G/LTE comme le mien, le [**Waveshare SIM7600E-H**](https://www.amazon.fr/Waveshare-SIM7600E-H-High-Speed-Connection-Positioning/dp/B07DYJH8N2). Je viens de le recevoir sur mon RPi5, et ça permet un failover automatique vers la 4G si la box Internet lâche. → HA reste accessible à distance, les automatisations tournent, et tu perds zéro contrôle.

**Je ferai un tuto complet d’installation (driver, configuration ModemManager + failover réseau dans HA) dès que j’ai tout testé – je posterai sur le forum .**

Promis, plus jamais de coupure qui plombe le système 🤪 !

---
