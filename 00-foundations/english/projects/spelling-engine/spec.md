---
title: "Project: Spelling Engine"
id: "FND-EN-PRJ-spelling-engine"
type: "project"
module: "00-foundations"
track: "english"
phase: "A"
order: 100
prerequisites: [E01]
stages: "E01–E03, then after 01 Lab 01"
artifact: "spelling-log.tsv + spell_quiz.py + suffix_rules.py + spell_report.py"
deliverable: "README + 'What my data says' note + short demo"
---

# Project: Spelling Engine

| | |
| :-- | :-- |
| **You build** | Your personal spelling dataset, a talking quiz program that tests you on your own errors with spaced review, a program that applies English suffix rules, and a progress report |
| **Deliverable** | A README, a one-page "What my data says about my spelling" note, and a short recorded demo |

---

## Why this matters

Generic spelling courses test you on generic words. This project tests you on **your** words: the exact errors you make, scheduled for review at the exact moment you are about to forget them. You will build the tool you learn with.

It is also your first real data project. You will collect data (your errors), store it in a simple format, write programs that read and update it, and draw conclusions from it. That loop — collect, store, process, conclude — is the shape of a huge amount of real software.

And in Milestone 4 you will write the English spelling rules from E02 as code and test them against real words. You will see exactly where the rules work and where English breaks them. Rules as code, tested against data: that is how engineers think.

