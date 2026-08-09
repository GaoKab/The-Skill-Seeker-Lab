# EWAH Hardware Development — HW-01 Signature Emblem System

Phase 01 of the hardware family: **the first physical EWAH product, developed before the hats.** Goal: luxury fashion hardware that becomes recognizable as EWAH design language (the way Hermès' H or Chanel's CC hardware is), not a logo pin. Full founder brief received August 2026; this document adds the engineering critique, the proposed system architecture, manufacturer research, and the RFQ.

## Hardware family roadmap (as briefed)

HW-01 Signature Brooch (now) → HW-02 mini stud · HW-03 magnetic emblem · HW-04 zip pull · HW-05 drawcord hardware · HW-06 premium button · HW-07 rivet. One visual language across all.

## Founder spec (HW-01, as briefed)

- Interlocked EWAH emblem; minimal, sculptural, architectural; no flourishes or sharp edges
- **24–26 mm diameter, ~3 mm thick**; solid brass preferred (zinc alloy fallback)
- Finishes: brushed antique gold (primary), gunmetal, matte black (RONE Reverence)
- Rounded edges, fabric- and skin-safe
- One face, four backs: A locking pin (shawls/wraps/dresses) · B low-profile screw/factory mount (hats — no exposed pin inside crown) · C magnetic (future outerwear) · D sew-on plate (permanent apparel)
- Hidden luxury detail: back engraving (EWAH / SCULPT · FLOW · FREEDOM / SCULPTED FOR MOVEMENT) — a discovery for the wearer, not marketing
- Jewellery-grade packaging: rigid box (cream or matte black), gold foil, microfiber pouch, certificate card
- Evaluation on receipt: visual quality, luxury feel, weight, comfort, attachment security, scratch/sweat/plating durability, ease of removal, compatibility with hats/wraps/dresses, packaging

## Engineering critique (industrial-designer pass — challenges and fixes)

