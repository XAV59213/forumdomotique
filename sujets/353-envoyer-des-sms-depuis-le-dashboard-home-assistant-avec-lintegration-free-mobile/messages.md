---
title: "Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)"
description: "Mettre un formulaire simple sur Lovelace pour choisir un destinataire (Papa, Maman, …) avoir une confirmation d’envoi et vider le champ Optionnel…"
image: /sujets/353-envoyer-des-sms-depuis-le-dashboard-home-assistant-avec-lintegration-free-mobile/images/og-partage.jpg
date: 2025-08-24
github_repo: freesmsxa
---
{% raw %}
<p class="forum-cta"><a href="https://forumdomotique.com/forums/topic/353-envoyer-des-sms-depuis-le-dashboard-home-assistant-avec-lint%C3%A9gration-free-mobile-sms-xa/">Lire et commenter sur Forum Domotique</a> · <a href="https://github.com/XAV59213/freesmsxa">Dépôt HACS : Free Mobile SMS XA</a></p>


<section class="carousel photo-carousel" data-carousel data-lightbox aria-roledescription="carrousel" aria-label="Photos de l’article (8)" tabindex="0">
<div class="carousel-track" data-track>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-08-2416-46-25.png" data-full="images/Capturedcrandu2025-08-2416-46-25.png" data-alt="Photo 1 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" aria-label="Agrandir la photo 1 : Photo 1 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)">
    <img src="images/Capturedcrandu2025-08-2416-46-25.png" alt="Photo 1 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" loading="eager">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-08-2416-46-17.png" data-full="images/Capturedcrandu2025-08-2416-46-17.png" data-alt="Photo 2 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" aria-label="Agrandir la photo 2 : Photo 2 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)">
    <img src="images/Capturedcrandu2025-08-2416-46-17.png" alt="Photo 2 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-08-2416-50-55.png" data-full="images/Capturedcrandu2025-08-2416-50-55.png" data-alt="Photo 3 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" aria-label="Agrandir la photo 3 : Photo 3 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)">
    <img src="images/Capturedcrandu2025-08-2416-50-55.png" alt="Photo 3 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-08-2417-14-50.png" data-full="images/Capturedcrandu2025-08-2417-14-50.png" data-alt="Photo 4 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" aria-label="Agrandir la photo 4 : Photo 4 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)">
    <img src="images/Capturedcrandu2025-08-2417-14-50.png" alt="Photo 4 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-08-2417-02-55.png" data-full="images/Capturedcrandu2025-08-2417-02-55.png" data-alt="Photo 5 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" aria-label="Agrandir la photo 5 : Photo 5 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)">
    <img src="images/Capturedcrandu2025-08-2417-02-55.png" alt="Photo 5 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-08-2417-05-19.png" data-full="images/Capturedcrandu2025-08-2417-05-19.png" data-alt="Photo 6 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" aria-label="Agrandir la photo 6 : Photo 6 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)">
    <img src="images/Capturedcrandu2025-08-2417-05-19.png" alt="Photo 6 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-08-2417-25-44.png" data-full="images/Capturedcrandu2025-08-2417-25-44.png" data-alt="Photo 7 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" aria-label="Agrandir la photo 7 : Photo 7 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)">
    <img src="images/Capturedcrandu2025-08-2417-25-44.png" alt="Photo 7 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" loading="lazy">
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-08-2417-25-16.png" data-full="images/Capturedcrandu2025-08-2417-25-16.png" data-alt="Photo 8 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" aria-label="Agrandir la photo 8 : Photo 8 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)">
    <img src="images/Capturedcrandu2025-08-2417-25-16.png" alt="Photo 8 — Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)" loading="lazy">
  </a>
</figure>
</div>
<button type="button" class="carousel-nav" data-prev aria-label="Photo précédente">‹</button>
<button type="button" class="carousel-nav" data-next aria-label="Photo suivante">›</button>
<div class="carousel-dots" data-dots></div>
<div class="carousel-live" data-live aria-live="polite"></div>
<p class="carousel-hint">Faites défiler les photos, ou ouvrez-les pour les agrandir (si JavaScript est activé).</p>
</section>

# Envoyer des SMS depuis le dashboard Home Assistant (avec l’intégration Free Mobile SMS XA)

> **Important** : ce guide fonctionne **uniquement** avec l’intégration personnalisée **Free Mobile SMS XA** développée ici : `https://github.com/XAV59213/freesmsxa`  
> Elle expose des services `notify.*` et un service `freesmsxa.send_sms` pour envoyer des SMS via l’API Free Mobile.

---

## 🎯 Objectif

Mettre un **formulaire simple** sur Lovelace pour :

- choisir un destinataire (Papa, Maman, …),
- saisir un message,
- cliquer sur **Envoyer**,
- avoir une **confirmation** d’envoi et **vider le champ**.

