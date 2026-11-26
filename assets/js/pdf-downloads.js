(function () {
  "use strict";

  // Complète le suivi GoatCounter des liens PDF du site (bouton
  // « Télécharger en PDF » et liens déjà présents dans le texte,
  // comme le guide 4008). Les PDF externes ne sont pas comptés.

  var PREFIX = "telechargement-pdf/";

  function pageTitle() {
    var t = document.title || "";
    return t.replace(/\s*\|\s*XAV59213\s*$/, "").trim();
  }

  function isSitePdf(anchor) {
    if (!anchor || !anchor.getAttribute) return false;
    var href = anchor.getAttribute("href");
    if (!href) return false;
    var url;
    try {
      url = new URL(href, document.baseURI);
    } catch (e) {
      return false;
    }
    if (url.origin !== location.origin) return false;
    return /\.pdf$/i.test(url.pathname);
  }

  function fileName(pathname) {
    var parts = pathname.split("/");
    return decodeURIComponent(parts[parts.length - 1] || "");
  }

  function tag(anchor) {
    if (anchor.getAttribute("data-goatcounter-click")) return;
    var url;
    try {
      url = new URL(anchor.getAttribute("href"), document.baseURI);
    } catch (e) {
      return;
    }
    var name = fileName(url.pathname);
    if (!name) return;
    anchor.setAttribute("data-goatcounter-click", PREFIX + name);
    if (!anchor.getAttribute("data-goatcounter-title")) {
      var title = pageTitle();
      anchor.setAttribute(
        "data-goatcounter-title",
        title ? "PDF – " + title : "PDF – " + name
      );
    }
  }

  function tagAll() {
    var links = document.querySelectorAll("a[href]");
    for (var i = 0; i < links.length; i++) {
      if (isSitePdf(links[i])) tag(links[i]);
    }
    if (window.goatcounter && typeof window.goatcounter.bind_events === "function") {
      window.goatcounter.bind_events();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", tagAll);
  } else {
    tagAll();
  }
})();
