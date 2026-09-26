# Handoff Report: Formatting & Structural Consistency Explorer (Survey 2)

**Author:** Explorer 2 (Formatting & Structural Consistency Explorer)  
**Date:** 2026-09-25T10:17:10Z  
**Working Directory:** `/home/noblixy/The Noblett Repository/.agents/explorer_survey_2`  
**Target Vault:** `/home/noblixy/The Noblett Repository` (excluding `.agents/`, `.git/`, `.obsidian/`)  
**Scope:** Strictly read-only investigation across all 85 markdown files in the vault.

---

## Executive Summary & Survey Metrics

| Survey Dimension | Census Metric | Status / Verdict |
| :--- | :--- | :--- |
| **Total Markdown Files Audited** | 85 files | 100% complete census across 10 directories |
| **Files with YAML Frontmatter** | 64 files (75.3%) | 44 curriculum blocks, 11 tracks, 8 templates, 1 hub (`Specializations Hub`) |
| **Files lacking Frontmatter** | 21 files (24.7%) | 11 hubs/indexes, 5 root files, 2 reference files, 2 templates, 1 audit report |
| **Header Hierarchy Level Skips** | 0 instances | Clean across all files (no H1 $\to$ H3, H2 $\to$ H4, etc.) |
| **Notes with Multiple H1s** | 1 instance | `ORIGINAL_REQUEST.md` (lines 1 & 5) |
| **Notes Starting with Non-H1** | 1 instance | `08 - Templates/Daily Log Entry Template.md` (starts with H2 `## {{date}}`) |
| **Header / Frontmatter Desyncs** | 2 critical notes | `31 - Specialization B2.md` and `32 - Information Theory.md` |
| **Template-to-Instance Mismatch**| 1 template | `08 - Templates/Block Note Template.md` has divergent H2 headings |
| **List Indentation Anomaly** | 17 files (158 lines) | Odd-space indents (3/5 spaces) from sublists under numbered items |
| **List Bullet Marker Mix** | 0 instances | Uniformly uses hyphen `-` across all 85 files |
| **Tab / Space Indentation Mix** | 0 instances | 0 files contain mixed tabs and spaces |
| **Malformed Checkboxes** | 0 instances | All task boxes strictly formatted as `- [ ]` |
| **Markdown Tables Detected** | 19 authentic tables | 8 files contain tables; 18 tables valid, 1 severely malformed |
| **Malformed Tables** | 1 instance | `Telemetry Log.md` lines 7–10 (table header immediately followed by list items) |
| **Raw HTML Tags** | 35 instances | `03 - Papers/Paper Reading Hub.md` (35 `<br>` tags in table cells) |
| **Fenced Code Blocks** | 33 blocks | 0 unclosed blocks; 18 bare code blocks lack language identifier (MD040) |
| **LaTeX Math Display Blocks** | 208 blocks | Across 27 files; 0 unclosed fences, 0 unmatched environments |
| **LaTeX Math Inline Instances** | 2,190 instances | 0 unclosed dollars; 0 leading/trailing space defects inside delimiters |
| **Backticked Wikilink Artifacts**| 95 lines (16 files) | `\`[[...]]\`` used instead of interactive `[[...]]`, breaking Obsidian graph |

---

## 1. Observation

### 1.1 Header Hierarchy Observations

1. **Header Level Continuity:**
   A programmatic scan inspecting every heading transition across all 85 files revealed 0 instances of skipped header levels (e.g., `#` directly to `###`, or `##` to `####`).

2. **Multiple H1 Headings:**
   - Exact file: `ORIGINAL_REQUEST.md`
   - Line 1: `# Original User Request`
   - Line 5: `# Teamwork Project Prompt`
   - All other 84 files contain at most one H1.

3. **Non-H1 File Opening:**
   - Exact file: `08 - Templates/Daily Log Entry Template.md`
   - Line 1: `## {{date}}` (starts at H2 because it is an append-snippet template intended for inclusion in `log.md`).

