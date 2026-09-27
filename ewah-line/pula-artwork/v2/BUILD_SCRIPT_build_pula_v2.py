#!/usr/bin/env python3
"""Build PULA / RAIN OBJECTS production artwork v2.

Fixes the two blockers in v1:
  1. All type converted to filled outline paths (no live <text>, no Arial dependency).
     Typeface: Liberation Sans Bold, SIL Open Font Licence, commercial use permitted.
  2. Rain replaced with the 75-thread asymmetric system from rain-line-system-v1.svg,
     with strokes expanded to filled paths.
Also: puff element isolated on its own file; separation colour convention stated.
"""
import math, os, re, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
RAIN_SRC = "/home/user/The-Skill-Seeker-Lab/ewah-line/pula-artwork/rain-line-system-v1.svg"
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 1600           # 12 x 16 in at 100 units/inch
NAVY   = "#0E2745"
BOTSBLUE = "#58A9E1"
INK    = "#111111"
WHITE  = "#FFFFFF"
SEP    = "#000000"          # separation convention: every separation is black on transparent

_font = TTFont(FONT)
_gs = _font.getGlyphSet()
_cmap = _font.getBestCmap()
_upm = _font["head"].unitsPerEm
_hmtx = _font["hmtx"]


def _adv(ch):
    gn = _cmap.get(ord(ch))
    return _hmtx[gn][0] if gn else _upm // 2


def text_width(s, size, tracking=0.0):
    """Advance width in SVG units. tracking is in SVG units per gap."""
    if not s:
        return 0.0
    w = sum(_adv(c) for c in s) * size / _upm
    return w + tracking * (len(s) - 1)


def text_paths(s, size, x, y, tracking=0.0, anchor="start"):
    """Return list of SVG path 'd' strings, glyphs outlined, baseline at y."""
    total = text_width(s, size, tracking)
    if anchor == "middle":
        x -= total / 2.0
    elif anchor == "end":
        x -= total
    out, pen_x = [], x
    k = size / _upm
    for ch in s:
        gn = _cmap.get(ord(ch))
        if gn and ch != " ":
            spen = SVGPathPen(_gs)
            # font units are y-up; flip and place baseline at y
            tpen = TransformPen(spen, (k, 0, 0, -k, pen_x, y))
            _gs[gn].draw(tpen)
            d = spen.getCommands()
            if d.strip():
                out.append(d)
        pen_x += _adv(ch) * k + tracking
    return out


def capsule(x1, y1, x2, y2, w):
    """Stroke with round caps -> filled path (a capsule)."""
    r = w / 2.0
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    if L == 0:
        return (f"M {x1-r:.3f} {y1:.3f} A {r:.3f} {r:.3f} 0 1 1 {x1+r:.3f} {y1:.3f} "
                f"A {r:.3f} {r:.3f} 0 1 1 {x1-r:.3f} {y1:.3f} Z")
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux                      # left normal
    ax, ay = x1 + nx * r, y1 + ny * r
    bx, by = x2 + nx * r, y2 + ny * r
    cx, cy = x2 - nx * r, y2 - ny * r
    dx2, dy2 = x1 - nx * r, y1 - ny * r
    return (f"M {ax:.3f} {ay:.3f} L {bx:.3f} {by:.3f} "
            f"A {r:.3f} {r:.3f} 0 0 1 {cx:.3f} {cy:.3f} L {dx2:.3f} {dy2:.3f} "
            f"A {r:.3f} {r:.3f} 0 0 1 {ax:.3f} {ay:.3f} Z")


# ---- load and scale the approved rain system -------------------------------
src = open(RAIN_SRC).read()
SCALE = W / 305.0                          # uniform: 305mm artboard -> 1200 units


def layer_lines(layer_id):
    m = re.search(rf'<g id="{layer_id}".*?>(.*?)</g>', src, re.S)
    if not m:
        return []
    rows = []
    for ln in re.findall(r"<line\b[^>]*/>", m.group(1)):
        g = lambda a: float(re.search(rf'{a}="([-\d.]+)"', ln).group(1))
        sw = re.search(r'stroke-width="([\d.]+)"', ln)
        rows.append((g("x1") * SCALE, g("y1") * SCALE, g("x2") * SCALE, g("y2") * SCALE,
                     (float(sw.group(1)) if sw else 0.5) * SCALE))
    return rows


