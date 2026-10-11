---
title: "Project: Ratio Workshop"
id: "FND-MA-PRJ-ratio-workshop"
type: "project"
module: "00-foundations"
track: "math"
phase: "B"
order: 390
prerequisites: [M04, MOD01-LAB01]
stages: "M05–M06"
artifact: "A scaled recipe; measured screen data; ratio_tools.py with three commands and tests; a measured download-time prediction"
deliverable: "Short lab report: how good is my download-time estimate?"
---

# Project: Ratio Workshop

| | |
| :-- | :-- |
| **You build** | Three small, genuinely useful tools — a recipe scaler that uses exact fractions, an image "fit-to-box" calculator, and a download-time estimator that gets bits, bytes, and units right — then you test the estimator against a real download |
| **Deliverable** | A short lab report |

---

## Why this matters

Fractions, ratios, percents, and units are where real-world math lives, and where real-world mistakes happen: a recipe tripled wrongly, an image stretched out of shape, a download estimate off by 8× because someone mixed bits and bytes. Each tool here is small, but each one handles a classic trap correctly, and each is tested.

The download estimator is a preview of [Module 09](../../../../09-networking/overview.md), where you'll measure and model your own network. The fit-to-box calculator is a preview of [Module 10](../../../../10-browser-engine/overview.md), where your browser engine must fit images into layout boxes without distorting them.

**Real-world analogs:** recipe apps, image editors' "constrain proportions" checkbox, browser image scaling (`object-fit: contain`), download progress bars.

---

## Milestones

### Milestone 1 — The recipe (M05, paper)

**Do:**
1. Pick a real recipe with at least 6 ingredients, including some fractions (½ cup, ¾ tsp, 1⅓ cups…).
2. Scale it **by hand** three ways: × 1½, × ⅔, and "to serve 7" (if the original serves 4, the factor is 7/4).
3. For every scaled amount, write the fraction in simplest form and as a mixed number.
4. **Look back [Pólya]:** which scaled amounts are awkward to measure (like 7/12 cup)? Round them to something measurable and explain your rounding in one sentence each.
5. Optional and recommended: cook the × 1½ version. Real feedback.

**Done when:** three scaled versions, all fractions simplified, rounding explained.

### Milestone 2 — Screens and aspect ratios (M06, paper and measuring)

