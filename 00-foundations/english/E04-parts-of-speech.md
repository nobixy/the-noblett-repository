---
title: "E04 — Parts of Speech"
stage: E04
track: english
hours: 15
weeks: 2
---

# E04 — Parts of Speech

**In this stage you will:** learn the eight kinds of words and the job each one does, learn the test for each, and use them to name things in code. You will start the [Machine Manual](projects/machine-manual/spec.md) project.

**Time:** about 15 hours over 2 weeks.

**Before you start:** E03 done. Spelling continues as a 10-minute daily habit.

---

## Why this matters

Every word in a sentence has a **job**. Grammar is just the study of those jobs and how they fit together, the same way a circuit diagram shows what each part does and how parts connect. Once you can see the jobs, you can:

- fix sentences that "sound wrong" by finding the part that is doing the wrong job;
- understand grammar explanations, which all use these names;
- name things in code clearly (the second half of this stage).

**The key idea:** a word's part of speech is decided by **what it does in this sentence**, not by the word itself. *Test* is a noun in "the test failed" and a verb in "test the code." The same is true in programming: the same bits can be a number or a letter, depending on how the program uses them. Keep this idea; it comes back in Module 06.

---

## Part 1 — The eight kinds of words

### 1. Nouns — names of things

A **noun** names a person, place, thing, or idea.
- People and things: *engineer, user, cable, laptop, file, packet*
- Places: *kitchen, server room, Germany*
- Ideas: *speed, security, freedom, error*

**Tests:** you can put *the* or *a* in front of it (*the cable*); you can usually make it plural (*cables*).

**Proper nouns** are names of specific things and start with a capital: *Linux, Python, Tuesday, London*.

### 2. Pronouns — stand-ins for nouns

A **pronoun** replaces a noun so you don't repeat it: *I, you, he, she, it, we, they, me, him, her, us, them, this, that, who, which*.

> The *server* crashed. *It* restarted after a minute.

**Rule:** a reader must always know which noun a pronoun points to. "The program sent the file to the server, and **it** crashed" — what crashed? The program, the file, or the server? Vague pronouns are one of the biggest sources of confusion in technical writing. When in doubt, repeat the noun. This is like a pointer in programming (Module 07): a pointer that might point to the wrong thing is a bug.

### 3. Verbs — actions and states

A **verb** says what happens or what is.
- Actions: *run, send, crash, compile, read, write, connect*
- States (linking verbs): *is, are, was, seems, becomes, feels*

**Tests:** it can change with time: *send / sent / will send*; you can put *I* or *it* in front: *it crashes*.

Verbs are the engine of a sentence. **Every complete sentence needs at least one verb.** You will study verbs in depth in E05.

### 4. Adjectives — describe nouns

An **adjective** tells you more about a noun: which one, what kind, how many.
> a **loose** cable · the **old** laptop · **slow** internet · **three** errors · the file is **empty**

**Tests:** it fits in "the ___ thing" or after "is": *the empty file*, *the file is empty*.

### 5. Adverbs — describe verbs (and more)

An **adverb** tells you how, when, where, or how much something happens.
> The program runs **slowly**. Restart it **now**. Try **again**. It is **very** fast.

Many adverbs end in *-ly* (*quickly, safely*). Many don't (*now, often, never, again, very, too, here*).

### 6. Prepositions — show relationships

A **preposition** shows where, when, or how one thing relates to another. It comes before a noun.
> **in** the folder · **on** the desk · **under** the cable · **from** the server · **to** the client · **after** the update · **with** a password · **between** two devices · **through** the router

Prepositions matter enormously in technical writing. "Copy the file **to** the server" and "copy the file **from** the server" are opposite instructions that differ by one small word.

### 7. Conjunctions — join things

A **conjunction** joins words or ideas.
- **Joining equals:** *and, but, or, so, yet, for, nor* (memory hook: FANBOYS = **F**or, **A**nd, **N**or, **B**ut, **O**r, **Y**et, **S**o)
- **Joining an idea that depends on another:** *because, although, if, when, while, unless, after, before, since*

> The test passed, **but** the build is slow. **If** the light is red, unplug it.

You will use these heavily in E07. They are the logic of English: *and, or, if, because, unless* map directly onto code (`and`, `or`, `if`).

### 8. Determiners — point to nouns

A **determiner** comes before a noun and says which one or how many: *the, a, an, this, that, these, those, my, your, its, their, every, each, some, any, no, two, many*.

> **the** file · **a** bug · **an** error · **this** cable · **every** test · **two** seconds

**a or an?** Use **an** before a vowel *sound*: *an error, an hour* (silent h), *an SSD* ("ess-ess-dee"). Use **a** before a consonant sound: *a bug, a user* ("you-zer"), *a USB cable* ("you-ess-bee").

