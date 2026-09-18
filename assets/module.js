(function () {
  "use strict";

  var script = document.currentScript;
  var moduleKey = script && script.dataset.moduleKey;
  if (!moduleKey) {
    console.error("module.js: atributo data-module-key ausente.");
    return;
  }

  var moduleFile = location.pathname.split("/").pop();
  var storageTheme = "vm_theme";
  var storageProgress = "vm_progress_" + moduleKey;
  var language = (document.documentElement.lang || "pt").split("-")[0];
  var messages = {
    pt: {
      sectionDone: "Seção concluída",
      sectionPending: "Ainda não concluída",
      buttonDone: "Concluído ✓",
      buttonPending: "Marcar como concluído",
      progress: function (done, total) {
        return done + " de " + total + " seções concluídas";
      }
    },
    en: {
      sectionDone: "Section completed",
      sectionPending: "Not yet completed",
      buttonDone: "Completed ✓",
      buttonPending: "Mark as completed",
      progress: function (done, total) {
        return done + " of " + total + " sections completed";
      }
    },
    es: {
      sectionDone: "Sección completada",
      sectionPending: "Aún no completada",
      buttonDone: "Completada ✓",
      buttonPending: "Marcar como completada",
      progress: function (done, total) {
        return done + " de " + total + " secciones completadas";
      }
    }
  };
  var text = messages[language] || messages.pt;

  function storageGet(key, fallback) {
    try {
      var value = localStorage.getItem(key);
      return value === null ? fallback : value;
    } catch (error) {
      return fallback;
    }
  }

  function storageSet(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (error) {
      // O site continua funcional quando o navegador bloqueia o armazenamento.
    }
  }

  storageSet("vm_lastmodule", moduleFile);

  var root = document.documentElement;
  function applyTheme(choice) {
    var followsSystem =
      choice === "auto" &&
      window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches;
    root.setAttribute("data-theme", choice === "dark" || followsSystem ? "dark" : "light");
  }
  applyTheme(storageGet(storageTheme, "auto"));

  var sidebar = document.getElementById("sidebar");
  var scrim = document.getElementById("sidebar-scrim");
  var menuToggle = document.getElementById("menu-toggle");

  function setSidebar(open) {
    if (sidebar) sidebar.classList.toggle("open", open);
    if (scrim) scrim.classList.toggle("show", open);
    if (menuToggle) menuToggle.setAttribute("aria-expanded", String(open));
  }

  if (menuToggle) {
    menuToggle.addEventListener("click", function () {
      setSidebar(!(sidebar && sidebar.classList.contains("open")));
    });
  }
  if (scrim) scrim.addEventListener("click", function () { setSidebar(false); });
  document.querySelectorAll("#toc-list a").forEach(function (link) {
    link.addEventListener("click", function () { setSidebar(false); });
  });

  var progressBar = document.getElementById("progress-bar");
  function updateReadingProgress() {
    if (!progressBar) return;
    var page = document.documentElement;
    var scrollTop = page.scrollTop || document.body.scrollTop;
    var scrollHeight = (page.scrollHeight || document.body.scrollHeight) - page.clientHeight;
    var percentage = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    progressBar.style.width = percentage + "%";
  }
  document.addEventListener("scroll", updateReadingProgress, { passive: true });
  updateReadingProgress();

  var sections = Array.prototype.slice.call(
    document.querySelectorAll("section.study-section")
  );
  var tocLinks = {};
  document.querySelectorAll("#toc-list a").forEach(function (link) {
    tocLinks[link.getAttribute("href").slice(1)] = link;
  });

  if ("IntersectionObserver" in window) {
    var spyObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = tocLinks[entry.target.id];
        if (!link || !entry.isIntersecting) return;
        Object.keys(tocLinks).forEach(function (id) {
          tocLinks[id].classList.remove("active");
        });
        link.classList.add("active");
        storageSet("vm_lastseen_" + moduleFile, entry.target.id);
      });
    }, { rootMargin: "-30% 0px -60% 0px", threshold: 0 });
    sections.forEach(function (section) { spyObserver.observe(section); });
  }

  if (location.hash.length > 1) {
    var deepLinkTarget = document.getElementById(location.hash.slice(1));
    if (deepLinkTarget) {
      requestAnimationFrame(function () {
        deepLinkTarget.classList.add("visible");
        deepLinkTarget.scrollIntoView({ behavior: "auto", block: "start" });
      });
    }
  }

  if ("IntersectionObserver" in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12 });
    sections.forEach(function (section) { revealObserver.observe(section); });
  } else {
    sections.forEach(function (section) { section.classList.add("visible"); });
  }

  function loadProgress() {
    try {
      return JSON.parse(storageGet(storageProgress, "{}"));
    } catch (error) {
      return {};
    }
  }

  function saveProgress(state) {
    storageSet(storageProgress, JSON.stringify(state));
  }

  function syncProgressToServer(section, done) {
    fetch("/api/progresso", {
      method: "POST",
      credentials: "same-origin",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ module: moduleFile, section: section, done: done })
    }).catch(function () {});
  }

  function mergeServerProgress() {
    return fetch("/api/progresso", { credentials: "same-origin" })
      .then(function (response) { return response.ok ? response.json() : null; })
      .then(function (data) {
        if (!data || !data.progress || !data.progress[moduleFile]) return;
        saveProgress(Object.assign({}, loadProgress(), data.progress[moduleFile]));
      })
      .catch(function () {});
  }

  function setText(element, selector, value) {
    var target = element && element.querySelector(selector);
    if (target) target.textContent = value;
  }

  function renderProgress() {
    var state = loadProgress();
    var completed = 0;

    sections.forEach(function (section) {
      var id = section.id;
      var isDone = Boolean(state[id]);
      if (isDone) completed += 1;

      var check = document.querySelector('.toc .check[data-target="' + id + '"]');
      var mark = section.querySelector(".section-mark");
      var button = section.querySelector(".btn-complete");

      if (check) {
        check.classList.toggle("done", isDone);
        check.textContent = isDone ? "✓" : "";
      }
      if (mark) {
        mark.classList.toggle("done", isDone);
        setText(mark, ".mark-text", isDone ? text.sectionDone : text.sectionPending);
      }
      if (button) {
        button.classList.toggle("done", isDone);
        button.setAttribute("aria-pressed", String(isDone));
        setText(button, ".btn-text", isDone ? text.buttonDone : text.buttonPending);
      }
    });

    var fill = document.getElementById("sidebar-fill");
    var label = document.getElementById("sidebar-label");
    var percentage = sections.length > 0 ? (completed / sections.length) * 100 : 0;
    if (fill) fill.style.width = percentage + "%";
    if (label) label.textContent = text.progress(completed, sections.length);
  }

  document.querySelectorAll(".btn-complete").forEach(function (button) {
    button.addEventListener("click", function () {
      var id = button.getAttribute("data-target");
      var state = loadProgress();
      state[id] = !state[id];
      saveProgress(state);
      syncProgressToServer(id, state[id]);
      renderProgress();
    });
  });
  mergeServerProgress().then(renderProgress);

  document.querySelectorAll(".toggle-compare").forEach(function (box) {
    var tabs = box.querySelectorAll(".tabs button");
    var panels = box.querySelectorAll(".panel");
    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (item) { item.classList.remove("active"); });
        panels.forEach(function (panel) { panel.classList.remove("active"); });
        tab.classList.add("active");
        if (panels[index]) panels[index].classList.add("active");
      });
    });
  });

  if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("/sw.js").catch(function () {});
    });
  }
})();
