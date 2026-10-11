---
title: "E05 — The Simple Sentence and Verbs"
id: "E05"
type: "lesson"
module: "00-foundations"
track: "english"
stage: "E05"
phase: "A"
order: 90
prerequisites: [E04]
---

# E05 — The Simple Sentence and Verbs

**In this stage you will:** learn what makes a complete sentence, the five basic sentence patterns, how verbs change for time (tense), how verbs agree with their subjects, the common irregular verbs, active vs passive voice, and the imperative form used in instructions and commit messages.

**Before you start:** E04 done. You can find the verb and the nouns in a sentence.

---

## Why this matters

A sentence is a small machine with a fixed core: **someone or something** (the subject) **does or is something** (the verb). Everything else is attached to that core. If you can find and build the core, you can write a correct sentence every time, and you can fix any sentence that feels wrong by checking its core.

For technical writing, the core is everything. "The kernel sends the process a signal" tells you exactly **who** acts (the kernel), **what** it does (sends), and **to what** (a signal, to the process). Vague technical writing almost always has a weak core: no clear actor, or a weak verb.

Verbs also carry **time**. "The test fails" (always, right now), "the test failed" (once, in the past), and "the test has failed" (it failed, and that matters now) say different things. Bug reports depend on getting this right.

---

## Part 1 — What makes a sentence complete

A **complete sentence** has:
1. a **subject** — who or what the sentence is about;
2. a **verb** — what the subject does or is;
3. a **complete thought** — it makes sense on its own.