**the or a?** *a* = any one, not yet known to the reader (*a bug appeared*). *the* = a specific one the reader already knows about (*the bug is in line 40*). This is the "given and new" idea you will meet again in E08.

### (Bonus) Interjections

*Wow, oh, oops, hey.* Exclamations. Rarely used in technical writing.

---

## Part 2 — One word, many jobs

The same spelling can do different jobs. Always ask: *what is it doing here?*

| Word | As a noun | As a verb | As an adjective |
| :-- | :-- | :-- | :-- |
| test | The **test** failed. | **Test** the code. | the **test** suite (a noun used to describe another noun) |
| file | Open the **file**. | **File** the report. | the **file** menu |
| run | The **run** took 2 seconds. | **Run** the program. | |
| fast | | | a **fast** computer |
| fast (adverb) | | It runs **fast**. | |
| back up | a **backup** | **back up** your files | the **backup** drive |

The last row connects to E03: the one-word/two-word rule is really a parts-of-speech rule. *Backup* (noun) vs *back up* (verb).

**Nouns as describers:** English often puts one noun before another to describe it: *test suite, file system, network cable, error message, power supply*. The first noun acts like an adjective. Technical English stacks these a lot: *network packet header checksum field*. Long stacks are hard to read; in E08 you'll learn to break them up.

---

## Part 3 — Parts of speech in code

Programmers use the same jobs to name things. Good names make code readable; bad names make it a puzzle.

| Thing in code | Should be a… | Good names | Bad names |
| :-- | :-- | :-- | :-- |
| A function (does something) | **verb** or verb + noun | `send`, `parse_header`, `open_file`, `count_words` | `data`, `processing`, `thing`, `doit` |
| A variable holding a thing | **noun** | `file_name`, `packet`, `user_count`, `total` | `x`, `temp2`, `stuff` |
| A collection of things | **plural noun** | `packets`, `users`, `lines` | `packet_list_array`, `p` |
| A true/false value | **adjective** or a **yes/no question** | `is_empty`, `has_data`, `can_retry`, `ready` | `flag`, `check`, `status` |
| A class or type (a kind of thing) | **singular noun** | `Packet`, `Parser`, `Connection` | `Packets`, `DoParsing` |
| An action that converts | **verb** `to_x` or `x_from_y` | `to_binary`, `celsius_from_fahrenheit` | `binary2`, `convert_stuff` |

**Rule of thumb:** read the code aloud as English. `if is_empty(queue): wait()` reads as "if the queue is empty, wait." That is good code. `if q_chk(x): w()` reads as nothing.

---

## Part 4 — Practice routine (2 weeks)

| Day | Lesson (15–20 min) |
| :-- | :-- |
| Week 1 Mon | Nouns and pronouns. Find 20 nouns in your copywork passage. Find every pronoun and draw an arrow to the noun it points to. |
| Tue | Verbs. Underline every verb in 10 sentences from the Python Tutorial. |
| Wed | Adjectives and adverbs. Describe your desk in 5 sentences; circle each adjective and adverb. |
| Thu | Prepositions and conjunctions. Write 10 directions from your front door to your kitchen using only prepositions to show the way. |
| Fri | Determiners, *a/an*, *the/a*. Practice Set 1. |
| Week 2 Mon | One word, many jobs. Practice Set 2. |
| Tue | Naming in code. Practice Set 3. |
| Wed | Word families. Practice Set 4. |
| Thu | Machine Manual Milestone 1 (inventory of parts and actions). |
| Fri | Self-check. |

**Every day:**
- **Warm-up [R]:** from memory, write the eight parts of speech with one example each. (Day 1: write as many as you can after reading. By day 5 you should get all eight in under 2 minutes.)
- **Spelling (10 min):** error log + review.
- **Copywork [C]:** Level 2. After diffing, label the part of speech of every word in one sentence of the original.

**Study protocols for this stage:**
- **[S] Subgoal labels for finding a word's part of speech:**
  1. Find the verb first (what happens?).
  2. Ask *who or what* does it → that's a noun or pronoun.
  3. Ask *what kind / which / how many* about each noun → adjectives and determiners.
  4. Ask *how / when / where* about the verb → adverbs.
  5. Find the small linking words → prepositions (before a noun) or conjunctions (joining ideas).
- **[W] Why-ladder:** why does English have determiners at all? (Try answering before reading on.) *Because the reader needs to know whether you mean any one thing or a specific one they already know. Without "the" vs "a", "restart server" could mean any server or the one we were talking about.* Why do pronouns cause bugs in writing? Write your answer.
- **[F] Feynman:** explain to a friend, without the grammar words, what a preposition does. Then explain it *with* the word, as if teaching it.

---

## Practice sets

### Practice Set 1 — Label every word (10 sentences)

Write the part of speech above each word: **N** noun, **P** pronoun, **V** verb, **Adj** adjective, **Adv** adverb, **Prep** preposition, **C** conjunction, **D** determiner, **I** interjection.

