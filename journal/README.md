# The Skill Seeker Journal — print-ready product

The paper companion to `skill_seeker_ai.py`. The app helps you pick the next
skill; this journal is the twelve weeks that come after you pick it.

Two upload-ready PDFs live in `dist/`. Nothing else needs doing to them.

| File | What it is | Upload as |
|---|---|---|
| `dist/skill-seeker-journal_interior_6x9_128pp.pdf` | 128 pages, 6 × 9 in, no bleed | KDP **Manuscript** |
| `dist/skill-seeker-journal_cover_6x9_128pp.pdf` | 12.538 × 9.250 in full wrap, 0.125 in bleed, 0.2883 in spine | KDP **Book Cover** |

## Print specification

* **Trim size** 6 × 9 in (15.24 × 22.86 cm) — KDP's most common, cheapest tier
* **Page count** 128 (even, as required; multiple of 4)
* **Interior** black & white on white paper, 100% vector, no images
* **Margins** inside/gutter 0.75 in, outside 0.55 in, top 0.62 in, bottom 0.66 in
  (KDP's minimum for 24–150 pages is 0.375 in inside, 0.25 in outside — this
  clears both comfortably). Margins mirror: gutter is on the left on odd
  pages, on the right on even pages.
* **Bleed** none on the interior; 0.125 in on all four sides of the cover
* **Spine** 128 × 0.002252 in = 0.2883 in, with spine text (KDP allows it from
  79 pages)
* **Barcode** a 2 × 1.2 in white area is reserved in the bottom-right of the
  back cover, where KDP prints the barcode
* **Fonts** EB Garamond, Inter and Space Grotesk — all SIL OFL 1.1, all fully
  embedded and subset. No base-14/unembedded fonts (KDP rejects those).
* **Greys** nothing lighter than 22% K or between 85–99% K, so every tone
  halftones predictably on a black & white press.

## What's inside the journal

* **1–16** front matter: how to use it, the SEEK loop, the five laws, the
  skill-selection lab, a signed charter, an honest baseline, the 12-week map
* **17–112** the core: 12 weeks × (1 Week Brief + 6 Daily Lab pages + 1 Week
  Debrief) = **72 guided practice sessions**
* **113–128** back matter: the twelve-week debrief, evidence ledger, resource
  log, wins log, stuck→solved tracker, people and asks, dot-grid notes, and a
  "your next twelve weeks" page

## Rebuilding / customising

```bash
pip install reportlab
python3 journal/build_journal.py
```

The four things most people want to change are the first four lines of the
config block at the top of `build_journal.py`:

```python
AUTHOR  = "Gao Kab"                # cover, spine, title page
IMPRINT = "The Skill Seeker Lab"   # publisher line on the copyright page
YEAR    = "2026"
ISBN    = ""                       # leave empty to use a free KDP ASIN
```

`AUTHOR` is the name on the cover, spine, title page and copyright page;
`IMPRINT` is the publisher line, kept separate so the book can be credited to a
person while still being published under the lab. The cover title auto-shrinks to fit, and the spine width and cover dimensions are
recalculated from the page count on every build, so a change to the page count
never desynchronises the cover.

The build asserts that the interior comes out to exactly 128 even pages and
fails loudly if a layout change breaks that.

### Changing trim size

Set `PW, PH` and re-check `M_GUT` against KDP's inside-margin table for the
resulting page count (24–150 → 0.375 in, 151–300 → 0.5 in, 301–500 → 0.625 in).
`PPI` (0.002252 in/page) is the white-paper, black-ink figure; use 0.0025 for
cream paper and 0.002347 for colour interiors.

## Font licences

`assets/fonts/` carries the SIL Open Font Licence 1.1 text for each family
(`OFL-*.txt`). OFL fonts may be embedded in a PDF and sold in printed form.
The `.ttf` files are static instances cut from the Google Fonts variable
originals with `fonttools varLib.instancer`.
