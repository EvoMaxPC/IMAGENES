import json
import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "tokens.json"), "r", encoding="utf-8") as f:
    TOKENS = json.load(f)

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_MONO_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def fnt(path, size):
    return ImageFont.truetype(path, size)

def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

W, H = 1920, 1080
BG = hex_rgb(TOKENS["palette"]["primary"]["deep_black"]["hex"])
SURF = hex_rgb(TOKENS["palette"]["primary"]["graphite"]["hex"])
ELEV = hex_rgb(TOKENS["palette"]["primary"]["graphite_elevated"]["hex"])
WHITE = hex_rgb(TOKENS["palette"]["primary"]["white"]["hex"])
YELLOW = hex_rgb(TOKENS["palette"]["primary"]["evo_yellow"]["hex"])
CYAN = hex_rgb(TOKENS["palette"]["primary"]["tech_cyan"]["hex"])
GREEN = hex_rgb(TOKENS["palette"]["functional"]["success_green"]["hex"])
RED = hex_rgb(TOKENS["palette"]["functional"]["error_red"]["hex"])
GRAY = hex_rgb(TOKENS["palette"]["functional"]["secondary_gray"]["hex"])
BORDER = hex_rgb(TOKENS["palette"]["functional"]["border_subtle"]["hex"])

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Subtle laboratory precision dot-grid (every 40px, ultra low contrast)
for gx in range(40, W, 40):
    for gy in range(40, H, 40):
        d.point((gx, gy), fill=(26, 32, 42))

# Top Header Bar
d.rounded_rectangle([64, 42, W - 64, 152], radius=14, fill=SURF, outline=BORDER, width=2)
# Yellow EVO accent bar on left of header
d.rounded_rectangle([64, 42, 74, 152], radius=4, fill=YELLOW)

d.text((98, 60), "EVO LABS", font=fnt(FONT_BOLD, 34), fill=WHITE)
d.text((290, 66), "·  SISTEMA DE PRODUCCIÓN AUDIOVISUAL", font=fnt(FONT_MONO_BOLD, 20), fill=CYAN)
d.text((98, 108), f"{TOKENS['brand']['slogan']}   |   {TOKENS['brand']['manifesto']}", font=fnt(FONT_REG, 18), fill=GRAY)

# Stage 1 badge top-right
d.rounded_rectangle([W - 468, 62, W - 88, 132], radius=10, fill=ELEV, outline=YELLOW, width=2)
d.text((W - 446, 74), "ETAPA 1 · VALIDACIÓN", font=fnt(FONT_MONO_BOLD, 15), fill=YELLOW)
d.text((W - 446, 98), "Dirección de Arte & Lenguaje Visual", font=fnt(FONT_BOLD, 15), fill=WHITE)

# ---------------- ROW 1: PALETTES & DEPTH ----------------
# Panel 1: Paleta Principal (Left)
p1 = [64, 176, 1180, 560]
d.rounded_rectangle(p1, radius=14, fill=SURF, outline=BORDER, width=2)
d.text((90, 198), "01 · PALETA PRINCIPAL", font=fnt(FONT_MONO_BOLD, 18), fill=YELLOW)
d.text((340, 199), "Jerarquía estricta · Cero neones gratuitos", font=fnt(FONT_REG, 16), fill=GRAY)

prim_items = [
    ("NEGRO PROFUNDO", TOKENS["palette"]["primary"]["deep_black"]["hex"], "Fondo base del laboratorio", WHITE),
    ("GRAFITO", TOKENS["palette"]["primary"]["graphite"]["hex"], "Superficies, paneles y código", WHITE),
    ("BLANCO", TOKENS["palette"]["primary"]["white"]["hex"], "Lectura principal y métricas", BG),
    ("AMARILLO EVO", TOKENS["palette"]["primary"]["evo_yellow"]["hex"], "Conceptos clave e identidad", BG),
    ("CIAN TECH", TOKENS["palette"]["primary"]["tech_cyan"]["hex"], "Interfaces, datos y diagramas", BG),
]