rain_main = layer_lines("RAIN_MAIN")
rain_refl = layer_lines("RAIN_REFLECTIVE")
assert rain_main and rain_refl, "rain source did not parse"


def svg(title, body, desc=""):
    d = f"\n  <desc>{desc}</desc>" if desc else ""
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="12in" height="16in" '
            f'viewBox="0 0 {W} {H}" version="1.1">\n'
            f'  <title>{title}</title>{d}\n{body}\n</svg>\n')


def paths(ds, fill, indent="  "):
    return "\n".join(f'{indent}<path fill="{fill}" d="{d}"/>' for d in ds)


files = {}

# ---- 01 HERO FRONT: PULA vertical, PUFF separation -------------------------
pula_glyphs = []
SZ = 200
for i, ch in enumerate("PULA"):
    pula_glyphs += text_paths(ch, SZ, 255, 330 + i * 190, anchor="middle")
files["PULA_V2_01_HERO_FRONT_PUFF_PULA.svg"] = svg(
    "Hero front - PULA - PUFF separation",
    paths(pula_glyphs, SEP),
    "3D PUFF SCREEN. This file is the puff separation only. Black on transparent is the "
    "separation convention: black marks where ink goes, it is not the ink colour. "
    "Type outlined, Liberation Sans Bold, SIL OFL.")

# ---- 02 HERO FRONT: rule + A ene placeholder -------------------------------
rule = capsule(183, 1060, 327, 1060, 8)
files["PULA_V2_02_HERO_FRONT_RULE.svg"] = svg(
    "Hero front - divider rule - standard ink",
    paths([rule], SEP),
    "Standard ink separation. The short rule sitting under PULA. "
    "A ene!! is NOT in this file, see the placeholder file.")

# ---- 03 HERO BACK: type ----------------------------------------------------
# Layout rule: the rain occupies x 705-1132. Type is LEFT-ALIGNED at x=LEFT and must
# finish before RAIN_X0 - GUTTER. Left-aligned reads as a deliberate asymmetric
# composition; slightly-off-centre reads as a printing error.
LEFT, RAIN_X0, GUTTER = 140.0, 705.0, 70.0
LINES = [("1966", 130, 9, 300.0),
         ("INDEPENDENCE LIVES ON", 33, 2.8, 402.0),
         ("FATSHE LENO", 56, 8.0, 566.0)]
back = []
for txt, size, tr, base in LINES:
    w = text_width(txt, size, tr)
    assert LEFT + w <= RAIN_X0 - GUTTER, (
        f"{txt!r} runs to {LEFT+w:.0f}, collides with rain at {RAIN_X0} "
        f"(needs to end by {RAIN_X0-GUTTER:.0f})")
    back += text_paths(txt, size, LEFT, base, tracking=tr, anchor="start")
    print(f"    back type {txt!r:26s} x {LEFT:.0f}-{LEFT+w:.0f}  gutter {RAIN_X0-(LEFT+w):.0f}")
files["PULA_V2_03_HERO_BACK_TYPE.svg"] = svg(
    "Hero back - type - standard ink separation",
    paths(back, SEP),
    "Standard ink separation. 1966 / INDEPENDENCE LIVES ON / FATSHE LENO. "
    "All type outlined, Liberation Sans Bold, SIL OFL. FATSHE LENO is the opening of "
    "Botswana's national anthem: spelling and spacing must not be altered by anyone.")

# ---- 04 HERO BACK: divider rule (Botswana blue) ----------------------------
files["PULA_V2_04_HERO_BACK_DIVIDER.svg"] = svg(
    "Hero back - divider rule - Botswana blue separation",
    paths([capsule(LEFT, 470, LEFT+130, 470, 8)], SEP),
    "Separate screen, Botswana blue. Match to the approved Pantone; the hex in the "
    "composite files is a screen reference only.")

