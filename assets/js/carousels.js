(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function slidesOf(track) {
    return Array.prototype.slice.call(track.querySelectorAll("[data-slide]"));
  }

  function closestIndex(track) {
    var slides = slidesOf(track);
    var left = track.scrollLeft;
    var best = 0;
    var bestDist = Infinity;
    for (var i = 0; i < slides.length; i++) {
      var d = Math.abs(slides[i].offsetLeft - left);
      if (d < bestDist) {
        bestDist = d;
        best = i;
      }
    }
    return best;
  }

  function goTo(track, index) {
    var slides = slidesOf(track);
    if (!slides.length) return;
    var i = ((index % slides.length) + slides.length) % slides.length;
    var behavior = reduceMotion ? "auto" : "smooth";
    track.scrollTo({ left: slides[i].offsetLeft, behavior: behavior });
  }

  function enhance(root) {
    var track = root.querySelector("[data-track]");
    if (!track) return;
    var slides = slidesOf(track);
    if (slides.length < 2) return;

    root.classList.add("is-enhanced");
    var prev = root.querySelector("[data-prev]");
    var next = root.querySelector("[data-next]");
    var dotsWrap = root.querySelector("[data-dots]");
    var live = root.querySelector("[data-live]");
    var autoplayMs = parseInt(root.getAttribute("data-autoplay") || "0", 10);
    if (reduceMotion) autoplayMs = 0;

    var dots = [];
    if (dotsWrap) {
      dotsWrap.innerHTML = "";
      slides.forEach(function (_, i) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "carousel-dot";
        b.setAttribute(
          "aria-label",
          "Aller à l’élément " + (i + 1) + " sur " + slides.length
        );
        b.addEventListener("click", function () {
          goTo(track, i);
          restartAuto();
        });
        dotsWrap.appendChild(b);
        dots.push(b);
      });
    }

    function sync() {
      var i = closestIndex(track);
      slides.forEach(function (s, n) {
        if (n === i) s.removeAttribute("aria-hidden");
        else s.setAttribute("aria-hidden", "true");
      });
      dots.forEach(function (d, n) {
        if (n === i) d.setAttribute("aria-current", "true");
        else d.removeAttribute("aria-current");
      });
      if (live) live.textContent = i + 1 + " / " + slides.length;
    }

    var timer = null;
    function stopAuto() {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
    }
    function startAuto() {
      stopAuto();
      if (!autoplayMs) return;
      timer = setInterval(function () {
        if (document.hidden) return;
        goTo(track, closestIndex(track) + 1);
      }, autoplayMs);
    }
    function restartAuto() {
      stopAuto();
      startAuto();
    }

    if (prev) {
      prev.addEventListener("click", function () {
        goTo(track, closestIndex(track) - 1);
        restartAuto();
      });
    }
    if (next) {
      next.addEventListener("click", function () {
        goTo(track, closestIndex(track) + 1);
        restartAuto();
      });
    }

    var raf = null;
    track.addEventListener(
      "scroll",
      function () {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          raf = null;
          sync();
        });
      },
      { passive: true }
    );

    root.addEventListener("mouseenter", stopAuto);
    root.addEventListener("mouseleave", startAuto);
    root.addEventListener("focusin", stopAuto);
    root.addEventListener("focusout", function (e) {
      if (!root.contains(e.relatedTarget)) startAuto();
    });

    root.addEventListener("keydown", function (e) {
      var keys = { ArrowLeft: -1, ArrowRight: 1 };
      if (e.key in keys) {
        if (e.target && e.target.tagName === "A") return;
        e.preventDefault();
        goTo(track, closestIndex(track) + keys[e.key]);
        restartAuto();
      } else if (e.key === "Home") {
        e.preventDefault();
        goTo(track, 0);
        restartAuto();
      } else if (e.key === "End") {
        e.preventDefault();
        goTo(track, slides.length - 1);
        restartAuto();
      }
    });

    document.addEventListener("visibilitychange", function () {
      if (document.hidden) stopAuto();
      else startAuto();
    });

    sync();
    startAuto();
  }

  function setupLightbox() {
    var triggers = Array.prototype.slice.call(
      document.querySelectorAll("[data-lightbox] [data-full]")
    );
    if (!triggers.length) return;

    var box = document.createElement("div");
    box.className = "lightbox";
    box.setAttribute("hidden", "");
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-modal", "true");
    box.setAttribute("aria-label", "Aperçu de la photo");
    box.innerHTML =
      '<button type="button" class="lightbox-close" aria-label="Fermer">&times;</button>' +
      '<button type="button" class="lightbox-nav" data-lightbox-prev aria-label="Photo précédente">‹</button>' +
      '<img alt="">' +
      '<button type="button" class="lightbox-nav" data-lightbox-next aria-label="Photo suivante">›</button>' +
      '<div class="lightbox-caption" aria-live="polite"></div>';
    document.body.appendChild(box);

    var img = box.querySelector("img");
    var caption = box.querySelector(".lightbox-caption");
    var closeBtn = box.querySelector(".lightbox-close");
    var index = 0;
    var lastFocus = null;

    function show(i) {
      index = ((i % triggers.length) + triggers.length) % triggers.length;
      var a = triggers[index];
      img.src = a.getAttribute("data-full");
      img.alt = a.getAttribute("data-alt") || "";
      caption.textContent = index + 1 + " / " + triggers.length;
    }

    function open(i) {
      lastFocus = document.activeElement;
      show(i);
      box.removeAttribute("hidden");
      document.body.classList.add("lightbox-open");
      closeBtn.focus();
    }

    function close() {
      box.setAttribute("hidden", "");
      document.body.classList.remove("lightbox-open");
      img.removeAttribute("src");
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    triggers.forEach(function (a, i) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        open(i);
      });
    });

    closeBtn.addEventListener("click", close);
    box.querySelector("[data-lightbox-prev]").addEventListener("click", function () {
      show(index - 1);
    });
    box.querySelector("[data-lightbox-next]").addEventListener("click", function () {
      show(index + 1);
    });
    box.addEventListener("click", function (e) {
      if (e.target === box) close();
    });
    document.addEventListener("keydown", function (e) {
      if (box.hasAttribute("hidden")) return;
      if (e.key === "Escape") close();
      else if (e.key === "ArrowLeft") show(index - 1);
      else if (e.key === "ArrowRight") show(index + 1);
    });
  }

  document.querySelectorAll("[data-carousel]").forEach(enhance);
  setupLightbox();
})();

  function setupFilters() {
    document.querySelectorAll("[data-filter-group]").forEach(function (group) {
      var buttons = group.querySelectorAll(".filter-btn");
      var cards = group.querySelectorAll("[data-card-list] .feature-card");
      if (!buttons.length || !cards.length) return;
      buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          var tag = btn.getAttribute("data-filter") || "*";
          buttons.forEach(function (b) {
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
          });
          cards.forEach(function (card) {
            var tags = (card.getAttribute("data-tags") || "").split(/\s+/);
            var show = tag === "*" || tags.indexOf(tag) !== -1;
            card.classList.toggle("is-filtered-out", !show);
          });
        });
      });
    });
  }
  setupFilters();
