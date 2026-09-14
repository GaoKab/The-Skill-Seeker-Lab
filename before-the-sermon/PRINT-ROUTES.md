# How to make it: the print routes, with numbers

*Researched 14 Sep 2026. Costs are Amazon.com / US unless stated; verify in each
vendor's live calculator before ordering — they change.*

The question: the mockup is a cream **linen** hardcover with **gold foil** and a
**ribbon**. Amazon can't make that. So — go find a manufacturer, turn it into
something Amazon can make, or manufacture it and sell it through Amazon anyway?

**Short answer: launch on KDP now (paperback + case-laminate hardcover), and
only order the linen/foil/ribbon edition once KDP sales prove demand.** The
reasoning and the numbers are below.

---

## The six routes

### A · KDP paperback, cream paper — *built, ready*
| | |
|---|---|
| Object | matte softcover, cream stock, cover printed in ink (cream + gold-ochre) |
| Print cost | $1.00 + 128 × $0.012 = **$2.54** |
| At $14.99 list | 60% × 14.99 − 2.54 = **$6.45 per copy** |
| Upfront | $0 · inventory $0 · Prime-eligible · live in ~72 h |
| What you lose vs mockup | hardness, cloth, foil, ribbon |

### B · KDP hardcover (case laminate) — *one cover rebuild away*
| | |
|---|---|
| Object | rigid boards, printed laminated cover, **white paper only**, no ribbon |
| Print cost | $5.65 + 128 × $0.012 = **$7.19** |
| At $22.99 list | 60% × 22.99 − 7.19 = **$6.60 per copy** |
| At $24.99 list | **$7.80 per copy** |
| Upfront | $0 · inventory $0 · same listing as the paperback |
| What you lose vs mockup | cloth texture, real foil, ribbon, cream paper |

This is the closest Amazon-native object. From two feet away a well-printed
cream cover with gold-ochre type reads as the mockup. Cover needs the hardcover
wrap: KDP adds ~0.625 in board overhang on each outer edge and ~0.375 in hinge
channels beside the spine, and the spine includes board thickness. That's a
`BLEED`/`HINGE` change plus a rebuild in `build_notebook.py`.

### C · IngramSpark hardcover (case laminate or jacketed)
| | |
|---|---|
| Object | as B, optionally with a dust jacket; **no cloth** |
| Print cost | ≈ **$6.00–6.50** at 128pp (IS quotes ~$8.50 at 300pp; Feb-2026 rates rose) |
| Economics | you set a 40–55% wholesale discount; at $22.99 / 40% ≈ $7.50; at 55% ≈ $4.00 |
| Gets you | bookstores, libraries, Amazon too. Setup/revision fees. More admin. |

Worth adding **after** launch if bookstores or churches want to order in bulk.
Not a first move.

