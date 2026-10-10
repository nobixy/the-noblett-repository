---
title: "Project: Study Deck"
module: "02-programming-fundamentals"
hours: 45
artifact: "deck: a command-line spaced-repetition app with plain-text cards, an append-only review log, two schedulers, importers, stats, and a forgetting-curve simulator"
deliverable: "Design note (before + after), README, 5-minute demo, short simulation report"
---

# Project: Study Deck

| | |
| :-- | :-- |
| **Module** | 02 Programming Fundamentals |
| **Time** | About 45 hours |
| **Prerequisites** | Labs 01–03 of this module; [Spelling Engine](../../../00-foundations/english/projects/spelling-engine/spec.md) Milestone 3 (helpful, not required) |
| **You build** | `deck`, your own spaced-repetition flashcard app. Cards live in plain Markdown files you edit in any editor. Every review is appended to a log. Two scheduling algorithms you can switch between. Importers for your spelling log and your blank-sheet misses. A stats screen. And a simulator that compares schedulers on a model of human forgetting |
| **Deliverable** | A design note (written before, updated after), README, recorded demo, and a short simulation report |

---

## Why this matters

You've been using spacing and retrieval since week 1 [I] [R]. Now you build the machine that runs them — and **you'll use it every day for the rest of this curriculum.** Every flashcard from every module goes into Study Deck. A tool you use daily gets tested harder than any homework.

The project also teaches core programming craft: a data model with invariants, a text format people edit by hand (which means parsing messy input carefully and never destroying it), an append-only log, algorithms you can swap, testing with a fake clock, and an experiment that answers a real question with a simulation.

**Real-world analogs:** Anki, SuperMemo, Duolingo's review scheduling; append-only event logs (used in databases — Module 11 — and in finance); A/B simulation of algorithms before deploying them.

---

## What you're building

### Cards: plain Markdown files

A deck is a folder of `.md` files. Each file holds many cards. A card:

```markdown
Q: Why does Euclid's algorithm give the GCD?
A: (a, b) and (b, a mod b) have exactly the same common divisors,
   and the numbers shrink each step until the remainder is 0.
@tags math m04 why
@id m04-euclid-why
```

- `Q:` starts a card. `A:` starts the answer, which continues over following lines until a blank line, the next `Q:`, or an `@` line.
- `@tags` (optional) — space-separated tags.
- `@id` (optional) — a stable identifier. **If missing, `deck` generates one and writes it back into the file** — changing nothing else in the file (not your spacing, not your comments, not the order).
- Lines starting with `#` are headings or comments and are kept as they are.

**Cloze cards** (fill-in-the-blank): `C: Each place is worth {{base}} times the place to its right.` The review shows the sentence with `[...]` and asks for the hidden part.

**Spelling cards:** `S: separate` with `@hook there is a rat in sep-a-rat-e`. The review speaks the word (`espeak-ng`, as in the Spelling Engine) and asks you to type it.

### The review log: append-only

Every review is one new line at the end of `reviews.tsv`:

```
2026-11-02T07:41:12	m04-euclid-why	good	leitner
```

(timestamp, card id, grade, scheduler used). The log is **never edited**, only appended to. **A card's current state (its box, its due date) is not stored anywhere — it is computed by replaying the log.**

> **[W] Why replay a log instead of storing each card's state?** Think about these: (1) You change scheduler next month — can you recompute everyone's due dates under the new rules? (2) A crash happens mid-write — what's the worst damage to an append-only file vs a rewritten file? (3) You want stats like "how many reviews last Tuesday" — where does that come from? Write your answer, and the cost of this design (replaying gets slower as the log grows — when would that matter, and what would you do?), in your design note. Module 11 will show you databases built on exactly this idea (write-ahead logs).

### Grades

`again` (forgot), `hard`, `good`, `easy`. Leitner uses only "right or wrong" (again = wrong; others = right). SM-2 uses all four.

### Schedulers

Both implement the same interface, so the rest of the program doesn't care which is active:

```python
class Scheduler(Protocol):
    def initial_state(self, created: date) -> CardState: ...
    def after_review(self, state: CardState, grade: Grade, today: date) -> CardState: ...
```

`CardState` holds at least `due: date` plus whatever the scheduler needs (a box number; an interval and an ease factor).

