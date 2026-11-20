(function () {
  "use strict";

  var API = "https://forumdomotique.goatcounter.com/counter/";
  var SINCE = "depuis le 20 novembre 2026";

  function parseCount(raw) {
    if (raw == null || raw === "") return NaN;
    var compact = String(raw).replace(/\s/g, "").replace(/,/g, "").replace(/\u00a0/g, "");
    return parseInt(compact, 10);
  }

  function makeEl(tag, className) {
    var el = document.createElement(tag);
    el.className = className || "page-views";
    el.setAttribute("aria-live", "polite");
    el.hidden = true;
    return el;
  }

  function showNouveau(el) {
    el.hidden = false;
    el.textContent = "👁 Nouveau";
    el.setAttribute("aria-label", "Pas encore de visites enregistrées");
  }

  function showCount(el, raw, singular, plural) {
    var num = parseCount(raw);
    if (!isFinite(num) || num <= 0) {
      showNouveau(el);
      return;
    }
    el.hidden = false;
    el.textContent = "👁 " + raw + (num > 1 ? plural : singular);
    el.setAttribute("aria-label", num + (num > 1 ? " visites" : " visite"));
  }

  function loadCount(path, onOk, onFail) {
    fetch(API + encodeURIComponent(path) + ".json", {
      method: "GET",
      credentials: "omit",
      mode: "cors"
    })
      .then(function (res) {
        if (res.status === 200) return res.json();
        onFail();
        return null;
      })
      .then(function (data) {
        if (!data) return;
        onOk(data);
      })
      .catch(function () {
        onFail();
      });
  }

  function placeArticleCounter() {
    var main = document.getElementById("content") || document.querySelector("main");
    if (!main) return null;
    var h1 = main.querySelector("h1");
    if (!h1) return null;
    var el = makeEl("p", "page-views");
    var meta = null;
    var head = h1.closest(".ha-article-head");
    if (head) meta = head.querySelector(".ha-meta");
    if (meta) {
      el = makeEl("span", "page-views");
      meta.appendChild(el);
    } else {
      h1.insertAdjacentElement("afterend", el);
    }
    return el;
  }

  function showSiteTotal(el, data) {
    var uniqueRaw = data && data.count_unique;
    var countRaw = data && data.count;
    var hasUnique = uniqueRaw != null && String(uniqueRaw).length > 0;
    var raw = hasUnique ? uniqueRaw : countRaw;
    var num = parseCount(raw);
    if (!isFinite(num) || num < 0) return false;
    var label;
    if (hasUnique) {
      label = (num > 1 ? " visiteurs " : " visiteur ") + SINCE;
    } else {
      label = (num > 1 ? " vues " : " vue ") + SINCE;
    }
    el.hidden = false;
    el.textContent = "👁 " + raw + label;
    el.setAttribute(
      "aria-label",
      hasUnique
        ? num + (num > 1 ? " visiteurs uniques " : " visiteur unique ") + SINCE
        : num + (num > 1 ? " vues " : " vue ") + SINCE
    );
    return true;
  }

  var isArticle = document.body.classList.contains("has-page-views");
  var footerBox = document.querySelector("[data-views-footer]");
  var pageEl = null;

  if (isArticle) {
    pageEl = placeArticleCounter();
  } else if (footerBox) {
    pageEl = footerBox.querySelector("[data-page-views]");
    if (!pageEl) {
      pageEl = makeEl("span", "page-views");
      pageEl.setAttribute("data-page-views", "");
      footerBox.appendChild(pageEl);
    }
  }

  if (pageEl) {
    var suffixOne = isArticle ? " vue" : " vue de cette page";
    var suffixMany = isArticle ? " vues" : " vues de cette page";
    loadCount(location.pathname, function (data) {
      showCount(pageEl, data.count, suffixOne, suffixMany);
      if (!isArticle && footerBox) footerBox.hidden = false;
    }, function () {
      showNouveau(pageEl);
      if (!isArticle && footerBox) footerBox.hidden = false;
    });
  }

  var totalEl = footerBox && footerBox.querySelector("[data-site-views]");
  if (totalEl) {
    loadCount("TOTAL", function (data) {
      if (showSiteTotal(totalEl, data)) footerBox.hidden = false;
    }, function () { /* masqué discrètement si l’API échoue */ });
  }
})();
