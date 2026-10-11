---
title: "E06 — Punctuation"
id: "E06"
type: "lesson"
module: "00-foundations"
track: "english"
stage: "E06"
phase: "B"
order: 310
prerequisites: [E05]
---

# E06 — Punctuation

**In this stage you will:** learn capital letters, end marks, the six comma rules, apostrophes, colons, semicolons, quotation marks, hyphens and dashes, parentheses, number style, and how to format code and commands in writing. You will finish the [Machine Manual](projects/machine-manual/spec.md).

**Before you start:** E05 done. You can find the core (subject + verb) of any sentence.

---

## Why punctuation matters

Punctuation tells the reader how to group words. Spoken English uses pauses and tone for this. Written English has only marks on the page.

Get it wrong and the meaning changes:
> Let's eat, Grandma. (talking to Grandma)
> Let's eat Grandma. (a very different plan)

> Delete the files, logs, and backups. (three things)
> Delete the files: logs and backups. (one thing — the files — which are the logs and backups)

In technical writing, punctuation can change an instruction. And you already work in a world where punctuation is exact: in code and commands, one missing comma or quote is an error. That exactness is a skill you can carry into English.

> **The big why [W]:** almost every punctuation rule exists to stop one specific misreading. For each rule below, find the misreading it prevents. If you can name it, you will never forget the rule.

---

## Part 1 — Capital letters and end marks

### Capitals

Use a capital letter for:
1. the **first word of a sentence**;
2. the word **I**;
3. **proper nouns** — names of specific people, places, organisations, products, days, months, languages: *Linux, Python, Raspberry Pi, Monday, October, English, Germany*;
4. **titles** of documents (main words): *The Python Tutorial*.

**Do not** use capitals for emphasis (USE *italics* OR **bold** INSTEAD). **Do not** capitalise ordinary nouns because they feel important (*the Server* ✗ → *the server* ✓).

**Tech names keep their official spelling,** even at the start of a sentence if you can avoid it: *iPhone, macOS, GitHub, JavaScript, npm, eBay*. Commands and file names are case-sensitive, so `ls` and `LS` are different things. Write them exactly as they are, in code format (Part 8).

**Acronyms** are usually all capitals: *USB, CPU, HTTP, TCP, RAM*. Their plurals take only *s*: *CPUs, APIs, URLs* (no apostrophe; see Part 3).

### End marks

- **Period / full stop (.)** ends a statement or command.
- **Question mark (?)** ends a direct question: *Did the test pass?* (But not an indirect question: *I asked whether the test passed.*)
- **Exclamation mark (!)** shows strong feeling. Avoid it in technical writing; let the facts be strong instead.

---

## Part 2 — The comma: six rules

The comma is the most-used and most-misused mark. Most of comma use is covered by six rules.

### Rule 1 — Commas in a list of three or more

> I bought a cable, a switch, and a power supply.

The comma before *and* is called the **serial comma** (or Oxford comma). This curriculum uses it, because it prevents misreadings:
> I thanked my parents, Linus Torvalds and Ada Lovelace.
> (Are my parents Linus and Ada?)
> I thanked my parents, Linus Torvalds, and Ada Lovelace.
> (Four people. Clear.)

### Rule 2 — Comma before *and, but, or, so* (FANBOYS) joining two complete sentences

> The test passed, **but** the build is slow.
> The disk was full, **so** the program stopped.

Both halves must be complete sentences (each with its own subject and verb). If the second half has no subject, no comma:
> The program read the file and printed it. (no comma: *printed* shares the subject *program*)

### Rule 3 — Comma after an introduction

When something comes before the main subject (a time, a condition, a reason, a linking word), put a comma after it.
> **After the update,** the laptop ran faster.
> **If the light is red,** unplug the cable.
> **However,** the second test failed.

Short introductions (2–3 words) can skip it, but the comma is never wrong.

### Rule 4 — Commas around extra information

If you could remove a part and the sentence would still mean the same thing, it is **extra**. Put commas around it.
> The router, **which is in the closet,** needs a restart.
> (There is one router. "Which is in the closet" is extra information.)

If the part tells you **which one**, it is **essential**. No commas.
> The router **that is in the closet** needs a restart.
> (There are several routers; this tells you which one.)

**which / that:** in American English, use *which* with commas (extra) and *that* without (essential). This one pairing will make your writing look careful.

### Rule 5 — Commas between equal describing words

> a slow, noisy fan

