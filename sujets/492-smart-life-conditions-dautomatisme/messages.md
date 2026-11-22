---
title: "SMART LIFE conditions d'automatisme"
description: "Merci pour ton message détaillé. Ton scénario semble bien pensé pour couper la clim quand une baie vitrée s’ouvre, et la remettre en marche quand toutes…"
image: /assets/images/vignettes-themes/divers.jpg

date: 2025-11-26
cover_alt: "Vignette de rubrique Divers — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/492-smart-life-conditions-dautomatisme/">Lire et commenter sur Forum Domotique</a></p>

# SMART LIFE conditions d'automatisme

- **Catégorie :** [Smart Life / Tuya Smart](https://forumdomotique.com/forums/88-smart-life-tuya-smart/)
- **Sujet :** https://forumdomotique.com/forums/topic/492-smart-life-conditions-dautomatisme/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 3
- **Premier message de XAV59213 :** 26 novembre 2025 à 18:35 (Europe/Paris)
- **Dernier message de XAV59213 :** 24 décembre 2025 à 17:07 (Europe/Paris)

---

## Message 1 — 26 novembre 2025 à 18:35 (Europe/Paris)

- **Identifiant :** `1342`
- **Lien :** https://forumdomotique.com/forums/topic/492-smart-life-conditions-dautomatisme/#findComment-1342

> **Le 11/11/2025 à 19:06, DAB a dit :**
> Bonjour j'ai un soucis ave un scénario, qui ne s'enclenche pas.
>
> C'est un ensemble de contact de porte posés sur des baie vitrées, qui lorsque "Quand une condition est remplie", actionne un relay à OFF au bout de 30 secondes.
>
> Le but est de couper la clim quand on ouvre les baies vitrée...
>
> Mais pour la remise ON du Relay, ou il faut la condition "Quand toutes les conditions sont remplie" mais ça ne fonctionne pas, le relay ne repasse pas sur ON, si je modifie la condition "au moins un..." il se réenclenche, mais même si j'ai un autre DOOR SENSOR à ON....
>
> Le scénario qui ne fonctionne pas:
>
> Si / "Quand toutes les conditions sont remplie" / DOOR SENSOR 1 OFF, DOOR SENSOR 2 OFF.... / ALORS / RELAY= SWITCH ON
>
> Merci pour vôtre aide.

Bonjour [@DAB](https://forumdomotique.com/profile/649-dab/),

Merci pour ton message détaillé. Ton scénario semble bien pensé pour couper la clim quand une baie vitrée s’ouvre, et la remettre en marche quand toutes sont fermées. Le problème avec la condition ‘Quand toutes les conditions sont remplies’ (pour tous les DOOR SENSOR à OFF) est courant dans SmartLife/Tuya : l’automation ne se déclenche parfois pas parce qu’elle attend un changement d’état sur un des dispositifs, mais si les conditions sont déjà partiellement remplies, ça peut bugger.

Voici quelques pistes pour tester et corriger :

1.  **Vérifie les bases** : Assure-toi que tous les capteurs sont en ligne (icône verte dans l’app), avec une bonne connexion Wi-Fi, et que leurs états se mettent à jour en temps réel (teste en ouvrant/fermant manuellement).

2.  **Ajoute un délai** : Modifie ton scénario en ajoutant un délai de 1-5 secondes avant l’action ‘RELAY ON’. Parfois, ça force l’app à réévaluer les conditions correctement.

3.  **Change le type de condition temporairement** : Teste avec ‘Quand une condition est remplie’ sur un seul capteur pour voir si ça déclenche. Si oui, le souci vient de la combinaison multiple. Tu peux alors créer des automations séparées : par exemple, une pour chaque capteur qui vérifie les autres (mais c’est plus compliqué).

4.  **Utilise un intermédiaire** : Si possible, intègre un interrupteur virtuel ou une scène ‘Tap-to-Run’ comme relais. Par exemple, crée une scène qui s’active quand tous les capteurs sont OFF, et qui allume le relais. Ou, si tu as un hub comme Home Assistant ou Google Home, migre là-bas pour une logique plus robuste (Tuya a des limitations sur les ‘all conditions’).

Pour le OFF avec délai 30s et ‘au moins un ouvert’, ça marche bien car c’est plus simple pour l’app. Si tu modifies pour ‘au moins un OFF’, c’est normal que ça se réenclenche même si d’autres sont ouverts, car ça ne vérifie pas tous.

Dis-moi si ça résout, ou donne plus de détails sur ta config (version app, type de relais) pour affiner !

> **il y a 53 minutes, Jean luc a dit :**
> bonjour
>
> pratiquement le meme probleme avec un portail que j'ai motorisé qui fonctionne parfaitement en vocal et au clique sur smartphone
>
> mais une fonction marche et ignore le reste en automatique qui rejoint un peu ton systeme
>
> je veux que le portail se referme au bout de 30s mais il s'ouvre bien et reste ouvert ne se referme , il y a des fins de course avec diodes d'inversion , mais ça fait comme toi la 1ere fonction marche pour ouvrir si je clic portail ou je demande alexa ouvre portail ça marche arriver en bout d'ouverture il reste ouvert , les fonction d'apres ne marchent pas
>
> par contre si je dis alexa ferme portail ou que je clique fermeture ça marche
>
> le probleme est que a la maison y a alexa et google home mais pas dans la voiture
>
> j'ai testé tuya exactement pareil , comme si les appli ne pouvaient pas faire 2 fonctions sur les meme appareils
>
> merci

Bonjour [@Jean luc](https://forumdomotique.com/profile/737-jean-luc/),

Ton problème avec le portail motorisé ressemble beaucoup à des limitations connues dans SmartLife/Tuya pour les actions en séquence sur le même appareil, surtout avec des délais ou des inversions (comme tes fins de course avec diodes). L’ouverture marche bien (vocal ou clic), mais la fermeture auto après 30s est ignorée, car l’app traite parfois mal les tâches multiples (ouvrir + délai + fermer) sur un relais ou un switch inching.

Voici des idées pour dépanner :

1.  **Vérifie la config du délai** : Dans ton automation, assure-toi d’avoir : déclencheur ‘ouverture portail’, puis tâche ‘Délai 30s’, puis ‘fermeture portail’. Si c’est un switch ‘inching’ (impulsion courte pour bouger le moteur), vérifie le temps d’impulsion (souvent 0.5-2s) dans les params du dispositif. Teste sans délai d’abord pour voir si la fermeture seule marche dans une automation.

2.  **Ajoute un capteur de position** : C’est la solution la plus fiable. Installe un contact sensor Wi-Fi Tuya sur le portail (pour détecter s’il est ouvert/fermé). Puis, crée une automation : quand le capteur passe à ‘ouvert’, délai 30s, si toujours ouvert, déclenche la fermeture. Certains capteurs ont une condition intégrée ‘ouvert depuis X secondes’, ce qui évite les bugs de séquence.

3.  **Mode auto-close hardware** : Si ton contrôleur de portail a un réglage physique (comme un potentiomètre pour le temps de fermeture auto, courant sur les modules Tuya pour portes/garages), active-le directement sur le hardware plutôt que via l’app. Ça bypass l’app et utilise tes fins de course.

4.  **Sépare les actions** : Essaie deux automations distinctes : une pour l’ouverture, et une autre déclenchée par un timer ou un événement (mais sans capteur, c’est dur). Ou utilise le geofencing (dans SmartLife > Smart > Automation > Quand la position change) pour fermer quand tu t’éloignes, mais ça dépend de ton phone.

5.  **Autres tests** : Puisque ça marche vocal/manuel, teste avec l’app Tuya directement (pas SmartLife) pour comparer. Vérifie les logs de l’automation (dans Smart > Automation > … > Logs) pour voir si le délai est ignoré. Si bug persistant, feedback au support Tuya avec détails (modèle du module, version app).

Pour Alexa/Google Home dans la voiture, tu peux utiliser l’app mobile Tuya/SmartLife avec geofencing ou shortcuts vocaux via ton phone.

Si tu as plus d’infos sur ton setup (modèle du module portail, type de switch), je peux creuser plus !

---

## Message 2 — 27 novembre 2025 à 06:50 (Europe/Paris)

- **Identifiant :** `1345`
- **Lien :** https://forumdomotique.com/forums/topic/492-smart-life-conditions-dautomatisme/#findComment-1345

Salut [@Jean luc](https://forumdomotique.com/profile/737-jean-luc/)

Voici des pistes concrètes pour contourner sans achat supplémentaire (en utilisant tes 3 NX-4592 et 2 Meross). Je base ça sur des setups similaires pour portails Tuya. Teste étape par étape, et vérifie toujours les logs des automations (dans Smart > Automations > … > Historique) pour voir où ça coince.

**1. Reconfigurer les modes des switches**

•  Tes NX-4592 sont probablement en mode “self-locking” (verrouillé : ON reste ON jusqu’à OFF manuel). Pour un moteur avec inversion, passe-les en mode “inching” (impulsion courte) si possible : ça envoie une pulse de 0.5-2s pour déclencher l’ouverture/fermeture, sans maintenir l’état.

•  Dans l’app : Appuie long sur le dispositif > Paramètres (roue crantée) > Mode de fonctionnement > Inching, et règle la durée (ex. 1s pour activer le relais sans le coller indéfiniment).

•  Avantage : Ça évite que le switch reste “ON” après fin de course, et simplifie les automations (pas besoin de gérer l’état persistant).

**2. Automations séparées au lieu d’une séquence**

•  Au lieu d’une seule automation avec countdown, crée-en plusieurs qui s’enchaînent via déclencheurs d’état. Exemple pour une ouverture auto-fermeture :

•  **Automation 1 : Ouverture** (déclenchée par vocal/clic ou geo si tu veux auto).

•  Si : Switch 1 (moteur) = ON (ou scène “Ouvre portail”).

•  Alors : Allume Alim (switch alim ON) > Délai 1s (pour sync) > Relais inversion ON (pour direction ouverture).

•  (Le moteur s’ouvre jusqu’à fin de course, qui coupe mécaniquement.)

•  **Automation 2 : Déclenchement fermeture après délai**

•  Si : Switch alim = ON ET Relais inversion = ON (état post-ouverture) > ET Ajoute une condition “Depuis X secondes” si disponible (sinon, utilise un délai dans l’action).

•  Alors : Délai 30s > Relais inversion OFF (inversion polarité pour fermeture).

•  (Le moteur ferme jusqu’à fin de course.)

•  **Automation 3 : Arrêt total après fermeture**

•  Si : Relais inversion = OFF ET (condition sur temps ou état, ex. délai 30-60s pour la fermeture complète).

•  Alors : Éteins Alim (switch alim OFF) ET Relais OFF si besoin.

•  Problème : Sans capteur de position (ouvert/fermé), c’est approximatif. Utilise un délai fixe basé sur le temps de fermeture réel de ton portail (mesure-le).

•  Si le countdown persiste à bugger, remplace-le par l’action “Délai” dans l’automation (disponible dans “Ajouter une tâche > Délai”).

**3. Utilise un switch virtuel comme “timer”**

•  Crée un switch virtuel (dans SmartLife > Smart > Ajouter > Dispositif virtuel > Interrupteur).

•  Automation ouverture : Ouvre comme d’hab, puis allume le switch virtuel.

•  Automation timer : Si switch virtuel = ON > Alors Délai 30s > Fermeture (relais OFF) > Éteins switch virtuel.

•  Ça “découple” les actions et évite les conflits sur le même appareil.

---

## Message 3 — 24 décembre 2025 à 17:07 (Europe/Paris)

- **Identifiant :** `1617`
- **Lien :** https://forumdomotique.com/forums/topic/492-smart-life-conditions-dautomatisme/#findComment-1617

Super [@Jean luc](https://forumdomotique.com/profile/737-jean-luc/) ,

Je suis content que tu aies enfin réussi à dompter ton portail, et merci pour ton retour.

---
