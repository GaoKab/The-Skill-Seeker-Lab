# Tech Pack Review — ChatGPT Drafts v0.1 (August 2026)

Four tech pack drafts received and stored in `tech-packs/`. Review against the frozen capsule (`07` §1), the funded round (`07` §5), and the P1 brief (`08`).

## Overall verdict

**Good drafts — genuinely usable structure.** They contain the right sections (style overview, callouts with non-negotiables, BOM, construction with stitch specs and tolerances, POMs, grade rules, branding, QC tests, revision log, approval gates), they carry EWAH's fit language correctly (waist-to-hip protection in grading, no-front-seam liners, rear-coverage rules, modesty-in-motion tests), and they include the ownership clause. With the corrections below, WF-01 can go to a factory.

**Best sign of quality:** the base-size body (38 / 31 / 43–44 in) gives a waist:hip ratio of ~0.72 — exactly the EWAH Curve Block spec. The grade rules grow hip faster than waist (+1.75→2.25 in vs +1.25→2.0 in) and hold length on larger sizes. Whoever/whatever drafted these was reading the same fit philosophy.

## Pack-by-pack

| Pack | Style | Status vs. plan | Assessment |
|---|---|---|---|
| **EWAH-WF-01** Warrior Flow Dress-Skort | Funded **Look 1 (P1)** ✅ | In the frozen capsule and the funded round | Aligns well with brief `08`: wrap-inspired bodice, mixed smooth/controlled-flow panels, dual movement openings, 5" no-front-seam liner with pocket, machine-safety test included. **This becomes the working factory tech pack for P1**, merged with `08` (which remains the design authority) |
| **EWAH-WF-02** Warrior Flow Short Summer Dress | ⚠️ **Not in the frozen capsule** | New style: above-knee dress, mesh insert neckline, curved side openings | Well-drafted; closest existing relative is the Summer Line's Shield/Warrior direction. File as **Phase 2 candidate** |
| **EWAH-ST-02** Air Sculpt Short Dress | ⚠️ **Not in the frozen capsule** | New style: perforated-panel modest summer dress | Strong modesty engineering (perforation over opaque layers, bra-coverage grading note). **Phase 2 candidate** — perforation/mesh is a new fabric platform (adds sourcing complexity) |
| **EWAH-SM-03** Mesh Flow Short Set | ⚠️ **Not in the frozen capsule** | New style: mesh top + lined skirt/skort set | Coherent, but furthest from the funded round (travel/resort lean). **Phase 2 candidate** |

## The conflict to resolve

The funded round is **Dress-Skort + Sculpt Flow Set (top + pant) + Throw-On Layer Dress**. These drafts cover the Dress-Skort — but **not the Sculpt Flow Set or the Layer Dress** — and instead add three new mesh/perforated summer styles. Two readings:

1. **The freeze holds (recommended):** WF-01 goes to the factory; WF-02/ST-02/SM-03 are filed as Phase 2 — they share the liner block and grading logic, so they'll be cheap to develop once P1 proves the block. Tech packs for the funded Set + Layer Dress get drafted next (from specs `15`), reusing the good structure of these drafts.
2. **The round is being re-scoped** toward a mesh summer capsule. That's a founder decision — but note it would replace already-chosen looks, add an unproven fabric platform (perforated/mesh), and restart the choice made in `07` §5.

**Recommendation: hold the freeze.** New drafts are inventory for later, not a new direction now.

## Corrections needed before WF-01 goes to a factory

1. **Units:** packs are in inches; all other EWAH docs are metric. Pick one (cm recommended) and state it on page 1 — mixed units cause real sampling errors
2. **BOM ↔ fabric platforms:** BOM lines say "TBD" supplier; map each to platform codes A/B/D (`03`) so factory quotes match our fabric standards (e.g., WF-01 main body = platform A at 230–260 gsm — note this is heavier than `08`'s 200–220 gsm; resolve to one number: recommend 220–240)
3. **Neckline decision:** `08` specifies crew/high-crew; WF-01 pack specifies wrap-inspired V/crossover (matching the reference image). Pick one for Proto 1 — recommend the **wrap-inspired crossover with the pack's internal stabilization**, since the wrap is the signature; the crew fallback lives in the revision log
4. **Length decision:** pack offers two CB lengths (36.5" above-knee / 39.5" knee). Proto 1 = above-knee (36.5") per `08`'s mid-thigh intent; knee variant deferred
5. **Missing pages a factory will ask for:** technical flats (front/back/side line drawings — the packs reference boards, which are photos, not flats), colorway page (Onyx + Antique Gold callouts per `13`), and label artwork. Flats remain the single biggest gap — a factory can quote without them but cannot pattern reliably
6. **Phone pocket:** `08` says right-side; keep "optional" out — it's a signature, make it required
7. Add the watermark ("EWAH — CONFIDENTIAL") to every page before sending

## Updated document hierarchy

- `08` = design authority for P1 (intent, seam maps, test criteria)
- `tech-packs/EWAH-WF01...docx` = the factory-facing document, corrected per above
- Discrepancy rule: where they conflict, `08` wins until the founder approves a change in writing