sx = 90
sw = 202
gap = 16
for idx, (label, hx, desc, fg_in) in enumerate(prim_items):
    x0 = sx + idx * (sw + gap)
    y0 = 240
    # Swatch card
    d.rounded_rectangle([x0, y0, x0 + sw, y0 + 290], radius=12, fill=ELEV, outline=BORDER, width=1)
    # Color block
    col = hex_rgb(hx)
    outline_col = BORDER if hx in ("#080A0D", "#15191F") else col
    d.rounded_rectangle([x0 + 12, y0 + 12, x0 + sw - 12, y0 + 148], radius=10, fill=col, outline=outline_col, width=2)
    d.text((x0 + 24, y0 + 114), hx, font=fnt(FONT_MONO_BOLD, 18), fill=fg_in)
    # Labels
    d.text((x0 + 14, y0 + 164), label, font=fnt(FONT_BOLD, 15), fill=WHITE)
    # Wrap desc cleanly
    words = desc.split()
    line1 = " ".join(words[:3])
    line2 = " ".join(words[3:])
    d.text((x0 + 14, y0 + 194), line1, font=fnt(FONT_REG, 14), fill=GRAY)
    if line2:
        d.text((x0 + 14, y0 + 216), line2, font=fnt(FONT_REG, 14), fill=GRAY)
    # RGB tag
    rgb = hex_rgb(hx)
    d.text((x0 + 14, y0 + 252), f"RGB {rgb[0]},{rgb[1]},{rgb[2]}", font=fnt(FONT_MONO, 13), fill=CYAN)

# Panel 2: Colores Funcionales + Escala de Profundidad (Right)
p2 = [1204, 176, W - 64, 560]
d.rounded_rectangle(p2, radius=14, fill=SURF, outline=BORDER, width=2)
d.text((1230, 198), "02 · SEMÁNTICA FUNCIONAL Y CAPAS", font=fnt(FONT_MONO_BOLD, 18), fill=CYAN)

func_rows = [
    ("#10B981", "VERDE · PASS / VERIFICADO", "Resultados positivos, pruebas superadas y mejoras reales"),
    ("#EF4444", "ROJO · FAIL / ADVERTENCIA", "Errores, riesgos, regresiones e hipótesis refutadas"),
    ("#8B95A5", "GRIS · SECUNDARIO", "Metadatos, ejes, notas de versión y referencias"),
]
fy = 242
for hx, title, sub in func_rows:
    col = hex_rgb(hx)
    d.rounded_rectangle([1230, fy, W - 90, fy + 66], radius=10, fill=ELEV, outline=BORDER, width=1)
    d.rounded_rectangle([1244, fy + 13, 1284, fy + 53], radius=8, fill=col)
    d.text((1300, fy + 12), title, font=fnt(FONT_BOLD, 15), fill=col)
    d.text((1300, fy + 36), sub, font=fnt(FONT_REG, 13), fill=GRAY)
    fy += 78

# Depth ladder
d.text((1230, 486), "JERARQUÍA DE PROFUNDIDAD:", font=fnt(FONT_MONO_BOLD, 14), fill=WHITE)
layers = [("#080A0D", "L0 Base"), ("#15191F", "L1 Panel"), ("#1E242D", "L2 Activo")]
lx = 1480
for hx, lname in layers:
    d.rounded_rectangle([lx, 478, lx + 114, 536], radius=8, fill=hex_rgb(hx), outline=BORDER, width=2)
    d.text((lx + 12, 490), lname, font=fnt(FONT_BOLD, 13), fill=WHITE)
    d.text((lx + 12, 510), hx, font=fnt(FONT_MONO, 12), fill=CYAN)
    lx += 126

# ---------------- ROW 2: SHOT GRAMMAR, SAFE ZONES, RULES ----------------
# Panel 3: Gramática de Planos (Bottom-Left)
p3 = [64, 584, 916, 944]
d.rounded_rectangle(p3, radius=14, fill=SURF, outline=BORDER, width=2)
d.text((90, 606), "03 · GRAMÁTICA DE PLANOS (COMPOSICIÓN)", font=fnt(FONT_MONO_BOLD, 18), fill=YELLOW)

