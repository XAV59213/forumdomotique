---
title: "domotiser un appartement"
description: "@Ellywick a tout à fait raison : si vous voulez débuter à moindre coût, Zigbee est actuellement la meilleure solution Home Assistant est un logiciel…"
image: /assets/images/og-default.png
date: 2025-06-22
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/205-domotiser-un-appartement/">Lire et commenter sur Forum Domotique</a></p>

# domotiser un appartement

- **Catégorie :** [Bien débuter en domotique](https://forumdomotique.com/forums/99-bien-d%C3%A9buter-en-domotique/)
- **Sujet :** https://forumdomotique.com/forums/topic/205-domotiser-un-appartement/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 22 juin 2025 à 11:42 (Europe/Paris)

---

## Message 1 — 22 juin 2025 à 11:42 (Europe/Paris)

- **Identifiant :** `508`
- **Lien :** https://forumdomotique.com/forums/topic/205-domotiser-un-appartement/#findComment-508

Bonjour [@Charli](https://forumdomotique.com/profile/192-charli/) ,

[@Ellywick](https://forumdomotique.com/profile/131-ellywick/) a tout à fait raison : si vous voulez débuter à moindre coût, Zigbee est actuellement la meilleure solution.

### Proposition : Installation légère de Home Assistant

Home Assistant est un logiciel open-source flexible que vous pouvez installer sur du matériel peu gourmand, idéal pour une approche "green" (faible consommation énergétique). Voici une configuration recommandée :

#### 1. Matériel : Raspberry Pi ou green de home assistant

- **Modèle** : **Raspberry Pi 4 (2 Go ou 4 Go)** – Consommation : environ 3-5W, parfait pour une solution écologique.

  - **Prix** : **50-100 €** (incluant une carte microSD 32 Go à ~10 € et un boîtier à ~5-10 €).

##### . NABU CASA - Box domotique Home Assistant Green 99,99

#### 2. Logiciel : Home Assistant OS

- **Version** : Utilisez la dernière version stable de **Home Assistant OS** (disponible sur le site officiel [home-assistant.io](https://home-assistant.io), actuellement v2025.6 au 22/06/2025). Cette version est optimisée pour une installation autonome.
- **Installation** : Téléchargez l’image, gravez-la sur la carte microSD avec un outil comme Balena Etcher, et configurez via l’interface web après démarrage.
- **Avantage** : Léger, mis à jour régulièrement.

#### 3. Clé Zigbee

- **Modèle** : **Sonoff ZBDongle-P** – Prix : **26.99 €**.
- **Raison** : Compatible avec Home Assistant, supporte le protocole Zigbee 3.0, et permet de connecter vos modules (ex. Sonoff ZBMini) sans hub supplémentaire. Consommation négligeable.

#### 4. Modules Zigbee

- **Recommandation** : **Sonoff ZBMini** – Prix : **11-15 € par unité** (pack de 4 à **45-50 €**).
- **Usage** : Installez-les derrière vos interrupteurs sans neutre pour contrôler les lumières, en les intégrant via Zigbee à Home Assistant.

#### 

### Coût total estimé

- Raspberry Pi 4 + accessoires : **65-100 €**

  [**lien**](https://www.amazon.fr/Raspberry-Starter-Alimentation-dissipateur-Thermique/dp/B0D1N3V2FF/ref=sr_1_6?adgrpid=56878558740&dib=eyJ2IjoiMSJ9.7lI8eeW17wtaJWRLUUnFSQhodaYcuUFfg_3JSi7YaZ_Vg34E9hhDFUWg5LE1RJLuGC6uzgZYlsacd42PUO4vbJN7P78jIUTRtLM-4vHo9zF0C35IzmMRzrIBJrAtzThQBNwbn9Gheu0l8w8c-JSRbqwrX8PoXKVBx3jzx8lthAq30xOMIc715M7AjP87RbSB3dhApOcV82Ez5VmWZWuWysh-EAq7647YLOdorI5V55Wm0_sncVlyZtihm8XFSn9WM4I0bjYhyFYszNard45bKVeEs-GSbrRKINASCsytiVs.424vfG7OXB_k2CZl8o1M01m7cV7OjsasdVJMuLosTOU&dib_tag=se&hvadid=601473472443&hvdev=c&hvexpln=0&hvlocphy=9111005&hvnetw=g&hvocijid=8908760317188718400--&hvqmt=e&hvrand=8908760317188718400&hvtargid=kwd-297124344473&hydadcr=7972_2270202&keywords=raspberry%2Bpi%2B4&mcid=8719601d1747324cb2e05e6897a1054d&qid=1750584338&sr=8-6&ufe=app_do%3Aamzn1.fos.49fccda8-a887-4188-817b-b9a64bb30e43&th=1)

- Home Assistant Green **99.99 €**

  [**lien**](https://www.domadoo.fr/fr/produits-compatibles-home-assistant/7046-nabu-casa-box-domotique-home-assistant-green-0860011789703.html?srsltid=AfmBOor6csIXmoG6s5Nn4B8y8mJ7GDTvF8aEGXhGi4lGYtZCOzfzlgAG)
- Sonoff ZBDongle-P : **26,99€**

[**lien**](https://www.amazon.fr/EFR32MG21-Coordinator-Universelle-Passerelle-Assistant/dp/B0B6P22YJC/ref=sr_1_2_sspa?crid=38A46NCN78Y7G&dib=eyJ2IjoiMSJ9.SYktf_nn6nX89F-4f3uNUNlobJANY2ykfkwatpryIGpdlY65ipgcvmU1xOlXqA6fRgjlCm8-fRonPpMs01F8NVvDKf-KO0Rg4zLl0kGAcgvw9iHN3lxxP7YwAKCtUdWi9aOqBqcdOjDUjvt8BGLzdiSROz0yZJLcAsMZWiD-Uz28GQGhDfgowlC4kPWmrkyZ33xY4fnnhyhnEC-XOYwhI-unWVhRC0RZzckDSBGZtFn7cerWEw17g7su6l57Bsw2sU3EZF_mjLMpXXM1M04KPhsFAhqprYZUpQ8Z98KXdbk.nwHUtImWNYh1cfGezGZPytNaSosIz4XTWbFV_uY48Sw&dib_tag=se&keywords=cles+zigbee&qid=1750584614&sprefix=cles+zig%2Caps%2C78&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)

- 4 x Sonoff ZBMini : **45-50 €**

[**lien**](https://www.amazon.fr/SONOFF-ZBMINIL2-Interrupteur-Compatible-Assistant/dp/B0BYJDDZZH?ref_=ast_sto_dp)

### Ou sinon, moins cher mais si tu as de la patience, tu peux installer sur un vieux PC.

[@Zatoufly](https://forumdomotique.com/profile/84-zatoufly/)

<https://www.youtube-nocookie.com/embed/Hth7xcKEpiM?list=PL3mnzRbk5wWZXmsNdGNz9XkmzdXLDt33k>

[@Howmation](https://forumdomotique.com/profile/206-howmation/)

<https://www.youtube-nocookie.com/embed/RRthYeq2fSM?feature=oembed>

---
