# Handoff Report: Link & Graph Topology Comprehensive Vault Survey

**Explorer:** Explorer 1 (Link & Graph Topology Explorer)  
**Agent Folder:** `/home/noblixy/The Noblett Repository/.agents/explorer_survey_1`  
**Date & Timestamp:** 2026-09-25T10:16:45Z  
**Target Repository:** `/home/noblixy/The Noblett Repository`  
**Authoritative Mission Reference:** `/home/noblixy/The Noblett Repository/.agents/ORIGINAL_REQUEST.md`  
**Mode:** Read-Only Investigation (No modifications to vault source files)

---

## Executive Summary

A forensic, programmatic investigation was conducted across every markdown file and attachment in `/home/noblixy/The Noblett Repository` (excluding `.agents/`, `.git/`, and `.obsidian/`). The survey evaluated link integrity, naming syntax, file structure, orphan notes, in/out-degree distribution, and directed reachability from navigation hubs.

Key metrics:
- **Total Vault Files Analyzed:** 87 files (85 Markdown `.md` notes, 1 PDF reference attachment, 1 `.gitignore`).
- **Total Wikilink Instances:** 547 occurrences across all notes.
- **Valid / Resolving Wikilinks:** 516 links (94.33%).
- **Broken / Flawed / Dead Wikilinks:** 31 links (5.67%) across 7 files, driven by 4 distinct root causes.
- **Casing Mismatches:** 0 (all resolved links match the exact case-sensitive filename).
- **Name Ambiguity:** 0 (all 85 note basenames are globally unique across the vault).
- **Current Orphan Notes (In-Degree = 0):** 18 notes (10 non-template domain notes, 4 templates, 3 Bedrock notes orphaned purely by broken link targets, 1 prompt artifact).
- **Dashboard Directed Reachability:** Only 55 / 85 notes (64.7%) are reachable from `00 - Dashboard.md`. 30 notes (35.3%) are completely unreachable.
- **Universal Hub Reachability:** Starting simultaneously from all 12 navigation hubs, 23 notes remain unreachable due to structural disconnection between the Master Tracking subsystem and the Curriculum subsystem.
- **Course Block Sinks (Out-Degree = 0):** 31 core curriculum blocks contain 0 outgoing links, representing complete navigational dead ends.

---

## 1. Observation

### 1.1 Complete Markdown File Catalog & Classification

The vault contains 85 Markdown notes, 1 PDF reference attachment, and 1 `.gitignore` distributed across Johnny.Decimal-style directories:

| Directory Path | File Count | Description / Role |
| :--- | :---: | :--- |
| `[Vault Root]` | 7 `.md` (+ 1 non-md) | `00 - Dashboard.md`, `Checklist.md`, `Your Shelf.md`, `how-i-study.md`, `log.md`, `Telemetry Log.md`, `ORIGINAL_REQUEST.md`, `.gitignore` |
| `01 - Curriculum/` (Root) | 1 `.md` | `Baseline Gap Analysis and Audit Report.md` |
| `01 - Curriculum/Phase -1 - Bedrock Foundations/` | 3 `.md` | `B0 - The Deep Learner's Toolkit.md`, `BM - Bedrock Mathematics.md`, `BW - Bedrock English and Grammar.md` |
| `01 - Curriculum/Phase 0 - Prerequisites/` | 5 `.md` | `P1 - Learning How to Learn.md` through `P5 - Tooling.md` |
| `01 - Curriculum/Year 1 - Fundamentals/` | 11 `.md` | Blocks `01` to `08`, plus 2 Bridge Syllabi (`04a - Differential Equations Bridge.md`, `08a - Circuits and Electronics Bridge.md`) |
| `01 - Curriculum/Year 2 - Systems/` | 9 `.md` | Blocks `09` to `15`, plus 1 Bridge Syllabus (`15a - Signals and Systems Bridge.md`) |
| `01 - Curriculum/Year 3 - Depth/` | 7 `.md` | Blocks `16 - Operating Systems.md` through `22 - Statistics.md` |
| `01 - Curriculum/Year 4 - Specialization/` | 7 `.md` | Core Blocks `23`, `24`, `25`, `27`, plus Specialization slots `26 - Specialization A1.md`, `28 - Specialization A2.md`, `29 - Specialization B1.md` |
| `01 - Curriculum/Year 5 - MEng/` | 3 `.md` | `30 - Capstone.md`, `31 - Specialization B2.md`, `32 - Information Theory.md` |
| `01 - Curriculum/Specializations/` | 12 `.md` | `Specializations Hub.md` + 11 Specialization Tracks (`Track 1` to `Track 11`) |
| `02 - Notes/` | 5 `.md` | 5 Domain Indices (`Hardware Index.md`, `Languages Index.md`, `Math Index.md`, `Systems Index.md`, `Theory Index.md`) |
| `03 - Papers/` | 1 `.md` | `Paper Reading Hub.md` (curates 35 landmark PhD papers with direct curriculum block links) |
| `04 - Writing/` | 1 `.md` | `Writing Hub.md` (writing deliverables and habit protocols) |
| `05 - Projects/` | 1 `.md` | `Projects Hub.md` (curriculum build milestones) |
| `06 - Breadth/` | 1 `.md` | `Breadth and Humanities Hub.md` (HASS subjects and language acquisition tracker) |
| `07 - Reference/` | 2 `.md` (+ 1 `.pdf`) | `Appendix E - Failure Modes.md`, `Appendix F - Curated URLs.md`, `The Independent EECS Program.pdf` |
| `08 - Templates/` | 10 `.md` | 10 reusable study, note, review, and build templates |
| `09 - Mindset & Habits/` | 1 `.md` | `Mindset Hub.md` (behavioral protocols and mental models) |
| **Total** | **85 `.md` + 2 others** | **87 total files** |

