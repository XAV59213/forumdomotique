---
title: "Brouillon — saintdujour — RÉPONSE dans le sujet 193 — ne rien publier ni modifier sans le OK de Xavier"
---

{% raw %}
# Brouillon — saintdujour — RÉPONSE dans le sujet 193 — ne rien publier ni modifier sans le OK de Xavier

**Sujet existant :** [🕊️ Intégration Home Assistant – Saints du Jour 🇫🇷](https://forumdomotique.com/forums/topic/193-%F0%9F%95%8A%EF%B8%8F-int%C3%A9gration-home-assistant-saints-du-jour-%F0%9F%87%AB%F0%9F%87%B7/) — Projets et Personnalisations — ouvert le 7 juin 2025 (v1.0.x, dépôt personnalisé, HA ≥ 2023.6, `sensor.saint_du_jour`), 2 messages ; dernière réponse de Xavier le 2 nov. 2026 (« Saints du Jour est dans HACS par défaut », carte native).

**Action recommandée :** publier la **réponse complète** ci-dessous dans le sujet existant. Le forum ne permet plus de modifier le premier message (délai de modification dépassé), la réponse se suffit donc à elle-même : nouveautés, photos, installation pas à pas, bouton HACS. Elle apporte notamment la 1.4.0 (7 nov. 2026), postérieure à l’annonce du 2 nov.

**Titre du sujet :** inchangé (le titre n’est sans doute plus modifiable non plus ; renommage éventuel à demander à Jack). Suggestion si renommage : 🙏 Saints du Jour – Le saint du jour (et de demain) dans Home Assistant 🇫🇷

**État vérifié :** dans hacs/default (liste `integration`), release 1.4.0 du 7 nov. 2026, HA ≥ 2024.6.0 (hacs.json).

**Points à confirmer par Xavier :**
- Le dépôt ne contient aucune capture de la carte : seule image disponible = logo (brand/logo.png). Ajouter une capture de la carte « Saint du jour » (ex. celle déjà postée le 2 nov., IMG_7810) ?
- L’option `show_tomorrow` et les autres options de carte sont reprises du README ; titre YAML simplifié.

**Mise en forme Invision :** coller dans l’éditeur visuel ; `###` = intertitre ; images insérées par leur URL ; le bouton « Ouvrir dans HACS » = image du badge sur laquelle on pose le lien.

---

## Réponse complète à publier dans le sujet

Bonjour à tous 👋

Petite mise à jour de ce sujet, avec une présentation complète de **Saints du Jour** 🙏 telle qu’elle est aujourd’hui, pour ceux qui la découvrent comme pour ceux qui l’utilisent déjà. Son rôle est tout simple : chaque jour, elle affiche le ou les saints fêtés selon le calendrier français. Et depuis peu, elle indique aussi ceux de **demain**, ce qui est bien pratique quand on veut penser à souhaiter une fête la veille.

Elle fait désormais partie de la **bibliothèque officielle de HACS**, et la version actuelle est la **[1.4.0](https://github.com/XAV59213/saintdujour/releases/tag/1.4.0)**.

👉 **Le plus simple :** cliquez sur ce bouton. Un clic ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=saintdujour&category=integration)

![Saints du Jour](https://raw.githubusercontent.com/XAV59213/saintdujour/main/custom_components/saintdujour/brand/logo.png)

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

*Pour ceux qui débutent : HACS, c’est un peu le « magasin d’applications » communautaire de Home Assistant. Il permet d’installer et de mettre à jour en quelques clics des intégrations qui ne sont pas fournies d’origine. S’il n’est pas encore installé chez vous, le guide officiel est ici : https://hacs.xyz/docs/use/*

L’intégration fait partie de la **bibliothèque HACS par défaut** : plus besoin d’ajouter un dépôt personnalisé.

**Le plus rapide :** un clic sur ce bouton ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=saintdujour&category=integration)

**Ou à la main :**

1. Dans Home Assistant, ouvrez **HACS** dans le menu de gauche
2. Tapez **Saints du Jour** dans la barre de recherche
3. Ouvrez la fiche, puis cliquez sur **Télécharger**
4. Redémarrez Home Assistant (**Paramètres > Système > bouton ⏻ en haut à droite > Redémarrer**)
5. Allez dans **Paramètres > Appareils et services > + Ajouter une intégration**, et cherchez **Saints du Jour**

⚠️ Petite subtilité qui piège souvent au début : HACS ne fait que **télécharger les fichiers**. Ce sont les étapes 4 et 5 qui créent réellement l’intégration et ses entités. Si vous ne voyez qu’une entité `update.…` après l’installation, c’est normal : c’est HACS qui surveille les mises à jour, il reste juste l’étape 5.

L’intégration n’a **ni paramètre ni option** : une fois ajoutée, les deux capteurs apparaissent sous l’appareil **Saints du Jour**.

Raccourci pour l’étape 5 : https://my.home-assistant.io/redirect/config_flow_start/?domain=saintdujour

### 🙏 La carte « Saint du jour »

Pas besoin de bricoler une carte Markdown comme dans mon message de juin 2025 : l’intégration apporte sa propre carte.

1. Ouvrez votre tableau de bord et passez en mode **Modifier**
2. Cliquez sur **Ajouter une carte** et cherchez **« Saint du jour »**
3. Dans l’éditeur, choisissez le titre, l’icône, les libellés et si vous voulez afficher la ligne de demain

Si la carte n’apparaît pas dans la liste juste après la mise à jour, videz le cache de votre navigateur.

Pour ceux qui préfèrent le YAML :

```yaml
type: custom:saintdujour-card
title: 🙏 Saints du jour
show_tomorrow: true
```

### 🔔 Exemple : la fête du jour chaque matin

Une petite automatisation qui envoie une notification à 8 h :

```yaml
automation:
  - alias: Fête du jour
    triggers:
      - trigger: time
        at: "08:00:00"
    actions:
      - action: notify.notify
        data:
          message: "Aujourd’hui, on fête {{ states('sensor.saints_du_jour_saint_du_jour') }} 🙏"
```

Petite remarque : sur une installation ancienne, le capteur peut s’appeler `sensor.saint_du_jour`. Vérifiez son nom dans **Paramètres > Appareils et services > Saints du Jour**.

### ⚠️ Bon à savoir

- Un saint par jour, issu d’un calendrier fixe français : les fêtes mobiles comme Pâques et les calendriers régionaux ne sont pas gérés
- Les noms sont en français, quelle que soit la langue de Home Assistant

### 🔗 Liens

- Dépôt GitHub : https://github.com/XAV59213/saintdujour
- Dernière version (1.4.0) : https://github.com/XAV59213/saintdujour/releases/tag/1.4.0
- Signaler un bug ou proposer une idée : https://github.com/XAV59213/saintdujour/issues

Vos retours, idées et remontées de bugs sont les bienvenus, ici ou sur GitHub 😉

Bonne domotique ! 🏠
Xavier (XAV59213)
{% endraw %}