4. **Curriculum Block H1 Naming Convention:**
   In 42 of 44 curriculum block notes, H1 follows the format `# <block_id> — <title>`.
   - `01 - Curriculum/Year 1 - Fundamentals/01 - CS61A.md:12`: `# Block 1 — Programming and Abstraction (Berkeley CS61A)`
   - `01 - Curriculum/Year 4 - Specialization/26 - Specialization A1.md:12`: `# Block 26 — Specialization Track A — Course 1`
   - `01 - Curriculum/Year 4 - Specialization/30 - Capstone.md:12`: `# Block 30 — Capstone Project & Thesis (MEng Year)`

5. **Critical Header Anomaly in Blocks 31 & 32:**
   - File: `01 - Curriculum/Year 5 - MEng/31 - Specialization B2.md`
     - Line 2: `block_id: "Specialization B2"` (Frontmatter)
     - Line 12: `# Specialization B2 — Specialization Track B — Course 2`
     - *Observation:* Should be `block_id: "Block 31"` and `# Block 31 — Specialization Track B — Course 2`.
   - File: `01 - Curriculum/Year 5 - MEng/32 - Information Theory.md`
     - Line 2: `block_id: "Information Theory"` (Frontmatter)
     - Line 3: `title: "Information Theory, Inference, and Learning Algorithms"`
     - Line 12: `# Information Theory — Information Theory, Inference, and Learning Algorithms`
     - *Observation:* Produces a stutter title because `block_id` was set to `"Information Theory"` instead of `"Block 32"`. Should be `# Block 32 — Information Theory, Inference, and Learning Algorithms`.

6. **Specialization Track H1 Delimiter Convention:**
   In all 11 specialization tracks (`Track 1` to `Track 11`), H1 uses a colon rather than an em-dash:
   - File: `01 - Curriculum/Specializations/Track 1 - AI and Machine Learning.md:11`: `# Track 1: AI and Machine Learning`
   - Whereas the filename uses spaced hyphens: `Track 1 - AI and Machine Learning.md`.

7. **Template-to-Instance H2 Heading Mismatch:**
   File: `08 - Templates/Block Note Template.md` specifies:
   - Line 16: `## 📖 Primary Curriculum & Syllabus`
   - Line 41: `## 📝 Study Notes & Problem Sets`
   Whereas all 35 actual core course files in `Year 1` through `Year 5` and the 3 bridge syllabi use:
   - `## 📖 Primary Syllabus & Core Content`
   - `## 📝 Study Notes, Psets & Proofs`

8. **Topic Note Index Heading Inconsistency:**
   In `02 - Notes/`:
   - `02 - Notes/Math/Math Index.md`: Line 6 is `## Areas` and Line 13 is `## Principles for Math Notes` (lacks `## Reference Courses`).
   - `02 - Notes/Systems/Systems Index.md`: Line 6 is `## Core Focus Areas` and Line 13 is `## Reference Courses`.
   - `02 - Notes/Theory/Theory Index.md`: Line 6 is `## Core Areas` and Line 13 is `## Reference Courses`.
   - `02 - Notes/Hardware/Hardware Index.md`: Line 6 is `## Core Areas` and Line 13 is `## Reference Courses`.
   - `02 - Notes/Languages/Languages Index.md`: Line 6 is `## Core Areas` and Line 13 is `## Reference Courses`.

---

### 1.2 YAML Frontmatter Observations

1. **Frontmatter Census:**
   - 64 files contain valid YAML frontmatter blocks delimited by `---`.
   - 21 files have 0 frontmatter.
   - YAML syntax errors: 0 across all files.

2. **Files Lacking Frontmatter (21 Notes):**
   - **Vault Hubs & Indexes (11 notes):**
     - `00 - Dashboard.md`
     - `02 - Notes/Hardware/Hardware Index.md`
     - `02 - Notes/Languages/Languages Index.md`
     - `02 - Notes/Math/Math Index.md`
     - `02 - Notes/Systems/Systems Index.md`
     - `02 - Notes/Theory/Theory Index.md`
     - `03 - Papers/Paper Reading Hub.md`
     - `04 - Writing/Writing Hub.md`
     - `05 - Projects/Projects Hub.md`
     - `06 - Breadth/Breadth and Humanities Hub.md`
     - `09 - Mindset & Habits/Mindset Hub.md`
     *(Note: `01 - Curriculum/Specializations/Specializations Hub.md` DOES have frontmatter: `title`, `tags`)*.
   - **Root Notes (5 notes):**
     - `Checklist.md`
     - `ORIGINAL_REQUEST.md`
     - `Your Shelf.md`
     - `how-i-study.md`
     - `log.md`
   - **Reference Notes (2 notes):**
     - `07 - Reference/Appendix E - Failure Modes.md`
     - `07 - Reference/Appendix F - Curated URLs.md`
   - **Curriculum Audit Document (1 note):**
     - `01 - Curriculum/Baseline Gap Analysis and Audit Report.md`
   - **Templates (2 notes):**
     - `08 - Templates/Daily Log Entry Template.md`
     - `08 - Templates/Zettelkasten Atomic Note Template.md` (uses inline bold metadata: `**Date:**`, `**Tags:**`, `**Connections:**`).

