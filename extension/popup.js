document.addEventListener("DOMContentLoaded", () => {
  const roleInput = document.getElementById("role");
  const toneSelect = document.getElementById("tone");
  const statusEl = document.getElementById("status");

  chrome.storage?.local.get(["promptLabRole", "promptLabTone"], (data) => {
    if (data?.promptLabRole) roleInput.value = data.promptLabRole;
    if (data?.promptLabTone) toneSelect.value = data.promptLabTone;
  });

  document.getElementById("save").addEventListener("click", () => {
    chrome.storage?.local.set(
      { promptLabRole: roleInput.value, promptLabTone: toneSelect.value },
      () => {
        statusEl.textContent = "Preferencias guardadas en almacenamiento local.";
      }
    );
  });
});
