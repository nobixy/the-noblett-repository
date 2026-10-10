---
title: "E01 — Spelling Baseline and High-Frequency Words"
stage: E01
track: english
hours: 15
weeks: 3
---

# E01 — Spelling Baseline and High-Frequency Words

**In this stage you will:** measure exactly where your spelling is today, learn a method for fixing any word for good, start your personal error log, and learn the 200 words that matter most.

**Time:** about 15 hours over 3 weeks (45–60 minutes on weekday evenings).

---

## Why start here

You cannot fix what you have not measured. Most adults who "can't spell" actually misspell a fairly small set of words, over and over, often because of a handful of patterns. Once you see your own list, the problem shrinks from "I'm bad at English" to "I have 60 words and 5 patterns to fix." That is a project, and you are good at projects.

There is also good news about English itself. English spelling looks random, but studies of English words have found that about half of them follow sound-to-letter rules exactly, and most of the rest have only one tricky spot. The irregular spots have reasons (the history box below). You will learn the rules in E02 and the word parts in E03. This stage builds the habit and the measuring tools.

**Connection to later work:** your error log is your first dataset. In [01 Intro CS Taste](../../01-intro-cs-taste/overview.md) and the [Spelling Engine](projects/spelling-engine/spec.md) project, you turn it into a program that reads words aloud and tests you. In Module 02 it becomes part of your own spaced-repetition app. You are building the tool you will learn with.

> **Why is English spelling so messy?** (a two-minute story, worth knowing)
> English spelling was mostly fixed in the 1400s–1600s, when printing spread. But English pronunciation kept changing, especially the long vowels (this is called the Great Vowel Shift). So "knight" was once said with the *k* and a throaty *gh*. The letters stayed; the sounds moved. English also borrowed words from French ("restaurant"), Latin ("receive"), and Greek ("rhythm", "psychology"), often keeping their original spelling. So English spelling is often a record of *where a word came from* and *how it used to sound*. When a spelling seems crazy, its history usually explains it, and the explanation makes it easier to remember. That is a why-ladder [W] you can use on any strange word.

---

## Part 1 — Measure your baseline (week 1, days 1–3)

Do all three tests before learning anything. Save the results in your workbench as `english/baseline-YYYY-MM-DD.md`. You will repeat these tests at the end of E03 and E10 and compare.

### Test A: Dictation (60 words)

You need someone or something to read words aloud, so you cannot see them.

1. Take your phone's voice recorder. Read the 60 words in the **Dictation list** below aloud, slowly, with a 5-second pause between words. Say each word, then a short sentence using it, then the word again. ("Separate. Keep the files separate. Separate.")
2. Do **not** study the list. Record it, then wait at least one day so you forget the visual memory of it.
3. Play the recording and write each word on paper or in a plain text file with spell check **off**.
4. Mark it against the list. Count your score out of 60.

*Linux option:* if you have `espeak-ng` installed (`sudo pacman -S espeak-ng`), the command `espeak-ng -s 120 "separate"` reads a word aloud. In the Spelling Engine project you will automate this.

**Dictation list** (a mix of very common words and commonly misspelled ones):

| | | | | | |
| :-- | :-- | :-- | :-- | :-- | :-- |
| because | which | their | there | they're | were |
| where | would | could | should | through | thought |
| though | enough | friend | believe | receive | piece |
| until | again | different | beginning | business | definitely |
| separate | necessary | probably | finally | really | usually |
| writing | written | address | argument | knowledge | library |
| government | environment | tomorrow | February | Wednesday | answer |
| surprise | similar | interest | immediately | occurred | recommend |
| beautiful | successful | although | whether | weather | their own |
| truly | across | already | all right | a lot | until then |

### Test B: Free-writing error rate

1. Set a timer for 15 minutes. Write about anything you know well: your job, a machine you use, a game you play. Spell check off. Do not stop to fix things.
2. Count the words you wrote. (On Linux: save as `freewrite.txt` and run `wc -w freewrite.txt`.)
3. Now find the misspellings. Run a spell checker *after* writing (`hunspell -l freewrite.txt` lists unknown words; or paste into any editor with spell check). Also read it once yourself: spell checkers miss real words used wrongly (*there* for *their*).
4. Calculate your **error rate**: misspellings ÷ words × 100. Example: 9 errors in 300 words = 3 errors per 100 words.