1. The old printer jams often.
2. She quickly restarted the server.
3. The cable under the desk is loose.
4. I saved the file, but the program crashed.
5. Data moves slowly through a long wire.
6. They tested every function carefully.
7. Run the test again.
8. The fast run finished in two seconds.
9. Because the battery was low, the laptop stopped.
10. Wow, this keyboard feels great!

<details>
<summary>Answers (Set 1)</summary>

1. The **D** · old **Adj** · printer **N** · jams **V** · often **Adv**
2. She **P** · quickly **Adv** · restarted **V** · the **D** · server **N**
3. The **D** · cable **N** · under **Prep** · the **D** · desk **N** · is **V** · loose **Adj**
4. I **P** · saved **V** · the **D** · file **N** · but **C** · the **D** · program **N** · crashed **V**
5. Data **N** · moves **V** · slowly **Adv** · through **Prep** · a **D** · long **Adj** · wire **N**
6. They **P** · tested **V** · every **D** · function **N** · carefully **Adv**
7. Run **V** · the **D** · test **N** · again **Adv**
8. The **D** · fast **Adj** · run **N** · finished **V** · in **Prep** · two **D** · seconds **N**
9. Because **C** · the **D** · battery **N** · was **V** · low **Adj** · the **D** · laptop **N** · stopped **V**
10. Wow **I** · this **D** · keyboard **N** · feels **V** · great **Adj**

Notes: *is, was, feels* are linking verbs (they connect a noun to a description). In 7 and 8, *run* changes job. Numbers like *two* act as determiners (some books call them adjectives; either answer is fine).
</details>

### Practice Set 2 — What job is the word doing? (8 items)

Say whether the **bold** word is a noun, verb, or adjective here.

1. Please **update** your browser.
2. The **update** broke my sound.
3. Click the **update** button.
4. The **network** is down.
5. Check the **network** settings.
6. They **network** at conferences.
7. Did you **back up** your work?
8. Where is the **backup**?

<details>
<summary>Answers (Set 2)</summary>

1. verb · 2. noun · 3. adjective (a noun describing *button*) · 4. noun · 5. adjective (describing *settings*) · 6. verb · 7. verb · 8. noun
</details>

### Practice Set 3 — Rename it (6 items)

Each name is bad. Write a better one and say which part of speech it uses.

1. `x` holds the number of users.
2. A function called `data()` downloads the weather data.
3. `flag` is `True` when the file exists.
4. `item` holds a list of many packets.
5. A function called `processing()` processes an order.
6. A class called `Users` describes one user.

<details>
<summary>Sample answers (yours may differ; check the part of speech)</summary>

1. `user_count` (noun) · 2. `download_weather()` (verb + noun) · 3. `file_exists` (a yes/no statement) · 4. `packets` (plural noun) · 5. `process_order()` (verb + noun) · 6. `User` (singular noun)
</details>

### Practice Set 4 — Word families (5 rows)

Fill in the table. Use E03's suffixes. Spelling counts.

| Verb | Noun | Adjective | Adverb |
| :-- | :-- | :-- | :-- |
| create | | | |
| compute | | | |
| rely | | | |
| secure | | (same as verb) | |
| simplify | | simple | |

<details>
<summary>Answers (Set 4)</summary>

| Verb | Noun | Adjective | Adverb |
| :-- | :-- | :-- | :-- |
| create | creation (also creator) | creative | creatively |
| compute | computation (also computer) | computational | computationally |
| rely | reliability (also reliance) | reliable | reliably |
| secure | security | secure | securely |
| simplify | simplicity (also simplification) | simple | simply |

Spelling notes: *rely → reliable* (Rule 3, y → i); *simple + ly = simply* (an exception: the *le* becomes *ly*, not *lely*).
</details>

---

## Self-check

1. **[R] Blank sheet:** the eight parts of speech, the job of each, the test for each, and two examples each. 10 minutes. Check.
2. **Label** five new sentences from your copywork passage. Check them with a grammar reference if unsure (Purdue OWL, free online: owl.purdue.edu).
3. **Pronoun hunt:** take a page of your own journal writing. Circle every *it, this, that, they*. For each, can a stranger tell what it points to? Fix the vague ones.
4. **Code names:** look at any small piece of code (yours from Module 01 if you have started, or the Python Tutorial's examples). Rate each name: good / unclear / bad, and fix one.

## Done when

- [ ] Practice Sets 1–4 done and checked; 80%+ on each, or redone with new examples.
- [ ] Blank-sheet recall of all eight parts with tests and examples.
- [ ] Pronoun hunt done on your own writing.
- [ ] [Machine Manual](projects/machine-manual/spec.md) Milestone 1 done.

**Next:** [E05 — The Simple Sentence and Verbs](E05-the-simple-sentence-and-verbs.md).
