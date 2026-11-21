---
title: "Créer sa box domotique parfaite : de l'impression 3D à la configuration Home Assistant !"
description: "Mes projets fabriqués de A à Z : j’ai imprimé le boîtier, monté le Raspberry Pi, câblé les LEDs WLED et configuré Home Assistant."
image: /creations/box-domotique-impression-3d-home-assistant/images/TYtqE1G2.jpeg
date: 2025-09-20
section: creations
forum_comments: false
featured: true
tags:
  - Impression 3D
  - Home Assistant
---

# Créer sa box domotique parfaite : de l'impression 3D à la configuration Home Assistant !

<p class="az-kicker"><span class="az-badge">A à Z</span> Une création de XAV59213 — impression 3D, montage et configuration Home Assistant.</p>

<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/402-cr%C3%A9er-sa-box-domotique-parfaite-de-limpression-3d-%C3%A0-la-configuration-home-assistant/">Lire et commenter sur Forum Domotique</a></p>

<section class="carousel photo-carousel" data-carousel data-lightbox aria-roledescription="carrousel" aria-label="Photos de la création (10)" tabindex="0">
<div class="carousel-track" data-track>
<figure class="photo-slide" data-slide>
  <a href="images/TYtqE1G2.jpeg" data-full="images/TYtqE1G2.jpeg" data-alt="La box terminée, face avant avec le logo Home Assistant" aria-label="Agrandir la photo 1 : La box terminée, face avant avec le logo Home Assistant">
    <img src="images/TYtqE1G2.jpeg" alt="La box terminée, face avant avec le logo Home Assistant" loading="eager">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/6x7flaj0.jpeg" data-full="images/6x7flaj0.jpeg" data-alt="Le Raspberry Pi 4 installé dans le boîtier imprimé en 3D" aria-label="Agrandir la photo 2 : Le Raspberry Pi 4 installé dans le boîtier imprimé en 3D">
    <img src="images/6x7flaj0.jpeg" alt="Le Raspberry Pi 4 installé dans le boîtier imprimé en 3D" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/ho8c4uTR.jpeg" data-full="images/ho8c4uTR.jpeg" data-alt="Câblage du Raspberry Pi dans le boîtier" aria-label="Agrandir la photo 3 : Câblage du Raspberry Pi dans le boîtier">
    <img src="images/ho8c4uTR.jpeg" alt="Câblage du Raspberry Pi dans le boîtier" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/HSaMASQ4.jpeg" data-full="images/HSaMASQ4.jpeg" data-alt="Boîtier fermé, antenne Zigbee en place" aria-label="Agrandir la photo 4 : Boîtier fermé, antenne Zigbee en place">
    <img src="images/HSaMASQ4.jpeg" alt="Boîtier fermé, antenne Zigbee en place" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/GSSkG4Gz.jpeg" data-full="images/GSSkG4Gz.jpeg" data-alt="Bandeau LED et plaque avant au logo Home Assistant" aria-label="Agrandir la photo 5 : Bandeau LED et plaque avant au logo Home Assistant">
    <img src="images/GSSkG4Gz.jpeg" alt="Bandeau LED et plaque avant au logo Home Assistant" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/x5PCf4A2.jpeg" data-full="images/x5PCf4A2.jpeg" data-alt="Raspberry Pi et D1 Mini dans le boîtier" aria-label="Agrandir la photo 6 : Raspberry Pi et D1 Mini dans le boîtier">
    <img src="images/x5PCf4A2.jpeg" alt="Raspberry Pi et D1 Mini dans le boîtier" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/BHCt2oKa.jpeg" data-full="images/BHCt2oKa.jpeg" data-alt="Montage avec le dongle Zigbee et le câble Ethernet" aria-label="Agrandir la photo 7 : Montage avec le dongle Zigbee et le câble Ethernet">
    <img src="images/BHCt2oKa.jpeg" alt="Montage avec le dongle Zigbee et le câble Ethernet" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/M4HZ3-OW.jpeg" data-full="images/M4HZ3-OW.jpeg" data-alt="Câblage des LEDs dans le boîtier" aria-label="Agrandir la photo 8 : Câblage des LEDs dans le boîtier">
    <img src="images/M4HZ3-OW.jpeg" alt="Câblage des LEDs dans le boîtier" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/ZA0esTQN.jpeg" data-full="images/ZA0esTQN.jpeg" data-alt="Pose des vis et des inserts filetés" aria-label="Agrandir la photo 9 : Pose des vis et des inserts filetés">
    <img src="images/ZA0esTQN.jpeg" alt="Pose des vis et des inserts filetés" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/an7p6TRN.jpeg" data-full="images/an7p6TRN.jpeg" data-alt="Insertion de la carte SD dans le Raspberry Pi" aria-label="Agrandir la photo 10 : Insertion de la carte SD dans le Raspberry Pi">
    <img src="images/an7p6TRN.jpeg" alt="Insertion de la carte SD dans le Raspberry Pi" loading="lazy">
  </a>
