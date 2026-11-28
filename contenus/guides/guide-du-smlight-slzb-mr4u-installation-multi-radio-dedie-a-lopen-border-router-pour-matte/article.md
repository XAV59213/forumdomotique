---
title: "Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread"
description: "Ces dernières semaines, j’ai beaucoup réfléchi à la façon d’intégrer plus sereinement des appareils Matter over Thread dans mon installation domotique…"
image: /contenus/guides/guide-du-smlight-slzb-mr4u-installation-multi-radio-dedie-a-lopen-border-router-pour-matte/images/guide-slzb-mr4u-couverture.jpg
date: 2025-12-17
section: guides
tags:
  - domotique
  - zigbee
  - matter
audience_key: guide-slzb-mr4u
pdf: /contenus/guides/guide-du-smlight-slzb-mr4u-installation-multi-radio-dedie-a-lopen-border-router-pour-matte/guide-du-smlight-slzb-mr4u-installation-multi-radio-dedie-a-lopen-border-router-pour-matte.pdf
---
<p class="forum-cta"><a href="https://forumdomotique.com/guides-tutoriels/home-assistant/guide-du-smlight-slzb-mr4u-installation-multi-radio-d%C3%A9di%C3%A9-%C3%A0-lopen-border-router-pour-matter-over-thread-r11/">Lire et commenter sur Forum Domotique</a></p>


