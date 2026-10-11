---
title: "LM06: Franklin Copywork"
type: learning-method
method_id: LM06
evidence: "Anecdotal; no controlled studies"
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
- **Done when:** you used it in 3 copywork sessions and pasted the stats into [[Writing Hub]].
- **Level:** Beginner Python (one standard-library module).
- **Fits with:** Protocol **C** (Franklin copywork) in every English session; [Copydiff](<../05-data-structures-and-algorithms/projects/copydiff/spec.md>) (Module 05) automates the diff.

## Sources
- Benjamin Franklin, *Autobiography* (1791; free at Project Gutenberg).
- Ericsson, Krampe & Tesch-Römer (1993), "The role of deliberate practice in the acquisition of expert performance", *Psychological Review* 100(3).
