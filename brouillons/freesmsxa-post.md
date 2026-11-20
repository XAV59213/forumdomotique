---
title: "Brouillon — freesmsxa — RÉPONSE dans le sujet 110 — ne rien publier ni modifier sans le OK de Xavier"
description: "Action recommandée : publier la réponse complète ci-dessous dans le sujet existant. Le forum ne permet plus de modifier le premier message (délai de…"
image: /assets/images/og-default.png
date: 2026-11-20
sitemap: false
robots: noindex, nofollow
---
# Brouillon — freesmsxa — RÉPONSE dans le sujet 110 — ne rien publier ni modifier sans le OK de Xavier

**Sujet existant :** [📨 Free Mobile SMS XA – Intégration Home Assistant](https://forumdomotique.com/forums/topic/110-%F0%9F%93%A8-free-mobile-sms-xa-int%C3%A9gration-home-assistant/) — Projets et Personnalisations — ouvert le 3 mai 2025 (v. V.4/V.6.5.2025, dépôt perso, `notify.papa_sms`, journal de 10 messages), 8 messages ; dernier : cc2i le 26 sept. 2026 (carte « Envoyer un SMS » absente chez lui). Xavier a fait un point le 25 sept. 2026 (≥ 6.12.2). Sujets tutoriels liés : [353](https://forumdomotique.com/forums/topic/353-envoyer-des-sms-depuis-le-dashboard-home-assistant-avec-lint%C3%A9gration-free-mobile-sms-xa/) et [354](https://forumdomotique.com/forums/topic/354-configurer-lenvoi-de-notifications-sms-dans-vos-automatisations-home-assistant-via-free-mobile-sms-xa/) (24 août 2025), à laisser tels quels ou à compléter d’une ligne « installation désormais via HACS par défaut ».

**Action recommandée :** publier la **réponse complète** ci-dessous dans le sujet existant. Le forum ne permet plus de modifier le premier message (délai de modification dépassé), la réponse se suffit donc à elle-même : nouveautés, photos, installation pas à pas, bouton HACS. Annonce HACS par défaut (PR hacs/default#13029 fusionnée le 3 nov. 2026, pas encore annoncée) et la 6.12.13.

**Titre du sujet :** inchangé (le titre n’est sans doute plus modifiable non plus ; renommage éventuel à demander à Jack). Suggestion si renommage : 📨 Free Mobile SMS XA – Des SMS gratuits depuis Home Assistant (Free Mobile)

**État vérifié :** dans hacs/default ; release 6.12.13 (8 nov. 2026) ; HA ≥ 2025.12.0 (hacs.json). ⚠️ Le README décrit encore l’installation en dépôt personnalisé.

**Points à confirmer par Xavier :**
- Les 3 captures du dépôt datent de mai 2025 (assistant, lignes, page Free) : ajouter une capture récente de la carte « Envoyer un SMS » (déjà postée le 24 sept. 2026 dans le sujet) ?
- Libellé exact du menu Free (« Mes options » / « Gérer mes options ») et envoi d’un SMS de test à la création de la ligne : repris du README, à vérifier.
- Phrase adressée à @cc2i : à garder ou retirer.

**Mise en forme Invision :** coller dans l’éditeur visuel ; `###` = intertitre ; images insérées par leur URL ; le bouton « Ouvrir dans HACS » = image du badge sur laquelle on pose le lien.

---

## Réponse complète à publier dans le sujet

Bonjour à tous 👋

Grosse mise à jour pour ce sujet : voici une présentation complète et à jour de **Free Mobile SMS XA** 📨, mon intégration Home Assistant pour recevoir des **SMS** de votre maison, gratuitement, grâce à l’option « Notifications par SMS » de Free Mobile.

Grande nouvelle : depuis le 3 novembre 2026, elle fait partie de la **bibliothèque officielle de HACS** (ceux qui l’avaient en dépôt personnalisé n’ont rien à faire), et la version actuelle est la **[6.12.13](https://github.com/XAV59213/freesmsxa/releases/tag/6.12.13)**.

👉 **Le plus simple :** cliquez sur ce bouton. Un clic ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=freesmsxa&category=integration)

![Free Mobile SMS XA](https://raw.githubusercontent.com/XAV59213/freesmsxa/main/images/logo.png)

### 🤔 À quoi ça sert, concrètement ?

Les notifications de l’application Home Assistant, c’est bien… tant que le téléphone a du réseau data, que l’appli est à jour et que la notif n’est pas noyée au milieu des autres. Pour les alertes qui comptent vraiment (alarme déclenchée, fuite d’eau, congélateur en panne, piscine trop chaude), rien ne vaut un bon vieux **SMS**.

Si vous êtes abonné **Free Mobile**, Free propose gratuitement une option qui permet d’envoyer des SMS **à votre propre numéro** depuis une adresse internet. Free Mobile SMS XA fait le lien avec Home Assistant :

- 🔔 vous envoyez un SMS depuis une automatisation, comme n’importe quelle notification
- 👥 vous pouvez déclarer **plusieurs lignes** (Papa, Maman…), chacune avec ses propres identifiants
- 📱 une **carte « Envoyer un SMS »** permet d’écrire un message depuis le tableau de bord
- 📊 vous suivez le nombre de SMS envoyés, ceux du jour et les éventuelles erreurs

⚠️ Petite limite côté Free : l’option n’envoie des SMS **qu’au numéro de la ligne** qui a fourni la clé. Pour prévenir toute la famille, chacun ajoute sa propre ligne.

### ✨ Ce qui a changé depuis la première version

Depuis la présentation de mai 2025, l’intégration a beaucoup évolué :

- ✅ **Dans la bibliothèque HACS par défaut**
- 📱 **Carte native « Envoyer un SMS »**, chargée automatiquement : choix du destinataire (détecté tout seul), option « TOUS LE MONDE ! » et compteur de **160 caractères**
- 🔔 Envoi moderne via **`notify.send_message`**, comme le recommande Home Assistant
- 📜 **Historique des 50 derniers envois** (réussis ou non), conservé après un redémarrage. Par respect de la vie privée, le texte des SMS n’est plus stocké
- 🚦 **Gestion du quota Free** : si vous envoyez trop de SMS trop vite, le capteur l’indique clairement
- 📈 Deux capteurs à mettre en graphique : **SMS envoyés** et **SMS aujourd’hui**
- 🔁 **Changer la clé API sans tout supprimer** (menu « Reconfigurer »), et une demande de réauthentification automatique si Free refuse la clé
- 🩺 **Diagnostics téléchargeables**, avec la clé API masquée
- 🐛 La fameuse erreur « event loop » qui bloquait les envois chez certains est corrigée depuis septembre
- 🔐 **Nouveau dans la 6.12.13** : plus de confidentialité (le texte des SMS et la clé n’apparaissent plus dans les journaux ni dans les diagnostics) et des noms d’entités plus propres, sans casser vos automatisations

⚠️ Il faut maintenant Home Assistant **2025.12** au minimum.

@cc2i, si la carte « Envoyer un SMS » n’apparaît toujours pas chez toi avec cette version, dis-moi ta version de HA et je regarde.

### 🔐 Étape 0 : récupérer vos identifiants Free Mobile

1. Connectez-vous à votre **espace abonné Free Mobile** : https://mobile.free.fr/moncompte
2. Allez dans **Mes options** (« Gérer mes options »)
3. Activez **Notifications par SMS**
4. Notez votre **identifiant utilisateur** et la **clé API** affichée

![Où trouver la clé API dans l’espace Free Mobile](https://raw.githubusercontent.com/XAV59213/freesmsxa/main/images/token.png)

### 🛠️ Installation pas à pas (bibliothèque officielle HACS)

*Pour ceux qui débutent : HACS, c’est un peu le « magasin d’applications » communautaire de Home Assistant. Il permet d’installer et de mettre à jour en quelques clics des intégrations qui ne sont pas fournies d’origine. S’il n’est pas encore installé chez vous, le guide officiel est ici : https://hacs.xyz/docs/use/*

L’intégration fait partie de la **bibliothèque HACS par défaut** : plus besoin d’ajouter un dépôt personnalisé.

**Le plus rapide :** un clic sur ce bouton ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=freesmsxa&category=integration)

**Ou à la main :**

1. Dans Home Assistant, ouvrez **HACS** dans le menu de gauche
2. Tapez **Free Mobile SMS XA** dans la barre de recherche
3. Ouvrez la fiche, puis cliquez sur **Télécharger**
4. Redémarrez Home Assistant (**Paramètres > Système > bouton ⏻ en haut à droite > Redémarrer**)
5. Allez dans **Paramètres > Appareils et services > + Ajouter une intégration**, et cherchez **Free Mobile SMS XA**

⚠️ Petite subtilité qui piège souvent au début : HACS ne fait que **télécharger les fichiers**. Ce sont les étapes 4 et 5 qui créent réellement l’intégration et ses entités. Si vous ne voyez qu’une entité `update.…` après l’installation, c’est normal : c’est HACS qui surveille les mises à jour, il reste juste l’étape 5.

À l’étape 5, l’assistant vous demande l’identifiant, la clé API et un nom pour la ligne (par exemple « Papa »). Un SMS de test est envoyé pour vérifier que tout fonctionne. Répétez l’opération pour chaque ligne.

⚠️ Version de Home Assistant : il faut au minimum la **2025.12**.

Raccourci pour l’étape 5 : https://my.home-assistant.io/redirect/config_flow_start/?domain=freesmsxa

![L’assistant de configuration](https://raw.githubusercontent.com/XAV59213/freesmsxa/main/images/Capture%20d%E2%80%99%C3%A9cran%20du%202025-05-02%2011-11-45.png)

![Les lignes configurées](https://raw.githubusercontent.com/XAV59213/freesmsxa/main/images/Capture%20d%E2%80%99%C3%A9cran%20du%202025-05-02%2011-12-06.png)

### 📲 Envoyer un SMS depuis une automatisation

Dans l’éditeur d’automatisations, choisissez l’action **Notifications > Envoyer un message de notification** (`notify.send_message`), puis la ou les lignes à prévenir. En YAML, ça donne :

```yaml
alias: Alarme activée
triggers:
  - trigger: state
    entity_id: alarm_control_panel.maison
    to: armed_away
actions:
  - action: notify.send_message
    target:
      entity_id:
        - notify.maman
        - notify.papa
    data:
      message: Alarme activée
```

Les noms `notify.papa` / `notify.maman` dépendent du nom donné à chaque ligne.

### 📱 La carte « Envoyer un SMS »

**Modifier le tableau de bord > Ajouter une carte > Envoyer un SMS.** En YAML : `type: custom:freesmsxa-send-card`.

Si elle n’apparaît pas tout de suite, redémarrez Home Assistant, puis fermez et rouvrez l’application (ou videz le cache du navigateur).

### 📚 Pour aller plus loin

- [Envoyer des SMS depuis le dashboard Home Assistant](https://forumdomotique.com/forums/topic/353-envoyer-des-sms-depuis-le-dashboard-home-assistant-avec-lint%C3%A9gration-free-mobile-sms-xa/)
- [Configurer l’envoi de notifications SMS dans vos automatisations](https://forumdomotique.com/forums/topic/354-configurer-lenvoi-de-notifications-sms-dans-vos-automatisations-home-assistant-via-free-mobile-sms-xa/)

### 🔗 Liens

- Dépôt GitHub : https://github.com/XAV59213/freesmsxa
- Dernière version (6.12.13) : https://github.com/XAV59213/freesmsxa/releases/tag/6.12.13
- Signaler un bug ou proposer une idée : https://github.com/XAV59213/freesmsxa/issues

Vos retours, idées et remontées de bugs sont les bienvenus, ici ou sur GitHub 😉

Bonne domotique ! 🏠
Xavier (XAV59213)
