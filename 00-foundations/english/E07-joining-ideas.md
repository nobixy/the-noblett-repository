---
title: "E07 — Joining Ideas"
id: "E07"
type: "lesson"
module: "00-foundations"
track: "english"
stage: "E07"
phase: "B"
order: 320
prerequisites: [E06]
---

# E07 — Joining Ideas

**In this stage you will:** learn to join ideas into longer sentences that show how they relate: *and*, *but*, *because*, *if*, *although*, *which*. You will fix run-on sentences and fragments for good, and learn parallel structure for lists and steps. You will start [Terminal Field Notes](projects/terminal-field-notes/spec.md).

**Before you start:** E06 done. You know the comma rules, especially Rules 2 and 3.

---

## Why this matters

Short sentences are clear. But a page of only short sentences hides the most important thing in technical writing: **how facts relate**.

> The disk was full. The program stopped. I deleted old logs. It worked.

Did the disk cause the stop? Did deleting logs fix it? The reader has to guess. Now:

> The program stopped **because** the disk was full. **After** I deleted old logs, it worked again.

The joining words carry the *logic*: cause, time, contrast, condition. This is the same logic you write in code with `if`, `else`, `and`, `or`, `while`. Engineers who write clear "because" and "unless" sentences are the ones whose explanations people trust.

---

## Part 1 — Clauses: the building blocks

A **clause** is a group of words with its own subject and verb.

- An **independent clause** can stand alone as a sentence: *the program stopped*.
- A **dependent clause** has a subject and verb but cannot stand alone; it starts with a word like *because, if, when, although, which*: *because the disk was full*.

You can think of the dependent clause as a function that needs to be called from somewhere: it doesn't run on its own.

**Four sentence types:**

| Type | Built from | Example |
| :-- | :-- | :-- |
| **Simple** | one independent clause | The program stopped. |
| **Compound** | two independent clauses, joined | The program stopped, and the fan went quiet. |
| **Complex** | one independent + one or more dependent | The program stopped because the disk was full. |
| **Compound-complex** | two+ independent + one+ dependent | The program stopped because the disk was full, so I deleted the old logs. |

Good writing mixes all four. Most of your sentences should be simple or complex; compound-complex sentences are useful but heavy.

---

## Part 2 — Joining equals: compound sentences

Use these when two ideas are equally important.

### With FANBOYS (and, but, or, so, yet, for, nor)

Comma + joining word (E06 Comma Rule 2):

| Word | Logic | Example |
| :-- | :-- | :-- |
| **and** | addition | The light turned green, **and** the download started. |
| **but** | contrast | The test passed, **but** it took ten minutes. |
| **or** | choice | You can use Wi-Fi, **or** you can plug in a cable. |
| **so** | result | The battery was low, **so** the laptop shut down. |
| **yet** | surprising contrast | The code looked right, **yet** it crashed. |

### With a semicolon

When the link is obvious: *The first test passed; the second failed.*

### With a linking adverb (however, therefore, also, instead, then)

These are **not** FANBOYS. They cannot join two sentences with just a comma. Use a full stop or a semicolon before them, and a comma after.
> ✗ The test passed, however it was slow.
> ✓ The test passed. However, it was slow.
> ✓ The test passed; however, it was slow.

| Word | Logic |
| :-- | :-- |
| however | contrast |
| therefore, as a result | result |
| also, in addition | addition |
| instead | replacement |
| then, next, finally | sequence |
| for example | example |

---

## Part 3 — Joining unequals: complex sentences

Use these when one idea is the main point and the other gives background: a reason, a time, a condition, a contrast.

### Subordinating words (the "dependent clause" starters)

| Logic | Words | Example |
| :-- | :-- | :-- |
| **cause** | because, since | The laptop shut down **because** the battery was empty. |
| **condition** | if, unless, as long as | **If** the light is red, unplug the cable. Don't unplug it **unless** the light is red. |
| **time** | when, while, before, after, until, as soon as | **When** the download finishes, restart. Wait **until** the light stops blinking. |
| **contrast** | although, even though, while, whereas | **Although** the test passed, the output looked wrong. |
| **purpose** | so that | Add a timeout **so that** the program never hangs. |

### Comma rule for complex sentences

- Dependent clause **first** → comma after it (E06 Rule 3):
  > **If the light is red,** unplug the cable.
- Dependent clause **second** → usually no comma:
  > Unplug the cable **if the light is red.**
  (Exception: *although/even though/whereas* usually take a comma either way, because they mark contrast.)

### Where to put the main idea

**The main idea goes in the independent clause.** Background goes in the dependent clause. Compare:

> Although the fix took two days, it doubled the speed. → *main point: it doubled the speed*
> Although it doubled the speed, the fix took two days. → *main point: it took two days*

Same facts, different message. Choose deliberately.

### Relative clauses: who, which, that

These attach information to a noun.
- **who** for people: *The engineer **who wrote this** has left.*
- **which** for things, extra information, with commas: *The server, **which is ten years old**, still works.*
- **that** for things, essential information, no commas: *The server **that hosts the website** is down.*

