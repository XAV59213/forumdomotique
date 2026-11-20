---
title: "Home Assistant 2026.3 : Un \\\\\\\\\\\\\\\"grand nettoyage\\\\\\\\\\\\\\\" bienvenu et plein de pépites communautaires"
description: "Franck Nijhof (Frenck) l'annonce clairement dans le billet officiel : « On a pris le temps de reviewer, polir et merger un nombre impressionnant de PRs…"
image: /assets/images/og-default.png
date: 2026-03-21
---
<p class="forum-cta"><a href="https://forumdomotique.com/actualites/home-assistant/home-assistant-20263-un-grand-nettoyage-bienvenu-et-plein-de-p%C3%A9pites-communautaires-r13/">Lire et commenter sur Forum Domotique</a></p>

# Home Assistant 2026.3 : Un "grand nettoyage" bienvenu et plein de pépites communautaires

- **Type :** Actualité
- **Catégorie :** Actualité domotique & maison connectée > Home Assistant
- **Lien :** https://forumdomotique.com/actualites/home-assistant/home-assistant-20263-un-grand-nettoyage-bienvenu-et-plein-de-p%C3%A9pites-communautaires-r13/
- **Date de publication :** 21 mars 2026 à 15:29 (Europe/Paris)
- **Auteur :** XAV59213

---

#### Après une version février particulièrement massive, l'équipe de Home Assistant a opté pour un rythme plus posé en mars 2026. Pas de révolution totale cette fois, mais un focus très appréciable sur le **polissage**, l'intégration massive de contributions communautaires, la correction de bugs et l'amélioration qualitative de dizaines d'intégrations existantes.

Franck Nijhof (Frenck) l'annonce clairement dans le billet officiel : « On a pris le temps de reviewer, polir et merger un nombre impressionnant de PRs communautaires. Et la communauté a livré ! »

Voici les points les plus marquants de cette version 2026.3.

#### 1. Aspirateurs robots : enfin le nettoyage par zone sans bidouiller

La star incontestée de cette release pour beaucoup d'utilisateurs : l'action **"Clean Area"** (nettoyer une ou plusieurs zones spécifiques).

Fini les codes de pièces obscurs en YAML ou les scripts compliqués. Vous pouvez maintenant :

- Associer les segments/cartes de votre aspirateur (via l'interface) aux zones définies dans Home Assistant
- Envoyer directement l'aspirateur nettoyer le salon + la cuisine, ou uniquement la chambre, depuis une automation, un dashboard, une voix, etc.

**Intégrations concernées** : Matter, Roborock, Ecovacs, et plusieurs autres qui ont rapidement suivi. Un énorme gain d'ergonomie pour tous ceux qui ont un robot aspirateur connecté.

#### 2. Android Companion App : wake word local expérimental

Grosse nouvelle pour les utilisateurs Android : l'application Companion supporte désormais (en mode expérimental) la détection de wake word **directement sur l'appareil**, sans passer par le cloud.

Mots-clés supportés pour le moment :

- « Okay Nabu »
- « Hey Jarvis »
- « Hey Mycroft »

Une fois réveillée, vous pouvez enchaîner directement avec une commande Assist. C'est un gros pas vers des satellites vocaux Android vraiment locaux et réactifs.

#### 3. Automatisations : l'éditeur visuel gagne en robustesse

Une fonctionnalité très demandée arrive enfin dans l'éditeur graphique :

- **"Continue on error"** — si une action échoue, l'automatisation ne s'arrête plus en cascade, elle continue d'exécuter les actions suivantes (configurable action par action).

Autres petits gains d'ergonomie dans l'éditeur :

- Meilleur drag & drop
- Améliorations de l'interface globale

#### 4. Dashboard : un nouveau pied de page (footer) et plus de flexibilité

Une nouvelle section **footer** apparaît dans les dashboards. Elle permet d'ajouter des éléments persistants en bas de page (horloge, infos rapides, boutons, etc.) sans qu'ils scrollent avec le reste.

#### 5. Tableau de bord Énergie : encore plus lisible et pratique

Plusieurs améliorations bienvenues :

- Vue "Now" (instantanée) qui affiche en direct la puissance électrique, le débit de gaz et le débit d'eau
- Réorganisation des onglets : Électricité / Gaz / Eau clairement séparés
- Tooltips des graphiques qui indiquent maintenant le jour de la semaine → beaucoup plus facile à lire quand on compare les semaines

#### 6. Intégrations : une avalanche de nouveautés et de quality scale up

Cette version est l'une des plus riches en termes de quantité d'intégrations touchées :

- Montée en **quality scale** (gold/silver/bronze) pour de très nombreuses intégrations (Matter, KNX, Roborock, SwitchBot, etc.)
- Améliorations massives sur Zigbee (mises à jour OTA du firmware plus fluides), plusieurs marques d'ampoules, capteurs, etc.
- Nouvelles intégrations (plus de 50 ajouts ou refontes notables selon les youtubers qui ont décortiqué le changelog complet)
- Possibilité pour les intégrations custom de fournir leurs propres icônes de marque via l'API brands

#### 7. Autres petites perles

- Meilleure gestion des erreurs dans les réponses Assist personnalisées
- Export de données plus facile
- Divers correctifs de performance et de stabilité

#### Patchs post-release

Comme d'habitude, plusieurs versions mineures correctives ont suivi rapidement :

- 2026.3.1 (6 mars)
- 2026.3.2
- 2026.3.3 (mi-mars)

Elles corrigent principalement des régressions (Rain Bird, Tibber, Reolink, InfluxDB, etc.).

### En résumé

Home Assistant 2026.3 n'est pas la mise à jour la plus "flashy" de l'année, mais elle est extrêmement solide et utile au quotidien.

Les ajouts pour les aspirateurs robots, le wake word Android local, l'option "continue on error" et les améliorations de l'énergie sont déjà adoptés par une grande partie de la communauté.

Si vous n'avez pas encore mis à jour, c'est le moment idéal — surtout si vous avez un robot aspirateur ou un téléphone Android que vous utilisez avec Assist.

Tu trouveras le billet officiel complet ici : <https://www.home-assistant.io/blog/2026/03/04/release-20263/>

Et toi, qu'est-ce qui t'excite le plus dans cette 2026.3 ? 😄