---

### 1.2 Wikilink Scan & Resolution Inventory

A comprehensive regex scan was performed across all 85 markdown notes for occurrences matching `!?\[\[([^\]]+)\]\]`:
- **Total Wikilink Occurrences:** 547
- **Resolved Wikilinks:** 516
- **Unresolved / Broken / Dead Wikilinks:** 31
- **Standard Markdown Links (`[text](url)`):** 31 occurrences (all 31 point to external HTTP/HTTPS resources; 0 internal markdown links).
- **Internal Anchor Links (`[[Target#Heading]]`):** 0 occurrences across the entire vault.

---

### 1.3 Forensic Inventory of All 31 Broken/Dead Wikilinks

The 31 broken link instances originate in 7 files and are classified into four distinct categories:

| # | Source File | Line | Verbatim Link Snippet | Target Extracted | Failure Category | Root Cause & Recommended Replacement |
|:---:|:---|:---:|:---|:---|:---:|:---|
| 1 | `00 - Dashboard.md` | 32 | `` `[[Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics\|Bedrock Math]]` `` | `Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics` | Cat A: Path Error | Target folder is inside `01 - Curriculum/`. Use `[[BM - Bedrock Mathematics\|Bedrock Math]]` or `[[01 - Curriculum/Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics\|Bedrock Math]]`. Remove wrapping backticks for active Obsidian linking. |
| 2 | `00 - Dashboard.md` | 33 | `` `[[Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar\|Bedrock English]]` `` | `Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar` | Cat A: Path Error | Same as above. Replace with `[[BW - Bedrock English and Grammar\|Bedrock English]]`. Remove backticks. |
| 3 | `00 - Dashboard.md` | 34 | `` `[[Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit\|Deep Learner's Toolkit]]` `` | `Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit` | Cat A: Path Error | Same as above. Replace with `[[B0 - The Deep Learner's Toolkit\|Deep Learner's Toolkit]]`. Remove backticks. |
| 4 | `Checklist.md` | 19 | `[[Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit\|B0]]` | `Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit` | Cat A: Path Error | Missing `01 - Curriculum/`. Replace with `[[B0 - The Deep Learner's Toolkit\|B0]]`. |
| 5 | `Checklist.md` | 20 | `[[Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics\|BM]]` | `Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics` | Cat A: Path Error | Missing `01 - Curriculum/`. Replace with `[[BM - Bedrock Mathematics\|BM]]`. |
| 6 | `Checklist.md` | 21 | `[[Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar\|BW]]` | `Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar` | Cat A: Path Error | Missing `01 - Curriculum/`. Replace with `[[BW - Bedrock English and Grammar\|BW]]`. |
| 7 | `log.md` | 7 | `[[Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics\|Bedrock Math (Arithmetic)]]` | `Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics` | Cat A: Path Error | Missing `01 - Curriculum/`. Replace with `[[BM - Bedrock Mathematics\|Bedrock Math (Arithmetic)]]`. |
| 8 | `log.md` | 7 | `[[Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar\|Bedrock English (Sentence Architecture)]]` | `Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar` | Cat A: Path Error | Missing `01 - Curriculum/`. Replace with `[[BW - Bedrock English and Grammar\|Bedrock English (Sentence Architecture)]]`. |
| 9 | `log.md` | 8 | `[[Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit\|The Deep Learner's Toolkit]]` | `Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit` | Cat A: Path Error | Missing `01 - Curriculum/`. Replace with `[[B0 - The Deep Learner's Toolkit\|The Deep Learner's Toolkit]]`. |
| 10 | `Your Shelf.md` | 10 | `[[Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics\\|Phase -1 Bedrock Math]]` | `Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics\` | Cat A & B | Missing `01 - Curriculum/` AND escaped table pipe `\\|`. Replace with `[[BM - Bedrock Mathematics\|Phase -1 Bedrock Math]]`. |
| 11 | `Your Shelf.md` | 11 | `[[P1 - Learning How to Learn\\|P1]]` | `P1 - Learning How to Learn\` | Cat B: Escaped Pipe | Backslash before pipe treated literally. Replace with `[[P1 - Learning How to Learn\|P1]]`. |
| 12 | `Your Shelf.md` | 12 | `[[P3 - Math Prerequisites\\|P3]]` | `P3 - Math Prerequisites\` | Cat B: Escaped Pipe | Replace with `[[P3 - Math Prerequisites\|P3]]`. |
| 13 | `Your Shelf.md` | 12 | `[[10 - Math for CS\\|Block 10]]` | `10 - Math for CS\` | Cat B: Escaped Pipe | Replace with `[[10 - Math for CS\|Block 10]]`. |
| 14 | `Your Shelf.md` | 13 | `[[P5 - Tooling\\|P5]]` | `P5 - Tooling\` | Cat B: Escaped Pipe | Replace with `[[P5 - Tooling\|P5]]`. |
| 15 | `Your Shelf.md` | 13 | `[[06 - C Fluency\\|Block 6]]` | `06 - C Fluency\` | Cat B: Escaped Pipe | Replace with `[[06 - C Fluency\|Block 6]]`. |
| 16 | `Your Shelf.md` | 13 | `[[16 - Operating Systems\\|Block 16]]` | `16 - Operating Systems\` | Cat B: Escaped Pipe | Replace with `[[16 - Operating Systems\|Block 16]]`. |
| 17 | `Your Shelf.md` | 17 | `[[03 - Physics I\\|Block 3]]` | `03 - Physics I\` | Cat B: Escaped Pipe | Replace with `[[03 - Physics I\|Block 3]]`. |
| 18 | `Your Shelf.md` | 19 | `[[06 - C Fluency\\|Block 6]]` | `06 - C Fluency\` | Cat B: Escaped Pipe | Replace with `[[06 - C Fluency\|Block 6]]`. |
| 19 | `Your Shelf.md` | 20 | `[[06 - C Fluency\\|Block 6]]` | `06 - C Fluency\` | Cat B: Escaped Pipe | Replace with `[[06 - C Fluency\|Block 6]]`. |
| 20 | `Your Shelf.md` | 20 | `[[13 - Algorithms I\\|Block 13]]` | `13 - Algorithms I\` | Cat B: Escaped Pipe | Replace with `[[13 - Algorithms I\|Block 13]]`. |
| 21 | `Your Shelf.md` | 21 | `[[09 - Computer Systems\\|Block 9]]` | `09 - Computer Systems\` | Cat B: Escaped Pipe | Replace with `[[09 - Computer Systems\|Block 9]]`. |
| 22 | `Your Shelf.md` | 22 | `[[12 - Interpreters\\|Block 12]]` | `12 - Interpreters\` | Cat B: Escaped Pipe | Replace with `[[12 - Interpreters\|Block 12]]`. |
| 23 | `Your Shelf.md` | 23 | `[[13 - Algorithms I\\|Block 13]]` | `13 - Algorithms I\` | Cat B: Escaped Pipe | Replace with `[[13 - Algorithms I\|Block 13]]`. |
| 24 | `Your Shelf.md` | 24 | `[[24 - Theory of Computation\\|Block 24]]` | `24 - Theory of Computation\` | Cat B: Escaped Pipe | Replace with `[[24 - Theory of Computation\|Block 24]]`. |
| 25 | `Your Shelf.md` | 32 | `[[Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar\|BW Bedrock English]]` | `Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar` | Cat A: Path Error | Missing `01 - Curriculum/`. Replace with `[[BW - Bedrock English and Grammar\|BW Bedrock English]]`. |
| 26 | `Your Shelf.md` | 33 | `[[Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar\|BW Bedrock English]]` | `Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar` | Cat A: Path Error | Missing `01 - Curriculum/`. Replace with `[[BW - Bedrock English and Grammar\|BW Bedrock English]]`. |
| 27 | `08 - Templates/Daily Log Entry Template.md` | 14 | `[[{{block_id}}]]` | `{{block_id}}` | Cat C: Template Var | Uninstantiated template variable. Recommend wrapping in inline code `` `[[{{block_id}}]]` `` or Templater tag. |
| 28 | `08 - Templates/Project Build Spec Template.md` | 14 | `[[{{associated_block}}]]` | `{{associated_block}}` | Cat C: Template Var | Uninstantiated template variable. Recommend wrapping in inline code `` `[[{{associated_block}}]]` `` or Templater tag. |
| 29 | `08 - Templates/Zettelkasten Atomic Note Template.md` | 36 | `[[Related Note 1]]` | `Related Note 1` | Cat C: Template Var | Placeholder string. Recommend wrapping in inline code or formatting as descriptive example. |
| 30 | `08 - Templates/Zettelkasten Atomic Note Template.md` | 37 | `[[Related Note 2]]` | `Related Note 2` | Cat C: Template Var | Placeholder string. Recommend wrapping in inline code or formatting as descriptive example. |
| 31 | `ORIGINAL_REQUEST.md` | 46 | `[[wikilink]]` | `wikilink` | Cat D: Meta-Text | Literal string in user specification text. Recommend escaping with backticks `` `[[wikilink]]` ``. |

---

### 1.4 Detailed Orphan Notes Inventory

An orphan note is defined as a note with an in-degree of 0 (no incoming wikilinks from any other `.md` note in the vault). Currently, **18 notes** have an in-degree of 0:

| Note Path | Out-Degree | Note Role / Purpose | Why It Is Currently Orphaned | Recommended Permanent Inbound Link Location |
| :--- | :---: | :--- | :--- | :--- |
| `01 - Curriculum/Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit.md` | 3 | Bedrock syllabus | Inbound links from `00 - Dashboard`, `Checklist`, `log` all failed due to missing `01 - Curriculum/` path prefix | Fixed automatically when Category A links are repaired |
| `01 - Curriculum/Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics.md` | 0 | Bedrock syllabus | Inbound links from `00 - Dashboard`, `Checklist`, `log`, `Your Shelf` failed due to path prefix and `\\|` | Fixed automatically when Category A & B links are repaired |
| `01 - Curriculum/Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar.md` | 3 | Bedrock syllabus | Inbound links from `00 - Dashboard`, `Checklist`, `log`, `Your Shelf` failed due to path prefix | Fixed automatically when Category A links are repaired |
| `Checklist.md` | 45 | Master progress checklist | `00 - Dashboard.md` fails to link to `Checklist.md` | Link from `00 - Dashboard.md` header navigation block |
| `Your Shelf.md` | 4 | Master book library & tracker | `00 - Dashboard.md` fails to link to `Your Shelf.md` | Link from `00 - Dashboard.md` header navigation block & `how-i-study.md` |
| `01 - Curriculum/Baseline Gap Analysis and Audit Report.md` | 137 | Canonical curriculum audit | Completely unlinked from Dashboard and hubs | Link from `00 - Dashboard.md` under `## 📈 The Vault` (Curriculum line) |
| `02 - Notes/Hardware/Hardware Index.md` | 3 | Domain atomic notes index | `02 - Notes/` is entirely omitted from `00 - Dashboard.md` | Add `02 - Notes` section to `00 - Dashboard.md` & cross-link in `how-i-study.md` |
| `02 - Notes/Languages/Languages Index.md` | 6 | Domain atomic notes index | Omitted from Dashboard | Add to `00 - Dashboard.md` & `how-i-study.md` |
| `02 - Notes/Math/Math Index.md` | 10 | Domain atomic notes index | Omitted from Dashboard | Add to `00 - Dashboard.md` & `how-i-study.md` |
| `02 - Notes/Systems/Systems Index.md` | 4 | Domain atomic notes index | Omitted from Dashboard | Add to `00 - Dashboard.md` & `how-i-study.md` |
| `02 - Notes/Theory/Theory Index.md` | 3 | Domain atomic notes index | Omitted from Dashboard | Add to `00 - Dashboard.md` & `how-i-study.md` |
| `07 - Reference/Appendix E - Failure Modes.md` | 0 | Failure mode diagnostics | Completely unlinked from Dashboard and hubs | Link from `00 - Dashboard.md`, `Mindset Hub.md`, and `how-i-study.md` |
| `07 - Reference/Appendix F - Curated URLs.md` | 0 | Curated course & text URLs | Completely unlinked from Dashboard and hubs | Link from `00 - Dashboard.md` and `Checklist.md` |
| `08 - Templates/Block Note Template.md` | 0 | Note creation template | Template (excluded by acceptance criteria, but unlinked) | Link from `how-i-study.md` Section 6 ("Notes System Taxonomy") |
| `08 - Templates/Daily Log Entry Template.md` | 0 | Habit template | Template | Link from `log.md` header |
| `08 - Templates/Weekly Review Template.md` | 0 | Review template | Template | Link from `log.md` and `how-i-study.md` |
| `08 - Templates/Zettelkasten Atomic Note Template.md` | 0 | Note creation template | Template | Link from `how-i-study.md` Section 6 and `02 - Notes/` indices |
| `ORIGINAL_REQUEST.md` | 0 | Prompt / Task artifact | Prompt artifact located at vault root | Meta-artifact; link from `00 - Dashboard.md` or archive into `.agents/` |

