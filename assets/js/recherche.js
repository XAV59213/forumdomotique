(function () {
  "use strict";

  var indexCache = null;
  var indexPromise = null;
  var previewLimit = 8;

  function normalize(value) {
    return String(value || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, " ")
      .trim();
  }

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function highlight(text, words) {
    var safe = escapeHtml(text);
    if (!words.length) return safe;
    var pattern = words
      .slice()
      .sort(function (a, b) { return b.length - a.length; })
      .map(function (word) {
        return word.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      })
      .join("|");
    if (!pattern) return safe;
    try {
      var re = new RegExp("(" + pattern + ")", "gi");
      return safe.replace(re, "<mark>$1</mark>");
    } catch (err) {
      return safe;
    }
  }

  function queryWords(query) {
    return normalize(query).split(" ").filter(function (word) {
      return word.length > 0;
    });
  }

  function scoreItem(item, words) {
    if (!words.length) return 0;
    var title = normalize(item.titre);
    var haystack = normalize(
      (item.titre || "") + " " + (item.resume || "") + " " + (item.rubrique || "")
    );
    var score = 0;
    var joined = words.join(" ");
    if (title === joined) score += 120;
    if (title.indexOf(joined) === 0) score += 80;
    else if (title.indexOf(joined) !== -1) score += 50;
    var allInTitle = true;
    var allInHay = true;
    for (var i = 0; i < words.length; i++) {
      var word = words[i];
      if (title.indexOf(word) === -1) allInTitle = false;
      if (haystack.indexOf(word) === -1) allInHay = false;
      else score += title.indexOf(word) !== -1 ? 18 : 8;
    }
    if (!allInHay) return 0;
    if (allInTitle) score += 30;
    return score;
  }

  function loadIndex(url) {
    if (indexCache) return Promise.resolve(indexCache);
    if (indexPromise) return indexPromise;
    indexPromise = fetch(url, { credentials: "same-origin" })
      .then(function (res) {
        if (!res.ok) throw new Error("index");
        return res.json();
      })
      .then(function (data) {
        indexCache = Array.isArray(data) ? data : [];
        return indexCache;
      })
      .catch(function () {
        indexPromise = null;
        return [];
      });
    return indexPromise;
  }

  function filterItems(items, query, rubrique) {
    var words = queryWords(query);
    var list = items;
    if (rubrique && rubrique !== "*") {
      list = list.filter(function (item) {
        return item.rubrique === rubrique;
      });
    }
    if (!words.length) return [];
    return list
      .map(function (item) {
        return { item: item, score: scoreItem(item, words) };
      })
      .filter(function (row) {
        return row.score > 0;
      })
      .sort(function (a, b) {
        return b.score - a.score || a.item.titre.localeCompare(b.item.titre, "fr");
      })
      .map(function (row) {
        return row.item;
      });
  }

  function uniqueRubriques(items) {
    var seen = {};
    var list = [];
    items.forEach(function (item) {
      if (item.rubrique && !seen[item.rubrique]) {
        seen[item.rubrique] = true;
        list.push(item.rubrique);
      }
    });
    var order = [
      "Guides",
      "Tests",
      "Intégrations",
      "Coin bistrot",
      "Mes créations",
      "Actualité HA",
      "Actualités",
      "Sujets"
    ];
    list.sort(function (a, b) {
      var ia = order.indexOf(a);
      var ib = order.indexOf(b);
      if (ia === -1) ia = 99;
      if (ib === -1) ib = 99;
      return ia - ib || a.localeCompare(b, "fr");
    });
    return list;
  }

  function cardHtml(item, words, compact) {
    var thumb = item.image
      ? '<img class="card-thumb" src="' +
        escapeHtml(item.image) +
        '" alt="" width="280" height="140" loading="lazy">'
      : "";
    var cls = "feature-card recherche-card" + (compact ? " recherche-card-compact" : "");
    return (
      '<a class="' +
      cls +
      '" href="' +
      escapeHtml(item.url) +
      '">' +
      thumb +
      '<div class="tag">' +
      escapeHtml(item.rubrique) +
      "</div>" +
      "<h3>" +
      highlight(item.titre, words) +
      "</h3>" +
      (item.resume ? "<p>" + highlight(item.resume, words) + "</p>" : "") +
      "</a>"
    );
  }

  function countLabel(n) {
    if (n === 0) return "Aucun résultat";
    if (n === 1) return "1 résultat";
    return n + " résultats";
  }

  function initPage() {
    var root = document.getElementById("recherche-page");
    if (!root) return;
    var input = document.getElementById("recherche-q");
    var filters = document.getElementById("recherche-filters");
    var count = document.getElementById("recherche-count");
    var results = document.getElementById("recherche-results");
    var form = root.querySelector(".recherche-form");
    var indexUrl = root.getAttribute("data-index");
    var currentRubrique = "*";
    var timer = null;

    var params = new URLSearchParams(window.location.search);
    if (input && params.get("q") && !input.value) input.value = params.get("q");
    if (params.get("rubrique")) currentRubrique = params.get("rubrique");

    function setUrl(query, rubrique, replace) {
      var url = new URL(window.location.href);
      if (query) url.searchParams.set("q", query);
      else url.searchParams.delete("q");
      if (rubrique && rubrique !== "*") url.searchParams.set("rubrique", rubrique);
      else url.searchParams.delete("rubrique");
      var next = url.pathname + url.search;
      if (replace) history.replaceState(null, "", next);
      else history.pushState(null, "", next);
    }

    function renderFilters(items) {
      if (!filters) return;
      var rubriques = uniqueRubriques(items);
      if (!rubriques.length) {
        filters.hidden = true;
        filters.innerHTML = "";
        return;
      }
      filters.hidden = false;
      var html =
        '<button type="button" class="filter-btn" data-rubrique="*" ' +
        (currentRubrique === "*" ? 'aria-pressed="true"' : 'aria-pressed="false"') +
        ">Toutes</button>";
      rubriques.forEach(function (name) {
        html +=
          '<button type="button" class="filter-btn" data-rubrique="' +
          escapeHtml(name) +
          '" ' +
          (currentRubrique === name ? 'aria-pressed="true"' : 'aria-pressed="false"') +
          ">" +
          escapeHtml(name) +
          "</button>";
      });
      filters.innerHTML = html;
    }

    function render() {
      var query = input ? input.value.trim() : "";
      var words = queryWords(query);
      loadIndex(indexUrl).then(function (items) {
        renderFilters(items);
        if (!query) {
          if (count) count.textContent = "Saisissez un mot pour lancer la recherche.";
          if (results) results.innerHTML = "";
          return;
        }
        var found = filterItems(items, query, currentRubrique);
        if (count) count.textContent = countLabel(found.length);
        if (results) {
          results.innerHTML = found.length
            ? found.map(function (item) { return cardHtml(item, words, false); }).join("")
            : '<p class="recherche-empty">Aucun contenu ne correspond. Essayez un autre mot, ou retirez le filtre de rubrique.</p>';
        }
      });
    }

    if (form) {
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        setUrl(input ? input.value.trim() : "", currentRubrique, false);
        render();
      });
    }
    if (input) {
      input.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(function () {
          setUrl(input.value.trim(), currentRubrique, true);
          render();
        }, 140);
      });
    }
    if (filters) {
      filters.addEventListener("click", function (event) {
        var btn = event.target.closest("[data-rubrique]");
        if (!btn) return;
        currentRubrique = btn.getAttribute("data-rubrique") || "*";
        setUrl(input ? input.value.trim() : "", currentRubrique, true);
        render();
      });
    }
    window.addEventListener("popstate", function () {
      var next = new URLSearchParams(window.location.search);
      if (input) input.value = next.get("q") || "";
      currentRubrique = next.get("rubrique") || "*";
      render();
    });
    render();
    if (input && input.value) input.focus();
  }

  function initHeader() {
    var header = document.querySelector(".site-header");
    var toggle = document.querySelector(".search-toggle");
    var panel = document.getElementById("site-search");
    if (!header || !toggle || !panel) return;

    var input = document.getElementById("site-search-q");
    var results = document.getElementById("site-search-results");
    var count = document.getElementById("site-search-count");
    var more = document.getElementById("site-search-more");
    var form = panel.querySelector(".site-search-form");
    var pageUrl = panel.getAttribute("data-page") || "/recherche/";
    var indexUrl = panel.getAttribute("data-index");
    var timer = null;
    var pageInput = document.getElementById("recherche-q");
    var onSearchPage = Boolean(document.getElementById("recherche-page"));

    function setOpen(open) {
      if (onSearchPage) {
        if (pageInput) {
          pageInput.focus();
          pageInput.select();
        }
        return;
      }
      panel.hidden = !open;
      header.classList.toggle("is-search-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Fermer la recherche" : "Ouvrir la recherche");
      if (open) {
        header.classList.remove("is-open");
        var navToggle = header.querySelector(".nav-toggle");
        if (navToggle) {
          navToggle.setAttribute("aria-expanded", "false");
          navToggle.setAttribute("aria-label", "Ouvrir le menu");
        }
        if (input) {
          input.focus();
          input.select();
        }
        renderPreview();
      }
    }

    function renderPreview() {
      if (panel.hidden) return;
      var query = input ? input.value.trim() : "";
      var words = queryWords(query);
      if (more) {
        var href = pageUrl + (query ? "?q=" + encodeURIComponent(query) : "");
        more.querySelector("a").setAttribute("href", href);
        more.hidden = false;
      }
      if (!query) {
        if (count) count.textContent = "Saisissez un mot pour lancer la recherche.";
        if (results) results.innerHTML = "";
        return;
      }
      loadIndex(indexUrl).then(function (items) {
        var found = filterItems(items, query, "*");
        if (count) {
          count.textContent =
            found.length > previewLimit
              ? countLabel(found.length) + " — voici les " + previewLimit + " premiers"
              : countLabel(found.length);
        }
        if (results) {
          results.innerHTML = found.length
            ? found.slice(0, previewLimit).map(function (item) {
                return cardHtml(item, words, true);
              }).join("")
            : '<p class="recherche-empty">Aucun contenu ne correspond. Essayez un autre mot.</p>';
        }
      });
    }

    toggle.addEventListener("click", function () {
      setOpen(panel.hidden);
    });
    document.addEventListener("keydown", function (event) {
      var key = event.key;
      var typing =
        event.target &&
        (event.target.tagName === "INPUT" ||
          event.target.tagName === "TEXTAREA" ||
          event.target.isContentEditable);
      if (key === "Escape") setOpen(false);
      if ((key === "k" || key === "K") && (event.metaKey || event.ctrlKey)) {
        event.preventDefault();
        setOpen(true);
      }
      if (key === "/" && !typing && !event.metaKey && !event.ctrlKey && !event.altKey) {
        event.preventDefault();
        setOpen(true);
      }
    });
    document.addEventListener("click", function (event) {
      if (panel.hidden) return;
      if (!header.contains(event.target)) setOpen(false);
    });
    if (form) {
      form.addEventListener("submit", function (event) {
        if (!input || !input.value.trim()) return;
        event.preventDefault();
        window.location.href = pageUrl + "?q=" + encodeURIComponent(input.value.trim());
      });
    }
    if (input) {
      input.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(renderPreview, 140);
      });
    }
    var navToggle = header.querySelector(".nav-toggle");
    if (navToggle) {
      navToggle.addEventListener("click", function () {
        if (!panel.hidden) setOpen(false);
      });
    }
  }

  initPage();
  initHeader();
})();
