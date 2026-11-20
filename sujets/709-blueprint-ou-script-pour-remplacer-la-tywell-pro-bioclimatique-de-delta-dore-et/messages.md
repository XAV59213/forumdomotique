---
title: "Blueprint ou script pour remplacer la Tywell Pro bioclimatique de Delta Dore et piloter les volets selon luminosité et température"
---

# Blueprint ou script pour remplacer la Tywell Pro bioclimatique de Delta Dore et piloter les volets selon luminosité et température

- **Catégorie :** [Tutoriels, Guides & Astuces des Membres](https://forumdomotique.com/forums/87-tutoriels-guides-astuces-des-membres/)
- **Sujet :** https://forumdomotique.com/forums/topic/709-blueprint-ou-script-pour-remplacer-la-tywell-pro-bioclimatique-de-delta-dore-et-piloter-les-volets-selon-luminosit%C3%A9-et-temp%C3%A9rature/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 24 janvier 2026 à 13:21 (Europe/Paris)

---

## Message 1 — 24 janvier 2026 à 13:21 (Europe/Paris)

- **Identifiant :** `1873`
- **Lien :** https://forumdomotique.com/forums/topic/709-blueprint-ou-script-pour-remplacer-la-tywell-pro-bioclimatique-de-delta-dore-et-piloter-les-volets-selon-luminosit%C3%A9-et-temp%C3%A9rature/#findComment-1873

Salut [@Krysc61](https://forumdomotique.com/profile/125-krysc61/)

Oui, il est tout à fait possible de reproduire les fonctionnalités bioclimatiques de la box Tywell Pro dans Home Assistant sans avoir à l’acheter, en utilisant des automatisations, scripts ou encore mieux des blueprints existants. Puisque tu as déjà une box Tydom Pro pour gérer tes volets roulants, je suppose que tu as intégré tes volets comme entités “cover” dans HA (via l’intégration communautaire Tydom, par exemple). Si ce n’est pas le cas, commence par ça pour avoir le contrôle basique.

La Tywell Pro gère les occultants (volets) de manière automatique en se basant sur :

•  La température intérieure (via un thermostat ou Tywell Control).

•  La température extérieure et l’ensoleillement (via service météo ou capteurs optionnels).

•  Des modes comme l’absence, la centralisation, et une suspension si une fenêtre est ouverte.

Dans HA, tu peux répliquer ça avec des entités existantes :

•  **Température intérieure** : Utilise ton thermostat ou un capteur (ex. : entity climate.ton_thermostat ou sensor.temp_interieure).

•  **Température extérieure et ensoleillement** : Intègre une entité météo comme Météo-France, OpenWeatherMap ou [Met.no](https://Met.no) (gratuits). Ça donne la temp extérieure, les prévisions, l’état du ciel (ensoleillé/nuageux), et même l’UV ou la radiation solaire. Pour plus de précision, ajoute un capteur lux extérieur si tu en as un.

•  **Position du soleil** : L’entité intégrée sun.sun donne l’azimut, l’élévation et les heures de lever/coucher, idéal pour détecter si le soleil tape sur tes fenêtres.

•  **Détection d’ouverture** : Si tu as des capteurs de fenêtre (ex. : Zigbee ou via Tydom), utilise-les pour suspendre la descente des volets.

**Recommandation : Le blueprint “Cover Control Automation (CCA)”**

Il existe un blueprint excellent et très complet appelé **Cover Control Automation (CCA)**, créé par Herr.Vorragend, qui fait exactement ce que tu décris (et plus !). Il est conçu pour une gestion intelligente et bioclimatique des volets, stores ou auvents, en respectant des logiques comme celles de la RE2020 (optimisation énergétique via ombrage solaire et régulation thermique).

**Fonctionnalités clés qui matchent la Tywell Pro :**

•  **Gestion bioclimatique** : Ferme/ouvre les volets en fonction de la position du soleil (azimut/élévation pour éviter la surchauffe en été), de la température intérieure/extérieure, des prévisions météo (ensoleillement, temp forecast), et de la luminosité. Par exemple : ferme les volets si soleil direct + temp ext > 25°C et int > 22°C, pour bloquer la chaleur.

•  **Modes saisonniers/adaptatifs** : Ajuste automatiquement selon les saisons (élévation solaire dynamique), sans intervention manuelle.

•  **Mode absence/vacances** : Intègre un “mode résident” (via un input_boolean) pour pauser ou adapter les automatisations quand tu n’es pas là.

•  **Suspension sécurisée** : Si une fenêtre est ouverte (via capteur), il gère la ventilation partielle ou totale et évite de fermer les volets pour ne pas bloquer.

•  **Commande centralisée** : Contrôle un groupe de volets, avec positions personnalisées (ex. : fermé à 0%, ouvert à 100%, intermédiaire pour ventilation).

•  **Routines et planification** : Basé sur calendrier (intègre tes calendars Google/Outlook pour horaires), jours ouvrés/week-ends, et exceptions.

•  **Respect des overrides manuels** : Si tu ajustes manuellement un volet, il respecte ça pendant un temps configurable avant de reprendre l’auto.

•  **Fonctions force** : Overrides pour pluie, vent, gel, etc., avec retour automatique à l’état normal.

C’est hyper configurable : tu définis tes seuils (temp, azimuth solaire, etc.), et il supporte les logiques AND/OR pour combiner les conditions. Ça optimise le confort thermique et les économies d’énergie, comme la Tywell.

**Comment l’installer et l’utiliser :**

1.  Dans HA, va dans **Paramètres > Automatisations & Scènes > Blueprints**, clique sur “Importer un blueprint”.

2.  Utilise cette URL pour importer : <https://github.com/hvorragend/ha-blueprints/blob/main/blueprints/automation/cover_control_automation.yaml> (ou cherche “Cover Control Automation CCA” dans le forum HA pour la version la plus récente).

3.  Crée une nouvelle automatisation basée sur ce blueprint.

4.  Configure :

•  Tes entités volets (cover).

•  Entité météo (weather).

•  Capteurs temp/lux si dispo.

•  Calendrier pour plannings.

•  Un helper text (input_text) de 254 chars min pour tracker les états.

5.  Teste avec des traces pour affiner.

Si tu n’as pas encore d’entité météo, ajoute-en une via les intégrations HA (ex. : Météo-France pour la précision locale à Lyon). Pour l’ensoleillement, si la météo ne suffit pas, utilise l’intégration Sun pour des calculs avancés.

Si ce blueprint est trop complet, tu peux commencer avec une automatisation simple en YAML :

•  Trigger : Temp int > 23°C ET condition météo = “sunny” ET élévation soleil > 10°.

•  Action : Fermer volets (cover.close_cover).

•  Inversement pour ouverture.

Mais le blueprint CCA est vraiment top pour une réplique fidèle sans effort. Si tu as des détails sur tes entités actuelles (thermostat, météo)

---