---

### 1.5 Graph Topology, In-Degree, Out-Degree, and Sinks

#### Top 10 Most-Referenced Notes (Highest In-Degree)
1. `01 - Curriculum/Year 2 - Systems/09 - Computer Systems.md`: **31 incoming links** (Central system architectural keystone)
2. `01 - Curriculum/Year 2 - Systems/14 - Computer Architecture.md`: **24 incoming links**
3. `01 - Curriculum/Year 3 - Depth/16 - Operating Systems.md`: **23 incoming links**
4. `01 - Curriculum/Year 2 - Systems/11 - Linear Algebra.md`: **20 incoming links**
5. `01 - Curriculum/Year 1 - Fundamentals/06 - C Fluency.md`: **18 incoming links**
6. `01 - Curriculum/Year 1 - Fundamentals/08 - Physics II.md`: **18 incoming links**
7. `01 - Curriculum/Year 3 - Depth/17 - Software Construction.md`: **18 incoming links**
8. `01 - Curriculum/Year 1 - Fundamentals/07 - Multivariable Calculus.md`: **16 incoming links**
9. `01 - Curriculum/Year 1 - Fundamentals/04 - Nand2Tetris.md`: **15 incoming links**
10. `01 - Curriculum/Year 2 - Systems/10 - Math for CS.md`: **15 incoming links**

