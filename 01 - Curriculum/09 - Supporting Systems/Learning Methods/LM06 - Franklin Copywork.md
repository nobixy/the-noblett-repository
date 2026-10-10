---
title: "LM06: Franklin Copywork"
type: learning-method
method_id: LM06
evidence: "Anecdotal; no controlled studies"
project_hours: 3
counts_toward: "BW"
---

# LM06 — Franklin Copywork
*Deep dive + project ([[DR-009 - Learning Method Deep Dives|DR-009]]). Hub: [[LM00 - Learning Methods Hub|Learning Methods]] · Method in practice: [[how-i-study]] §1*

> [!NOTE] Evidence: **Anecdotal; no controlled studies**

## In plain words
Take a short passage by a great writer and make notes on what each sentence says. Put the original away for a few days, rewrite it from your notes, then compare yours with the original and learn from every difference.

## The evidence, honestly
The source is Benjamin Franklin's own *Autobiography*: he taught himself to write this way using essays from *The Spectator*.
No controlled study tests the method itself. What it has going for it is deliberate practice with immediate, specific feedback (the original is the answer key), plus retrieval of the structure.
Use it, but measure whether your writing improves (e.g. editor feedback, clarity of your posts). Don't assume it does.

## Using it in EECS
- Do it with technical prose: a paragraph from the Go spec, a Raymond Chen post, a Julia Evans zine, or a section of a famous paper.
- The same trick works for code: retype a small, well-written function from memory, then diff.

## Common mistakes
- Waiting only an hour, so you just remember the words.
- Comparing loosely. Compare word by word.

## 🔨 Project: Copywork Diff tool
A Python script using `difflib` that compares your rewrite with the original word by word. It prints added and removed words, plus average sentence length and the longest sentence in each version. No-code option: compare on paper with two highlighter colours.
- **Done when:** you used it on 3 copywork days and pasted the stats into [[Writing Hub]].
- **Time:** about 3 h, counted inside [[BW - Bedrock English and Grammar|BW]]'s existing hours (replaces 5 of the 10 parsing sentences and 5 of the 10 de-nominalization drills; the diff tool does copywork's comparison step).
- **Level / when:** Beginner Python (one standard-library module). Week 6, with the Twine story.

## Sources
- Benjamin Franklin, *Autobiography* (1791; free at Project Gutenberg).
- Ericsson, Krampe & Tesch-Römer (1993), "The role of deliberate practice in the acquisition of expert performance", *Psychological Review* 100(3).
