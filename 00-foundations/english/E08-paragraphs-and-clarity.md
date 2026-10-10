---
title: "E08 — Paragraphs and Clarity"
stage: E08
track: english
hours: 25
weeks: 4
---

# E08 — Paragraphs and Clarity

**In this stage you will:** build paragraphs with one clear point, order sentences so each one connects to the last, apply the clarity rules (real actors as subjects, real actions as verbs), cut wasted words, and revise your own drafts with a checklist. You will start speaking your explanations out loud. Projects: finish [Terminal Field Notes](projects/terminal-field-notes/spec.md); start [Explain-a-System](projects/explain-a-system/spec.md).

**Time:** about 25 hours over 4 weeks.

**Before you start:** E07 done. You can join ideas with the right logic words and fix run-ons and fragments.

---

## Why this matters

Sentences are bricks. Paragraphs are walls. A reader can follow a wall of good bricks only if the bricks are laid in an order that makes sense.

Most "bad writing" in engineering is not bad grammar. It is **unclear writing**: paragraphs with no point, sentences where you can't tell who did what, and too many words. This stage is about clarity, which is the most valuable writing skill an engineer can have.

The rules here come mostly from Joseph Williams, *Style: Lessons in Clarity and Grace* (a companion book if you want more; not required). They are not about taste. They are about how readers actually process sentences: readers expect the actor to be the subject, the action to be the verb, and familiar information to come before new information. When you meet those expectations, reading feels easy.

---

## Part 1 — The paragraph

A **paragraph** is a group of sentences about **one** idea.

**Structure:**
1. **Topic sentence** (first, usually): states the paragraph's point.
2. **Support** (2–5 sentences): explanation, example, evidence, steps, or reasons.
3. **Closing** (optional): a consequence or a link to the next paragraph.

> **The cache makes the second load of a page much faster.** *(topic)* The first time you visit a site, your browser downloads every image and file. It saves copies on your disk. On the next visit, it uses those copies instead of downloading again. *(support)* That's why a site you visit every day appears almost instantly. *(closing)*

### Tests for a good paragraph

- **The point test:** cover everything except the first sentence. Does it tell you what the paragraph is about? If not, write a topic sentence.
- **The one-idea test:** does every sentence support the topic sentence? Move any that don't to their own paragraph, or delete them.
- **The skim test:** read only the first sentence of every paragraph in a document. You should get the whole argument. (Busy readers — your future teammates — read exactly this way.)

**Paragraph length:** in technical writing, 2–6 sentences. Long paragraphs on screens are hard to read.

> **Code connection:** one idea per paragraph is like one job per function. A function called `parse_and_send_and_log` should be three functions. A paragraph that explains the cache, then the network, then the screen should be three paragraphs.

---

## Part 2 — Old before new: making sentences connect

**Readers understand a sentence best when it starts with something they already know and ends with something new.** Then the new thing at the end becomes the known thing that starts the next sentence. The sentences link like a chain.

> ✗ *Unclear chain:* Your browser saves copies of files on the disk. A cache is the place where these copies are stored. Faster loading is the result of the cache.
> ✓ *Clear chain:* Your browser saves copies of files on the disk. **These copies** are kept in a place called **the cache**. **The cache** makes pages load faster.

Each bold phrase repeats or refers to something from the end of the previous sentence. That is the **old-before-new** principle.

**Practical rule:** start each sentence with a word or idea the reader just saw. Put the new, important, or complicated part at the **end** of the sentence. The end of a sentence is the stress position: it's where the reader's attention lands.

---

## Part 3 — The clarity rules

### Rule 1 — Make the main actors the subjects

The **actor** is whoever or whatever *does* the action. Put it in the subject.

> ✗ *A decision was made by the team to replace the server.* (subject: "a decision")
> ✓ *The team decided to replace the server.* (subject: the actor)

### Rule 2 — Put the main actions in verbs

Many unclear sentences hide their action inside a noun. These hidden-verb nouns are called **nominalizations**: *decide → decision, fail → failure, analyse → analysis, install → installation, connect → connection*.

> ✗ *The installation of the update caused a failure of the network connection.*
> ✓ *When we installed the update, the network stopped connecting.*

| Hidden action (noun) | Real action (verb) |
| :-- | :-- |
| make a decision | decide |
| perform an analysis | analyse |
| carry out an investigation | investigate |
| give an explanation | explain |
| there was a failure of the disk | the disk failed |
| the reduction of memory use | reduce memory use |
| provide support for | support |

Nominalizations are sometimes right (*"Installation takes five minutes"* is fine as a heading-like statement). But when a paragraph feels heavy, look for them first.