<section class="carousel photo-carousel" data-carousel data-lightbox aria-roledescription="carrousel" aria-label="Photos de l’article (16)" tabindex="0">
<div class="carousel-track" data-track>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1411-57-15.png" data-full="images/Capturedcrandu2025-12-1411-57-15.png" data-alt="Photo 1 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 1 : Photo 1 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1411-57-15-591.webp 591w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1411-57-15-591.jpg" srcset="images/affichage/Capturedcrandu2025-12-1411-57-15-591.jpg 591w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 1 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="591" height="478" loading="eager" decoding="async" fetchpriority="high">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1410-54-55.png" data-full="images/Capturedcrandu2025-12-1410-54-55.png" data-alt="Photo 2 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 2 : Photo 2 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1410-54-55-640.webp 640w, images/affichage/Capturedcrandu2025-12-1410-54-55-922.webp 922w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1410-54-55-922.jpg" srcset="images/affichage/Capturedcrandu2025-12-1410-54-55-640.jpg 640w, images/affichage/Capturedcrandu2025-12-1410-54-55-922.jpg 922w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 2 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="922" height="399" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1410-52-29.png" data-full="images/Capturedcrandu2025-12-1410-52-29.png" data-alt="Photo 3 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 3 : Photo 3 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1410-52-29-640.webp 640w, images/affichage/Capturedcrandu2025-12-1410-52-29-723.webp 723w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1410-52-29-723.jpg" srcset="images/affichage/Capturedcrandu2025-12-1410-52-29-640.jpg 640w, images/affichage/Capturedcrandu2025-12-1410-52-29-723.jpg 723w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 3 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="723" height="679" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1310-17-35.png" data-full="images/Capturedcrandu2025-12-1310-17-35.png" data-alt="Photo 4 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 4 : Photo 4 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1310-17-35-640.webp 640w, images/affichage/Capturedcrandu2025-12-1310-17-35-1200.webp 1200w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1310-17-35-1200.jpg" srcset="images/affichage/Capturedcrandu2025-12-1310-17-35-640.jpg 640w, images/affichage/Capturedcrandu2025-12-1310-17-35-1200.jpg 1200w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 4 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="1200" height="159" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1411-00-06.png" data-full="images/Capturedcrandu2025-12-1411-00-06.png" data-alt="Photo 5 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 5 : Photo 5 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1411-00-06-640.webp 640w, images/affichage/Capturedcrandu2025-12-1411-00-06-760.webp 760w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1411-00-06-760.jpg" srcset="images/affichage/Capturedcrandu2025-12-1411-00-06-640.jpg 640w, images/affichage/Capturedcrandu2025-12-1411-00-06-760.jpg 760w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 5 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="760" height="867" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1411-06-01.png" data-full="images/Capturedcrandu2025-12-1411-06-01.png" data-alt="Photo 6 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 6 : Photo 6 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1411-06-01-640.webp 640w, images/affichage/Capturedcrandu2025-12-1411-06-01-740.webp 740w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1411-06-01-740.jpg" srcset="images/affichage/Capturedcrandu2025-12-1411-06-01-640.jpg 640w, images/affichage/Capturedcrandu2025-12-1411-06-01-740.jpg 740w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 6 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="740" height="541" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1310-24-18.png" data-full="images/Capturedcrandu2025-12-1310-24-18.png" data-alt="Photo 7 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 7 : Photo 7 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1310-24-18-460.webp 460w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1310-24-18-460.jpg" srcset="images/affichage/Capturedcrandu2025-12-1310-24-18-460.jpg 460w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 7 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="460" height="814" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1411-01-50.png" data-full="images/Capturedcrandu2025-12-1411-01-50.png" data-alt="Photo 8 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 8 : Photo 8 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1411-01-50-608.webp 608w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1411-01-50-608.jpg" srcset="images/affichage/Capturedcrandu2025-12-1411-01-50-608.jpg 608w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 8 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="608" height="648" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-1411-02-40.png" data-full="images/Capturedcrandu2025-12-1411-02-40.png" data-alt="Photo 9 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 9 : Photo 9 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-1411-02-40-541.webp 541w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-1411-02-40-541.jpg" srcset="images/affichage/Capturedcrandu2025-12-1411-02-40-541.jpg 541w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 9 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="541" height="602" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-2314-55-49.png" data-full="images/Capturedcrandu2025-12-2314-55-49.png" data-alt="Photo 10 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 10 : Photo 10 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-2314-55-49-640.webp 640w, images/affichage/Capturedcrandu2025-12-2314-55-49-914.webp 914w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-2314-55-49-914.jpg" srcset="images/affichage/Capturedcrandu2025-12-2314-55-49-640.jpg 640w, images/affichage/Capturedcrandu2025-12-2314-55-49-914.jpg 914w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 10 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="914" height="749" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-2314-52-51.png" data-full="images/Capturedcrandu2025-12-2314-52-51.png" data-alt="Photo 11 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 11 : Photo 11 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-2314-52-51-640.webp 640w, images/affichage/Capturedcrandu2025-12-2314-52-51-838.webp 838w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-2314-52-51-838.jpg" srcset="images/affichage/Capturedcrandu2025-12-2314-52-51-640.jpg 640w, images/affichage/Capturedcrandu2025-12-2314-52-51-838.jpg 838w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 11 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="838" height="509" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-2314-59-51.png" data-full="images/Capturedcrandu2025-12-2314-59-51.png" data-alt="Photo 12 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 12 : Photo 12 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-2314-59-51-640.webp 640w, images/affichage/Capturedcrandu2025-12-2314-59-51-914.webp 914w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-2314-59-51-914.jpg" srcset="images/affichage/Capturedcrandu2025-12-2314-59-51-640.jpg 640w, images/affichage/Capturedcrandu2025-12-2314-59-51-914.jpg 914w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 12 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="914" height="749" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-2317-30-06.png" data-full="images/Capturedcrandu2025-12-2317-30-06.png" data-alt="Photo 13 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 13 : Photo 13 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-2317-30-06-640.webp 640w, images/affichage/Capturedcrandu2025-12-2317-30-06-919.webp 919w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-2317-30-06-919.jpg" srcset="images/affichage/Capturedcrandu2025-12-2317-30-06-640.jpg 640w, images/affichage/Capturedcrandu2025-12-2317-30-06-919.jpg 919w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 13 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="919" height="853" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-2317-30-43.png" data-full="images/Capturedcrandu2025-12-2317-30-43.png" data-alt="Photo 14 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 14 : Photo 14 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-2317-30-43-640.webp 640w, images/affichage/Capturedcrandu2025-12-2317-30-43-974.webp 974w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-2317-30-43-974.jpg" srcset="images/affichage/Capturedcrandu2025-12-2317-30-43-640.jpg 640w, images/affichage/Capturedcrandu2025-12-2317-30-43-974.jpg 974w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 14 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="974" height="486" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-2317-30-57.png" data-full="images/Capturedcrandu2025-12-2317-30-57.png" data-alt="Photo 15 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 15 : Photo 15 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-2317-30-57-640.webp 640w, images/affichage/Capturedcrandu2025-12-2317-30-57-963.webp 963w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-2317-30-57-963.jpg" srcset="images/affichage/Capturedcrandu2025-12-2317-30-57-640.jpg 640w, images/affichage/Capturedcrandu2025-12-2317-30-57-963.jpg 963w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 15 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="963" height="652" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
<figure class="photo-slide" data-slide>
  <a href="images/Capturedcrandu2025-12-2317-48-03.png" data-full="images/Capturedcrandu2025-12-2317-48-03.png" data-alt="Photo 16 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" aria-label="Agrandir la photo 16 : Photo 16 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread">
    <picture>
  <source type="image/webp" srcset="images/affichage/Capturedcrandu2025-12-2317-48-03-640.webp 640w, images/affichage/Capturedcrandu2025-12-2317-48-03-913.webp 913w" sizes="(max-width: 42em) 92vw, 800px">
  <img src="images/affichage/Capturedcrandu2025-12-2317-48-03-913.jpg" srcset="images/affichage/Capturedcrandu2025-12-2317-48-03-640.jpg 640w, images/affichage/Capturedcrandu2025-12-2317-48-03-913.jpg 913w" sizes="(max-width: 42em) 92vw, 800px" alt="Photo 16 — Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread" width="913" height="751" loading="lazy" decoding="async">
