# KDP upload sheet

Everything you need to paste into the Kindle Direct Publishing paperback flow.
Start at <https://kdp.amazon.com> → **Create** → **Paperback**.

---

## 1 · Paperback Details

**Language** English

**Book Title**
```
The Skill Seeker Journal
```

**Subtitle**
```
12 Weeks, 72 Guided Sessions, One Skill You Actually Keep — A Practice Journal for Learning Anything
```

**Series** leave blank · **Edition number** 1

**Author** — whatever you set as `AUTHOR` in `build_journal.py`. It currently
reads *The Skill Seeker Lab*. If you want it credited to you, change that
constant, rebuild, and use the same name here. **The name on the cover and the
name in this field must match**, or KDP flags it in review.

**Description** (paste as-is; KDP accepts basic HTML, ~4000 char limit)

```html
<b>Most learning fails quietly.</b> You pick four skills, buy three courses, and six weeks later you cannot name a single thing you made.

This is a working notebook for the twelve weeks after you decide. One skill. Six short sessions a week. Seventy-two in total.

<b>It starts by ending the deciding.</b> A skill-selection lab walks you through three candidates and scores each one on pull, payoff, proof and practicality, so you choose once and stop reopening the question. Then you sign a charter with a real number, a real time and a real place — because intentions evaporate and commitments with a time survive.

<b>Then it gets out of your way.</b> Every week opens with a two-minute brief and closes with an honest debrief. In between are six daily lab pages built around the most valuable field in the whole journal: the Friction Log. Not what you studied. Not how long you sat there. <i>Exactly where it stopped working, and what you will try next time.</i> That one question, asked seventy-two times, is what turns practice into skill.

<b>What's inside</b>
• A skill-selection lab and scoring grid that ends the deciding
• A signed charter with a time, a place and a number
• A twelve-week map you can sketch in pencil
• 12 Week Briefs and 12 honest Week Debriefs
• 72 daily lab pages built around the Friction Log
• An Evidence Ledger — proof of what you made, not hours you logged
• Resource log, wins log, stuck-to-solved tracker and people-to-ask list
• A twelve-week debrief and a page that sets up your next twelve

<b>Details</b> 128 pages · 6 × 9 inches · matte cover · lined and structured interior · undated, so you can start on any Monday you like.

No streaks to break. No app to open. Pick one skill, give it twelve weeks, and let the log tell you the truth.
```

**Publishing Rights** → *I own the copyright and hold the necessary
publishing rights.*

**Primary audience** → Not for children · Adult content: **No**

**Categories** (choose three)
1. Self-Help → Personal Growth → Success
2. Business & Money → Skills
3. Education & Teaching → Studying & Workbooks → Study Skills

**Keywords** (7 slots, one per box)
```
skill building journal
learning journal for adults
90 day practice notebook
deliberate practice planner
undated self improvement journal
habit and skill tracker
career change workbook
```

---

## 2 · Paperback Content

| Field | Value |
|---|---|
| Print ISBN | **Get a free KDP ISBN** (or paste your own into `ISBN` in `build_journal.py`, rebuild, then enter it here) |
| Publication date | leave blank |
| Print options | **Black & white interior with white paper** |
| Trim size | **6 × 9 in (15.24 × 22.86 cm)** |
| Bleed | **No bleed** |
| Cover finish | **Matte** (glossy also works; matte suits the dark cover better) |
| Manuscript | upload `dist/skill-seeker-journal_interior_6x9_128pp.pdf` |
| Book cover | **Upload a print-ready PDF cover** → `dist/skill-seeker-journal_cover_6x9_128pp.pdf` |

> Choosing a different paper type or trim size changes the required spine
> width and invalidates the cover file. If you do, edit `PPI` / `PW` / `PH` in
> `build_journal.py` and rebuild before uploading.

Run **Launch Previewer** and page through it. The previewer will confirm the
128-page count, the margins and the spine fit.

---

## 3 · Paperback Rights & Pricing

* **Territories** → All territories (worldwide rights)
* **Primary marketplace** → Amazon.com

Printing cost for a 128-page 6 × 9 B&W paperback is roughly **$2.55** on
Amazon.com. KDP pays 60% of list price minus printing cost, so:

| List price | Printing | Your royalty |
|---|---|---|
| $9.99 | ~$2.55 | ~$3.44 |
| $11.99 | ~$2.55 | ~$4.64 |
| $12.99 | ~$2.55 | ~$5.24 |
| $14.99 | ~$2.55 | ~$6.44 |

$11.99–$14.99 is the normal band for a structured guided journal; plain lined
notebooks sit lower, but this one has real content in it. Check the live
printing cost KDP shows you — the figures above are indicative.

---

## Printing it yourself instead

The same two files work at any print shop. Tell them:

* interior: 128pp, 6 × 9 in, single-sided-imposed duplex, black on white,
  **no scaling / print at 100%** (the margins are already asymmetric for the
  gutter, so "fit to page" would ruin them)
* cover: 12.538 × 9.25 in, full colour, 0.125 in bleed already included, trim
  marks not included
* binding: perfect bound or, for a journal that lies flat while you write in
  it, wire-o or lay-flat — worth the extra if it's for your own use

---

## Other storefronts

The same PDFs upload as-is to **IngramSpark** and **Lulu**, both of which use
the same 6 × 9 trim and accept a full-wrap cover PDF. IngramSpark computes
spine width slightly differently (paper stock varies), so regenerate the cover
with their spine figure in `PPI` if you go that route.
