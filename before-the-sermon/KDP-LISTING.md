# KDP upload sheet — Before the Sermon

<https://kdp.amazon.com> → **Create** → **Paperback**.

## 1 · Paperback Details

**Language** English

**Book Title**
```
Before the Sermon
```
**Subtitle**
```
Sitting With Scripture — A Guided Reading Notebook for Engaging the Bible Slowly, Thoughtfully, and Without Intimidation
```
**Author**
```
Gao Kab
```
Must match the cover. To change it, edit `AUTHOR` in `build_notebook.py`, rebuild, update here.

**Description** (paste as-is)
```html
<b>Sit with the text before anyone explains it.</b>

Before the Sermon: Sitting With Scripture is a guided reading notebook designed to help people engage Scripture slowly, thoughtfully, and without intimidation. It is not a devotional, commentary, or theology guide. It does not explain passages or tell readers what to believe.

Instead, it offers a structured way to sit with the text, notice what is written, reflect honestly, and build confidence as a reader — before sermons, summaries, or conclusions. The notebook is meant to be used alongside the Bible, not instead of it.

<b>How it works</b>
Fifty-two facing-page spreads, each with the same six questions: what the text actually says, what keeps pulling your attention, what you are bringing to it, what confused you, what you felt, and what you think the text is exploring. The questions repeat on purpose — you are not meant to get better at the questions, you are meant to get better at reading.

<b>Who it's for</b>
• People who feel intimidated by the Bible
• Readers who don't know how to read Scripture on their own
• Christians who want to slow down their reading
• Seekers or non-Christians who are curious but cautious
• Anyone who wants to engage the Bible without pressure, performance, or expertise

No prior knowledge, belief, or background is assumed.

<b>This notebook does not</b> interpret Scripture for you, push application or action, or assume belief or expertise. <b>Its purpose is to</b> change how you read, train attention and patience, allow meaning to surface slowly, and build honest reading confidence.

Confusion, silence, and "I don't know" are treated as valid outcomes.

<b>Details</b> 128 pages · 6 × 9 inches · cream paper · 52 guided reading spreads · a readings index, overflow pages, and space for the questions you still carry · undated.

A reading companion, not a replacement for sermons.
```

**Publishing Rights** I own the copyright · **Primary audience** not for children · Adult content: No

**Categories**
1. Christian Books & Bibles → Christian Living → Devotionals *(closest shelf; the description makes clear it isn't one)*
2. Christian Books & Bibles → Bible Study & Reference → Bible Study → Guides
3. Religion & Spirituality → Christian Books & Bibles → Christian Living → Spiritual Growth

**Keywords**
```
bible study journal for beginners
scripture reading notebook
guided bible reading journal
bible journaling prompts
inductive bible study notebook
sermon notes journal
christian journal for seekers
```

## 2 · Paperback Content

| Field | Value |
|---|---|
| Print ISBN | Get a free KDP ISBN (or set `ISBN` in the script, rebuild, paste here) |
| Print options | **Black & white interior with cream paper** |
| Trim size | **6 × 9 in (15.24 × 22.86 cm)** |
| Bleed | **No bleed** |
| Cover finish | **Matte** — essential for this cover; glossy will look wrong on cream |
| Manuscript | `dist/before-the-sermon_interior_6x9_128pp.pdf` |
| Book cover | Upload a print-ready PDF → `dist/before-the-sermon_cover_6x9_128pp.pdf` |

> Cream paper changes the spine width (0.320 in vs 0.288 in on white). The
> cover file already uses the cream figure. If you pick white paper, or switch
> to a colour interior, rebuild first.

## 2b · Hardcover (same listing, second format)

After the paperback is created, choose **Create hardcover** on the same title.

| Field | Value |
|---|---|
| Print options | **Black & white interior, white paper** (KDP hardcover has no cream) |
| Trim size | 6 × 9 in |
| Bleed | No bleed |
| Cover finish | **Matte** |
| Manuscript | the same `dist/before-the-sermon_interior_6x9_128pp.pdf` |
| Book cover | `dist/before-the-sermon_cover-HARDCOVER_6x9_128pp.pdf` — **first run KDP's cover calculator and confirm wrap 0.51 / hinge 0.40 / spine 0.348** (see README) |
| List price | **$24.99** → print $7.19 → royalty ≈ $7.80 |

Order an **author proof** of both formats before publishing (~$8 + shipping).

## 3 · Rights & Pricing

All territories · Amazon.com primary.

Printing **$2.54** for 128pp B&W cream 6 × 9 ($1.00 fixed + $0.012/page; check KDP's live figure).

| List | Royalty |
|---|---|
| $12.99 | ~$5.25 |
| $14.99 | ~$6.45 |
| $16.99 | ~$7.65 |

Guided Scripture notebooks with real structure sit at $14–18; the cream stock
and the restraint of the design support the upper end.

## Printing it yourself

Same two files at any print shop: interior 128pp 6 × 9 duplex on **cream or
natural stock**, print at 100% (margins are mirrored; never "fit to page");
cover 12.57 × 9.25 in full colour, bleed included. For the object in the
mockup — linen, foil, ribbon — you want a short-run book manufacturer; send
them the same interior PDF and ask for a cover die-line to their spec.