**Real-world analogs:** spaced-repetition apps (Anki, Duolingo's review system), spell checkers, and any system that tracks a user's mistakes to adapt (adaptive testing, recommendation systems).

---

## The data format

Everything starts from one file: `~/workbench/english/spelling-log.tsv`. Tab-separated, one header line, one word per line.

From Milestone 3 on, it has these columns (Milestones 1–2 use only the first five):

| Column | Meaning | Example |
| :-- | :-- | :-- |
| `date` | Date you first logged the error (YYYY-MM-DD) | `2026-10-12` |
| `wrong` | How you misspelled it (first time) | `seperate` |
| `right` | Correct spelling | `separate` |
| `tags` | Comma-separated error tags (E01 + E02 tags) | `vowel-unclear,pattern-schwa` |
| `hook` | Your memory hook | `there is a rat in sep-a-rat-e` |
| `box` | Leitner box, 1–5 | `2` |
| `due` | Next review date | `2026-10-15` |
| `right_count` | Times spelled right in a quiz | `3` |
| `wrong_count` | Times spelled wrong in a quiz (including the first) | `2` |

**Rules:**
- One row per *correct* word. If you misspell the same word a new way, don't add a row; increase `wrong_count`.
- No tabs inside fields. Commas are allowed inside `tags` and `hook`.
- The file is **plain text** so you can edit it in any editor and track it with git. (Why plain text and not a spreadsheet file? [W] Write your own answer in the README. Hint: think about what other programs and tools can read it, and what `git diff` shows.)

---

## Milestones

### Milestone 1 — The log (during E01, no code)

**Do:**
1. Create `spelling-log.tsv` with the header line `date	wrong	right	tags	hook`.
2. Add every error from your E01 baseline tests.
3. From now on, add every misspelling you notice anywhere: your journal, messages, code comments. Keep a small paper note between sessions and type them in at the start of the next session.

**Done when:** 30+ rows, each with at least one tag and a hook.

**Checkpoint:** none needed yet; the E01 self-check covers it.

### Milestone 2 — The section report by hand (during E02–E03, no code)

**Do:** at the end of every section, as part of the Section Review, write a short report in `english/spelling-reports.md`:
- rows added this section;
- the count of each tag (on paper, or with the `cut | sort | uniq -c` command shown in E02);
- your top two tags;
- words that are now "learned" (right in dictation on 4 separate spaced reviews, E01 rule).

**Done when:** 4 section reports written, and you can say your top two tags without looking.

**[W] Question to answer in the report:** *Why does your top tag happen? What is your brain doing when you make that error?* (Example: "For schwa errors, I spell the word the way I say it, and the lazy vowel gives no clue.")

### Milestone 3 — The talking quiz (after 01 Lab 01)

Build `spell_quiz.py`, a command-line program that quizzes you on words that are due for review.

**Required behaviour:**
1. Read `spelling-log.tsv`. Add the extra columns (`box`, `due`, `right_count`, `wrong_count`) if they are missing, with `box=1`, `due=today`, `right_count=0`, `wrong_count=1`.
2. Select every word whose `due` date is today or earlier. Shuffle them (interleaving [I]). Limit to 20 per session (a command-line option `--max N` changes this).
3. For each word:
   - **Speak it** using `espeak-ng` (run it from Python with the `subprocess` module). If `espeak-ng` is not installed, print a clear message and fall back to showing the hook with the word's letters hidden (e.g. `s _ _ _ _ _ _ e — there is a rat in…`).
   - Let the user type the spelling. Typing `r` replays the audio.
   - Compare. If right: print `✓`, move the word up one box (max 5).
   - If wrong: print the correct spelling, **show which letters were wrong** (see "Letter diff" below), show the hook, move the word to box 1, and ask the user to type it correctly once before moving on (immediate correction).
4. Set the new `due` date from the box: box 1 → +1 day, box 2 → +3 days, box 3 → +7 days, box 4 → +21 days, box 5 → +60 days. (These are the spacing intervals from [study-protocols](../../../../study-protocols.md#i--interleave-and-space).)
5. Write the file back. **Never lose data:** write to a temporary file first, then rename it over the original. (Why? [W] What happens to your log if the program crashes halfway through writing?)
6. At the end, print a summary: words reviewed, right, wrong, and the next due date for the earliest word.

**Letter diff:** show the user's attempt above the correct word with markers under the positions that differ. A simple position-by-position comparison is fine for this milestone:
```
you typed:  seperate
correct:    separate
               ^
```
(When the lengths differ, a position-by-position comparison gives confusing results. Note this as a limitation; you'll fix it properly in Module 05's Copydiff project.)

**Subgoal labels [S]:** write these as comments before coding:
```python
# 1. Load the log into a list of rows (dictionaries)
# 2. Fill in missing columns with defaults
# 3. Pick the due words, shuffle, limit
# 4. For each word: speak, read answer, compare, update box and due date
# 5. Save safely (temp file, then rename)
# 6. Print the summary
```

**Done when:**
- You have used it in **14 sessions** (not necessarily in a row) and the file is correct after every session.
- The tests below pass.

**Tests to write** (`test_spell_quiz.py`, using plain `assert` or `pytest`):
- Loading a log with only 5 columns fills the defaults correctly.
- A word due yesterday is selected; a word due tomorrow is not.
- Box and due date update correctly for right and wrong answers, including at box 5 (stays 5) and box 1 wrong (stays 1).
- Saving and reloading gives back the same data (a "round-trip" test).
- A hook containing a comma survives a save and reload.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *Why does a wrong answer send the word all the way back to box 1, instead of down one box?* (There is a real trade-off. Answer it both ways.)

### Milestone 4 — Rules as code

Build `suffix_rules.py` with one function:

```python
def add_suffix(word: str, suffix: str) -> str:
    """Return word + suffix, spelled using the E02 rules."""
```

It must apply, in a sensible order: **Rule 1** (doubling, for one-syllable 1-1-1 words), **Rule 2** (drop the silent e, keeping it after soft c/g before *-able*/*-ous*), **Rule 3** (y to i, except before *-ing* and after a vowel), and plural *-s/-es* from **Rule 5** when the suffix is `s`.

**Simplification allowed:** you can't easily detect stress in code. Handle multi-syllable doubling with a small exceptions dictionary (`{"begin", "occur", "prefer", "refer", "commit", "control", "forget", "transmit"}` double; everything else doesn't), and *say so* in the README.

**Test it against data:** create `suffix_cases.tsv` with at least **60** rows of `word	suffix	expected`, taken from E02's practice sets, E03's word lists, and your own error log. Include the exceptions (*truly, argument, daily, paid, said*). Write `check_rules.py` that runs every case and prints:
- the accuracy (e.g. `54/60 = 90%`);
- every failure, as `word + suffix: expected X, got Y`.

**Then analyse [W]:** sort the failures into (a) bugs in your code, (b) exceptions to the rule, (c) cases the rule doesn't cover (stress). Fix (a). Leave (b) and (c) and explain them.

**Done when:** accuracy ≥ 85% on your own 60+ cases, and every remaining failure is explained in a table in the README.

**Checkpoint:** Feynman target: *explain to a friend how your code decides whether to double a letter*. Compare your explanation to E02's rule. Did writing code change how you understand the rule?

### Milestone 5 — The progress report

Build `spell_report.py`, which reads the log and the baseline files and prints:
- total words logged; words learned (box 5, or `right_count ≥ 4`); words currently in each box;
- tag counts, as a text bar chart:
  ```
  pattern-schwa   ████████████ 12
  rule-double     ███████ 7
  homophone       █████ 5
  ```
- your free-writing error rate from each baseline file (E01, E03 retest, and any later ones), oldest to newest.

**Done when:** it runs on your real data and the numbers match a hand count for one tag.

---

## How you know it works

- The quiz never corrupts or loses your log (test: interrupt it with Ctrl+C in the middle of a session, then check the file).
- The spacing behaves as specified (tests in Milestone 3).
- The rule engine's accuracy is measured, not guessed.
- Most importantly: **your dictation scores and free-writing error rate improve**. That is the real test of a learning tool.

## Common pitfalls

- **Tabs vs spaces.** Some editors turn Tab into spaces. Check with `cat -A spelling-log.tsv` (tabs show as `^I`). Configure your editor to keep real tabs in `.tsv` files.
- **Dates as text.** Compare dates as `datetime.date` objects, not strings (string comparison works for `YYYY-MM-DD` only by luck of the format; know why).
- **Writing the file while reading it.** Read everything into memory first, then write.
- **Overbuilding.** Don't add a GUI, a database, or accounts. A small tool you use every session beats a big one you never finish.
- **Studying only in the tool.** The quiz is for review. New words still get the full Look–Say–Cover–Write–Check treatment by hand.

## Communication deliverable

1. **README.md** (E06 level is fine): what it is, how to run each program, the file format, the rule-engine accuracy table, and your answers to the two [W] questions in the spec (plain text; temp-file save).
2. **"What my data says about my spelling"** (one page, E07–E08 level): your top tags, how they changed, what you think causes them, and what you'll do about it. Include at least one number from `spell_report.py`.
3. **Demo (short, recorded):** run one quiz session and the report, and explain how the boxes work.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | The tool *is* retrieval practice; dictation, not recognition |
| **I** | Due words are shuffled; tags mix in every session |
| **W** | Plain text vs spreadsheet; temp-file save; reset-to-box-1 trade-off; failure analysis of the rule engine |
| **S** | Subgoal comments before coding each program |
| **F** | Explaining the doubling code vs the doubling rule |
| **T** | README, data note, and demo |

## Stretch goals

- **Sentence mode:** the quiz speaks a whole sentence containing the word (store sentences in a new column).
- **Confusables mode:** for homophones, speak a sentence and ask which word fits (*their/there/they're*).
- **Error-pattern guesser:** when you misspell a word, guess the tag automatically (doubled letter missing? e dropped wrongly?) and suggest it.
- **Stress dictionary:** use the CMU Pronouncing Dictionary (free, has stress marks) to handle multi-syllable doubling properly. Measure the accuracy change.
- **Merge into Study Deck** in Module 02: spelling words become one card type among many.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Data | 100+ rows, consistent tags and hooks, never corrupted | 30+ rows, mostly consistent | Gaps, broken rows |
| Quiz | All behaviour + tests pass; used in 14+ sessions | Works; few tests | Crashes or loses data |
| Rule engine | ≥ 90%, failures fully classified | ≥ 85%, failures listed | < 85% or not measured |
| Report | Accurate, matches a hand count | Runs | Missing |
| Writing | README + data note clear, revised with the E08 checklist | Complete | Missing parts |
| Demo | Clear, under 2:30 | Recorded | Missing |

**Done when:** every area scores at least 2, and Data and Quiz score 3.

## Connections

- **Back:** E01–E03 (everything), [01 Lab 01](../../../../01-intro-cs-taste/labs/lab-01-python-first-steps.md) (Python).
- **Forward:** Module 02 [Study Deck](../../../../02-programming-fundamentals/projects/study-deck/spec.md) generalises this to any flashcard; Module 05 [Copydiff](../../../../05-data-structures-and-algorithms/projects/copydiff/spec.md) replaces the position-by-position letter diff with a real diff algorithm.