### D · Lulu linen wrap hardcover — *the only print-on-demand linen*
| | |
|---|---|
| Object | real cotton-poly linen (6 colours), foil title **on the spine only**, dust jacket |
| Print cost | from ≈ **$14** for B&W hardcover (confirm in Lulu's calculator) |
| The catch | **Amazon does not accept any Lulu hardcover.** Linen and casewrap route only to Ingram, or you sell direct (Lulu storefront / Shopify). |
| Also | no foil on the front cover — the lockup would be printed on the jacket |

A zero-inventory way to offer a genuine linen edition **direct**, at $34.99+.
Not an Amazon route.

### E · Offshore offset (PrintNinja and similar) — *the actual mockup*
| | |
|---|---|
| Object | cloth over boards, foil-stamped front and spine, satin ribbon, head/tail bands, cream paper |
| MOQ | **250**; pricing becomes sane at **500–1,000** |
| Print cost | case-wrap 6×9 200pp ≈ $4–6 at 1,000. Cloth + foil + ribbon + cream stock + freight: budget **$7–12 per unit landed** at 500–1,000. Get their quote — 1 business day. |
| Upfront | **≈ $4,000–8,000** · lead time **4–6 wks production + 6–8 wks ocean** (≈ 1 wk air, at a cost) |
| Then you hold stock | and sell it either via Amazon FBA or direct |

**Selling manufactured stock on Amazon (FBA):** 15% referral + **$1.80** book
closing fee + ≈ **$3.35** fulfilment (small standard 12–16 oz incl. 2026 fuel
surcharge) + inbound and storage. At **$29.99**: 4.50 + 1.80 + 3.35 + ~0.70 =
$10.35 in fees → **≈ $10.60 per copy** on a $9 unit. Better per copy than KDP,
with $5–8k of capital and three months in front of it. Professional seller
account: $39.99/mo.

### F · Domestic short-run (Gorham, Bookmobile, 100–250 copies)
| | |
|---|---|
| Object | cloth + foil, ribbon on request, made in the US, ~2–3 weeks |
| Print cost | Gorham, 6×9 150pp cloth with foil: **$45.19 at 100, $38.96 at 250, $35.45 at 500** (site currently paused for new orders) |
| Use | proof copies, gifts, a launch batch of 25 — **not** a retail edition |

---

## Side by side (Before the Sermon, 128pp, per copy)

| Route | Object fidelity | Print cost | Sell at | You keep | Upfront | Time to sale |
|---|---|---|---|---|---|---|
| A KDP paperback | ★★☆☆☆ | $2.54 | $14.99 | $6.45 | $0 | days |
| B KDP hardcover | ★★★☆☆ | $7.19 | $24.99 | $7.80 | $0 | days |
| C IngramSpark HC | ★★★☆☆ | ~$6.25 | $24.99 | $4–8 | ~$100 | 1–2 wks |
| D Lulu linen | ★★★★☆ | ~$14 | $34.99 | ~$15 (direct only) | $0 | days, **no Amazon** |
| E Offshore cloth+foil | ★★★★★ | $7–12 | $29.99 (FBA) | ~$10.60 | $4–8k | 10–14 wks |
| F US short-run | ★★★★★ | $35–45 | — | negative | $4k+ | 2–3 wks |

---

## Recommendation

**1. Launch both products on KDP now.** Skill Seeker as a paperback. Before the
Sermon as paperback **and** hardcover on one listing — Amazon shows both
formats, the hardcover at $22.99–24.99 catches the buyer who wants the object,
the paperback at $14.99 catches everyone else. Zero capital, Prime shipping,
you learn the real demand in 60–90 days instead of guessing it.

**2. Do not order the linen edition first.** The only way to get the mockup
object at a sellable unit cost is 500–1,000 copies offshore — $4–8k and three
months — before a single sale has told you whether anyone wants it. That is the
classic way self-publishers lose money: a garage full of beautiful books.

**3. Earn the premium edition.** If the KDP hardcover moves — say 150–200
copies in the first 90 days, or a church/group asks about bulk — get the
PrintNinja quote, order 500, list it as a *Linen Edition* at $29.99–34.99 via
FBA on the same product page, and sell the first batch to the people who
already bought the paperback. The KDP sales are your market research and your
launch list.

**4. Optional, anytime:** put the Lulu linen wrap up for direct sale from the
Before the Sermon site. No stock, real linen, $34.99 — a signal about whether
the premium tier has buyers, at zero risk.

What I would *not* do: IngramSpark on day one (admin for no gain until
bookstores ask), or a US short-run for retail (the unit cost is above the
retail price).

---

## Sources
KDP hardcover costs — <https://kdp.amazon.com/en_US/help/topic/GHT976ZKSKUXBB6H>
KDP 2026 paperback/hardcover rates — <https://cambric.pub/guides/kdp-printing-cost-guide/> · <https://theauthorcentral.com/blog/kdp-hardcover-printing-cost/>
KDP hardcover specs (white only, 75–550pp, wrap/hinge) — <https://coverlabpro.com/kdp-cover-size-guide.html> · <https://bookcoverslab.com/kdp-cover-templates/6x9-hardcover>
Lulu linen wrap — <https://www.lulu.com/products> · Lulu distribution exclusions (no Amazon for hardcovers) — <https://help.lulu.com/en/support/solutions/articles/64000267552-global-distribution-print-exclusions>
IngramSpark 2026 rates — <https://simplelifecalc.com/guides/ingramspark-print-costs-explained> · <https://blog.bublish.com/ingramspark-raising-prices-in-2026>
PrintNinja MOQ, options, lead time, pricing — <https://printninja.com/printing-products/hardcover-book-printing/> · <https://printninja.com/cloth-and-faux-leather/>
Gorham cloth hardcover price chart — <https://gorhamprinting.com/prices-book-printing/price-charts.html>
Bookmobile short-run — <https://www.bookmobile.com/art-book-printing/short-run-hardcover-book-printing/>
Amazon book referral + closing fee — <https://www.dotcomreps.com/blog/amazon-fba-fees-books> · FBA 2026 fees + surcharge — <https://warehousingcosts.com/guides/amazon-fba-fulfillment-fees> · <https://amzprep.com/amazon-fba-fees/>
