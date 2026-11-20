---
title: "Shema de principe"
---

# Shema de principe

- **Catégorie :** [Tâches Ménagères Automatisées](https://forumdomotique.com/forums/74-t%C3%A2ches-m%C3%A9nag%C3%A8res-automatis%C3%A9es/)
- **Sujet :** https://forumdomotique.com/forums/topic/289-shema-de-principe/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 1
- **Premier message de XAV59213 :** 30 novembre 2025 à 17:45 (Europe/Paris)

---

## Message 1 — 30 novembre 2025 à 17:45 (Europe/Paris)

- **Identifiant :** `1409`
- **Lien :** https://forumdomotique.com/forums/topic/289-shema-de-principe/#findComment-1409

kikou [@romantho](https://forumdomotique.com/profile/299-romantho/) bienvenue a toi et désoler pour le retard il y a tellement de post !

Voici une solution simple, fiable et peu chère pour ton étendoir automatique anti-pluie, avec commande manuelle possible à tout moment.

### Fonctions demandées

- Sortie automatique dès qu’il ne pleut plus (ou manuellement)
- Rentrée automatique dès qu’il pleut (ou manuellement)
- Priorité à la commande manuelle (tu peux forcer la montée ou la descente même s’il pleut)
- Les actionneurs 12 V ont déjà des fins de course intégrées → ils s’arrêtent tout seuls en butée

### Matériel nécessaire (en plus de ce que tu as déjà)

1. 1 relais inverseur DPDT 12 V (double inverseur) – 10 A mini → très important, c’est lui qui inverse le sens des actionneurs Exemple : Finder 40.52 ou 40.61, ou un relais automobile 5 broches « change-over »
2. 2 relais simples NO (normalement ouvert) 12 V – 10-30 A (un pour la montée, un pour la descente)
3. 1 interrupteur à 3 positions à rappel (haut/bas avec position centrale au repos) type interrupteur de store ou de volet roulant. Référence courante : Legrand 067901 ou Céliane 067175 (ou équivalent Schneider, etc.) → c’est un inverseur à rappel automatique au centre.
4. 1 capteur de pluie 12 V 4 fils Généralement :

   - Marron ou Rouge : +12 V
   - Bleu : GND (0 V)
   - Noir : sortie « il pleut » (contact fermé quand il pleut ou sortie 0 V quand il pleut selon modèle)
   - Jaune/Vert : souvent non utilisé ou sortie « pas de pluie » → La très grande majorité des capteurs de pluie 12 V ferment un contact (ou mettent la sortie à 0 V) quand il pleut.
5. 1 petite boîte de dérivation ou coffret étanche pour tout mettre à l’abri
6. Du câble 2 x 1,5 mm² ou 2,5 mm² pour les actionneurs (selon longueur)
7. Quelques dominos ou Wago + un peu de gaine thermo

### Principe de fonctionnement ultra-simple

- L’interrupteur manuel à 3 positions peut à tout moment forcer la montée ou la descente.
- Quand tu laisses l’inter au centre → c’est le capteur de pluie qui prend la main :

  - S’il pleut → descente auto
  - S’il ne pleut plus → montée auto

### Schéma de principe

> Alim 12V +
>
> │
>
> ├───────► +12V capteur pluie (fil rouge/marron)
>
> │
>
> ├───────► Bobine des 3 relais (les 3 bobines en parallèle)
>
> │
>
> Alim 12V - (GND)
>
> │
>
> └───────► GND capteur pluie (fil bleu)
>
> Sortie capteur pluie quand il pleut (fil noir) → relié au GND
>
> Quand il ne pleut pas → sortie ouverte
>
> Interrupteur à 3 positions (type store) :
>
> Position HAUT (poussoir vers le haut) → broche 1 reliée à broche 2
>
> Position BAS (poussoir vers le bas) → broche 1 reliée à broche 3
>
> Position milieu → rien relié
>
> Broche 1 de l’inter → reliée en permanence au +12V
>
> Broche 2 (sortie quand tu pousses haut) → commande le relais MONTÉE
>
> Broche 3 (sortie quand tu pousses bas) → va au fil noir du capteur pluie
>
> Relais 1 : MONTÉE (bobine entre +12V et broche 2 de l’inter)
>
> Relais 2 : DESCENTE (bobine entre +12V et (broche 3 inter OU fil noir capteur))
>
> Relais inverseur (DPDT) : on utilise les 2 jeux de contacts inverseurs
>
> Commun 1 et Commun 2 → vers les 2 fils des actionneurs
>
> NO1 et NC2 → +12V
>
> NC1 et NO2 → GND
>
> Contacts des relais Montée et Descente :
>
> Quand le relais MONTÉE est excité → il alimente la bobine du relais inverseur dans un sens
>
> Quand le relais DESCENTE est excité → il alimente la bobine du relais inverseur dans l’autre sens

### Schéma de câblage simplifié (le plus simple qui marche très bien)

On va faire encore plus simple avec seulement 2 relais (c’est suffisant et très répandu pour les stores/volets)

Matériel réduit :

- 1 inverseur à rappel 3 positions (inter store)
- 1 relais DPDT 12 V 10-30A (relais inverseur de sens)
- 1 tout petit relais 12 V 5-10A pour le capteur pluie

Câblage :

> +12V ────────────────────────────────────────┐
>
> │
>
> ├─────► +12V capteur pluie
>
> │
>
> ├─────► broche fixe haut de l’inter store
>
> │
>
> ├─────► broche fixe bas de l’inter store (via une diode* si tu veux être propre)
>
> │
>
> └─────► bobine relais inverseur (pin 86)
>
> GND ────────────────────────────────────────┐
>
> ├─────► GND capteur pluie
>
> └─────► sortie capteur quand il pleut (fil noir) → relié au GND quand il pleut
>
> Inter store (3 positions à rappel) :
>
> - Broche du milieu → +12V
>
> - Broche HAUT → bobine relais « montée » (ou directement pin 85 du relais inverseur)
>
> - Broche BAS → sortie capteur pluie (fil noir) + aussi relié à pin 85 du relais inverseur via une diode (1N4007) pour la commande manuelle descente
>
> Relais inverseur 5 broches (type automobile ou Finder 40.52) :
>
> - 30 → +12V alimentation moteur
>
> - 87 → GND
>
> - 87a → un fil moteur
>
> - 87b → l’autre fil moteur
>
> - 86 → +12V bobine
>
> - 85 → GND bobine (relié à la sortie « commande descente » : inter bas OU capteur pluie)
>
> Quand tu appuies HAUT → +12V sur 86 → moteur tourne dans un sens (sortie)
>
> Quand tu appuies BAS ou quand il pleut → 85 relié au GND → moteur tourne dans l’autre sens (rentrée)

C’est la solution la plus simple et la plus utilisée pour les stores avec capteur pluie.

### Liste finale du matériel à acheter

- 1 interrupteur de volet roulant 3 positions à rappel (réf Legrand 067901 ou équivalent) → ~15-20 €
- 1 relais inverseur 12 V 30 A 5 broches (automobile ou Finder) → ~5-10 €
- 1 diode 1N4007 (optionnelle mais propre) → 0,20 €
- 1 petit porte-fusible + fusible 15-20A
- Du câble et des Wago

Tu mets tout ça dans une petite boîte étanche près de l’alim 12 V.

Si tu veux, je te fais un schéma dessin propre (je peux te le décrire précisément .

Tu me dis si tu veux la version ultra-basique avec 2 relais ou une version un peu plus propre avec 3 relais et diodes anti-retour. Les deux marchent très bien. La plupart des gens font la version ultra-basique et ça tient des années.

---