</figure>
</div>
<button type="button" class="carousel-nav" data-prev aria-label="Faire défiler vers la gauche">‹</button>
<button type="button" class="carousel-nav" data-next aria-label="Faire défiler vers la droite">›</button>
<p class="carousel-hint">Faites défiler horizontalement pour voir les photos de la création.</p>
</section>


## Salut la communauté domotique !

Je suis un débutant en la matière sur la 3D, mais grâce à un tuto ultra clair d'Abrégé sur YouTube (lien en bas), j'ai réussi à monter ma propre box domotique DIY. C'est pas cher, customisable à mort, et hyper satisfaisant de voir tout fonctionner avec Home Assistant. Si vous êtes un peu perdu avec l'électronique et le soft, ce guide est pour vous. On va y aller étape par étape, sans jargon compliqué. Budget total estimé : autour de 150-200€ selon les options.

**Pourquoi faire ça ?** Une box perso, c'est plus stable qu'une cloud payante, open-source, et vous pouvez l'améliorer comme vous voulez (Zigbee, Matter, LED RGB... le rêve !). Prêt ? Allons-y !

## 1. La Liste des Composants (Le Matos Essentiel)

Pas besoin d'être ingénieur, tout est dispo sur Amazon, AliExpress ou Kubii. J'ai mis des liens directs pour simplifier.