**Subgoal labels [S] for clarifying any sentence:**
1. Find the actors (who or what does things?).
2. Find the actions (what do they do? look inside nouns).
3. Make the actors subjects and the actions verbs.
4. Put old information first and new information last.

### Rule 3 — Get to the verb quickly

Readers hold the subject in their head until they reach the verb. A long gap is tiring.

> ✗ *The script that we wrote last week to check every file in the backup folder for errors and send a report **fails**.*
> ✓ *The script **fails**. We wrote it last week to check the backup folder for errors and send a report.*

### Rule 4 — Prefer the positive

> ✗ *Do not forget to not unplug it.* ✓ *Keep it plugged in.*
> ✗ *The test did not pass.* ✓ *The test failed.*

---

## Part 4 — Cutting words

Every unneeded word costs the reader attention. Cut:

| Cut | Write |
| :-- | :-- |
| in order to | to |
| due to the fact that | because |
| at this point in time | now |
| in the event that | if |
| has the ability to | can |
| is able to | can |
| it is important to note that | (delete; just say it) |
| basically, really, very, actually, just, quite | (usually delete) |
| the reason is because | because |
| each and every | each / every |
| a total of 5 | 5 |
| past history / future plans / end result | history / plans / result |

**Also cut:**
- **Throat-clearing** at the start: "*In this paragraph I am going to explain…*" → just explain.
- **Saying it twice:** "*The program is slow and takes a long time.*"
- **Hedging everything:** "*It might possibly perhaps be the cable.*" → "*It is probably the cable.*" (One hedge is honest; three are noise.)

**Don't cut** words that carry meaning: units, conditions, the actor, the reason. Short is good; vague is not.

---

## Part 5 — Revising: the edit checklist

Nobody writes clearly in one draft. Clear writers **revise**. Use this order, from big to small (fixing commas in a paragraph you then delete is wasted time):

1. **Cool off [D].** Wait at least a few hours, ideally overnight. You can't see your own errors while the draft is fresh.
2. **Structure:** read only the first sentence of each paragraph. Does the argument make sense? Reorder or add topic sentences.
3. **Paragraphs:** one idea each? Old before new?
4. **Sentences:** actors as subjects? Actions as verbs? Verb close to subject?
5. **Words:** cut the table in Part 4.
6. **Read it aloud.** Every place you stumble is a problem. This is the single most effective editing trick.
7. **Spelling and punctuation:** last. Use your error log's top tags as a checklist. Then run a spell checker.

Write the checklist on a card and keep it by your desk.

---

## Part 6 — Speaking: the spoken explanation

From this stage on, part of your practice is out loud. Engineers explain things in meetings, code reviews, interviews, and demos. Spoken explanation follows the same rules as writing, with three additions:

1. **Say the point first.** "*The second load is faster because of the cache.*" Then explain.
2. **Signpost.** Tell the listener where you are: "*There are three parts. First… Second… Finally…*" A reader can look back; a listener can't.
3. **One example beats three definitions.** Listeners remember stories and examples.

**The weekly recording:** once a week, record a 2–3 minute explanation of something you built or learned (phone voice memo is fine). Listen back once. Count filler words (*um, like, basically, you know*). Note one thing to improve. Keep the count in your log. It falls quickly with practice.

---

## Part 7 — Practice routine (4 weeks)

| Week | Focus |
| :-- | :-- |
| 1 | Mon–Tue: paragraph structure; write 3 paragraphs about your Module 01 project · Wed–Thu: old before new · Fri: Practice Set 1 |
| 2 | Mon–Tue: clarity Rules 1–2 · Wed: Rules 3–4 · Thu: cutting words · Fri: Practice Set 2 |
| 3 | Mon–Wed: revise three of your own pieces using the checklist (Practice Set 3) · Thu–Fri: Field Notes Milestone 2 |
| 4 | Mon–Wed: Explain-a-System, first explainer (write + record) · Thu: weekly recording · Fri: self-check |

**Daily:**
- **Warm-up [R]:** write the clarity rules and the revision checklist from memory.
- **Write one paragraph** (5–10 min) about something you did or learned today. Next day, revise yesterday's paragraph with the checklist before writing the new one.
- **Spelling (10 min)** + **copywork [C]**: **Level 3** (Paul Graham, Feynman Lectures, Joel Spolsky). In the diff, now notice *structure*: where did the author put the topic sentence? How do the sentences chain?