This number is the one that matters most, because it is about your *real* writing. Typical goal by E03: under 1 per 100. By E10: under 0.3 per 100.

### Test C: Proofreading

The passage below has **15 spelling errors**. Find as many as you can in 10 minutes. Write each wrong word and its correction. Then check the answers.

> Yesterday I tryed to set up my new computer. The instructions where not very clear, and I definately did not have enough time. First I had to seperate the cables, wich took a long time becuase they were tangled. Then the screen would'nt turn on. I beleive the problem was the power cable, but I wasnt sure. I went threw every step again untill it worked. Finaly the screen came on, and I was realy suprised how fast the computer was. Next time I will read the hole manual first.

<details>
<summary>Answers (Test C)</summary>

1. tryed → **tried** · 2. where → **were** · 3. definately → **definitely** · 4. seperate → **separate** · 5. wich → **which** · 6. becuase → **because** · 7. would'nt → **wouldn't** · 8. beleive → **believe** · 9. wasnt → **wasn't** · 10. threw → **through** · 11. untill → **until** · 12. Finaly → **Finally** · 13. realy → **really** · 14. suprised → **surprised** · 15. hole → **whole**

Bonus point if you can say *why* "would'nt" is wrong: the apostrophe stands where letters were removed. *Would not* loses the *o* of *not*, so the apostrophe goes between *n* and *t*: *wouldn't*. Knowing the reason is the habit we want.
</details>

### Write your baseline note

In `baseline-YYYY-MM-DD.md`, record:
- Dictation score: __ / 60
- Free-writing error rate: __ per 100 words
- Proofreading score: __ / 15
- Every word you got wrong in any test (these start your error log)
- One sentence: what kind of mistakes do you see most? (Guess. You will check this guess later.)

---

## Part 2 — Start your error log (week 1, day 4)

Your **error log** is the most important file in this track. Every misspelled word you notice, from any source, goes in it. Keep it as a plain text file in your workbench: `english/spelling-log.tsv`. ("TSV" means tab-separated values: one row per line, columns separated by a Tab key press. It is a simple data format that programs can read. You will write such a program in the Spelling Engine project.)

The columns:

```
date	wrong	right	tag	note
2026-10-12	becuase	because	letter-order	by + cause; "big elephants can always understand small elephants"
2026-10-12	seperate	separate	vowel-unclear	there is "a rat" in sep-A-RAT-e
2026-10-12	threw	through	homophone	threw = past of throw; through = in one side, out the other
```