1. **Openwork monogram will snag and won't cast crisply at 25 mm.** The interlocked emblem's strokes at this scale are ~1 mm — open (pierced) construction risks casting fill defects, bent strokes in wear, and snagging on knits and mesh (EWAH's core fabrics). **Fix: make Version 1 a solid disc with the emblem in raised relief — a seal/medallion, not a cut-out.** Crisper rendering, zero snag, structurally rigid at 3 mm, and the back stays flat for engraving. It also reads culturally rich (seal / coin / gold-weight lineage) without cliché. The pierced openwork version becomes a later fine-jewellery piece where it belongs.
2. **A flat 3 mm disc reads industrial, not jewellery.** **Fix: lens/dome profile** — ~3 mm at center tapering to ~2 mm at a rounded rim. Catches light like jewellery, feels finished in the hand, still low-profile on fabric.
3. **Manufacturing route matters more than material.** For a 25 mm relief medallion, **die-struck brass** (coin/insignia method) gives the sharpest emblem lines and modest tooling cost; lost-wax or MIM only if the design goes truly 3-D. Zinc die-casting is the budget fallback but softens detail — accept only after seeing struck brass side-by-side.
4. **Weight check (do the math before the supplier does):** 25 mm × ~2.5 mm average solid brass ≈ **10–11 g** — exactly the premium-feel range. Zinc alloy at the same geometry ≈ 8 g; noticeable but acceptable.
5. **Plating: specify PVD, not standard electroplate, for anything worn in sweat.** Brushed antique gold PVD (or heavy e-coat over plate) survives salt sweat and abrasion far longer than costume electroplate; it's also nickel-safe. Salt-spray test 24–48 h in the spec; plating thickness stated in microns on the quote.
6. **Pins must never meet performance knits.** A pin pierces elastane and starts runs. Scope Version A (locking pin) to **wovens only** — shawls, RONE crepe, jackets. On knits and technical fabrics, only B (mount), C (magnet), or D (sew-on). Write this on the spec sheet so no one "helpfully" pins a dress sample.
7. **Magnets (Version C): feasible, with three cautions** — N45–N52 pairs need corrosion-sealed coating (sweat kills bare neodymium), holding power drops fast with fabric thickness (>1.5 mm needs bigger magnets), and packaging needs the standard magnet-safety note. Keep for coats/outerwear as briefed; don't force it into v1.

## The bigger idea: the EWAH Dock system (proposed — this is the proprietary play)

The brief asks for one face with interchangeable backs. Take it one step further and **invert it: standardize the *garment side*, not the brooch side.**

- **The Dock:** a small, low-profile receiving fitting — a discreet reinforced eyelet/plate, sewn or riveted — built into EWAH products at a standard position: bucket hat side panel, RONE wrap crown edge, dress hem corner, jacket lapel, tote strap.
- **The Emblem head:** one medallion with a **quarter-turn (bayonet) lock** on its back that seats into any Dock. Insert, twist 90°, locked; twist back to release. No pin, no fabric damage, no snag, one-handed, secure under movement.
- **What this buys:** a true hardware *ecosystem* — one emblem travels across every EWAH and RONE product ("move your crown from your hat to your wrap"); garments ship with the subtle Dock and the emblem becomes a purchasable accessory (jewellery-margin revenue, gifting, colorway collecting); and the mechanism itself — not just the logo — becomes the recognizable, ownable signature. A quarter-turn medallion lock is patent/registered-design territory in a way a brooch never is.
- **Engineering:** the Dock is a ~10–12 mm anodized/PVD ring with two internal lugs; the emblem back carries the mating bayonet plate. Both parts die-cast or machined; pull-off in locked state ≥ 70 N; rotation detent so it can't self-release. Prototype alongside the classic pin version — the pin version still serves non-EWAH garments (a brooch anyone can wear on anything is the gateway; the Dock is the ecosystem).
- Quarter-turn beats magnets (secure under impact, no card/pacemaker concerns) and beats threads (fast, satisfying, one-handed — the "click" is part of the luxury).

**Recommended v1 scope:** solid relief medallion, dome profile, die-struck brass, PVD antique gold + matte black, with **two backs tooled: locking pin (A) and quarter-turn bayonet (proto of the Dock system)**. Screw-mount hat version (B) derives from the bayonet tooling. Magnet (C) and sew-plate (D) in round 2.

## Manufacturer research (July–Aug 2026)

| Supplier | Country | Profile | Notes for EWAH |
|---|---|---|---|
| **Micromet Srl** | Italy (luxury district) | Metal accessories specifically for high fashion/luxury houses; brass/bronze; premium finishing | The "trust anchor" quote — highest quality + EU legal reach; expect higher tooling/unit cost, possibly higher MOQs; ask about small-brand programs |
| **TALMUD** | China | Custom brooch manufacturer since 2005, OEM/ODM, accepts sample submissions | Mid-route candidate; verify luxury-grade plating (PVD) capability |
| Guangzhou/Dongguan/Shenzhen metal-hardware cluster | China | Deep capability: casting, die-striking, machining, PVD, laser engraving; MOQs often 100–500; tooling ~$100–500 | Source via verified-supplier search ("die struck brass badge PVD", "luxury metal fashion hardware OEM"); apply `11` §2 verification and `14` escrow rules |
| Yiwu accessories cluster (e.g., Jintang) | China | Badges, buckles, buttons at commodity scale | **Caution tier** — promotional-pin DNA; use only with a physical luxury reference sample in hand |
| Jewellery casters (local) | Botswana/SA or founder's market | Lost-wax brass casting, small runs | Wildcard for RONE-narrative limited editions ("cast in Botswana") — expensive per unit, priceless as story |

**RFQ fields (per the brief):** country · MOQ · prototype capability + cost · tooling cost and **EWAH ownership of tooling in writing** · lead time · luxury clients if disclosable (treat name-drops per `11` §2 — verify or ignore) · plating spec in microns + salt-spray results · communication quality across first 3 emails.

**Cost picture (typical, verify by quote):** tooling/die $100–500 one-time per face/back · prototypes $30–80 each · production $0.80–3.00/unit at 300–500 pcs (brass, PVD, China) — Italy roughly 3–5×. Packaging (rigid box + pouch + card) $1.50–4.00/set at small runs.

## ⚠️ EMBLEM CORRECTION GATE (before any CAD)

The emblem artwork on all boards contains a lettering error: **two E's instead of one** — the monogram does not correctly render E-W-A-H. Caught before vectors, CAD, or tooling exist, so cost ≈ zero. Two legitimate resolution paths for the identity designer + founder to choose:

1. **Strict correction:** redraw the interlock so E, W, A, H each appear exactly once. Safest for meaning (each letter carries a brand value: Strength · Flow · Form · Harmony — a missing or doubled letter breaks that story).
2. **Deliberate mirrored symmetry:** luxury monograms routinely mirror a letter for balance — Chanel's mirrored C's, Gucci's interlocked G's, Fendi's FF. A design where the E is intentionally mirrored as bookends *can* be legitimate — but only if W, A, and H are all genuinely present, and only as a *deliberate, documented* choice, not a preserved accident.

Either way: the corrected emblem must be re-verified letter-by-letter (E? W? A? H? once each, or mirrored by intent?) before the vector package is accepted — add this check to the acceptance of the designer's files. The CAD commission (`20`) does not start until the corrected vector exists.

## ✅✅ REFINEMENT v2 — OFFICIAL: OVAL OPENWORK EMBLEM (see `boards/hw01-medallion-oval-refinement.png`) — *geometry direction only; letterforms pending the correction gate above*

Second iteration supersedes the circular board below where they conflict. **Official direction: oval openwork medallion at the original emblem proportions** — true to the identity mark — in fine rounded-wire construction, antique gold, shown applied to the Air Sculpt and Layered Safari hats.

**What the oval + wire construction changes (engineering consequences, for the CAD brief):**
1. **Dimensions:** circular Ø25 mm no longer applies. Propose **~28 × 19 mm** (matches the identity emblem's proportions; similar visual mass to Ø25) — confirm against hat crown at scale.
2. **Construction route:** fine rounded-wire openwork = **lost-wax cast brass** (stamping can't produce round-section wire forms). Minimum wire section **Ø ≥ 1.5 mm**; consider a slightly deeper-than-wide (elliptical) section for stiffness across the long spans; the rim carries the structure.
3. **Weight:** wire openwork is much lighter than the solid-relief spec — expect **~4–6 g**, not 10–11 g. If premium heft matters, thicken the rim (the E/W/A/H wires stay fine); decide at the resin-print stage, in hand.
4. **Back engraving relocates:** there is no back plane on wire construction. SCULPT · FLOW · FREEDOM moves to the **outer rim band** (engraved around the oval rim edge) or a small integrated back bar — jeweler resolves in CAD.
5. **Snag discipline doubles:** open loops + fine wire on knits/mesh demands fully polished, radiused wire everywhere and the snag test against platform-A knit, mesh, AND hat brim fabric before approval.
6. **The oval turns the future Dock into a feature:** a quarter-turn lock with an oval face makes orientation *legible* — insert sideways, twist upright, seated. The "crowning" gesture becomes part of the product ritual. Keep for Phase 2, but design the rim's back with this in mind.

**Trade-off accepted with this direction:** fine-wire cast openwork is more jewellery, more identity-true, and more delicate than the bold pierced disc — slightly higher unit cost (casting + hand-finish), slightly lower durability tolerance. The evaluation criteria (scratch, sweat, attachment security, snag) now do real gatekeeping: **if the wire version fails wear testing on hats, the bold circular v1 below is the pre-approved fallback.** Both boards stay in the repo for exactly that reason.

---

## LOCKED v1 DESIGN (August 2026) — circular bold openwork — now the FALLBACK (see `boards/hw01-medallion-design-board.png`)

The founder's revised board locks the design and closes the review gate. **Founder decision: TRUE-TO-LOGO OPENWORK** — the interlocked emblem pierced within the ring, overruling the solid-relief-disc recommendation below. The revision resolves the original fragility objection by **bolding the letterforms (~2 mm strokes, fully interconnected)**; the openwork concern stands only as the mitigation list below.

**Confirmed key specs (from the board):** Ø 25.0 mm · 3.0 mm center / 2.0 mm rim · relief raised 0.4–0.6 mm · rim 1.8 mm (1.5–2.0 range) · smooth rounded bullnose edge · solid brass, 10–11 g · finishes: antique gold, gunmetal, matte black (PVD) · back engraving SCULPT · FLOW · FREEDOM perimeter ring on all versions · four backs (A pin/wovens, B hat screw-bayonet mount, C magnetic, D sew-on) · **no pins through performance knits** · **Dock quarter-turn system = Phase 2, not in v1 prototype** · gold/gunmetal: brushed field + polished rim + raised polished emblem; matte black: uniform matte + polished emblem tops.

**One spec ambiguity to resolve in CAD (the only open question):** the board says both "openwork" (front views show full piercing — see-through) and "raised 0.4–0.6 mm over recessed field" (implies a solid backing plane). Two valid readings: **(A) fully pierced** ring monogram (as rendered), or **(B) solid backplate with recessed field** behind raised letters. Recommendation: pierced (A) for pin/jewelry versions; the hat screw-mount version may need a small solid boss behind center for the fastener regardless — let the jeweler resolve in CAD and state the choice in the proportions rationale.

**Openwork engineering mitigations (carry into the CAD brief):** minimum stroke width ≥ 1.8 mm · every letter element connected to ring or neighbor (no cantilevers) · all pierced inner edges radiused + polished (snag-test against platform-A knit and mesh before approval) · manufacturing route becomes stamped + pierced brass or lost-wax cast (die-strike alone can't pierce) — get both quoted.

**Roadmap status:** Step 1 done (this lock) → Step 2 (vector from identity designer) is the active blocker. The board itself carries drafted versions of the three outreach emails (identity designer / 89 Carat Street / hardware RFQ) — consistent with `20` and the RFQ fields here.

---

## Hardware Design Review (gate before CAD commission — CLOSED by the lock above; kept for the record)

Seven decisions answered before the jeweler opens Rhino — so they design one object rather than discover it. Recommendations below; founder confirms or adjusts each.

| # | Question | Recommendation | Reasoning |
|---|---|---|---|
| 1 | Circular or organic outline? | **Circle** | The emblem itself is organic/interlocked; a circle frames it with architecture and reads coin/seal. Critically, the quarter-turn Dock needs rotational symmetry — an oval face would sit sideways mid-twist. The identity sheet's oval enclosure lives on *inside* the relief artwork; the medallion body is circular. (If the founder prefers the oval identity shape, it's viable for the pin version but complicates the Dock — decide here.) |
| 2 | Raised vs recessed? | **Emblem raised 0.4–0.6 mm over a lightly recessed field; two levels only** | Two-level relief die-strikes crisply; more levels muddy at 25 mm |
| 3 | Rim width? | **1.5–2.0 mm** at 25 mm diameter | Enough frame to read as a coin/seal without shrinking the emblem |
| 4 | Rim polished, center brushed? | **Yes — polished rim + brushed field** (gold/gunmetal). Matte black version: uniform matte with polished emblem top surfaces only | The classic luxury-coin contrast; controlled light-catch |
| 5 | Back engraving placement? | **Perimeter ring: SCULPT · FLOW · FREEDOM around the edge** | Works identically on the flat pin-back AND the Dock bayonet back (whose center is occupied by mechanism) — one engraving spec for all versions |
| 6 | Edge profile? | **Smooth rounded (bullnose)** | No coin knurling (abrasive against knits), no sharp bevel; comfortable against skin and fabric |
| 7 | One size or two? | **25 mm only for v1** | The 18 mm mini is HW-02 — don't double tooling cost before the design is validated in the wild |

## Expanded CAD deliverables (per design review feedback)

Beyond CAD + print + finishing notes, the commission also requires: **high-quality renders in all three finishes** and **a short written rationale for the chosen proportions and relief depths** — filed here as the start of the EWAH Atelier archive, so the reasoning survives for future revisits.

## Hardware review session (on prototype arrival — do NOT approve same-day)

Lay the prototypes on a table with: bucket-hat fabric candidates · black crepe (RONE) · performance jersey (platform A) · logo printouts · **two lighting conditions (daylight + warm indoor)**. Then judge:
- Does it feel expensive? · Does it catch too much light? · Too heavy? · Does it overpower the garment? · **Would someone wear it as jewelry on its own?**
Record verdicts in the revision log. This session carries the same weight as the CAD itself.

## Roadmap (locked sequence — minimizes rework)

1. Hardware Design Review — confirm the seven answers above
2. Emblem vector from identity designer *(blocking)*
3. Commission to the alum (`20`)
4. Receive + review CAD (renders judged against fabrics before tooling)
5. Prototype quotes from 3–5 luxury hardware manufacturers
6. Physical samples → hardware review session
7. Approve HW-01 Signature Medallion
8. Only then integrate into the first bucket-hat prototype

**Strategic note:** starting with the medallion means the first perfected asset is *reusable across decades of product* — hats, wraps, dresses, outerwear, bags — rather than a single flagship garment. The medallion is the first artifact of the brand: EWAH exists the day it's in hand.

## Sequencing

HW-01 is now **the first physical product** (before hats). It's also the cheapest confidence win available (~$300–700 all-in to hold three finished finishes). It does **not** touch the Capsule 01 apparel budget: run it as a parallel micro-track. Blocking item (unchanged, now urgent): **the emblem vector from the identity designer** — the hardware supplier needs it as clean vector/DXF; nothing tools until it exists. The hidden-engraving and packaging specs go in the first RFQ so they're quoted together.
