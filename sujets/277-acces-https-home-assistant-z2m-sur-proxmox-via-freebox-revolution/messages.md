---
title: "Accès https home assistant + Z2M sur proxmox via freebox revolution"
---

# Accès https home assistant + Z2M sur proxmox via freebox revolution

- **Catégorie :** [Sauvegardes et Sécurité](https://forumdomotique.com/forums/82-sauvegardes-et-s%C3%A9curit%C3%A9/)
- **Sujet :** https://forumdomotique.com/forums/topic/277-acc%C3%A8s-https-home-assistant-z2m-sur-proxmox-via-freebox-revolution/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 24 juillet 2025 à 17:33 (Europe/Paris)

---

## Message 1 — 24 juillet 2025 à 17:33 (Europe/Paris)

- **Identifiant :** `622`
- **Lien :** https://forumdomotique.com/forums/topic/277-acc%C3%A8s-https-home-assistant-z2m-sur-proxmox-via-freebox-revolution/#findComment-622

> **Il y a 22 heures, SMA7829 a dit :**
> Bonjour à tous,
>
> Je cherche comment accéder à home assistant depuis l'extérieur (WAN Internet). J'ai lu et vu de nombreux tutos mais ils ne correspondaient pas à ma configuration et je n'ai pas encore réussi. Votre aide me serait bien utile.
>
> Ma configuration :
>
> -freebox revolution (adresse IP fixe), nom de domaine perso (NDD.freeboxos.fr)
>
> -serveur domotique : Lenovo sous Proxmox avec VM Home assistant + LXC Docker-Frigate + LXC MQTT + LXC Z2M + LXC Nginx
>
> -serveur NAS : HP Proliant N54L sous Proxmox avec OpenMediaVault + dossier partagé pour les sauvegardes HA et les flux caméras
>
> J'ai essayé avec le nom de domaine perso configuré dans la freebox : j'atterris systématiquement sur l'interface de ma freebox. J'ai vu que certains y arrivent ... :(
>
> J'ai essayé avec Duckdns : OK mais je ne privilégie pas cette configuration à long terme car je souhaite maîtriser ma sécurité de bout en bout
>
> Je vais tenter avec Nginx : j'ai créé un LXC à cet effet. Toutefois cela me semble être assez consistant comme manip...
>
> Si l'un de vous a une configuration équivalente peut-il m'apporter son aide pour arriver à accéder en https à mon home assistant ?
>
> Grand merci par avance.

Je suis moi même sur freebox dès ce week-end je t’aiderai à mettre en place pour moi passe par duckdns tu peux aussi passer par domaine freebox ou directement avec ton ip fix port :8123. Pour infos j ai mis en place le custom compenant pour la freebox <https://forumdomotique.com/forums/topic/101-pr%C3%A9sentation-du-projet-freebox_homexa/#comment-175>

---