- **tag:** what *kind* of error it was. Start with these tags; you will add rule tags in E02:
  - `letter-order` — right letters, wrong order (becuase)
  - `missing-letter` — a letter left out (finaly, acros)
  - `extra-letter` — (untill, truely)
  - `vowel-unclear` — the vowel sound is unclear when spoken (seperate, definately)
  - `homophone` — a real word, but the wrong one (there/their, threw/through)
  - `apostrophe` — (wasnt, would'nt)
  - `double-letter` — (ocured, accomodate, recomend)
  - `sound-spelling` — written the way it sounds, but English spells it differently (tryed, wich)
- **note:** your memory hook (see Part 3).

**Rule:** a word leaves the log only after you have spelled it right in dictation on 4 different days spread over at least 3 weeks (the spacing schedule: 1, 3, 7, 21 days). Mark it `learned` in the note column then; do not delete it. Your learned list is a record of progress.

---

## Part 3 — How to learn a spelling for good

Use this method for every word in your log and every word in the lists below. It is called **Look–Say–Cover–Write–Check**, with two additions that matter for adults: *find the hard spot* and *make a hook*.

**Subgoal labels [S] for learning one word:**

1. **Look:** see the whole word. Say it normally.
2. **Split:** break it into syllables (beats): *sep-a-rate*, *Wed-nes-day*, *gov-ern-ment*.
3. **Find the hard spot:** which letter or letters would you get wrong? Underline them. Usually it is one spot: sep**a**rate, gover**n**ment, Wed**nes**day.
4. **Hook the hard spot.** Pick the hook type that works:
   - *Spelling voice:* say it the way it is spelled, not the way it sounds: "Wed-NES-day", "gov-ERN-ment", "Feb-RU-ary".
   - *Word inside a word:* "sep-**a rat**-e", "be-**lie**-ve (never believe a lie)", "**hear** with your **ear**", "the **end** of a **friend**ship" (fri-**end**).
   - *Related word:* "**sign**" → "signature" (the silent *g* is heard in the relative); "**muscle**" → "muscular"; "**definite**" → "finite" (so it is defin-**i**-te, never defin-**a**-te).
   - *Meaning:* "**together**" is "to get her" — silly is fine. Silly is memorable.
   - *Rule:* if a rule from E02 explains it, the rule is the hook.
5. **Cover** the word. Wait 5 seconds.
6. **Write** it from memory, saying the spelling voice.
7. **Check** letter by letter. If wrong, go back to step 3. If right, write it twice more, then write it in a sentence of your own.

This takes about one minute per word. That is the right speed. Ten words a day, done this way, beats fifty words copied quickly.

> **Why this works [W]:** Step 6 is retrieval [R]: pulling the spelling from memory is what makes it stick, not looking at it. Step 3 focuses your effort on the only part that is actually hard. Step 4 gives your memory something meaningful to hold, which is easier than holding a random letter string. Step 7 gives instant feedback so you don't practise a mistake.

---

## Part 4 — The two core lists (weeks 1–3)

Learn these lists over three weeks using the daily routine in Part 5. Many of the words you already know. Test each word first (dictation); only study the ones you miss. That is efficient, and the testing itself strengthens the ones you know.

### Core List A — 100 words that make up about half of everything you read

These short words are everywhere. Most you know. The bolded ones are the ones adults most often get wrong or mix up.

> the · of · and · a · to · in · is · you · that · it · he · **was** · for · on · **are** · as · with · his · **they** · I · at · be · this · have · from · or · one · had · by · **word** · but · not · **what** · all · **were** · we · **when** · your · can · **said** · **there** · use · an · each · **which** · she · do · how · **their** · if · will · up · other · about · out · many · then · them · these · so · some · her · **would** · make · like · him · into · time · has · look · two · more · **write** · go · see · number · no · way · **could** · people · my · than · first · water · been · call · **who** · oil · **its** · now · find · long · down · day · did · get · come · made · may · part · **know** · **because** · **does** · **where** · **through** · **should** · **again** · **any** · **many** · **friend**

### Core List B — 100 everyday words adults commonly misspell

> accept · accidentally · accommodate · achieve · across · address · a lot · all right · already · although · amateur · apparent · argument · basically · beautiful · beginning · believe · business · calendar · category · cemetery · changeable · colleague · coming · committee · completely · conscious · definitely · describe · description · desperate · different · disappear · disappoint · embarrass · environment · exaggerate · exercise · existence · experience · familiar · February · finally · foreign · forty · forward · friend · government · grammar · guarantee · guard · height · humorous · immediately · independent · interest · interrupt · knowledge · library · license · lightning · maintenance · medicine · minute · mischievous · necessary · neighbor · noticeable · occasion · occurred · occurrence · opinion · original · parallel · particular · perform · piece · possession · possible · prefer · privilege · probably · pronunciation · publicly · receive · recommend · referred · relevant · restaurant · rhythm · schedule · separate · similar · sincerely · successful · surprise · though · threshold · tomorrow · truly · until · weird · whether

**American or British?** This curriculum uses **American spelling** (color, center, organize, license, neighbor) because most programming documentation, code, and tools use it. If you prefer British spelling, choose it once and stay consistent. Mixing them is the real error.

### Core List C — your error log

The words in your own error log from Part 1 come first, every day, before the lists above. Your own mistakes are the most valuable words to study.

---

## Part 5 — The three-week routine

Each weekday (45–60 minutes total, alongside copywork):

| Step | Time | What |
| :-- | :-- | :-- |
| 1 | 3 min | **Warm-up recall [R]:** write yesterday's 10 words from memory. Check. Misses go back to today's list. |
| 2 | 12 min | **10 words** with Look–Say–Cover–Write–Check: 4 from your error log, 3 from List A or B (new), 3 due for review (spacing). |
| 3 | 15–20 min | **Copywork [C], Level 1:** one 2–3 sentence passage from Simple English Wikipedia (e.g. the article "Computer"). Use the fast version from [study-protocols](../../study-protocols.md#c--franklin-copywork) on Monday–Thursday; the full version (hide for a day) on Friday. |
| 4 | 5 min | **Sentence use:** write 3 sentences, each using one of today's words, about something you did today. |
| 5 | 2 min | **Log:** new misspellings from any source go in `spelling-log.tsv`. |

**Fridays:** 20-word dictation test from the week's words plus 5 from earlier weeks (mixed, [I]). Record the score.

**Spacing by hand (until you build the tool):** use a paper box with five sections, or five envelopes, labelled *1 day, 3 days, 7 days, 21 days, 60 days*. Each word is a card. Right → move it one section to the right. Wrong → back to *1 day*. Each day, study the cards whose time has come. (This is called a Leitner box. You will program one in Module 02.)

---

## Part 6 — Study protocols in this stage

- **[R] Retrieval:** every spelling test is dictation, never "look at the list and see if it looks right." Recognising a word is much easier than producing it, and producing it is the skill you need.
- **[W] Why-ladder:** each day, pick one word from your log and ask "why is it spelled like that?" Look it up on etymonline.com (the Online Etymology Dictionary, free). Example: *because* → "by cause" in Middle English → that's why it has *cause* inside it. Write the answer as the word's hook.
- **[F] Feynman:** at the end of week 2, write half a page explaining to a friend *how you learn a spelling* and *why it works*. Mark any step you cannot justify. (The "Why this works" box above is the answer to check against, after you write yours.)
- **[I] Interleaving:** Friday tests mix this week's words with older ones. Never test one week's words alone.
- **[D] Diffuse:** some words will not stick. After three failed days, stop studying that word for a week. Put it on a sticky note somewhere you'll see it without trying (the bathroom mirror). Then go back to it.

---

## Self-check (end of week 3)

Do this cold, without studying first.

1. **Dictation:** record and take a 40-word dictation: 20 random words from List B, 10 from your error log, 10 from List A's bolded words. Target: **36/40**.
2. **Proofreading:** find the 10 errors.
   > I recieved you're message on Wendsday. Their is a problem with the adress you gave me, and I am not shure which biulding it is. Could you tell me wether it is the one acros from the libary?

3. **Explain:** in 3–5 sentences, explain the Look–Say–Cover–Write–Check method and why the *Write from memory* step matters.
4. **Free-write again:** 15 minutes, any topic. Compute your new error rate. Compare with your baseline.

<details>
<summary>Answers (self-check 2)</summary>

recieved → **received** · you're → **your** · Wendsday → **Wednesday** · Their → **There** · adress → **address** · shure → **sure** · biulding → **building** · wether → **whether** · acros → **across** · libary → **library**

*received* follows the "i before e, except after c" rule from E02. *you're* means *you are*; "you are message" makes no sense, so it must be *your*.
</details>

---

## Done when

- [ ] Baseline note written with all three test results.
- [ ] `spelling-log.tsv` exists and has at least 30 entries, each with a tag and a hook.
- [ ] You have used Look–Say–Cover–Write–Check on at least 100 words.
- [ ] Self-check dictation ≥ 36/40.
- [ ] Your free-writing error rate has dropped from your baseline (any amount counts).
- [ ] 10+ copywork sessions logged with difference counts.

**Next:** [E02 — Sound Patterns and Spelling Rules](E02-sound-patterns-and-spelling-rules.md). Your error log's tags will tell you which rules matter most to you.
