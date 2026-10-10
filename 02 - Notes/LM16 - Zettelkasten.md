---
title: "LM16: Zettelkasten"
type: learning-method
method_id: LM16
evidence: "Practitioner method; not tested"
project_hours: 5
counts_toward: "P5"
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
- The Zettelkasten template is in `06 - Templates/`.

## Common mistakes
- Copying text instead of rewriting it.
- Notes with no links.
- Spending more time organizing notes than studying.

## 🔨 Project: Vault Link-Graph Analyzer
A Python script that walks your vault, parses its wikilinks (the double-square-bracket links), and lists orphan notes, the most-linked notes, and notes with no outgoing links. Stretch: draw the graph with `networkx`. This is a preview of network science in Block 19a.
- **Done when:** it runs on your vault, its orphan list matches Obsidian's graph view, and you wrote 5 atomic notes that link orphans in.
- **Time:** about 5 h, counted inside [[P5 - Tooling|P5]]'s existing hours (counts as the Missing Semester exercises for lecture 2 (shell tools and scripting), 4 (data wrangling) and 6 (version control): the exercises are your own tools).
- **Level / when:** Intermediate Python (os.walk, regex, dicts). Last, in P5.

## Sources
- Ahrens, *How to Take Smart Notes* (2017).
- Slamecka & Graf (1978), "The generation effect", *Journal of Experimental Psychology: Human Learning and Memory* 4(6).
