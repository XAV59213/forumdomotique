---
title: "Brouillon — jourferier — RÉPONSE dans le sujet 194 — ne rien publier ni modifier sans le OK de Xavier"
---

# Brouillon — jourferier — RÉPONSE dans le sujet 194 — ne rien publier ni modifier sans le OK de Xavier

**Sujet existant :** [## 🇫🇷 [Intégration HA] Jour Férié – Capteur de jours fériés](https://forumdomotique.com/forums/topic/194-%F0%9F%87%AB%F0%9F%87%B7-int%C3%A9gration-ha-jour-f%C3%A9ri%C3%A9-capteur-de-jours-f%C3%A9ri%C3%A9s/) — Projets et Personnalisations — ouvert le 7 juin 2025 (v1.0.x : `sensor.jour_ferie` + service `create_card`, dépôt perso), 13 messages ; dernier : Xavier le 4 mai 2026 (réponse à thierryha54 sur l’Alsace-Moselle).

**Action recommandée :** publier la **réponse complète** ci-dessous dans le sujet existant. Le forum ne permet plus de modifier le premier message (délai de modification dépassé), la réponse se suffit donc à elle-même : nouveautés, photos, installation pas à pas, bouton HACS. Annonce aussi l’arrivée dans HACS par défaut (PR hacs/default#10509 fusionnée le 9 nov. 2026, pas encore annoncée). Le titre du sujet commence par « ## » en trop : à faire corriger par Jack si le titre n’est plus modifiable.

**Titre du sujet :** inchangé (le titre n’est sans doute plus modifiable non plus ; renommage éventuel à demander à Jack). Suggestion si renommage : 🇫🇷 Jour Férié – Les jours fériés français dans Home Assistant (capteurs, calendrier, carte)

**État vérifié :** dans hacs/default ; release 1.2.8 (7 nov. 2026) ; HA ≥ 2024.6.0. ⚠️ Le README du dépôt décrit encore l’installation en dépôt personnalisé et affiche un badge « HACS Custom » : à mettre à jour côté GitHub.

**Points à confirmer par Xavier :**
- Alsace-Moselle (Vendredi saint, Saint-Étienne) : rien dans le code de la 1.2.8. Le paragraphe pour @thierryha54 (« c’est noté ») est à valider, ou à retirer.
- Aucune capture dans le dépôt (logo seulement). Ajouter une capture de la carte « Jours fériés » ?
- Calcul automatique de Pâques/Ascension/Pentecôte : d’après sa réponse du 4 mai 2026 et const.py.

**Mise en forme Invision :** coller dans l’éditeur visuel ; `###` = intertitre ; images insérées par leur URL ; le bouton « Ouvrir dans HACS » = image du badge sur laquelle on pose le lien.

---

## Réponse complète à publier dans le sujet

Bonjour à tous 👋

Ça faisait un moment que je n’avais pas donné de nouvelles ici ! Voici une présentation complète et à jour de **Jour Férié** 🇫🇷, l’intégration Home Assistant qui sait, chaque jour, si l’on est un jour férié en France, si demain en est un, et combien de jours il reste avant le prochain.

Grande nouvelle : depuis le 9 novembre 2026, elle fait partie de la **bibliothèque officielle de HACS**. Ceux qui l’avaient installée en dépôt personnalisé n’ont rien à faire, tout continue de fonctionner. La version actuelle est la **[1.2.8](https://github.com/XAV59213/jourferier/releases/tag/1.2.8)**.

👉 **Le plus simple :** cliquez sur ce bouton. Un clic ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=jourferier&category=integration)

![Jour Férié](https://raw.githubusercontent.com/XAV59213/jourferier/main/image/logo.png)

### 🤔 À quoi ça sert, concrètement ?

Un jour férié, ça change souvent le programme de la maison : pas de réveil à 6 h 30, le chauffage du bureau qui n’a pas besoin de démarrer, le ramassage des poubelles décalé… Le problème, c’est que Home Assistant ne le sait pas tout seul.

Jour Férié lui apprend. L’intégration calcule elle-même les jours fériés français, y compris ceux qui bougent chaque année comme **Pâques, l’Ascension ou la Pentecôte** : pas besoin de les saisir à la main, et ils se mettent à jour automatiquement d’une année sur l’autre. Tout se passe en local.

Elle crée :

- 🗓️ un capteur **Jour Férié** (`sensor.jour_ferie`) : le nom du jour férié du jour (ou « aucun »), le prochain jour férié, le nombre de jours restants et le prochain **pont** potentiel
- 🔀 un capteur **« Aujourd’hui est férié »** (`binary_sensor.est_ferie`) : allumé les jours fériés, parfait pour bloquer un réveil ou une alarme
- 🔀 un capteur **« Demain est férié »** (`binary_sensor.demain_est_ferie`) : pour tout préparer la veille
- 📅 un **calendrier** (`calendar.jour_ferie_calendar`) avec tous les jours fériés, visible dans l’onglet Calendrier de Home Assistant

### ✨ Ce qui a changé depuis la première version

Depuis la présentation de juin 2025 :

- ✅ **Dans la bibliothèque HACS par défaut**, après une revue du code par frenck
- 🔀 **Deux capteurs binaires** : aujourd’hui férié, demain férié
- 📅 **Le calendrier des jours fériés**
- 🌉 Le **prochain pont** potentiel dans les attributs du capteur
- 🎉 **Une carte Lovelace livrée avec l’intégration**, avec éditeur visuel
- 🧹 L’ancien service `jourferier.create_card` a été retiré : la carte native le remplace

### 🛠️ Installation pas à pas (bibliothèque officielle HACS)

*Pour ceux qui débutent : HACS, c’est un peu le « magasin d’applications » communautaire de Home Assistant. Il permet d’installer et de mettre à jour en quelques clics des intégrations qui ne sont pas fournies d’origine. S’il n’est pas encore installé chez vous, le guide officiel est ici : https://hacs.xyz/docs/use/*

L’intégration fait partie de la **bibliothèque HACS par défaut** : plus besoin d’ajouter un dépôt personnalisé.

**Le plus rapide :** un clic sur ce bouton ouvre directement l’intégration dans votre HACS, et le dépôt est ajouté automatiquement :

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=XAV59213&repository=jourferier&category=integration)

**Ou à la main :**

1. Dans Home Assistant, ouvrez **HACS** dans le menu de gauche
2. Tapez **Jour Férié** dans la barre de recherche
3. Ouvrez la fiche, puis cliquez sur **Télécharger**
4. Redémarrez Home Assistant (**Paramètres > Système > bouton ⏻ en haut à droite > Redémarrer**)
5. Allez dans **Paramètres > Appareils et services > + Ajouter une intégration**, et cherchez **Jour Férié**

⚠️ Petite subtilité qui piège souvent au début : HACS ne fait que **télécharger les fichiers**. Ce sont les étapes 4 et 5 qui créent réellement l’intégration et ses entités. Si vous ne voyez qu’une entité `update.…` après l’installation, c’est normal : c’est HACS qui surveille les mises à jour, il reste juste l’étape 5.

Aucune configuration n’est demandée : les capteurs et le calendrier apparaissent dès l’ajout.

Raccourci pour l’étape 5 : https://my.home-assistant.io/redirect/config_flow_start/?domain=jourferier

### 🎉 La carte « Jours fériés »

1. Ouvrez votre tableau de bord en mode **Modifier**
2. **Ajouter une carte**, puis cherchez **« Jours fériés »**
3. Choisissez le capteur (par défaut `sensor.jour_ferie`) et le titre

Elle affiche par exemple : « Aujourd’hui, pas de jour férié. Le prochain jour férié est **Toussaint** dans **1 jour**. »

```yaml
type: custom:jour-ferie-card
entity: sensor.jour_ferie
title: Jours fériés 🎉
```

Si elle n’apparaît pas, videz le cache du navigateur.

### 💬 Et l’Alsace-Moselle ?

@thierryha54, merci pour ta question de mai : les jours propres à l’Alsace-Moselle (Vendredi saint, Saint-Étienne) ne sont pas encore intégrés dans cette version, c’est noté.

### ⏰ Exemple : pas de réveil les jours fériés

Dans votre automatisation de réveil, il suffit d’ajouter cette condition : elle ne se déclenchera que les jours **non** fériés.

```yaml
condition:
  - condition: state
    entity_id: binary_sensor.est_ferie
    state: "off"
```

### 🔗 Liens

- Dépôt GitHub : https://github.com/XAV59213/jourferier
- Dernière version (1.2.8) : https://github.com/XAV59213/jourferier/releases/tag/1.2.8
- Signaler un bug ou proposer une idée : https://github.com/XAV59213/jourferier/issues

Vos retours, idées et remontées de bugs sont les bienvenus, ici ou sur GitHub 😉

Bonne domotique ! 🏠
Xavier (XAV59213)
