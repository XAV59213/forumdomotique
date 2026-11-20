---
layout: ha-release
title: "Home Assistant 2026.2 : le dashboard Home devient la vue par défaut, les add-ons deviennent des Apps"
short_title: "2026.2 : Home par défaut, add-ons → Apps"
description: "Home Assistant 2026.2 (4 février 2026) en français : dashboard Home par défaut, base de données d’appareils de l’Open Home Foundation, add-ons renommés Apps, nouvelle recherche rapide Ctrl+K, carte Distribution et breaking changes."
excerpt_fr: "Le dashboard Home devient « Overview », la Device Database de l’Open Home Foundation arrive dans Labs, les add-ons s’appellent désormais Apps et la recherche rapide Ctrl+K est entièrement repensée."
image: /actualite-home-assistant/home-assistant-2026-2/images/cover.png
cover_alt: "Couverture : nouveautés de Home Assistant 2026.2, février 2026"
date: 2026-02-04
release_date: 2026-02-04
section: actualite-ha
version: "2026.2"
month: "Février 2026"
official_title: "2026.2: Home, sweet overview"
release_url: https://www.home-assistant.io/blog/2026/02/04/release-20262/
changelog_url: https://www.home-assistant.io/changelogs/core-2026.2/
forum_url: https://forumdomotique.com/actualites/home-assistant/home-assistant-20262-la-mise-%C3%A0-jour-de-f%C3%A9vrier-2026-rend-le-dashboard-home-par-d%C3%A9faut-et-lance-la-device-database-r12/
tags: [home-assistant, mise-a-jour, 2026.2]
seo:
  type: NewsArticle
gallery:
  - src: images/new-overview.webp
    caption: "Le nouveau dashboard Overview (ex-Home), vue par défaut des nouvelles installations."
  - src: images/discovered-devices.webp
    caption: "Les appareils découverts s’ajoutent directement depuis la section « For You »."
  - src: images/assign-devices-page.webp
    caption: "La page Appareils propose d’affecter rapidement chaque appareil à une pièce."
  - src: images/device-database-statistics.webp
    caption: "Le tableau public de statistiques de la base de données d’appareils de l’Open Home Foundation."
  - src: images/labs-device-database-analytics.webp
    caption: "L’option de partage anonyme des appareils, à activer dans Labs."
  - src: images/addons-are-now-apps.webp
    caption: "Dans le menu Paramètres, « Add-ons » devient « Apps »."
  - src: images/quick-search.webp
    caption: "La nouvelle recherche rapide (Ctrl+K / ⌘+K) avec ses filtres par catégorie."
  - src: images/distribution-card.webp
    caption: "La carte Distribution : la répartition d’une grandeur (puissance, stockage…) entre plusieurs entités."
  - src: images/heading-card-buttons.webp
    caption: "Des boutons d’action dans la carte de titre."
---

<p class="forum-cta">Cet article reprend et met à jour <a href="https://forumdomotique.com/actualites/home-assistant/home-assistant-20262-la-mise-%C3%A0-jour-de-f%C3%A9vrier-2026-rend-le-dashboard-home-par-d%C3%A9faut-et-lance-la-device-database-r12/">mon actualité publiée sur Forum Domotique</a>, vérifiée point par point avec les notes officielles.</p>

Après une 2026.1 plus calme post-fêtes, l’équipe frappe fort avec la **2026.2**, sortie le **4 février 2026** (« le mois de l’amour », selon Frenck 💝). Au programme : le dashboard **Home devient la vue par défaut**, la **base de données d’appareils** de l’Open Home Foundation fait appel à la communauté, les **add-ons sont renommés Apps**, et la **recherche rapide** est entièrement repensée.

<div class="ha-callout info" markdown="1">
**En bref**
- 🏠 Le dashboard Home devient **Overview**, la vue par défaut des nouvelles installations.
- 🔍 **Device database** : partage anonyme et volontaire (opt-in) de vos appareils, via Labs.
- 📦 Les **add-ons deviennent des Apps**.
- ⌨️ **Quick search** (Ctrl+K / ⌘+K) : naviguer, lancer une commande, trouver une entité.
- 📊 Nouvelle **carte Distribution** et premières **conditions par usage** dans Labs.
</div>

## ✨ Les nouveautés phares

### 🏠 Le dashboard Home devient la norme

Le dashboard **Home** que l’on testait depuis plusieurs mois prend le nom d’**Overview** et devient **la vue par défaut de toutes les nouvelles installations**. Si vous utilisez Home Assistant depuis longtemps **sans avoir personnalisé** votre vue par défaut, Home Assistant vous suggère de basculer ; sinon, il reste disponible dans **Paramètres › Tableaux de bord** pour l’essayer quand vous voulez.

