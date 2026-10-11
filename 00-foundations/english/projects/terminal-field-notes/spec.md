---
title: "Project: Terminal Field Notes"
id: "FND-EN-PRJ-terminal-field-notes"
type: "project"
module: "00-foundations"
track: "english"
phase: "B"
order: 340
prerequisites: [E06]
stages: "E07–E08"
artifact: "A field notebook of 15+ observations of your Linux machine, revised into a 1,200–1,800 word guide"
deliverable: "The guide + before/after revision statistics"
---

# Project: Terminal Field Notes

| | |
| :-- | :-- |
| **You build** | A field notebook: short observations, one or more per session, of what your computer is doing, written like a naturalist's notes. Then you revise them into a clear guide: *What My Computer Is Doing Right Now* |
| **Deliverable** | The guide, and a short note with before/after revision numbers |

---

## Why this matters

Scientists keep field notes: dated, exact observations, with questions and guesses clearly labelled. Engineers do the same in lab notebooks and debugging logs. Writing an observation precisely ("*`free -h` showed 5.1 GiB used of 15 GiB*") is very different from writing a feeling ("*memory seemed fine*"), and it's a skill.

This project trains two things at once:
1. **Joining ideas** (E07): observations need *because, when, although, so* to show how facts relate.
2. **Paragraph clarity** (E08): turning raw notes into a clear guide is exactly the work of revision.

And it is a preview. Every command you explore here opens a door to a later module: processes and memory (Module 08, operating systems), disks and files (Modules 07–08), network addresses (Module 09), the boot log (Module 08). You will meet these things again, and you will already have written about them.

**Real-world analogs:** lab notebooks, incident logs, debugging journals, system-administration runbooks.

---

## The entry format

Keep the notebook as `~/workbench/english/field-notes.md`. Each entry:

```markdown
### 2026-11-03 — What is using my memory?

**Command:** `free -h`

**Observed:** The "used" column showed 5.1Gi out of 15Gi total. The "buff/cache" column showed 6.2Gi.

**What I think it means:** My programs are using about a third of the memory. Linux uses much of the rest as a cache, because empty memory is wasted memory.

**Question:** If the cache uses 6.2Gi, why does "available" say 9.4Gi instead of 3.7Gi?
```

**Rules:**
- **Observed** is past tense and contains only facts you saw. Copy numbers and messages exactly. Code format for commands and output.
- **What I think it means** is present tense, and it is allowed to be wrong. Use joining words (*because, so, although, when*) to show your reasoning.
- **Question** is one real question. Some you'll answer later; some you'll answer by research. Write the answer as a later entry when you find it.
- 3–6 sentences per entry, not counting the command.

---

## The commands to explore

One or two per entry. Run them; don't just read about them. Use `man <command>` or `<command> --help` to understand options.

| Area | Commands | A question to start with |
| :-- | :-- | :-- |
| **Who am I, where am I** | `whoami`, `pwd`, `hostname`, `uname -a` | What does each part of `uname -a` mean? |
| **Files** | `ls -l`, `ls -la ~`, `stat <file>`, `file <file>` | What do the letters `-rw-r--r--` mean? |
| **Disk** | `df -h`, `du -sh ~/*`, `lsblk` | Which folder in my home uses the most space? |
| **Memory** | `free -h` | Why is so much memory "cache"? |
| **Processes** | `ps aux | head`, `top` (press `q` to quit), `pstree` | Which program uses the most CPU right now? What is process 1? |
| **Hardware** | `lscpu`, `lsusb`, `lspci`, `sensors` (if installed) | How many cores does my CPU have? What's plugged into my USB ports? |
| **Time and uptime** | `uptime`, `date` | What does "load average" mean? |
| **Network** | `ip addr`, `ip route`, `ping -c 4 example.com`, `ss -tuln` | What is my computer's address? What is listening on my machine? |
| **The boot** | `journalctl -b | head -50`, `systemd-analyze` | What happens in the first second after power-on? How long does my boot take? |
| **Inside a program** | `which python3`, `ldd $(which python3)`, `strace -c ls` (may need install) | What does `ls` ask the operating system to do? |

---

## Milestones

### Milestone 1 — Fifteen entries (E07)

**Do:** write at least **15 entries** across several sections, covering at least **6 of the 10 areas**. At least 3 entries should answer a question from an earlier entry.

**Writing focus (E07):** in "What I think it means," use at least one complex sentence (*because, when, although, if*) per entry. Check every entry for run-ons and fragments before moving on.