#### Top 5 Most-Referencing Notes (Highest Out-Degree)
1. `01 - Curriculum/Baseline Gap Analysis and Audit Report.md`: **137 outgoing links**
2. `03 - Papers/Paper Reading Hub.md`: **55 outgoing links**
3. `Checklist.md`: **45 outgoing links**
4. `01 - Curriculum/Specializations/Specializations Hub.md`: **23 outgoing links**
5. `01 - Curriculum/Specializations/Track 5 - Programming Languages and Compilers.md`: **14 outgoing links**

#### The 31 Dead-End Sink Notes (Out-Degree = 0)
31 core course files have an out-degree of 0:
- Phase 0: `P3 - Math Prerequisites`, `P4 - Programming On-Ramp`
- Year 1: `01 - CS61A`, `02 - Calculus I`, `03 - Physics I`, `04 - Nand2Tetris`, `05 - SICP`, `06 - C Fluency`, `07 - Multivariable Calculus`, `08 - Physics II`
- Year 2: `09 - Computer Systems`, `10 - Math for CS`, `11 - Linear Algebra`, `12 - Interpreters`, `13 - Algorithms I`, `14 - Computer Architecture`, `15 - Probability`
- Year 3: `16 - Operating Systems`, `17 - Software Construction`, `18 - Real Analysis`, `19 - Networking`, `20 - Algorithms II`, `21 - Databases`, `22 - Statistics`
- Year 4: `23 - Distributed Systems`, `24 - Theory of Computation`, `25 - Convex Optimization`, `27 - Intensive Cryptopals or TLA+`
- Year 5: `30 - Capstone`, `32 - Information Theory`
- Foundation: `BM - Bedrock Mathematics`

