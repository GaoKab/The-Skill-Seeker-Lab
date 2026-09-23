#!/usr/bin/env python3
"""
BEFORE THE SERMON — Sitting With Scripture. Print-ready generator.

Builds two upload-ready PDFs for Amazon KDP (or any print shop):

    dist/before-the-sermon_interior_6x9_128pp.pdf   <- KDP "Manuscript"
    dist/before-the-sermon_cover_6x9_128pp.pdf      <- KDP "Book Cover"

Trim 6 x 9 in, 128 pages. Interior is black & white on CREAM paper by default
(the mockups' warm stock); flip COLOR_INTERIOR for a terracotta accent on
white paper. Run:  python3 before-the-sermon/build_notebook.py
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
# EDIT THESE AND RE-RUN.
# ----------------------------------------------------------------------------
AUTHOR         = "Gao Kab"
IMPRINT        = "Before the Sermon"
YEAR           = "2026"
ISBN           = ""
AUTHOR_ON_TITLE_PAGE = False  # Gao asked for her name off the interior title page (23 Sep)
COLOR_INTERIOR = False        # False: B&W on cream paper (cheapest, matches the
                              #        mockups' stock). True: terracotta accent,
                              #        KDP standard colour, white paper only.

TITLE     = "BEFORE"
TITLE2    = "SERMON"
SUBTITLE  = "Sitting With Scripture"
TAGLINE   = "A Notebook for Thoughtful Reading"
READINGS  = 52                # one spread per reading; a year of Sundays

# The six questions, repeated on every spread. Merged from the interior mockup
# (question form) and the website's "Each Spread Prompts You To" list, with the
# mockup's overlap removed and the site's "assumptions" prompt carried across.
PROMPTS = [
    ("What does the text actually say?",
     "Before any meaning: what is written, what is repeated, whose voice is "
     "speaking."),
    ("What keeps pulling your attention?",
     "A word, a phrase, a turn you can’t get past. You don’t have to "
     "know why yet."),
    ("What are you bringing to it?",
     "Assumptions, memories, what you’ve been told this means. Name them "
     "so you can set them down."),
    ("What confused you, or sat uneasily?",
     "Questions are welcome here, even uncomfortable ones. Nothing has to "
     "resolve."),
    ("What did you feel as you read?",
     "Not what you think you should feel. What you felt."),
    ("What do you think this text is exploring?",
     "Not what it teaches. What it is about."),
]
CLOSING = ("Before you close the book",
           ["What will you sit with longer?",
            "What might this text be asking of you?"])

# ----------------------------------------------------------------------------
# Print specification
# ----------------------------------------------------------------------------
PW, PH   = 6 * inch, 9 * inch
PAGES    = 128
M_GUT    = 0.75 * inch
M_OUT    = 0.55 * inch
M_TOP    = 0.62 * inch
M_BOT    = 0.66 * inch
CW       = PW - M_GUT - M_OUT
CT       = PH - M_TOP
CB       = M_BOT
LINE_GAP = 19.0

# KDP pages-per-inch: white B&W 0.002252 / cream B&W 0.0025 / colour 0.002347
PPI   = (0.002347 if COLOR_INTERIOR else 0.0025) * inch
BLEED = 0.125 * inch
SAFE  = 0.25 * inch

# ---- KDP HARDCOVER (case laminate) geometry ---------------------------------
# White paper only. Wrap and hinge are KDP-published; the spine formula is the
# consensus of two third-party calculators (0.002252 in/page + 0.06 in board).
# BEFORE UPLOADING: run KDP's cover calculator for 6x9 / 128 pages, and if its
# template shows different spine / wrap / hinge figures, set them here and
# rebuild. Three constants, one rebuild.
HC_WRAP  = 0.51 * inch                     # KDP: art extends 0.51 in (15 mm) past trim, incl. bleed
HC_HINGE = 0.40 * inch                     # KDP: 0.4 in (10 mm) between spine and safe area
HC_SPINE = (PAGES * 0.002252 + 0.06) * inch
HC_SAFE  = 0.635 * inch                    # KDP: text/images 0.635 in (16 mm) from book edge

HERE  = os.path.dirname(os.path.abspath(__file__))
DIST  = os.path.join(HERE, "dist")
FONTS = os.path.join(HERE, "assets", "fonts")

# ----------------------------------------------------------------------------
# Ink. Site palette: cream oklch(98% .01 60), warm near-black oklch(30% .01 60),
# terracotta oklch(55% .08 35). In B&W the accent becomes a mid warm grey that
# halftones reliably (~55% K).
# ----------------------------------------------------------------------------
INK    = Color(0.16, 0.14, 0.12) if COLOR_INTERIOR else Color(0.10, 0.10, 0.10)
MID    = Color(0.42, 0.42, 0.42)
RULE   = Color(0.68, 0.68, 0.68)
HAIR   = Color(0.79, 0.79, 0.79)          # ~21% K, lightest tone used
ACCENT = HexColor("#A3573A") if COLOR_INTERIOR else Color(0.40, 0.40, 0.40)

# Cover (always colour)
CV_BG   = HexColor("#F1EBDF")   # cream linen
CV_INK  = HexColor("#3B342C")   # warm near-black
CV_GOLD = HexColor("#A8843B")   # printed "gold"
CV_DIM  = HexColor("#7D7367")

DISP    = "Cormorant"           # Medium
DISP_B  = "Cormorant-Bold"
DISP_SB = "Cormorant-SemiBold"
DISP_I  = "Cormorant-Italic"    # Medium Italic
DISP_SI = "Cormorant-SemiBoldItalic"
BODY    = "Crimson"
BODY_I  = "Crimson-Italic"
BODY_SB = "Crimson-SemiBold"
UI      = "Lato"
UI_B    = "Lato-Bold"
UI_I    = "Lato-Italic"


def register_fonts():
    pairs = [
        (DISP,    "CormorantGaramond-Medium.ttf"),
        (DISP_B,  "CormorantGaramond-Bold.ttf"),
        (DISP_SB, "CormorantGaramond-SemiBold.ttf"),
        (DISP_I,  "CormorantGaramond-MediumItalic.ttf"),
        (DISP_SI, "CormorantGaramond-SemiBoldItalic.ttf"),
        (BODY,    "CrimsonText-Regular.ttf"),
        (BODY_I,  "CrimsonText-Italic.ttf"),
        (BODY_SB, "CrimsonText-SemiBold.ttf"),
        (UI,      "Lato-Regular.ttf"),
        (UI_B,    "Lato-Bold.ttf"),
        (UI_I,    "Lato-Italic.ttf"),
    ]
    for name, fn in pairs:
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, fn)))
    # KDP rejects unembedded fonts; stop ReportLab listing Helvetica per page.
    rl_config.canvas_basefontname = BODY


# ----------------------------------------------------------------------------
# Page engine (shared design with journal/build_journal.py; kept self-contained
# so a change to one product can never silently alter a book already on sale)
# ----------------------------------------------------------------------------
class Book:
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=(PW, PH))
        self.c.setTitle(f"Before the Sermon: {SUBTITLE}")
        self.c.setAuthor(AUTHOR)
        self.c.setSubject("A guided reading notebook for Scripture")
        self.page = 0

    def np(self, folio=True, running=""):
        if self.page > 0:
            self.c.showPage()
        self.page += 1
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
        recto = self.page % 2 == 1
        if running:
            c.setFont(UI, 6.4); c.setFillColor(MID)
            (c.drawRightString(self.x1, y, running.upper()) if not recto
             else c.drawString(self.x0, y, running.upper()))
        c.setFont(DISP, 9.0); c.setFillColor(MID)
        c.drawCentredString(self.x0 + CW / 2, y, str(self.page))
        c.setFillColor(INK)

    def blank(self, n=1):
        for _ in range(n):
            self.np(folio=False)

    # -- primitives ----------------------------------------------------------
    def hline(self, y, x=None, w=None, color=RULE, lw=0.5):
        x = self.x0 if x is None else x
        w = CW if w is None else w
        self.c.setStrokeColor(color); self.c.setLineWidth(lw)
        self.c.line(x, y, x + w, y)

    def text(self, s, y, font=BODY, size=10, color=INK, align="l", x=None,
             w=None):
        c = self.c
        x = self.x0 if x is None else x
        w = CW if w is None else w
        c.setFont(font, size); c.setFillColor(color)
        if align == "l":
            c.drawString(x, y, s)
        elif align == "c":
            c.drawCentredString(x + w / 2, y, s)
        else:
            c.drawRightString(x + w, y, s)
        c.setFillColor(INK)

    def para(self, s, y, font=BODY, size=10.5, leading=15, color=INK, x=None,
             w=None, align="l"):
        x = self.x0 if x is None else x
        w = CW if w is None else w
        for block in s.split("\n"):
            if not block.strip():
                y -= leading * 0.55
                continue
            for ln in simpleSplit(block, font, size, w):
                self.text(ln, y, font, size, color, align, x, w)
                y -= leading
        return y

    def kicker(self, s, y, size=7.0, color=MID, x=None, w=None, align="l",
               tracking=1.9):
        c = self.c
        x = self.x0 if x is None else x
        w = CW if w is None else w
        c.setFont(UI, size); c.setFillColor(color)
        total = sum(pdfmetrics.stringWidth(ch, UI, size) + tracking
                    for ch in s.upper()) - tracking
        cx = {"c": x + (w - total) / 2, "r": x + w - total}.get(align, x)
        for ch in s.upper():
            c.drawString(cx, y, ch)
            cx += pdfmetrics.stringWidth(ch, UI, size) + tracking
        c.setFillColor(INK)
        return cx

    def lines(self, y, n, gap=LINE_GAP, x=None, w=None, color=RULE, lw=0.5):
        x = self.x0 if x is None else x
        w = CW if w is None else w
        for _ in range(n):
            y -= gap
            self.hline(y, x, w, color, lw)
        return y

    def inline_field(self, lab, y, x, w, size=9.5):
        """Italic serif label on the left of a rule: Passage ________"""
        c = self.c
        c.setFont(DISP_I, size + 1.5); c.setFillColor(MID)
        c.drawString(x, y, lab)
        end = x + pdfmetrics.stringWidth(lab, DISP_I, size + 1.5) + 6
        self.hline(y - 3, end, x + w - end, RULE, 0.5)
        c.setFillColor(INK)

    def ornament(self, y, x=None, w=None, color=None, half=26):
        """line · line — the mark from the cover, used as a section break."""
        c = self.c
        color = ACCENT if color is None else color
        x = self.x0 if x is None else x
        w = CW if w is None else w
        cx = x + w / 2
        c.setStrokeColor(color); c.setLineWidth(0.6)
        c.line(cx - half - 6, y, cx - 6, y)
        c.line(cx + 6, y, cx + half + 6, y)
        c.setFillColor(color)
        c.circle(cx, y, 1.5, stroke=0, fill=1)
        c.setFillColor(INK)

    def page_head(self, kicker, title, sub=None):
        y = CT
        if kicker:
            self.kicker(kicker, y, 6.8, MID)
            y -= 18
        for i, ln in enumerate(title.split("\n")):
            self.text(ln, y - 12, DISP_SB, 24, INK)
            y -= 12 + 16 if i == 0 else 27
        if sub:
            y -= 6
            y = self.para(sub, y, BODY_I, 10.6, 14.6, MID)
            y += 1
        y -= 10
        self.ornament(y)
        y -= 24
        return y

    def distribute(self, heights, y_start, y_end=None, min_gap=6.0,
                   max_gap=34.0):
        y_end = CB if y_end is None else y_end
        n = len(heights)
        gap = ((y_start - y_end) - sum(heights)) / (n - 1) if n > 1 else 0.0
        gap = max(min_gap, min(max_gap, gap))
        ys, y = [], y_start
        for h in heights:
            ys.append(y)
            y -= h + gap
        return ys

    def prompt(self, n, q, hint, y, nlines):
        """Numbered question in accent italic, hint under it, ruled lines."""
        c = self.c
        c.setFont(DISP_SI, 14.5); c.setFillColor(ACCENT)
        num = f"{n}."
        c.drawString(self.x0, y, num)
        nx = self.x0 + pdfmetrics.stringWidth(num, DISP_SI, 14.5) + 5
        c.drawString(nx, y, q)
        y -= 13
        y = self.para(hint, y, BODY, 8.8, 11.6, MID, x=nx, w=CW - (nx - self.x0))
        y -= 1
        return self.lines(y, nlines)

    @staticmethod
    def prompt_h(nlines, hint_lines=1):
        return 13 + hint_lines * 11.6 + 1 + nlines * LINE_GAP

    def save(self):
        self.c.showPage()
        self.c.save()


# ============================================================================
# COPY — everything in quotes here is recovered from the site (Home.tsx).
# The few lines authored for print are marked NEW in the README.
# ============================================================================
WHAT_IT_IS = (
    "Before the Sermon: Sitting With Scripture is a guided reading notebook "
    "designed to help people engage Scripture slowly, thoughtfully, and "
    "without intimidation. It is not a devotional, commentary, or theology "
    "guide. It does not explain passages or tell readers what to believe.\n\n"
    "Instead, it offers a structured way to sit with the text, notice what is "
    "written, reflect honestly, and build confidence as a reader — before "
    "sermons, summaries, or conclusions. The notebook is meant to be used "
    "alongside the Bible, not instead of it."
)
WHO = ["People who feel intimidated by the Bible",
       "Readers who don’t know how to read Scripture on their own",
       "Christians who want to slow down their reading",
       "Seekers or non-Christians who are curious but cautious",
       "Anyone who wants to engage the Bible without pressure, performance, "
       "or expertise"]
NOT_DO  = ["Interpret Scripture for you", "Push application or action",
           "Assume belief or expertise"]
PURPOSE = ["Change how you read", "Train attention and patience",
           "Allow meaning to surface slowly", "Build honest reading confidence"]
VOICE   = [("Calm", "not authoritative"), ("Invitational", "not instructional"),
           ("Reflective", "not prescriptive"), ("Gentle", "but serious")]
MOVES   = [("Observe", "Notice what the text actually says — repetition, "
                       "emphasis, and voice — without rushing to conclusions."),
           ("Acknowledge", "Acknowledge confusion or discomfort. Sit with "
                           "questions. There are no right answers required."),
           ("Decide", "Decide what you want to sit with longer. Let meaning "
                      "surface slowly rather than being imposed.")]


# ============================================================================
# FRONT MATTER — pages 1-13
# ============================================================================
def front_matter(b):
    c = b.c

    # 1 half title
    b.np(folio=False)
    b.text("Before the Sermon", PH / 2 + 6, DISP_SB, 22, INK, "c", M_GUT, CW)
    b.ornament(PH / 2 - 12, M_GUT, CW)
    b.blank(1)                                                        # 2

    # 3 title page
    b.np(folio=False)
    y = PH - 2.35 * inch
    b.kicker(TAGLINE, y, 7.2, MID, M_GUT, CW, "c")
    y -= 52
    b.text(TITLE, y, DISP_B, 40, INK, "c", M_GUT, CW)
    y -= 30
    b.ornament(y + 8, M_GUT, CW, INK, half=30)
    b.text("the", y + 4, DISP_I, 12, MID, "c", M_GUT, CW)
    y -= 36
    b.text(TITLE2, y, DISP_B, 40, INK, "c", M_GUT, CW)
    y -= 40
    b.text(SUBTITLE, y, DISP_I, 17, MID, "c", M_GUT, CW)
    if AUTHOR_ON_TITLE_PAGE:
        b.kicker(AUTHOR, 1.55 * inch, 7.6, INK, M_GUT, CW, "c")

    # 4 copyright
    b.np(folio=False)
    body = (
        f"Before the Sermon: {SUBTITLE}\n"
        f"Copyright © {YEAR} {AUTHOR}. All rights reserved.\n\n"
        "No part of this publication may be reproduced, distributed, or "
        "transmitted in any form or by any means without the prior written "
        "permission of the publisher, except for brief quotations in a review "
        "and for the purchaser’s own personal, non-commercial use of the "
        "writing pages within this copy.\n\n"
        "This notebook is a reading companion, not a replacement for sermons. "
        "It does not interpret Scripture, and it does not tell you what to "
        "believe.\n\n"
        f"Published by {IMPRINT}."
    )
    if ISBN:
        body += f"\nISBN: {ISBN}"
    body += (f"\n\nFirst edition, {YEAR}. Printed on demand.\n\n"
             "Set in Cormorant Garamond, Crimson Text and Lato.")
    b.para(body, 3.2 * inch, BODY, 8.8, 12.4, MID, M_OUT, CW)

    # 5 belongs to
    b.np(folio=False)
    y = PH - 2.7 * inch
    b.kicker("This notebook belongs to", y, 7.0, MID, M_GUT, CW, "c")
    y -= 46
    b.hline(y, M_GUT + 0.3 * inch, CW - 0.6 * inch, INK, 0.7)
    y -= 58
    b.kicker("Begun", y + 12, 6.4, MID, M_GUT + 0.3 * inch, CW * 0.4)
    b.hline(y, M_GUT + 0.3 * inch, CW * 0.42, RULE, 0.6)
    b.kicker("Translation I am reading", y + 12, 6.4, MID,
             M_GUT + 0.3 * inch + CW * 0.5, CW * 0.4)
    b.hline(y, M_GUT + 0.3 * inch + CW * 0.5, CW * 0.42, RULE, 0.6)
    y -= 70
    b.para("There is no right pace for this. Some readings will take an "
           "evening. Some will take a season.", y, BODY_I, 10.4, 14.4, MID,
           M_GUT + 0.3 * inch, CW - 0.6 * inch, "c")
    b.blank(1)                                                        # 6

    # 7 what this notebook is
    b.np(running="What this notebook is")
    y = b.page_head("Read this first", "What this\nnotebook is")
    y = b.para(WHAT_IT_IS, y, BODY, 12.2, 18.0, INK)
    y -= 26
    b.kicker("Who it is for", y, 6.8, MID); y -= 20
    for w in WHO:
        c.setFillColor(ACCENT); c.circle(b.x0 + 3, y + 3.2, 1.4, stroke=0, fill=1)
        y = b.para(w, y, BODY, 11.4, 16.0, INK, x=b.x0 + 14, w=CW - 14)
        y -= 4
    y -= 14
    b.para("No prior knowledge, belief, or background is assumed.", y, BODY_I,
           11.6, 16.0, MID)

    # 8 what makes it different
    b.np(running="What makes it different")
    y = b.page_head(None, "What makes it\ndifferent")
    half = (CW - 22) / 2
    b.kicker("This notebook does not", y, 6.8, ACCENT, b.x0, half)
    b.kicker("Its purpose is to", y, 6.8, ACCENT, b.x0 + half + 22, half)
    y -= 20
    yl = yr = y
    for s in NOT_DO:
        yl = b.para(s, yl, BODY, 10.6, 14.6, INK, b.x0, half) - 4
    for s in PURPOSE:
        yr = b.para(s, yr, BODY, 10.6, 14.6, INK, b.x0 + half + 22, half) - 4
    y = min(yl, yr) - 16
    b.hline(y, color=HAIR); y -= 30
    b.para("Confusion, silence, and “I don’t know” are treated "
           "as valid outcomes.", y, DISP_SI, 15, 19, INK, align="c")
    y -= 42
    b.hline(y, color=HAIR); y -= 24
    b.kicker("The voice of this notebook", y, 6.8, MID); y -= 22
    for i, (a, bb) in enumerate(VOICE):
        col, row = i % 2, i // 2
        x = b.x0 + col * (half + 22)
        yy = y - row * 52
        b.text(a, yy, DISP_SB, 20, INK, x=x)
        b.text(bb, yy - 16, UI, 8.2, MID, x=x)
    y -= 112
    b.para("It avoids religious jargon, moralizing language, and pressure to "
           "apply or conclude.", y, BODY_I, 10.4, 14.4, MID)

    # 9 the three movements
    b.np(running="How it works")
    y = b.page_head("How it works", "Three movements",
                    "The notebook consists primarily of repeating guided "
                    "spreads designed to be used during Scripture reading "
                    "sessions. Each one moves through the same three motions.")
    for i, (name, desc) in enumerate(MOVES, 1):
        c.setFont(DISP_SI, 26); c.setFillColor(ACCENT)
        c.drawString(b.x0, y - 8, f"{i}")
        b.text(name, y, DISP_SB, 17, INK, x=b.x0 + 26)
        y -= 16
        y = b.para(desc, y, BODY, 10.6, 14.6, MID, x=b.x0 + 26, w=CW - 26)
        y -= 22
    y -= 4
    b.hline(y, color=HAIR); y -= 24
    b.kicker("Each spread prompts you to", y, 6.8, MID); y -= 18
    for s in ["Observe what the text actually says",
              "Notice repetition, emphasis, and voice",
              "Identify assumptions you may be bringing",
              "Acknowledge confusion without rushing to resolve it",
              "Reflect on how the passage touches your life",
              "Choose what you want to sit with longer"]:
        c.setFillColor(ACCENT); c.circle(b.x0 + 3, y + 3.2, 1.4, stroke=0, fill=1)
        y = b.para(s, y, BODY, 10.4, 14.2, INK, x=b.x0 + 14, w=CW - 14) - 2
    y -= 10
    b.para("The same set of questions repeats throughout to build familiarity "
           "and confidence.", y, BODY_I, 10.4, 14.4, MID)

    # 10 before you begin
    b.np(running="Before you begin")
    y = b.page_head(None, "Before you begin")
    y = b.para(
        "Open the Bible to whatever you are reading — a passage from a "
        "plan, the text for Sunday, a chapter you keep avoiding. Read it once "
        "without a pen. Then read it again with one.\n\n"
        "Write the reference and the date at the top of the spread. Then take "
        "the six questions in order. They are the same on every spread on "
        "purpose: you are not meant to get better at the questions, you are "
        "meant to get better at reading.\n\n"
        "Short answers are fine. Blank lines are fine. “I don’t know "
        "what this means” is a complete answer, and often the most honest "
        "one on the page.\n\n"
        "Nothing here has to be finished before the sermon. The point is only "
        "to have looked, properly, for yourself — so that when someone "
        "else explains the text, you meet their reading with one of your "
        "own.", y, BODY, 12.2, 18.0, INK)
    y -= 22
    b.ornament(y); y -= 34
    b.para("You are never being tested here.", y, DISP_SI, 15, 19, INK, align="c")

    # 11-12 reading log
    for part in (0, 1):
        b.np(running="Readings")
        y = CT
        if part == 0:
            y = b.page_head("An index you fill in", "Readings",
                            "One line per spread. A place to see, later, "
                            "where you have been.")
        else:
            b.kicker("Readings · continued", y, 6.8, MID)
            y -= 12
            b.ornament(y, half=14); y -= 18
        colw = [28, 62, CW - 28 - 62 - 92, 92]
        for i, h in enumerate(("", "DATE", "PASSAGE", "ONE WORD")):
            if h:
                b.kicker(h, y + 5, 5.8, MID, b.x0 + sum(colw[:i]) + 4, colw[i])
        c.setStrokeColor(INK); c.setLineWidth(0.7); c.line(b.x0, y, b.x1, y)
        rows = READINGS // 2
        rowh = (y - CB - 6) / rows
        for r in range(rows):
            ry = y - r * rowh
            b.text(f"{part * rows + r + 1:02d}", ry - rowh / 2 - 3, UI, 6.6,
                   HAIR, x=b.x0 + 4)
            c.setStrokeColor(HAIR); c.setLineWidth(0.5)
            for xo in (colw[0], colw[0] + colw[1], colw[0] + colw[1] + colw[2]):
                c.line(b.x0 + xo, ry, b.x0 + xo, ry - rowh)
            c.setStrokeColor(RULE); c.line(b.x0, ry - rowh, b.x1, ry - rowh)

    # 13 how to use a spread (recto, faces the first spread)
    b.np(running="How to use a spread")
    y = b.page_head(None, "How to use\na spread",
                    "Every reading takes two facing pages. They are always "
                    "the same.")
    rows = [("Passage · Date", "Write the reference exactly as you would "
             "say it aloud, and the date. Later this is how you will find "
             "your way back."),
            ("1 – 2", "Observe. What the text actually says, and what "
             "keeps pulling at you. Stay on the surface longer than feels "
             "natural."),
            ("3 – 4", "Acknowledge. What you brought with you, and what "
             "confused or unsettled you. Nothing has to be solved."),
            ("5 – 6", "Notice. What you felt, and what you think the text "
             "is exploring — not what it teaches, what it is about."),
            ("Closing", "Decide. One thing to sit with longer. One question "
             "the text might be asking of you. A line each; or leave them.")]
    for h, t in rows:
        b.text(h, y, DISP_SI, 14.5, ACCENT)
        y -= 16
        y = b.para(t, y, BODY, 11.2, 15.8, INK)
        y -= 18
    y -= 2
    b.hline(y, color=HAIR); y -= 24
    b.para("Turn the page.", y, DISP_SI, 15, 19, MID, align="c")


# ============================================================================
# THE SPREADS — pages 14-117, READINGS x 2 pages
# ============================================================================
def spread(b, n):
    c = b.c
    NL = 5                                   # ruled lines per question

    # ---- left page (verso) ---------------------------------------------------
    b.np(running=f"Reading {n:02d}")
    assert b.page % 2 == 0, "a spread must open on a left-hand page"
    y = CT
    b.inline_field("Passage", y - 4, b.x0, CW * 0.62)
    b.inline_field("Date", y - 4, b.x0 + CW * 0.70, CW * 0.30)
    y -= 18
    b.hline(y, color=INK, lw=0.7)
    y -= 22
    NL_L = NL + 1                            # left page has no closing block
    H = [b.prompt_h(NL_L, 1 if len(PROMPTS[i][1]) < 62 else 2) for i in range(3)]
    ys = b.distribute(H, y, min_gap=14, max_gap=30)
    for i in range(3):
        b.prompt(i + 1, PROMPTS[i][0], PROMPTS[i][1], ys[i], NL_L)

    # ---- right page (recto) --------------------------------------------------
    b.np(running=f"Reading {n:02d}")
    y = CT - 4
    H = [b.prompt_h(NL, 1 if len(PROMPTS[i][1]) < 62 else 2) for i in range(3, 6)]
    H.append(18 + len(CLOSING[1]) * (LINE_GAP + 10))
    ys = b.distribute(H, y, min_gap=14, max_gap=30)
    for k, i in enumerate(range(3, 6)):
        b.prompt(i + 1, PROMPTS[i][0], PROMPTS[i][1], ys[k], NL)
    yy = ys[3]
    b.text(CLOSING[0], yy, DISP_SI, 12.5, MID)
    yy -= 10
    for q in CLOSING[1]:
        yy -= 12
        b.text(q, yy, BODY_I, 9.4, INK)
        yy -= 4
        b.hline(yy - LINE_GAP + 8, color=RULE)
        yy -= LINE_GAP - 6


def core(b):
    for n in range(1, READINGS + 1):
        spread(b, n)


# ============================================================================
# BACK MATTER — pages 118-128
# ============================================================================
def back_matter(b):
    c = b.c

    # 118 passages I keep returning to (verso)
    b.np(running="Returning")
    y = b.page_head("After the readings", "Passages I keep\nreturning to",
                    "Some texts do not let go. List them here, with a word "
                    "about why, and come back when you need them.")
    b.kicker("Passage", y, 5.8, MID, b.x0, CW * 0.36)
    b.kicker("Why it stays", y, 5.8, MID, b.x0 + CW * 0.40, CW * 0.60)
    y -= 4
    n = int((y - CB) // (LINE_GAP + 8))
    for _ in range(n):
        y -= LINE_GAP + 8
        b.hline(y, b.x0, CW * 0.36, RULE, 0.5)
        b.hline(y, b.x0 + CW * 0.40, CW * 0.60, HAIR, 0.5)

    # 119 questions I still carry (recto)
    b.np(running="Still carrying")
    y = b.page_head(None, "Questions I\nstill carry",
                    "Unresolved is allowed. These are not a to-do list. They "
                    "are the questions worth keeping company with.")
    n = int((y - CB) // (LINE_GAP + 9))
    for _ in range(n):
        y -= LINE_GAP + 9
        c.setFillColor(ACCENT); c.circle(b.x0 + 2, y + 3.5, 1.3, stroke=0, fill=1)
        b.hline(y, b.x0 + 12, CW - 12, RULE, 0.5)

    # 120-125 sitting longer (6 ruled pages)
    for i in range(6):
        b.np(running="Sitting longer")
        y = CT
        if i == 0:
            y = b.page_head("Overflow", "Sitting longer",
                            "For the readings that needed more than a spread.")
        else:
            b.kicker("Sitting longer", y, 6.8, MID)
            y -= 12
            b.ornament(y, half=14); y -= 14
        n = int((y - CB) // LINE_GAP)
        b.lines(y, n)

    # 126 a note at the end (verso)
    b.np(folio=False)
    y = PH / 2 + 60
    b.kicker("At the end", y, 6.8, MID, M_OUT, CW, "c")
    y -= 30
    y = b.para(
        "If some of these pages are half-empty, nothing went wrong. Silence "
        "was allowed from the start.\n\n"
        "What you have now is not a set of answers. It is a record of "
        "having looked — slowly, honestly, on your own — before "
        "anyone told you what to see.",
        y, BODY, 11.0, 16.0, INK, M_OUT + 0.25 * inch, CW - 0.5 * inch, "c")
    y -= 12
    b.ornament(y, M_OUT, CW)

    # 127 about (recto)
    b.np(folio=False)
    y = PH - 2.6 * inch
    b.kicker("About", y, 6.8, MID, M_GUT, CW, "c")
    y -= 32
    b.text("Before the Sermon", y, DISP_SB, 19, INK, "c", M_GUT, CW)
    y -= 22
    b.ornament(y, M_GUT, CW)
    y -= 30
    y = b.para(
        "A guided reading companion designed to help you engage Scripture "
        "slowly, thoughtfully, and without intimidation — before "
        "explanation, interpretation, or performance.\n\n"
        "This notebook exists to help you engage the Bible thoughtfully and "
        "confidently. It is a reading companion, not a replacement for "
        "sermons.",
        y, BODY, 10.8, 15.6, INK, M_GUT, CW, "c")

    # 128 colophon (verso)
    b.np(folio=False)
    y = 1.9 * inch
    b.text(f"Before the Sermon · {SUBTITLE}", y, DISP_I, 10.5, MID, "c",
           M_OUT, CW)
    y -= 15
    b.text(f"{IMPRINT}  ·  {YEAR}", y, UI, 7.0, MID, "c", M_OUT, CW)
    y -= 14
    b.text(f"6 × 9 in  ·  {PAGES} pages  ·  "
           f"{'colour' if COLOR_INTERIOR else 'cream'} interior",
           y, UI, 7.0, MID, "c", M_OUT, CW)


# ============================================================================
# COVER
# ============================================================================
def build_cover(path, pages, hardcover=False):
    if hardcover:
        spine, edge, hinge, safe = HC_SPINE, HC_WRAP, HC_HINGE, HC_SAFE
    else:
        spine, edge, hinge, safe = pages * PPI, BLEED, 0.0, SAFE
    W = 2 * (edge + PW + hinge) + spine
    H = 2 * edge + PH
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle("Before the Sermon \u2014 " + ("hardcover" if hardcover else "cover"))
    c.setAuthor(AUTHOR)
    bx, by = edge, edge                     # back-cover trim origin
    sx = edge + PW + hinge                  # spine left edge
    fx = sx + spine + hinge                 # front-cover trim origin
    top = edge + PH
    SAFE_ = safe

    c.setFillColor(CV_BG); c.rect(0, 0, W, H, stroke=0, fill=1)

    def track(txt, y, font, size, color, cx, tracking):
        c.setFont(font, size); c.setFillColor(color)
        total = sum(pdfmetrics.stringWidth(ch, font, size) + tracking
                    for ch in txt) - tracking
        x = cx - total / 2
        for ch in txt:
            c.drawString(x, y, ch)
            x += pdfmetrics.stringWidth(ch, font, size) + tracking

    # ---- front -------------------------------------------------------------
    cxm = fx + PW / 2
    # thin double frame
    for inset, lw in ((SAFE_ + 6, 0.9), (SAFE_ + 11, 0.4)):
        c.setStrokeColor(CV_GOLD); c.setLineWidth(lw)
        c.rect(fx + inset, by + inset, PW - 2 * inset, PH - 2 * inset,
               stroke=1, fill=0)

    track(TAGLINE.upper(), top - 1.55 * inch, UI, 7.4, CV_DIM, cxm, 3.2)

    size = 54.0
    while pdfmetrics.stringWidth(TITLE2, DISP_B, size) > PW - 2 * (SAFE_ + 40):
        size -= 0.5
    c.setFillColor(CV_GOLD); c.setFont(DISP_B, size)
    ty = top - 3.45 * inch
    c.drawCentredString(cxm, ty, TITLE)
    # ornament with "the"
    oy = ty - 30
    c.setStrokeColor(CV_GOLD); c.setLineWidth(0.9)
    c.line(cxm - 78, oy, cxm - 22, oy)
    c.line(cxm + 22, oy, cxm + 78, oy)
    c.setFont(DISP_I, 15); c.setFillColor(CV_GOLD)
    c.drawCentredString(cxm, oy - 5, "the")
    c.setFont(DISP_B, size)
    c.drawCentredString(cxm, oy - 22 - size * 0.62, TITLE2)

    sy = oy - 22 - size * 0.62 - 42
    c.setFont(DISP_I, 20); c.setFillColor(CV_INK)
    c.drawCentredString(cxm, sy, SUBTITLE)

    # small leaf-less ornament near the foot, then author
    c.setStrokeColor(CV_GOLD); c.setLineWidth(0.7)
    c.line(cxm - 18, by + 1.62 * inch, cxm + 18, by + 1.62 * inch)
    c.setFillColor(CV_GOLD); c.circle(cxm, by + 1.62 * inch, 1.6, stroke=0, fill=1)
    track(AUTHOR.upper(), by + 1.22 * inch, UI, 8.4, CV_INK, cxm, 3.0)

    # ---- spine -------------------------------------------------------------
    if pages >= 100:
        c.saveState()
        c.translate(sx + spine / 2, by + PH / 2); c.rotate(-90)
        c.setFillColor(CV_INK); c.setFont(DISP_SB, 9.5)
        c.drawString(-PH / 2 + 0.7 * inch, -3.2, "BEFORE THE SERMON")
        c.setFont(DISP_I, 8.5); c.setFillColor(CV_DIM)
        w1 = pdfmetrics.stringWidth("BEFORE THE SERMON", DISP_SB, 9.5)
        c.drawString(-PH / 2 + 0.7 * inch + w1 + 10, -3.0, SUBTITLE)
        c.setFont(UI, 6.6); c.setFillColor(CV_INK)
        c.drawRightString(PH / 2 - 0.7 * inch, -2.4, AUTHOR.upper())
        c.restoreState()

    # ---- back --------------------------------------------------------------
    lx = bx + SAFE_ + 16
    lw = PW - 2 * (SAFE_ + 16)
    bcx = bx + PW / 2
    yy = top - 1.25 * inch
    track("A NOTEBOOK FOR THOUGHTFUL READING", yy, UI, 7.2, CV_GOLD, bcx, 3.0)
    yy -= 36
    c.setFillColor(CV_INK); c.setFont(DISP_SI, 19)
    for ln in ("Sit with the text", "before anyone explains it."):
        c.drawCentredString(bcx, yy, ln); yy -= 24
    yy -= 6
    c.setStrokeColor(CV_GOLD); c.setLineWidth(0.7)
    c.line(bcx - 18, yy, bcx + 18, yy)
    c.setFillColor(CV_GOLD); c.circle(bcx, yy, 1.6, stroke=0, fill=1)
    yy -= 28
    c.setFillColor(CV_INK)
    for p in WHAT_IT_IS.split("\n\n"):
        for ln in simpleSplit(p, BODY, 10.4, lw):
            c.setFont(BODY, 10.4); c.drawString(lx, yy, ln); yy -= 14.4
        yy -= 7
    yy -= 4
    half = (lw - 20) / 2
    c.setFont(UI, 6.6); c.setFillColor(CV_GOLD)
    track("THIS NOTEBOOK DOES NOT", yy, UI, 6.6, CV_GOLD, lx + half / 2, 2.2)
    track("ITS PURPOSE IS TO", yy, UI, 6.6, CV_GOLD, lx + half + 20 + half / 2, 2.2)
    yy -= 18
    yl = yr = yy
    c.setFillColor(CV_INK); c.setFont(BODY, 9.8)
    for s in NOT_DO:
        c.drawCentredString(lx + half / 2, yl, s); yl -= 14
    for s in PURPOSE:
        c.drawCentredString(lx + half + 20 + half / 2, yr, s); yr -= 14
    yy = min(yl, yr) - 18
    c.setFont(DISP_SI, 12.5); c.setFillColor(CV_INK)
    c.drawCentredString(bcx, yy, "Confusion, silence, and “I don’t "
                                 "know” are valid outcomes.")
    yy -= 30
    c.setFont(UI, 7.4); c.setFillColor(CV_DIM)
    voice = "   ·   ".join(f"{a}, {bb}" for a, bb in VOICE)
    for ln in simpleSplit(voice, UI, 7.4, lw):
        c.drawCentredString(bcx, yy, ln); yy -= 11

    iy = by + SAFE_ + 4                     # imprint block sits on the safe line
    if ISBN:
        c.setFillColor(CV_DIM); c.setFont(UI, 6.4)
        c.drawString(lx, iy, f"ISBN {ISBN}"); iy += 12
    c.setFillColor(CV_DIM); c.setFont(BODY_I, 8.2)
    c.drawString(lx, iy, "A reading companion, not a replacement for sermons.")
    c.setFont(UI, 6.8)
    c.drawString(lx, iy + 12, IMPRINT.upper())

    c.setFillColor(HexColor("#FFFFFF"))
    if hardcover:
        c.rect(bx + PW - 0.25 * inch - 2.0 * inch, by + 0.76 * inch,
               2.0 * inch, 1.2 * inch, stroke=0, fill=1)
    else:
        c.rect(bx + PW - SAFE - 2.0 * inch, by + SAFE, 2.0 * inch, 1.2 * inch,
               stroke=0, fill=1)
    c.showPage(); c.save()
    return spine, W, H


def main():
    register_fonts()
    os.makedirs(DIST, exist_ok=True)
    interior = os.path.join(DIST, f"before-the-sermon_interior_6x9_{PAGES}pp.pdf")
    b = Book(interior)
    front_matter(b)
    assert b.page == 13, f"front matter should end on page 13, got {b.page}"
    core(b)
    back_matter(b)
    n = b.page
    b.save()
    assert n % 2 == 0 and n == PAGES, f"expected {PAGES} pages, produced {n}"
    cover = os.path.join(DIST, f"before-the-sermon_cover_6x9_{n}pp.pdf")
    spine, W, H = build_cover(cover, n)
    hc = os.path.join(DIST, f"before-the-sermon_cover-HARDCOVER_6x9_{n}pp.pdf")
    hs, HW, HH = build_cover(hc, n, hardcover=True)
    print(f"interior : {interior}\n           {n} pages, 6 x 9 in, "
          f"{'colour' if COLOR_INTERIOR else 'B&W on cream'}, no bleed")
    print(f"cover    : {cover}\n           paperback {W/inch:.3f} x {H/inch:.3f} in "
          f"incl. bleed, spine {spine/inch:.4f} in")
    print(f"hardcover: {hc}\n           {HW/inch:.3f} x {HH/inch:.3f} in incl. "
          f"{HC_WRAP/inch:.2f} in wrap, hinge {HC_HINGE/inch:.2f} in, spine "
          f"{hs/inch:.3f} in  \u2014 CONFIRM AGAINST KDP'S TEMPLATE BEFORE UPLOAD")


if __name__ == "__main__":
    main()
