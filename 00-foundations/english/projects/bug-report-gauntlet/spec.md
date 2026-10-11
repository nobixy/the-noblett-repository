---
title: "Project: Bug Report Gauntlet"
id: "FND-EN-PRJ-bug-report-gauntlet"
type: "project"
module: "00-foundations"
track: "english"
phase: "C"
order: 700
prerequisites: [E08]
stages: "E09"
artifact: "A graded review of 5 real bug reports, 10 bug reports of your own, and reproduction-test results"
deliverable: "The reports, the reproduction log, and a one-page reflection"
---

# Project: Bug Report Gauntlet

| | |
| :-- | :-- |
| **You build** | Ten bug reports that pass a strict test: someone else can reproduce the bug using only your report |
| **Deliverable** | The ten reports, the reproduction log, the review of five public reports, and a reflection |

---

## Why this matters

A good bug report is one of the most useful things an engineer can write. It turns "something's wrong" into a problem someone can actually fix. Open-source maintainers often close vague reports without reading them, and they fix clear ones fast. Inside companies, people who write clear reports get their problems solved and earn trust.

Writing the report also makes *you* a better debugger. To write "steps to reproduce," you must find the exact trigger. To make the steps minimal, you must remove everything that doesn't matter. By the time the report is minimal, you often know the cause.

The "gauntlet" is the test: a report passes only if someone else can reproduce the bug from it alone.

**Real-world analogs:** GitHub issues, Jira tickets, security disclosure reports, incident write-ups.

---

## Milestones

### Milestone 1 — Judge five real reports

Go to the public issue tracker of a large open-source project you use or have heard of (for example, the GitHub issues of VS Code, Firefox's Bugzilla, Python's issue tracker, or any popular tool). Pick **five bug reports**: some good, some bad.

Grade each with this rubric (0–2 points per row):

| Row | 0 | 1 | 2 |
| :-- | :-- | :-- | :-- |
| Title | Vague ("broken") | Symptom only | Symptom + trigger |
| Environment | Missing | Partial | OS, version, relevant details |
| Steps | Missing | Incomplete or not minimal | Complete and minimal |
| Expected vs actual | Missing | One of them | Both, clearly |
| Evidence | None | Paraphrased error | Exact output, logs, screenshot |
| Tone | Rude or demanding | Neutral but unclear | Polite, factual |

**Done when:** five reports graded, with one sentence per report on the single biggest improvement it needed. Note how maintainers responded to the best and worst ones.

### Milestone 2 — Five bugs from your own projects

Your own code has bugs. You've fixed many already; your git history and journal stuck notes remember them. Choose **five** (or create fresh ones by checking out an old commit with `git checkout <commit>`).

For each, write a full report using the E09 structure:

```
Title:
Environment:
Steps to reproduce:
Expected result:
Actual result:
Frequency:
Notes (facts first, then labelled guesses):
```

**Make the steps minimal:** start from what you remember, then remove steps one at a time. If the bug still happens without a step, delete it. Keep going until every remaining step is needed. Record how many steps you started with and ended with.

**Done when:** five reports with minimal steps, each with exact error output in code format.

### Milestone 3 — Five bugs in the wild

Find **five** real bugs or annoyances in software you use: a website that misbehaves, an app that freezes, a command-line tool with a confusing error, a game glitch. Write a report for each.

**For one or two of them, consider filing for real** (this is optional, and it's a real public action, so do it carefully):
1. Search the project's issue tracker first. If the bug is already reported, add your details as a comment only if they are new and useful.
2. Read the project's contributing guidelines or issue template, and follow it.
3. Be polite and factual. Maintainers are often volunteers.

**Done when:** five reports written; any you filed are linked in the log.

### Milestone 4 — The gauntlet: reproduction tests

**This is the real test.** A report passes when someone reproduces the bug from the report alone.

For at least **six** of your ten reports, run a reproduction test:
- **With a person:** give them the report and the software. Watch silently. Log every question and stumble. Pass = they see the bug without asking you anything.
- **Without a person:** wait until a later section (long enough that you forget the details), then follow your own report *exactly as written* in a **clean environment**: a fresh user account, a fresh virtual machine, or a fresh container (`docker run -it --rm python:3.12 bash`, if you have Docker). Pass = the bug appears, following only the written steps.

For each failure, fix the report and test again.

**Done when:** at least six reports have passed a reproduction test, and at least two of those were tested by another person.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *the report that failed its first reproduction test. What did you leave out, and why did it feel unnecessary to write?* (This is the curse of knowledge again, from the Machine Manual.)

---

## Common pitfalls

- **"It doesn't work."** Always say what *does* happen instead.
- **Paraphrased errors.** Copy them exactly. People search error messages letter by letter.
- **Hidden environment differences.** "It works on my machine" usually means a version, file, or setting you didn't mention. Clean-environment testing finds these.
- **Guesses as facts.** "The bug is caused by the cache" — unless you proved it, write "Possible cause: …".
- **Multiple bugs in one report.** Split them.
- **Blaming people.** Describe what the software does, not what the developer should have done.

## Communication deliverable

In `~/workbench/english/bug-gauntlet/`:
- `public-review.md`: the five graded public reports, with links.
- `reports/01.md` … `reports/10.md`: your reports.
- `reproduction-log.md`: for each test, who/how, pass/fail, problems found, fixes made.
- `reflection.md` (one page): the most common gap in your first drafts; how minimal steps changed your understanding of the bugs; what you'd tell a beginner about writing bug reports, in five bullet points.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 2, write the bug-report structure from memory |
| **W** | Why each rubric row matters; the failed-reproduction why-ladder |
| **S** | The report structure is a set of subgoal labels; minimising steps is a procedure |
| **D** | The wait (until a later section) before self-reproduction |
| **T** | The gauntlet itself |

## Stretch goals

- **Bisect a bug:** for one of your own bugs, use `git bisect` to find the exact commit that introduced it. Add the commit to the report.
- **Write a regression test** for each of your own five bugs: a test that fails when the bug is present. Link it in the report. (This becomes standard practice in Module 02.)
- **Triage practice:** spend one session on a project's "needs reproduction" or "needs info" issues. Try to reproduce one and add your results.

## Self-grading rubric

Score each of your ten reports with the Milestone 1 rubric (max 12).

**Done when:** every report scores at least 10/12, and at least six passed the gauntlet.

## Connections

- **Back:** E09 (bug report structure, precise words), E05 (past tense for what happened, present for what the system does).
- **Forward:** every project from Module 02 on. Each project's "Common pitfalls" section is really a list of bugs; your stuck notes [D] become bug reports; and in Module 02 you start writing a regression test for every bug you fix.