**Do:**
1. For every screen you own (laptop, phone, monitor, TV): find its resolution in pixels (system settings, or search the model) and measure its visible width and height with a tape measure.
2. Compute each **aspect ratio** from the pixel counts, simplified with the GCD (M04): e.g. 1920 × 1080 → ÷120 → **16 : 9**. Compare with the ratio of your physical measurements. Are pixels square?
3. **Fit-to-box by hand:** a 4000 × 3000 photo must fit inside a 1280 × 720 window without stretching. Find the biggest size that fits. (Hint: try scaling to fit the width, then to fit the height; one of them won't fit.)

**Done when:** a table of your screens with simplified ratios, and the fit-to-box answer with working.

<details>
<summary>Check (step 3)</summary>

Scale to width: 1280/4000 = 0.32 → 1280 × 960, too tall. Scale to height: 720/3000 = 0.24 → 960 × 720 ✓. Answer: **960 × 720**, centred with 160 px of empty space on each side.
</details>

### Milestone 3 — `ratio_tools.py` (M06, Python)

One program with three commands. Use `fractions.Fraction` for exact arithmetic wherever possible.

**`scale-recipe`:** reads a recipe file and a factor, and prints the scaled recipe.

```
# recipe.txt  (format: amount<TAB>unit<TAB>ingredient; amounts may be "3/4", "1 1/3", "2")
1 1/3	cup	flour
3/4	tsp	salt
2	whole	eggs
```

`python3 ratio_tools.py scale-recipe recipe.txt 3/2` prints amounts as simplified mixed numbers (`2 cup flour`, `1 1/8 tsp salt`, `3 whole eggs`).

**`fit`:** `python3 ratio_tools.py fit 4000x3000 1280x720` prints `960x720` and the simplified aspect ratio `4:3`. Rules:
- Never stretch: the output's aspect ratio must match the input's as closely as whole pixels allow.
- Never exceed the box.
- Round **down** to whole pixels (explain why down, not to nearest, in a comment [W]).

**`eta`:** download-time estimator.
`python3 ratio_tools.py eta --size 2GB --speed 50Mbps --done 35%` prints the remaining time in a human format (`3 min 28 s`).
- Size units: `B, KB, MB, GB` (powers of 1,000) and `KiB, MiB, GiB` (powers of 1,024).
- Speed units: `bps, kbps, Mbps, Gbps` (**bits** per second, powers of 1,000) and `B/s, KB/s, MB/s` (**bytes** per second).
- Convert everything to bytes and seconds using conversion factors (M06 Part 6). Write the factors as named constants.

**Tests** (`test_ratio_tools.py`), each with an answer you worked out by hand first:
- Scaling `1 1/3` by `3/2` gives exactly `2`.
- `fit 1920x1080 1280x1280` → `1280x720`; `fit 1080x1920 1280x720` (portrait) → `405x720`.
- `eta --size 2GB --speed 50Mbps --done 0%` → 320 seconds.
- `eta --size 1GiB --speed 1MB/s` → 1,073.74… seconds (1,073,741,824 ÷ 1,000,000).
- Bits vs bytes: 100 Mbps for 12.5 MB takes 1 second.

**Done when:** all tests pass, and you've used each command on a real case of your own.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why does the program convert everything to bytes and seconds first, instead of handling each pair of units separately?* (Think: how many conversion rules would you need otherwise?)

### Milestone 4 — Test the estimator against reality

**Do:**
1. Find a large public file to download (a Linux ISO from a mirror is ideal; 1–4 GB).
2. Measure your connection speed (any speed-test site, or your router's stats). Record it with units.
3. Predict the download time with `eta`. **Write the prediction down before downloading.**
4. Download with `curl -o /dev/null -w "%{time_total}s %{speed_download}B/s\n" <url>` (this discards the file and prints total time and average speed in bytes per second).
5. Compute the **percent error**: |actual − predicted| ÷ actual × 100 (M06).
6. Repeat at a different time of day.

**Done when:** two predictions and two measurements, with percent errors.

---

## Common pitfalls

- **Mixed numbers in parsing:** `"1 1/3"` is one amount, not two. Split on the space, then add.
- **Floats for recipes:** `0.1 + 0.2` problems (M06 Part 7). Use `Fraction`.
- **Bits vs bytes:** the single most common unit error in networking. Lowercase b = bits; uppercase B = bytes. Test it.
- **KB vs KiB:** decide and document. Your speed test site and your file manager may not agree.
- **Expecting the estimate to be perfect:** real downloads have start-up delays and varying speed. A good lab report explains the gap, not hides it.

## Communication deliverable

**Lab report** (one page, [Lab Report Template](<../../../../04 - System/Lab Report Template.md>), E07–E08 level): *"How accurate is a simple size ÷ speed estimate of download time?"* Include your predictions, measurements, percent errors, and two or three likely reasons for the difference. (Your reasons are hypotheses; Module 09 will let you test them.)

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before coding `eta`, write all the unit conversion factors from memory |
| **W** | Round-down rule; convert-to-base-units design; percent error's denominator |
| **S** | Each command's steps as comments before code |
| **I** | Milestones mix fractions, ratios, percents, and units |
| **T** | The lab report |

## Stretch goals

- **Pixel density:** compute each screen's pixels per inch: diagonal in pixels (Pythagoras, M10) ÷ diagonal in inches.
- **Live progress bar:** wrap `curl` so `eta` updates every second from the real progress.
- **Unit checker:** make `eta` refuse nonsense like `--speed 5GB` (a size, not a speed), with a clear error message.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Paper work | Recipe and screens correct, rounding explained | Minor errors | Incomplete |
| Tools | All three commands work; exact fractions; units right | Two commands | One or none |
| Tests | Hand-worked answers for every test | Some tests | None |
| Reality check | Prediction before measurement; percent error | Measured only | Missing |
| Lab report | Clear, honest about error | Complete | Missing |

**Done when:** every area at least 2.

## Connections

- **Back:** M04 (GCD for ratios), M05 (fractions), M06 (percents, units, floats).
- **Forward:** Module 09 (latency and bandwidth: why your estimate missed), Module 10 (image fitting in layout), [Fare Detective](../fare-detective/spec.md) (models with a fixed part and a rate).