3. **Frontmatter Field Schemas in Curriculum Blocks (44 Notes):**
   All 44 notes have exactly 10 keys:
   `['block_id', 'date_completed', 'date_started', 'hours_actual', 'hours_estimate', 'milestone', 'primary_resource', 'status', 'term', 'title']`
   - In 42 notes, `status` is `"not-started"` (or `"in-progress"` in `B0`).
   - In 33 notes, `block_id` is `"Block N"`.
   - In Phase -1 and Phase 0, `block_id` is `"B0"`, `"BM"`, `"BW"`, `"P1"`..`"P5"`.
   - In `31 - Specialization B2.md`, `block_id` is `"Specialization B2"`.
   - In `32 - Information Theory.md`, `block_id` is `"Information Theory"`.

4. **Frontmatter Field Schemas in Specialization Tracks (11 Notes):**
   All 11 notes have exactly 7 keys:
   `['aliases', 'prerequisites', 'status', 'target_profile', 'term', 'title', 'track_id']`
   - `status`: `"planned"` (Differs from `"not-started"` in curriculum blocks).
   - `prerequisites`: Represented as a single quoted comma-separated string rather than a YAML sequence.
     - Example from `Track 1 - AI and Machine Learning.md:6`:
       `prerequisites: "[[01 - CS61A]], [[07 - Multivariable Calculus]], [[11 - Linear Algebra]], [[13 - Algorithms I]], [[15 - Probability]], [[25 - Convex Optimization]]"`
   - `aliases`: Formatted as an unquoted flow sequence containing hyphenated titles.
     - Example from `Track 1:8`: `aliases: [Track 1 - AI and Machine Learning, Track 1 - Artificial Intelligence and Machine Learning]`.

5. **Frontmatter in `Telemetry Log.md`:**
   - Lines 1–3:
     ```yaml
     ---
     type: telemetry
     ---
     ```
   - Only a single key (`type`), lacking `title`, `date`, or standard properties.

---

### 1.3 List Formatting Observations

1. **Tabs vs. Spaces:**
   Across all 85 files, 0 lines contain mixed tabs and spaces. 0 lines use tab characters for list indentation.

2. **Bullet Marker Consistency:**
   Every single unordered list across the entire 85 notes uses the hyphen (`-`). Not a single asterisk (`*`) or plus (`+`) is used as an unordered list bullet marker.

3. **Checkbox Syntax:**
   All 464 checkboxes across 51 files strictly conform to the markdown task format `- [ ]` (or `- [x]`). 0 malformed checkbox brackets exist.