</picture>
  </a>
</figure>
</div>
<button type="button" class="carousel-nav" data-prev aria-label="Photo précédente">‹</button>
<button type="button" class="carousel-nav" data-next aria-label="Photo suivante">›</button>
<div class="carousel-dots" data-dots></div>
<div class="carousel-live" data-live aria-live="polite"></div>
<p class="carousel-hint">Faites défiler les photos, ou ouvrez-les pour les agrandir (si JavaScript est activé).</p>
</section>

# Guide du SMLight SLZB-MR4U : Installation multi-radio dédié à l’Open Border Router pour Matter over Thread

- **Type :** Guide
- **Catégorie :** Guides & tutoriels domotique > Home Assistant
- **Lien :** https://forumdomotique.com/guides-tutoriels/home-assistant/guide-du-smlight-slzb-mr4u-installation-multi-radio-d%C3%A9di%C3%A9-%C3%A0-lopen-border-router-pour-matter-over-thread-r11/
- **Date de publication :** 17 décembre 2025 à 13:16 (Europe/Paris)
- **Auteur :** XAV59213

---

Ces dernières semaines, j’ai beaucoup réfléchi à la façon d’intégrer plus sereinement des appareils Matter over Thread dans mon installation domotique.

Avec l’arrivée progressive de nouveaux capteurs et interrupteurs compatibles Thread, je sentais que mon ancien setup Z2mqtt commençait à montrer ses limites pour accueillir cette nouvelle génération de devices. J’avais déjà exploré Zigbee2MQTT avec des modules SMLight par le passé, mais cette fois, mon intérêt s’est porté spécifiquement sur la partie Thread et Matter.

Quand j’ai découvert le **SLZB-MR4U**, une version évoluée de la série multi-radio de SMLight, l’idée d’avoir un coordinateur capable de gérer un réseau Thread de manière dédiée, tout en gardant une radio Zigbee puissante, m’a vraiment séduit.

![Capture d’écran du 2025-12-14 11-57-15.png](images/Capturedcrandu2025-12-1411-57-15.png)

Je voulais un dispositif que je puisse placer au centre de la maison, alimenté en PoE pour oublier les contraintes d’alimentation, et configuré comme Open Border Router pour que Home Assistant prenne la main sur le réseau Matter. C’est exactement ce que promet ce module, et après plusieurs semaines d’utilisation intensive, je peux dire qu’il tient largement ses promesses sur cet aspect.

![Capture d’écran du 2025-12-14 10-54-55.png](images/Capturedcrandu2025-12-1410-54-55.png)

L’installation physique est un jeu d’enfant. J’ai branché un câble Ethernet PoE directement depuis mon switch, et le module s’est alimenté instantanément. Pas besoin de bloc secteur encombrant, ce qui est un vrai plus quand on veut le placer dans les combles ou au centre de la maison. Une fois connecté au réseau, l’adresse IP apparaît facilement via le routeur ou en scannant le réseau local. L’interface web SLZB-OS est accessible en quelques clics, et c’est là que tout se joue pour la configuration. Pour mon usage centré sur l’Open Border Router, j’ai d’abord mis à jour le firmware SLZB-OS vers la dernière version stable, puis j’ai configuré la radio Texas Instruments CC2674P10 (Radio 2) en mode Matter over Thread en flashant le firmware RCP dédié. L’autre radio, la Silicon Labs EFR32MG26 (Radio 1), je l’ai mise en coordinateur Zigbee pour en profiter en parallèle lors de tests secondaires, mais l’intérêt principal restait Thread. Certaines versions précoces demandaient un reflash manuel pour stabiliser le mode OTBR, mais avec les firmwares récents, tout est fluide. Une fois cela fait, le module expose un port spinel accessible via l’IP du dispositif, généralement sur le port 6638 ou 7638 (similaire selon la radio choisie).

