document.addEventListener("DOMContentLoaded", () => {
  const roleInput = document.getElementById("role");
  const toneSelect = document.getElementById("tone");
  const formatSelect = document.getElementById("format");
  const constraintInput = document.getElementById("constraint");
  const statusEl = document.getElementById("status");
  const sampleInput = document.getElementById("sample");
  const previewEl = document.getElementById("preview");

  const KEYS = ["promptLabRole", "promptLabTone", "promptLabFormat", "promptLabConstraint"];

  if (typeof chrome !== "undefined" && chrome?.storage?.local) {
    chrome.storage.local.get(KEYS, (data) => {
      if (data?.promptLabRole) roleInput.value = data.promptLabRole;
      if (data?.promptLabTone) toneSelect.value = data.promptLabTone;
      if (data?.promptLabFormat) formatSelect.value = data.promptLabFormat;
      if (data?.promptLabConstraint) constraintInput.value = data.promptLabConstraint;
    });
  }

  document.getElementById("save").addEventListener("click", () => {
    const payload = {
      promptLabRole: roleInput.value.trim(),
      promptLabTone: toneSelect.value,
      promptLabFormat: formatSelect.value,
      promptLabConstraint: constraintInput.value.trim()
    };

    if (typeof chrome !== "undefined" && chrome?.storage?.local) {
      chrome.storage.local.set(payload, () => {
        statusEl.textContent = "✓ Preferencias guardadas en chrome.storage.local";
        setTimeout(() => { statusEl.textContent = ""; }, 2600);
      });
    } else {
      statusEl.textContent = "✓ Perfil validado (modo vista previa local)";
    }
  });

  document.getElementById("test").addEventListener("click", () => {
    const raw = sampleInput.value.trim() || "explicame marketing para pymes";
    const before = window.PromptLabOptimizer.analyze(raw);
    const optimized = window.PromptLabOptimizer.optimize(raw, {
      role: roleInput.value,
      tone: toneSelect.value,
      format: formatSelect.value,
      constraint: constraintInput.value
    });
    const after = window.PromptLabOptimizer.analyze(optimized);
    previewEl.style.display = "block";
    previewEl.textContent = `[Score: ${before.score}/10 → ${after.score}/10]\n\n${optimized}`;
  });
});