{% include ha-figure.html src="images/new-overview.webp" caption="Le nouvel Overview : un tableau de bord généré automatiquement, centré sur vos pièces." %}

- Vous aimiez l’ancien Overview pour bâtir vos propres dashboards ? **Paramètres › Tableaux de bord › Créer**, puis le modèle **Overview (legacy)**.
- Les **appareils découverts** apparaissent dans une carte de la section **For You** : on les ajoute sur place, sans fouiller dans les menus.
- La page **Appareils** (apparue en 2026.1) propose maintenant d’affecter chaque appareil à la bonne pièce.
- Le bouton **Modifier** des pages de pièce mène directement aux réglages de la pièce (capteur de température ou d’humidité principal).
- Le thème par défaut abandonne la **barre supérieure bleue** pour un look plus sobre, et les **thèmes se règlent par utilisateur** depuis le profil.

C’est le plus gros changement d’ergonomie depuis longtemps : le dashboard est centré sur « ce qui se passe chez vous » plutôt que sur une liste technique.

### 🔍 Device database : la communauté à la rescousse (opt-in !)

Trouver des informations fiables sur un appareil avant de l’acheter n’est pas simple. L’**Open Home Foundation** construit donc une **base de données d’appareils** alimentée par des données réelles. Avant même l’appel officiel, plus de **10 000 appareils uniques** issus de plus de **260 intégrations** avaient été partagés par des utilisateurs volontaires.

{% include ha-figure.html src="images/sharing-your-devices-with-ohf-device-database.webp" caption="L’option de partage des appareils dans les Analytics de Home Assistant." %}

**Pour participer, pas à pas :**
1. Ouvrez **Paramètres › Système › Labs** et activez l’analyse des appareils (*device analytics*).
2. Une section **Device analytics** apparaît dans **Home Assistant Analytics**.
3. Avant d’envoyer quoi que ce soit, utilisez **Preview device analytics** (en haut à droite) pour voir exactement ce qui serait partagé.

🔒 **Aucune donnée personnelle** n’est collectée : seules des informations agrégées et anonymisées sont transmises, et l’on peut se retirer à tout moment.

### 📦 Les add-ons deviennent des Apps

Gros changement de vocabulaire : les **add-ons s’appellent désormais des Apps**. La raison est simple : « Add-ons » et « Intégrations » sonnaient pareil, et les nouveaux venus installaient l’un à la place de l’autre. Votre téléviseur a des applis, votre téléphone aussi… Home Assistant aussi, désormais.

{% include ha-figure.html src="images/addons-are-now-apps.webp" caption="Le menu Paramètres affiche maintenant « Apps » à la place de « Add-ons »." %}

Rien à réinstaller : vos modules existants (Mosquitto, ESPHome, Frigate…) restent en place, seul le nom change dans l’interface.

### ⌨️ Quick search : le chemin le plus court vers tout

La « quick bar » est remplacée par **Quick search**, un véritable centre de commande : naviguer, lancer une commande, trouver une entité, un appareil ou une pièce. On l’ouvre partout avec **Ctrl + K** (Windows/Linux) ou **⌘ + K** (macOS). Des filtres en haut (**Navigate**, **Commands**, **Entities**, **Devices**, **Areas**) affinent les résultats ; flèches, Entrée et Échap suffisent pour tout faire au clavier. Sur mobile, on peut l’associer à un geste.

{% include ha-figure.html src="images/quick-search.webp" caption="Quick search et ses filtres par catégorie." %}

Les raccourcis historiques fonctionnent toujours : `e` (entités), `d` (appareils), `c` (commandes), `a` (Assist) et `m` (créer un « My link » de la page).

### 🤖 Automatisations : les conditions par usage arrivent (Labs)

Nouveaux déclencheurs : **calendrier** (début/fin d’un évènement), **personne** (arrivée/départ) et **aspirateur** (retour à la base). Surtout, une première série de **conditions par usage** : alarme armée/désarmée/déclenchée, satellite Assist, climat (chauffe, refroidit…), présence, ventilateur, humidificateur, tondeuse, serrure, lecteur multimédia, personne, sirène, interrupteur et aspirateur. On écrit « **Si la serrure est verrouillée** » plutôt que de comparer un état.

À activer dans **Paramètres › Système › Labs**.

### 📊 La carte Distribution

