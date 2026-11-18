# EVO LABS — ETAPA 1: Dirección de Arte y Lenguaje Visual

> **Eslogan:** NO LO CREAS. COMPRUÉBALO.  
> **Manifiesto:** HACEMOS MILAGROS, PERO LOS MEDIMOS.  
> **Regla fundamental:** TU PC NO ES MAGIA. ES UN SISTEMA. Y TODO SISTEMA DEJA PISTAS.  
> **Principio editorial:** INVESTIGAMOS. CONSTRUIMOS. EXPERIMENTAMOS. MEDIMOS. COMPROBAMOS.

---

## 1. Propósito del Sistema Visual
EVO LABS no es un canal genérico de noticias tech, ni un formato gamer con neones saturados, ni una plantilla automatizada de videos IA. Cada frame debe transmitir **un laboratorio independiente de ingeniería y experimentación**: sobrio, preciso, verificable, didáctico y cercano.

Toda decisión estética en este documento queda formalizada en `tokens.json` y renderizada en `art_direction_board.png` para su validación antes de avanzar a la Etapa 2.

---

## 2. Análisis de Referencia de Calidad (Ale Javi Rivera -> Lenguaje Original EVO LABS)
De la referencia de nivel (`@alejavirivera`) se adoptan **principios comunicativos**, nunca diseños ni identidad gráfica:

| Principio de nivel observado | Cómo se traduce originalmente en EVO LABS |
|---|---|
| Claridad explicativa directa sin rodeos | Ir al problema/experimento en los primeros 15s; cada plano responde una pregunta técnica concreta. |
| Demostración real de herramientas | Prioridad absoluta a capturas reales (IDE, terminal, navegador, métricas) con zoom funcional, nunca mockups falsos. |
| Ritmo dinámico pero comprensible | Cortes limpios en pausas reales, cambios de plano solo cuando aportan información nueva. |
| Atractivo visual limpio y moderno | Profundidad en capas oscuras (`#080A0D` / `#15191F`), contraste alto (`#F5F7FA`) y dos acentos estrictos (`#FFD400` y `#00D2FF`). |
| Cercanía y credibilidad | Mostrar errores reales, hipótesis que fallan y mediciones antes/después verificables. |

---

## 3. Dirección de Arte y Semántica de Color

### Paleta Principal (`tokens.json -> palette.primary`)
- **Negro profundo (`#080A0D`)**: Fondo base del laboratorio. Evita el negro puro `#000000` plano y da profundidad limpia.
- **Grafito (`#15191F`)** y **Grafito elevado (`#1E242D`)**: Tarjetas de evidencia, bloques de código, paneles laterales y contenedores de métricas.
- **Blanco (`#F5F7FA`)**: Tipografía principal y datos de lectura rápida. Contraste superior a `18:1` sobre `#080A0D` y `15:1` sobre `#15191F`.
- **Amarillo EVO (`#FFD400`)**: Reservado exclusivamente para **conceptos fundamentales**, palabras clave de hipótesis, etiquetas de fase crítica y sello de marca EVO LABS.
- **Cian tecnológico (`#00D2FF`)**: Reservado para **interfaces, telemetría, trazas de datos, código resaltado y diagramas técnicos**.

### Colores Funcionales (`tokens.json -> palette.functional`)
- **Verde (`#10B981`)**: Pruebas superadas, mejoras comprobadas y estados `PASS`.
- **Rojo (`#EF4444`)**: Errores, riesgos, regresiones, hipótesis refutadas y alertas `FAIL`.
- **Gris (`#8B95A5`)**: Metadatos, etiquetas secundarias, ejes de gráficos y referencias.
- **Borde estructural (`#28303D`)**: Delimitación limpia de `1px–2px` sin resplandores exagerados.

### Reglas Estrictas de Disciplina Visual
- **PROHIBIDO**: neones difusos excesivos, efectos sci-fi genéricos (hologramas vacíos, partículas aleatorias sin sentido), saturación de paneles decorativos o interfaces ficticias cuando se demuestra software real.
- **OBLIGATORIO**: cada elemento gráfico en pantalla debe tener una función narrativa o explicativa verificable (indicar qué cambió, qué se midió o dónde mirar).

---

## 4. Lenguaje Visual y Gramática de Planos (`shot_grammar`)

El video combina 4 capas coordinadas:
1. **Narración / Presentador**: voz masculina natural, cercana y conversacional; pausas estratégicas antes de cada dato clave.
2. **Capturas reales**: aplicaciones reales, terminal, código, paneles de configuración y resultados medibles.
3. **Motion graphics funcionales**: títulos sobrios, etiquetas de experimento, diagramas de flujo, comparaciones A/B y barras de progreso.
4. **Composición en 4 planos base**:
   - `S1_FULL_REAL` (**100% Pantalla Completa Real**): ejecución en vivo y demos sin ruido visual.
   - `S2_FOCUS_ZOOM` (**Zoom Intencional 115%–160%**): oscurecimiento del entorno (`55%`) + caja de foco `#00D2FF` sobre la línea/botón exacto.
   - `S3_LAB_SPLIT` (**División 62% / 38%**): evidencia o diagrama activo a la izquierda + panel estructurado `#15191F` a la derecha.
   - `S4_AB_PROOF` (**Comparación A/B 50% / 50%**): contraste directo Antes (`#EF4444`/`#8B95A5`) vs. Después (`#10B981`/`#00D2FF`) con delta medido.

---

## 5. Zonas Seguras y Formatos (`16:9` y `9:16`)
- **YouTube Horizontal (`1920 × 1080`, 16:9)**: `30 fps` en tutoriales / `60 fps` en demos de alta fluidez. Márgenes seguros: `64px` superior, `96px` inferior (reserva para barra de progreso/controles/subtítulos discretos), `84px` laterales. Grilla de `12 columnas` con `24px` de canaleta.
- **YouTube Shorts (`1080 × 1920`, 9:16)**: `60 fps`. Márgenes seguros estrictos: `220px` superior, `380px` inferior (UI de Shorts), `72px` izquierda, `150px` derecha (botones de interacción).

---

## 6. Mapeo Visual de las 8 Fases Narrativas
1. **GANCHO** (`#FFD400`) — Resultado medido o pregunta técnica directa (`0–15s`).
2. **CONTEXTO** (`#00D2FF`) — Sistema bajo análisis y relevancia práctica.
3. **HIPÓTESIS** (`#FFD400`) — Qué esperamos comprobar o lograr.
4. **EXPERIMENTO** (`#00D2FF`) — Procedimiento real paso a paso.
5. **DEMOSTRACIÓN** (`#00D2FF`) — Ejecución real en vivo.
6. **COMPROBACIÓN** (`#10B981`) — Medición A/B, límites y errores encontrados.
7. **CONCLUSIÓN** (`#F5F7FA`) — Aprendizaje técnico verificable.
8. **IDENTIDAD EVO** (`#FFD400`) — *"No lo creas. Compruébalo."*

---

## 7. Entregables de la Etapa 1 (Verificables en este directorio)
- `evo_labs/01_art_direction/tokens.json` — Tokens exactos de color, formatos, planos y fases.
- `evo_labs/01_art_direction/render_board.py` — Generador reproducible en Python del tablero visual.
- `evo_labs/01_art_direction/art_direction_board.png` — Lámina de referencia visual `1920 × 1080` lista para validación.
