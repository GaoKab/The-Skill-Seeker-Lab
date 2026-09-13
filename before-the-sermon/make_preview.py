#!/usr/bin/env python3
"""Build dist/PREVIEW.png — a contact sheet of the cover and key spreads."""
import os
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")
INT = os.path.join(DIST, "before-the-sermon_interior_6x9_128pp.pdf")
COV = os.path.join(DIST, "before-the-sermon_cover_6x9_128pp.pdf")

PAGES = [(3, "Title"), (7, "What this notebook is"),
         (8, "What makes it different"), (9, "Three movements"),
         (10, "Before you begin"), (11, "Readings index"),
         (13, "How to use a spread"), (14, "Spread, left"),
         (15, "Spread, right"), (118, "Passages I keep returning to"),
         (119, "Questions I still carry"), (120, "Sitting longer"),
         (127, "About")]
DPI, COLS, PAD, BG = 88, 4, 26, (246, 245, 242)


def main():
    cov = pymupdf.open(COV)[0].get_pixmap(dpi=DPI)
    cover = Image.frombytes("RGB", (cov.width, cov.height), cov.samples)

    doc = pymupdf.open(INT)
    thumbs = []
    for n, _ in PAGES:
        px = doc[n - 1].get_pixmap(dpi=DPI)
        thumbs.append(Image.frombytes("RGB", (px.width, px.height), px.samples))

    tw, th = thumbs[0].size
    rows = (len(thumbs) + COLS - 1) // COLS
    cw = COLS * tw + (COLS + 1) * PAD
    cover = cover.resize((cw - 2 * PAD,
                          round(cover.height * (cw - 2 * PAD) / cover.width)))
    sheet = Image.new("RGB", (cw, cover.height + rows * th +
                              (rows + 2) * PAD), BG)
    sheet.paste(cover, (PAD, PAD))
    y0 = cover.height + 2 * PAD
    for i, im in enumerate(thumbs):
        r, c = divmod(i, COLS)
        sheet.paste(im, (PAD + c * (tw + PAD), y0 + r * (th + PAD)))
    out = os.path.join(DIST, "PREVIEW.png")
    sheet.save(out, optimize=True)
    print("wrote", out, sheet.size)


if __name__ == "__main__":
    main()
