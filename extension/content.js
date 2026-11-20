// Inyecta la barra de Prompt Lab (Score en vivo + Optimizar + Deshacer) en ChatGPT Web
(() => {
  const BAR_ID = "promptlab-toolbar";
  const BTN_ID = "promptlab-optimize-btn";
  const SCORE_ID = "promptlab-score-badge";
  const UNDO_ID = "promptlab-undo-btn";

  let lastRawPrompt = "";
  let attachedBox = null;

  function getPromptBox() {
    return (
      document.querySelector('#prompt-textarea[contenteditable="true"]') ||
      document.querySelector('div.ProseMirror[contenteditable="true"]') ||
      document.querySelector("#prompt-textarea") ||
      document.querySelector("textarea")
    );
  }

  function readPromptText(el) {
    if (!el) return "";
    if (el.tagName === "TEXTAREA") return el.value || "";
    return (el.innerText || el.textContent || "").replace(/\u200B/g, "");
  }

  function writePromptText(el, newText) {
    if (!el) return;
    el.focus();

    if (el.tagName === "TEXTAREA") {
      const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value")?.set;
      if (setter) setter.call(el, newText);
      else el.value = newText;
      el.dispatchEvent(new Event("input", { bubbles: true }));
      el.dispatchEvent(new Event("change", { bubbles: true }));
      return;
    }

    // ProseMirror / contenteditable: construir nodos <p> limpios y notificar a React
    const lines = newText.split(/\n/);
    const frag = document.createDocumentFragment();
    for (const line of lines) {
      const p = document.createElement("p");
      if (line.length === 0) {
        p.appendChild(document.createElement("br"));
      } else {
        p.textContent = line;
      }
      frag.appendChild(p);
    }
    el.replaceChildren(frag);
    el.dispatchEvent(new InputEvent("input", { bubbles: true, cancelable: true, inputType: "insertText", data: newText }));
  }

  function updateScoreBadge() {
    const badge = document.getElementById(SCORE_ID);
    const box = getPromptBox();
    if (!badge || !box || !window.PromptLabOptimizer) return;

    const raw = readPromptText(box);
    if (!raw.trim()) {
      badge.textContent = "Score: —";
      badge.style.color = "#94a3b8";
      badge.style.borderColor = "#334155";
      return;
    }

    const { score } = window.PromptLabOptimizer.analyze(raw);
    badge.textContent = `Score: ${score}/10`;
    if (score >= 9) {
      badge.style.color = "#10b981";
      badge.style.borderColor = "rgba(16, 185, 129, 0.55)";
    } else if (score >= 6) {
      badge.style.color = "#ffd400";
      badge.style.borderColor = "rgba(255, 212, 0, 0.55)";
    } else {
      badge.style.color = "#f87171";
      badge.style.borderColor = "rgba(248, 113, 113, 0.55)";
    }
  }

  function bindInputListener(box) {
    if (!box || attachedBox === box) return;
    attachedBox = box;
    box.addEventListener("input", () => updateScoreBadge());
  }

  function injectToolbar() {
    const box = getPromptBox();
    if (!box || !box.parentElement) return;
    bindInputListener(box);

    if (document.getElementById(BAR_ID)) {
      updateScoreBadge();
      return;
    }

    const bar = document.createElement("div");
    bar.id = BAR_ID;
    Object.assign(bar.style, {
      display: "flex",
      alignItems: "center",
      gap: "8px",
      marginTop: "8px",
      flexWrap: "wrap"
    });

    const btn = document.createElement("button");
    btn.id = BTN_ID;
    btn.type = "button";
    btn.textContent = "✦ Optimizar con Prompt Lab";
    Object.assign(btn.style, {
      padding: "6px 14px",
      borderRadius: "999px",
      border: "1px solid rgba(0, 210, 255, 0.55)",
      background: "linear-gradient(135deg, #0f172a, #1e293b)",
      color: "#f5f7fa",
      fontSize: "12px",
      fontWeight: "700",
      cursor: "pointer",
      boxShadow: "0 4px 14px rgba(0, 210, 255, 0.16)"
    });

    const badge = document.createElement("span");
    badge.id = SCORE_ID;
    badge.textContent = "Score: —";
    Object.assign(badge.style, {
      padding: "4px 10px",
      borderRadius: "999px",
      border: "1px solid #334155",
      background: "#0b0f17",
      color: "#94a3b8",
      fontSize: "11px",
      fontWeight: "700",
      fontFamily: "monospace"
    });

    const undoBtn = document.createElement("button");
    undoBtn.id = UNDO_ID;
    undoBtn.type = "button";
    undoBtn.textContent = "↩ Deshacer";
    undoBtn.style.display = "none";
    Object.assign(undoBtn.style, {
      padding: "5px 10px",
      borderRadius: "999px",
      border: "1px solid #334155",
      background: "#15191f",
      color: "#cbd5e1",
      fontSize: "11px",
      fontWeight: "600",
      cursor: "pointer"
    });

    btn.addEventListener("click", () => {
      const target = getPromptBox();
      const raw = readPromptText(target);
      if (!raw.trim()) return;

      if (window.PromptLabOptimizer.isOptimized(raw)) {
        btn.textContent = "✓ Ya está en 10/10";
        setTimeout(() => { btn.textContent = "✦ Optimizar con Prompt Lab"; }, 2000);
        return;
      }

      lastRawPrompt = raw;
      const before = window.PromptLabOptimizer.analyze(raw);

      const applyOptimized = (cfg = {}) => {
        const optimized = window.PromptLabOptimizer.optimize(raw, {
          role: cfg.promptLabRole,
          tone: cfg.promptLabTone,
          format: cfg.promptLabFormat,
          constraint: cfg.promptLabConstraint
        });
        writePromptText(target, optimized);
        updateScoreBadge();
        undoBtn.style.display = "inline-block";
        btn.textContent = `✓ Optimizado (${before.score}/10 → 10/10)`;
        setTimeout(() => { btn.textContent = "✦ Optimizar con Prompt Lab"; }, 2400);
      };

      if (typeof chrome !== "undefined" && chrome?.storage?.local) {
        chrome.storage.local.get(
          ["promptLabRole", "promptLabTone", "promptLabFormat", "promptLabConstraint"],
          (cfg) => applyOptimized(cfg || {})
        );
      } else {
        applyOptimized({});
      }
    });

    undoBtn.addEventListener("click", () => {
      const target = getPromptBox();
      if (!target || !lastRawPrompt) return;
      writePromptText(target, lastRawPrompt);
      updateScoreBadge();
      undoBtn.style.display = "none";
    });

    bar.appendChild(btn);
    bar.appendChild(badge);
    bar.appendChild(undoBtn);
    box.parentElement.appendChild(bar);
    updateScoreBadge();
  }

  const observer = new MutationObserver(() => injectToolbar());
  observer.observe(document.body, { childList: true, subtree: true });
  injectToolbar();
})();