(Review E06 Rule 4 if the comma difference isn't automatic yet.)

### Code and English: the same logic

| English | Python |
| :-- | :-- |
| *If the file exists, open it. Otherwise, create it.* | `if exists(f): open(f)` / `else: create(f)` |
| *Wait until the light is green.* | `while not light_is_green(): wait()` |
| *Retry unless you have tried three times.* | `if tries < 3: retry()` |
| *Open the file and read the first line.* | `f = open(name); line = f.readline()` |

**Code comments should explain *why*, and "why" is a *because* sentence.**
> ✗ `# add 1 to i` (says what the code says)
> ✓ `# Start at 1 because line 0 is the header.`

---

## Part 4 — Run-ons and fragments

### Run-on sentences

A **run-on** is two or more independent clauses jammed together without proper joining. Two kinds:
- **Fused sentence** (no punctuation): *The test failed I don't know why.*
- **Comma splice** (only a comma): *The test failed, I don't know why.*

**Four fixes** (pick by meaning):
1. Full stop: *The test failed. I don't know why.*
2. Comma + FANBOYS: *The test failed, and I don't know why.*
3. Semicolon: *The test failed; I don't know why.*
4. Make one clause dependent, *if* there is a real relationship: *The test failed, so I added more logging* → ***Because** the test failed, I added more logging.*

**Fix 4 only works when there is a real logical relationship.** "The test failed. I don't know why." has no cause or condition linking the halves, so fixes 1–3 are the right choices there. Don't force a *because* that isn't true.

**Long chains with *and* are also a kind of run-on:**
> I opened the case and I took out the card and I cleaned it and I put it back and it worked.
> → I opened the case, took out the card, and cleaned it. After I put it back, it worked.

### Fragments

A **fragment** is a piece of a sentence punctuated as if it were whole. The most common kind is a lone dependent clause:
> The program stopped. **Because the disk was full.** ✗
> → The program stopped because the disk was full. ✓

Others: a phrase with no verb (*The light on the router.*), or a verb with no subject (*Restarted it twice.*).

**Fix:** attach it to the sentence before or after, or add the missing subject or verb.

---

## Part 5 — Parallel structure

When you list things, or write steps, **give every item the same grammatical shape**.

> ✗ The tool lets you **copy** files, **renaming** them, and **the deletion** of old ones.
> ✓ The tool lets you **copy**, **rename**, and **delete** files.

> ✗ Steps: 1. Open the terminal. 2. The folder should be changed. 3. Running the script.
> ✓ Steps: 1. Open the terminal. 2. Change to the project folder. 3. Run the script.

Parallel structure is easier to read because the reader learns the shape from the first item and reuses it. It's like a list in code where every element has the same type.

**Paired words must be parallel too:** *either… or, both… and, not only… but also*.
> ✗ You can **either** use Wi-Fi **or** plugging in a cable.
> ✓ You can **either** use Wi-Fi **or** plug in a cable.

---

## Part 6 — Sentence combining

**Sentence combining** is a well-tested way to build writing skill: you take short sentences and join them into one better sentence, choosing the joining words yourself. There are many good answers. The point is to choose the relationship deliberately.

Example:
> The laptop is old. It runs Linux. It runs fast.
> → The old laptop runs Linux fast.
> → Although the laptop is old, it runs Linux fast. *(emphasises the surprise)*

Do 5 per session in this stage (Practice Set 2 has a starter set; then make your own from your journal).

---

## Part 7 — Practice routine (3 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Session 1: clauses and the four sentence types · Session 2: compound sentences (FANBOYS, semicolons) · Session 3: linking adverbs · Sessions 4–5: complex sentences, Practice Set 1 |
| 2 | Session 1: relative clauses · Session 2: run-ons · Session 3: fragments · Session 4: parallel structure · Session 5: Practice Set 2 |
| 3 | Sessions 1–2: Practice Set 3 (your own writing) · Sessions 3–4: Field Notes Milestone 1 · Session 5: self-check |

**Every session:**
- **Warm-up [R]:** write the logic table (cause / condition / time / contrast / purpose) with two joining words each, from memory.
- **Combine 5 [S]:** five sentence-combining sets. For each, first label the relationship (*cause? contrast? time?*), then choose the joining word.
- **Spelling** and **copywork [C]** (Level 2; move to **Level 3** when ready). In the diff, look at how the author joins ideas. Count their sentence types.

**Study protocols:**
- **[W]** For every joining word you use, ask: is that the real relationship? "Because" claims a cause. Is it really the cause, or did it just happen at the same time? (This question will save you in debugging too: "it broke after the update" is not the same as "it broke because of the update.")
- **[F]** Teach the difference between *however* and *but* to a friend. Explain why *however* can't join two sentences with only a comma.
- **[D]** Combining sentences is creative. If one won't come right, leave it overnight; it usually solves itself.

---

## Practice sets

### Practice Set 1 — Join with the right logic (10 items)

Join each pair using the relationship in brackets. Punctuate correctly.

1. The battery was empty. The laptop shut down. *(cause)*
2. The light is red. Unplug the cable. *(condition)*
3. The code looked correct. It crashed. *(contrast)*
4. The download finishes. Restart the computer. *(time)*
5. Add a timeout. The program never hangs. *(purpose)*
6. The first test passed. The second test failed. *(contrast, using *however*)*
7. You can use Wi-Fi. You can plug in a cable. *(choice)*
8. The server is ten years old. It still works. *(relative clause with *which*)*
9. The engineer wrote this code. She has left the company. *(relative clause with *who*)*
10. The disk was full. I deleted old logs. *(result, using *so*)*

<details>
<summary>Sample answers (Set 1)</summary>

1. The laptop shut down because the battery was empty. *(or)* Because the battery was empty, the laptop shut down.
2. If the light is red, unplug the cable.
3. Although the code looked correct, it crashed. *(or)* The code looked correct, but it crashed.
4. When the download finishes, restart the computer.
5. Add a timeout so that the program never hangs.
6. The first test passed. However, the second test failed. *(or with a semicolon)*
7. You can use Wi-Fi, or you can plug in a cable. *(or)* You can use Wi-Fi or plug in a cable.
8. The server, which is ten years old, still works.
9. The engineer who wrote this code has left the company.
10. The disk was full, so I deleted old logs.
</details>

### Practice Set 2 — Fix and combine (10 items)

Fix each run-on, fragment, or non-parallel structure. Some need combining.

1. I restarted the router it still didn't work.
2. The fan is loud, it needs cleaning.
3. Because the cable was loose.
4. The tool can resize images, converting them, and the compression of files.
5. Plugged in the charger and waited.
6. The test passed, however it was slow.
7. I opened the case and I removed the fan and I cleaned it and I put it back.
8. You should either restart the service or rebooting the machine.
9. The light on the switch. It blinks twice when it starts.
10. Although the update was small. It fixed three bugs.

<details>
<summary>Sample answers (Set 2)</summary>

1. I restarted the router, but it still didn't work.
2. The fan is loud. It needs cleaning. *(or)* The fan is loud because it needs cleaning. *(only if that's the real cause)*
3. Attach it: *The connection dropped because the cable was loose.*
4. The tool can resize, convert, and compress images.
5. I plugged in the charger and waited.
6. The test passed; however, it was slow. *(or)* The test passed. However, it was slow.
7. I opened the case, removed the fan, cleaned it, and put it back.
8. You should either restart the service or reboot the machine.
9. The light on the switch blinks twice when it starts.
10. Although the update was small, it fixed three bugs.
</details>

### Practice Set 3 — Your own writing

Take a page from your journal or field notes. Find:
- every run-on and fragment (fix them);
- every place where two short sentences have a hidden relationship (cause, contrast, time) — join them with the right word;
- every list — make it parallel.

Save before and after (`english/joining-before-after.md`). Count changes.

---

## Watch, practise, and write

*Companions, not replacements: the lessons above come first. Full list: [courses-and-videos.md](../../courses-and-videos.md#foundations-english).*

- **Watch:** Khan Academy Grammar: 'Syntax: conventions of standard English' (run-ons, fragments, parallel structure). *Grammar and Punctuation* (Coursera), the sentence modules.
- **Practise:** Sentence combining: 5 per session from your own journal.
- **Fun writes this stage** ([prompt bank](writing-prompts.md)): #50 excuses a printer gives · #51 robot butler rules · #56 run-on rescue · #58 code comments that explain why

---

## Self-check

1. **[R] Blank sheet:** independent vs dependent clauses; the four sentence types; FANBOYS vs linking adverbs and their punctuation; the logic table; four fixes for a run-on; what parallel structure is.
2. **Rewrite this paragraph** so the logic is clear, using at least one cause, one contrast, one condition, and one time word. Fix all run-ons and fragments.
   > The Wi-Fi kept dropping. I moved the router. It still dropped. I checked the logs. There were many errors at night. My neighbor's network uses the same channel. I changed the channel. It works now. Mostly. It drops when the microwave runs.
3. **Code comments:** write three "why" comments (using *because*, *so that*, or *unless*) for any three lines in your Module 01 code.

<details>
<summary>Sample answer (Self-check 2)</summary>

*The Wi-Fi kept dropping. Although I moved the router, it still dropped. When I checked the logs, I saw many errors at night, because my neighbor's network uses the same channel. After I changed the channel, the connection became mostly stable. However, it still drops when the microwave runs. If that becomes a problem, I will switch to the 5 GHz band.*

(Your version will differ. Check that each joining word states a relationship that is actually true.)
</details>

## Done when

- [ ] Practice Sets 1–3 done and checked.
- [ ] Self-check paragraph rewritten with all four logic types.
- [ ] Your code comments explain *why* (check your Module 01 code).
- [ ] [Terminal Field Notes](projects/terminal-field-notes/spec.md) Milestone 1 done.

**Next:** [E08 — Paragraphs and Clarity](E08-paragraphs-and-clarity.md).
