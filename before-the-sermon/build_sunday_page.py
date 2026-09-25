#!/usr/bin/env python3
"""The Sunday Page — the free printable spread (lead magnet). One page, letter
and A4, B&W. Same six questions as the notebook, pulled from build_notebook."""
import os, sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_notebook as N

def build(path, size):
    N.register_fonts()
    W, H = size
    c = canvas.Canvas(path, pagesize=size)
    c.setTitle("The Sunday Page — Before the Sermon")
    c.setAuthor("Before the Sermon")
    M = 0.85 * inch
    x0, x1 = M, W - M
    cw = x1 - x0
    y = H - M

    def kick(s, yy, size=7.0, color=N.MID, x=None, w=None, align="l"):
        x = x0 if x is None else x; w = cw if w is None else w
        c.setFont(N.UI, size); c.setFillColor(color)
        tr = 1.9
        tot = sum(pdfmetrics.stringWidth(ch, N.UI, size) + tr for ch in s.upper()) - tr
        cx = {"c": x + (w - tot) / 2, "r": x + w - tot}.get(align, x)
        for ch in s.upper():
            c.drawString(cx, yy, ch); cx += pdfmetrics.stringWidth(ch, N.UI, size) + tr
    def line(yy, x=None, w=None, col=N.RULE, lw=0.5):
        x = x0 if x is None else x; w = cw if w is None else w
        c.setStrokeColor(col); c.setLineWidth(lw); c.line(x, yy, x + w, yy)

    # head
    kick("Before the Sermon  ·  The Sunday Page", y, 7.2, N.MID, align="c")
    y -= 26
    c.setFont(N.DISP_SB, 22); c.setFillColor(N.INK)
    c.drawCentredString(W / 2, y, "Read it twice. Then answer these.")
    y -= 18
    c.setFont(N.BODY_I, 10.5); c.setFillColor(N.MID)
    c.drawCentredString(W / 2, y, "Before the sermon, the summary, or the commentary. No right answers.")
    y -= 22
    # ornament
    c.setStrokeColor(N.ACCENT); c.setLineWidth(0.6)
    c.line(W/2 - 32, y, W/2 - 6, y); c.line(W/2 + 6, y, W/2 + 32, y)
    c.setFillColor(N.ACCENT); c.circle(W/2, y, 1.5, stroke=0, fill=1)
    y -= 30
    # passage / date
    c.setFont(N.DISP_I, 12); c.setFillColor(N.MID)
    c.drawString(x0, y, "Passage"); e = x0 + pdfmetrics.stringWidth("Passage", N.DISP_I, 12) + 6
    line(y - 3, e, x0 + cw * 0.62 - e)
    c.drawString(x0 + cw * 0.70, y, "Date"); e = x0 + cw * 0.70 + pdfmetrics.stringWidth("Date", N.DISP_I, 12) + 6
    line(y - 3, e, x1 - e)
    y -= 16
    line(y, col=N.INK, lw=0.7)
    y -= 6

    # six questions, distributed to the closing block
    NL = 3
    qh = 13 + 11.6 + 2 + NL * 17.5
    closing_h = 16 + 2 * 26
    foot = M + 30
    avail = y - foot - closing_h
    gap = (avail - 6 * qh) / 6
    for i, (q, hint) in enumerate(N.PROMPTS, 1):
        y -= gap
        c.setFont(N.DISP_SI, 13.5); c.setFillColor(N.ACCENT)
        num = f"{i}."; c.drawString(x0, y, num)
        nx = x0 + pdfmetrics.stringWidth(num, N.DISP_SI, 13.5) + 5
        c.drawString(nx, y, q)
        y -= 12.5
        c.setFont(N.BODY, 8.6); c.setFillColor(N.MID); c.drawString(nx, y, hint)
        y -= 2
        for _ in range(NL):
            y -= 17.5; line(y)
    # closing
    y -= 22
    c.setFont(N.DISP_SI, 12); c.setFillColor(N.MID); c.drawString(x0, y, N.CLOSING[0])
    for q in N.CLOSING[1]:
        y -= 18
        c.setFont(N.BODY_I, 9.2); c.setFillColor(N.INK); c.drawString(x0, y, q)
        y -= 8; line(y)
    # foot
    kick("Free to print and share  ·  @beforesermon  ·  the notebook has fifty-two of these", M - 4, 6.4, N.MID, align="c")
    c.showPage(); c.save()

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
    build(os.path.join(out, "the-sunday-page_letter.pdf"), letter)
    build(os.path.join(out, "the-sunday-page_A4.pdf"), A4)
    print("wrote the-sunday-page_letter.pdf and _A4.pdf")