Nouvelle carte qui affiche, sous forme de barre horizontale proportionnelle, **la répartition d’une grandeur entre plusieurs entités** : quels circuits consomment le plus en ce moment, comment se répartit le stockage… La légende est interactive (les pourcentages se recalculent quand on masque une entité) et la carte vérifie que les entités sont comparables (même domaine, même classe ; W et kW se mélangent sans souci).

## 🧩 Nouvelles intégrations

✅ Six ajouts :

- **Cloudflare R2** : sauvegardes vers R2 (offre gratuite généreuse, pas de frais de sortie).
- **Green Planet Energy** : prix dynamiques de l’électricité de ce fournisseur allemand.
- **HDFury** : boîtiers vidéo HDMI (VRROOM, Diva…).
- **NRGkick** : chargeur mobile de véhicule électrique NRGkick Gen2, en local.
- **Prana** : VMC double flux Prana.
- **uHoo** : capteurs de qualité de l’air intérieur.

**Namecheap DynamicDNS**, **OpenEVSE**, **Proxmox VE** et **WaterFurnace** se configurent désormais depuis l’interface.

## 🔧 Améliorations notables

- **ESPHome** gère les **chauffe-eau** ; **Music Assistant** les sons de pré-annonce ; **Spotify** les « Titres likés » ; **Sonos** les podcasts favoris.
- **Reolink** : carillon spécial animaux ; **Hikvision** : caméras ; **Powerfox** : compteurs de gaz.
- Les **Outils de développement** (*Tools*) rejoignent la zone **Paramètres**.
- **Calendriers en couleur** dans les cartes, **prévisualisation en direct** dans l’éditeur de templates, **Paramètres** toujours visible en bas de la barre latérale.
- **Carte de titre** avec boutons d’action ; **carte de pièce** où l’on choisit précisément les entités affichées.
- Le **tableau Énergie** accepte des capteurs de puissance à polarité inversée sans template.

## ⚠️ Breaking changes à surveiller

- **Groupes de capteurs** : un groupe devient indisponible si tous ses membres sont indisponibles ou absents.
- **Sentry** (auto-hébergé) : serveur 20.6.0 minimum.
- **Tractive** : capteurs `activity`, `calories burned` et `sleep` supprimés.
- **Tuya** : les modes HVAC en double sont convertis en *presets*.
- **VeSync** : le preset `advanced_sleep` devient `sleep`.

## 🩹 Versions correctives

Après chaque version mensuelle, Home Assistant publie des versions correctives (en principe une par semaine, le vendredi) qui ne contiennent que des corrections de bugs et des mises à jour de bibliothèques. Voici le détail de celles de la **2026.2**, d’après la liste officielle des changements. Le nombre indiqué compte tous les changements listés, mises à jour de bibliothèques comprises.

{% include ha-patches.html key="2026-2" %}

## 💾 Conseil de mise à jour

1. **Sauvegarde complète** avant tout (Paramètres › Système › Sauvegardes).
2. Si vos scripts appellent des add-ons, rassurez-vous : seul le nom change dans l’interface.
3. Mettez à jour depuis **Paramètres › Système › Mises à jour**, de préférence vers la dernière version corrective.

## 📋 Résumé des nouveautés

| Fonctionnalité | Description | Impact |
| --- | --- | --- |
| Overview (ex-Home) par défaut | Appareils découverts visibles, affectation aux pièces | Ergonomie familiale |
| Device database | Partage anonyme et volontaire | Meilleure compatibilité future |
| Add-ons → Apps | Nouveau nom, rien à réinstaller | Plus clair pour les débutants |
| Quick search Ctrl+K | Accès instantané à tout | Gain de temps |
| Conditions par usage (Labs) | Alarme, serrure, climat… | Automatisations lisibles |
| Carte Distribution | Répartition d’une grandeur | Suivi énergie |

<div class="ha-avis" markdown="1">
### 💬 L’avis de Xavier

Cette 2026.2 marque un virage : Home Assistant parle enfin comme ses utilisateurs (Apps, Overview, conditions « par usage »). Pour un débutant, la différence est énorme. La Device database mérite qu’on y participe : plus elle est riche, plus il sera simple de choisir du matériel compatible. Et si vous ne deviez retenir qu’un raccourci : **Ctrl + K**.
</div>

Qu’en pensez-vous de cette 2026.2 ? Prêt à partager vos appareils ? Réagissez sur [Forum Domotique](https://forumdomotique.com/actualites/home-assistant/home-assistant-20262-la-mise-%C3%A0-jour-de-f%C3%A9vrier-2026-rend-le-dashboard-home-par-d%C3%A9faut-et-lance-la-device-database-r12/) !

<p class="ha-signature">— Xavier (XAV59213)</p>
