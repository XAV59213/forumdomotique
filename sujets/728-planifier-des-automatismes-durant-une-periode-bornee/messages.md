---
title: "Planifier des automatismes durant une période bornée"
---

{% raw %}
# Planifier des automatismes durant une période bornée

- **Catégorie :** [Confort et Ambiance](https://forumdomotique.com/forums/67-confort-et-ambiance/)
- **Sujet :** https://forumdomotique.com/forums/topic/728-planifier-des-automatismes-durant-une-p%C3%A9riode-born%C3%A9e/
- **Auteur du premier message du sujet :** un autre membre (XAV59213 a répondu dans ce sujet)
- **Messages de XAV59213 dans ce sujet :** 2
- **Premier message de XAV59213 :** 31 janvier 2026 à 08:16 (Europe/Paris)
- **Dernier message de XAV59213 :** 31 janvier 2026 à 13:25 (Europe/Paris)

---

## Message 1 — 31 janvier 2026 à 08:16 (Europe/Paris)

- **Identifiant :** `1921`
- **Lien :** https://forumdomotique.com/forums/topic/728-planifier-des-automatismes-durant-une-p%C3%A9riode-born%C3%A9e/#findComment-1921

Salut [@BièreNard](https://forumdomotique.com/profile/8-bi%C3%A8renard/)

on peut réaliser ton scénario avec une automation en YAML (ou via l’interface graphique, mais le YAML est plus précis pour les boucles). Voici comment programmer : tous les soirs, 15 minutes après le coucher du soleil, allumer la lumière toutes les 30 minutes pendant 20 minutes, jusqu’à 23h30.

**Prérequis**

•  Assure-toi que l’intégration “Sun” est activée dans HA (elle l’est par défaut).

•  Remplace light.ta_lumiere par l’ID réel de ton entité lumière (vérifie dans les États des développeurs).

**Automation en YAML**

Ajoute ceci dans ton fichier automations.yaml (ou crée une nouvelle automation via l’interface et édite en YAML) :

```yaml
- id: 'allumer_lumiere_apres_coucher_soleil'
  alias: Allumer lumière après coucher du soleil
  description: Allume la lumière toutes les 30 min pendant 20 min, jusqu'à 23h30
  trigger:
    - platform: sun
      event: sunset
      offset: '+00:15:00'  # 15 minutes après le coucher du soleil
  condition: []  # Pas de conditions supplémentaires ici
  action:
    - repeat:
        while:
          - condition: time
            before: '23:30:00'  # Répète tant que l'heure est avant 23h30
        sequence:
          - service: light.turn_on
            target:
              entity_id: light.ta_lumiere  # Remplace par ton entité
          - delay:
              minutes: 20  # Allumée pendant 20 minutes
          - service: light.turn_off
            target:
              entity_id: light.ta_lumiere
          - delay:
              minutes: 10  # Éteinte pendant 10 minutes (pour un cycle de 30 min total)
  mode: single  # Mode single pour éviter les chevauchements
```

**Explications**

•  **Déclencheur** : Se déclenche 15 minutes après le coucher du soleil (via l’offset positif).

•  **Boucle (repeat while)** : Avant chaque cycle, HA vérifie si l’heure est avant 23h30. Si oui, il exécute le cycle ; sinon, il arrête. Cela évite de démarrer un nouveau cycle après 23h30.

•  **Cycle** : Allume la lumière, attend 20 min, éteint, attend 10 min (ce qui fait un intervalle de 30 min entre allumages).

•  Si le cycle en cours dépasse 23h30 (par exemple, si un allumage commence à 23h25), il se terminera normalement. Pour forcer une extinction pile à 23h30, tu pourrais ajouter une automation séparée avec un déclencheur à heure fixe (platform: time à 23:30) qui éteint la lumière.

Via l’interface graphique de HA

Si tu préfères l’UI :

1. Va dans Paramètres > Automatisations & Scènes > Créer une automation.

2. Ajoute un déclencheur : Type “Soleil”, Événement “Coucher du soleil”, Offset “+00:15:00”.

3. Ajoute une action : Type “Répéter”, Sous-type “Tant que” (while), Condition “Heure” avant 23:30:00.

4. Dans la séquence de la répétition :

• Action “Allumer la lumière” (sélectionne ton entité).

• Action “Attendre” 20 minutes.

• Action “Éteindre la lumière”.

• Action “Attendre” 10 minutes.

5. Enregistre et teste (tu peux simuler le déclencheur via les outils dev).

---

## Message 2 — 31 janvier 2026 à 13:25 (Europe/Paris)

- **Identifiant :** `1935`
- **Lien :** https://forumdomotique.com/forums/topic/728-planifier-des-automatismes-durant-une-p%C3%A9riode-born%C3%A9e/#findComment-1935

salut [@BièreNard](https://forumdomotique.com/profile/8-bi%C3%A8renard/) ,

Super, content que ça t'ait aidé à découvrir les blocs de contrôle (repeat, while, choose, etc.) dans l'interface de Home Assistant.

c'est effectivement très puissant une fois qu'on maîtrise un peu le YAML ou les blocs correspondants !

Pour ton **PS** sur la **durée aléatoire** (random duration) dans la séquence, c'est une demande très courante (simulation de présence, variation naturelle, etc.).

Voici comment l'intégrer facilement dans ton scénario existant.

### Option la plus simple et recommandée (YAML templaté)

Remplace ton délai fixe par un délai **aléatoire** avec le filtre Jinja2 random intégré à HA :

Dans la boucle repeat, modifie les deux delay comme suit :

```yaml
action:
  - repeat:
      while:
        - condition: time
          before: '23:30:00'
      sequence:
        - service: light.turn_on
          target:
            entity_id: light.ta_lumiere
        - delay:
            minutes: "{{ range(15, 26) | random }}"   # durée ON aléatoire entre 15 et 25 min (exemple)
        - service: light.turn_off
          target:
            entity_id: light.ta_lumiere
        - delay:
            minutes: "{{ range(5, 16) | random }}"    # durée OFF aléatoire entre 5 et 15 min (exemple)
```

1. range(a, b) | random choisit un entier aléatoire de **a inclus** à **b-1 inclus** (donc pour 15–25 min → range(15, 26)).
2. Tu peux aussi mixer minutes et secondes pour plus de finesse :

```yaml
- delay:
    minutes: "{{ range(15, 21) | random }}"
    seconds: "{{ range(0, 60) | random }}"   # variation de 0–59 s en plus
```

- L'aléatoire est recalculé **à chaque itération** de la boucle → chaque cycle aura une durée différente.

### Via l'interface graphique (UI)

1. Quand tu ajoutes ou édites un bloc « Attendre » (delay),
2. Passe en mode YAML pour ce bloc uniquement (clique sur les 3 points > Éditer en YAML),
3. Mets par exemple :

```yaml
minutes: "{{ range(10, 31) | random }}"
```

ou

```yaml
seconds: "{{ range(300, 1201) | random }}"   # 5 à 20 minutes en secondes
```

1. Valide → ça reste compatible UI, même si le délai est templaté.

### Variantes avancées si besoin

- **Durée ON fixe mais départ aléatoire** : ajoute un premier delay aléatoire juste après le trigger (avant la boucle).

```yaml
action:
  - delay:
      minutes: "{{ range(0, 16) | random }}"   # décalage initial 0–15 min
  - repeat: ...
```

1. **Aléatoire plus fin ou avec seed** : le random de base est suffisant pour la plupart des usages. Si tu veux vraiment du « vrai » random (pas reproductible),

   c'est déjà le cas ici.
2. **Éviter les dépassements à 23h30** : ton while before: '23:30:00' est déjà très bien. Si un cycle long commence juste avant, il finira naturellement (comme tu l'as noté). Pour forcer l'extinction à 23h30 pile :

- Crée une automation séparée :

```yaml
trigger:
  - platform: time
    at: '23:30:00'
action:
  - service: light.turn_off
    target:
      entity_id: light.ta_lumiere
```

Teste avec des valeurs courtes (ex. range(1,6) pour 1–5 min) comme tu l'as fait pour valider une fois OK, remets tes plages réelles.

Si tu veux poster ton exemple finalisé dans ton nouveau fil (avec la durée aléatoire), n'hésite pas à partager le YAML ou une capture, ça aidera sûrement d'autres membres !

Bonne continuation avec tes automatisations 😊

---
{% endraw %}
