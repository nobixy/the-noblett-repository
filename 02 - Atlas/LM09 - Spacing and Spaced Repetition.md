---
title: "LM09: Spacing and Spaced Repetition"
type: learning-method
method_id: LM09
evidence: "Strong"
---

# LM09 — Spacing and Spaced Repetition
*Deep dive + project ([[DR-009 - Learning Method Deep Dives|DR-009]]). Hub: [[LM00 - Learning Methods Hub|Learning Methods]] · Method in practice: [[how-i-study]] §1*

> [!NOTE] Evidence: **Strong**

## In plain words
Spread practice of the same material over days and weeks instead of cramming it into one sitting. Spaced repetition software (Anki) schedules each card just before you would forget it.

## The evidence, honestly
Cepeda et al. (2006): a meta-analysis of 839 tests of the spacing effect found spaced study beats massed study, and the best gap grows as you need to remember for longer.
Cepeda et al. (2008): the best gap is very roughly 10–20% of how long you need to remember it.
Dunlosky et al. (2013): distributed practice is rated **high utility**.
Scheduling algorithms: SM-2 (Wozniak, SuperMemo, 1987) is the classic. Anki has offered FSRS, a newer model fitted to review data, since version 23.10.

## Using it in EECS
- Make cards for definitions, complexity facts, formulas, shell commands, and "what does this code print?".
- Don't make cards for things you can only learn by doing (writing a proof, designing a circuit). Practise those, spaced.

## Common mistakes
- Cards with too much on them. Keep one fact per card.
- Cards made from things you never understood.
- Skipping reviews and then deleting the backlog.

## 🔨 Project: Your own spaced-repetition app (Leitner → SM-2 → FSRS)
Grow a Leitner-box app into SM-2: an ease factor, review intervals, and cards stored in a JSON file kept in git. (If you have built [Study Deck](<../02-programming-fundamentals/projects/study-deck/spec.md>) in Module 02, it already does this; skip to the stretch.) Stretch: compare its schedule with the open-source `fsrs` Python package.
- **Done when:** it schedules your 20+ cards with SM-2, a unit test checks the intervals for a known review sequence, and you used it in 14 sessions.
- **Level:** Beginner-to-intermediate Python.
- **Fits with:** Protocol **I** (interleave and space); [Study Deck](<../02-programming-fundamentals/projects/study-deck/spec.md>) (Module 02) is the curriculum's own spaced-repetition app. The review intervals are part of the technique itself, not a curriculum schedule.

## Sources
- Cepeda, Pashler, Vul, Wixted & Rohrer (2006), "Distributed practice in verbal recall tasks", *Psychological Bulletin* 132(3), 354–380.
- Cepeda, Vul, Rohrer, Wixted & Pashler (2008), "Spacing effects in learning: a temporal ridgeline of optimal retention", *Psychological Science* 19(11).
- SM-2 description: supermemo.com; FSRS: github.com/open-spaced-repetition.