*Observation:* While incoming links to these courses are abundant, once a reader navigates to any core course syllabus, there are zero links to move forward, backward, or return to higher-level curriculum indices.

---

### 1.6 Navigation Hubs & Graph Reachability Gaps

#### Catalog of Vault Hubs (12 Identified)
1. `00 - Dashboard.md` (Top-level command center)
2. `01 - Curriculum/Specializations/Specializations Hub.md` (Gateway to Tracks 1–11)
3. `02 - Notes/Hardware/Hardware Index.md` (Topic hub for hardware)
4. `02 - Notes/Languages/Languages Index.md` (Topic hub for PL & compilers)
5. `02 - Notes/Math/Math Index.md` (Topic hub for mathematics)
6. `02 - Notes/Systems/Systems Index.md` (Topic hub for OS & architecture)
7. `02 - Notes/Theory/Theory Index.md` (Topic hub for algorithms & complexity)
8. `03 - Papers/Paper Reading Hub.md` (Gateway to 35 seminal papers)
9. `04 - Writing/Writing Hub.md` (Gateway to technical essays & writing habits)
10. `05 - Projects/Projects Hub.md` (Gateway to engineering builds)
11. `06 - Breadth/Breadth and Humanities Hub.md` (Gateway to HASS & language tracker)
12. `09 - Mindset & Habits/Mindset Hub.md` (Gateway to cognitive and behavioral protocols)

#### Reachability Analysis from `00 - Dashboard.md`
- **Reachable Notes from Dashboard:** 55 notes (64.71%)
- **Unreachable Notes from Dashboard:** 30 notes (35.29%)

The 30 unreachable notes from `00 - Dashboard.md` are:
1. `Checklist.md`
2. `Your Shelf.md`
3. `01 - Curriculum/Baseline Gap Analysis and Audit Report.md`
4. `01 - Curriculum/Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit.md`
5. `01 - Curriculum/Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics.md`
6. `01 - Curriculum/Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar.md`
7. `01 - Curriculum/Phase 0 - Prerequisites/P1 - Learning How to Learn.md`
8. `01 - Curriculum/Phase 0 - Prerequisites/P2 - Reading, Thinking, and Writing.md`
9. `01 - Curriculum/Phase 0 - Prerequisites/P3 - Math Prerequisites.md`
10. `01 - Curriculum/Phase 0 - Prerequisites/P4 - Programming On-Ramp.md`
11. `01 - Curriculum/Phase 0 - Prerequisites/P5 - Tooling.md`
12. `01 - Curriculum/Year 1 - Fundamentals/02 - Calculus I.md`
13. `01 - Curriculum/Year 1 - Fundamentals/03 - Physics I.md`
14. `01 - Curriculum/Year 4 - Specialization/26 - Specialization A1.md`
15. `01 - Curriculum/Year 4 - Specialization/28 - Specialization A2.md`
16. `01 - Curriculum/Year 4 - Specialization/29 - Specialization B1.md`
17. `01 - Curriculum/Year 5 - MEng/30 - Capstone.md`
18. `01 - Curriculum/Year 5 - MEng/31 - Specialization B2.md`
19. `02 - Notes/Hardware/Hardware Index.md`
20. `02 - Notes/Languages/Languages Index.md`
21. `02 - Notes/Math/Math Index.md`
22. `02 - Notes/Systems/Systems Index.md`
23. `02 - Notes/Theory/Theory Index.md`
24. `07 - Reference/Appendix E - Failure Modes.md`
25. `07 - Reference/Appendix F - Curated URLs.md`
26. `08 - Templates/Block Note Template.md`
27. `08 - Templates/Daily Log Entry Template.md`
28. `08 - Templates/Weekly Review Template.md`
29. `08 - Templates/Zettelkasten Atomic Note Template.md`
30. `ORIGINAL_REQUEST.md`

