#!/usr/bin/env python3
"""
THE SKILL SEEKER JOURNAL — print-ready generator.

Builds two upload-ready PDFs for Amazon KDP (or any print shop):

    dist/skill-seeker-journal_interior_6x9_128pp.pdf   <- KDP "Manuscript"
    dist/skill-seeker-journal_cover_6x9_128pp.pdf      <- KDP "Book Cover"

Trim 6 x 9 in, 128 pages, black & white interior on white paper.
Run:  python3 journal/build_journal.py
"""

import os
from reportlab import rl_config
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

# ----------------------------------------------------------------------------
# EDIT THESE FOUR LINES AND RE-RUN — everything else follows automatically.
# ----------------------------------------------------------------------------
AUTHOR      = "The Skill Seeker Lab"   # name printed on cover, spine, title page
IMPRINT     = "The Skill Seeker Lab"   # publisher line on the copyright page
YEAR        = "2026"
ISBN        = ""                       # leave "" to use a free KDP ASIN instead

TITLE       = "THE SKILL SEEKER"
TITLE2      = "JOURNAL"
SUBTITLE    = "12 weeks. 72 guided sessions.\nOne skill you actually keep."

# ----------------------------------------------------------------------------
# Print specification
# ----------------------------------------------------------------------------
PW, PH   = 6 * inch, 9 * inch          # trim size
PAGES    = 128                          # must match what we actually emit
M_GUT    = 0.75 * inch                  # inside / gutter margin (KDP min 0.375")
M_OUT    = 0.55 * inch                  # outside margin      (KDP min 0.25")
M_TOP    = 0.62 * inch
M_BOT    = 0.66 * inch
CW       = PW - M_GUT - M_OUT           # content width  = 4.70"
CT       = PH - M_TOP                   # content top y
CB       = M_BOT                        # content bottom y

LINE_GAP = 19.0                         # handwriting line pitch (~0.264")

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")
FONTS = os.path.join(HERE, "assets", "fonts")

# ----------------------------------------------------------------------------
# Ink. Interior is grayscale only; KDP B&W presses halftone anything under 100%K,
# so nothing lighter than ~12% K and nothing between 85-99% K is used.
# ----------------------------------------------------------------------------
BLACK  = Color(0, 0, 0)
INK    = Color(0.10, 0.10, 0.10)
MID    = Color(0.42, 0.42, 0.42)
RULE   = Color(0.66, 0.66, 0.66)
HAIR   = Color(0.78, 0.78, 0.78)   # 22% K — lightest tone used

# Cover palette (full colour)
CV_BG  = HexColor("#14171F")
CV_FG  = HexColor("#F5F3EE")
CV_ACC = HexColor("#D9A441")
CV_DIM = HexColor("#8E94A3")

SERIF   = "Garamond"
SERIF_B = "Garamond-Bold"
UI      = "Inter"
UI_M    = "Inter-Med"
UI_B    = "Inter-Bold"
DISP    = "Grotesk"
DISP_B  = "Grotesk-Bold"


def register_fonts():
    """Register the OFL text faces and make one of them the canvas default,
    so no page can fall back to a non-embedded base-14 font."""
    pairs = [
        (SERIF,   "EBGaramond-Regular.ttf"),
        (SERIF_B, "EBGaramond-SemiBold.ttf"),
        (UI,      "Inter-Regular.ttf"),
        (UI_M,    "Inter-Medium.ttf"),
        (UI_B,    "Inter-SemiBold.ttf"),
        (DISP,    "SpaceGrotesk-Medium.ttf"),
        (DISP_B,  "SpaceGrotesk-Bold.ttf"),
    ]
    for name, fn in pairs:
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, fn)))
    # KDP rejects PDFs with unembedded fonts; ReportLab otherwise lists
    # Helvetica in every page's resources as the canvas base font.
    rl_config.canvas_basefontname = UI