4. **Indentation Inconsistency (The 3-Space / 5-Space Defect):**
   While 68 files strictly use 2-space or 4-space indentation, exactly 17 files contain odd-space indentations (3 spaces and 5 spaces) across 158 lines.
   - Example 1: `01 - Curriculum/Year 3 - Depth/16 - Operating Systems.md`:
     - Line 66: `1. **Soundness ($a \to b \implies V(a) < V(b)$):**`
     - Line 68: `   - Base case ($k=1$):` (3 spaces)
     - Line 69: `     - If $a$ and $b$ occur on the same process...` (5 spaces)
   - Example 2: `01 - Curriculum/Baseline Gap Analysis and Audit Report.md`:
     - Line 24: `2. **The Missing Physical & Continuous Foundation:** ...`
     - Line 25: `   - **Zero linear circuit theory or analog electronics:** ...` (3 spaces)
     - Line 191: `  4. *Fourier Representations:*` (2 spaces)
     - Line 192: `     - Continuous-Time Fourier Series (CTFS)...` (5 spaces)
   - Example 3: `01 - Curriculum/Year 4 - Specialization/23 - Distributed Systems.md`:
     - Line 62: `1. **Quorum Intersection Property:**`
     - Line 63: `   - *Proof*: Electing a leader requires a majority vote...` (3 spaces)
   - Affected files (17 files):
     `Baseline Gap Analysis and Audit Report.md`, `BM - Bedrock Mathematics.md`, `Specializations Hub.md`, `04a - Differential Equations Bridge.md`, `08a - Circuits and Electronics Bridge.md`, `10 - Math for CS.md`, `13 - Algorithms I.md`, `15a - Signals and Systems Bridge.md`, `16 - Operating Systems.md`, `17 - Software Construction.md`, `20 - Algorithms II.md`, `21 - Databases.md`, `22 - Statistics.md`, `23 - Distributed Systems.md`, `24 - Theory of Computation.md`, `30 - Capstone.md`, `32 - Information Theory.md`.

---

### 1.4 Markdown Table Observations

1. **Table Inventory:**
   Exactly 19 authentic tables exist across 8 files in the vault:
   - `01 - Curriculum/Baseline Gap Analysis and Audit Report.md` (4 tables: lines 44, 72, 111, 303)
   - `01 - Curriculum/Specializations/Specializations Hub.md` (2 tables: lines 37, 50)
   - `01 - Curriculum/Year 2 - Systems/10 - Math for CS.md` (1 table: line 57)
   - `03 - Papers/Paper Reading Hub.md` (7 tables: lines 28, 40, 52, 64, 76, 88, 100)
   - `07 - Reference/Appendix F - Curated URLs.md` (1 table: line 3)
   - `Telemetry Log.md` (1 table: line 7)
   - `Your Shelf.md` (1 table: line 8)
   - `how-i-study.md` (2 tables: lines 42, 106)

2. **Critical Schema Defect in `Telemetry Log.md`:**
   - File: `Telemetry Log.md`
   - Lines 7–10:
     ```markdown
     | Date | Time | Event | Data |
     | ---- | ---- | ----- | ---- |
     - TELEMETRY: 2026-09-25 | 06:15 AM | Wake Up
     - TELEMETRY: 2026-09-25 | 05:03 PM | Left Work
     ```
   - *Observation:* Lines 7–8 define a 4-column markdown table header. Lines 9–10 are bulleted list items that split values with pipes.
   - *Impact:* This completely breaks table rendering in Obsidian (renders as an empty/corrupted table header followed by unformatted list items).
   - *Cross-Reference with `00 - Dashboard.md`:* The Dataview query in `00 - Dashboard.md:18` queries `FLATTEN file.lists AS item WHERE contains(item.text, "TELEMETRY:")`. It expects list items, NOT table rows! The table header lines 7–8 are orphaned artifacts.

3. **Outer Pipe Consistency:**
   In 18 of the 19 tables, 100% of header rows, separator rows, and data rows have consistent leading and trailing outer pipes (`| ... |`).

4. **Visual Column Alignment (Monospace Raggedness):**
   In 18 of the 19 tables, column cells are unpadded (cells have variable widths, pipes do not align vertically in monospace plain text/source view). While standard Markdown and Obsidian parse this correctly, it violates clean table alignment standards in source editing.

---

### 1.5 Raw HTML, Broken Rendering Artifacts, Code & Math Blocks

1. **Raw HTML Usage:**
   - Across the entire vault, only 1 file contains raw HTML tags: `03 - Papers/Paper Reading Hub.md`.
   - It contains 35 instances of the `<br>` tag across lines 30–106.
   - Example (`Paper Reading Hub.md:30`):
     ```markdown
     | 1 | **"The UNIX Time-Sharing System"**<br>Dennis M. Ritchie & Ken Thompson | 1974 | *Communications of the ACM* | ...
     ```
   - *Observation:* `<br>` was used inside table cells to stack paper titles and authors in a single column without splitting into two separate columns.