**Study protocols:**
- **[S]** The four clarity labels (Part 3) on every sentence you revise.
- **[W]** Why does old-before-new work? Answer in your own words before reading the explanation again. Then ask: does the same principle apply to code? (Yes: a function that uses names defined just above it is easier to read than one that uses names defined far away.)
- **[F]** Your weekly recording *is* a spoken Feynman pass.
- **[D]** The revision checklist starts with a cooling-off break. Respect it.
- **[T]** The first Explain-a-System piece is read by someone else. Their confusion is your feedback.

---

## Practice sets

### Practice Set 1 — Paragraph surgery

**A.** This paragraph has no topic sentence and one sentence that doesn't belong. Write a topic sentence and remove the outsider.

> First the computer checks that the hardware works. Then it loads a small program from a chip on the motherboard. That program finds the operating system on the disk and starts it. My computer has a blue case. Finally the operating system starts the login screen.

**B.** Reorder these sentences so they follow old-before-new.

> (a) The router sends each packet toward its destination. (b) A message you send is broken into small pieces called packets. (c) Your computer gives these packets to the router. (d) At the destination, the packets are put back together into the message.

<details>
<summary>Answers (Set 1)</summary>

**A.** Topic sentence, for example: *When you press the power button, your computer starts up in a few steps.* Remove: *My computer has a blue case.*

**B.** b → c → a → d. Each sentence starts with what the last one ended with: *message → packets → packets → router/packets → destination.*
</details>

### Practice Set 2 — Clarity rewrites (8 sentences)

Rewrite each one with real actors as subjects and real actions as verbs. Cut extra words.

1. An investigation of the crash was carried out by the team.
2. There was a failure of the hard disk in the server.
3. The reduction of memory usage is the goal of this change.
4. In order to make an improvement to the speed, a decision was made to add a cache.
5. It is important to note that the installation of the update requires a restart.
6. The program has the ability to perform the conversion of images.
7. Due to the fact that the battery was low, a shutdown of the laptop occurred.
8. At this point in time, the testing of the new version is basically being done by Sam.

<details>
<summary>Sample answers (Set 2)</summary>

1. The team investigated the crash.
2. The server's hard disk failed.
3. This change reduces memory use.
4. We added a cache to make it faster. *(or)* To speed it up, we decided to add a cache.
5. The update needs a restart after you install it.
6. The program can convert images.
7. The laptop shut down because the battery was low.
8. Sam is testing the new version now.
</details>

### Practice Set 3 — Your own writing

Take three pieces you wrote in E05–E07 (journal entries, field notes, the machine manual). Revise each with the full checklist. Save before and after (`english/clarity-before-after.md`) and count: words before, words after, nominalizations removed, passive sentences changed to active (when the actor mattered).

---

## Watch, practise, and write

*Companions, not replacements: the lessons above come first. Full list: [courses-and-videos.md](../../courses-and-videos.md#foundations-english).*

- **Watch:** *Writing in the Sciences* (Stanford, Coursera): the first weeks on cutting clutter and active voice. *Good with Words: Writing and Editing* (University of Michigan, Coursera).
- **Practise:** Hemingway Editor (free, hemingwayapp.com) *after* you've revised by hand: see which long sentences you missed.
- **Fun writes this stage** ([prompt bank](writing-prompts.md)): #60 explain your favourite game · #62 old-before-new chain · #63 the fog machine · #67 before and after

---

## Self-check

1. **[R] Blank sheet (10 min):** paragraph structure; the three paragraph tests; old before new; the four clarity rules; ten wordy phrases and their short forms; the seven-step revision checklist.
2. **Rewrite** this paragraph (about 90 words) into a clear paragraph of about 50 words:
   > It is important to note that there are a number of different reasons why the performance of a computer can basically become slower over a period of time. The installation of too many programs that start automatically is one reason. Another reason is the fact that the disk can become full, which causes a reduction in the ability of the system to perform the creation of temporary files. In order to make an improvement, a removal of unneeded programs should be performed by the user.
3. **Spoken [F] [T]:** a 3-minute recording explaining how your Module 01 project works. Count filler words.

<details>
<summary>Sample answer (Self-check 2)</summary>

*A computer can slow down over time for two common reasons. First, too many programs start automatically. Second, the disk can fill up, so the system cannot create the temporary files it needs. To speed it up, remove programs you don't need.* (about 50 words)
</details>

## Done when

- [ ] Practice Sets 1–3 done.
- [ ] Self-check rewrite is under 60 words and keeps every real fact.
- [ ] Four weekly recordings made; filler words counted each time.
- [ ] [Terminal Field Notes](projects/terminal-field-notes/spec.md) complete.
- [ ] [Explain-a-System](projects/explain-a-system/spec.md) explainer 1 done.

**Next:** [E09 — Technical Description and Instructions](E09-technical-description-and-instructions.md).
