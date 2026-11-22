---
title: "Smart Life / Automatisation portail avec localisation"
description: "Pour que ton portail s’ouvre automatiquement quand tu rentres à la maison (grâce à la localisation), il y a deux façons principales de faire selon ce que…"
image: /assets/images/vignettes-themes/divers.jpg

date: 2025-12-31
cover_alt: "Vignette de rubrique Divers — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/">Lire et commenter sur Forum Domotique</a></p>

# Smart Life / Automatisation portail avec localisation

- **Catégorie :** [Smart Life / Tuya Smart](https://forumdomotique.com/forums/88-smart-life-tuya-smart/)
- **Sujet :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 9
- **Premier message de XAV59213 :** 31 décembre 2025 à 16:40 (Europe/Paris)
- **Dernier message de XAV59213 :** 18 janvier 2026 à 12:08 (Europe/Paris)

---

## Message 1 — 31 décembre 2025 à 16:40 (Europe/Paris)

- **Identifiant :** `1651`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1651

Salut [@wakyky](https://forumdomotique.com/profile/992-wakyky/) !

Merci pour ton message !

Pour que ton portail s’ouvre automatiquement quand tu rentres à la maison (grâce à la localisation), il y a deux façons principales de faire selon ce que tu utilises :

**1. Si tu utilises seulement l’app Smart Life (ou Tuya)**

L’app a déjà une fonction geofencing intégrée, c’est super simple :

•  Ouvre l’app Smart Life

•  Va dans l’onglet **Smart** (ou **Scènes/Automatisations**)

•  Clique sur le **+** pour créer une nouvelle automatisation

•  Choisis **Localisation** comme condition (il y a souvent “Quand j’arrive” ou “Quand je rentre”)

•  Définit une zone autour de chez toi (par exemple 300-500 m pour qu’il anticipe ton arrivée)

•  Comme action : sélectionne ton module de portail et choisis **Allumer** (ou l’action qui déclenche l’impulsion)

•  Ton réglage **Inching 2s** est nickel, ça envoie juste une petite impulsion de 2 secondes, parfait pour simuler la télécommande.

Petits conseils :

•  Pense à autoriser la localisation **en permanence** pour l’app Smart Life dans les réglages de ton téléphone.

•  Le geofencing peut parfois être un peu lent ou imprécis (ça dépend du GPS), teste différents rayons pour trouver le bon timing.

**2. Si tu utilises Home Assistant**

C’est encore plus précis et fiable avec HA !

•  Vérifie que ton module Tuya/Smart Life est bien intégré dans Home Assistant.

•  Installe l’app Companion Home Assistant sur ton téléphone pour tracker ta position.

•  Crée une zone “maison” (ou une zone plus grande pour anticiper) dans HA.

•  Ensuite, fais une automatisation : quand tu entres dans la zone → impulsion de 2 secondes sur le switch du module.

Du coup, pour t’aider au mieux, dis-moi :

•  C’est quel modèle précis de module que tu as mis ? (Sonoff, Moes, un générique Tuya… ?)

•  C’est quel moteur de portail (marque/modèle) ?

•  Tu gères tout via l’app **Smart Life** seule, ou tu as **Home Assistant** comme hub central ?

Avec ces infos, je pourrai te guider étape par étape encore plus précisément.

À très vite !

---

## Message 2 — 11 janvier 2026 à 14:17 (Europe/Paris)

- **Identifiant :** `1731`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1731

> **il y a une heure, wakyky a dit :**
> Bonjour
>
> avez vous bien eu mon précédent message avec les réponses à vos questions ?
>
> Si oui est il possible d’avoir un retour de votre part.
>
> Merci d’avance
>
> Julien

Salut [@wakyky](https://forumdomotique.com/profile/992-wakyky/)

Désoler je n'avait pas activer M’avertir lorsqu’une réponse est postée.🫣

Merci pour ces précisions ! On va essayer de résoudre tes deux points un par un, en se basant sur le fonctionnement typique des modules Yokis/Tuya/SmartLife pour une motorisation de portail comme la Somfy Lockyvia (qui est généralement commandée par impulsion sèche).

### 1. Le paramètre « Relay Status » (ON / OFF / Remember last status)

Ce paramètre définit le comportement du relais **après une coupure de courant** (ou remise sous tension du module).

Pour une motorisation de portail/garage commandée par impulsion (comme presque toutes les Somfy), **il faut absolument choisir « Remember last status »** (mémoriser le dernier état).

Voici pourquoi :

- Le portail n'a pas de position « ON » ou « OFF » permanente, c'est une impulsion courte qui déclenche l'ouverture ou la fermeture.
- Si tu mets « ON », le relais resterait collé après une coupure → risque de déclencher en boucle ou de griller quelque chose.
- Si tu mets « OFF », le relais serait ouvert → pas de souci immédiat, mais pas logique.
- Avec **« Remember last status »**, le relais revient à l'état inactif (ouvert) après la coupure, ce qui est le comportement le plus sûr et le plus adapté pour ce type d'usage.

→ **Ma recommandation** : positionne-le sur **Remember last status**.

### 2. Problème de localisation GPS dans SmartLife (adresse décalée de ~300 m une fois enregistrée)

C'est un problème **assez fréquent** avec SmartLife/Tuya, surtout en zone résidentielle ou péri-urbaine. Le décalage vient souvent de :

- Une imprécision du GPS au moment de l'enregistrement (bâtiments, arbres, voiture...).
- Une correction automatique par les serveurs Tuya qui "snap" sur une adresse approximative.
- Le mode de localisation du téléphone (mode économie d'énergie qui utilise plus le Wi-Fi/cellulaire que le vrai GPS).

Solutions à essayer dans l'ordre :

1. Supprime complètement l'adresse domicile actuelle dans SmartLife (dans les paramètres Maison / Home → éditer la localisation).
2. Va **physiquement au milieu de ton entrée/portail**, téléphone en main, avec :

   - GPS activé en mode haute précision (Paramètres → Localisation → Mode haute précision).
   - Mode avion OFF, données mobiles + Wi-Fi activés.
   - Attends 1-2 minutes que le GPS se stabilise très bien (tu peux ouvrir Google Maps pour vérifier que tu es pile au bon endroit).
3. Recrée l'adresse domicile en pointant **manuellement** le plus précisément possible sur la carte (tu peux souvent déplacer le pin).
4. Si ça persiste, beaucoup d'utilisateurs règlent un rayon de géolocalisation un peu plus grand (ex. : 200-300 m au lieu de 50-100 m) pour compenser le décalage et rendre le déclenchement plus fiable.
5. Vérifie aussi que SmartLife a l'autorisation de localisation **« Tout le temps »** (paramètres téléphone → Applications → SmartLife → Localisation).

Le geofencing SmartLife reste malheureusement assez aléatoire (délais parfois longs, ratés occasionnels), même quand l'adresse est bonne. C'est une limite connue de l'app.

### 3. Automatisation pour fermer le portail une fois le véhicule stationné (sans cellules/capteurs)

Sans capteur physique (détecteur de présence voiture, contact fin de course, etc.), **c'est très compliqué de faire ça de manière fiable et sûre** uniquement avec SmartLife.

Les options réalistes (et leurs limites) :

- **Solution la plus simple et courante** : ajouter un **délai fixe** après l'arrivée Exemple d'automatisation :

  - Déclencheur : Arrivée à domicile (geofencing)
  - Action 1 : Ouvrir le portail
  - Action 2 : Attendre X minutes (ex. 3 à 5 min, le temps de rentrer et se garer)
  - Action 3 : Fermer le portail

  → C'est ce que font la majorité des gens sans capteur. Pas parfait, mais pragmatique.
- **Variante un peu plus fine** : utiliser une seconde condition sur ton téléphone Exemple : arrivée + « téléphone connecté au Wi-Fi de la maison » (ou Bluetooth si tu as un détecteur compatible) → mais ça reste approximatif.
- **La vraie solution fiable** (recommandée si tu veux vraiment éviter les oublis) : ajouter un capteur de présence voiture (PIR extérieur robuste + IP65, compatible Tuya/SmartLife Zigbee ou Wi-Fi) pointé sur l'emplacement parking. Tu pourras alors faire :

  - Arrivée → ouvrir
  - Présence voiture détectée + délai 1-2 min sans mouvement → fermer

Sans capteur supplémentaire, on reste limité au délai fixe (le plus robuste reste 3-4 minutes pour la plupart des gens).

N'hésite pas si tu as besoin d'aide pour la formulation exacte des automatisations ou si tu veux tester une capture d'écran de tes scénarios actuels. Bon courage, et prudence avec le portail ! 🚗🚪

---

## Message 3 — 12 janvier 2026 à 09:49 (Europe/Paris)

- **Identifiant :** `1741`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1741

Salut [@wakyky](https://forumdomotique.com/profile/992-wakyky/)

Merci pour tes questions précises ! Je vais répondre point par point

**1. Suppression de l’adresse domicile dans SmartLife**

Non, supprimer uniquement l’adresse domicile (utilisée pour le geofencing) ne devrait pas t’obliger à réinstaller l’ensemble de tes appareils. L’adresse est un paramètre spécifique pour les automatisations basées sur la localisation, et elle est indépendante de la configuration de tes devices (comme ton module Yokis). Tu peux la supprimer et la recréer sans toucher au reste de ta “Home” dans l’app. Attention cependant : si tu supprimes accidentellement la “Home” entière (pas juste l’adresse), là oui, tu perdras tout et devras ré-ajouter les appareils. Pour éviter ça, va précisément dans les paramètres de la Home > Localisation, et supprime seulement l’adresse – pas la Home elle-même.

**2. Activer le GPS en haute précision sur iPhone**

Sur iPhone (iOS 19 ou supérieur en 2026), c’est simple et rapide. Voici les étapes :

1.  Ouvre **Réglages** > **Confidentialité et sécurité** > **Services de localisation**.

2.  Assure-toi que les **Services de localisation** sont activés (toggle en vert).

3.  Fais défiler jusqu’à l’app **SmartLife** (ou Tuya), tape dessus.

4.  Sous “Autoriser l’accès à la localisation”, choisis **Toujours** ou **Lors de l’utilisation de l’app** (pour le geofencing, “Toujours” est recommandé).

5.  Active l’option **Localisation précise** (toggle en vert) – c’est ça qui améliore la précision GPS.

Ça utilise le GPS pur, Wi-Fi et cellulaire pour une meilleure précision. Si ton iPhone est en mode économie d’énergie, ça peut réduire la précision – désactive-le temporairement pour tester.

**3. Home Assistant (HA) : Installation, fiabilité et compatibilité**

J’avais mentionné HA comme alternative plus avancée à SmartLife pour des automatisations locales et plus fiables. Voici les détails :

•  **Moyen le plus simple d’installer HA** :  
L’option la plus plug-and-play en 2026 est d’acheter le **Home Assistant Green** (environ 100-150 €), un petit boîtier prêt à l’emploi avec HA OS préinstallé. Tu le branches, tu le connectes à ton réseau, et c’est parti en 5-10 minutes via l’app mobile ou le navigateur.   Sinon, sur un Raspberry Pi 4/5 (avec SSD pour la vitesse), télécharge HA OS depuis le site officiel, flash-le sur une carte SD/USB avec un outil comme Raspberry Pi Imager, et boot dessus – ça prend 15-20 minutes max.   Pas besoin de compétences avancées ; l’interface web guide tout. Évite les installations complexes comme Docker si tu débutes.

•  **Est-ce vraiment plus fiable que SmartLife ?**  
Oui, globalement bien plus fiable pour plusieurs raisons : HA fonctionne localement (pas besoin d’internet pour contrôler tes appareils une fois configurés), ce qui évite les lags, déconnexions cloud ou pannes serveur comme avec SmartLife/Tuya.    Les automatisations sont ultra-personnalisables (ex. : geofencing plus précis via ton téléphone ou capteurs), et il y a moins de dépendance à des serveurs distants. SmartLife est pratique pour débuter, mais HA est plus stable à long terme, surtout si tu as beaucoup d’appareils. Des utilisateurs rapportent des réponses quasi-instantanées avec HA vs des délais sur SmartLife.

•  **Compatibilité avec tes appareils (Yokis sur Somfy Lockyvia)** :  
Oui, la plupart seront compatibles via des intégrations dédiées. Pour ton module **Yokis** (souvent basé sur Tuya), HA a l’intégration **LocalTuya** qui permet un contrôle local sans cloud – super fiable.  Pour **Somfy Lockyvia**, c’est via l’intégration **Overkiz** (qui supporte Somfy nativement, y compris les motorisations de portail).    Si tu as un hub Somfy (comme TaHoma), active le mode développeur pour une connexion locale. Tes autres appareils SmartLife/Tuya migreront facilement – tu pourras même garder SmartLife en parallèle au début.

---

## Message 4 — 12 janvier 2026 à 10:36 (Europe/Paris)

- **Identifiant :** `1746`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1746

> **il y a 10 minutes, wakyky a dit :**
> De nouveau merci pour ces précisions
>
> Dans le cadre d'une éventuelle migration vers HA la solution HA Green me parait adequat vu mes compétences...😂
>
> SI je comprends bien, je peux donc "récupérer" mes appareils SmartLife déjà installés sans avoir à les reconfigurer ? Concernant le sujet avec l'automatisation du portail lorsque j'arrive chez moi, je garde l'automatisation créée sur SmartLife qui va "redescendre" dans HA ou je dois créer une nouvelle automatisation via HA qui serait plus fiable ?
>
> HA est il également compatible avec Atlantic Cozytouch ?
>
> Si je passe sur HA, quels marques d'objets connectés préconisez vous pour lumières ? caméras ? Thermostats ? modules ?

De rien, ravi d’aider ! 😊 Allons droit au but sur tes questions concernant la migration vers Home Assistant (HA). Je vais répondre en détail.

**1. Récupérer tes appareils SmartLife sans reconfigurer**

Oui, absolument ,tu peux intégrer la plupart de tes appareils SmartLife (basés sur Tuya) directement dans HA sans les réinitialiser ni les reconfigurer dans l’app SmartLife.  L’intégration **LocalTuya** (disponible via HACS, le store communautaire de HA) permet un contrôle local en scannant ton réseau pour détecter les appareils déjà connectés. Tu auras besoin des clés API Tuya (obtenues via un outil comme Tuya Developer ou un script simple), mais une fois fait, HA prend le relais sans toucher à ta config existante.  Si tu gardes SmartLife en parallèle au début, les deux apps coexisteront sans conflit. Pour ton module Yokis/Somfy, ça marchera via l’intégration Overkiz (native à HA), qui supporte les motorisations Somfy comme la Lockyvia.

**2. Automatisation du portail : Garder celle de SmartLife ou en créer une nouvelle dans HA ?**

Les deux sont possibles, mais je recommande fortement de **recréer l’automatisation directement dans HA pour plus de fiabilité et de flexibilité**.  L’automatisation SmartLife “redescendra” partiellement via LocalTuya (tu pourras la déclencher depuis HA), mais elle restera dépendante du cloud Tuya ce qui peut causer des lags ou des ratés si internet plante. Dans HA, tu pourras faire une automatisation locale 100% (basée sur geofencing via l’app HA Companion sur ton iPhone), avec des conditions avancées comme “arrivée + connexion Wi-Fi maison” ou un délai pour la fermeture.  C’est plus stable, et tu évites les problèmes aléatoires de SmartLife. Si tu veux tester, commence par importer tes devices, puis duplique l’automatisation dans HA c’est simple via l’interface Automations.

**3. Compatibilité HA avec Atlantic Cozytouch**

Oui, HA est compatible avec Atlantic Cozytouch !

L’intégration officielle passe par **Overkiz** (native dans HA), qui supporte de nombreux appareils Cozytouch comme les pompes à chaleur ou chauffe-eau Atlantic.  Pour les modèles non couverts (comme certains anciens ou spécifiques comme l’Aqueo/Excellia), il y a une intégration custom fiable via HACS : “Atlantic Cozytouch” (de gduteil sur GitHub), qui utilise l’API cloud mais avec un fallback local possible.  Ça marche bien pour la plupart des users configure avec tes identifiants Cozytouch, et tu auras contrôle total (températures, modes, etc.) dans HA. Si tu as un modèle précis, vérifie sur le forum HA pour des retours spécifiques.

**4. Marques recommandées pour objets connectés avec HA**

HA est ultra-compatible (plus de 2000 intégrations !), mais priorise les marques avec support local (sans cloud obligatoire) pour éviter les déconnexions.  Voici mes recos basées sur fiabilité, prix et intégration en 2026 je vise un mix abordable/avancé, compatible Matter/Zigbee/Z-Wave pour l’avenir :

•  **Lumières** : **Philips Hue** (top pour intégration locale via Hue Bridge, couleurs riches, fiable ; ~20-50€/ampoule).    Alternative budget : **IKEA Tradfri** (Zigbee/Matter, bon marché ~10-20€, excellentes pour automatisations). Ou **TP-Link Kasa** (Wi-Fi local, dimmable, ~15€). Évite les marques pure cloud si possible.

•  **Caméras** : **Reolink** (local-only via ONVIF/RTSP, excellentes pour surveillance sans abo ; ~50-150€, support Frigate dans HA pour détection AI).    Alternative : **Amcrest/Dahua** (qualité pro, local, ~80€). Pour sans fil : **Eufy** (batterie/solaire, intégration via HA sans cloud). Évite Nest/Arlo si tu veux du pur local.

•  **Thermostats** : **Ecobee** (intégration locale parfaite, capteurs intelligents, ~150-200€ ; top pour économies d’énergie).    Alternative budget : **Honeywell T6 Z-Wave** (~100€, local via Z-Wave). Ou **Meross/Venstar** (Wi-Fi local, simples et fiables).

•  **Modules (relais/switches)** : **Shelly** (Wi-Fi local, minuscules pour intégration discrète, ~15-30€ ; excellents pour automatisations avancées).   Alternative : **Zooz** (Z-Wave LR, fiable et bon marché ~20-40€). Pour dimmers : **Leviton** ou **TP-Link Kasa** (Matter-compatible).

Le HA Green est parfait pour débuter plug-and-play.

Si tu migres, installe HA d’abord en test sur un vieux PC/Raspberry pour importer tes devices sans risque. Si besoin de liens ou tutos précis (ex. : config LocalTuya ou autre), dis-moi !

---

## Message 5 — 13 janvier 2026 à 09:22 (Europe/Paris)

- **Identifiant :** `1772`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1772

Pas de problème, je t’aiderai à mettre en place tes intégrations avec plaisir !

Oui, tu peux garder les apps Somfy, Atlantic, Netatmo, etc., en parallèle de HA ; elles fonctionneront comme avant, car HA s’intègre sans les remplacer (c’est du local/cloud hybride).

Voici des liens officiels pour les intégrations HA :

Somfy : <https://www.home-assistant.io/integrations/somfy/>

Atlantic : <https://www.home-assistant.io/integrations/cozytouch/>

Netatmo : <https://www.home-assistant.io/integrations/netatmo/>

SmartLife (Tuya) : <https://www.home-assistant.io/integrations/tuya/>

Basculer tes devices SmartLife vers HA peut soulager ton WiFi si tu utilises des intégrations locales (moins de polling cloud), mais ça dépend de ta config.

Pour Zigbee, pars sur un Sonoff Zigbee 3.0 USB Dongle Plus (modèle P ou E), très bien pour commencer – abordable et compatible ZHA/Zigbee2MQTT.

---

## Message 6 — 14 janvier 2026 à 09:39 (Europe/Paris)

- **Identifiant :** `1778`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1778

Salut [@wakyky](https://forumdomotique.com/profile/992-wakyky/) ,

Tuya, tu peux soit l’installer en local, soit via l’application en cloud.

Pour Somfy et Atlantic, oui, les mêmes possibilités et plus via des scènes et automatisations que tu récupères via Home Assistant

---

## Message 7 — 14 janvier 2026 à 11:53 (Europe/Paris)

- **Identifiant :** `1782`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1782

Commence par le cloud, celui que j’ai mis en lien, puis après tu auras le temps de les intégrer en local.

---

## Message 8 — 15 janvier 2026 à 11:30 (Europe/Paris)

- **Identifiant :** `1793`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1793

Avec plaisir 👍

---

## Message 9 — 18 janvier 2026 à 12:08 (Europe/Paris)

- **Identifiant :** `1814`
- **Lien :** https://forumdomotique.com/forums/topic/643-smart-life-automatisation-portail-avec-localisation/#findComment-1814

L’appli **Home Assistant Companion** (dispo sur Android et iOS) est globalement très bien faite et agréable à utiliser au quotidien. Elle permet de :

<https://play.google.com/store/apps/details?id=io.homeassistant.companion.android&hl=fr>

<https://apps.apple.com/fr/app/home-assistant/id1099568401>

- Contrôler tes appareils (lumières, volets, prises, etc.)
- Voir l’état de tes capteurs
- Recevoir des notifications push super puissantes (on peut faire des actions très avancées dessus)
- Utiliser des widgets, des raccourcis, la localisation pour des automatisations, etc.

### La solution recommandée pour 95 % des utilisateurs → **Nabu Casa**

C’est clairement la méthode **la plus simple et la plus fiable** en 2025-2026.

Étapes typiques (souvent ça prend vraiment 5 min) :

1. Dans Home Assistant → **Paramètres → Home Assistant Cloud** (ou "Nabu Casa")
2. Tu crées un compte (ou tu te connectes) → tu prends l’essai gratuit 30 jours ou tu payes directement (~6-6,50 €/mois)
3. Tu actives **Remote Access** (bouton ON)
4. Dans l’appli mobile :

   - Menu → **Companion App** → **Home Assistant URL** (ou Serveur)
   - Tu choisis **"Use Home Assistant Cloud"** / **Utiliser Home Assistant Cloud**
5. L’appli bascule automatiquement entre connexion locale (wifi maison) et connexion distante

Et c’est tout. Pas de ports à ouvrir, pas de certificat à gérer, pas de galère avec l’IP qui change, connexion quasi instantanée, très sécurisé (tout chiffré de bout en bout).

Beaucoup de gens trouvent que les 6-7 €/mois valent largement le coup pour la tranquillité + ça aide financièrement les développeurs de Home Assistant (projet open source qui coûte très cher à maintenir).

### Tu veux absolument rester 100 % gratuit ?

Les meilleures options actuelles sont :

- **Cloudflare Tunnel** (avec le add-on officiel) → assez populaire en 2025-2026, plutôt stable
- **Tailscale** (VPN très simple) → hyper sécurisé, mais tu dois lancer le VPN sur ton téléphone (moins fluide que Nabu Casa)

Mais dans les deux cas… c’est quand même plus long et plus chiant à configurer que Nabu Casa.

**Bref résumé perso :** Si tu veux pouvoir piloter tranquillement depuis ton téléphone quand tu es au boulot / en vacances sans te prendre la tête → prends Nabu Casa (essai gratuit 30 jours pour tester, tu risques pas grand-chose). Si tu aimes vraiment bidouiller et que tu refuses de payer → vise Cloudflare Tunnel ou Tailscale.

Tu as déjà une préférence entre les deux philosophies (facilité vs gratuit) ? 😄

---