2. **Fenced Code Blocks & MD040 (Bare Code Blocks):**
   - 33 fenced code blocks exist across the vault.
   - 0 unclosed code blocks.
   - **18 code blocks lack language identifiers** (bare ` ``` `):
     - All 11 Specialization Tracks contain an untagged ASCII architecture diagram in their Capstone Build section:
       - `Track 1:155`, `Track 2:145`, `Track 3:147`, `Track 4:150`, `Track 5:148`, `Track 6:148`, `Track 7:153`, `Track 8:149`, `Track 9:145`, `Track 10:157`, `Track 11:150`
     - `01 - Curriculum/Baseline Gap Analysis and Audit Report.md`: lines 93, 155, 237
     - `01 - Curriculum/Specializations/Specializations Hub.md`: line 19
     - `01 - Curriculum/Year 3 - Depth/16 - Operating Systems.md`: line 120
     - `01 - Curriculum/Year 4 - Specialization/24 - Theory of Computation.md`: line 63
     - `03 - Papers/Paper Reading Hub.md`: line 112

3. **LaTeX Math Block Integrity:**
   - 208 display math blocks (`$$...$$`) across 27 files.
   - 2,190 inline math instances (`$...$`).
   - 0 unclosed math delimiters.
   - 0 unmatched LaTeX environments (`\begin{...}` / `\end{...}`).
   - 0 math instances with leading or trailing space inside the dollar delimiters (`$ x$` or `$x $`).

4. **Severe Rendering Artifact: Backticked Wikilinks `\`[[...]]\``:**
   Across 16 files, **95 lines contain wikilinks enclosed in backticks** (inline code formatting).
   - In Obsidian, enclosing a wikilink in backticks renders it as literal inline code (`<code>[[Link]]</code>`). It **disables interactive hyperlink navigation** and **prevents the Obsidian graph indexer from recognizing the relationship**.
   - Breakdown of the 95 lines across 16 files:
     - `01 - Curriculum/Baseline Gap Analysis and Audit Report.md`: 54 lines
     - `00 - Dashboard.md`: 6 lines (lines 32, 33, 34, 37, 38, 39)
     - `01 - Curriculum/Specializations/Specializations Hub.md`: 5 lines
     - `01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md`: 5 lines
     - `01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md`: 4 lines
     - `01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md`: 3 lines
     - `01 - Curriculum/Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit.md`: 3 lines
     - `01 - Curriculum/Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar.md`: 3 lines
     - `01 - Curriculum/Phase 0 - Prerequisites/P2 - Reading, Thinking, and Writing.md`: 3 lines
     - `how-i-study.md`: 3 lines (lines 14, 18, 32)
     - `01 - Curriculum/Phase 0 - Prerequisites/P1 - Learning How to Learn.md`: 1 line
     - `03 - Papers/Paper Reading Hub.md`: 1 line (line 8)
     - `04 - Writing/Writing Hub.md`: 1 line (line 7)
     - `05 - Projects/Projects Hub.md`: 1 line (line 7)
     - `Checklist.md`: 1 line (line 14)
     - `ORIGINAL_REQUEST.md`: 1 line (line 46)

---

### 1.6 Mathematical Proofs & Q.E.D. Conventions

1. **Proof Section Inventory:**
   - Exactly 41 curriculum notes contain Section 5: `## 📝 Study Notes, Psets & Proofs`.
   - Across these sections, 100 formal proof or theorem elements are present.
2. **Q.E.D. Marker Inconsistency:**
   - Where a Q.E.D. symbol is used, it uniformly uses `$\blacksquare$` (31 occurrences across 16 notes).
   - However, in several mathematically rigorous courses, formal proofs terminate abruptly with no Q.E.D. marker at all:
     - `01 - Curriculum/Year 3 - Depth/22 - Statistics.md`: 8 proofs, 0 Q.E.D. markers.
     - `01 - Curriculum/Year 4 - Specialization/25 - Convex Optimization.md`: 6 proofs, 0 Q.E.D. markers.
3. **Heading Style Variation:**
   - Some courses use markdown subheadings: `### Theorem 1 (Spectral Theorem)` followed by `#### Proof:` (e.g. `11 - Linear Algebra.md`, `18 - Real Analysis.md`).
   - Other courses format proofs as bold bullet points: `- **Formal Proof of FLP Impossibility:**` (e.g. `23 - Distributed Systems.md`).

---

## 2. Logic Chain

```
Observation 1.1.5 (Block 31/32 IDs)
       │
       ▼
[Deduction L1]: When Year 5 MEng blocks were authored, automated agents populated `block_id` with course titles ("Specialization B2", "Information Theory") instead of standard sequential identifiers ("Block 31", "Block 32").
       │
       ▼
[Deduction L2]: Block notes generate their H1 headers by concatenating `<block_id> — <title>`. In Block 32, this caused the stutter title `# Information Theory — Information Theory, Inference, and Learning Algorithms`.
```

```
Observation 1.2.2 & 1.2.4 (Frontmatter Inconsistencies)
       │
       ▼
[Deduction L3]: Specializations Hub was created with YAML frontmatter, while all other vault Hubs (00 - Dashboard, Paper Reading Hub, Writing Hub, Projects Hub, Breadth Hub, Mindset Hub, and five 02 - Notes indexes) were authored without YAML.
       │
       ▼
[Deduction L4]: Specialization tracks use `status: planned` while curriculum blocks use `status: not-started`. Additionally, track prerequisites are stored as a flat string `prerequisites: "[[...]]"` rather than a YAML list, impeding programmatic querying via Dataview.
```

```
Observation 1.3.4 (Odd-space Indentation)
       │
       ▼
[Deduction L5]: In 17 files, agents aligned sub-bullets to match the 3-character visual column of numbered list items (`1. ` $\to$ 3 spaces, `  4. ` $\to$ 5 spaces). While valid in CommonMark loose parsing, this triggers markdownlint MD005/MD007 errors and conflicts with the 2-space standard used across the other 68 files.
```

```
Observation 1.4.2 & Dashboard Query (Telemetry Log Defect)
       │
       ▼
[Deduction L6]: An Apple Shortcut automation appends raw telemetry log lines (`- TELEMETRY: YYYY-MM-DD | ...`). An agent erroneously inserted a markdown table header (`| Date | Time | Event | Data |`) at the top of Telemetry Log.md.
       │
       ▼
[Deduction L7]: In Dashboard.md, Dataview queries `file.lists` looking for `TELEMETRY:`. The orphaned table header breaks markdown preview of the file and serves no purpose for Dataview.
```

```
Observation 1.5.4 (Backticked Wikilinks)
       │
       ▼
[Deduction L8]: Authors attempting to highlight wikilinks in prose or lists wrapped them in backticks (`\`[[...]]\``).
       │
       ▼
[Deduction L9]: In Obsidian, inline code blocks suppress internal link resolution. As a result, 95 links across 16 files fail to generate graph edges, appear in graph view, or navigate on click in reading mode.
```

---

## 3. Caveats

1. **Excluded Directories:** Investigation strictly adhered to the boundary constraints, excluding `.agents/`, `.git/`, and `.obsidian/`.
2. **Dataview Runtime Interaction:** Dataview queries execute dynamically inside the Obsidian client. While static queries were verified (such as in `00 - Dashboard.md`), runtime rendering errors cannot be triggered in headless shell environments; however, the data structures feeding them were verified directly.
3. **Template Placeholders:** Template files in `08 - Templates/` contain legitimate Jinja/Obsidian placeholders (e.g. `{{date}}`, `{{title}}`, `{{subject}}`). These are expected template mechanics, not broken agent artifacts.

---

## 4. Conclusion & Standard Styling Recommendations

### 4.1 Categorized Defect Inventory

| Defect ID | Category | Affected Files | Severity | Description |
| :--- | :--- | :--- | :--- | :--- |
| **DEF-01** | Header Desync | `31 - Specialization B2.md`, `32 - Information Theory.md` | High | `block_id` anomalous (`Specialization B2` and `Information Theory`); causes stutter title in Block 32. Should be `Block 31` and `Block 32`. |
| **DEF-02** | Template Mismatch | `08 - Templates/Block Note Template.md` | Medium | H2 headings in template (`Primary Curriculum & Syllabus`, `Study Notes & Problem Sets`) diverge from the 35 core course files. |
| **DEF-03** | Broken Table | `Telemetry Log.md` | High | Orphaned table header followed by bullet items; breaks markdown preview. |
| **DEF-04** | Broken Links (Backticks) | 16 files (95 lines, including `00 - Dashboard.md`, `how-i-study.md`, `Specializations Hub.md`) | High | Wikilinks wrapped in backticks (`\`[[...]]\``) suppress graph edges and link clicking. |
| **DEF-05** | Missing Frontmatter | 11 Hub/Index notes, 5 Root files, 2 Reference files | Medium | Hubs and indexes lack consistent YAML frontmatter schemas. |
| **DEF-06** | Track Schema Discrepancy| All 11 Track files | Medium | `status: planned` vs `not-started`; `prerequisites` stored as string instead of YAML list. |
| **DEF-07** | Bare Code Blocks (MD040)| 18 files (all 11 Tracks, `Specializations Hub.md`, etc.) | Low | ASCII diagrams and logs in bare ` ``` ` without language tags (`text` or `bash`). |
| **DEF-08** | Raw HTML (`<br>`) | `03 - Papers/Paper Reading Hub.md` | Low | 35 instances of `<br>` in table cells. |
| **DEF-09** | Odd List Indentation | 17 files (158 lines) | Low | 3-space and 5-space indentation under numbered items instead of standard 2/4 spaces. |
| **DEF-10** | Proof Q.E.D. Inconsistency | `22 - Statistics.md`, `25 - Convex Optimization.md`, etc. | Low | Formal proofs missing terminating `$\blacksquare$` markers. |

---

### 4.2 Standard Vault-Wide Styling Specification (Recommended)

To ensure long-term consistency and cohesive presentation across the entire vault, the following rules should be adopted:

#### Rule 1: YAML Frontmatter Schemas
Every note in the vault must belong to a defined note archetype and adhere to its schema:
- **Curriculum Block Note:**
  ```yaml
  ---
  block_id: "Block 1" # or B0, BM, BW, P1..P5
  title: "Full Course Title"
  term: "Year 1 Fall"
  status: not-started # not-started | in-progress | done
  hours_estimate: 200
  hours_actual: 0
  primary_resource: "Resource Name"
  milestone: "Concrete milestone description"
  date_started: ""
  date_completed: ""
  ---
  ```
- **Specialization Track Note:**
  ```yaml
  ---
  track_id: "Track 1"
  title: "AI and Machine Learning"
  term: "Years 4 & 5"
  status: not-started # align with curriculum blocks
  target_profile: "Target roles..."
  prerequisites:
    - "[[01 - CS61A]]"
    - "[[07 - Multivariable Calculus]]"
  aliases:
    - "Track 1 - AI and Machine Learning"
    - "Track 1 - Artificial Intelligence and Machine Learning"
  ---
  ```
- **Hub & Index Notes:**
  ```yaml
  ---
  title: "Hub Title"
  type: hub # or index
  tags:
    - hub
    - navigation
  ---
  ```

#### Rule 2: Title & H1 Hierarchy
- Every note must have exactly one H1 at the top of the body (line 1 after frontmatter).
- Curriculum blocks must strictly follow: `# <block_id> — <title>` (e.g. `# Block 31 — Specialization Track B — Course 2` and `# Block 32 — Information Theory, Inference, and Learning Algorithms`).
- Specialization tracks must follow: `# Track N: <title>`.
- Header levels must strictly increment by at most 1 (no skipping levels).
- Block Note Template headings must be synchronized with the 35 actual course files.

