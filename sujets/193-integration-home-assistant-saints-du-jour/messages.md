---
title: "🕊️ Intégration Home Assistant – Saints du Jour 🇫🇷"
description: "Je vous présente une petite intégration personnalisée que j’ai développée pour Home Assistant : Saints du Jour Ce composant affiche automatiquement le…"
image: /sujets/193-integration-home-assistant-saints-du-jour/images/Capturedcrandu2025-06-0714-58-19.png
date: 2025-06-07
---
{% raw %}
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/193-%F0%9F%95%8A%EF%B8%8F-int%C3%A9gration-home-assistant-saints-du-jour-%F0%9F%87%AB%F0%9F%87%B7/">Lire et commenter sur Forum Domotique</a> · <a href="https://github.com/XAV59213/saintdujour">Dépôt HACS : Saints du Jour</a></p>

# 🕊️ Intégration Home Assistant – Saints du Jour 🇫🇷

- **Catégorie :** [Projets et Personnalisations](https://forumdomotique.com/forums/12-projets-et-personnalisations/)
- **Sujet :** https://forumdomotique.com/forums/topic/193-%F0%9F%95%8A%EF%B8%8F-int%C3%A9gration-home-assistant-saints-du-jour-%F0%9F%87%AB%F0%9F%87%B7/
- **Auteur du premier message du sujet :** XAV59213
- **Messages de XAV59213 dans ce sujet :** 3
- **Premier message de XAV59213 :** 7 juin 2025 à 14:59 (Europe/Paris)
- **Dernier message de XAV59213 :** 20 novembre 2026 à 10:10 (Europe/Paris)

---

## Message 1 — 7 juin 2025 à 14:59 (Europe/Paris)

- **Identifiant :** `412`
- **Lien :** https://forumdomotique.com/forums/topic/193-%F0%9F%95%8A%EF%B8%8F-int%C3%A9gration-home-assistant-saints-du-jour-%F0%9F%87%AB%F0%9F%87%B7/#findComment-412

Bonjour à tous 👋

Je vous présente une petite intégration personnalisée que j’ai développée pour Home Assistant : **Saints du Jour**.

### 📌 Description

Ce composant affiche **automatiquement le saint célébré chaque jour** selon le calendrier liturgique français. Parfait pour ceux qui aiment connaître le saint du jour ou veulent enrichir leur interface avec une touche culturelle/religieuse.

### ✅ Fonctionnalités

- 📅 Affiche le saint du jour (ex : *les Pierre et Paul* le 29 juin)
- 🔁 Mise à jour automatique chaque jour
- 🧩 Intégration graphique via l’interface (pas besoin d’éditer `configuration.yaml`)
- 🖼️ Carte Lovelace disponible (type `entity`)
- 🕊️ Léger, local, sans API externe ni dépendances

---

### 🛠️ Installation via HACS

1. Ouvrez **HACS > Intégrations**
2. Cliquez sur les **trois points > Dépôt personnalisé**
3. Ajoutez ce dépot

   <https://github.com/XAV59213/saintdujour>

   1. en tant que type `Intégration`
   2. Recherchez et installez **Saints du Jour**
   3. Redémarrez Home Assistant
   4. Allez dans **Paramètres > Appareils & Services > Ajouter une intégration** et cherchez **Saints du Jour**

   ---

   ### 🧾 Exemple de carte Lovelace

   ```yaml
   type: entity
   entity: sensor.saint_du_jour
   name: Saint du Jour
   ```

   ou en markdown

   ```markdown
    **Saint du jour** : {{ states('sensor.saint_du_jour') | default('Aucun', true) }}
   ```

   vous pouvez ajouter cette icon 🙏avant les ** dans la balise du haut ça ne passe pas

   ![Capture d’écran du 2025-06-07 14-58-19.png](images/Capturedcrandu2025-06-0714-58-19.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_06/Capturedcrandu2025-06-0714-58-19.png.0f627b736c0b933c126f5b5ec45b7b05.png -->

   ### 🧠 Infos techniques

   - Domaine : `saintdujour`
   - Aucun paramétrage dans `configuration.yaml`
   - Basé sur un dictionnaire intégré avec les saints du calendrier
   - Compatible Home Assistant `>= 2023.6.0`

   ---

   ### 🧑‍💻 Code source & contributions

   📦 GitHub :  
   👉 <https://github.com/XAV59213/saintdujour>

   Si vous avez des suggestions, idées d’amélioration ou retours, n’hésitez pas à commenter ou ouvrir un ticket !

   ---

   Merci et bonne intégration ! 🙏  
   Xav59213

---

## Message 2 — 2 novembre 2026 à 20:03 (Europe/Paris)

- **Identifiant :** `5541`
- **Lien :** https://forumdomotique.com/forums/topic/193-%F0%9F%95%8A%EF%B8%8F-int%C3%A9gration-home-assistant-saints-du-jour-%F0%9F%87%AB%F0%9F%87%B7/#findComment-5541

![IMG_7810.png](images/IMG_7810.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2026_11/IMG_7810.png.c6f1bf275d141e333e7515d773dddfb1.png -->

**Saints du Jour est dans HACS par défaut 🎉**  
  
Salut à tous,  
  
Petite nouvelle de plus : mon intégration Saints du Jour vient d'être acceptée dans la bibliothèque HACS officielle ! Elle peut mettre quelques heures à apparaître dans HACS, mais ensuite plus besoin de dépôt personnalisé : vous cherchez « Saints du Jour » dans HACS, vous téléchargez, vous redémarrez, puis vous ajoutez l'intégration dans Paramètres, Appareils et services.  
Lien direct : https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=saintdujour&category=integration  
  
Pour ceux qui ne la connaissent pas, c'est tout simple : elle affiche chaque jour le ou les saints fêtés selon le calendrier français. Vous avez un capteur pour le saint du jour, et un autre pour celui de demain, pratique quand on souhaite la fête la veille. Rien à configurer, ça se met à jour tout seul chaque jour.  
  
Elle arrive aussi avec sa propre carte, « Saint du jour ». Pas de fichier à copier ni de ressource à ajouter : vous ajoutez la carte depuis le tableau de bord, et l'éditeur visuel vous laisse choisir le titre, l'icône, les libellés et l'affichage du lendemain. Elle retrouve même toute seule les capteurs si vous les avez renommés.  
  
Et bien sûr, ça marche très bien dans une automatisation, pour une notif du matin ou une annonce sur une enceinte du genre « Bonne fête aux Martin ! ».  
  
Le dépôt : https://github.com/XAV59213/saintdujour  
  
Si vous avez des idées ou un souci, dites-le moi ici ou sur GitHub 😉  
  
Bonne domotique !  
XAV59213

---

## Message 3 — 20 novembre 2026 à 10:10 (Europe/Paris)

- **Identifiant :** `5578`
- **Lien :** https://forumdomotique.com/forums/topic/193-%F0%9F%95%8A%EF%B8%8F-int%C3%A9gration-home-assistant-saints-du-jour-%F0%9F%87%AB%F0%9F%87%B7/#findComment-5578

Bonjour à tous 👋

Petite mise à jour de ce sujet, avec une présentation complète de **Saints du Jour** 🙏 telle qu’elle est aujourd’hui, pour ceux qui la découvrent comme pour ceux qui l’utilisent déjà. Son rôle est tout simple : chaque jour, elle affiche le ou les saints fêtés selon le calendrier français. Et depuis peu, elle indique aussi ceux de **demain**, ce qui est bien pratique quand on veut penser à souhaiter une fête la veille.

Elle fait désormais partie de la **bibliothèque officielle de HACS**, et la version actuelle est la [**1.4.0**](https://github.com/XAV59213/saintdujour/releases/tag/1.4.0).

👉 **Le plus simple :** cliquez sur ce bouton. Un clic ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

![Ouvrir dans HACS](images/hacs_repository.svg)
<!-- source : https://my.home-assistant.io/badges/hacs_repository.svg -->

![Saints du Jour](images/logo.png)
<!-- source : https://raw.githubusercontent.com/XAV59213/saintdujour/main/custom_components/saintdujour/brand/logo.png -->

### 🤔 À quoi ça sert, concrètement ?

On a tous un calendrier des PTT quelque part dans la cuisine, avec le saint du jour sous chaque date. Saints du Jour, c’est la même chose, mais dans Home Assistant. Une fois installée, elle crée deux capteurs :

- **Saint du Jour** : par exemple « les Pierre et Paul » le 29 juin
- **Saint de Demain** : le même principe pour le lendemain

À partir de là, on peut l’afficher sur un écran mural ou une tablette, recevoir une petite notification le matin, ou faire annoncer par une enceinte « Bonne fête aux Martin ! ».

Tout fonctionne **en local** : le calendrier est embarqué dans l’intégration, il n’y a aucun compte à créer ni aucun accès Internet nécessaire. Et il n’y a rien à configurer : l’ajout se fait en un clic.

### ✨ Ce qui a changé depuis la première version

Depuis la première présentation de juin 2025, l’intégration a pas mal grandi :

- ✅ **Dans la bibliothèque HACS par défaut** : plus besoin d’ajouter de dépôt personnalisé
- 🗓️ **Nouveau capteur « Saint de Demain »**
- 🙏 **Une carte Lovelace livrée avec l’intégration**, avec son éditeur visuel : rien à copier, aucune ressource à ajouter
- 🔎 La carte **retrouve toute seule les capteurs**, même si vous les avez renommés
- 🎄 **Nouveau dans la 1.4.0 : correction du 25 décembre**. Le jour de Noël manquait dans le calendrier et le capteur affichait « Inconnu »
- 🩺 **Diagnostics téléchargeables** en cas de souci, sans aucune donnée personnelle
- 🧪 Des tests automatisés qui vérifient notamment que les **366 jours** de l’année sont bien couverts

### 🛠️ Installation pas à pas (bibliothèque officielle HACS)

*Pour ceux qui débutent : HACS, c’est un peu le « magasin d’applications » communautaire de Home Assistant. Il permet d’installer et de mettre à jour en quelques clics des intégrations qui ne sont pas fournies d’origine. S’il n’est pas encore installé chez vous, le guide officiel est ici :* [*https://hacs.xyz/docs/use/*](https://hacs.xyz/docs/use/)

L’intégration fait partie de la **bibliothèque HACS par défaut** : plus besoin d’ajouter un dépôt personnalisé.

**Le plus rapide :** un clic sur ce bouton ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

![Ouvrir dans HACS](images/hacs_repository.svg)
<!-- source : https://my.home-assistant.io/badges/hacs_repository.svg -->

**Ou à la main :**

1. Dans Home Assistant, ouvrez **HACS** dans le menu de gauche
2. Tapez **Saints du Jour** dans la barre de recherche
3. Ouvrez la fiche, puis cliquez sur **Télécharger**
4. Redémarrez Home Assistant (**Paramètres > Système > bouton ⏻ en haut à droite > Redémarrer**)
5. Allez dans **Paramètres > Appareils et services > + Ajouter une intégration**, et cherchez **Saints du Jour**

⚠️ Petite subtilité qui piège souvent au début : HACS ne fait que **télécharger les fichiers**. Ce sont les étapes 4 et 5 qui créent réellement l’intégration et ses entités. Si vous ne voyez qu’une entité `update.…` après l’installation, c’est normal : c’est HACS qui surveille les mises à jour, il reste juste l’étape 5.

L’intégration n’a **ni paramètre ni option** : une fois ajoutée, les deux capteurs apparaissent sous l’appareil **Saints du Jour**.

Raccourci pour l’étape 5 : <https://my.home-assistant.io/redirect/config_flow_start/?domain=saintdujour>

### 🙏 La carte « Saint du jour »

Pas besoin de bricoler une carte Markdown comme dans mon message de juin 2025 : l’intégration apporte sa propre carte.

1. Ouvrez votre tableau de bord et passez en mode **Modifier**
2. Cliquez sur **Ajouter une carte** et cherchez **« Saint du jour »**
3. Dans l’éditeur, choisissez le titre, l’icône, les libellés et si vous voulez afficher la ligne de demain

Si la carte n’apparaît pas dans la liste juste après la mise à jour, videz le cache de votre navigateur.

Pour ceux qui préfèrent le YAML :

```plaintext
type: custom:saintdujour-card
title: 
```

🙏

Saints du jour show_tomorrow: true

### 🔔 Exemple : la fête du jour chaque matin

Une petite automatisation qui envoie une notification à 8 h :

```plaintext
automation:
  - alias: Fête du jour
    triggers:
      - trigger: time
        at: "08:00:00"
    actions:
      - action: notify.notify
        data:
          message: "Aujourd’hui, on fête {{ states('sensor.saints_du_jour_saint_du_jour') }} 
```

🙏

"

Petite remarque : sur une installation ancienne, le capteur peut s’appeler `sensor.saint_du_jour`. Vérifiez son nom dans **Paramètres > Appareils et services > Saints du Jour**.

### ⚠️ Bon à savoir

- Un saint par jour, issu d’un calendrier fixe français : les fêtes mobiles comme Pâques et les calendriers régionaux ne sont pas gérés
- Les noms sont en français, quelle que soit la langue de Home Assistant

### 🔗 Liens

- Dépôt GitHub : <https://github.com/XAV59213/saintdujour>
- Dernière version (1.4.0) : <https://github.com/XAV59213/saintdujour/releases/tag/1.4.0>
- Signaler un bug ou proposer une idée : <https://github.com/XAV59213/saintdujour/issues>

Vos retours, idées et remontées de bugs sont les bienvenus, ici ou sur GitHub 😉

Bonne domotique ! 🏠  
Xavier (XAV59213)

---
{% endraw %}
