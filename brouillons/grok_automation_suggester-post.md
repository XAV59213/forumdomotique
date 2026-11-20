---
title: "Brouillon — grok_automation_suggester — RÉPONSE dans le sujet 192 — ne rien publier ni modifier sans le OK de Xavier"
description: "Action recommandée : publier la réponse complète ci-dessous (premier message non modifiable). Priorité basse : depuis juin 2025, uniquement de la…"
image: /assets/images/og-default.png
date: 2026-11-20
sitemap: false
robots: noindex, nofollow
---
# Brouillon — grok_automation_suggester — RÉPONSE dans le sujet 192 — ne rien publier ni modifier sans le OK de Xavier

**Sujet existant :** [🧠 Grok Automation Suggester – Des idées d’automatisations IA directement dans Home Assistant !](https://forumdomotique.com/forums/topic/192-%F0%9F%A7%A0-grok-automation-suggester-des-id%C3%A9es-dautomatisations-ia-directement-dans-home-assistant/) — Projets et Personnalisations — ouvert le 7 juin 2025 (v1.0.4/1.0.5), 1 seul message, aucune réponse.

**Action recommandée :** publier la **réponse complète** ci-dessous (premier message non modifiable). Priorité basse : depuis juin 2025, uniquement de la maintenance (traductions, CI, zip).

**Titre proposé :** (inchangé)

**État vérifié :** dépôt personnalisé (pas dans hacs/default, aucune demande) ; release v1.0.10 (31 oct. 2026) ; HA ≥ 2024.6.0 ; modèle par défaut `grok-3-latest` (const.py).

**Points à confirmer par Xavier :**
- Vaut-il la peine de publier ? Aucune nouveauté fonctionnelle depuis juin 2025.
- Le README dit la clé xAI « gratuite (ou premium) » : je ne l’ai pas repris, à vérifier côté xAI.
- Le modèle `grok-3-latest` est-il toujours valide chez xAI ?
- Captures de juin 2025 (v1.1.1 visible dessus, alors que les releases actuelles sont en 1.0.x) : en refaire ? Les noms réels des capteurs sur la capture sont `sensor.grok_automation_suggester_status` / `_suggestions`, pas ceux du README.

**Mise en forme Invision :** coller dans l’éditeur visuel ; `###` = intertitre ; images insérées par leur URL ; le bouton « Ouvrir dans HACS » = image du badge sur laquelle on pose le lien.

---

## Réponse complète à publier dans le sujet

Bonjour à tous 👋

Petite mise à jour de ce sujet, avec une présentation complète et à jour de **Grok Automation Suggester** 🧠, pour ceux qui la découvrent comme pour ceux qui l’utilisent déjà. La version actuelle est la **[v1.0.10](https://github.com/XAV59213/grok_automation_suggester/releases/tag/v1.0.10)**, et l’installation se fait via un **dépôt HACS personnalisé**.

👉 **Le plus simple :** cliquez sur ce bouton. Un clic ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=grok_automation_suggester&category=integration)

![Grok Automation Suggester](https://raw.githubusercontent.com/XAV59213/grok_automation_suggester/main/images/Grok-Logo-Text-512x256.png)

### 🤔 À quoi ça sert, concrètement ?

Quand on débute avec Home Assistant, on a souvent plein d’appareils… et peu d’idées pour les faire travailler ensemble. Grok Automation Suggester demande à l’intelligence artificielle **Grok** de **xAI** de regarder vos entités (lumières, capteurs, interrupteurs…) et de vous **proposer des idées d’automatisations**, avec le code YAML prêt à copier, et une bonne dose d’humour intergalactique 🚀

Par exemple : « Yo, j’ai repéré ton détecteur de mouvement dans le salon, et je pense que ta lampe pourrait s’allumer toute seule le soir. Voici une idée… »

Les suggestions arrivent dans une **notification** de Home Assistant et dans un capteur. Rien n’est appliqué automatiquement : c’est vous qui choisissez ce que vous gardez.

### ✨ Ce qui a changé depuis juin 2025

Pas de grosse nouveauté fonctionnelle, surtout de l’entretien :

- 🌍 l’interface en **français et en anglais**
- 🧹 un manifest allégé (les bibliothèques fournies par Home Assistant ne sont plus redemandées) et une validation automatique **HACS** et **Hassfest** à chaque modification
- 📦 une installation propre via HACS (archive dédiée, compteur de téléchargements)
- 🏷️ une icône officielle et une licence MIT

### 🔑 Étape 0 : une clé API xAI

1. Connectez-vous sur https://console.x.ai
2. Créez une **clé API** et gardez-la de côté : l’assistant d’installation vous la demandera

⚠️ L’utilisation de l’API est soumise aux conditions et aux tarifs de xAI : vérifiez-les sur la console avant de lancer de grosses analyses.

### 🛠️ Installation pas à pas (dépôt personnalisé HACS)

*Pour ceux qui débutent : HACS, c’est un peu le « magasin d’applications » communautaire de Home Assistant. Il permet d’installer et de mettre à jour en quelques clics des intégrations qui ne sont pas fournies d’origine. S’il n’est pas encore installé chez vous, le guide officiel est ici : https://hacs.xyz/docs/use/*

L’intégration n’est pas (encore) dans la bibliothèque HACS par défaut : on l’ajoute comme **dépôt personnalisé**, ça prend trente secondes.

**Le plus rapide :** un clic sur ce bouton ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=grok_automation_suggester&category=integration)

**Ou à la main :**

1. Dans Home Assistant, ouvrez **HACS** dans le menu de gauche
2. Cliquez sur les **⋮** en haut à droite, puis sur **Dépôts personnalisés**
3. Collez l’adresse `https://github.com/XAV59213/grok_automation_suggester`, choisissez le type **Intégration**, puis **Ajouter**
4. Cherchez **Grok Automation Suggester** dans HACS, ouvrez la fiche et cliquez sur **Télécharger**
5. Redémarrez Home Assistant (**Paramètres > Système > bouton ⏻ en haut à droite > Redémarrer**)
6. Allez dans **Paramètres > Appareils et services > + Ajouter une intégration**, et cherchez **Grok Automation Suggester**

⚠️ HACS ne fait que **télécharger les fichiers** : ce sont le redémarrage et l’étape 6 qui créent réellement l’intégration et ses entités.

À l’étape 6, collez votre clé API. Vous pouvez aussi choisir le modèle (par défaut `grok-3-latest`), le nombre maximum de tokens, etc. Il faut Home Assistant **2024.6** ou plus récent.

Raccourci pour l’étape 6 : https://my.home-assistant.io/redirect/config_flow_start/?domain=grok_automation_suggester

![Les capteurs créés par l’intégration](https://raw.githubusercontent.com/XAV59213/grok_automation_suggester/main/images/Capture%20d%E2%80%99%C3%A9cran%20du%202025-06-06%2018-22-56.png)

### 🎯 Demander des idées

Allez dans **Outils de développement > Actions** et lancez `grok_automation_suggester.generate_suggestions` :

- `all_entities` : `true` pour analyser toutes vos entités, `false` pour seulement les nouvelles
- `custom_prompt` (facultatif) : par exemple « Crée des automatisations pour économiser l’énergie »

Les idées arrivent dans une **notification** de Home Assistant, et la version complète est enregistrée dans le fichier `grok_suggestions.yaml` de votre configuration. Deux capteurs résument tout : **Suggestions** (le résumé des dernières idées) et **Status**, qui indique si la connexion à l’API fonctionne.

![Les suggestions complètes, enregistrées dans grok_suggestions.yaml](https://raw.githubusercontent.com/XAV59213/grok_automation_suggester/main/images/Capture%20d%E2%80%99%C3%A9cran%20du%202025-06-06%2018-26-13.png)

Merci au projet d’origine **ai_automation_suggester**, dont cette intégration s’inspire.

### 🔗 Liens

- Dépôt GitHub : https://github.com/XAV59213/grok_automation_suggester
- Dernière version (v1.0.10) : https://github.com/XAV59213/grok_automation_suggester/releases/tag/v1.0.10
- Signaler un bug ou proposer une idée : https://github.com/XAV59213/grok_automation_suggester/issues

Vos retours, idées et remontées de bugs sont les bienvenus, ici ou sur GitHub 😉

Bonne domotique ! 🏠
Xavier (XAV59213)