#### Rule 3: Wikilink Formatting
- **Never wrap wikilinks in backticks.** Use `[[Note Name]]` or `[[Note Name|Alias]]`.
- For note references in prose, prefer short note names if unique (`[[01 - CS61A]]`), rather than folder-prefixed paths, unless disambiguation is required.
- Do not append `.md` extensions inside wikilinks (e.g., use `[[log]]` not `[[log.md]]`).

#### Rule 4: List Formatting
- Use hyphen `-` as the universal unordered bullet marker.
- Use a strict **2-space indentation** rule per nesting level (2 spaces for level 1 sub-items, 4 spaces for level 2).
- When nesting sub-items under numbered list items, indent with 2 or 4 spaces rather than attempting to align to the column width of the number.
- Task items must strictly use `- [ ] ` or `- [x] `.

#### Rule 5: Markdown Tables
- All tables must maintain leading and trailing outer pipes (`| ... |`).
- Table rows must match header column counts exactly.
- Avoid raw HTML `<br>` tags inside table cells; where two pieces of information exist (such as paper title and author), either place them in separate columns or inline them: `**"Title"** (Authors)`.
- In `Telemetry Log.md`, remove the malformed table header so the file is a clean list of telemetry events compatible with Dataview.

#### Rule 6: Code Blocks & Math Environments
- Every fenced code block must declare a language tag. Use ```` ```text ```` for ASCII diagrams, ```` ```bash ```` for shell sessions, ```` ```dataview ```` for queries.
- Mathematical proofs in `## 📝 Study Notes, Psets & Proofs` should conclude with the standard filled tombstone Q.E.D. marker: `$\blacksquare$`.