shots = [
    ("S1 · PANTALLA REAL", "100% captura de app/terminal + pill discreto", "full"),
    ("S2 · ZOOM INTENCIONAL", "Crop 115-160% + entorno dim 55% + foco cian", "zoom"),
    ("S3 · DIVISIÓN 62 / 38", "Evidencia activa (izq) + panel datos (der)", "split"),
    ("S4 · PRUEBA A / B", "Antes (#EF4444) vs Después (#10B981) medido", "ab"),
]
for i, (stitle, sdesc, mode) in enumerate(shots):
    col_i = i % 2
    row_i = i // 2
    bx = 90 + col_i * 402
    by = 646 + row_i * 142
    bw, bh = 386, 126
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=10, fill=ELEV, outline=BORDER, width=1)
    # Mini wireframe 16:9 (112x64)
    wx, wy, ww, wh = bx + 14, by + 16, 128, 72
    d.rounded_rectangle([wx, wy, wx + ww, wy + wh], radius=6, fill=BG, outline=GRAY, width=1)
    if mode == "full":
        d.rounded_rectangle([wx + 6, wy + 6, wx + ww - 6, wy + wh - 6], radius=4, fill=(18, 28, 38), outline=CYAN, width=1)
        d.rounded_rectangle([wx + 10, wy + 10, wx + 46, wy + 20], radius=3, fill=YELLOW)
    elif mode == "zoom":
        d.rounded_rectangle([wx + 6, wy + 6, wx + ww - 6, wy + wh - 6], radius=4, fill=(12, 14, 18))
        d.rounded_rectangle([wx + 28, wy + 18, wx + 100, wy + 56], radius=4, fill=(16, 42, 56), outline=CYAN, width=2)
    elif mode == "split":
        d.rounded_rectangle([wx + 6, wy + 6, wx + 76, wy + wh - 6], radius=4, fill=(18, 28, 38), outline=CYAN, width=1)
        d.rounded_rectangle([wx + 82, wy + 6, wx + ww - 6, wy + wh - 6], radius=4, fill=SURF, outline=YELLOW, width=1)
    elif mode == "ab":
        d.rounded_rectangle([wx + 6, wy + 6, wx + 61, wy + wh - 6], radius=4, fill=(42, 18, 22), outline=RED, width=1)
        d.rounded_rectangle([wx + 67, wy + 6, wx + ww - 6, wy + wh - 6], radius=4, fill=(14, 40, 32), outline=GREEN, width=1)

    d.text((bx + 156, by + 18), stitle, font=fnt(FONT_BOLD, 14), fill=WHITE)
    words = sdesc.split()
    mid = len(words) // 2 + 1
    d.text((bx + 156, by + 46), " ".join(words[:mid]), font=fnt(FONT_REG, 13), fill=GRAY)
    d.text((bx + 156, by + 66), " ".join(words[mid:]), font=fnt(FONT_REG, 13), fill=GRAY)
    d.text((bx + 14, by + 98), f"REGISTRO: {mode.upper()}", font=fnt(FONT_MONO, 12), fill=CYAN)

# Panel 4: Zonas Seguras 16:9 & 9:16 (Bottom-Center)
p4 = [940, 584, 1380, 944]
d.rounded_rectangle(p4, radius=14, fill=SURF, outline=BORDER, width=2)
d.text((964, 606), "04 · FORMATOS Y ZONAS SEGURAS", font=fnt(FONT_MONO_BOLD, 18), fill=CYAN)

# 16:9 wireframe
d.text((964, 646), "16:9 · 1920×1080 (30/60 fps)", font=fnt(FONT_BOLD, 13), fill=WHITE)
fx, fy, fw, fh = 964, 672, 240, 135
d.rectangle([fx, fy, fx + fw, fy + fh], fill=BG, outline=GRAY, width=1)
# Safe area
d.rectangle([fx + 10, fy + 8, fx + fw - 10, fy + fh - 12], outline=CYAN, width=1)
d.text((fx + 22, fy + 56), "SAFE 16:9\n84px / 64px / 96px", font=fnt(FONT_MONO, 12), fill=CYAN)