> **The light** (subject) **blinks** (verb). ✓
> **The red light on the router** (subject) **blinks** (verb) **twice** (adverb). ✓
> Blinks twice. ✗ (no subject: what blinks?)
> The red light on the router. ✗ (no verb: what about it?)
> Because the light blinks. ✗ (not a complete thought: because… what? — you'll fix these in E07)

A group of words that is missing one of these is a **fragment**. Fragments are fine in notes and slides. In reports and docs, use full sentences.

**Commands are the exception.** "Restart the router." has no written subject; the subject is "you," understood. This is called the **imperative**, and it's complete.

### Finding the core: subgoal labels [S]

1. **Find the verb.** Ask: what happens, or what is? (If there are several verbs, find the main one.)
2. **Find the subject.** Ask: *who or what* does that? It usually comes before the verb.
3. **Find what's left of the core:** does the verb act *on* something (an object)? Or does it describe the subject (a complement)?
4. **Everything else is detail** attached to the core: adjectives, adverbs, prepositional phrases.

Example: *"After the update, the old laptop in the kitchen finally connected to the network."*
1. Verb: *connected*.
2. Who connected? *the old laptop* (the subject is *laptop*, with *the old* describing it, and *in the kitchen* telling which one).
3. Connected to what? *to the network* (a prepositional phrase).
4. Details: *After the update* (when), *finally* (how).
**Core:** *The laptop connected.*

**Trap:** the subject is never inside a prepositional phrase. In "*The list of errors* is long," the subject is *list*, not *errors*. That matters for agreement (Part 4).

---

## Part 2 — The five sentence patterns

Almost every English sentence is built on one of five patterns. Learn to see them.

| # | Pattern | Example | Code of it |
| :-- | :-- | :-- | :-- |
| 1 | **Subject + Verb** | The program **crashed**. | S V |
| 2 | **Subject + Verb + Object** | The program **deleted** the file. | S V O |
| 3 | **Subject + Linking verb + Complement** | The file **is** empty. / The file **is** a log. | S LV C |
| 4 | **Subject + Verb + Indirect object + Object** | The server **sent** the client a reply. | S V IO O |
| 5 | **Subject + Verb + Object + Object complement** | The error **made** the screen red. / We **named** the file *notes.txt*. | S V O OC |

- An **object** receives the action: *deleted* **what**? → *the file*.
- An **indirect object** is who/what the action is done *for* or *to*: sent **to whom**? → *the client*. You can usually rewrite it with *to*: "The server sent a reply **to the client**."
- A **complement** describes or renames the subject after a linking verb (*is, are, was, seems, becomes*).
- An **object complement** describes or renames the object: made the screen **red**.

> **Why learn patterns? [W]** Because each pattern is a different kind of claim. Pattern 1: something happened. Pattern 2: something acted on something. Pattern 3: something has a property. In technical writing, choosing the pattern is choosing what you are claiming. "The file is corrupt" (3: a property) and "The update corrupted the file" (2: a cause) are different claims. The second one is more useful in a bug report, because it names the cause.

---

## Part 3 — Verb tenses: verbs carry time

### The forms of a verb

Every verb has a few forms. For a **regular** verb like *work*:

| Form | Example | Used for |
| :-- | :-- | :-- |
| base | work | *I work, to work, will work, can work* |
| -s form | works | *he/she/it works* |
| past | worked | *I worked yesterday* |
| past participle | worked | *I have worked, it was worked* |
| -ing form | working | *I am working* |

Regular verbs add **-ed** for both the past and past participle, using the E02 rules (*stopped, tried, used*).

### The six tenses you need

| Tense | Form | Example | Means |
| :-- | :-- | :-- | :-- |
| **Simple present** | base / -s | The script **runs** every hour. | always, habitually, or a general truth |
| **Simple past** | past | The script **ran** at 3 p.m. | finished, at a time in the past |
| **Simple future** | will + base | The script **will run** at 3 p.m. | later |
| **Present continuous** | am/is/are + -ing | The script **is running** now. | in progress right now |
| **Present perfect** | has/have + past participle | The script **has run** 40 times. | happened before now, and matters now |
| **Past continuous** | was/were + -ing | The script **was running** when the power failed. | in progress at a past moment |

**Technical writing uses mostly the simple present.** Documentation describes what a system *does* (always): "The `ls` command **lists** files." Bug reports and lab reports use the **simple past** for what you did and saw: "I **ran** the test. It **failed**." Use the **present perfect** for something that happened and is still relevant: "This bug **has appeared** in three versions."

**Keep tense consistent.** Do not switch tense in the middle of a description unless the time actually changes.
> ✗ I opened the file and then I click Save and it crashed.
> ✓ I opened the file, clicked Save, and the program crashed.

### Irregular verbs

About 150 common verbs don't use *-ed*. You already know most when speaking; spelling them is the issue. Learn this table in chunks of 10 (flashcards).

| Base | Past | Past participle | | Base | Past | Past participle |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| be | was / were | been | | lead | led | led |
| begin | began | begun | | leave | left | left |
| break | broke | broken | | lose | lost | lost |
| bring | brought | brought | | make | made | made |
| build | built | built | | mean | meant | meant |
| buy | bought | bought | | pay | paid | paid |
| catch | caught | caught | | put | put | put |
| choose | chose | chosen | | read | read | read |
| come | came | come | | run | ran | run |
| do | did | done | | say | said | said |
| draw | drew | drawn | | see | saw | seen |
| drive | drove | driven | | seek | sought | sought |
| eat | ate | eaten | | send | sent | sent |
| fall | fell | fallen | | set | set | set |
| feel | felt | felt | | shut | shut | shut |
| find | found | found | | sit | sat | sat |
| fly | flew | flown | | speak | spoke | spoken |
| forget | forgot | forgotten | | spend | spent | spent |
| get | got | got / gotten (US) | | split | split | split |
| give | gave | given | | stand | stood | stood |
| go | went | gone | | take | took | taken |
| have | had | had | | teach | taught | taught |
| hide | hid | hidden | | tell | told | told |
| hold | held | held | | think | thought | thought |
| keep | kept | kept | | throw | threw | thrown |
| know | knew | known | | understand | understood | understood |
| lay | laid | laid | | wake | woke | woken |
| lie (rest) | lay | lain | | wear | wore | worn |
| light | lit | lit | | win | won | won |
| | | | | write | wrote | written |

**Common errors:** *I have wrote* ✗ → *I have **written*** ✓ · *it has broke* ✗ → *it has **broken*** ✓ · *I seen it* ✗ → *I **saw** it* or *I **have seen** it* ✓ · *I brung* ✗ → *I **brought*** ✓.

**Spelling notes:** *write → wrote → written* (double t: *writ-ten*, short i; E02 Rule 1). *Bought* (buy) vs *brought* (bring): *br*ing → *br*ought. *Thought* (think) vs *taught* (teach).

---

## Part 4 — Agreement: the verb matches the subject

In the present tense, the verb changes for **he / she / it** (and any single thing):

| Subject | Verb |
| :-- | :-- |
| I / you / we / they / the files | **run**, **are**, **have**, **do** |
| he / she / it / the file | **runs**, **is**, **has**, **does** |

**Rule:** singular subject → singular verb (*-s* form). Plural subject → plural verb (base form).

**The traps:**
1. **A phrase between subject and verb.** Find the real subject (Part 1).
   > The list of errors **is** long. (*list* is singular) ✓ · The list of errors are long ✗
   > The cables behind the desk **are** loose. (*cables*) ✓
2. **"There is / there are."** The subject comes *after* the verb.
   > There **is** one error. There **are** three errors.
3. **"Each" and "every"** are singular.
   > Each test **runs** in a sandbox. Every file **has** a name.
4. **"Data."** Modern technical English usually treats *data* as singular ("the data **is** saved"). Both are accepted; pick one and be consistent.
5. **Joined with "and"** → plural. *The keyboard and the mouse **are** wireless.*
   **Joined with "or"** → match the nearer one. *The keyboard or the mice **are** broken.*

---

## Part 5 — Active and passive voice

**Active:** the subject *does* the action. *The script **deleted** the file.*
**Passive:** the subject *receives* the action. *The file **was deleted** (by the script).*

The passive is built with **be + past participle**: *was deleted, is stored, has been sent, will be compiled*.

**When to use which:**
- **Prefer active** when you know who did it. It is shorter and clearer, and it names the cause. In a bug report, "the update deleted my settings" is more useful than "my settings were deleted."
- **Use passive** when the actor is unknown, unimportant, or obvious: *"The packet **is dropped** if the checksum is wrong."* (Who drops it? The receiver, obviously.) Specs and docs use passive often, and that's fine.

**The danger:** passive lets you hide the actor. "Mistakes were made." By whom? In technical writing, a hidden actor often hides the actual cause of the problem. When you write a passive sentence, ask: *should the reader know who or what did this?* If yes, make it active.

---

## Part 6 — The imperative: instructions and commit messages

The **imperative** is the command form: the base verb, no subject.
> **Open** the terminal. **Type** `ls`. **Press** Enter.

You will write imperatives constantly:
- **Instructions:** "Install Python. Clone the repository. Run `make test`."
- **Git commit messages:** the convention is a short imperative line that completes the sentence *"If applied, this commit will…"*:
  > ✓ `Fix crash when the input file is empty`
  > ✓ `Add retry limit to the downloader`
  > ✗ `fixed stuff` · ✗ `Fixing the crash` · ✗ `crash fix maybe`

Start every commit message you write from now on with a capitalised imperative verb. That is real practice, every time you commit.

---

## Part 7 — Practice routine (3 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Session 1: complete sentences and fragments · Session 2: finding the core · Sessions 3–4: the five patterns · Session 5: Practice Set 1 |
| 2 | Session 1: verb forms and the six tenses · Sessions 2–3: irregular verbs (in chunks of 10, flashcards) · Session 4: agreement · Session 5: Practice Set 2 |
| 3 | Session 1: active and passive · Session 2: imperatives and commit messages · Session 3: Practice Set 3 · Session 4: Machine Manual Milestone 2 · Session 5: self-check |

**Every session:**
- **Warm-up [R]:** write the five patterns from memory with your own example of each.
- **Sentences of the session:** write 5 sentences about something you did recently. Then label each one's core (S, V, O) and its pattern number.
- **Spelling** + **copywork [C]** (Level 2). In the diff, check every verb's tense and agreement in your rebuild.

**Study protocols:**
- **[S]** Use the four "finding the core" labels on every sentence you analyse until you can do it without the list.
- **[W]** For every agreement trap above, answer: *what would a reader misunderstand if the verb didn't agree?* (Often: nothing, but they would trust you less. Sometimes: which thing you mean.)
- **[F]** Explain active vs passive to a friend using your own example from work. Then explain when passive is the *right* choice.
- **[I]** Practice Set 2 mixes tense, irregular verbs and agreement on purpose.

---

## Practice sets

### Practice Set 1 — Core and pattern (10 sentences)

For each sentence: (a) is it complete or a fragment? (b) if complete, write the core (subject + verb + object/complement) and the pattern number (1–5).

1. The router restarted.
2. The fan on the old laptop makes a loud noise.
3. Plugged in the cable.
4. The screen is too dark.
5. My friend gave me an old monitor.
6. The update made the system slow.
7. Because the disk was full.
8. Restart the computer.
9. The light on the front panel.
10. The test suite became the most important part of the project.

<details>
<summary>Answers (Set 1)</summary>

1. Complete · *router restarted* · Pattern 1
2. Complete · *fan makes noise* · Pattern 2
3. Fragment (no subject; who plugged it in?) — *I plugged in the cable.* would be Pattern 2
4. Complete · *screen is dark* · Pattern 3
5. Complete · *friend gave me monitor* · Pattern 4 (*me* = indirect object)
6. Complete · *update made system slow* · Pattern 5 (*slow* describes *system*)
7. Fragment (not a complete thought) — fix in E07: *The program stopped because the disk was full.*
8. Complete (imperative; subject *you* understood) · *(you) restart computer* · Pattern 2
9. Fragment (no verb)
10. Complete · *test suite became part* · Pattern 3
</details>

### Practice Set 2 — Verbs (15 items, mixed [I])

Choose or write the correct form.

1. Yesterday I (write) ______ the first version.
2. I have (write) ______ three versions so far.
3. The list of open bugs (is / are) ______ getting shorter.
4. There (is / are) ______ two cables missing.
5. Each test (take / takes) ______ about a second.
6. She has (break) ______ the build again.
7. We (buy / bought / brought) ______ a new router last week.
8. Right now the computer (update) ______ itself. (present continuous)
9. The script (run) ______ every night at midnight. (general truth)
10. The keyboard and the mouse (need / needs) ______ new batteries.
11. I (see) ______ the error twice yesterday.
12. He (teach / taught / thought) ______ me how to solder last year.
13. The server (send) ______ 400 requests since this morning. (present perfect)
14. The program (lie / lay) ______ unused for years. (past)
15. The power failed while I (save) ______ the file. (past continuous)

<details>
<summary>Answers (Set 2)</summary>

1. wrote · 2. written · 3. is (*list*) · 4. are (*two cables*) · 5. takes · 6. broken · 7. bought · 8. is updating · 9. runs · 10. need · 11. saw · 12. taught · 13. has sent · 14. lay (*lie* = rest; its past is *lay*. Yes, this one is strange; it's on the flashcard list for a reason.) · 15. was saving
</details>

### Practice Set 3 — Voice and imperatives (10 items)

**A.** Rewrite in the active voice. Invent a sensible actor if none is given.
1. The file was deleted by the cleanup script.
2. The settings were changed.
3. A new cable was bought by my roommate.
4. The bug was found during testing.
5. The password was reset by the admin yesterday.

**B.** Rewrite each as a good commit message (imperative, capital letter, no full stop, under 60 characters).
6. "fixed the bug where it crashes on empty files"
7. "adding a help message"
8. "I changed the timeout from 5 to 10 seconds"
9. "removed old unused code"
10. "updates readme with install steps"

<details>
<summary>Sample answers (Set 3)</summary>

1. The cleanup script deleted the file. · 2. (e.g.) The installer changed the settings. · 3. My roommate bought a new cable. · 4. (e.g.) We found the bug during testing. *or* The test suite found the bug. · 5. The admin reset the password yesterday.
6. `Fix crash on empty input files` · 7. `Add a help message` · 8. `Increase timeout from 5 to 10 seconds` · 9. `Remove unused code` · 10. `Add install steps to README`
</details>

---

## Watch, practise, and write

*Companions, not replacements: the lessons above come first. Full list: [courses-and-videos.md](../../courses-and-videos.md#foundations-english).*

- **Watch:** Khan Academy Grammar: the syntax and verb-tense units. Oxford Online English (YouTube): verb tense lessons.
- **Practise:** Khan Academy Grammar exercises on subject–verb agreement and tense.
- **Fun writes this stage** ([prompt bank](writing-prompts.md)): #29 commit log of your life · #31 the life of a packet · #34 active or passive detective · #38 diary of a CPU

---

## Self-check

1. **[R] Blank sheet:** what makes a sentence complete; the five patterns with examples; the six tenses with examples; the agreement traps.
2. **Irregular verbs:** cover the past and past-participle columns. Write them for all 58 verbs. Target: **54/58**.
3. **Fix this paragraph** (8 errors in tense, agreement, form, or fragments):
   > Last week I install a new graphics card. The box with all the cables were heavy. I have wrote down every step. First I open the case. Then plugged the card in. There was two screws missing, so I use tape. The computer start fine after that.
4. **Teach-back [F]:** record a short explanation of "how to find the subject and verb of any sentence."

<details>
<summary>Answers (Self-check 3)</summary>

*Last week I **installed** a new graphics card. The box with all the cables **was** heavy. I **wrote** (or **have written**) down every step. First I **opened** the case. Then **I plugged** the card in. There **were** two screws missing, so I **used** tape. The computer **started** fine after that.*

The 8 errors: install → installed · were → was (subject is *box*) · have wrote → wrote / have written · open → opened · "Then plugged" fragment → "Then I plugged" · was → were (*two screws*) · use → used · start → started.
</details>

## Done when

- [ ] Practice Sets 1–3 done; 80%+ or redone with new examples.
- [ ] Irregular verbs ≥ 54/58, and on flashcards.
- [ ] Self-check paragraph fixed with all 8 errors found.
- [ ] Every git commit you've made since starting this stage uses an imperative message.
- [ ] [Machine Manual](projects/machine-manual/spec.md) Milestone 2 done.

**Next:** [E06 — Punctuation](E06-punctuation.md).
