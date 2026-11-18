// Inyecta el botón de Prompt Lab en el editor de ChatGPT Web
(() => {
  const BUTTON_ID = "promptlab-optimize-btn";

  function getPromptBox() {
    return (
      document.querySelector("#prompt-textarea") ||
      document.querySelector('div[contenteditable="true"][id="prompt-textarea"]') ||
      document.querySelector("textarea")
    );
  }

  function readPromptText(el) {
    if (!el) return "";
    return el.tagName === "TEXTAREA" ? el.value : el.innerText;
  }

  function writePromptText(el, newText) {
    if (!el) return;
    el.focus();
    if (el.tagName === "TEXTAREA") {
      el.value = newText;
      el.dispatchEvent(new Event("input", { bubbles: true }));
    } else {
      el.innerText = newText;
      el.dispatchEvent(new InputEvent("input", { bubbles: true, data: newText }));
    }
  }

  function injectButton() {
    if (document.getElementById(BUTTON_ID)) return;
    const box = getPromptBox();
    if (!box || !box.parentElement) return;

    const btn = document.createElement("button");
    btn.id = BUTTON_ID;
    btn.type = "button";
    btn.textContent = "Optimizar con Prompt Lab";
    Object.assign(btn.style, {
      marginTop: "8px",
      padding: "6px 14px",
      borderRadius: "999px",
      border: "1px solid rgba(139, 92, 246, 0.55)",
      background: "linear-gradient(135deg, #2563eb, #7c3aed)",
      color: "#ffffff",
      fontSize: "12px",
      fontWeight: "600",
      cursor: "pointer",
      boxShadow: "0 4px 14px rgba(59, 130, 246, 0.25)"
    });

    btn.addEventListener("click", () => {
      const target = getPromptBox();
      const raw = readPromptText(target);
      if (!raw.trim()) return;

      const analysis = window.PromptLabOptimizer.analyze(raw);
      const optimized = window.PromptLabOptimizer.optimize(raw);
      writePromptText(target, optimized);

      btn.textContent = `Optimizado (${analysis.score}/10 -> 10/10)`;
      setTimeout(() => {
        btn.textContent = "Optimizar con Prompt Lab";
      }, 2400);
    });

    box.parentElement.appendChild(btn);
  }

  const observer = new MutationObserver(() => injectButton());
  observer.observe(document.body, { childList: true, subtree: true });
  injectButton();
})();