![Capture d’écran du 2025-12-14 10-52-29.png](images/Capturedcrandu2025-12-1410-52-29.png)

La mise en route dans Home Assistant suit une procédure maintenant bien rodée, mais qui demande un peu d’attention pour éviter les pièges classiques. J’ai installé l’add-on **OpenThread Border Router** depuis le magasin d’add-ons,en veillant à activer les options avancées dans les paramètres pour débloquer le champ Network Device.

![Capture d’écran du 2025-12-13 10-17-35.png](images/Capturedcrandu2025-12-1310-17-35.png)

![Capture d’écran du 2025-12-14 11-00-06.png](images/Capturedcrandu2025-12-1411-00-06.png)

![Capture d’écran du 2025-12-14 11-06-01.png](images/Capturedcrandu2025-12-1411-06-01.png)

Ensuite, il suffit d’entrer l’adresse du module au format ip:port, sans http ni rien d’autre. Le démarrage peut prendre un moment la première fois, le temps que le backbone Thread se forme. J’ai rencontré un petit accroc au début avec des timeouts spinel dans les logs, mais un simple reflash de la puce EFR32 via l’interface web a tout résolu, et depuis, c’est d’une stabilité exemplaire.

![Capture d’écran du 2025-12-13 10-24-18.png](images/Capturedcrandu2025-12-1310-24-18.png)

Une fois l’add-on lancé, j’ajoute l’intégration Matter dans Home Assistant, puis l’intégration Open Thread Border Router, et le réseau Thread est prêt.

Home Assistant devient alors le commissioner Matter, ce qui simplifie énormément l’appairage des nouveaux appareils.

![Capture d’écran du 2025-12-14 11-01-50.png](images/Capturedcrandu2025-12-1411-01-50.png)![Capture d’écran du 2025-12-14 11-02-40.png](images/Capturedcrandu2025-12-1411-02-40.png)

L’intégration dans Home Assistant est particulièrement fluide quand on se concentre sur le rôle d’Open Border Router. L’add-on OTBR communique directement avec la radio réseau du **SLZB-MR4U**, et une fois configuré, tout apparaît automatiquement. Les appareils Thread rejoignent le réseau sans intervention manuelle compliquée, et Home Assistant gère le commissioning Matter de façon transparente. Ce qui simplifie vraiment la vie, c’est de ne plus dépendre d’un hub propriétaire pour les devices Matter : tout passe par HA, avec les automatisations habituelles.

En activant la seconde radio pour quelques tests, le module tient la charge sans broncher. À éviter peut-être les firmwares trop expérimentaux au début, mieux vaut partir sur des versions stables pour la puce EFR32MG26.

Ce qui ressort le plus après cette utilisation, c’est la flexibilité offerte par cette double radio dédiée et la connectivité PoE qui permet un placement optimal. La portée et la stabilité en mode Open Border Router sont excellentes, et le fait de pouvoir centraliser Zigbee et Thread dans un seul boîtier sans compromis rend l’installation plus propre. Côté améliorations, j’aurais aimé une documentation encore plus détaillée sur les spécificités de la version U, comme le passthrough USB qui peut être utile pour des setups hybrides, même si je ne l’ai pas exploité ici. Quelques utilisateurs ont signalé des besoins de reflash initial pour stabiliser Thread, mais avec les mises à jour récentes, cela semble résolu. Globalement, c’est un module qui gagne en maturité rapidement grâce au support actif de SMLight.

Après ces semaines de test centrées sur la configuration Open Border Router, je garde sans hésiter le **SLZB-MR4U** dans mon installation principale. Il répond parfaitement à ceux qui veulent un réseau Matter over Thread robuste et intégré nativement à Home Assistant, tout en conservant la possibilité d’un Zigbee puissant en parallèle. Si vous avez déjà une base Zigbee solide et que vous envisagez d’ajouter des appareils Thread sans multiplier les dongles, ce module est une solution crédible et durable. Il simplifie la transition vers Matter sans sacrifier la fiabilité, et c’est exactement ce que je cherchais.

