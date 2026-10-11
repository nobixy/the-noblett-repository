---
title: "Foundations: English"
id: "FND-EN"
type: "overview"
module: "00-foundations"
track: "english"
phase: "A"
order: 30
prerequisites: []
checkpoints: [FND-EN-ASSESS]
tags: [module, foundations, english]
---

# Foundations: English

*Part of [00 — Foundations](../overview.md).*

**From spelling to design documents.** This track rebuilds English from the bottom: how words are spelled, what each kind of word does, how a sentence is put together, how punctuation works, how sentences become paragraphs, and finally how to describe a system, write instructions, report a bug, argue for a design, and give a demo out loud.

It is written for an adult who is smart, works hard, and was never given a solid base in spelling and grammar. No baby talk. No shame. Just the rules, the reasons behind them, a lot of practice, and projects that make you use it.

---

## Why this matters for an engineer

Engineers write all the time: commit messages, bug reports, READMEs, design docs, messages to teammates, and answers to "how does this work?" A good engineer who cannot explain their work is treated as a weaker engineer. A clear writer gets trusted with bigger problems.

Writing is also a thinking tool. When you write a design doc, you find the holes in your design before you code them. When you explain a bug in clear sentences, you often find the cause while writing. This is why every project in this curriculum has a writing deliverable.

And the skills transfer directly:
- **Spelling** → function names, error messages, search queries (a misspelled search finds nothing), and looking professional.
- **Parts of speech** → naming things in code. Functions are verbs (`send_packet`), data is nouns (`packet`), true/false values are adjectives or questions (`is_empty`).
- **Sentence structure** → knowing *who does what to what*. "The kernel sends the process a signal." Precise subjects and verbs are how you describe systems without confusion.
- **Punctuation** → code is punctuation-heavy, and so are command lines and file paths. Exactness transfers.
- **Paragraphs** → one idea per paragraph is like one job per function.
- **Technical writing** → bug reports, docs, design reviews. The everyday work.

---

## What you will be able to do at the end

1. Spell the 1,000 most common English words and the 300 most common technical words correctly without help.
2. Recognise the eight parts of speech and use them to name things in code.
3. Write correct simple, compound, and complex sentences with correct verb forms and punctuation.
4. Write a clear paragraph with one main idea, and a one-page piece made of such paragraphs.
5. Describe how a system works, step by step, so that a beginner can follow.
6. Write instructions that a stranger can follow without asking you a question.
7. Write a bug report that someone else can use to reproduce the bug.
8. Write a design document that explains a plan, compares alternatives, and argues for a choice.
9. Give a short, structured spoken demo of something you built.

---

## The ten stages

Each stage is one file. Do them in order. Each has teaching, practice for every session, a self-check with answers, and a "done when" line.

| Stage | Title | Core content | Project hook |
| :-- | :-- | :-- | :-- |
| [E01](E01-spelling-baseline-and-high-frequency-words.md) | Spelling baseline and high-frequency words | Measure where you are; the words that make up most text; how to learn a spelling | [Spelling Engine](projects/spelling-engine/spec.md) starts |
| [E02](E02-sound-patterns-and-spelling-rules.md) | Sound patterns and spelling rules | Vowel and consonant patterns; the big six spelling rules | Spelling Engine: rule tags |
| [E03](E03-word-parts-and-confusable-words.md) | Word parts and confusable words | Prefixes, suffixes, roots; their/there/they're and 40 more pairs; technical vocabulary | Spelling Engine: v1 complete |
| [E04](E04-parts-of-speech.md) | Parts of speech | What each kind of word does; naming in code | [Machine Manual](projects/machine-manual/spec.md) starts |
| [E05](E05-the-simple-sentence-and-verbs.md) | The simple sentence and verbs | Subject–verb–object; the five sentence patterns; tense; agreement; irregular verbs | Machine Manual |
| [E06](E06-punctuation.md) | Punctuation | Capitals, end marks, commas, apostrophes, colons, semicolons, quotes, dashes, code formatting | Machine Manual: complete |
| [E07](E07-joining-ideas.md) | Joining ideas | Compound and complex sentences; run-ons and fragments; parallel lists | [Terminal Field Notes](projects/terminal-field-notes/spec.md) |
| [E08](E08-paragraphs-and-clarity.md) | Paragraphs and clarity | Topic sentences; old-before-new; the clarity rules; cutting words | Field Notes; [Explain-a-System](projects/explain-a-system/spec.md) starts |
| [E09](E09-technical-description-and-instructions.md) | Technical description and instructions | Describing systems; instructions; bug reports; READMEs; speaking clearly | [Bug Report Gauntlet](projects/bug-report-gauntlet/spec.md); Explain-a-System |
| [E10](E10-argument-and-design-documents.md) | Argument and design documents | Claim–reason–evidence; trade-offs; design docs; editing; demos | [First Design Doc](projects/first-design-doc/spec.md) |