#### Reachability Analysis from ANY Hub (Union of all 12 Hubs)
Even if a user starts at ANY of the 12 hubs simultaneously, **23 notes** remain unreachable:
`Checklist.md`, `Your Shelf.md`, `Baseline Gap Analysis and Audit Report.md`, `B0`, `BM`, `BW`, `P1`, `P2`, `P4`, `P5`, `03 - Physics I`, `26 - Specialization A1`, `28 - Specialization A2`, `29 - Specialization B1`, `30 - Capstone`, `31 - Specialization B2`, `Appendix E`, `Appendix F`, the 4 unused templates, and `ORIGINAL_REQUEST.md`.

---

## 2. Logic Chain

The step-by-step causal chain linking observations to final conclusions:

### Step 1: Obsidian Path Resolution Mechanics Cause 12 Broken Links
- *Observation:* `00 - Dashboard.md`, `Checklist.md`, `log.md`, and `Your Shelf.md` reference `Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics` without `01 - Curriculum/`.
- *Mechanism:* In Obsidian, any wikilink containing a forward slash (`/`) is resolved either from the vault root or relative to the source note's directory. Since no directory named `Phase -1 - Bedrock Foundations` exists at the root of the vault (it is located at `01 - Curriculum/Phase -1 - Bedrock Foundations`), the target path fails to resolve.
- *Inference:* Because all 85 file basenames in the vault are globally unique, Obsidian's shortest-path resolver resolves bare basenames without folders. Using `[[BM - Bedrock Mathematics|Bedrock Math]]` (or prepending `01 - Curriculum/`) immediately restores resolution for all 12 instances.

### Step 2: Markdown Table Syntax Interference in `Your Shelf.md` Causes 14 Broken Links
- *Observation:* In `Your Shelf.md` lines 10–24, links inside the table were written with an escaped pipe: `[[Target\|Alias]]`.
- *Mechanism:* The author escaped the pipe to prevent standard markdown table splitters from breaking columns. However, Obsidian's internal wikilink tokenizer expects unescaped `|` inside `[[...]]` delimiters. As a result, the wikilink parser ingests the trailing backslash as part of the filename (`Target\`), looking for a non-existent file ending in a literal backslash.
- *Inference:* Removing the backslash so the syntax becomes `[[Target|Alias]]` resolves all 14 broken links instantly while rendering cleanly within Obsidian tables.

### Step 3: Unlinked Master Tracking Subsystem Isolates Foundational Curriculum Blocks
- *Observation:* `Checklist.md` contains 45 valid outgoing links pointing to all 32 curriculum blocks, Phase 0, and Bedrock Foundations. However, `Checklist.md` itself has an in-degree of 0 (it is not linked from `00 - Dashboard.md`).
- *Mechanism:* Notes such as `P1`, `P2`, `P4`, `P5`, `03 - Physics I`, `26`, `28`, `29`, `30`, and `31` receive inbound links from `Checklist.md` (and `Baseline Gap Analysis`), but receive zero inbound links from any hub currently reachable from Dashboard.
- *Inference:* The graph is split into two disconnected clusters. Adding a single direct link from `00 - Dashboard.md` to `Checklist.md` immediately connects the entire foundational sequence into the Dashboard reachability tree, rescuing 12 stranded curriculum blocks.

### Step 4: Complete Omission of `02 - Notes/` and `07 - Reference/` from Dashboard
- *Observation:* `00 - Dashboard.md` lines 43–50 (`## 📈 The Vault`) list `Mindset & Habits`, `Curriculum`, `Paper Summaries`, `Writing Repository`, `Project Specs`, and `Breadth & Languages`. It completely omits `02 - Notes` (the 5 topic indices) and `07 - Reference` (Appendices E & F).
- *Mechanism:* Because no other note in the vault links to `Hardware Index.md`, `Languages Index.md`, `Math Index.md`, `Systems Index.md`, `Theory Index.md`, `Appendix E`, or `Appendix F`, all 7 notes exist as isolated orphan nodes.
- *Inference:* Adding `02 - Notes` (Topic Indices) and `07 - Reference` (Appendices) to `00 - Dashboard.md` eliminates 7 of the 10 domain orphan notes and links their outgoing subgraphs into the global graph.

