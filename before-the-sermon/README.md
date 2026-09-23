# Before the Sermon — Sitting With Scripture · print-ready product

A guided reading notebook: six questions, repeated across 52 facing-page spreads,
to help someone sit with a passage of Scripture before anyone explains it. Not a
devotional, commentary, or theology guide. It never interprets the text.

Three upload-ready PDFs live in `dist/` — one interior, two covers (paperback and hardcover share the interior).

| File | What it is | Upload as |
|---|---|---|
| `dist/before-the-sermon_interior_6x9_128pp.pdf` | 128 pages, 6 × 9 in, no bleed | KDP **Manuscript** |
| `dist/before-the-sermon_cover_6x9_128pp.pdf` | paperback: 12.570 × 9.250 in full wrap, 0.125 in bleed, 0.320 in spine | KDP **Paperback → Book Cover** |
| `dist/before-the-sermon_cover-HARDCOVER_6x9_128pp.pdf` | hardcover: 14.168 × 10.020 in, 0.51 in wrap, 0.40 in hinges, 0.348 in spine, white paper | KDP **Hardcover → Book Cover** |

> **Hardcover geometry — confirm before upload.** KDP publishes the wrap (0.51 in)
> and hinge (0.40 in); the spine formula (pages × 0.002252 + 0.06) is the consensus
> of two third-party calculators, not KDP's page. Run KDP's cover calculator for
> 6 × 9 / 128 pages / white and compare its template to these three numbers. If
> any differ, set `HC_WRAP`, `HC_HINGE`, `HC_SPINE` in `build_notebook.py` and
> rebuild. KDP's previewer rejects a mismatched hardcover cover, so this is a
> two-minute check, not a risk.

## Where the words came from

Every sentence of positioning, audience, voice and purpose is **your own copy**,
recovered from the compiled `Home.tsx` in the site bundle (`index-A6JIjT7X.js`).
The palette and typefaces are from the site's CSS variables. The concept
document is `CONCEPT.md` beside this file.

The six questions are a **merge**: the interior mockup's question form, with its
#1/#2 overlap removed and the website's "identify assumptions you may be
bringing" prompt carried across. Change them in the `PROMPTS` list at the top of
`build_notebook.py` — it's one edit and every spread updates.

Copy written **new for print** (not recovered — read it, and replace anything
that isn't in your voice):

* p2 — gift page: "If this came as a gift" · For / From / On / Because · "No one has to finish it. Someone only has to open it."
* p5 — "There is no right pace for this…"
* p10 — the whole *Before you begin* page, and "You are never being tested here."
* p13 — the *How to use a spread* explanations, and "Turn the page."
* the two closing prompts on every spread — "What will you sit with longer?" is
  the site's *Decide* movement; "What might this text be asking of you?" is from
  the mockup
* p118–119 subtitles, p126 *At the end* note
* back cover: "Sit with the text before anyone explains it."
* the one-line hints under each of the six questions

## Print specification

* **Trim** 6 × 9 in · **128 pages** · **black & white on cream paper** — the
  mockups' warm stock. In B&W the site's terracotta becomes a warm mid-grey.
* `COLOR_INTERIOR = True` switches to the terracotta accent. KDP colour interiors
  are **white paper only** and cost ~$4.10 to print instead of ~$2.40, so you can
  have cream paper *or* colour ink, not both. Cream is the default because the
  paper *is* the aesthetic. The spine width recalculates automatically.
* **Margins** gutter 0.75 in, outside 0.55 in (KDP minimums 0.375 / 0.25),
  mirrored across the spread.
* **Spine** 128 × 0.0025 in (cream) = 0.320 in, with spine text.
* **Fonts** Cormorant Garamond, Crimson Text, Lato — SIL OFL 1.1, licence texts
  in `assets/fonts/`, all embedded and subset. No unembedded fonts.
* **Greys** nothing lighter than ~21% K.
* Verified: zero elements outside KDP's 0.25 in safe area on all 128 pages and
  the cover; every spread opens on a left-hand page.

## The cover, honestly

Your mockup is cream linen with gold foil and a ribbon. **KDP can't make that.**
This cover reproduces the lockup — BEFORE / *the* / SERMON in a printed
gold-ochre on cream, double hairline frame — as a matte paperback or case-
laminate hardcover. It reads as the same design; it is not foil on cloth. Real
linen, foil and a sewn ribbon means offset printing with a book manufacturer at
a few hundred copies minimum. The interior PDF works unchanged for that too.

## Structure

* **1–13** half title, title, copyright, belongs-to, *What this notebook is*,
  *What makes it different* (does-not / purpose / voice), *Three movements*,
  *Before you begin*, a 52-row **Readings** index, *How to use a spread*
* **14–117** 52 spreads. Left page: Passage · Date, questions 1–3. Right page:
  questions 4–6, then *Before you close the book*.
* **118–128** *Passages I keep returning to*, *Questions I still carry*, six
  *Sitting longer* overflow pages, a closing note, About, colophon

## Rebuilding

```bash
pip install reportlab
python3 before-the-sermon/build_notebook.py
python3 before-the-sermon/make_preview.py     # optional contact sheet
```

`AUTHOR`, `IMPRINT`, `YEAR`, `ISBN`, `COLOR_INTERIOR`, `READINGS` and `PROMPTS`
are the config block at the top of the script. The build asserts an even
128-page count and that the front matter ends on page 13 so the first spread
opens on a left-hand page.
