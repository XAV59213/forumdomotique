---
title: "ZBDongle-E et Z2M"
---

# ZBDongle-E et Z2M

- **Catégorie :** [Sonoff](https://forumdomotique.com/forums/55-sonoff/)
- **Sujet :** https://forumdomotique.com/forums/topic/113-zbdongle-e-et-z2m/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 31 janvier 2026 à 13:13 (Europe/Paris)

---

## Message 1 — 31 janvier 2026 à 13:13 (Europe/Paris)

- **Identifiant :** `1934`
- **Lien :** https://forumdomotique.com/forums/topic/113-zbdongle-e-et-z2m/#findComment-1934

> **Le 24/05/2025 à 19:18, nico8383 a dit :**
> bonjour,
>
> je suis sur HA Yellow, donc pas de clef externe, je me suis servi du add-on Silicon Labs Flasher pour flasher le firmware.
>
> mais quand je lance Z2M j'ai ce message d'erreur : zh:ember:uart:ash: Received ERROR from adapter while connecting, with code=RESET_WATCHDOG.
>
> 9a n’empêche pas le démarrage du module. Je ne sais pas si c'est grave . Merci

Bonjour !

Sur le **Home Assistant Yellow**, ce message d’erreur :

```plaintext
zh:ember:uart:ash: Received ERROR from adapter while connecting, with code=RESET_WATCHDOG
```

est **très courant** quand on utilise le driver **ember** (le nouveau driver recommandé pour les puces Silicon Labs type MGM21x du Yellow).

**La bonne nouvelle** : Dans la très grande majorité des cas (surtout si tu as flashé avec le Silicon Labs Flasher add-on), **ce n’est pas grave** et **ça n’empêche pas le fonctionnement normal** une fois que Z2M a démarré.

### Pourquoi ce message apparaît-il ?

- C’est lié au protocole ASH (la couche de communication UART entre le host et le NCP).
- Au démarrage, le module reset parfois via un **watchdog** (souvent à cause d’un petit décalage timing, flow control hardware mal géré, ou comportement du firmware).
- Z2M voit ce reset comme une erreur, mais il **retente automatiquement** la connexion et passe en général en mode normal après.

### Est-ce que tu dois t’inquiéter ?

- **Non**, tant que :

  - Z2M démarre complètement (tu arrives à accéder à l’interface web de Z2M)
  - Les appareils Zigbee sont bien découverts / contrôlés
  - Pas de redémarrages en boucle de l’add-on toutes les 1-2 minutes
  - Pas d’erreurs répétées du style ERROR_EXCEEDED_MAXIMUM_ACK_TIMEOUT_COUNT ou ASH_NCP_FATAL_ERROR**après** le démarrage

Si tout fonctionne normalement après ce message → tu peux l’ignorer, c’est un warning connu et bénin sur HA Yellow + ember.

### Ce que tu peux vérifier / essayer si tu veux être tranquille

1. Regarde les logs Z2M complets (juste après le démarrage) : est-ce que ça continue avec des messages normaux genre « Coordinator firmware type: EmberZNet » puis « Zigbee2MQTT started » ?
2. Vérifie ta config Z2M (configuration.yaml de l’add-on) :

```plaintext
serial:
  port: /dev/ttyAMA1   # ← normalement c’est ça sur Yellow
adapter: ember
```

1. → **Ne mets surtout pas**rtscts: true (ou enlève cette ligne si elle existe). Beaucoup de gens ont le watchdog précisément à cause de ça sur Yellow/SkyConnect.
2. Quelle version de firmware as-tu flashée ? Les firmwares **7.4.x** (surtout 7.4.3 ou 7.4.4) marchent bien. Si tu es sur une version très récente ou beta, tu peux essayer de revenir sur une version stable connue (ex: 7.4.3.0 ou 7.4.4.0).
3. Si malgré tout tu as des plantages / reconnexions fréquentes → essaie de redémarrer complètement le Yellow (power cycle, pas juste restart HA) après avoir arrêté Z2M.

En résumé : **si tout marche**, ce message est juste « bruyant » mais pas problématique sur HA Yellow avec ember.

N’hésite pas à me donner plus de logs (les 30-40 lignes autour du démarrage de Z2M) si tu vois d’autres erreurs après, ou si l’add-on redémarre en boucle. 😊

---