# ----------------------------------------------------------------------------
# Page engine
# ----------------------------------------------------------------------------
class Book:
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=(PW, PH))
        self.c.setTitle(f"{TITLE} {TITLE2}")
        self.c.setAuthor(AUTHOR)
        self.c.setSubject("Guided 12-week skill-building journal")
        self.page = 0
        self.y = CT

    # -- page lifecycle ------------------------------------------------------
    def np(self, folio=True, running=""):
        """Start a new page. Odd pages are rectos (right-hand)."""
        if self.page > 0:
            self.c.showPage()
        self.page += 1
        self.y = CT
        if folio:
            self._folio(running)
        return self

    @property
    def x0(self):
        return M_GUT if self.page % 2 == 1 else M_OUT

    @property
    def x1(self):
        return self.x0 + CW

    def _folio(self, running=""):
        c = self.c
        y = M_BOT - 22
        c.setFont(UI, 6.6)
        c.setFillColor(MID)
        recto = self.page % 2 == 1
        if running:
            c.drawString(self.x0, y, running.upper()) if recto else None
            if not recto:
                c.drawRightString(self.x1, y, running.upper())
        c.setFont(UI_M, 7.4)
        c.setFillColor(MID)
        if recto:
            c.drawRightString(self.x1, y, str(self.page))
        else:
            c.drawString(self.x0, y, str(self.page))
        c.setFillColor(INK)

    def blank(self, n=1):
        for _ in range(n):
            self.np(folio=False)

    # -- primitives ----------------------------------------------------------
    def hline(self, y, x=None, w=None, color=RULE, lw=0.5):
        c = self.c
        x = self.x0 if x is None else x
        w = CW if w is None else w
        c.setStrokeColor(color)
        c.setLineWidth(lw)
        c.line(x, y, x + w, y)

    def text(self, s, y, font=UI, size=9, color=INK, align="l", x=None, w=None):
        c = self.c
        x = self.x0 if x is None else x
        w = CW if w is None else w
        c.setFont(font, size)
        c.setFillColor(color)
        if align == "l":
            c.drawString(x, y, s)
        elif align == "c":
            c.drawCentredString(x + w / 2, y, s)
        else:
            c.drawRightString(x + w, y, s)
        c.setFillColor(INK)

    def para(self, s, y, font=SERIF, size=10.5, leading=14.5, color=INK,
             x=None, w=None, align="l"):
        """Draw a wrapped paragraph. Returns the y below the last line."""
        x = self.x0 if x is None else x
        w = CW if w is None else w
        for block in s.split("\n"):
            if not block.strip():
                y -= leading * 0.6
                continue
            for ln in simpleSplit(block, font, size, w):
                self.text(ln, y, font, size, color, align, x, w)
                y -= leading
        return y

    def label(self, s, y, size=7.2, color=INK, x=None, tracking=1.25):
        """Small all-caps tracked field label."""
        c = self.c
        x = self.x0 if x is None else x
        c.setFont(UI_B, size)
        c.setFillColor(color)
        cx = x
        for ch in s.upper():
            c.drawString(cx, y, ch)
            cx += pdfmetrics.stringWidth(ch, UI_B, size) + tracking
        c.setFillColor(INK)
        return cx

    def kicker(self, s, y, size=7.2, color=MID, x=None, align="l", w=None):
        c = self.c
        x = self.x0 if x is None else x
        w = CW if w is None else w
        c.setFont(UI_B, size)
        c.setFillColor(color)
        tracking = 1.6
        total = sum(pdfmetrics.stringWidth(ch, UI_B, size) + tracking
                    for ch in s.upper()) - tracking
        if align == "c":
            cx = x + (w - total) / 2
        elif align == "r":
            cx = x + w - total
        else:
            cx = x
        for ch in s.upper():
            c.drawString(cx, y, ch)
            cx += pdfmetrics.stringWidth(ch, UI_B, size) + tracking
        c.setFillColor(INK)

    # -- composite elements --------------------------------------------------
    def page_head(self, kicker, title, sub=None, rule=True):
        """Standard section head. Leaves self.y under it."""
        y = CT
        if kicker:
            self.kicker(kicker, y, 7.4, MID)
            y -= 17
        for i, ln in enumerate(title.split("\n")):
            self.text(ln, y - 9, DISP_B, 19, INK)
            y -= 9 + 14 if i == 0 else 23
        if sub:
            y -= 6
            y = self.para(sub, y, SERIF, 10.2, 13.6, MID)
            y += 2
        if rule:
            y -= 8
            self.hline(y, color=INK, lw=1.0)
            y -= 16
        self.y = y
        return y

    def lines(self, y, n, gap=LINE_GAP, x=None, w=None, color=RULE, lw=0.5):
        x = self.x0 if x is None else x
        w = CW if w is None else w
        for i in range(n):
            y -= gap
            self.hline(y, x, w, color, lw)
        return y

    def field(self, lab, y, n=1, gap=LINE_GAP, x=None, w=None, size=7.2,
              color=INK):
        """Caps label with n writing lines under it."""
        x = self.x0 if x is None else x
        w = CW if w is None else w
        if lab:
            self.label(lab, y, size, color, x)
            y -= 6
        return self.lines(y, n, gap, x, w)

    def inline_field(self, lab, y, x, w, size=7.2):
        """Label sitting on the left of a single rule, e.g. DATE ______."""
        end = self.label(lab, y, size, INK, x)
        self.hline(y - 3.5, end + 3, w - (end + 3 - x), HAIR, 0.5)
        return y

    def boxfield(self, lab, x, y, w, h, size=7.0, fill=None, lw=0.6,
                 color=RULE):
        c = self.c
        if fill:
            c.setFillColor(fill)
            c.rect(x, y - h, w, h, stroke=0, fill=1)
        c.setStrokeColor(color)
        c.setLineWidth(lw)
        c.rect(x, y - h, w, h, stroke=1, fill=0)
        if lab:
            self.label(lab, y - 11, size, MID, x + 7)
        c.setFillColor(INK)
        return y - h

    def checkbox(self, x, y, s=8.0, lw=0.6):
        c = self.c
        c.setStrokeColor(INK)
        c.setLineWidth(lw)
        c.rect(x, y, s, s, stroke=1, fill=0)
        return x + s

    def checks(self, items, y, x=None, w=None, size=7.4, box=8.0, gap=13):
        """A row of labelled checkboxes, wrapped to width."""
        x = self.x0 if x is None else x
        w = CW if w is None else w
        cx, cy = x, y
        for it in items:
            tw = pdfmetrics.stringWidth(it, UI, size)
            need = box + 4 + tw + gap
            if cx + need - gap > x + w + 1:
                cx = x
                cy -= 16
            self.checkbox(cx, cy - box + 1.5, box)
            self.c.setFont(UI, size)
            self.c.setFillColor(INK)
            self.c.drawString(cx + box + 4, cy - box + 3.5, it)
            cx += need
        return cy - box - 2

    def scale(self, y, x, n=5, d=9.0, gap=5.0, numbered=True, size=6.2):
        """A row of numbered circles used for 1-n ratings."""
        c = self.c
        cx = x
        for i in range(1, n + 1):
            c.setStrokeColor(RULE)
            c.setLineWidth(0.6)
            c.circle(cx + d / 2, y + d / 2, d / 2, stroke=1, fill=0)
            if numbered:
                c.setFont(UI, size)
                c.setFillColor(MID)
                c.drawCentredString(cx + d / 2, y + d / 2 - size * 0.34, str(i))
            cx += d + gap
        c.setFillColor(INK)
        return cx - gap

    def dotgrid(self, x, y_top, w, h, step=14.0, r=0.45):
        c = self.c
        c.setFillColor(HAIR)
        cols = int(w // step) + 1
        rows = int(h // step) + 1
        ox = x + (w - (cols - 1) * step) / 2
        for i in range(cols):
            for j in range(rows):
                c.circle(ox + i * step, y_top - j * step, r, stroke=0, fill=1)
        c.setFillColor(INK)

    def tag(self, s, x, y, pad=5.5, h=13.0, size=6.8, fill=INK, fg=None):
        """Solid label chip, e.g. WEEK 04."""
        c = self.c
        tracking = 1.2
        wdt = sum(pdfmetrics.stringWidth(ch, UI_B, size) + tracking
                  for ch in s.upper()) - tracking
        c.setFillColor(fill)
        c.rect(x, y, wdt + pad * 2, h, stroke=0, fill=1)
        c.setFillColor(fg if fg else Color(1, 1, 1))
        cx = x + pad
        c.setFont(UI_B, size)
        for ch in s.upper():
            c.drawString(cx, y + (h - size) / 2 + 1.2, ch)
            cx += pdfmetrics.stringWidth(ch, UI_B, size) + tracking
        c.setFillColor(INK)
        return x + wdt + pad * 2

    def distribute(self, heights, y_start, y_end=None, min_gap=6.0,
                   max_gap=34.0):
        """Even vertical rhythm: return a top-y for each block."""
        y_end = CB if y_end is None else y_end
        n = len(heights)
        gap = ((y_start - y_end) - sum(heights)) / (n - 1) if n > 1 else 0.0
        gap = max(min_gap, min(max_gap, gap))
        ys, y = [], y_start
        for h in heights:
            ys.append(y)
            y -= h + gap
        return ys

    @staticmethod
    def field_h(n):
        return 6 + n * LINE_GAP

    @staticmethod
    def panel_h(n):
        return 22 + n * LINE_GAP + 7

    def panel_field(self, lab, y, n, x=None, w=None, pad=10, lw=0.9,
                    color=INK):
        """Emphasised bordered block with n writing lines. Height = panel_h(n)."""
        c = self.c
        x = self.x0 if x is None else x
        w = CW if w is None else w
        h = self.panel_h(n)
        c.setStrokeColor(color)
        c.setLineWidth(lw)
        c.rect(x, y - h, w, h, stroke=1, fill=0)
        self.label(lab, y - 14, 7.0, INK, x + pad)
        ly = y - 22
        for _ in range(n):
            ly -= LINE_GAP
            self.hline(ly, x + pad, w - 2 * pad, HAIR, 0.5)
        return y - h

    def save(self):
        self.c.showPage()
        self.c.save()


# ============================================================================
# WEEKLY HOUSE LINES — original to this journal (no third-party quotations)
# ============================================================================
WEEK_LINES = [
    "Start before you are ready. Ready is something you build, not something you wait for.",
    "The first ten attempts are tuition. Pay them quickly and stop flinching.",
    "You never find time for a skill. You take it from something else. Decide what.",
    "Confusion is not failure. It is the sound of arriving at the edge of what you know.",
    "Practise the part you avoid. That is the exact place the skill is hiding.",
    "Halfway is the quietest stretch: the novelty is gone and the mastery hasn't landed. Return anyway.",
    "Teach it badly to one person. Nothing finds a gap faster than explaining.",
    "Consistency is not intensity. It is only ever the act of coming back.",
    "You are already better than whoever opened this journal. Make the log prove it.",
    "Stop collecting resources. You have enough to reach the next level twice over.",
    "Finish something small and real. A finished small thing outranks an unfinished great one.",
    "A skill is not a finish line. It is the new floor you get to stand on.",
]

WEEK_FOCUS_HINT = [
    "Exposure \u2014 touch the real thing",
    "Fundamentals \u2014 name the parts",
    "First build \u2014 one whole thing",
    "Friction \u2014 attack what sticks",
    "Speed \u2014 the same rep, faster",
    "Depth \u2014 one layer underneath",
    "Feedback \u2014 show it to someone",
    "Repair \u2014 fix your weakest work",
    "Stretch \u2014 reach above your level",
    "Consolidate \u2014 teach and document",
    "Ship \u2014 finish one real artefact",
    "Proof \u2014 assemble the evidence",
]


# ============================================================================
# FRONT MATTER
# ============================================================================
def front_matter(b):
    c = b.c

    # ---- 1. half title (recto) --------------------------------------------
    b.np(folio=False)
    b.kicker("The Skill Seeker Lab", PH / 2 + 34, 7.6, MID, align="c")
    b.text(TITLE, PH / 2 - 2, DISP_B, 21, INK, "c")
    b.text(TITLE2, PH / 2 - 26, DISP_B, 21, INK, "c")
    c.setStrokeColor(INK); c.setLineWidth(1.0)
    c.line(PW / 2 - 26, PH / 2 - 46, PW / 2 + 26, PH / 2 - 46)

    b.blank(1)                                             # 2

    # ---- 3. title page -----------------------------------------------------
    b.np(folio=False)
    y = PH - 2.25 * inch
    b.kicker("A guided practice journal", y, 8.0, MID, align="c",
             x=M_OUT, w=PW - 2 * M_OUT)
    y -= 46
    tsize = 30.0
    while max(pdfmetrics.stringWidth(t, DISP_B, tsize)
              for t in (TITLE, TITLE2)) > PW - 2 * (M_OUT + 10) and tsize > 14:
        tsize -= 0.5
    b.text(TITLE, y, DISP_B, tsize, INK, "c", M_OUT, PW - 2 * M_OUT)
    y -= tsize * 1.2
    b.text(TITLE2, y, DISP_B, tsize, INK, "c", M_OUT, PW - 2 * M_OUT)
    y -= 26
    c.setStrokeColor(CV_ACC if False else INK); c.setLineWidth(1.2)
    c.line(PW / 2 - 34, y, PW / 2 + 34, y)
    y -= 30
    for ln in SUBTITLE.split("\n"):
        b.text(ln, y, SERIF, 12.5, MID, "c")
        y -= 17
    b.kicker(AUTHOR, 1.55 * inch, 8.0, INK, align="c",
             x=M_OUT, w=PW - 2 * M_OUT)

    # ---- 4. copyright ------------------------------------------------------
    b.np(folio=False)
    y = 3.1 * inch
    body = (
        f"{TITLE.title()} {TITLE2.title()}\n"
        f"Copyright © {YEAR} {AUTHOR}. All rights reserved.\n\n"
        "No part of this publication may be reproduced, distributed, or "
        "transmitted in any form or by any means without the prior written "
        "permission of the publisher, except for brief quotations in a "
        "review and for the purchaser's own personal, non-commercial use of "
        "the writing pages within this copy.\n\n"
        "This journal is a general self-education tool. It is not "
        "professional, medical, financial, or career advice, and no "
        "particular outcome is promised or implied. What you get out of it "
        "depends entirely on the work you put into it.\n\n"
        f"Published by {IMPRINT}."
    )
    if ISBN:
        body += f"\nISBN: {ISBN}"
    body += f"\n\nFirst edition, {YEAR}.\nPrinted on demand.\n\n"
    body += "Interior and cover set in EB Garamond, Inter and Space Grotesk."
    b.para(body, y, SERIF, 8.6, 12.0, MID, x=M_OUT, w=CW)

    # ---- 5. belongs to -----------------------------------------------------
    b.np(folio=False)
    y = PH - 2.6 * inch
    b.kicker("Property of", y, 7.6, MID, align="c")
    y -= 44
    b.hline(y, x=M_GUT + 0.25 * inch, w=CW - 0.5 * inch, color=INK, lw=0.8)
    b.text("NAME", y - 13, UI, 6.6, MID, "c", M_GUT, CW)
    y -= 62
    b.hline(y, x=M_GUT + 0.25 * inch, w=CW - 0.5 * inch, color=INK, lw=0.8)
    b.text("THE SKILL I AM BUILDING", y - 13, UI, 6.6, MID, "c", M_GUT, CW)
    y -= 62
    half = (CW - 0.5 * inch - 16) / 2
    b.hline(y, x=M_GUT + 0.25 * inch, w=half, color=INK, lw=0.8)
    b.text("STARTED", y - 13, UI, 6.6, MID, "c", M_GUT + 0.25 * inch, half)
    b.hline(y, x=M_GUT + 0.25 * inch + half + 16, w=half, color=INK, lw=0.8)
    b.text("FINISHED", y - 13, UI, 6.6, MID, "c",
           M_GUT + 0.25 * inch + half + 16, half)
    y -= 70
    b.para("If found, I would genuinely like this back:", y, SERIF, 9.5, 13,
           MID, x=M_GUT + 0.25 * inch, w=CW - 0.5 * inch, align="c")
    y -= 26
    b.hline(y, x=M_GUT + 0.25 * inch, w=CW - 0.5 * inch, color=HAIR, lw=0.5)
    y -= 24
    b.hline(y, x=M_GUT + 0.25 * inch, w=CW - 0.5 * inch, color=HAIR, lw=0.5)

    b.blank(1)                                             # 6

    # ---- 7. how to use -----------------------------------------------------
    b.np(running="How to use this journal")
    y = b.page_head("Read this once", "How to use this journal")
    y = b.para(
        "This is a working notebook, not a book you read. It runs for twelve "
        "weeks and asks for six short sessions a week — seventy-two in total. "
        "One skill. That is the whole design.", y, SERIF, 10.4, 14.2, INK)
    y -= 12
    steps = [
        ("Choose once, properly.",
         "Pages 11–14 walk you through picking a single skill and scoring "
         "it honestly. Do that section in one sitting, then stop choosing."),
        ("Sign the charter.",
         "Page 13 turns the choice into a commitment with a time, a place and "
         "an amount. Vague intentions die in week two."),
        ("Brief the week.",
         "Every week opens with a Week Brief: one focus, one rep to repeat, "
         "one obstacle plan. Two minutes on a Sunday."),
        ("Run the session, log the friction.",
         "Each Daily Lab page takes three minutes after practice. The Friction "
         "Log is the most valuable field in this journal — where you got "
         "stuck is where the skill actually lives."),
        ("Debrief and adjust.",
         "Each week closes with a Debrief: keep what worked, drop what didn't, "
         "change exactly one thing."),
        ("Bank the evidence.",
         "The Evidence Ledger at the back is the proof. Hours are not progress. "
         "Things you made are progress."),
    ]
    for i, (h, t) in enumerate(steps, 1):
        b.text(f"{i:02d}", y, DISP_B, 11.5, MID)
        b.text(h, y, UI_B, 9.3, INK, x=b.x0 + 26, w=CW - 26)
        y -= 13
        y = b.para(t, y, SERIF, 9.6, 12.8, MID, x=b.x0 + 26, w=CW - 26)
        y -= 7
    y -= 2
    b.hline(y, color=HAIR)
    y -= 16
    b.para("Miss a day? Leave the page blank and carry on. This journal is "
           "built to survive gaps — it is not built to survive quitting.",
           y, SERIF, 9.8, 13.4, INK)

    # ---- 8. the seek loop --------------------------------------------------
    b.np(running="The SEEK loop")
    y = b.page_head("The method", "The SEEK loop",
                    "Every session in this journal is one turn of the same "
                    "four-step loop. Twelve weeks is just seventy-two turns.")
    gapx, gapy = 30, 26
    box_w = (CW - gapx) / 2
    box_h = 96
    # clockwise: top-left, top-right, bottom-right, bottom-left
    cells = [
        ("S", "SELECT", "One skill, one reason, one next rep. Narrow beats "
                        "broad every single time."),
        ("E", "EXPOSE", "Make contact with the real thing early and badly. "
                        "Reading about it is not contact."),
        ("E", "EVALUATE", "Find where you broke. Name the friction out loud "
                          "and write it down."),
        ("K", "KEEP", "Keep the rep that worked, drop the rest, carry one "
                      "change into tomorrow."),
    ]
    pos = [(0, 0), (1, 0), (1, 1), (0, 1)]
    top = y
    for (letter, name, desc), (col, row) in zip(cells, pos):
        bx = b.x0 + col * (box_w + gapx)
        by = top - row * (box_h + gapy)
        c.setStrokeColor(RULE); c.setLineWidth(0.7)
        c.rect(bx, by - box_h, box_w, box_h, stroke=1, fill=0)
        c.setFillColor(INK)
        c.rect(bx, by - 24, 24, 24, stroke=0, fill=1)
        c.setFillColor(Color(1, 1, 1))
        c.setFont(DISP_B, 13)
        c.drawCentredString(bx + 12, by - 17.5, letter)
        c.setFillColor(INK)
        b.kicker(name, by - 44, 7.6, INK, x=bx + 10)
        b.para(desc, by - 59, SERIF, 9.2, 12.2, MID, x=bx + 10, w=box_w - 20)

    # clockwise arrows between the four cells
    def arrow(x1, y1, x2, y2):
        import math
        c.setStrokeColor(MID); c.setFillColor(MID); c.setLineWidth(0.8)
        a = math.atan2(y2 - y1, x2 - x1)
        c.line(x1, y1, x2 - 4.5 * math.cos(a), y2 - 4.5 * math.sin(a))
        p = c.beginPath()
        p.moveTo(x2, y2)
        p.lineTo(x2 - 6.5 * math.cos(a - 0.40), y2 - 6.5 * math.sin(a - 0.40))
        p.lineTo(x2 - 6.5 * math.cos(a + 0.40), y2 - 6.5 * math.sin(a + 0.40))
        p.close()
        c.drawPath(p, stroke=0, fill=1)
        c.setFillColor(INK)

    lcx = b.x0 + box_w / 2                    # left column centre
    rcx = b.x0 + box_w + gapx + box_w / 2     # right column centre
    ty = top - box_h / 2                      # top row centre
    byc = top - box_h - gapy - box_h / 2      # bottom row centre
    arrow(b.x0 + box_w + 6, ty, b.x0 + box_w + gapx - 6, ty)          # TL -> TR
    arrow(rcx, top - box_h - 6, rcx, top - box_h - gapy + 6)          # TR -> BR
    arrow(b.x0 + box_w + gapx - 6, byc, b.x0 + box_w + 6, byc)        # BR -> BL
    arrow(lcx, top - box_h - gapy + 6, lcx, top - box_h - 6)          # BL -> TL

    y = top - 2 * box_h - gapy - 26

    b.hline(y, color=HAIR); y -= 18
    b.kicker("What one turn looks like", y, 7.4, MID); y -= 16
    y = b.para(
        "Twenty-five minutes on a Tuesday. You SELECT one rep: "
        "\u201cwrite a function that prints the longest line in a file.\u201d "
        "You EXPOSE yourself to it by opening the editor instead of a "
        "tutorial. You EVALUATE \u2014 it broke on empty files and you don't "
        "know why. You KEEP the habit of running it after every change, and "
        "tomorrow's rep becomes \u201chandle the empty case first.\u201d\n\n"
        "That is one line in the Friction Log and one in the fix box \u2014 "
        "three minutes of writing. Seventy-two of those and you are a "
        "different practitioner.", y, SERIF, 9.8, 13.2, INK)
    note = ("Make it the Friction Log. Everything else here is scaffolding "
            "around one question: where exactly did it stop working, and "
            "what will I try next?")
    nl = len(simpleSplit(note, SERIF, 9.6, CW - 24))
    h = 30 + nl * 12.8 + 10
    box_top = CB + h
    assert box_top < y - 14, "SEEK loop callout collides with the prose"
    c.setStrokeColor(INK); c.setLineWidth(1.0)
    c.rect(b.x0, CB, CW, h, stroke=1, fill=0)
    b.kicker("If you only ever fill in one field", box_top - 17, 7.0, INK,
             x=b.x0 + 12)
    b.para(note, box_top - 34, SERIF, 9.6, 12.8, MID, x=b.x0 + 12, w=CW - 24)

    # ---- 9. five laws ------------------------------------------------------
    b.np(running="The five laws")
    y = b.page_head("Hold these", "The five laws of\nskill seeking")
    laws = [
        ("One skill at a time.",
         "Breadth is the reward for depth, never the route to it. Park the "
         "other three skills on page 11 and come back to them in April."),
        ("Reps beat research.",
         "A bad attempt teaches you more in ten minutes than a good article "
         "teaches you in an hour. Buying the course is not doing the course."),
        ("Friction is the map.",
         "The place you get stuck, avoid, or quietly skip is not an obstacle "
         "to the skill. It is the skill. Go straight at it."),
        ("Evidence over hours.",
         "Nobody was ever good at something because they sat near it for "
         "forty hours. Log what you produced, not how long you suffered."),
        ("Small and daily.",
         "Twenty protected minutes six days a week will beat four heroic "
         "hours once a fortnight, every time, without exception."),
    ]
    for i, (h, t) in enumerate(laws, 1):
        b.tag(f"Law {i:02d}", b.x0, y - 12, h=13.5)
        y -= 24
        b.text(h, y, DISP_B, 12.5, INK)
        y -= 15
        y = b.para(t, y, SERIF, 10.0, 13.4, MID)
        y -= 14
    y -= 6
    b.hline(y, color=INK, lw=0.8)
    y -= 20
    y = b.para("When a week goes wrong it is almost always because one of "
               "these five got quietly broken. Come back to this page and "
               "work out which one.", y, SERIF, 9.8, 13.2, INK)
    y -= 20
    b.kicker("The law I break most often is", y, 7.0, MID)
    b.lines(y - 8, 1)

    b.blank(1)                                             # 10


def selection_lab(b):
    c = b.c

    # ---- 11. selection lab, part 1 ----------------------------------------
    b.np(running="Skill selection lab")
    y = b.page_head("Do this first \u00b7 part one", "Skill selection lab",
                    "Twelve weeks is long enough to matter and short enough "
                    "to finish. Spend twenty minutes here so you never have "
                    "to reopen the question.")
    H = [32,                # main reason checks (2 rows)
         b.field_h(1),      # field / industry
         26 + 3 * 44,       # three skills block (A/B/C rows)
         b.field_h(2),      # what is stopping me
         32,                # constraints checks
         b.field_h(2)]      # biggest constraint plan
    ys = b.distribute(H, y, min_gap=10, max_gap=26)

    b.label("My main reason for learning something new", ys[0], 7.2)
    b.checks(["Career change", "Promotion", "Start a business",
              "Creative work", "Personal growth", "Curiosity",
              "Someone I want to help"], ys[0] - 14)

    b.field("The field or industry that pulls me most", ys[1], 1)

    yy = ys[2]
    b.label("Three skills I keep circling back to", yy, 7.2)
    b.text("Write them down so you can stop carrying them around.", yy - 11,
           SERIF, 9.2, MID)
    yy -= 26
    for letter in ("A", "B", "C"):
        b.tag(letter, b.x0, yy - 11, h=12.5, size=6.4)
        b.hline(yy - 3.5, b.x0 + 26, CW - 26, RULE, 0.6)
        yy -= 19
        end = b.label("so that I can", yy, 5.8, MID, b.x0 + 26, tracking=0.8)
        b.hline(yy - 3.5, end + 4, b.x1 - end - 4, HAIR, 0.5)
        yy -= 25

    b.field("What is actually stopping me right now", ys[3], 2)

    b.label("The honest constraints", ys[4], 7.2)
    b.checks(["Time", "Money", "Confidence", "Focus", "Access to tools",
              "Nobody to ask", "Fear of looking stupid"], ys[4] - 14)

    b.field("The biggest one is \u2014 and here is what I will do about it",
            ys[5], 2)

    # ---- 12. selection lab, part 2 ----------------------------------------
    b.np(running="Skill selection lab")
    y = b.page_head("Part two", "Score them, then choose",
                    "Score each skill 1\u20135 in all four columns and add up "
                    "the rows. The highest total is your skill. If two tie, "
                    "pick the one you are slightly afraid of.")
    H = [54,                # the four criteria
         4 * 30,            # scoring table incl. header row
         b.field_h(1),      # protected minutes
         32,                # budget checks
         58,                # the choice box
         b.field_h(2)]      # parked skills
    ys = b.distribute(H, y, min_gap=10, max_gap=24)

    yy = ys[0]
    for k in ("PULL \u2014 how much do I want this on a dull Tuesday?",
              "PAYOFF \u2014 what does having it change about my life?",
              "PROOF \u2014 can I show evidence of it within twelve weeks?",
              "PRACTICAL \u2014 do I have the time, tools and money today?"):
        yy = b.para(k, yy, SERIF, 9.2, 13.0, MID)

    # scoring table, fully boxed
    ty = ys[1]
    colw = [92] + [(CW - 92) / 5] * 5
    rowh = 30
    heads = ["", "PULL", "PAYOFF", "PROOF", "PRACT.", "TOTAL"]
    cx = b.x0
    for i, h in enumerate(heads):
        if h:
            b.kicker(h, ty - 20, 5.8, MID, x=cx, w=colw[i], align="c")
        cx += colw[i]
    c.setStrokeColor(INK); c.setLineWidth(0.9)
    c.rect(b.x0, ty - 4 * rowh, CW, 4 * rowh, stroke=1, fill=0)
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    for r in range(1, 4):
        c.line(b.x0, ty - r * rowh, b.x1, ty - r * rowh)
    cx = b.x0
    for i in range(len(colw) - 1):
        cx += colw[i]
        c.setStrokeColor(HAIR if i else RULE); c.setLineWidth(0.6)
        c.line(cx, ty, cx, ty - 4 * rowh)
    for r, nm in enumerate(("SKILL A", "SKILL B", "SKILL C"), start=1):
        b.kicker(nm, ty - r * rowh - 19, 6.4, INK, x=b.x0 + 8)

    b.field("Minutes a day I can genuinely protect \u2014 be pessimistic",
            ys[2], 1, w=CW * 0.58)

    b.label("My learning budget for the next twelve weeks", ys[3], 7.2)
    b.checks(["Free only", "Under $100", "$100\u2013$500", "$500+",
              "No limit"], ys[3] - 14)

    c.setStrokeColor(INK); c.setLineWidth(1.2)
    c.rect(b.x0, ys[4] - 58, CW, 58, stroke=1, fill=0)
    b.kicker("The skill I am choosing", ys[4] - 17, 7.2, INK, x=b.x0 + 12)
    b.hline(ys[4] - 43, b.x0 + 12, CW - 24, RULE, 0.6)

    b.field("The two I am parking until this is finished", ys[5], 2)

    # ---- 13. charter -------------------------------------------------------
    b.np(running="My skill charter")
    y = b.page_head("Sign it", "My skill charter",
                    "Intentions evaporate. Commitments with a time, a place "
                    "and a number survive. Fill in every blank.")
    H = [b.field_h(1),      # I am learning
         b.field_h(2),      # because
         b.field_h(2),      # by week twelve
         52,                # the non-negotiable
         b.field_h(1),      # first rep
         b.field_h(1),      # giving up
         b.field_h(1),      # telling
         20,                # start / end dates
         26]                # signature
    ys = b.distribute(H, y, min_gap=8, max_gap=22)

    b.field("I am learning", ys[0], 1)
    b.field("Because it will let me", ys[1], 2)
    b.field("By the end of week twelve I will have made, done or shown",
            ys[2], 2)

    yy = ys[3]
    b.kicker("The non-negotiable", yy, 7.2, MID)
    yy -= 22
    c.setFont(SERIF, 10.6); c.setFillColor(INK)
    cx = b.x0
    c.drawString(cx, yy, "I will practise")
    cx += pdfmetrics.stringWidth("I will practise ", SERIF, 10.6)
    b.hline(yy - 3, cx, 40, RULE, 0.6); cx += 46
    c.drawString(cx, yy, "minutes a day,")
    cx += pdfmetrics.stringWidth("minutes a day, ", SERIF, 10.6)
    b.hline(yy - 3, cx, 28, RULE, 0.6); cx += 34
    c.drawString(cx, yy, "days a week,")
    yy -= 24
    cx = b.x0
    c.drawString(cx, yy, "at")
    cx += pdfmetrics.stringWidth("at ", SERIF, 10.6)
    b.hline(yy - 3, cx, 86, RULE, 0.6); cx += 92
    tail = "(time), at"
    c.drawString(cx, yy, tail)
    cx += pdfmetrics.stringWidth(tail + " ", SERIF, 10.6)
    endw = pdfmetrics.stringWidth("(place).", SERIF, 10.6)
    b.hline(yy - 3, cx, b.x1 - endw - 6 - cx, RULE, 0.6)
    c.drawString(b.x1 - endw, yy, "(place).")

    b.field("My very first rep \u2014 small enough to do today", ys[4], 1)
    b.field("What I am giving up to make the room", ys[5], 1)
    b.field("Who I am telling, so that quitting is awkward", ys[6], 1)

    half = (CW - 20) / 2
    b.inline_field("Start date", ys[7], b.x0, half)
    b.inline_field("Week 12 ends", ys[7], b.x0 + half + 20, half)

    b.hline(ys[8] - 14, b.x0, half, INK, 0.8)
    b.text("SIGNED", ys[8] - 26, UI, 6.4, MID, x=b.x0)
    b.hline(ys[8] - 14, b.x0 + half + 20, half, INK, 0.8)
    b.text("DATE", ys[8] - 26, UI, 6.4, MID, x=b.x0 + half + 20)

    # ---- 14. baseline ------------------------------------------------------
    b.np(running="Baseline")
    y = b.page_head("Week zero", "Honest baseline",
                    "You cannot show progress you never measured. Be harsh "
                    "here \u2014 a low baseline is a gift to your week-twelve "
                    "self.")
    H = [28 + 6 * 26,       # six sub-skills + scale header
         b.field_h(3),      # can already do
         b.field_h(3),      # cannot do yet
         b.field_h(2),      # the lie
         b.field_h(2)]      # what good looks like
    ys = b.distribute(H, y, min_gap=10, max_gap=24)

    yy = ys[0]
    b.label("Break the skill into six parts and rate each one today", yy, 7.2)
    b.text("1 = no idea what this even means    10 = I could be paid for this",
           yy - 11, SERIF, 8.6, MID)
    yy -= 26
    scale_x = b.x0 + CW * 0.48
    cx = scale_x
    for i in range(1, 11):
        b.text(str(i), yy + 2, UI_B, 5.6, MID, "c", cx, 10.4)
        cx += 10.4 + 3.2
    yy -= 8
    for _ in range(6):
        b.hline(yy - 3.5, b.x0, CW * 0.44, RULE, 0.6)
        b.scale(yy - 6, scale_x, n=10, d=10.4, gap=3.2, numbered=False)
        yy -= 26

    b.field("What I can already do, without help", ys[1], 3)
    b.field("What I definitely cannot do yet", ys[2], 3)
    b.field("The lie I have been telling myself about this skill", ys[3], 2)
    b.field("What \u201cgood enough\u201d would honestly look like in twelve "
            "weeks", ys[4], 2)

    # ---- 15. twelve week map ----------------------------------------------
    b.np(running="The twelve-week map")
    y = b.page_head("Plan the arc", "The twelve-week map",
                    "A rough sketch beats no sketch. Pencil it in now and "
                    "change it whenever the work tells you to.")
    colw = [40, CW - 40 - 126 - 32, 126, 32]
    for i, h in enumerate(("WEEK", "FOCUS", "EVIDENCE BY SUNDAY", "DONE")):
        b.kicker(h, y + 6, 5.9, MID,
                 x=b.x0 + sum(colw[:i]) + (0 if i in (0, 3) else 5),
                 w=colw[i], align="c" if i in (0, 3) else "l")
    c.setStrokeColor(INK); c.setLineWidth(0.9)
    c.line(b.x0, y, b.x1, y)
    rowh = (y - CB - 40) / 12
    for r in range(12):
        ry = y - r * rowh
        b.text(f"{r+1:02d}", ry - rowh / 2 - 3, DISP_B, 9.0, INK, "c",
               b.x0, colw[0])
        hint = WEEK_FOCUS_HINT[r]
        b.text(hint, ry - rowh / 2 - 3, SERIF, 7.8, Color(.72, .72, .72),
               x=b.x0 + colw[0] + 5, w=colw[1] - 10)
        c.setStrokeColor(HAIR); c.setLineWidth(0.5)
        for xoff in (colw[0], colw[0] + colw[1]):
            c.line(b.x0 + xoff, ry, b.x0 + xoff, ry - rowh)
        c.line(b.x1 - colw[3], ry, b.x1 - colw[3], ry - rowh)
        b.checkbox(b.x1 - colw[3] / 2 - 4.5, ry - rowh / 2 - 4.5, 9.0)
        c.setStrokeColor(RULE); c.setLineWidth(0.5)
        c.line(b.x0, ry - rowh, b.x1, ry - rowh)
    yy = y - 12 * rowh - 18
    b.text("The grey text is a suggested arc \u2014 write straight over it.",
           yy, SERIF, 8.6, MID)

    b.blank(1)                                             # 16


# ============================================================================
# CORE — 12 weeks x 8 pages = 96 pages
# ============================================================================
def week_brief(b, w):
    c = b.c
    b.np(running=f"Week {w:02d}")
    y = CT - 15
    b.tag(f"Week {w:02d}", b.x0, y, h=15, size=7.2)
    b.kicker("of twelve", y + 4.4, 6.8, MID, x=b.x1 - 52)
    y -= 26
    b.text("Week brief", y, DISP_B, 20, INK)
    y -= 13
    b.hline(y, color=INK, lw=1.0)
    y -= 17

    epi = WEEK_LINES[w - 1]
    epi_h = len(simpleSplit(epi, SERIF, 10.2, CW)) * 13.6

    H = [epi_h,                 # house line
         20,                    # week of / to
         b.field_h(1),          # focus
         b.field_h(2),          # the rep
         b.field_h(3),          # evidence by sunday
         46,                    # sessions planned
         b.field_h(1),          # derailer
         b.field_h(3),          # plan
         b.field_h(1)]          # resource
    ys = b.distribute(H, y, min_gap=8, max_gap=24)

    b.para(epi, ys[0], SERIF, 10.2, 13.6, MID)

    half = (CW - 16) / 2
    b.inline_field("Week of", ys[1] - 8, b.x0, half)
    b.inline_field("to", ys[1] - 8, b.x0 + half + 16, half)

    b.field("This week's focus \u2014 one sentence", ys[2], 1)
    b.field("The rep I am repeating all week", ys[3], 2)
    b.field("Evidence I will hold in my hand by Sunday", ys[4], 3)

    b.label("Sessions planned", ys[5], 7.2)
    cx, by = b.x0, ys[5] - 36
    step = (CW - 22) / 7
    for dl in ("M", "T", "W", "T", "F", "S", "S"):
        c.setStrokeColor(RULE); c.setLineWidth(0.7)
        c.rect(cx, by, 22, 22, stroke=1, fill=0)
        b.text(dl, by - 10, UI, 6.6, MID, "c", cx, 22)
        cx += step

    b.field("The thing most likely to derail me this week", ys[6], 1)
    b.field("If that happens, my plan is", ys[7], 3)
    b.field("Resource I am using \u2014 course, book, person, project",
            ys[8], 1)


def daily_lab(b, w, d):
    c = b.c
    b.np(running=f"Week {w:02d}")

    # ---- header strip ------------------------------------------------------
    y = CT - 13.5
    b.tag(f"Week {w:02d}", b.x0, y, h=13.5, size=6.4)
    c.setStrokeColor(INK); c.setLineWidth(0.7)
    c.rect(b.x0 + 66, y, 42, 13.5, stroke=1, fill=0)
    b.kicker(f"Day {d}", y + 4.2, 6.4, INK, x=b.x0 + 66, w=42, align="c")
    b.inline_field("Date", y + 4.2, b.x0 + 122, CW - 122)
    y -= 12
    b.hline(y, color=INK, lw=1.0)
    y -= 18

    # ---- evenly distributed body ------------------------------------------
    H = [b.field_h(1),          # today's rep
         35,                    # session boxes
         b.field_h(6),          # what I actually did
         b.panel_h(4),          # friction log
         b.field_h(2),          # the fix
         30,                    # evidence checks
         14,                    # ratings
         b.field_h(1)]          # one line
    ys = b.distribute(H, y, min_gap=10, max_gap=22)

    b.field("Today's rep \u2014 the one thing I am practising", ys[0], 1)

    seg = (CW - 24) / 3
    for i, lab in enumerate(("Start", "End", "Total min")):
        x = b.x0 + i * (seg + 12)
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.rect(x, ys[1] - 26, seg, 26, stroke=1, fill=0)
        b.text(lab.upper(), ys[1] - 34, UI, 5.8, MID, "c", x, seg)

    b.field("What I actually did", ys[2], 6)

    b.panel_field("Friction log \u2014 exactly where I got stuck", ys[3], 4)

    b.field("The fix I will try next time", ys[4], 2)

    b.label("Evidence produced", ys[5], 7.2)
    b.checks(["Made something", "Practised", "Taught it", "Applied it",
              "Failed usefully"], ys[5] - 14, size=7.0)

    b.text("DIFFICULTY", ys[6] - 3, UI_B, 6.4, MID)
    b.scale(ys[6] - 9, b.x0 + 62, 5, 9.2, 4.6)
    b.text("FOCUS", ys[6] - 3, UI_B, 6.4, MID, x=b.x0 + CW * 0.56)
    b.scale(ys[6] - 9, b.x0 + CW * 0.56 + 34, 5, 9.2, 4.6)

    b.field("One line I do not want to forget", ys[7], 1)


def week_debrief(b, w):
    c = b.c
    b.np(running=f"Week {w:02d}")
    y = CT - 15
    b.tag(f"Week {w:02d}", b.x0, y, h=15, size=7.2)
    y -= 26
    b.text("Week debrief", y, DISP_B, 20, INK)
    y -= 13
    b.hline(y, color=INK, lw=1.0)
    y -= 18

    H = [18,                    # sessions actually run
         b.field_h(4),          # evidence produced
         b.field_h(3),          # what worked
         b.field_h(3),          # what did not
         40,                    # where I am scale
         30,                    # compared with last week
         b.panel_h(2)]          # the one change
    ys = b.distribute(H, y, min_gap=8, max_gap=26)

    b.label("Sessions I actually ran", ys[0], 7.2)
    cx = b.x1 - (6 * 16 - 4)
    for _ in range(6):
        b.checkbox(cx, ys[0] - 2.5, 12)
        cx += 16

    b.field("Evidence I produced this week \u2014 list it, no adjectives",
            ys[1], 4)
    b.field("What worked. Keep doing it.", ys[2], 3)
    b.field("What did not work. Stop doing it.", ys[3], 3)

    b.label("Where I am on this skill today", ys[4], 7.2)
    end = b.scale(ys[4] - 24, b.x0 + 2, 10, 11.0, 6.4, size=6.0)
    b.text("1  beginner", ys[4] - 36, UI, 6.0, MID)
    b.text("10  competent", ys[4] - 36, UI, 6.0, MID, "r", b.x0,
           end - b.x0)

    b.label("Compared with last week", ys[5], 7.2)
    b.checks(["Clearly ahead", "About even", "Behind", "Hard to tell"],
             ys[5] - 14)

    b.panel_field("The one change I am making next week", ys[6], 2, lw=1.1)


def core(b):
    for w in range(1, 13):
        week_brief(b, w)                  # recto
        for d in range(1, 7):
            daily_lab(b, w, d)            # 6 pages
        week_debrief(b, w)                # verso


# ============================================================================
# BACK MATTER — 16 pages
# ============================================================================
def _ledger(b, kicker, title, sub, cols, rows, running, numbered=True,
            first_head=True):
    """Generic ruled table page used by several back-matter logs."""
    c = b.c
    b.np(running=running)
    if first_head:
        y = b.page_head(kicker, title, sub)
    else:
        y = CT
        b.kicker(title.upper(), y, 7.4, MID)
        y -= 14
        b.hline(y, color=INK, lw=0.8)
        y -= 14
    widths, heads = zip(*cols)
    total = sum(widths)
    widths = [wd / total * CW for wd in widths]
    for i, h in enumerate(heads):
        if h:
            b.kicker(h, y + 6, 6.0, MID, x=b.x0 + sum(widths[:i]),
                     w=widths[i], align="l")
    c.setStrokeColor(INK); c.setLineWidth(0.8)
    c.line(b.x0, y, b.x1, y)
    rowh = (y - CB - 8) / rows
    for r in range(rows):
        ry = y - r * rowh
        cx = b.x0
        for i, wd in enumerate(widths):
            if i:
                c.setStrokeColor(HAIR); c.setLineWidth(0.5)
                c.line(cx, ry, cx, ry - rowh)
            cx += wd
        c.setStrokeColor(RULE); c.setLineWidth(0.5)
        c.line(b.x0, ry - rowh, b.x1, ry - rowh)
        if numbered:
            b.text(f"{r+1:02d}", ry - rowh / 2 - 3, UI, 6.4, HAIR,
                   x=b.x0 + 3)


def back_matter(b):
    c = b.c

    # ---- 113/114: the twelve-week debrief ---------------------------------
    b.np(running="The twelve-week debrief")
    y = b.page_head("You made it", "The twelve-week debrief",
                    "Seventy-two possible sessions ago you signed a charter "
                    "on page 13. Go and read it before you fill this in.")
    H = [b.field_h(1), b.field_h(2), b.field_h(3), b.field_h(2),
         b.field_h(2), b.field_h(3), b.field_h(3)]
    ys = b.distribute(H, y, min_gap=8, max_gap=26)
    b.field("Sessions I ran, honestly, out of seventy-two", ys[0], 1,
            w=CW * 0.4)
    b.field("Where I was in week one", ys[1], 2)
    b.field("Where I am now \u2014 in specifics, not feelings", ys[2], 3)
    b.field("The single thing that moved the needle most", ys[3], 2)
    b.field("What genuinely surprised me", ys[4], 2)
    b.field("The week it nearly fell apart, and what saved it", ys[5], 3)
    b.field("What I would tell someone starting this journal tomorrow",
            ys[6], 3)

    b.np(running="The twelve-week debrief")
    y = CT
    b.kicker("The twelve-week debrief \u00b7 continued", y, 7.4, MID)
    y -= 14
    b.hline(y, color=INK, lw=0.8)
    y -= 20
    H = [40, b.field_h(3), b.field_h(4), b.field_h(3), b.field_h(2),
         b.field_h(3)]
    ys = b.distribute(H, y, min_gap=8, max_gap=26)

    b.label("Where I am on this skill now", ys[0], 7.2)
    end = b.scale(ys[0] - 24, b.x0 + 2, 10, 11.0, 6.4, size=6.0)
    b.text("1  beginner", ys[0] - 36, UI, 6.0, MID)
    b.text("10  competent", ys[0] - 36, UI, 6.0, MID, "r", b.x0, end - b.x0)

    b.field("Against the baseline on page 14, what actually changed",
            ys[1], 3)
    b.field("What I can now do that I could not do twelve weeks ago",
            ys[2], 4)
    b.field("What is still out of reach \u2014 and whether I care", ys[3], 3)
    b.field("The piece of evidence I am proudest of", ys[4], 2)
    b.field("Do I keep going with this skill, or bank it and move on?",
            ys[5], 3)

    # ---- 115/116: evidence ledger -----------------------------------------
    _ledger(b, "The proof", "Evidence ledger",
            "Hours are not progress. This page is progress. Log every real "
            "thing you made, shipped, fixed, taught or performed.",
            [(11, ""), (22, "DATE"), (100, "WHAT I MADE OR DID"),
             (45, "WHERE IT LIVES")], 15, "Evidence ledger")
    _ledger(b, "", "Evidence ledger · continued", "",
            [(11, ""), (22, "DATE"), (100, "WHAT I MADE OR DID"),
             (45, "WHERE IT LIVES")], 20, "Evidence ledger",
            first_head=False)

    # ---- 117/118: resource log --------------------------------------------
    _ledger(b, "What I used", "Resource log",
            "Courses, books, videos, tools, people. Rate them after you "
            "finish them — and be willing to write “no” in the "
            "last column.",
            [(26, "TYPE"), (96, "NAME"), (26, "COST"), (30, "WORTH IT?")],
            15, "Resource log", numbered=False)
    _ledger(b, "", "Resource log · continued", "",
            [(26, "TYPE"), (96, "NAME"), (26, "COST"), (30, "WORTH IT?")],
            20, "Resource log", numbered=False, first_head=False)

    # ---- 119: wins ---------------------------------------------------------
    _ledger(b, "Bank them", "Wins and breakthroughs",
            "The moment something clicked, someone noticed, or a thing you "
            "could not do became a thing you could. You will forget these. "
            "Write them down.",
            [(11, ""), (24, "DATE"), (145, "WHAT HAPPENED")], 16, "Wins")

    # ---- 120: stuck -> solved ---------------------------------------------
    _ledger(b, "Pattern hunting", "Stuck → solved",
            "Pull the repeats out of your Friction Logs. The same obstacle "
            "showing up three times is not bad luck — it is the next "
            "thing to learn.",
            [(74, "WHAT I GOT STUCK ON"), (74, "HOW IT GOT UNSTUCK"),
             (24, "DATE")], 14, "Stuck to solved", numbered=False)

    # ---- 121: people -------------------------------------------------------
    b.np(running="People")
    y = b.page_head("Nobody does this alone", "People and asks",
                    "Skills travel through people faster than through "
                    "documentation. Keep a list of who helped, and a list of "
                    "what you still need to ask.")
    b.kicker("Who helped, and how", y, 6.6, MID)
    c.setStrokeColor(INK); c.setLineWidth(0.8)
    b.hline(y - 8, color=INK, lw=0.8)
    y = b.lines(y - 8, 8)
    y -= 18
    b.kicker("Questions I still need to ask someone", y, 6.6, MID)
    b.hline(y - 8, color=INK, lw=0.8)
    y -= 8
    n = int((y - CB - 6) // (LINE_GAP + 4))
    for _ in range(n):
        y -= LINE_GAP + 4
        b.checkbox(b.x0, y + 2, 8.0)
        b.hline(y, b.x0 + 14, CW - 14, RULE, 0.5)

    # ---- 122-125: notes ----------------------------------------------------
    for i in range(4):
        b.np(running="Notes")
        b.kicker("Notes", CT, 7.4, MID)
        b.hline(CT - 10, color=INK, lw=0.8)
        b.dotgrid(b.x0, CT - 32, CW, CT - 32 - CB - 4, step=14.2)

    # ---- 126: next twelve weeks -------------------------------------------
    b.np(running="Your next twelve weeks")
    y = b.page_head("Do not stop here", "Your next twelve weeks",
                    "The end of a journal is the worst possible moment to "
                    "stop. Decide the next thing while the habit is still "
                    "warm.")
    H = [48, b.field_h(2), b.field_h(2), b.field_h(3), b.field_h(3), 40]
    ys = b.distribute(H, y, min_gap=8, max_gap=28)

    b.checks(["Go deeper on the same skill", "Take skill B from page 11",
              "Combine this with something I already have",
              "Teach this skill to someone else",
              "Turn it into work that pays"], ys[0])
    b.field("Next skill, or next level of this one", ys[1], 2)
    b.field("The first rep of the next twelve weeks", ys[2], 2)
    b.field("What I am keeping from this journal that worked", ys[3], 3)
    b.field("What I am changing about how I practise", ys[4], 3)

    half = (CW - 20) / 2
    b.hline(ys[5] - 14, b.x0, half, INK, 0.8)
    b.text("SIGNED", ys[5] - 26, UI, 6.4, MID, x=b.x0)
    b.hline(ys[5] - 14, b.x0 + half + 20, half, INK, 0.8)
    b.text("DATE", ys[5] - 26, UI, 6.4, MID, x=b.x0 + half + 20)

    # ---- 127: about --------------------------------------------------------
    b.np(folio=False)
    y = PH - 2.4 * inch
    b.kicker("About", y, 7.6, MID, align="c", x=M_GUT, w=CW)
    y -= 34
    b.text("The Skill Seeker Lab", y, DISP_B, 17, INK, "c", M_GUT, CW)
    y -= 26
    c.setStrokeColor(INK); c.setLineWidth(1.0)
    c.line(PW / 2 - 22, y, PW / 2 + 22, y)
    y -= 28
    y = b.para(
        "The Skill Seeker Lab exists for one stubborn problem: most people "
        "know roughly what they want to be good at, and almost nobody has a "
        "structure for getting there.\n\n"
        "So we build structures. Short ones, with blanks in them. This "
        "journal is the paper version — twelve weeks, seventy-two "
        "sessions, one skill, and a Friction Log that tells you the truth.\n\n"
        "If it worked for you, the most useful thing you can do is tell one "
        "other person which page mattered.",
        y, SERIF, 10.4, 14.4, INK, x=M_GUT, w=CW, align="c")
    y -= 30
    b.kicker("Keep going", y, 7.0, MID, align="c", x=M_GUT, w=CW)

    # ---- 128: colophon -----------------------------------------------------
    b.np(folio=False)
    y = 1.9 * inch
    b.text(f"{TITLE.title()} {TITLE2.title()}", y, DISP_B, 9.5, MID, "c",
           M_OUT, CW)
    y -= 15
    b.text(f"{IMPRINT}  ·  {YEAR}", y, UI, 7.4, MID, "c", M_OUT, CW)
    y -= 15
    b.text("6 × 9 in  ·  128 pages", y, UI, 7.4, MID, "c", M_OUT, CW)


# ============================================================================
# COVER — full wrap: back cover + spine + front cover, with bleed
# ============================================================================
BLEED   = 0.125 * inch
SAFE    = 0.25 * inch
PPI     = 0.002252 * inch      # KDP: white paper, black & white interior


def build_cover(path, pages):
    spine = pages * PPI
    W = BLEED * 2 + PW * 2 + spine
    H = BLEED * 2 + PH
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle(f"{TITLE} {TITLE2} — cover")
    c.setAuthor(AUTHOR)

    bx, by = BLEED, BLEED              # back-cover trim origin
    sx = BLEED + PW                    # spine left edge
    fx = sx + spine                    # front-cover trim origin
    top = BLEED + PH

    # full bleed background
    c.setFillColor(CV_BG)
    c.rect(0, 0, W, H, stroke=0, fill=1)

    # ---------------- front cover ------------------------------------------
    cxm = fx + PW / 2

    # hairline frame inside the safe area
    c.setStrokeColor(CV_ACC); c.setLineWidth(0.7)
    c.rect(fx + SAFE + 8, by + SAFE + 8, PW - 2 * (SAFE + 8),
           PH - 2 * (SAFE + 8), stroke=1, fill=0)

    # kicker
    def track(txt, y, font, size, color, cx, tracking):
        c.setFont(font, size); c.setFillColor(color)
        total = sum(pdfmetrics.stringWidth(ch, font, size) + tracking
                    for ch in txt) - tracking
        x = cx - total / 2
        for ch in txt:
            c.drawString(x, y, ch)
            x += pdfmetrics.stringWidth(ch, font, size) + tracking

    track("A GUIDED PRACTICE JOURNAL", top - 1.28 * inch, UI_B, 8.4, CV_ACC,
          cxm, 3.0)

    # title
    # title, auto-fitted so it can never touch the frame
    inner = PW - 2 * (SAFE + 8) - 44
    size = 42.0
    while max(pdfmetrics.stringWidth(t, DISP_B, size)
              for t in (TITLE, TITLE2)) > inner and size > 16:
        size -= 0.5
    c.setFillColor(CV_FG)
    c.setFont(DISP_B, size)
    c.drawCentredString(cxm, top - 2.58 * inch, TITLE)
    c.drawCentredString(cxm, top - 2.58 * inch - size * 1.14, TITLE2)

    # rule
    ry = top - 2.58 * inch - size * 1.14 - 30
    c.setStrokeColor(CV_ACC); c.setLineWidth(1.6)
    c.line(cxm - 30, ry, cxm + 30, ry)

    # subtitle
    c.setFillColor(CV_DIM)
    yy = ry - 30
    for ln in SUBTITLE.split("\n"):
        c.setFont(SERIF, 15)
        c.drawCentredString(cxm, yy, ln)
        yy -= 21

    # twelve-week tick motif
    ty = by + 2.20 * inch
    n, step = 12, 15.0
    startx = cxm - (n - 1) * step / 2
    for i in range(n):
        filled = i < 7
        c.setStrokeColor(CV_ACC if filled else CV_DIM)
        c.setFillColor(CV_ACC if filled else CV_BG)
        c.setLineWidth(1.0)
        c.rect(startx + i * step - 3, ty, 6, 16, stroke=1, fill=1 if filled else 0)
    track("TWELVE WEEKS · SEVENTY-TWO SESSIONS · ONE SKILL",
          ty - 20, UI_B, 6.8, CV_DIM, cxm, 2.2)

    # author
    track(AUTHOR.upper(), by + 1.05 * inch, UI_B, 10.0, CV_FG, cxm, 2.6)

    # ---------------- spine -------------------------------------------------
    if pages >= 100:
        c.saveState()
        c.translate(sx + spine / 2, by + PH / 2)
        c.rotate(-90)
        c.setFillColor(CV_FG)
        c.setFont(DISP_B, 8.4)
        c.drawString(-PH / 2 + 0.75 * inch, -3.0,
                     f"{TITLE} {TITLE2}")
        c.setFillColor(CV_DIM)
        c.setFont(UI_M, 7.0)
        c.drawRightString(PH / 2 - 0.75 * inch, -2.6, AUTHOR.upper())
        c.restoreState()

    # ---------------- back cover -------------------------------------------
    lx = bx + SAFE + 14
    lw = PW - 2 * (SAFE + 14)
    yy = top - 1.15 * inch

    track("STOP COLLECTING SKILLS. FINISH ONE.", yy, UI_B, 8.2, CV_ACC,
          bx + PW / 2, 2.4)
    yy -= 34

    c.setFillColor(CV_FG)
    c.setFont(DISP_B, 15.5)
    c.drawCentredString(bx + PW / 2, yy, "Twelve weeks.")
    yy -= 21
    c.drawCentredString(bx + PW / 2, yy, "Seventy-two sessions.")
    yy -= 21
    c.drawCentredString(bx + PW / 2, yy, "One skill you actually keep.")
    yy -= 30

    c.setStrokeColor(CV_DIM); c.setLineWidth(0.5)
    c.line(bx + PW / 2 - 26, yy, bx + PW / 2 + 26, yy)
    yy -= 26

    blurb = (
        "Most learning fails quietly. You pick four skills, buy three "
        "courses, and six weeks later you cannot name a single thing you "
        "made. This journal fixes the structure, not your willpower.",
        "Inside is a twelve-week working lab. You choose one skill and score "
        "it honestly. You sign a charter with a real time and a real place. "
        "Then you run six short sessions a week and log the only thing that "
        "matters: exactly where you got stuck, and what you will try next.",
    )
    c.setFillColor(CV_DIM)
    for p in blurb:
        for ln in simpleSplit(p, SERIF, 10.2, lw):
            c.setFont(SERIF, 10.2)
            c.drawString(lx, yy, ln)
            yy -= 14.2
        yy -= 8

    yy -= 4
    track("WHAT IS INSIDE", yy, UI_B, 7.0, CV_ACC, bx + PW / 2, 2.2)
    yy -= 20

    bullets = [
        "A skill-selection lab that ends the deciding",
        "A signed charter with a time, a place and a number",
        "72 daily lab pages built around a Friction Log",
        "12 week briefs and 12 honest week debriefs",
        "An evidence ledger — proof, not hours",
        "Resource log, wins log and stuck-to-solved tracker",
    ]
    for bl in bullets:
        c.setFillColor(CV_ACC)
        c.setFont(UI_B, 8.6)
        c.drawString(lx + 4, yy, "—")
        c.setFillColor(CV_FG)
        c.setFont(UI, 9.0)
        c.drawString(lx + 18, yy, bl)
        yy -= 15.5

    # closing line
    yy -= 12
    c.setStrokeColor(CV_DIM); c.setLineWidth(0.5)
    c.line(lx, yy, lx + lw, yy)
    yy -= 24
    c.setFillColor(CV_FG)
    c.setFont(SERIF, 11.4)
    c.drawCentredString(bx + PW / 2, yy,
                        "Pick one skill. Give it twelve weeks.")
    yy -= 17
    c.setFillColor(CV_DIM)
    c.setFont(SERIF, 11.4)
    c.drawCentredString(bx + PW / 2, yy, "Everything you need is in here.")

    # imprint, kept clear of the barcode block
    c.setFillColor(CV_DIM)
    c.setFont(UI_B, 7.4)
    c.drawString(lx, by + 0.42 * inch, IMPRINT.upper())
    if ISBN:
        c.setFont(UI, 6.6)
        c.drawString(lx, by + 0.42 * inch - 11, f"ISBN {ISBN}")

    # KDP barcode reserve: 2.0 x 1.2 in, clear white, bottom-right of back cover
    c.setFillColor(HexColor("#FFFFFF"))
    c.rect(bx + PW - SAFE - 2.0 * inch, by + SAFE,
           2.0 * inch, 1.2 * inch, stroke=0, fill=1)

    c.showPage()
    c.save()
    return spine, W, H


# ============================================================================
def main():
    register_fonts()
    os.makedirs(DIST, exist_ok=True)

    interior = os.path.join(DIST, "skill-seeker-journal_interior_6x9_128pp.pdf")
    b = Book(interior)
    front_matter(b)
    selection_lab(b)
    core(b)
    back_matter(b)
    n = b.page
    b.save()

    assert n % 2 == 0, f"page count {n} must be even for print"
    assert n == PAGES, f"expected {PAGES} pages, produced {n}"

    cover = os.path.join(DIST, f"skill-seeker-journal_cover_6x9_{n}pp.pdf")
    spine, W, H = build_cover(cover, n)

    print(f"interior : {interior}")
    print(f"           {n} pages, {PW/inch:g} x {PH/inch:g} in, no bleed")
    print(f"cover    : {cover}")
    print(f"           {W/inch:.3f} x {H/inch:.3f} in incl. 0.125 in bleed, "
          f"spine {spine/inch:.4f} in")


if __name__ == "__main__":
    main()
