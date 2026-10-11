---
title: "LM16: Zettelkasten"
type: learning-method
method_id: LM16
evidence: "Practitioner method; not tested"
---

# LM16 — Zettelkasten
*Deep dive + project ([[DR-009 - Learning Method Deep Dives|DR-009]]). Hub: [[LM00 - Learning Methods Hub|Learning Methods]] · Method in practice: [[how-i-study]] §1*

> [!NOTE] Evidence: **Practitioner method; not tested**

## In plain words
Keep a slip-box of small notes, one idea each, in your own words, each linked to related notes. Over time the links, not the folders, become your understanding.

## The evidence, honestly
The method comes from sociologist Niklas Luhmann's slip-box and Ahrens' *How to Take Smart Notes* (2017).
There are no controlled studies of the method itself.
Its parts do have support: writing in your own words (the generation effect, Slamecka & Graf 1978) and linking to what you already know (elaboration).
The risk is that note-taking becomes the hobby (your how-i-study quote).

## Using it in EECS
- One note per mechanism: "TLB", "two's complement", "Little's law".
- Link each to where it shows up (OS, architecture, networking).
- The Zettelkasten template is in `04 - System/`.

## Common mistakes
- Copying text instead of rewriting it.
- Notes with no links.
- Spending more time organizing notes than studying.

## 🔨 Project: Vault Link-Graph Analyzer
A Python script that walks your vault, parses its wikilinks (the double-square-bracket links), and lists orphan notes, the most-linked notes, and notes with no outgoing links. Stretch: draw the graph with `networkx`. This is a preview of Module 12's [Matrix Studio](<../12-math-for-engineering/projects/matrix-studio/spec.md>), which ranks your vault's notes by their links with eigenvectors.
- **Done when:** it runs on your vault, its orphan list matches Obsidian's graph view, and you wrote 5 atomic notes that link orphans in.
- **Level:** Intermediate Python (os.walk, regex, dicts).
- **Fits with:** This vault itself; the [[Zettelkasten Atomic Note Template]].

## Sources
- Ahrens, *How to Take Smart Notes* (2017).
- Slamecka & Graf (1978), "The generation effect", *Journal of Experimental Psychology: Human Learning and Memory* 4(6).