**Done when:** 15+ entries, 6+ areas, 3+ answered questions, no run-ons or fragments.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: without looking, write what each of the 10 areas' commands tells you. Why-ladder target: pick your most surprising observation and ask "why?" three times. Use `man` pages and search to answer.

### Milestone 2 — The guide, draft 1 (E08)

**Do:** turn your notes into a guide titled **"What My Computer Is Doing Right Now"** for a reader who has just installed Linux and is curious. 1,200–1,800 words.

**Structure:**
1. **Introduction** (one paragraph): what this guide shows and how to use it.
2. **One section per area** (choose 5–6 areas). Each section:
   - a heading;
   - a topic sentence saying what this area is about;
   - the command(s), with an example of the output (from your notes);
   - what the output means, in clear paragraphs;
   - one "try this" suggestion.
3. **Conclusion** (one paragraph): what surprised you most, and what you want to learn next.

**Writing focus (E08):** topic sentences; old-before-new; one idea per paragraph. Define every technical term on first use (*process, cache, kernel, interface*).

**Done when:** draft 1 is complete. Save it as `guide-v1.md` and **don't touch it until a later section** [D].

### Milestone 3 — Revise, measure, and get a reader (E08)

**Do:**
1. Revise using the full E08 checklist, in order: structure → paragraphs → sentences → words → read aloud → spelling. Save as `guide-v2.md`.
2. **Measure** (`wc -w`, and by hand):
   - word count before and after;
   - number of nominalizations removed;
   - number of passive sentences changed to active (where the actor mattered);
   - number of sentences that now start with old information that didn't before.
3. **One reader:** ask someone (a friend, a study partner, an online community) to read one section and tell you the one place they got lost. Fix it.
4. **Diff** v1 and v2 in the terminal: `diff guide-v1.md guide-v2.md | head -50`, or `git diff --word-diff` if both are in git. Read your own changes.

**Done when:** v2 is done, the numbers are recorded, and one reader's confusion is fixed.

---

## Common pitfalls

- **Explaining before observing.** Run the command first. Write what you *saw*. Then think.
- **Copying explanations from the web.** Research is good; copying is not. Read, close the tab, then write in your own words [R]. Link your source.
- **Paraphrasing output.** Copy it exactly in code format. Exact output is evidence.
- **Running dangerous commands.** Everything in the table is read-only. Don't run commands with `sudo` or `rm` that you found online unless you understand every part.
- **A guide that is a list of commands.** The guide is about *what the computer is doing*. Commands are how we look. Keep the focus on the machine.

## Communication deliverable

1. `field-notes.md` (the raw notebook, unedited after Milestone 1).
2. `guide-v2.md` (the final guide).
3. `revision-note.md`: half a page with the Milestone 3 numbers and three sentences on what you learned about your own writing.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Milestone 1 checkpoint: recall what each command shows |
| **W** | Every "Question" line; the three-level why on your most surprising observation |
| **F** | The guide is a long-form Feynman explanation for a curious beginner |
| **D** | The cooling-off between drafts |
| **C** | Copywork during this project: Julia Evans' writing on Linux tools (jvns.ca), which is exactly this kind of "here's what I observed and what it means" explanation |
| **T** | The reader in Milestone 3 |

## Stretch goals

- **Watch it change:** run the same command at different times (just booted, under load, after hours) and write a short comparison.
- **Draw it:** a diagram of the processes tree (`pstree`) with captions for the five most important ones.
- **Publish:** post the guide on a blog or a GitHub repository. Strangers' questions are excellent feedback.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Observations | Exact, copied output; clear fact vs guess | Mostly exact | Vague or paraphrased |
| Joining ideas | Logic words used correctly and truthfully | Some | Lists of short disconnected sentences |
| Guide structure | Every section has a topic sentence; skim test passes | Most sections | Missing topic sentences |
| Revision | Measured; v2 clearly better; reader's issue fixed | Revised, not measured | No real revision |
| Definitions | Every technical term defined on first use | Most | Few |

**Done when:** all areas at least 2, and Revision at 3.

## Connections

- **Back:** E07 (joining ideas), E08 (paragraphs, clarity, revision); [Machine Manual](../machine-manual/spec.md) (terminal commands).
- **Forward:** Module 07 (files, system calls — revisit your `strace` entry), Module 08 (processes, memory, boot), Module 09 (`ip`, `ping`, `ss`). When you reach those modules, reread your notes and write one entry correcting something you got wrong. That entry is a great measure of how far you've come.