| Composant | Description | Lien / Prix Approx. | Pourquoi ? |
| --- | --- | --- | --- |
| **Raspberry Pi 4 (4Go ou 8Go)** | Le cerveau de la box. Prenez un kit starter pour avoir tout inclus. | [Kit 4Go chez Kubii (code ABREGE-MAKE pour -5%)](https://www.kubii.com/fr/kits-nano-ordinateurs/3011-starter-kit-raspberry-pi4-4gb-3272496302112.html) ~60€ | Puissant pour HA, tourne 24/7 sans broncher. |
| **Carte SD (32Go min)** | Pour installer Home Assistant. | Incluse dans le kit ou [Amazon](https://amzn.to/4d0LdPx) ~10€ | Stockage rapide et fiable. |
| **Alimentation RPi** | 5V/3A USB-C. | Incluse dans le kit ou [Amazon](https://amzn.to/3J74C3c) ~10€ | Évite les crashes dus à une alim foireuse. |
| **Dongle Zigbee** | Pour connecter vos capteurs (Sonoff, IKEA...). | [AliExpress](https://s.click.aliexpress.com/e/_DFelMZ7) ~15€ | Le must pour une domotique sans fil low-cost. |
| **Boîtier 3D** | Fichiers STL gratuits. | [Printables](https://www.printables.com/fr/model/835545-box-domotique-2024-version-zigbee-matter) Gratuit | Personnalisable, avec support pour RPi et dongle. |
| **Inserts filetés M2.5** | Pour fixer le RPi et la plaque avant. | [Amazon](https://amzn.to/49tjlR5) ~5€ (paquet) | Fixation solide sans abîmer le plastique. |
| **Vis M2.5x5mm** | Pour l'assemblage. | [AliExpress](https://s.click.aliexpress.com/e/_DEMfZAh) ~2€ | Petites mais costaudes. |
| **Aimants 10x2mm** | Pour coller la box au mur. | [Amazon](https://amzn.to/3vzhM6f) ~5€ | Montage facile, sans percer partout. |
| **Colle forte** | Pour fixer les aimants. | [Amazon](https://amzn.to/4aO1rJP) ~5€ | Une goutte suffit, attention aux doigts ! |
| **Rallonge USB-A** | Pour déporter le dongle Zigbee. | [Amazon](https://amzn.to/49qIprN) ~5€ | Évite les interférences radio. |
| **Bandeau LED WS2812B (60 LEDs/m)** | Pour un éclairage ambiance. Optionnel mais cool. | [AliExpress](https://s.click.aliexpress.com/e/_DEYI9jT) ~10€ | Intégrable à HA pour des automatisations fun. |
| **ESP8266 D1 Mini** | Contrôleur pour les LEDs via WLED. | [AliExpress](https://s.click.aliexpress.com/e/_DcyKdeZ) ~3€ | Facile à flasher, compatible HA. |
| **Adaptateur NVMe + SSD M.2** | Pour booster le stockage (optionnel). | [Adaptateur Ali](https://s.click.aliexpress.com/e/_Ddrh19f) + [SSD Amazon](https://amzn.to/4aGBeg7) ~30€ | HA plus fluide si vous avez beaucoup de devices. |
| **Ventilo 5V 40mm** | Refroidissement (conseillé). | [Amazon](https://amzn.to/3Ja3KLq) ~5€ | Le RPi chauffe, ça prolonge la vie de la box. |
| **Dissipateur thermique** | Petit bonus. | [AliExpress](https://fr.aliexpress.com/item/4000252442732.htm) ~2€ | Pas obligatoire mais why not. |
| **Plaque acrylique 3mm** | Pour la face avant (ou imprimez-la). | [Plexiglass sur mesure](https://plexiglasssurmesure.fr/produit/plaque-plexiglass-givre-3mm/) ~10€ | Look pro, protège les composants. |

Astuce débutant : Commencez par le minimum (RPi 4+ SD + dongle + boîtier). Ajoutez les LEDs après pour tester. Total mini : ~100€.

## 2. Impression 3D du Boîtier (Facile si vous avez une imprimante)

- Téléchargez les fichiers abrége STL sur [Printables](https://www.printables.com/fr/model/835545-box-domotique-2024-version-zigbee-matter).
- Téléchargez les fichiers Ivo STL sur [Printables.](https://www.printables.com/model/1316089-box-domotique-pour-raspberry-pi-5)
- Utilisez du PLA ou PETG (durable). Paramètres : 0.2mm de hauteur de couche, 20% infill, supports si besoin pour les parties complexes.
- Temps d'impression : 4-6h selon votre machine (Ender 3 ou Prusa ou ARTILLERY GENIUS OK).
- Une fois imprimé, chauffez les inserts M2.5 avec un fer à souder ou un pistolet à air et enfoncez-les dans les trous prévus.

Pour slice vos impression en gcode et modifier le sens d'impression j'utilise cura <https://ultimaker.com/fr/software/ultimaker-cura/>

![Capture d’écran du 2025-09-20 15-02-01.png](images/Capturedcrandu2025-09-2015-02-01.png)

**INFOS :** Vérifiez l'orientation des pièces avant impression pour éviter les supports inutiles E T les ponts . Si pas d'imprimante, demandez à un fablab ou sur le forum !

![Capture d’écran du 2025-09-20 14-41-45.png](images/Capturedcrandu2025-09-2014-41-45.png)![Capture d’écran du 2025-09-20 14-42-15.png](images/Capturedcrandu2025-09-2014-42-15.png)![Capture d’écran du 2025-09-20 14-42-27.png](images/Capturedcrandu2025-09-2014-42-27.png)![Capture d’écran du 2025-09-20 14-52-03.png](images/Capturedcrandu2025-09-2014-52-03.png)

## 3.a Assemblage Physique (Comme du Lego, mais avec des vis)

- Montez le RPi sur la base avec les vis M2.5.
- Collez les aimants sur l'arrière pour le fix au mur (séchage 24h).
- Branchez le dongle Zigbee via la rallonge USB et fixez-le dans son compartiment.
- Si LEDs : Soudez/connectez le bandeau au D1 Mini (tutos WLED en 5 min). Intégrez-le dans le boîtier.
- Ajoutez le ventilo sur le RPi si chaud (câblez sur GPIO 5V).
- Fermez avec la plaque acrylique (vis ou clips).

**Conseil :** Testez tout à plat avant de fermer. Utilisez un multimètre si vous doutez des connexions. Temps : 30-45 min.

## 3.b montage de la carte rpi4 (Attention!!!)

Dans mon cas, le ventilo Noctua était plug and play sur Raspberry Pi 4B ; cela a bien fonctionné avec Noctua connecté avec Noir (GND) sur le port 6, Rouge (Alimentation) sur le port 4 et Jaune (PWM) sur le port 8, même si la masse et l'alimentation sont inversées selon <https://pinout.xyz/#>.

![Capture d’écran du 2025-09-21 12-22-19.png](images/Capturedcrandu2025-09-2112-22-19.png)

#### . Montage 1 : tout est relié au même pin.

![Capture d’écran du 2025-09-25 16-59-29.png](images/Capturedcrandu2025-09-2516-59-29.png)

#### . Montage 2 : conçu pour des raisons pratiques : en cas de défaillance des LEDs ou de la ventilation, il permet d'éviter de modifier toutes les soudures.

![Capture d’écran du 2025-09-26 13-36-57.png](images/Capturedcrandu2025-09-2613-36-57.png)

## 3.c Montage des leds

![GSSkG4Gz.jpeg](images/GSSkG4Gz.jpeg)

![M4HZ3-OW.jpeg](images/M4HZ3-OW.jpeg)

## 3.d Paramétrage D1MINI (Bientôt disponible pas encore reçu !)

**Pour les LEDs :** Flashez le D1 Mini avec [ESPHOME FLASHER](https://install.wled.me/).

a. Installer ESPhome Flasher ▶ [https://github.com/esphome/esphome-fl...](https://github.com/esphome/esphome-fl)

b. Ouvrir l'application ESPhome Flasher

c. Brancher votre D1 mini en usb sur votre pc, choisir le port de com puis dans le browse aller chercher votre téléchargement bin moi esp8266_compact

Firmware WLED ▶ [https://github.com/Aircoookie/WLED/re...](https://github.com/Aircoookie/WLED/releases) Voici le lien directe de téléchargement du [ESP8266.bin](https://github.com/wled/WLED/releases/download/v0.15.1/WLED_0.15.1_ESP8266.bin)

j'ai eu des erreur avec la version esp8266.bin

![FVasgKeN.jpeg](images/FVasgKeN.jpeg)

##### Maintenant allons sur le téléphone !

Installer l'application WLED:

Application WLED iOS ▶ [https://apps.apple.com/us/app/wled/id...](https://apps.apple.com/us/app/wled/id1475695033)

Application WLED Google ▶ [https://play.google.com/store/apps/de...](https://play.google.com/store/apps/details?id=com.aircoookie.WLED&hl=fr_CH&gl=US&pli=1)

**Étape 1 :** Laisser votre usbD1MINI BRANCHER SUR VOTRE PC C'EST PAS FINI !

**Étape 2** : Sur votre téléphone déconnecter vous de votre réseau WIFI , puis cherche Wled il va vous demander un mot de passe ; **wled1234**

**Étape 3** : Maintenant vous pouvez ouvrir l’application wled de votre téléphone.

**Étape 4** : Paramétrage de votre réseau sur le d1 mini, il va vous proposer un scan pour trouver votre wifi !

Un petit clic y a plus cas mettre votre mot de passe réseau

**Étape 5 : Y a plus qua configurer les led !**

**Maintenant que vous avez paramétrer le wifi sur le d1mini il doit apparaitre sur votre réseau rechercher l'ip local du d1mini puis ajouter le a l'intégration wled**

![3dJ5dUuW.jpeg](images/3dJ5dUuW.jpeg)

![6DJKNNcx.jpeg](images/6DJKNNcx.jpeg)

![Ttl7fVEr.jpeg](images/Ttl7fVEr.jpeg)

**Étape 6 :** Configuration finale des GPIO et caractéristiques des LED **(Direction l'pplication wled config /LED preferences)**

![cp1SJiQu.jpeg](images/cp1SJiQu.jpeg)

![Fl_nQH1E.jpeg](images/Fl_nQH1E.jpeg)

- Modifier mA/led par vos LED moi de type 5v ws281x
- Length : Quantité de led
- Data GPIO :4 c'est le fil vert de la data l emplacement que j'ai indiquer D2 = GPIO 4
- Sauvegarder il ne vous reste plus qu'a faire finaliser les branchement !

![EnyQyO6w.jpeg](images/EnyQyO6w.jpeg)

![Capture d’écran du 2025-09-27 14-06-49.png](images/Capturedcrandu2025-09-2714-06-49.png)

<video class="creation-video" controls preload="metadata" width="900">
  <source src="images/TNlSggyB.mp4" type="video/mp4">
  Votre navigateur ne permet pas la lecture de la vidéo.
</video>

## 4. Installation du Logiciel (Home Assistant en 10 min)

- Téléchargez [Raspberry Pi Imager](https://www.raspberrypi.com/software/) sur votre PC.
- Insérez la carte SD, choisissez "Raspberry Pi OS" mais sélectionnez l'option Home Assistant (image complète HA). Écrivez sur la SD.
- Insérez la SD dans le RPi, branchez alim + Ethernet (WiFi après).
- Attendez 20-30 min : HA s'installe seul. Accédez via <http://homeassistant.local:8123> (ou IP du RPi).

CHOISIR LE MODÈLE DE VOTRE RASPBERRY

![Capture d’écran du 2025-09-20 12-47-42.png](images/Capturedcrandu2025-09-2012-47-42.png)![Capture d’écran du 2025-09-20 12-47-49.png](images/Capturedcrandu2025-09-2012-47-49.png)

CHOISIR LE SYSTÈME HOMEASSITANT

![Capture d’écran du 2025-09-20 12-54-11.png](images/Capturedcrandu2025-09-2012-54-11.png)![Capture d’écran du 2025-09-20 12-49-09.png](images/Capturedcrandu2025-09-2012-49-09.png)![Capture d’écran du 2025-09-20 12-49-18.png](images/Capturedcrandu2025-09-2012-49-18.png)![Capture d’écran du 2025-09-20 12-49-28.png](images/Capturedcrandu2025-09-2012-49-28.png)![Capture d’écran du 2025-09-20 12-49-49.png](images/Capturedcrandu2025-09-2012-49-49.png)

CHOISIR VOTRE SD POUR INSTALLATION DE l'OS

![Capture d’écran du 2025-09-20 12-54-22.png](images/Capturedcrandu2025-09-2012-54-22.png)![Capture d’écran du 2025-09-20 12-54-11.png](images/Capturedcrandu2025-09-2012-54-11.png)

C’est presque fini , Vous pouvez maintenant appuyer sur Maj + Ctrl + X pour afficher une boîte de dialogue de paramètres avancés et configurer

![Capture d’écran du 2025-09-20 13-09-21.png](images/Capturedcrandu2025-09-2013-09-21.png)![Capture d’écran du 2025-09-20 13-08-51.png](images/Capturedcrandu2025-09-2013-08-51.png)![Capture d’écran du 2025-09-20 13-09-01.png](images/Capturedcrandu2025-09-2013-09-01.png)![Capture d’écran du 2025-09-20 13-09-12.png](images/Capturedcrandu2025-09-2013-09-12.png)

y a plus cas faire suivant

![Capture d’écran du 2025-09-20 13-09-21.png](images/Capturedcrandu2025-09-2013-09-21.png)![Capture d’écran du 2025-09-20 13-09-28.png](images/Capturedcrandu2025-09-2013-09-28.png)![Capture d’écran du 2025-09-20 13-09-57.png](images/Capturedcrandu2025-09-2013-09-57.png)

- Insérez la SD dans le RPi, branchez alim + Ethernet (WiFi après).

![an7p6TRN.jpeg](images/an7p6TRN.jpeg)![BHCt2oKa.jpeg](images/BHCt2oKa.jpeg)![_elfBcRl.jpeg](images/elfBcRl.jpeg)

- Attendez 20-30 min : HA s'installe seul. Accédez via <http://homeassistant.local:8123> ou l ip de votre Raspberry Pi.

![RpdxbYqf.jpeg](images/RpdxbYqf.jpeg)![Capture d’écran du 2025-09-21 11-51-17.png](images/Capturedcrandu2025-09-2111-51-17.png)

![Capture d’écran du 2025-09-21 11-51-30.png](images/Capturedcrandu2025-09-2111-51-30.png)

**Pour le Dongle Zigbee :**

- Flashez-le avec [Silabs Firmware Builder](https://darkxst.github.io/silabs-firmware-builder/) (choisissez EZSP pour ZHA).
- Si pas reconnu, installez les drivers Silicon Labs [ici](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads).
- Dans HA, ajoutez l'intégration ZHA (ou Zigbee2MQTT si pref).

## 5. Configuration Home Assistant (Les Bases pour Débuter)

- Créez votre user lors du premier login OU envoyer une sauvegarde.

![Capture d’écran du 2025-09-21 11-52-13.png](images/Capturedcrandu2025-09-2111-52-13.png)

- Ajoutez ZHA : Settings > Devices & Services > Add Integration > ZHA. Sélectionnez le dongle.
- Pairez vos premiers devices (ampoules Zigbee) : Appuyez sur reset, scannez dans HA.
- Automatisation simple : Créez une scène pour allumer les LEDs au coucher du soleil (via blueprint ou YAML basique).
- Dashboard : Utilisez Lovelace pour un interface clean (ajoutez cartes pour lumières, capteurs).

**Tips pour nuls :**

- Sauvegardez tout via Google Drive dans HA.
- Si bug : Redémarrez le RPi (bouton ou SSH). Forums HA en français sont top.
- Sécurité : Changez le mot de passe, utilisez HTTPS.
- Évoluez : Ajoutez ESP32 pour plus de capteurs.

## Conclusion

Et voilà, votre box est prête ! La mienne tourne depuis des mois sans souci, et j'ai ajouté des volets roulants Zigbee2MQTT sans galère. C'est addictif, vous verrez. Si vous suivez le tuto vidéo d'Abrégé, c'est encore plus visuel – il explique tout avec humour.

Lien YouTube : [Fabriquer la box domotique parfaite ! (Home Assistant 2024)](https://www.youtube.com/watch?v=l0vsfXwWngg)

*(Sources : Basé sur le tuto d'Abrégé, vérifié en septembre 2025. .)*

![6x7flaj0.jpeg](images/6x7flaj0.jpeg)![HSaMASQ4.jpeg](images/HSaMASQ4.jpeg)![ho8c4uTR.jpeg](images/ho8c4uTR.jpeg)![ZA0esTQN.jpeg](images/ZA0esTQN.jpeg)![TYtqE1G2.jpeg](images/TYtqE1G2.jpeg)![x5PCf4A2.jpeg](images/x5PCf4A2.jpeg)

![FVasgKeN.jpeg](images/FVasgKeN.jpeg)

