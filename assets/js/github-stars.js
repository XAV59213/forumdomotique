(function () {
  var nodes = document.querySelectorAll("[data-github-repo]");
  if (!nodes.length) return;
  var repos = [];
  nodes.forEach(function (el) {
    var name = el.getAttribute("data-github-repo");
    if (name && repos.indexOf(name) === -1) repos.push(name);
  });
  repos.forEach(function (repo) {
    var key = "gh-stars:XAV59213/" + repo;
    var count = null;
    try {
      var cached = sessionStorage.getItem(key);
      if (cached !== null) count = JSON.parse(cached);
    } catch (e) {}
    var apply = function (n) {
      document.querySelectorAll('[data-github-repo="' + repo + '"]').forEach(function (el) {
        el.textContent = String(n);
        el.hidden = false;
        el.setAttribute("aria-label", n + " étoile" + (n > 1 ? "s" : ""));
      });
    };
    if (typeof count === "number") {
      apply(count);
      return;
    }
    fetch("https://api.github.com/repos/XAV59213/" + encodeURIComponent(repo), {
      headers: { Accept: "application/vnd.github+json" }
    }).then(function (r) {
      if (!r.ok) return null;
      return r.json();
    }).then(function (data) {
      if (!data || typeof data.stargazers_count !== "number") return;
      try { sessionStorage.setItem(key, JSON.stringify(data.stargazers_count)); } catch (e) {}
      apply(data.stargazers_count);
    }).catch(function () { /* compteur laissé masqué */ });
  });
})();
