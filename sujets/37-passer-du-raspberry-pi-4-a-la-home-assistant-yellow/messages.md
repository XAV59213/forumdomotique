---
title: "Passer du Raspberry Pi 4 à la Home Assistant Yellow ?"
description: "Non, passer à la Yellow ne sert à rien pour ton problème Tu veux juste arrêter d’avoir peur de la carte SD qui crashe → la solution : des backups…"
image: /sujets/37-passer-du-raspberry-pi-4-a-la-home-assistant-yellow/images/og-partage.jpg

date: 2025-10-21
cover_alt: "Boîtier Home Assistant Yellow translucide sur un bureau, au coucher du soleil"
---
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/37-passer-du-raspberry-pi-4-%C3%A0-la-home-assistant-yellow/">Lire et commenter sur Forum Domotique</a></p>

# Passer du Raspberry Pi 4 à la Home Assistant Yellow ?

- **Catégorie :** [Box & Matériel](https://forumdomotique.com/forums/97-box-mat%C3%A9riel/)
- **Sujet :** https://forumdomotique.com/forums/topic/37-passer-du-raspberry-pi-4-%C3%A0-la-home-assistant-yellow/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 21 octobre 2025 à 18:18 (Europe/Paris)

---

## Message 1 — 21 octobre 2025 à 18:18 (Europe/Paris)

- **Identifiant :** `1082`
- **Lien :** https://forumdomotique.com/forums/topic/37-passer-du-raspberry-pi-4-%C3%A0-la-home-assistant-yellow/#findComment-1082

Salut [@CyberDuck](https://forumdomotique.com/profile/78-cyberduck/) !

**Non, passer à la Yellow ne sert à rien pour ton problème.**

Tu veux juste arrêter d’avoir peur de la carte SD qui crashe → **la solution : des backups automatiques**.

---

### Ce qu’il faut faire (3 étapes ultra simples) :

1. **Fais un backup complet maintenant** → *Paramètres > Système > Sauvegardes > Créer une sauvegarde complète* → Télécharge le fichier sur ton PC.
2. **Installe l’addon “Google Drive Backup”** → Dans *Add-ons > Boutique > cherche “Google Drive” > Installe* → Connecte ton compte Google (1 clic) → Il sauvegarde **automatiquement chaque nuit** dans ton Drive.
3. **Et c’est tout.** Même si ta carte SD meurt demain → tu restaures en 10 min sur un autre Pi ou même sur la Yellow plus tard.

---

Si tu veux pas de cloud → copie le backup sur un disque USB ou un NAS avec l’addon **Samba**.

---

**Résultat** :

- 0 stress
- 0 dépense
- 💪Ton Pi 4 reste parfait pour Home Assistant

La Yellow ? C’est juste plus joli et un peu plus rapide ❤️.

**Mais elle ne t’empêche pas de perdre tes données.** Les backups, oui.

---