# 9:16 wireframe
d.text((1236, 646), "Shorts 9:16", font=fnt(FONT_BOLD, 13), fill=WHITE)
sx0, sy0, sw0, sh0 = 1236, 672, 108, 192
d.rectangle([sx0, sy0, sx0 + sw0, sy0 + sh0], fill=BG, outline=GRAY, width=1)
d.rectangle([sx0 + 7, sy0 + 22, sx0 + sw0 - 15, sy0 + sh0 - 38], outline=YELLOW, width=1)
d.text((sx0 + 14, sy0 + 88), "SAFE\n9:16", font=fnt(FONT_MONO, 12), fill=YELLOW)

d.text((964, 826), "Exportación Estándar:", font=fnt(FONT_BOLD, 14), fill=WHITE)
d.text((964, 852), "MP4 · H.264 · AAC · Voz -16 LUFS", font=fnt(FONT_MONO, 13), fill=GREEN)
d.text((964, 876), "True Peak <= -1 dBTP", font=fnt(FONT_MONO, 13), fill=GRAY)
d.text((964, 900), "Herramientas: OBS · Kdenlive · Audacity", font=fnt(FONT_REG, 13), fill=GRAY)

# Panel 5: Reglas DO / DON'T (Bottom-Right)
p5 = [1404, 584, W - 64, 944]
d.rounded_rectangle(p5, radius=14, fill=SURF, outline=BORDER, width=2)
d.text((1430, 606), "05 · DISCIPLINA VISUAL (DO / DON'T)", font=fnt(FONT_MONO_BOLD, 18), fill=YELLOW)

dos = [
    "✓ Capturas reales con zoom intencional",
    "✓ Máximo 2 acentos activos (#FFD400 / #00D2FF)",
    "✓ Cada gráfico mide o explica un dato",
]
donts = [
    "✗ Cero neones exagerados ni sci-fi vacío",
    "✗ Cero interfaces falsas en demos de software",
    "✗ Cero subtítulos gigantes que tapen el código",
]
ry = 650
for item in dos:
    d.rounded_rectangle([1430, ry, W - 90, ry + 36], radius=8, fill=(15, 36, 30), outline=GREEN, width=1)
    d.text((1444, ry + 9), item, font=fnt(FONT_REG, 14), fill=WHITE)
    ry += 44

ry += 10
for item in donts:
    d.rounded_rectangle([1430, ry, W - 90, ry + 36], radius=8, fill=(40, 18, 22), outline=RED, width=1)
    d.text((1444, ry + 9), item, font=fnt(FONT_REG, 14), fill=WHITE)
    ry += 44

# ---------------- BOTTOM FOOTER: 8-PHASE STORYTELLING PIPELINE ----------------
d.rounded_rectangle([64, 964, W - 64, 1038], radius=12, fill=SURF, outline=BORDER, width=2)
d.text((86, 976), "ESTRUCTURA", font=fnt(FONT_MONO_BOLD, 13), fill=GRAY)
d.text((86, 996), "8 FASES:", font=fnt(FONT_MONO_BOLD, 15), fill=YELLOW)

phases = TOKENS["storytelling_phases"]
px = 205
pw = 196
pgap = 12
for ph in phases:
    acc = hex_rgb(ph["accent"])
    d.rounded_rectangle([px, 976, px + pw, 1026], radius=8, fill=ELEV, outline=acc, width=1)
    d.text((px + 10, 982), f"0{ph['phase']}", font=fnt(FONT_MONO_BOLD, 13), fill=acc)
    d.text((px + 38, 982), ph["name"], font=fnt(FONT_BOLD, 13), fill=WHITE)
    d.text((px + 10, 1004), ph["purpose"][:24] + "…", font=fnt(FONT_REG, 11), fill=GRAY)
    px += pw + pgap

out_path = os.path.join(BASE_DIR, "art_direction_board.png")
img.save(out_path, optimize=True)
print("Saved:", out_path)
