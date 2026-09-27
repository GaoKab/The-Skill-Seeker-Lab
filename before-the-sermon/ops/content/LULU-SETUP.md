# Lulu — account, private copies first, publish when ready
*Decided 27 Sep: Gao creates the account (her identity, her terms). Private print copies first; publishing is a switch on the same project, flipped whenever she chooses. Lulu takes 20% of profit on distributed sales; private copies are at print cost.*

## Files (in `dist/`, built to Lulu's geometry)
| Book | Interior (same file for every printer) | Lulu paperback cover |
|---|---|---|
| Before the Sermon | `before-the-sermon_interior_6x9_128pp.pdf` | `before-the-sermon_cover_6x9_128pp_lulu.pdf` — 12.598 × 9.25 in, spine 0.348 |
| Skill Seeker Journal | `skill-seeker-journal_interior_6x9_128pp.pdf` | `skill-seeker-journal_cover_6x9_128pp_lulu.pdf` — 12.598 × 9.25 in, spine 0.348 |

**Re-upload these covers (rebuilt 27 Sep):** Lulu's preview showed three things inside its 0.5 in safety zone — the imprint lines, KDP's barcode box, and the outer frame. The `_lulu` covers now keep all text 0.5 in from trim, carry **no barcode box** (Lulu places its own, with its own white background, only on distributed copies), and set the frame 0.5 in in. Spine from Lulu's own formula (pages ÷ 444 + 0.06); Lulu shows 0.35. **Lulu shows its number on the cover template step** — if it differs from 0.348 by more than 0.01, send it and the cover is rebuilt in a minute. Page numbers now sit 0.51 in from the foot, inside Lulu's 0.5 in safety rule.

## The wizard — Before the Sermon (repeat for Skill Seeker)
1. **lulu.com → Sign up** (free). Then **Create → Print Book**.
2. **Start Your Project:** Book title `Before the Sermon` · Subtitle `Sitting With Scripture` · Contributor: role *Author*, name `Before the Sermon` (Skill Seeker: `The Skill Seeker Lab`) · Language English · Category *Religion › Christianity › Devotional* (nearest) · Keywords from `KDP-LISTING.md`.
3. **Copyright & ISBN:** *Get a free Lulu ISBN.* Costs nothing, never expires, and is what lets you publish later without starting over. If ISBN is only offered under a "publish" path, take that path and set **access Private** — nothing is public until you switch it.
4. **Design your project → Book specs:** Interior colour *Black & White Standard* · Paper **Cream** (Skill Seeker: **White**) · Book size **US Trade 6 × 9** · Binding *Paperback · Perfect Bound* · Cover finish *Matte*.
5. **Upload interior PDF.** Lulu checks page size (6 × 9 ✓), fonts (embedded ✓), page count (128 ✓). A *safety margin* warning, if any, is advisory — the lowest text is 0.51 in from trim.
6. **Cover:** choose *Upload your own cover* → read the template's **spine width** → upload `…_lulu.pdf`. Lulu previews the wrap; check the spine text is centred.
7. **Review → Confirm and Publish.** On Lulu, "publish" means *finish the project so it can be printed*. A project started under **Print your book** (the review screen shows only a **Print Cost** line, no retail price or revenue line) has no storefront listing and no distribution, so this button makes nothing public. Only a project with **Global Distribution** switched on becomes public, and that switch is on a separate step you have not taken.
8. **Order copies:** after confirming, the project appears under *My Projects* → **Order** → quantity 2 → pay print cost + shipping. **Actual print cost on screen, 27 Sep: $5.19 per copy** (128 pp, Standard B&W, 60# cream, perfect bound, matte). They arrive in 1–2 weeks; these are the photos, the trailer, and the first real look at the object.
9. **Check the spine on the printed copy**, not the preview: Lulu's preview is a flat render. If the title sits visibly off centre on the real spine, tell me the direction and we adjust `COVER_SPINE_IN` by a few hundredths and re-upload before the next order.

## Publishing later — same project, five minutes
Project → **Access → Public** → **Global Distribution ON** → set retail price ($14.99) → Lulu shows your revenue after print cost and its 20% → accept the distribution requirements (ISBN present, standard size, no crop marks — all true). Live on Lulu's store immediately; Amazon via Ingram ≈ 12 weeks. If Global Distribution greys out **Cream**, choose White for the distributed edition.

## Hardcover (Before the Sermon, later)
Lulu casewrap or linen-wrap 6 × 9 needs its own cover geometry — create the project, screenshot the cover template dimensions, send them; the build takes any numbers.