1. **Leitner** (what you've done by hand): boxes 1–5, intervals 1, 3, 7, 21, 60 days. Right → up one box; wrong → box 1.
2. **SM-2** (published by Piotr Woźniak in 1987 for SuperMemo, the ancestor of most modern schedulers). Each card has an **ease factor** EF (starts at 2.5, minimum 1.3) and an **interval** I in days:
   - Map grades to quality q: again = 1, hard = 3, good = 4, easy = 5.
   - If q < 3: the repetition count resets to 0 and I = 1 (relearn tomorrow).
   - Otherwise: first success I = 1, second I = 6, after that I = round(I × EF), and the repetition count goes up by 1.
   - **In both cases**, then update the ease: EF ← EF + (0.1 − (5 − q) × (0.08 + (5 − q) × 0.02)), but never below 1.3. (So `easy` raises EF by 0.1, `good` leaves it unchanged, `hard` lowers it by 0.14, and `again` lowers it by 0.54.)
   - Due date = today + I.

Read the formula slowly. Plug in q = 5, 4, 3 by hand and see what each does to EF [W]. (You may adjust SM-2 — many apps do — but document every change and why.)

### The command line

```
deck review [--deck PATH] [--tag TAG] [--limit N] [--scheduler leitner|sm2]
deck add [--file FILE]            # interactive: type Q, A, tags
deck stats                         # see below
deck import-spelling PATH.tsv      # Spelling Engine log → S: cards
deck import-misses PATH.md         # blank-sheet "missed" items → Q/A cards
deck check                         # lint every card file; report problems with file:line
deck simulate ...                  # Milestone 6
```

---

## Milestones

### Milestone 1 — Design note and the card parser

1. **Design note v1** (1–2 pages, E06–E08 level) *before coding*: the data model (classes and their invariants), the two files (card Markdown, review log), the module layout, and your answer to the replay-the-log why-ladder.
2. **Parser:** `parse_deck(path) -> list[Card]` with **line numbers kept** for every card. Malformed input never crashes: it produces a `Problem(file, line, message)` (e.g. "Q: with no A:", "duplicate @id m04-euclid-why (also at line 40)").
3. **ID write-back:** cards without `@id` get one (a short slug from the question plus a counter, or a random 6-character code — choose and justify [W]), written back by inserting **one line** after the card, leaving every other byte of the file identical.
4. `deck check` prints all problems.

**Tests:** a messy fixture file (extra blank lines, Windows line endings, a missing A:, a duplicate id, a multi-line answer, a cloze card). **Round-trip test:** for a file where every card already has an id, parsing and rewriting must produce **byte-identical** output.

**Done when:** `deck check` works on a messy deck and the byte-identical round-trip test passes.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why must ID write-back preserve every other byte?* (Who else edits these files, and what do they expect?)

### Milestone 2 — Review with Leitner, on a fake clock

1. `CardState` and the Leitner scheduler, **pure functions** with no file access and no clock lookups.
2. `replay(log_entries, cards, scheduler) -> dict[id, CardState]`.
3. `deck review`: compute states, pick due cards (due ≤ today), **shuffle** them [I], show each question, wait for Enter, show the answer, read a grade, append to the log immediately (so a crash loses at most one review).
4. Cards whose `@id` no longer exists in any file are ignored in the log (deleted cards); new cards (no log entries) are due today.

**Tests (all with an injected `today`):**
- a new card (box 1, due day 0) reviewed right on days 0, 3, 10, and 31 moves to boxes 2, 3, 4, and 5, and is next due on day 91;
- a wrong answer at box 4 sends it to box 1, due tomorrow;
- replaying the same log twice gives the same states (determinism);
- appending to the log, then replaying, gives the same result as updating in memory.

**Done when:** you review your real cards with it for 3 days.

### Milestone 3 — SM-2, and switching schedulers

1. Implement SM-2 behind the same interface.
2. `--scheduler sm2` (remember the choice in a small config file).
3. Because state is replayed from the log, switching schedulers **recomputes every card's due date** from history. Verify this works.

**Tests:** hand-computed SM-2 sequences for three grade patterns (all `good`; `good, good, again, good`; all `easy`) — work them out on paper first [S], with EF and I after every step.

**Done when:** both schedulers pass their tests, and switching on your real deck works.

**Checkpoint:** Milestone Checkpoint. Feynman target: *how SM-2 decides the next interval*, explained without the formula first, then with it.

### Milestone 4 — Stats and forecast

`deck stats` prints:
- cards total, new, due today, overdue;
- reviews per day for the last 30 days as a text bar chart;
- **retention**: the percentage of reviews (excluding new cards) graded better than `again`, over the last 30 days;
- a **forecast**: how many cards will be due on each of the next 14 days if you keep up;
- your current daily streak.

**Done when:** stats are correct on a fixture log (hand-checked), and you've looked at your own.

### Milestone 5 — Importers and the spelling card type

1. `deck import-spelling` turns your Spelling Engine `spelling-log.tsv` into `S:` cards (word, hook, tags from error tags), without duplicating cards already imported (match on the word).
2. `S:` reviews speak the word and check the typed answer; a wrong answer shows the letter-level difference (Spelling Engine Milestone 3) and grades automatically.
3. `deck import-misses` reads a blank-sheet retrieval note: every line under a heading containing "Missed" in the form `- question :: answer` becomes a Q/A card. (Update your [Blank-Sheet Retrieval Template](<../../../04 - System/Blank-Sheet Retrieval Template.md>) to use this form — your workflow and your tool now fit together.)

**Done when:** both importers run on your real files without creating duplicates when run twice.

### Milestone 6 — The forgetting-curve simulator

Which scheduler works better for you — and what does "better" mean? Real data takes months. A **simulation** gives a first answer in seconds.

**The model** (a simplified version of a well-known memory model): each simulated card has a **stability** S (in days). The probability you recall it after t days is

$$P(\text{recall}) = e^{-t/S}$$

After a successful review, S grows (multiply by a factor, e.g. 2.5); after a failure, S drops back (e.g. to 1). Start new cards at S = 1.

`deck simulate --scheduler leitner --cards 300 --new-per-day 10 --days 180 --seed 1` runs the model: each simulated day, review the due cards; for each, flip a weighted coin with P(recall) to decide right or wrong; grade accordingly; record the workload (reviews that day).

**Experiment:** for both schedulers, report:
- average reviews per day (workload);
- average recall probability across all cards at day 180 (retention);
- the worst day's workload.

Then vary one model parameter (the stability growth factor) and see whether the winner changes.

**Done when:** a table of results for both schedulers and three parameter values, with a short written conclusion.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *what can this simulation tell you, and what can't it?* (Is your memory really e^(−t/S)? What would you need to measure to find out? Your own review log is that data.)

---

## Testing guidance

- **Inject the clock everywhere** (Lab 02). No function except the CLI entry point calls `date.today()`.
- **Pure core, thin shell:** schedulers and replay are pure functions (inputs → outputs, no files, no printing). The CLI is a thin layer that reads files, calls the core, and prints. Test the core heavily; test the shell with a few end-to-end runs in `tmp_path`.
- **Byte-identical round trips** for the card files.
- **Seeds** for shuffle and simulation, so tests are repeatable.

## Common pitfalls

- **Destroying hand-written files.** Never rewrite a whole card file from parsed data; insert only what you must. Test it.
- **Timezones and dates:** store timestamps in the log; compute "today" in local time; compare dates, not timestamps, for due-ness. Decide and document what "a day" is (does a review at 00:30 count for yesterday?).
- **Floating EF drift:** keep EF rounded to 2 decimals after each update (a documented choice), or tests become fragile.
- **Duplicates on import:** importing twice must not double your cards.
- **Feature creep:** no GUI, no sync, no accounts. A tool you use beats a tool you're still building.

## Communication deliverable

1. **Design note** v1 (before Milestone 1) and **v2** (after Milestone 6) with a short "what changed and why" section.
2. **README** that passes the five-minute stranger test: install, card format, every command, how to run tests.
3. **Demo (5 minutes):** a real review session, a scheduler switch, stats, and the simulation results.
4. **Simulation report** (1 page, [Lab Report Template](<../../../04 - System/Lab Report Template.md>)): question, model, results table, conclusion, limits.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | The tool itself; plus: before Milestone 3, write the SM-2 rules from memory |
| **F** | SM-2 in plain words; the replay design in plain words |
| **W** | Replay vs stored state; ID scheme; preserving bytes; what the simulation can't tell you |
| **S** | Hand-computed SM-2 sequences as labelled steps; subgoal comments in replay |
| **I** | Shuffled reviews; tags let you build mixed sessions across subjects |
| **T** | Design notes, README, demo, report |

## Stretch goals

- **A third scheduler:** read about FSRS (an open-source modern scheduler that fits a memory model to your own review history) and implement a simplified version. Run it in your simulator.
- **Fit your own forgetting curve:** from your real review log, estimate how recall probability falls with days since last review. Plot it. (Module 12's statistics will make this rigorous.)
- **Speed:** with 100,000 log lines, how long does replay take? Add a cache file of computed states that's rebuilt when the log grows (and argue why it's safe).
- **Image cards** shown in the terminal with an external viewer.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Parsing and files | Problems with file:line; byte-identical round trip; safe ID write-back | Parses; some file damage risk | Crashes on messy input |
| Core design | Pure schedulers; replay; injected clock; invariants documented | Mostly | Tangled with I/O |
| Schedulers | Both, hand-computed tests, switching recomputes | One | Buggy |
| Stats and importers | Correct on fixtures; idempotent imports | Partial | Missing |
| Simulation | Results table, parameter sweep, honest limits | Runs | Missing |
| Daily use | Used 14+ days | 7+ days | Barely |
| Communication | Notes v1/v2, README, demo, report | Most | Few |

**Done when:** every area at least 2; Core design and Daily use at 3.

## Connections

- **Back:** Spelling Engine (data, quiz, letter diff), Lab 02 (fake clocks, golden files), Lab 03 (invariants), M06/M11 (percentages; e^(−t/S) is an exponential decay).
- **Forward:** every later module's flashcards; Module 05 (faster storage and search for big decks); Module 11 (append-only logs and recovery); Module 12 (fitting your forgetting curve).

> **Originality note:** the card format, log-replay design, importers, and simulation experiment were designed for this curriculum. SM-2 is a published algorithm used here as a component; its formula is credited above.