### Pace

There is no schedule. Each stage's practice routine is written as numbered **sections** of five **English sessions** each (see [study-protocols § The session loop](../../study-protocols.md#the-session-loop)), and a stage is done when its "Done when" list is true. Spelling practice and copywork continue after E10 as a short part of every English session.

**Start in the right place:** take the [placement diagnostic](placement.md) first. **Go faster** if a stage's self-check is easy on the first try: do the self-check, fix misses, and move on. **Go slower** if the self-check score is under 80%: repeat the practice section with new examples. There is no prize for speed.

---

## The English session

| Step | What | Protocol |
| :-- | :-- | :-- |
| 1 | **Warm-up recall:** write the last session's rule from memory, with one example | [R] |
| 2 | **Spelling:** the session's word set using Look–Say–Cover–Write–Check (E01) | [R] [I] |
| 3 | **Stage lesson or practice set** from the current stage file | [S] [W] |
| 4 | **Copywork** at your current level (below) | [C] |
| 5 | **Log:** misspelled words go in your error log; one line in the journal | — |
| + | **Fun write** (most sessions): a prompt from the [writing prompt bank](writing-prompts.md) for your stage — fast, no spell checker, then check it for this stage's skill | [C] [T] |
| + | **Touch typing** on keybr.com (Sections 1–12), then Monkeytype's English 1k list ([how](../first-sections.md#touch-typing-sections-112)) | [I] |

Flashcard review can go here or in a math session. Spelling cards and grammar-rule cards share the same deck as everything else.

**Minimum session:** one copywork sentence (fast version) and your flashcards. That counts.

---

## Copywork ladder

Franklin copywork [C] is the backbone of this track. You rebuild good sentences from memory and compare. The passages get harder as you climb. Pick passages about technology and how things work, so the vocabulary is useful to you.

| Level | Use during | Sources (all free online) | Passage length |
| :-- | :-- | :-- | :-- |
| **1. Plain** | E01–E04 | **Simple English Wikipedia** articles on machines and technology (simple.wikipedia.org: "Computer", "Electricity", "Bicycle", "Internet"); **VOA Learning English** science and technology stories | 2–3 sentences |
| **2. Clear technical** | E05–E07 | **The Python Tutorial** (docs.python.org/3/tutorial), first paragraphs of each section; **Julia Evans**' blog (jvns.ca) and zines; the "DESCRIPTION" section of short man pages (`man ls`, `man cp`, `man echo`) | 3–5 sentences |
| **3. Essays** | E08–E09 | **Paul Graham** essays (paulgraham.com), e.g. "Write Simply", "How to Do Great Work"; **The Feynman Lectures on Physics** Vol. I ch. 1–4 (feynmanlectures.caltech.edu); **Joel Spolsky** (joelonsoftware.com), e.g. "Painless Bug Tracking", "Painless Functional Specifications" | 5–8 sentences |
| **4. Engineering prose** | E10 and after | **RFC 768** (UDP, 3 pages, a model of short precise spec writing); **Rob Pike**, "Notes on Programming in C"; **Go proposal** design docs (github.com/golang/proposal); **The Architecture of Open Source Applications** chapters (aosabook.org) | a full paragraph or short section |

**Rules for copywork:**
- No spell checker during copywork. The point is to catch your own errors in the diff.
- Count your differences. Write the count in the log. Watch it fall over the sections: that is your progress graph.
- Move up a level when you can rebuild a passage at your level with fewer than 3 spelling errors and the meaning intact, three times in a row.

---

## Video course

