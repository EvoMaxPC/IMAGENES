// Motor local de optimización de prompts (sin APIs externas)
window.PromptLabOptimizer = {
  analyze(rawText) {
    const text = (rawText || "").trim();
    const lower = text.toLowerCase();
    const issues = [];
    let score = 10;

    if (text.length < 25) {
      issues.push("Objetivo demasiado corto o ambiguo");
      score -= 2;
    }
    if (!/(actúa como|eres un|como experto|rol:|persona:)/i.test(lower)) {
      issues.push("Falta definir el rol de la IA");
      score -= 2;
    }
    if (!/(contexto|para una|empresa|proyecto|audiencia|público|pymes|principiantes)/i.test(lower)) {
      issues.push("Contexto o público objetivo insuficiente");
      score -= 2;
    }
    if (!/(evita|sin |no uses|máximo|límite|restricci)/i.test(lower)) {
      issues.push("Faltan restricciones claras");
      score -= 2;
    }
    if (!/(formato|lista|tabla|pasos|markdown|json|secciones|bullets)/i.test(lower)) {
      issues.push("Formato de salida no especificado");
      score -= 2;
    }

    return { score: Math.max(1, score), issues };
  },

  optimize(rawText, options = {}) {
    const clean = (rawText || "").trim();
    if (!clean) return "";

    const role = options.role || "Consultor senior especialista en el tema solicitado";
    const tone = options.tone || "Claro, práctico y profesional";
    const format = options.format || "Lista estructurada por secciones con ejemplos accionables";

    return [
      `Rol: Actúa como ${role}.`,
      `Objetivo: ${clean}`,
      `Contexto y audiencia: Adapta la explicación para un lector que busca aplicación real inmediata, evitando teoría innecesaria.`,
      `Restricciones: Sé preciso, evita rellenos genéricos, incluye al menos 2 ejemplos concretos y verifica coherencia paso a paso.`,
      `Formato y tono: Responde en español usando ${format}, con un tono ${tone}.`
    ].join("\n\n");
  }
};
