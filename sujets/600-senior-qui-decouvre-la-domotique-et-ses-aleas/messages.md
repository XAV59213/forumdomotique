---
title: "Sénior qui découvre la domotique et ses aléas"
description: "Bonjour @Rajac11 et surtout bienvenue sur le forum ! Pas de souci pour le côté « bavard », au contraire : ton message est très clair et détaillé, ça aide…"
image: /assets/images/og-default.png
date: 2025-12-11
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/600-s%C3%A9nior-qui-d%C3%A9couvre-la-domotique-et-ses-al%C3%A9as/">Lire et commenter sur Forum Domotique</a></p>

# Sénior qui découvre la domotique et ses aléas

- **Catégorie :** [Présentez-vous](https://forumdomotique.com/forums/5-pr%C3%A9sentez-vous/)
- **Sujet :** https://forumdomotique.com/forums/topic/600-s%C3%A9nior-qui-d%C3%A9couvre-la-domotique-et-ses-al%C3%A9as/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 5
- **Premier message de XAV59213 :** 11 décembre 2025 à 20:25 (Europe/Paris)
- **Dernier message de XAV59213 :** 10 janvier 2026 à 16:51 (Europe/Paris)

---

## Message 1 — 11 décembre 2025 à 20:25 (Europe/Paris)

- **Identifiant :** `1518`
- **Lien :** https://forumdomotique.com/forums/topic/600-s%C3%A9nior-qui-d%C3%A9couvre-la-domotique-et-ses-al%C3%A9as/#findComment-1518

Bonjour [@Rajac11](https://forumdomotique.com/profile/841-rajac11/) et surtout bienvenue sur le forum !

Pas de souci pour le côté « bavard », au contraire : ton message est très clair et détaillé, ça aide énormément à comprendre le problème.

Ce que tu décris avec le seuil « inférieur à 3 kWh » qui ne déclenche jamais et « supérieur à 3 kWh » qui déclenche à l’inverse de ce qu’on attend, c’est un grand classique (et très contre-intuitif) avec les automatisations Tuya / Smart Life.

La raison est la suivante :

Dans Smart Life, quand tu crées une condition du type

« Lorsque le statut de l’appareil change » → « Consommation électrique » → « inférieure à 3 kWh »

L’application ne regarde pas la valeur actuelle de la consommation journalière,

elle déclenche l’automatisation uniquement au moment précis où la valeur passe en dessous de 3 kWh (c’est-à-dire au moment de la traversée du seuil de 3 vers moins de 3).

Or, sur presque tous les modules Tuya/Tongou qui mesurent l’énergie (surtout ceux avec compteur journalier) :

•  La consommation journalière est remise à zéro à minuit (00h00).

•  Elle commence donc à 0 kWh et monte progressivement dans la journée.

Résultat :

•  À 18h00, ta consommation journalière est presque toujours déjà > 3 kWh (même les jours peu ensoleillés tu as souvent au moins la conso de veille + un peu de chauffe).

•  Donc la valeur est déjà largement au-dessus de 3 kWh depuis longtemps.

•  Le moment où elle est passée « en dessous de 3 kWh » n’a existé que… entre 00h00 et le moment où tu as atteint 3 kWh dans la matinée.

•  À 18h00 ce changement d’état a eu lieu depuis des heures → l’automatisation ne se déclenche pas.

Quand tu mets « supérieur à 3 kWh », le passage du seuil a lieu dans la journée (quand tu dépasses 3 kWh), donc à 18h00 la condition est considérée comme vraie et l’automatisation part.

Bref : ce n’est pas un bug ni de l’appli ni du module, c’est juste le fonctionnement (très mal documenté) de la condition « Lorsque le statut change » sur les valeurs qui évoluent dans un seul sens dans la journée.

Solutions qui marchent à 100 % pour ton cas d’usage :

1.  La plus simple et la plus fiable aujourd’hui (2025)  
Utiliser la condition « Automation → Condition → Heure planifiée » (ex : tous les jours à 18h00)  
puis dedans mettre « Si consommation électrique (valeur actuelle) < 3 kWh »  
→ là il regarde vraiment la valeur à 18h, pas le moment du changement.

---

## Message 2 — 12 décembre 2025 à 18:57 (Europe/Paris)

- **Identifiant :** `1523`
- **Lien :** https://forumdomotique.com/forums/topic/600-s%C3%A9nior-qui-d%C3%A9couvre-la-domotique-et-ses-al%C3%A9as/#findComment-1523

Merci ☺️

 Le train de la domotique est déjà en marche… et toi, t’es monté à bord. Que le voyage commence. 😏

---

## Message 3 — 14 décembre 2025 à 08:17 (Europe/Paris)

- **Identifiant :** `1532`
- **Lien :** https://forumdomotique.com/forums/topic/600-s%C3%A9nior-qui-d%C3%A9couvre-la-domotique-et-ses-al%C3%A9as/#findComment-1532

Salut [@Rajac11](https://forumdomotique.com/profile/841-rajac11/)

Peux tu tester cette façon

1.  Ouvre l’app **Smart Life** (assure-toi qu’elle est à jour sur le Play Store).

2.  Va en bas au milieu : **Scène** (ou “Smart” / “Automation” selon la langue).

3.  En haut à droite : **+** pour créer une nouvelle scène.

4.  Choisis **“Lancer à une heure précise”** (ou “Heure planifiée” / “Schedule”).

•  Sélectionne **Tous les jours**.

•  Heure : **18:00**.

•  Répétition : tous les jours.

•  Valide.

5.  Ensuite, ajoute une **Condition** :

•  Clique sur **+ Ajouter une condition**.

•  Choisis **Statut de l’appareil**.

•  Sélectionne ton module Tongou (celui qui mesure la conso sur la ligne cumulus).

•  Choisis le paramètre : **Consommation d’électricité** → **Aujourd’hui** (ou “Today’s electricity” / “Consommation du jour”).

•  Opérateur : **Inférieur à**.

•  Valeur : **4 kWh** (commence par 4 pour tenir compte des ~1.86 kWh HC de la nuit ; tu pourras ajuster à 3.5 ou 4.5 après tests).

6.  Ajoute l’**Action** :

•  Clique sur **+ Ajouter une action**.

•  Choisis **Lancer une scène** ou directement **Contrôler l’appareil**.

•  Sélectionne ta scène existante “Activation Marche Forcée Arsun” (ou directement le micro-relais : Allumer / Activer).

7.  En bas : Nomme la scène, par exemple “Compléter Cumulus si solaire insuffisant à 18h”.

8.  Active le curseur en haut à droite pour que la scène soit **ON**.

9.  Sauvegarde.

→ Résultat attendu :

•  Tous les jours à 18h pile, l’app vérifie la conso journalière réelle.

•  Si < 4 kWh (solaire faible + HC) → active la marche forcée.

•  Si > 4 kWh (comme tes 6.67 kWh) → rien ne se passe.

Ça devrait marcher du premier coup, car on force la vérification à l’heure exacte, sans dépendre du “changement de statut”.

---

## Message 4 — 14 décembre 2025 à 19:47 (Europe/Paris)

- **Identifiant :** `1540`
- **Lien :** https://forumdomotique.com/forums/topic/600-s%C3%A9nior-qui-d%C3%A9couvre-la-domotique-et-ses-al%C3%A9as/#findComment-1540

Salut [@Rajac11](https://forumdomotique.com/profile/841-rajac11/) !

Pas de lassitude du tout, au contraire : tes retours détaillés et précis sont super utiles pour affiner et comprendre exactement ce qui se passe. Bravo pour avoir suivi les étapes à la lettre, et merci pour les infos sur la version app (7.0.5, récente) et le modèle exact (TO-Q-SY1-JWT). On va décortiquer tout ça calmement.

**D’abord, les bonnes nouvelles**

•  Ta scène s’est bien déclenchée à 18h quand la conso journalière était à **2.1 kWh** (avec condition <4 kWh) → c’est **parfait**, ça prouve que la logique “horaire planifié + condition sur valeur actuelle” fonctionne.

•  Le problème avec “<2.0 kWh” qui s’active quand même à 2.1 kWh : c’est presque sûrement un **arrondi ou une imprécision d’affichage** dans l’app Smart Life. Ces modules Tongou/Tuya mesurent souvent avec une précision de 0.01-0.1 kWh, et la valeur “aujourd’hui” peut fluctuer légèrement (rafraîchissement toutes les 5-10 sec, ou petit décalage serveur). Si la valeur réelle était genre 1.98-2.05 kWh au moment exact du check à 15h, ça passe sous 2.0. C’est frustrant, mais courant sur ces modules (pas un bug de ton appareil, plutôt la limite de la plateforme Tuya).

Pour confirmer : observe la valeur exacte dans l’app juste avant/après 18h sur plusieurs jours, et ajuste le seuil à **< 3.5 kWh** ou **< 4.0 kWh** (en tenant compte de tes ~1.86 kWh HC nocturnes). Ça te donnera une marge confortable sans déclencher par erreur les bons jours ensoleillés.

**Sur le module TO-Q-SY1-JWT**

•  **État du relais** : Laisse-le sur **ON** (c’est le mode normal pour qu’il route/contrôle le cumulus). OFF couperait tout en permanence.

•  **Vérifier le micro-logiciel** : Malheureusement, l’app Smart Life ne propose pas de mise à jour manuelle visible (c’est automatique lors de l’appairage ou en arrière-plan). Ton modèle est connu pour avoir un firmware stable mais parfois capricieux sur les stats journalières (reset pas toujours pile à minuit, ou petits décalages). Un **reset usine** peut aider à “rafraîchir” :

1.  Dans l’app : Appareil → … (en haut droite) → Supprimer l’appareil → Choisis “Déconnecter et effacer les données”.

2.  Ré-appaire comme au premier jour (mode appairage du module). Ça efface l’historique, mais remet les compteurs à zéro et peut corriger des bizarreries de mesure. Tes tests réseau sont bons, donc pas de souci connexion.

**Sur tes scènes et le “fanion” visuel**

•  Oui, tu peux avoir **plusieurs actions** dans la même scène : ajoute ton ancien module Tongou comme deuxième action (mettre son relais ON pour le voyant). Ça ne perturbe pas la mesure.

•  Pour un **compte à rebours d’1 heure** sur la marche forcée (au lieu d’une scène OFF à 5h) : Dans ta scène “Marche Forcée Arsun”, quand tu ajoutes l’action sur le micro-relais (ON), cherche l’option “Délai” ou “Compte à rebours” (certains modules/relais Tuya le permettent directement). Si pas dispo, crée une deuxième scène simple :

•  Déclencheur : Quand le micro-relais passe à ON.

•  Attente : 1 heure.

•  Action : Micro-relais OFF. Ça évite la chauffe trop longue en HC.

**Pourquoi ça reste “aléatoire” parfois ?**

Tuya/Smart Life est génial pour le basique, mais les conditions sur “consommation du jour” sont limitées (pas toujours précises à 100%, surtout avec chauffe HC qui “pollue” le compteur journalier). Ton setup Arsun est top, mais sans sonde température intégrée comme l’a dit [@filoo](https://forumdomotique.com/profile/232-filoo/) , on bricole avec l’énergie routée → c’est déjà une super optimisation !

Si tu veux t’affranchir vraiment de ces petits aléas sans passer à Home Assistant (qui serait la solution ultime, mais plus technique) :

•  Ajoute une **sonde de température Tuya** (genre sonde étanche DS18B20 compatible, ou un thermostat Tuya pour cumulus) directement dans le ballon. Puis modifie la scène pour une condition “ET” : (heure 18h) ET (température ballon < 55°C) ET (conso jour < seuil). Ça complétera seulement si vraiment besoin, indépendamment du solaire.

Tiens-moi au courant des prochains tests (après reset ou ajustement seuil), on va stabiliser ça à 100% ! T’es déjà très proche du fonctionnement parfait.

Courage, et encore bravo pour ton installation solaire + Arsun, c’est du beau travail ☀️🔧

---

## Message 5 — 10 janvier 2026 à 16:51 (Europe/Paris)

- **Identifiant :** `1716`
- **Lien :** https://forumdomotique.com/forums/topic/600-s%C3%A9nior-qui-d%C3%A9couvre-la-domotique-et-ses-al%C3%A9as/#findComment-1716

Salut [@Rajac11](https://forumdomotique.com/profile/841-rajac11/)   
Merci pour ton message et surtout pour tes vœux très sympas !

je te retourne la pareille pour 2026 : excellente santé, plein de soleil pour ton installation solaire et que ton Arsun tourne à plein régime ! 😄  
Je comprends bien ton constat : avec ce début d’année peu ensoleillé, le complément chauffe-eau en heures creuses devient vite indispensable les soirs de douche, mais tu veux l’optimiser pour ne pas le lancer tous les jours (et encore moins le week-end), et plutôt un jour sur deux en semaine seulement (lundi, mercredi, vendredi ça fait déjà un rythme proche de 3 jours/semaine, mais tu vises plutôt alterné = environ 2–3/semaine selon les semaines).  
Smart Life (Tuya) est malheureusement assez limité sur les logiques complexes du type « un jour sur deux » ou « pair/impair » sans aide extérieure. Pas de compteur de jours natif ni de modulo dans les conditions.  
Solution la plus simple et fiable avec ton témoin Tongou (prise/relais/énergie connecté Tuya)  
On va utiliser deux « fanions » (appelés « interrupteurs virtuels » ou « scènes Tap-to-Run » que l’on toggle comme des booleans) pour créer un bascule qui alterne.  
Méthode recommandée : deux interrupteurs virtuels + 3 automatisations  
  
Crée deux interrupteurs virtuels (dans Smart Life → Automatisation → Ajouter → Interrupteur virtuel ou « Tap-to-Run » que tu laisses vide) :  
Fanion A = « Complement_HC_Actif » (on/off)  
Fanion B = « Complement_HC_ToggleHelper » (on/off) — sert juste de bascule  
(Si tu n’as pas d’interrupteur virtuel natif, crée deux scènes Tap-to-Run vides nommées comme ci-dessus, tu pourras les activer/désactiver comme des switches.)  
Automatisation 1 : « Toggle le jour pair » (exécutée tous les matins pour préparer la journée)  
Déclencheur : Horaire fixe → tous les jours à 06:00 (ou 07:00)  
Condition : Jour de la semaine → Lundi, Mardi, Mercredi, Jeudi, Vendredi (exclut samedi/dimanche)  
Condition supplémentaire (si possible) : si le Fanion B est OFF (selon version app, ça peut être « statut du switch virtuel »)  
Action :  
Allumer Fanion B (toggle helper → passe à ON)  
Si Fanion A est OFF → Allumer Fanion A  
Sinon (A est ON) → Éteindre Fanion A  
  
→ Résultat : chaque jour ouvré, on inverse l’état du fanion principal A.Alternative plus simple si ta version Smart Life autorise bien les conditions multiples :  
Déclencheur : Horaire 06:00 tous les jours ouvrés  
Action : Inverser (toggle) Fanion A directement  
→ Certains utilisateurs rapportent que le toggle marche sur les interrupteurs virtuels quand on l’appelle comme action.  
  
Automatisation 2 : Le vrai complément HC (celle que tu as déjà, mais améliorée)  
Déclencheur : Horaire fixe → 18:00 (ou quand tu veux tester la prod solaire)  
Condition :  
Production solaire < 4.0 kWh (via ton capteur Tongou si tu as un compteur solaire, ou via une scène qui simule ça)  
OU Fanion A est ON (c’est ça la clé !)  
  
Action : Lancer le complément chauffe-eau 2h30 (ou la durée que tu veux)  
  
Optionnel — Automatisation 3 : Reset week-end  
Déclencheur : Samedi 00:01  
Action : Éteindre Fanion A (pour être sûr de repartir propre le lundi)  
  
  
Avec cette astuce du Fanion A, tu alternes vraiment un jour sur deux en semaine, et rien le week-end.  
Variante encore plus simple (si le toggle direct marche chez toi)  
  
Crée un seul fanion « Complement_HC_Actif »  
Automatisation toggle quotidien :  
Déclencheur : 06:00, jours semaine seulement  
Action : Inverser le fanion  
  
Puis ta scène de 18h00 vérifie si le fanion est ON → lance le complément  
  
Teste ça en premier, c’est souvent le plus propre quand ça fonctionne.  
Dis-moi quelle version exacte de l’app tu as (Smart Life ou Tuya Smart ?) et si tu arrives à créer des interrupteurs virtuels ou à toggler un Tap-to-Run, je t’affinerai encore plus précisément.  
Bon courage pour tes réglages, et surtout plein de beaux kWh solaires pour la suite de l’hiver !  
Cordialement,

---