---

## 5. Verification Method

To independently verify all observations and metrics in this report, execute the following commands in bash from the repository root (`/home/noblixy/The Noblett Repository`):

### 5.1 Verification of Headers, Titles & Blocks 31/32
```bash
python3 -c '
import yaml, re
for block in ["31 - Specialization B2.md", "32 - Information Theory.md"]:
    p = "/home/noblixy/The Noblett Repository/01 - Curriculum/Year 5 - MEng/" + block
    with open(p) as f:
        text = f.read()
    data = yaml.safe_load(text.split("---")[1])
    bid = data.get("block_id")
    h1 = re.search(r"^#\s+(.+)$", text, re.M).group(1)
    print(f"{block} -> block_id: {bid} | H1: {h1}")
'
```
*Expected Output:*
```
31 - Specialization B2.md -> block_id: Specialization B2 | H1: Specialization B2 — Specialization Track B — Course 2
32 - Information Theory.md -> block_id: Information Theory | H1: Information Theory — Information Theory, Inference, and Learning Algorithms
```

### 5.2 Verification of Backticked Wikilinks
```bash
python3 -c '
import os, re
vault = "/home/noblixy/The Noblett Repository"
count = 0
for root, dirs, files in os.walk(vault):
    if any(x in root for x in [".agents", ".git", ".obsidian"]): continue
    for f in files:
        if not f.endswith(".md"): continue
        with open(os.path.join(root, f)) as fh:
            for idx, l in enumerate(fh, 1):
                if re.search(r"`\[\[.*?\]\]`", l):
                    count += 1
print(f"Total lines with backticked wikilinks: {count}")
'
```
*Expected Output:* `Total lines with backticked wikilinks: 95`

