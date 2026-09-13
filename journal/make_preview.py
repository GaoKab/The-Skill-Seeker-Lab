#!/usr/bin/env python3
"""Build dist/PREVIEW.png — a contact sheet of the cover and key spreads."""
import os
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")
INT = os.path.join(DIST, "skill-seeker-journal_interior_6x9_128pp.pdf")
COV = os.path.join(DIST, "skill-seeker-journal_cover_6x9_128pp.pdf")

PAGES = [(3, "Title"), (7, "How to use it"), (8, "The SEEK loop"),
         (11, "Skill selection lab"), (13, "Skill charter"),
         (15, "The twelve-week map"), (17, "Week brief"),
         (19, "Daily lab × 72"), (24, "Week debrief"),
         (113, "Twelve-week debrief"), (115, "Evidence ledger"),
         (126, "Your next twelve weeks")]
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