### Step 5: Sink Nodes in Curriculum Architecture
- *Observation:* 31 out of 32 core curriculum course notes have an out-degree of 0.
- *Mechanism:* When the course notes were originally scaffolded, they contained no navigation breadcrumbs (e.g. `Back to Dashboard`, `Checklist`, or prerequisite/sequencing links).
- *Inference:* While not strictly "broken", this creates dead-end UX and weak graph centrality. Implementing standard bidirectional links (e.g., breadcrumb to Dashboard/Checklist, or `Prerequisites: [[Block X]]`, `Next: [[Block Y]]`) transforms these sinks into cohesive graph traversals.

---

## 3. Caveats

1. **Linux Filesystem Case Sensitivity:** All testing and scans were performed in a Linux environment (`Ubuntu/Debian` on ext4). Obsidian on macOS or Windows may appear more forgiving with casing, but case-exact compliance is strictly required for cross-platform repository portability.
2. **Template Wikilinks:** The 4 broken links in `08 - Templates/` (`{{block_id}}`, `{{associated_block}}`, `Related Note 1`, `Related Note 2`) are standard template variables and placeholders. Under the Acceptance Criteria ("excluding templates"), they do not constitute curriculum defects; however, in Obsidian's visual Graph View, they will display as unresolved dangling nodes unless escaped with code spans or formatted as Templater tags.
3. **`ORIGINAL_REQUEST.md` at Vault Root:** This file exists at `/home/noblixy/The Noblett Repository/ORIGINAL_REQUEST.md` and contains the literal text `[[wikilink]]`. This file is an agent orchestrator artifact duplicated from `.agents/ORIGINAL_REQUEST.md`. It is not part of the educational curriculum, but technically counts as an orphan markdown file inside the vault root.
4. **Scope Boundaries:** Explorer 1 operated strictly in read-only mode. No edits, file creations in vault source folders, or code patches were applied to vault content.

---

## 4. Conclusion & Actionable Recommendations

### 4.1 Summary Verdict
The vault's graph topology is substantially intact (94.33% valid links), and all 85 note basenames are globally unique. The link defects and orphan nodes are not distributed randomly; they stem from **three highly localized formatting patterns** (Bedrock path prefix omission, table pipe escaping in `Your Shelf.md`, and missing top-level links in `00 - Dashboard.md`).

Fixing these three specific areas will:
1. Eliminate 100% of broken wikilinks across real curriculum notes (achieving 0 dead wikilinks).
2. Eliminate 100% of non-template orphan notes (achieving 0 orphans per Acceptance Criteria).
3. Increase `00 - Dashboard.md` graph reachability from 64.7% to 100% of non-template vault notes.

---

### 4.2 Priority Remediation Action Plan

#### Task 1: Repair Bedrock Foundation Path Errors (12 Link Corrections)
Replace `[[Phase -1 - Bedrock Foundations/<Note>|<Alias>]]` with simple basenames `[[<Note>|<Alias>]]`:
- `00 - Dashboard.md` (lines 32–34):
  - Change `[[Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics|Bedrock Math]]` to `[[BM - Bedrock Mathematics|Bedrock Math]]` and remove surrounding backticks.
  - Change `[[Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar|Bedrock English]]` to `[[BW - Bedrock English and Grammar|Bedrock English]]` and remove surrounding backticks.
  - Change `[[Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit|Deep Learner's Toolkit]]` to `[[B0 - The Deep Learner's Toolkit|Deep Learner's Toolkit]]` and remove surrounding backticks.
- `Checklist.md` (lines 19–21):
  - Change `[[Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit|B0]]` to `[[B0 - The Deep Learner's Toolkit|B0]]`.
  - Change `[[Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics|BM]]` to `[[BM - Bedrock Mathematics|BM]]`.
  - Change `[[Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar|BW]]` to `[[BW - Bedrock English and Grammar|BW]]`.
- `log.md` (lines 7–8):
  - Change to `[[BM - Bedrock Mathematics|Bedrock Math (Arithmetic)]]`.
  - Change to `[[BW - Bedrock English and Grammar|Bedrock English (Sentence Architecture)]]`.
  - Change to `[[B0 - The Deep Learner's Toolkit|The Deep Learner's Toolkit]]`.
- `Your Shelf.md` (lines 10, 32, 33):
  - Change line 10 to `[[BM - Bedrock Mathematics|Phase -1 Bedrock Math]]`.
  - Change lines 32 & 33 to `[[BW - Bedrock English and Grammar|BW Bedrock English]]`.

#### Task 2: Remove Escaped Pipes in `Your Shelf.md` (14 Link Corrections)
In `Your Shelf.md` table lines 10–24, remove the backslash before the pipe in all wikilinks:
- Line 11: `[[P1 - Learning How to Learn|P1]]`
- Line 12: `[[P3 - Math Prerequisites|P3]]`, `[[10 - Math for CS|Block 10]]`
- Line 13: `[[P5 - Tooling|P5]]`, `[[06 - C Fluency|Block 6]]`, `[[16 - Operating Systems|Block 16]]`
- Line 17: `[[03 - Physics I|Block 3]]`
- Line 19: `[[06 - C Fluency|Block 6]]`
- Line 20: `[[06 - C Fluency|Block 6]]`, `[[13 - Algorithms I|Block 13]]`
- Line 21: `[[09 - Computer Systems|Block 9]]`
- Line 22: `[[12 - Interpreters|Block 12]]`
- Line 23: `[[13 - Algorithms I|Block 13]]`
- Line 24: `[[24 - Theory of Computation|Block 24]]`