Test: could you say "slow **and** noisy fan"? Could you swap them ("noisy, slow fan")? If yes, use a comma. If not, don't: *a bright red light* (not "bright and red"; *bright* describes *red*).

### Rule 6 — Commas in numbers, dates, addresses, and when speaking to someone

> 1,000,000 · October 10, 2026 · Portland, Oregon · Thanks, Sam.

(In code, never put commas in numbers: `1000000`. Python allows `1_000_000`.)

### Two comma mistakes to stop making

1. **No comma between a subject and its verb.**
   > ✗ The cable under the desk, is loose.
   > ✓ The cable under the desk is loose.
2. **No comma alone between two complete sentences.** This is called a **comma splice**.
   > ✗ The test failed, I don't know why.
   > ✓ The test failed. I don't know why.
   > ✓ The test failed, and I don't know why.
   > ✓ The test failed; I don't know why. (Part 4)

---

## Part 3 — Apostrophes

The apostrophe (') has exactly **two** jobs.

### Job 1: Show missing letters (contractions)

| Full | Short | Missing |
| :-- | :-- | :-- |
| do not | don't | o |
| it is / it has | it's | i / ha |
| they are | they're | a |
| would not | wouldn't | o |
| I am | I'm | a |
| you have | you've | ha |

**In formal technical writing** (design docs, reports, documentation), most writers avoid contractions. In messages, READMEs, and blog posts, they're fine.

### Job 2: Show possession (belonging)

| Owner | Add | Example |
| :-- | :-- | :-- |
| one owner | **'s** | the **server's** address · **James's** laptop |
| plural owner ending in s | **'** | the **servers'** addresses (many servers) |
| plural owner not ending in s | **'s** | the **children's** room · **people's** data |

### The apostrophe never makes a plural

> ✗ two CPU's · the 1990's · three file's · API's
> ✓ two CPUs · the 1990s · three files · APIs

### The *its* rule

**Possessive pronouns never have apostrophes:** *its, his, hers, ours, yours, theirs, whose*.
> The program saved **its** state. (belongs to it)
> **It's** saving now. (it is)

---

## Part 4 — Colons and semicolons

### Colon (:)

A colon says **"here it comes."** It follows a **complete sentence** and introduces a list, an explanation, or an example.
> You need three tools: a multimeter, a soldering iron, and wire cutters.
> The cause was simple: the cable was unplugged.

**Rule:** what comes before the colon must be a complete sentence.
> ✗ You need: a multimeter and wire.
> ✓ You need a multimeter and wire.
> ✓ You need two things: a multimeter and wire.

(Exception: labels and headings, like "Note:" or "Done when:", are fine.)

### Semicolon (;)

A semicolon has two jobs.
1. **Joins two complete sentences** that are closely related, when you don't want a full stop.
   > The first test passed; the second one timed out.
2. **Separates items in a list when the items contain commas.**
   > The meetings are in Austin, Texas; Denver, Colorado; and Portland, Oregon.

If you are unsure, use a full stop. You can write excellent technical English without ever using a semicolon.

> **Programmer's note:** in many programming languages the semicolon ends a statement. In English it does not end anything; it *joins*. Don't let C habits leak into your prose.

---

## Part 5 — Quotation marks

Use quotation marks for:
1. **exact words** someone said or wrote: *The error said "permission denied."*
2. **titles** of short works (articles, chapters, essays): *Paul Graham's essay "Write Simply."*
3. **a word used as a word** (italics also work): *The word "data" is often singular.*

**American rule:** periods and commas go **inside** the closing quote: *He called it "the fast version."* Question marks go inside only if they belong to the quote.

**The technical problem:** that American rule breaks commands. If you write

> Type "ls -la."

a reader might type the full stop too. **For commands, file names, code, and anything the reader must type exactly, use code formatting instead of quotes** (Part 8):

> Type `ls -la`.

---

## Part 6 — Hyphens and dashes

### Hyphen (-): joins words

1. **Describing words joined before a noun:**
   > a **64-bit** processor · a **well-known** bug · an **open-source** project · a **read-only** file · a **two-step** process
   After the noun, usually no hyphen: *the project is open source.*
2. **Some prefixes:** *re-enter, co-author, self-hosted, non-blocking* (check a dictionary; many are one word: *reboot, nonzero*).
3. **Numbers from 21 to 99 written as words:** *twenty-one*.

### Dashes

- **En dash (–)** for ranges: *pages 3–7, 2–4 hours, Monday–Friday*. A hyphen is acceptable if you can't type the en dash.
- **Em dash (—)** for a sharp break or an aside: *The fix was simple — once we found the bug.* Use sparingly. A comma, colon, or parentheses usually work.

---

## Part 7 — Parentheses and numbers

### Parentheses ( )

Use for extra information the reader can skip:
> The Pico (a $5 microcontroller board) runs MicroPython.

If the parenthesis is inside a sentence, the full stop goes outside. (If it is a whole sentence on its own, like this one, the stop goes inside.)

### Numbers in writing

| Rule | Example |
| :-- | :-- |
| Spell out zero to nine; use digits for 10 and up | three files · 12 files |
| Always use digits with units | 5 V · 3 ms · 8 GB · 2 hours |
| Always use digits for versions, measurements, and code values | version 3.12 · port 8080 · 0.5 seconds |
| Don't start a sentence with digits | ✗ 12 tests failed. ✓ Twelve tests failed. ✓ In total, 12 tests failed. |
| Put a space between number and unit | 5 MB (not 5MB) — except % and ° (50%, 90°) |

---

## Part 8 — Code formatting in writing

You will write most of your technical documents in **Markdown** (like these files). Markdown uses backticks for code.

| What | How to write it | Looks like |
| :-- | :-- | :-- |
| A command, file name, function, variable, key | `` `ls -la` `` | `ls -la` |
| A multi-line block of code or terminal output | three backticks on their own lines before and after | a grey block |
| A key press | `Ctrl+C` or <kbd>Ctrl</kbd>+<kbd>C</kbd> | |

**Rules:**
1. Anything the reader must **type exactly** goes in code format.
2. Anything the computer **prints** goes in code format, copied exactly (don't fix its spelling or punctuation; it's evidence).
3. Don't put punctuation inside code format unless it's part of the code.

> To list hidden files, run `ls -a`. If you see `.bashrc`, your shell config exists.

---

## Part 9 — Practice routine (3 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Session 1: capitals and end marks · Session 2: comma rules 1–2 · Session 3: comma rules 3–4 · Session 4: comma rules 5–6, splices · Session 5: Practice Set 1 |
| 2 | Session 1: apostrophes · Session 2: colons and semicolons · Session 3: quotes and code formatting · Session 4: hyphens, dashes, parentheses, numbers · Session 5: Practice Set 2 |
| 3 | Sessions 1–2: Practice Set 3 (your own writing) · Sessions 3–4: Machine Manual Milestone 3 · Session 5: self-check |

**Every session:**
- **Warm-up [R]:** write the six comma rules from memory, each with an example. (By section 2, add the two apostrophe jobs and the colon rule.)
- **Punctuation hunt:** in this session's copywork passage, label every punctuation mark with the rule it follows. When the author breaks a rule, ask why [W].
- **Spelling** and **copywork [C]** (Level 2). Punctuation differences now count in your diff.

**Study protocols:**
- **[W]** For each comma rule, write the misreading it prevents. Example for Rule 4: without commas, "The router which is in the closet needs a restart" suggests there are several routers.
- **[S]** Subgoal labels for checking any comma: (1) Is it in a list? (2) Is it before FANBOYS joining two complete sentences? (3) Is it after an introduction? (4) Is it around extra info? (5) Between equal describers? (6) Number/date/name? → If none apply, delete it.
- **[F]** Teach the apostrophe to a friend, briefly. Record it. The only content: two jobs, and "never for plurals."

---

## Practice sets

### Practice Set 1 — Commas (10 sentences)

Add or remove commas. Some sentences are already correct.

1. I need a screwdriver a multimeter and some wire.
2. The test passed but the build took ten minutes.
3. After the update the fan got louder.
4. The laptop which I bought in 2019 still works.
5. The cable that connects the monitor is loose.
6. The program read the file and printed the result.
7. The light on the router, is blinking.
8. The download failed, I will try again.
9. My old, slow laptop runs Linux.
10. However the second test failed.

<details>
<summary>Answers (Set 1)</summary>

1. I need a screwdriver, a multimeter, and some wire. (Rule 1)
2. The test passed, but the build took ten minutes. (Rule 2)
3. After the update, the fan got louder. (Rule 3)
4. The laptop, which I bought in 2019, still works. (Rule 4: extra info; there's one laptop)
5. Correct as is. (*that* = essential: which cable)
6. Correct as is. (*printed* has no new subject, so no comma)
7. The light on the router is blinking. (no comma between subject and verb)
8. The download failed. I will try again. *or* …failed, so I will try again. *or* …failed; I will try again. (comma splice)
9. Correct as is. (Rule 5: "old and slow" works)
10. However, the second test failed. (Rule 3)
</details>

### Practice Set 2 — Everything else (12 sentences)

Fix the punctuation, capitals, and formatting.

1. the server's are in the basement.
2. Its not the cable, its the port.
3. We bought three new CPU's.
4. You need: a breadboard and an LED.
5. The first test passed, the second timed out.
6. To see the files type "ls."
7. This is a well known problem with 64 bit builds.
8. I use python on linux every Monday.
9. 12 tests failed after the update.
10. The childrens' laptops are slow.
11. The file is 5MB and the copy took 3ms.
12. Read the chapter "Errors and Exceptions" in the python tutorial.

<details>
<summary>Answers (Set 2)</summary>

1. The servers are in the basement. (capital; no apostrophe for plurals)
2. It's not the cable; it's the port. (*it is*; also fix the comma splice: semicolon, full stop, or "…the cable. It's the port.")
3. We bought three new CPUs.
4. You need a breadboard and an LED. *or* You need two things: a breadboard and an LED.
5. The first test passed; the second timed out. (or a full stop)
6. To see the files, type `ls`. (Rule 3 comma; code format; full stop outside)
7. This is a well-known problem with 64-bit builds.
8. I use Python on Linux every Monday.
9. Twelve tests failed after the update. (or: After the update, 12 tests failed.)
10. The children's laptops are slow.
11. The file is 5 MB, and the copy took 3 ms. (spaces before units; comma before *and* joining two sentences)
12. Read the chapter "Errors and Exceptions" in *The Python Tutorial*. (capitals for the title; the title of a whole work is often in italics)
</details>

### Practice Set 3 — Your own writing

Take three of your journal entries from your first sections. Fix every punctuation error using the subgoal checklist above. Count the fixes. Save before and after versions in your workbench (`english/punctuation-before-after.md`). This is the most valuable practice set in the stage, because they are *your* habits.

---

## Watch, practise, and write

*Companions, not replacements: the lessons above come first. Full list: [courses-and-videos.md](../../courses-and-videos.md#foundations-english).*

- **Watch:** Khan Academy Grammar: the punctuation unit. *Grammar and Punctuation* (UC Irvine, Coursera), the punctuation modules.
- **Practise:** Khan Academy punctuation exercises; then Practice Set 3 on your own writing.
- **Fun writes this stage** ([prompt bank](writing-prompts.md)): #40 CPU and RAM argue · #43 the apostrophe crime scene · #45 the terminal transcript · #46 commas change everything

---

## Self-check

1. **[R] Blank sheet:** the six comma rules with examples; the two jobs of the apostrophe; colon rule; semicolon's two jobs; when to use code format instead of quotes.
2. **Fix this paragraph** (10 errors):
   > First open the terminal, then type "cd projects." The projects folder which is in your home directory has three sub folders: notes code and docs. Its important to check the files permission's before you run the script, if the script cant run you will see an error.
3. **Explain [F]:** write a short paragraph explaining to a beginner why you should write `ls -la` in code format instead of in quotation marks.

<details>
<summary>Answers (Self-check 2)</summary>

*First, open the terminal. Then type `cd projects`. The `projects` folder, which is in your home directory, has three subfolders: `notes`, `code`, and `docs`. It's important to check the file's permissions before you run the script. If the script can't run, you will see an error.*

The 10 fixes: (1) comma after *First* · (2) comma splice after *terminal* → full stop · (3) command in code format, not quotes (and the period moved outside) · (4–5) commas around *which is in your home directory* (counts as two) · (6) *sub folders* → *subfolders* · (7) list commas: *notes, code, and docs* · (8) *Its* → *It's* · (9) *files permission's* → *file's permissions* · (10) comma splice after *script* → full stop; plus *cant* → *can't* and comma after *run* (Rule 3) — if you found these too, count them as bonus points.
</details>

## Done when

- [ ] Practice Sets 1–3 done; 80%+ on Sets 1–2, or redone with new examples.
- [ ] Self-check paragraph fixed with at least 10 corrections.
- [ ] Copywork diffs now include punctuation, and your punctuation-difference count is falling.
- [ ] [Machine Manual](projects/machine-manual/spec.md) complete, including the usability test.

**Next:** [E07 — Joining Ideas](E07-joining-ideas.md).