- **Primary:** **Khan Academy Grammar** (Khan Academy) — [YouTube playlist](https://www.youtube.com/playlist?list=PL6CQ7apI_8PjSBN8BxukW5Z76k8lRMQEf) · [course with exercises](https://www.khanacademy.org/humanities/grammar). Parts of speech, punctuation and syntax, in nearly the order of E04–E07.
- **Alternate:** **Writing in the Sciences** (Stanford Online, Dr. Kristin Sainani, on Coursera; listed as Free) — [course](https://www.coursera.org/learn/sciwrite). Modules 1–4 for clarity and revision in E08–E10.
- **Which lectures go with which lab and project:** the map in [resources](<resources.md#lesson-to-vault-map>). Watch with the [V protocol](../../study-protocols.md#v--watch-actively) and [use courses as companions](../../study-protocols.md#using-video-courses).
- **Gaps:** Spelling (E01–E03) has no good video course, and E09–E10 lean on Google's free [Technical Writing One](https://developers.google.com/tech-writing/one) and [Two](https://developers.google.com/tech-writing/two).

---

## Fun, videos, and courses

- **[Writing prompts](writing-prompts.md):** 150+ fun prompts sorted by stage, plus constraint games, project-tied prompts, and speaking prompts for your section recording.
- **Video course:** see [above](#video-course). Every stage file also has a short **Watch, practise, and write** section with extra videos for that stage.
- **[The first sections](../first-sections.md):** Sections 1–12 with targets, companions, and badges for the start.
- **[Placement diagnostic](placement.md):** where to start, and which stages you can test out of.

## How the study methods run through this track

| Protocol | How it shows up in English |
| :-- | :-- |
| **R** Blank-sheet retrieval | Spelling tests from memory (dictation, not recognition). Rule recall: write the rule and two examples from memory. Each section: rewrite the stage's rules on a blank page. |
| **F** Feynman pass | Explain each grammar idea in plain words: "What does a comma before *and* do?" You also teach-back each stage's main rule out loud once (record it). |
| **W** Why-ladder | Every rule gets a "why does this rule exist?" Most English rules exist to stop a reader from misreading. You will find the misreading each rule prevents. |
| **S** Subgoal labels | Sentence analysis and editing are procedures. Each has labelled steps (e.g. "find the verb → find who does it → find what it is done to"). |
| **I** Interleave and space | Mixed practice sets in every stage, plus review sets with old stages' rules. Spelling words return on the flashcard spacing schedule ([I], part of the technique). |
| **C** Copywork | Every English session, climbing the ladder above. |
| **D** Diffuse break | When a sentence will not come right, write the stuck note and leave it. Writing especially benefits from coming back in a later session. |
| **T** Teach-back and write-up | Every project ends with a piece of writing someone else reads or uses, and from E08 on, a spoken version. |

---

## Projects in this track

Each project grows with you across several stages. Each one is a small part of each session, but real.

| Project | Stages | What you make |
| :-- | :-- | :-- |
| [Spelling Engine](projects/spelling-engine/spec.md) | E01–E03, then Module 01–02 | Your own error log, rule tags, and a quiz program that reads words aloud and tests you on *your* misspellings |
| [Machine Manual](projects/machine-manual/spec.md) | E04–E06 | A tested user manual for a real machine in your home, then for five terminal commands |
| [Terminal Field Notes](projects/terminal-field-notes/spec.md) | E07–E08 | A field notebook of what your Linux machine does, growing into a short guide: "What my computer does when I…" |
| [Explain-a-System](projects/explain-a-system/spec.md) | E08–E09 | Five written and spoken explainers of everyday systems, each previewing a later module |
| [Bug Report Gauntlet](projects/bug-report-gauntlet/spec.md) | E09 | Ten bug reports for real and planted bugs, tested by whether someone else can reproduce them |
| [First Design Doc](projects/first-design-doc/spec.md) | E10 | The design doc for Copydiff, the copywork diff tool you build in Module 05, reviewed and revised before you build it |

---

## Connections

- **Before:** nothing. This is the start.
- **Alongside:** [Math foundations](../math/overview.md) in math sessions. [01 Intro CS Taste](../../01-intro-cs-taste/overview.md) starts after E01. Its write-ups are sized for where you are.
- **After:** every module's deliverables. Module 05's first project, Copydiff (a tool that automates step 6 of copywork for the rest of your life), is built from the design doc you write in E10.
- **Deliverables grow with you.** Modules 01–02 ask for short written notes and spoken demos sized for E02–E07. Modules 03–04 add lab reports (E08). From Module 05 on, every major project starts with a full design doc (E10).

| Later need | Comes from |
| :-- | :-- |
| Naming variables and functions well | E03 (word parts), E04 (parts of speech) |
| Commit messages ("Fix crash when file is empty") | E05 (imperative verbs) |
| Code comments that explain *why* | E07 (because/so/although clauses) |
| README files | E09 |
| Bug reports and issue comments | E09 |
| Design docs, lab reports | E08, E10 |
| Demo videos and interviews | E08–E10 spoken practice |

---

## Track assessment

When you finish E10, take this cold, in one sitting (checkpoint id `FND-EN-ASSESS`), and file it in your journal:

1. **Dictation:** 50 words chosen at random from your E01–E03 lists (use your Spelling Engine to read them aloud). Target: 48/50.
2. **Editing:** take a 300-word paragraph you wrote early on (from your journal). Fix every error and rewrite it clearly. Count the changes.
3. **Description:** in 400 words, explain how something you built in Module 01 works, for a beginner.
4. **Instructions:** write instructions for installing and running that project. Give them to someone who has never seen it. They must succeed without asking you a question.
5. **Spoken:** a short recorded explanation of the same project, no script, from notes only.

**Done when:** all five are finished and the dictation is ≥ 46/50. If not, note the weakest area, work through its stage's practice sections again, and retake that part.