#### Task 3: Enhance `00 - Dashboard.md` Navigation (Rescues 10 Orphan Notes & Connects Graph)
Update `00 - Dashboard.md` to include:
1. In the header blockquotes (lines 3–6):
   ```markdown
   > - **Daily Study Log:** [[log.md]]
   > - **Living Study Manifesto:** [[how-i-study.md]]
   > - **Telemetry Log:** [[Telemetry Log.md]]
   > - **Degree Progress Checklist:** [[Checklist.md]]
   > - **Book Acquisition Tracker:** [[Your Shelf.md]]
   ```
2. Under `## 📈 The Vault` (lines 43–50):
   ```markdown
   - 🧠 **Mindset & Habits**: [[09 - Mindset & Habits/Mindset Hub|Mindset Hub]]
   - 📑 **Curriculum**: [[01 - Curriculum/Baseline Gap Analysis and Audit Report|Curriculum Audit & Gap Report]] · [[01 - Curriculum/Specializations/Specializations Hub|Specializations Hub]]
   - 📓 **Topic Notes**: [[02 - Notes/Hardware/Hardware Index|Hardware]] · [[02 - Notes/Languages/Languages Index|Languages]] · [[02 - Notes/Math/Math Index|Math]] · [[02 - Notes/Systems/Systems Index|Systems]] · [[02 - Notes/Theory/Theory Index|Theory]]
   - 📄 **Paper Summaries**: [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] (Three-pass method)
   - ✍️ **Writing Repository**: [[04 - Writing/Writing Hub|Writing Hub]] (Daily 500 words, Franklin copywork & technical essays)
   - 🛠️ **Project Specs & Lab Builds**: [[05 - Projects/Projects Hub|Projects Hub]]
   - 🌍 **Breadth & Languages**: [[06 - Breadth/Breadth and Humanities Hub|Breadth Hub]]
   - 📚 **Reference & Appendices**: [[07 - Reference/Appendix E - Failure Modes|Appendix E (Failure Modes)]] · [[07 - Reference/Appendix F - Curated URLs|Appendix F (Curated URLs)]]
   ```

#### Task 4: Template Placeholders & Root Prompt Clean-up
1. In `08 - Templates/Daily Log Entry Template.md` and `Project Build Spec Template.md`, wrap `[[{{block_id}}]]` and `[[{{associated_block}}]]` in code spans `` `[[{{block_id}}]]` `` or format as Templater syntax `<% tp.file.title %>`.
2. In `08 - Templates/Zettelkasten Atomic Note Template.md`, change `[[Related Note 1]]` and `[[Related Note 2]]` to code spans `` `[[Related Note 1]]` ``.
3. In `ORIGINAL_REQUEST.md` line 46, wrap `` `[[wikilink]]` `` in code spans so automated test parsers do not evaluate it as a broken link.
4. Link `Block Note Template` and `Zettelkasten Atomic Note Template` in `how-i-study.md` Section 6, and link `Daily Log Entry Template` and `Weekly Review Template` in `log.md`.

#### Task 5: Address Curriculum Block Sinks
In subsequent authoring passes, add navigation links at the top or bottom of each of the 32 course blocks:
- Breadcrumb header: `[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]]`
- Sequential navigation footer: `[[Previous Block]] ← Overview → [[Next Block]]`

---

## 5. Verification Method

### 5.1 Programmatic Graph Verification Command
An independent agent or reviewer can verify the findings by running the survey script developed during this audit:
```bash
python3 /home/noblixy/The\ Noblett\ Repository/.agents/explorer_survey_1/survey.py
```
Expected output under current vault state:
- `Total vault files: 87, MD files: 85`
- `Total wikilinks: 547`
- `Resolved wikilinks: 516`
- `Unresolved/Dead wikilinks: 31`
- `Orphan notes: 18`

### 5.2 E2E Curriculum Test Suite Command
Run the authoritative test suite from vault root:
```bash
python3 .agents/test_suite/test_curriculum.py
```
Under current vault state, Tier 2 Test `T2.1: Vault-Wide Wikilink Integrity Validator` fails due to `ORIGINAL_REQUEST.md:46 -> [[wikilink]]`.

### 5.3 Post-Remediation Invalidation Conditions
The recommendations of this report will be verified and considered successful when:
1. `test_curriculum.py` runs with `Total Tests Run: 19 | Passed: 19 | Failed: 0` and overall verdict `[GREEN]`.
2. A strict parser checking all `.md` files outside `.agents/` finds exactly **0 unresolved wikilinks**.
3. A strict inbound link scanner confirms that every `.md` file (excluding `08 - Templates/` and prompt artifacts) has **at least 1 valid incoming link**.
4. A breadth-first search starting at `00 - Dashboard.md` reaches **100% of non-template markdown files**.
