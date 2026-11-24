(function () {
  var OWNER = "XAV59213";
  var REPO_OK = /^[A-Za-z0-9._-]+$/;
  var LIST_SIZE = 5;
  var blocks = document.querySelectorAll("[data-github-activity]");
  if (!blocks.length) return;

  var repos = [];
  blocks.forEach(function (el) {
    var name = el.getAttribute("data-github-activity");
    if (name && REPO_OK.test(name) && repos.indexOf(name) === -1) repos.push(name);
  });

  function cacheKey(repo) {
    return "gh-activity:" + OWNER + "/" + repo;
  }

  function readCache(repo) {
    try {
      var raw = sessionStorage.getItem(cacheKey(repo));
      if (!raw) return null;
      var data = JSON.parse(raw);
      if (!data || !Array.isArray(data.issues) || !Array.isArray(data.pulls)) return null;
      return data;
    } catch (e) {
      return null;
    }
  }

  function writeCache(repo, data) {
    try {
      sessionStorage.setItem(cacheKey(repo), JSON.stringify(data));
    } catch (e) {}
  }

  function api(url) {
    return fetch(url, { headers: { Accept: "application/vnd.github+json" } }).then(function (res) {
      return res.json().then(function (body) {
        return { ok: res.ok, status: res.status, body: body, res: res };
      }).catch(function () {
        return { ok: false, status: res.status, body: null, res: res };
      });
    });
  }

  function searchUrl(repo, qualifiers, perPage) {
    var q = "repo:" + OWNER + "/" + repo + " " + qualifiers;
    return "https://api.github.com/search/issues?q=" + encodeURIComponent(q) +
      "&sort=updated&order=desc&per_page=" + (perPage || LIST_SIZE);
  }

  function pullsUrl(repo, state, perPage) {
    return "https://api.github.com/repos/" + OWNER + "/" + encodeURIComponent(repo) +
      "/pulls?state=" + state + "&sort=updated&direction=desc&per_page=" + perPage;
  }

  function linkCount(res, body) {
    var link = res.headers.get("Link") || "";
    var match = /[?&]page=(\d+)>;\s*rel="last"/.exec(link);
    if (match) return parseInt(match[1], 10);
    return Array.isArray(body) ? body.length : 0;
  }

  function mapIssue(item) {
    return {
      number: item.number,
      title: item.title || "",
      state: item.state,
      updated_at: item.updated_at,
      html_url: item.html_url
    };
  }

  function mapPull(item) {
    return {
      number: item.number,
      title: item.title || "",
      state: item.state,
      merged: Boolean(item.merged_at),
      updated_at: item.updated_at,
      html_url: item.html_url
    };
  }

  function mergeRecent(groups, limit) {
    var all = [];
    groups.forEach(function (list) {
      if (Array.isArray(list)) all = all.concat(list);
    });
    all.sort(function (a, b) {
      return String(b.updated_at || "").localeCompare(String(a.updated_at || ""));
    });
    var seen = {};
    var out = [];
    all.forEach(function (item) {
      if (seen[item.number]) return;
      seen[item.number] = true;
      out.push(item);
    });
    return out.slice(0, limit);
  }

  function isGithubUrl(url, repo, kind, number) {
    if (typeof url !== "string") return false;
    var expected = "https://github.com/" + OWNER + "/" + repo + "/" + kind + "/" + number;
    return url === expected || url.indexOf(expected + "#") === 0 || url.indexOf(expected + "?") === 0;
  }

  function safeItemUrl(item, repo, isPr) {
    var kind = isPr ? "pull" : "issues";
    var fallback = "https://github.com/" + OWNER + "/" + repo + "/" + kind + "/" + item.number;
    return isGithubUrl(item.html_url, repo, kind, item.number) ? item.html_url : fallback;
  }

  function formatDate(iso) {
    if (!iso) return "";
    var d = new Date(iso);
    if (isNaN(d.getTime())) return "";
    return d.toLocaleDateString("fr-FR", {
      day: "numeric",
      month: "short",
      year: "numeric",
      timeZone: "Europe/Paris"
    });
  }

  function plural(n, singular, pluralForm) {
    return n + " " + (n === 1 ? singular : pluralForm);
  }

  function issueCountPhrase(open, closed) {
    return plural(open, "ouverte", "ouvertes") + " · " + plural(closed, "fermée", "fermées");
  }

  function prCountPhrase(data) {
    var parts = [plural(data.prsOpen, "ouverte", "ouvertes")];
    if (data.closedIncludesMerged && data.prsClosedUnmerged === 0) {
      parts.push(plural(data.prsMerged, "fusionnée", "fusionnées"));
    } else if (data.prsMerged > 0 && data.prsClosedUnmerged > 0) {
      parts.push(plural(data.prsMerged, "fusionnée", "fusionnées"));
      parts.push(plural(data.prsClosedUnmerged, "fermée", "fermées"));
    } else if (data.prsMerged > 0) {
      parts.push(plural(data.prsMerged, "fusionnée", "fusionnées"));
    } else {
      parts.push(plural(data.prsClosedUnmerged, "fermée", "fermées"));
    }
    return parts.join(" · ");
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function badgeFor(item, isPr) {
    var label, cls;
    if (isPr && item.merged) {
      label = "Fusionnée";
      cls = "is-merged";
    } else if (item.state === "open") {
      label = "Ouverte";
      cls = "is-open";
    } else {
      label = "Fermée";
      cls = "is-closed";
    }
    return el("span", "github-activity-badge " + cls, label);
  }

  function renderList(repo, items, isPr, emptyLabel) {
    if (!items.length) return el("p", "github-activity-empty", emptyLabel);
    var ul = el("ul", "github-activity-list");
    items.forEach(function (item) {
      if (typeof item.number !== "number") return;
      var li = el("li", "github-activity-item");
      var link = el("a", "github-activity-item-link");
      link.href = safeItemUrl(item, repo, isPr);
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      var num = el("span", "github-activity-num", "#" + item.number);
      var title = el("span", "github-activity-item-title", item.title || "(sans titre)");
      link.appendChild(num);
      link.appendChild(document.createTextNode(" "));
      link.appendChild(title);
      var meta = el("p", "github-activity-item-meta");
      meta.appendChild(badgeFor(item, isPr));
      var date = formatDate(item.updated_at);
      if (date) {
        meta.appendChild(document.createTextNode(" · " + date));
      }
      li.appendChild(link);
      li.appendChild(meta);
      ul.appendChild(li);
    });
    return ul;
  }

  var desktopMq = window.matchMedia("(min-width: 800px)");

  function syncPanels(root) {
    var desktop = desktopMq.matches;
    var tabs = root.querySelectorAll('[role="tab"]');
    var panels = root.querySelectorAll('[role="tabpanel"]');
    panels.forEach(function (panel) {
      var on = panel.classList.contains("is-active");
      if (desktop || on) panel.removeAttribute("hidden");
      else panel.setAttribute("hidden", "");
    });
    tabs.forEach(function (tab) {
      if (desktop) tab.tabIndex = -1;
      else tab.tabIndex = tab.getAttribute("aria-selected") === "true" ? 0 : -1;
    });
  }

  function bindTabs(root) {
    var tabs = root.querySelectorAll('[role="tab"]');
    var panels = root.querySelectorAll('[role="tabpanel"]');
    if (!tabs.length) return;
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var id = tab.getAttribute("aria-controls");
        tabs.forEach(function (t) {
          var selected = t === tab;
          t.setAttribute("aria-selected", selected ? "true" : "false");
        });
        panels.forEach(function (panel) {
          panel.classList.toggle("is-active", panel.id === id);
        });
        syncPanels(root);
      });
    });
    if (typeof desktopMq.addEventListener === "function") {
      desktopMq.addEventListener("change", function () { syncPanels(root); });
    } else if (typeof desktopMq.addListener === "function") {
      desktopMq.addListener(function () { syncPanels(root); });
    }
    syncPanels(root);
  }

  function render(block, repo, data, failed) {
    var live = block.querySelector("[data-github-activity-live]");
    var status = block.querySelector("[data-github-activity-status]");
    if (failed || !data) {
      if (live) {
        live.hidden = true;
        live.textContent = "";
      }
      if (status) {
        status.hidden = false;
        status.textContent = "La liste n’a pas pu être chargée. Vous pouvez la consulter directement sur GitHub.";
      }
      return;
    }
    if (!live || !status) return;
    live.textContent = "";

    var counts = el("div", "github-activity-counts");
    var issuesCount = el("p", "github-activity-count");
    issuesCount.appendChild(el("span", "github-activity-count-label", "Issues"));
    issuesCount.appendChild(document.createTextNode(" : " + issueCountPhrase(data.issuesOpen, data.issuesClosed)));
    var prsCount = el("p", "github-activity-count");
    prsCount.appendChild(el("span", "github-activity-count-label", "Pull requests"));
    prsCount.appendChild(document.createTextNode(" : " + prCountPhrase(data)));
    counts.appendChild(issuesCount);
    counts.appendChild(prsCount);
    live.appendChild(counts);

    var uid = "github-activity-" + repo;
    var tabs = el("div", "github-activity-tabs");
    tabs.setAttribute("role", "tablist");
    tabs.setAttribute("aria-label", "Issues et pull requests");
    var tabIssues = el("button", "github-activity-tab");
    tabIssues.type = "button";
    tabIssues.id = uid + "-tab-issues";
    tabIssues.setAttribute("role", "tab");
    tabIssues.setAttribute("aria-selected", "true");
    tabIssues.setAttribute("aria-controls", uid + "-panel-issues");
    tabIssues.tabIndex = 0;
    tabIssues.textContent = "Issues";
    var tabPrs = el("button", "github-activity-tab");
    tabPrs.type = "button";
    tabPrs.id = uid + "-tab-prs";
    tabPrs.setAttribute("role", "tab");
    tabPrs.setAttribute("aria-selected", "false");
    tabPrs.setAttribute("aria-controls", uid + "-panel-prs");
    tabPrs.tabIndex = -1;
    tabPrs.textContent = "Pull requests";
    tabs.appendChild(tabIssues);
    tabs.appendChild(tabPrs);
    live.appendChild(tabs);

    var panels = el("div", "github-activity-panels");
    var issuesPanel = el("div", "github-activity-panel is-active");
    issuesPanel.id = uid + "-panel-issues";
    issuesPanel.setAttribute("role", "tabpanel");
    issuesPanel.setAttribute("aria-labelledby", uid + "-tab-issues");
    issuesPanel.appendChild(el("h3", "github-activity-col-title", "Issues récentes"));
    issuesPanel.appendChild(renderList(repo, data.issues, false, "Aucune issue pour le moment."));

    var prsPanel = el("div", "github-activity-panel");
    prsPanel.id = uid + "-panel-prs";
    prsPanel.setAttribute("role", "tabpanel");
    prsPanel.setAttribute("aria-labelledby", uid + "-tab-prs");
    prsPanel.setAttribute("hidden", "");
    prsPanel.appendChild(el("h3", "github-activity-col-title", "Pull requests récentes"));
    prsPanel.appendChild(renderList(repo, data.pulls, true, "Aucune pull request pour le moment."));

    panels.appendChild(issuesPanel);
    panels.appendChild(prsPanel);
    live.appendChild(panels);
    bindTabs(live);

    live.hidden = false;
    status.hidden = true;
    status.textContent = "";
  }

  function fetchActivity(repo) {
    return Promise.all([
      api(searchUrl(repo, "is:issue is:open", LIST_SIZE)),
      api(searchUrl(repo, "is:issue is:closed", LIST_SIZE)),
      api(pullsUrl(repo, "all", 100))
    ]).then(function (results) {
      var openSearch = results[0];
      var closedSearch = results[1];
      var pullsRes = results[2];
      if (!openSearch.ok || !closedSearch.ok || !pullsRes.ok) {
        throw new Error("api");
      }
      var issuesOpen = typeof openSearch.body.total_count === "number" ? openSearch.body.total_count : 0;
      var issuesClosed = typeof closedSearch.body.total_count === "number" ? closedSearch.body.total_count : 0;
      var issues = mergeRecent([
        (openSearch.body.items || []).map(mapIssue),
        (closedSearch.body.items || []).map(mapIssue)
      ], LIST_SIZE);

      var pullsRaw = Array.isArray(pullsRes.body) ? pullsRes.body : [];
      var recentPulls = pullsRaw.slice(0, LIST_SIZE).map(mapPull);
      var data = {
        issuesOpen: issuesOpen,
        issuesClosed: issuesClosed,
        issues: issues,
        pulls: recentPulls,
        prsOpen: 0,
        prsMerged: 0,
        prsClosedUnmerged: 0,
        closedIncludesMerged: false
      };

      if (pullsRaw.length < 100) {
        data.prsOpen = pullsRaw.filter(function (p) { return p.state === "open"; }).length;
        data.prsMerged = pullsRaw.filter(function (p) { return p.merged_at; }).length;
        data.prsClosedUnmerged = pullsRaw.filter(function (p) { return p.state === "closed" && !p.merged_at; }).length;
        return data;
      }

      var listedMerged = pullsRaw.filter(function (p) { return p.merged_at; }).length;
      var listedOpen = pullsRaw.filter(function (p) { return p.state === "open"; }).length;
      var listedClosedUnmerged = pullsRaw.filter(function (p) { return p.state === "closed" && !p.merged_at; }).length;
      var allListedClosedAreMerged = listedClosedUnmerged === 0;

      return Promise.all([
        api(pullsUrl(repo, "open", 1)),
        api(pullsUrl(repo, "closed", 1))
      ]).then(function (counts) {
        if (!counts[0].ok || !counts[1].ok) {
          data.prsOpen = listedOpen;
          data.prsMerged = listedMerged;
          data.prsClosedUnmerged = listedClosedUnmerged;
          return data;
        }
        data.prsOpen = linkCount(counts[0].res, counts[0].body);
        var closedTotal = linkCount(counts[1].res, counts[1].body);
        if (allListedClosedAreMerged) {
          data.prsMerged = closedTotal;
          data.prsClosedUnmerged = 0;
        } else {
          data.prsMerged = listedMerged;
          data.prsClosedUnmerged = Math.max(0, closedTotal - listedMerged);
          data.closedIncludesMerged = true;
        }
        return data;
      });
    });
  }

  function apply(repo, data, failed) {
    document.querySelectorAll('[data-github-activity="' + repo + '"]').forEach(function (block) {
      render(block, repo, data, failed);
    });
  }

  repos.forEach(function (repo) {
    var cached = readCache(repo);
    if (cached) {
      apply(repo, cached, false);
      return;
    }
    fetchActivity(repo).then(function (data) {
      writeCache(repo, data);
      apply(repo, data, false);
    }).catch(function () {
      apply(repo, null, true);
    });
  });
})();