![Capture d’écran du 2025-08-24 16-46-25.png](images/Capturedcrandu2025-08-2416-46-25.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_08/Capturedcrandu2025-08-2416-46-25.png.2016a8e76f81ee3859362237961b2373.png -->

![Capture d’écran du 2025-08-24 16-46-17.png](images/Capturedcrandu2025-08-2416-46-17.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_08/Capturedcrandu2025-08-2416-46-17.png.caa0cbefa8ebc9d1f8272478d6a9f01e.png -->

Optionnel : afficher l’**état** et l’**historique** des SMS grâce au capteur créé par l’intégration.

![Capture d’écran du 2025-08-24 16-50-55.png](images/Capturedcrandu2025-08-2416-50-55.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_08/Capturedcrandu2025-08-2416-50-55.png.8c1f89f93957378bc7a0f7b5aa5949f5.png -->

![Capture d’écran du 2025-08-24 17-14-50.png](images/Capturedcrandu2025-08-2417-14-50.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_08/Capturedcrandu2025-08-2417-14-50.png.01f3385cbefb684c16a0a66af7c1a3e0.png -->

---

## ✅ Prérequis

1. Avoir un ou plusieurs comptes Free Mobile avec l’option **“Notifications par SMS”** activée (identifiant + clé API).
2. Installer l’intégration personnalisée **Free Mobile SMS XA** :

   - via HACS → Dépôts personnalisés → `https://github.com/XAV59213/freesmsxa` → catégorie *Intégration* ;
   - redémarrer HA ;
   - **Paramètres → Appareils & services → Ajouter une intégration → Free Mobile SMS XA** ;
   - saisir `username` + `access_token` ; un SMS de test valide les identifiants.
3. Vérifier que des services `notify.*` ont été créés (ex. `notify.papa_sms`, `notify.maman_sms`) dans **Outils de développement → Services**.

> Si vous ne voyez pas vos `notify.*`, c’est que l’intégration n’est pas encore configurée ou a échoué.

---

## 🧱 Étape 1 — Créer 2 Entrées

**Paramètres → Appareils & services → Entrée → + Créer Entrée**

- **1 Liste (input_select)**

  - Nom : `Destinataire App` (ou `Destinataire SMS`)

    - Options (une par ligne) : **sans** le `notify.`

      ```plaintext
      papa
      maman
      ect..
      ```

  → entité : `input_select.destinataire_app`

  ![Capture d’écran du 2025-08-24 17-02-55.png](images/Capturedcrandu2025-08-2417-02-55.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_08/Capturedcrandu2025-08-2417-02-55.png.9cf8c7f736e0e02f6609900e75e5fd77.png -->
- **2 Texte (input_text)**

  - Nom : `Message SMS`
  - (facultatif) Longueur max : 160  
    → entité : `input_text.message_sms`

  ![Capture d’écran du 2025-08-24 17-05-19.png](images/Capturedcrandu2025-08-2417-05-19.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_08/Capturedcrandu2025-08-2417-05-19.png.29e75c7b18488e80ce06a6fa7c22964b.png -->

  ---

  ## 🧠 Étape 2 — Le script d’envoi

  Le script ci-dessous :

  - choisit le bon service `notify.<sélection>`,
  - **annule** si le message est vide,
  - crée une **notification de succès**,
  - **efface le message** après envoi.

  **Automatisations & scènes → Scripts → Nouveau → Éditeur YAML :**

```yaml
alias: Envoyer message ciblé (App mobile)
mode: restart
sequence:
  - variables:
      dest: "{{ states('input_select.destinataire_app') }}"
      msg: "{{ states('input_text.message_sms') }}"
  - choose:
      - conditions:
          - condition: template
            value_template: "{{ msg | trim == '' }}"
        sequence:
          - data:
              title: Envoi annulé
              message: Aucun message à envoyer. Merci de saisir un texte.
            action: persistent_notification.create
          - stop: Message vide
  - choose:
      - conditions:
          - condition: template
            value_template: "{{ dest == 'Maman' }}"
        sequence:
          - target:
              entity_id: notify.maman
            data:
              message: "{{ msg }}"
            action: notify.send_message
      - conditions:
          - condition: template
            value_template: "{{ dest == 'Papa' }}"
        sequence:
          - target:
              entity_id: notify.papa
            data:
              message: "{{ msg }}"
            action: notify.send_message
      - conditions:
          - condition: template
            value_template: "{{ dest == 'Naomie' }}"
        sequence:
          - target:
              entity_id: notify.naomie
            data:
              message: "{{ msg }}"
            action: notify.send_message
      - conditions:
          - condition: template
            value_template: "{{ dest == 'Xavier' }}"
        sequence:
          - target:
              entity_id: notify.xavier
            data:
              message: "{{ msg }}"
            action: notify.send_message
      - conditions:
          - condition: template
            value_template: "{{ dest == 'Anais' }}"
        sequence:
          - target:
              entity_id:
                - notify.anais
            data:
              message: "{{ msg }}"
            action: notify.send_message
      - conditions:
          - condition: template
            value_template: "{{ dest == 'TOUS LE MONDE !' }}"
        sequence:
          - target:
              entity_id:
                - notify.maman
                - notify.papa
                - notify.xavier
                - notify.naomie
                - notify.anais
            data:
              message: "{{ msg }}"
            action: notify.send_message
    default:
      - data:
          title: Envoi annulé
          message: Destinataire « {{ dest }} » inconnu. Vérifie ton sélecteur.
        action: persistent_notification.create
      - stop: Destinataire inconnu
  - data:
      title: Message envoyé 
      message: "Envoyé à « {{ dest }} » : {{ msg }}"
    action: persistent_notification.create
  - target:
      entity_id: input_text.message_sms
    data:
      value: ""
    action: input_text.set_value
description: ""
```

Variante si vous préférez **utiliser explicitement** le service de l’intégration :  
remplacez l’étape 2 par :

```yaml
- service: freesmsxa.send_sms
  data:
    target: "notify.{{ dest }}"
    message: "{{ msg }}"
```

## 🧩 Étape 3 — La carte Lovelace (dashboard)

**Tableau de bord → Modifier → + Ajouter une carte → Carte YAML :**

```yaml
type: vertical-stack
cards:
  - type: entities
    title: Envoyer un message SMS
    state_color: true
    entities:
      - entity: input_select.destinataire_app
        name: Destinataire
      - entity: input_text.message_sms
        name: Message

  - type: button
    name: Envoyer
    icon: mdi:send
    tap_action:
      action: call-service
      service: script.turn_on
      target:
        entity_id: script.envoyer_message_cible_app_mobile  # <-- adapte avec l'ID exact de ton script
```

![Capture d’écran du 2025-08-24 17-25-44.png](images/Capturedcrandu2025-08-2417-25-44.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_08/Capturedcrandu2025-08-2417-25-44.png.cd0e7eba87980105b9217da337ef48bd.png -->

![Capture d’écran du 2025-08-24 17-25-16.png](images/Capturedcrandu2025-08-2417-25-16.png)
<!-- source : https://cdn.forumdomotique.com/monthly_2025_08/Capturedcrandu2025-08-2417-25-16.png.57b341091d97a45b3a7aef330b992281.png -->

> Pour connaître l’ID exact du script : **Outils de développement → États**, filtre `script.`.

---

## 🔎 (Optionnel) Carte “État + Historique des SMS”

Si vous avez configuré le **capteur** créé par l’intégration (nom ressemblant à `<Alias> - SMS`), vous pouvez afficher :

- le **compteur** d’envois,
- le **dernier envoi**,
- l’**historique** (10 derniers) depuis l’attribut `sms_log`.

Adaptez `sensor.TON_CAPTEUR` à votre entité réelle (voir **États**).

```yaml
type: vertical-stack
cards:
  - type: entity
    entity: sensor.TON_CAPTEUR
    name:  Maman SMS - État
    state_color: true
    unit: sms
    attribute: sms_count

  - type: markdown
    title:  Historique des derniers SMS
    content: >
      {% set log = state_attr('sensor.TON_CAPTEUR', 'sms_log') %}
      {% if log %}
      {% for item in log %}
      • **{{ item['time'] | as_datetime | as_local | strftime('%d/%m %H:%M:%S') }}** : {{ item['message'] }}
      {% endfor %}
      {% else %}
      Aucun SMS envoyé.
      {% endif %}
```

## 🧰 Dépannage (FAQ)

- **“Notify service not found”**  
  → Dans **Outils de développement → Services**, notez les noms exacts `notify.*`.  
  → Les **options** de `input_select.destinataire_app` doivent être **sans** `notify.` (ex. `papa_sms`, pas `notify.papa_sms`).  
  → Le script reconstruit `notify.{{ dest }}`.
- **Rien ne se passe en cliquant sur “Envoyer”**  
  → Vérifiez que la carte appelle bien `script.turn_on` et l’`entity_id` du script est correct (voir **États**).
- **Le champ ne se vide pas**  
  → Vérifiez que `input_text.message_sms` existe, et l’étape `input_text.set_value` est bien en fin de script.
- **Pas de capteur / pas d’historique**  
  → Ajoutez l’intégration et la ligne Free Mobile ; le capteur est créé par l’intégration lors de la config.  
  → L’historique s’alimente après vos premiers envois.

---

## 🔐 Remarques sécurité & vie privée

- Les clés Free Mobile sont **stockées dans la config** de l’intégration et ne s’affichent pas en clair dans le device registry.
- Pensez à **limiter l’accès** à cette carte Lovelace (utilisateurs/onglets) si nécessaire.

---

## 📦 Références

- Intégration **Free Mobile SMS XA** (obligatoire) : `https://github.com/XAV59213/freesmsxa`
- Home Assistant — Helpers (Aides), Scripts, Lovelace.

---

## 🏁 Conclusion

En quelques minutes, vous avez :

- un formulaire **Destinataire + Message + Bouton Envoyer**,
- un envoi **100 % SMS** via l’intégration **Free Mobile SMS XA**,
- une **confirmation** d’envoi et un champ **réinitialisé**,
- et, si vous voulez, un **suivi de l’historique** des SMS.

{% endraw %}
