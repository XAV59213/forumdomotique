---
title: "Problème de démarrage avec Zigbee2MQTT et dongle SLZB MR2 (erreur de configuration)"
description: "Merci pour ton message et bienvenue dans la domotique ! 😊 SLZB MR2 est un excellent choix, surtout en Ethernet Je prépare un test complet avec…"
image: /assets/images/vignettes-themes/zigbee.jpg

date: 2025-10-21
cover_alt: "Vignette de rubrique Zigbee — XAV59213, Forum Domotique"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/449-probl%C3%A8me-de-d%C3%A9marrage-avec-zigbee2mqtt-et-dongle-slzb-mr2-erreur-de-configuration/">Lire et commenter sur Forum Domotique</a></p>

# Problème de démarrage avec Zigbee2MQTT et dongle SLZB MR2 (erreur de configuration)

- **Catégorie :** [Café Domotique](https://forumdomotique.com/forums/85-caf%C3%A9-domotique/)
- **Sujet :** https://forumdomotique.com/forums/topic/449-probl%C3%A8me-de-d%C3%A9marrage-avec-zigbee2mqtt-et-dongle-slzb-mr2-erreur-de-configuration/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 21 octobre 2025 à 17:33 (Europe/Paris)

---

## Message 1 — 21 octobre 2025 à 17:33 (Europe/Paris)

- **Identifiant :** `1079`
- **Lien :** https://forumdomotique.com/forums/topic/449-probl%C3%A8me-de-d%C3%A9marrage-avec-zigbee2mqtt-et-dongle-slzb-mr2-erreur-de-configuration/#findComment-1079

> **Le 18/10/2025 à 22:17, Davy76 a dit :**
> Salut à tous,
>
> Je me présente, Davy, 44 ans, tout nouveau dans la domotique 🙂  
>   
> J’ai acheté le dongle **SLZB MR2** suite aux conseilles dans la vidéo de **Zatoufly**, mais impossible de faire fonctionner **Zigbee2MQTT**.
>
> Je passe par **Ethernet**, j’ai bien copié la configuration sur la plateforme du dongle, mais j’obtiens cette erreur au démarrage :
>
> Si quelqu’un a une idée de ce qui cloche ou un exemple de config correcte pour le SLZB MR2 en Ethernet, je suis preneur !
>
> Merci d’avance pour votre aide 🙏

Salut Davy,

Merci pour ton message et bienvenue dans la domotique !

😊 **SLZB MR2** est un excellent choix, surtout en Ethernet.

Je prépare **un test complet avec installation pas à pas (Zigbee2MQTT +** SMLIGHT SLZB-MR4 **en Ethernet et usb )** dans les prochaines semaines. Je vais tout détailler :

- config du dongle
- YAML Zigbee2MQTT
- dépannage des erreurs courantes

Je posterai ça ici dès que c’est prêt.

En attendant, la cause Zigbee2MQTT **refuse de démarrer** parce que la valeur serial.adapter dans ton configuration.yaml **n’est pas reconnue** ou **mal orthographiée**.

Pour le **SLZB-MR2**, il faut **impérativement** mettre :

```yaml
serial:
  port: tcp://IP-DU-DONGLE:6638   # ou mdns://slzb-mr2
  adapter: zstack
```

Ou Astuce : Si tu utilises mDNS (et que ton réseau le supporte) :

```yaml
serial:
  port: mdns://slzb-mr2
  adapter: zstack
```

3. **Sauvegarde** → **Redémarre Zigbee2MQTT**

---

### Vérifications

- Le dongle est bien en **mode Ethernet** dans son interface web ? (pas USB)

---