### 5.3 Verification of Malformed Table in `Telemetry Log.md`
```bash
head -n 11 "/home/noblixy/The Noblett Repository/Telemetry Log.md"
```
*Expected Output:* Displays table header on lines 7–8 followed immediately by `- TELEMETRY: ...` list items on lines 9–10.

### 5.4 Verification of Bare Code Blocks (MD040)
```bash
python3 -c '
import os
vault = "/home/noblixy/The Noblett Repository"
bare = []
for root, dirs, files in os.walk(vault):
    if any(x in root for x in [".agents", ".git", ".obsidian"]): continue
    for f in files:
        if not f.endswith(".md"): continue
        with open(os.path.join(root, f)) as fh:
            in_code = False
            for idx, l in enumerate(fh, 1):
                if l.strip().startswith("```"):
                    if not in_code:
                        in_code = True
                        if l.strip() == "```":
                            bare.append(f"{f}:{idx}")
                    else:
                        in_code = False
print(f"Total bare code blocks: {len(bare)}")
'
```
*Expected Output:* `Total bare code blocks: 18`

### 5.5 Invalidation Conditions
This report's findings would be invalidated if:
1. Block 31 and Block 32 were intentionally excluded from standard `Block N` numbering (refuted by the curriculum roadmap where they represent sequential blocks 31 and 32).
2. Backticked wikilinks `\`[[...]]\`` were proven to create native interactive graph edges in Obsidian (refuted by Obsidian link parsing specifications).
3. The table header in `Telemetry Log.md` was required by Dataview (refuted by `00 - Dashboard.md:18`, which queries `file.lists`).
