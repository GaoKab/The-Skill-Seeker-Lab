# PULA artwork v1 — review

**Received 27 Sept 2026.** Archived at `pula-artwork/v1-received-27sep/`. Ten SVGs, a production README, a handoff PDF.

**Verdict: do not send to a printer yet. Two blocking faults, both fixable, neither requiring a redraw.**

## What is genuinely right, and it is most of the thinking

- **Separations exist as individual files**, and they decompose the composite correctly. The hero back holds 15 threads across four colours; blue 5, white 4, navy 3, black 2, and each separation file contains exactly those threads at exactly those x positions. That is competent work, not a guess.
- **Artboards are 12 × 16 in at 100 units per inch**, matching the standard tee print area.
- **Approved vocabulary respected.** 1966, INDEPENDENCE LIVES ON, FATSHE LENO. Nothing off the locked list, and no revival of PEOPLE / LAND / OPPORTUNITY.
- **The Coordinates tee change is captured**: front is PULA plus A ene!! only, back is coordinates plus flag, no BOTSWANA, no PULA, no map.
- **The README is good.** It flags puff intent, names reflective candidates, states that physical ink matching is required rather than pretending hex values are enough, asks for a separation proof before sampling, and repeats the instruction to verify the coordinates before bulk.

## BLOCKER 1 — every letter is live text, not outlines

Audit result: **15 `<text>` elements, zero `<path>` elements across the whole kit.**

Every word is set as live text calling `font-family="Arial, Helvetica, sans-serif"`. Nothing has been converted to outlines.

**Why this stops production.** A print file with live text renders using whatever font the opening machine has. A printer on Linux with no Arial gets a substitute and the lockup silently changes shape. Even with Arial present, different renderers space text differently. This is the most common single cause of wrong print output, and it is exactly what tech pack v1 meant by "rebuilt as clean vector separations." **Live text is not a vector separation.**

**Second problem underneath it: Arial is Monotype's.** It ships with operating systems for system use. Building a commercial brand lockup on it, printing it and selling the garment is a licensing question, not a free ride. This gets solved for nothing by rebuilding in an SIL Open Font Licence face, which permits commercial use and embedding outright.

**Fix: every glyph converted to a filled path.** Not optional, not a nicety.

## BLOCKER 2 — the rain is a comb, not rain

The hero back threads sit at x = 830, 850, 870, 890, 910, 930, 950, 970, 990, 1010, 1030, 1050, 1070, 1090.

**A perfectly regular 20-unit grid.** Every gap identical. All threads start within 30 units of the top, all run unbroken to their end, all are exactly vertical.

Tech pack v1's binding language: *"very thin thread-like mostly-vertical lines, **asymmetric clusters, varied length and spacing**"* and *"never broad diagonal stripes, never thickened into bars."* It also called for some threads broken mid-fall.

Evenly spaced parallel lines are not asymmetric clusters. At arm's length this reads as a comb, a barcode or a fence. It is the one visual element the whole collection is named for, and it is the element most likely to make the garment look cheap.

**This one is already solved.** `pula-artwork/rain-line-system-v1.svg` holds **75 threads in three asymmetric clusters**, with varied length, varied spacing, varied stroke weight, roughly a fifth broken mid-fall, and seven isolated on a reflective layer. It was built to the pack's rules. It should replace the 15-line comb rather than anything new being drawn.

## Smaller faults worth fixing in the same pass

| Issue | Detail |
|---|---|
| **No puff separation** | The README says PULA is intended as 3D puff, but file 01 carries PULA, the divider rule and A ene!! together. Puff needs its own file so the printer can burn a separate screen |
| **Separation files are black** | `RAIN_BLUE.svg` and `RAIN_WHITE_REFLECTIVE.svg` both stroke `#000000`. Black-on-white is a legitimate separation convention, but the filenames imply colour and the README never states the convention. Say which it is, or the printer will ask, or worse, assume |
| **A ene!! is Arial regular** | Specified as handwritten or script. What is there is a placeholder wearing the wrong clothes, and it is the warmest element in the collection |
| **Strokes, not filled shapes** | Rain is `<line stroke-width="…">`. Most RIPs cope, but printers generally want strokes expanded to filled outlines for the same reason type needs outlining |
| **Reflective share** | 4 of 15 threads, about 27%. The pack says reflective is selective. Defensible, but check it against the 7-of-75 ratio in the existing rain system |

## What I can fix without a designer

**Rebuild all type as outlined paths in Liberation Sans**, which is metric-compatible with Arial and carries an open licence permitting commercial use. That fixes Blocker 1 and the Arial licensing problem in one pass. **Swap the comb for the 75-thread rain system.** That fixes Blocker 2. **Split the puff element into its own file**, expand strokes to filled paths, and correct the separation colour convention.

**What still needs a person:** the "A ene!!" script, and a designer's eye on whether Liberation Sans is the right letterform for a hero puff lockup. It is even-stroked and clean, which puff likes, but it is a workhorse face and not a display one.

That reduces the outstanding commission from the full brief in `27` to one script phrase and one typographic opinion.
