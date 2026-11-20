(function () {
  "use strict";

  var main = document.getElementById("content") || document.querySelector("main");
  if (!main) return;

  var h1 = main.querySelector("h1");
  if (!h1) return;

  var el = document.createElement("p");
  var meta = null;
  var head = h1.closest(".ha-article-head");
  if (head) meta = head.querySelector(".ha-meta");
  if (meta) {
    el = document.createElement("span");
  }
  el.className = "page-views";
  el.setAttribute("aria-live", "polite");
  el.hidden = true;

  if (meta) meta.appendChild(el);
  else h1.insertAdjacentElement("afterend", el);

  function showNouveau() {
    el.hidden = false;
    el.textContent = "👁 Nouveau";
    el.setAttribute("aria-label", "Pas encore de visites enregistrées");
  }

  function showCount(raw) {
    var compact = String(raw).replace(/\s/g, "").replace(/,/g, "").replace(/\u00a0/g, "");
    var num = parseInt(compact, 10);
    if (!isFinite(num) || num <= 0) {
      showNouveau();
      return;
    }
    el.hidden = false;
    el.textContent = "👁 " + raw + (num > 1 ? " vues" : " vue");
    el.setAttribute("aria-label", num + (num > 1 ? " visites" : " visite"));
  }

  var url = "https://forumdomotique.goatcounter.com/counter/" +
    encodeURIComponent(location.pathname) + ".json";

  fetch(url, { method: "GET", credentials: "omit", mode: "cors" })
    .then(function (res) {
      if (res.status === 200) return res.json();
      showNouveau();
      return null;
    })
    .then(function (data) {
      if (!data) return;
      showCount(data.count);
    })
    .catch(function () {
      showNouveau();
    });
})();