# ---- 05/06 RAIN ------------------------------------------------------------
files["PULA_V2_05_RAIN_STANDARD.svg"] = svg(
    f"Rain - standard ink separation - {len(rain_main)} threads",
    paths([capsule(*r) for r in rain_main], SEP),
    "Strokes expanded to filled outlines. Asymmetric clusters, varied length, varied "
    "spacing, some threads broken mid-fall, per tech pack v1.")
files["PULA_V2_06_RAIN_REFLECTIVE.svg"] = svg(
    f"Rain - reflective separation - {len(rain_refl)} threads",
    paths([capsule(*r) for r in rain_refl], SEP),
    "Reflective ink screen. Selective by design: only these threads are reflective.")

# ---- 07 COORDINATES --------------------------------------------------------
coords = text_paths("22.3285° S   24.6849° E", 58, 600, 430, tracking=3.2, anchor="middle")
files["PULA_V2_07_COORD_BACK_TEXT.svg"] = svg(
    "Coordinates back - standard ink separation",
    paths(coords, SEP),
    "UNVERIFIED CONTENT. Confirm the coordinates are the intended location before "
    "any screen is burned. Type outlined, Liberation Sans Bold.")

# ---- 08/09 COMPOSITES (reference only) -------------------------------------
files["PULA_V2_08_HERO_FRONT_COMPOSITE.svg"] = svg(
    "Hero front - COMPOSITE - reference only, do not print from this file",
    paths(pula_glyphs, NAVY) + "\n" + paths([rule], INK) +
    f'\n  <rect x="150" y="1100" width="210" height="90" fill="none" stroke="{BOTSBLUE}" '
    f'stroke-width="3" stroke-dasharray="10 8"/>'
    f'\n  <text x="255" y="1152" fill="{BOTSBLUE}" font-size="26" font-family="sans-serif" '
    f'text-anchor="middle">A ene!! TO COME</text>',
    "REFERENCE ONLY. Shows placement and colour intent. The dashed box marks where the "
    "hand-lettered A ene!! goes and is not artwork.")

files["PULA_V2_09_HERO_BACK_COMPOSITE.svg"] = svg(
    "Hero back - COMPOSITE - reference only, do not print from this file",
    f'  <rect x="0" y="0" width="{W}" height="{H}" fill="{NAVY}"/>\n' +
    paths([capsule(*r) for r in rain_main], BOTSBLUE) + "\n" +
    paths([capsule(*r) for r in rain_refl], WHITE) + "\n" +
    paths(back, WHITE) + "\n" + paths([capsule(LEFT, 470, LEFT+130, 470, 8)], BOTSBLUE),
    "REFERENCE ONLY, on a navy ground to show how the composition reads. "
    "Print from the separation files, never from this one.")

# ---- 10 A ENE placeholder --------------------------------------------------
files["PULA_V2_10_A_ENE_PLACEHOLDER_DO_NOT_PRINT.svg"] = svg(
    "A ene!! - PLACEHOLDER - DO NOT PRINT",
    f'  <rect x="150" y="1090" width="210" height="100" fill="none" stroke="#CC0000" '
    f'stroke-width="4" stroke-dasharray="12 8"/>\n'
    f'  <text x="255" y="1132" fill="#CC0000" font-size="28" font-family="sans-serif" '
    f'text-anchor="middle">A ene!!</text>\n'
    f'  <text x="255" y="1168" fill="#CC0000" font-size="18" font-family="sans-serif" '
    f'text-anchor="middle">PLACEHOLDER - NOT ARTWORK</text>',
    "This element is NOT production artwork. A ene!! is specified as hand-lettered or "
    "script. It must be drawn or set in a licensed script face and outlined before "
    "any screen is burned. The box shows position and approximate size only.")

for name, content in files.items():
    open(os.path.join(OUT, name), "w").write(content)

print(f"wrote {len(files)} files to {OUT}")
print(f"rain: {len(rain_main)} standard + {len(rain_refl)} reflective = "
      f"{len(rain_main)+len(rain_refl)} threads")
print(f"scale: 305mm -> {W} units ({SCALE:.5f}x)")
for n in sorted(files):
    s = files[n]
    print(f"  {n:52s} paths={s.count('<path'):4d}  live_text={s.count('<text')}")
