# Comprehensive Vault Inventory, Architecture & EECS Curriculum Audit

**Survey Date:** 2026-09-25  
**Survey Agent:** Vault Inventory Explorer (`teamwork_preview_explorer_survey_vault`)  
**Target Repository:** `/home/noblixy/The Noblett Repository`  
**Reference Document:** `/home/noblixy/The Noblett Repository/07 - Reference/The Independent EECS Program.pdf`  
**Original Prompt Reference:** `/home/noblixy/The Noblett Repository/.agents/ORIGINAL_REQUEST.md`

---

## 1. Executive Summary

This audit provides an exhaustive investigation of the current state of **The Noblett Repository** Obsidian vault. The vault is an implementation of **"The Independent EECS Program"**—a rigorous, multi-year, self-directed curriculum benchmarked against MIT Course 6-3 (Computer Science and Engineering) and extended toward MEng depth, with added emphasis on mathematics, writing, deliberate cognitive practice, and habit formation.

### Core Discoveries:
1. **Structural Maturity vs. Content Density:** The vault possesses an exceptional, world-class organizational taxonomy (numbered Johnny.Decimal folders `00` through `09`), active telemetry dashboards, comprehensive habit-tracking mechanisms, and 10 standardized Obsidian templates. However, the vault is currently in its **foundational scaffold phase**. The core topical notes folders (`02 - Notes/`, `03 - Papers/`, `04 - Writing/`, `05 - Projects/`) contain only structural index and hub files.
2. **Curriculum Topology:** The vault contains 47 curriculum notes across a 7-phase sequence: Phase -1 (Bedrock Foundations), Phase 0 (Prerequisites), Year 1 (Fundamentals), Year 2 (Systems), Year 3 (Depth), Year 4 (Advanced Core & Specializations), Year 5 (MEng & Capstone), plus 6 predefined Specialization Tracks.
3. **The "Placeholder" Bottleneck:** Several advanced blocks (Block 26 Specialization A1, Block 28 Specialization A2, Block 29 Specialization B1, Block 31 Specialization B2) are purely generic placeholder cards containing 10–12 lines of checklist text deferring to the track notes. Furthermore, the 6 specialization track notes are brief 36-line summaries lacking weekly syllabi, mathematical rigor, and graduate papers.
4. **Curriculum Baseline Gaps (Requirement R1):** When audited against MIT EECS (Course 6-1, 6-2, 6-3, 6-4) and ACM/IEEE CS2023 guidelines, the existing core is heavily biased toward software systems and discrete algorithms, completely missing fundamental physical and mathematical EECS pillars:
   - **Circuits & Electronics (MIT 6.002 / 6.2000)** (missing from core)
   - **Signals and Systems (MIT 6.003 / 6.3000)** (missing from core; only an elective option in Track 6)
   - **Differential Equations (MIT 18.03)** (missing from mathematics sequence)
   - **Complex Variables (MIT 18.04)** (missing)
   - **Core Computer Security / Cryptography** (relegated to an elective)
   - **Human-Computer Interaction (HCI)** (missing)
   - **Embedded Systems & Real-Time Microcontroller Interfacing** (missing from core)
   - **Numerical Analysis & Scientific Computing** (missing)
5. **Vertical Depth Gaps (Requirement R2):** The current syllabi are undergraduate summaries (50–70 lines) lacking explicit PhD-level seminal/modern research papers, formal mathematical proofs, and advanced graduate mathematics (measure-theoretic probability, abstract algebra, spectral graph theory, category theory).
6. **Horizontal Expansion Gaps (Requirement R3):** Modern cutting-edge paradigms requested by the user—such as **TinyML/Edge AI**, **Rust for Systems Engineering & Formal Verification**, and **Hardware-in-the-Loop (HIL) Virtualization**—are absent as dedicated, production-grade tracks.

---

## 2. Comprehensive Vault File & Directory Inventory

Excluding agent metadata (`.agents/`), git metadata (`.git/`), and internal configuration (`.obsidian/`), the vault comprises **77 files** across **12 subdirectories**.

### Directory Structure & File Counts

```text
The Noblett Repository/
├── 00 - Dashboard.md                  [Automated Telemetry, Bedrock Hub, Navigational Map]
├── Checklist.md                       [Master EECS Completion Checklist]
├── how-i-study.md                     [Living Study Manifesto & Cognitive Strategy]
├── log.md                             [Master Daily Study Log]
├── ORIGINAL_REQUEST.md                [Top-Level Mission Specification]
├── Telemetry Log.md                   [Automated iPhone / Smart Plug Telemetry]
├── Your Shelf.md                      [Physical & Digital Book Inventory]
├── .gitignore                         [Git exclusion rules]
├── 01 - Curriculum/                   (47 files across 8 subdirectories)
│   ├── Phase -1 - Bedrock Foundations/ (3 files: B0, BM, BW)
│   ├── Phase 0 - Prerequisites/       (5 files: P1 to P5)
│   ├── Year 1 - Fundamentals/         (8 files: Blocks 01 to 08)
│   ├── Year 2 - Systems/              (7 files: Blocks 09 to 15)
│   ├── Year 3 - Depth/                (7 files: Blocks 16 to 22)
│   ├── Year 4 - Specialization/       (7 files: Blocks 23 to 29)
│   ├── Year 5 - MEng/                 (3 files: Blocks 30 to 32)
│   └── Specializations/               (7 files: Hub + Tracks 1 to 6)
├── 02 - Notes/                        (5 files across 5 subdirectories)
│   ├── Hardware/Hardware Index.md
│   ├── Languages/Languages Index.md
│   ├── Math/Math Index.md
│   ├── Systems/Systems Index.md
│   └── Theory/Theory Index.md
├── 03 - Papers/                       (1 file: Paper Reading Hub.md)
├── 04 - Writing/                      (1 file: Writing Hub.md)
├── 05 - Projects/                     (1 file: Projects Hub.md)
├── 06 - Breadth/                      (1 file: Breadth and Humanities Hub.md)
├── 07 - Reference/                    (3 files: Appendix E, Appendix F, The Independent EECS Program.pdf)
├── 08 - Templates/                    (10 files: Markdown & Templater templates)
└── 09 - Mindset & Habits/             (1 file: Mindset Hub.md)
```

### Complete Inventory Table

| Relative Path | Size (Bytes) | Category | Current State & Purpose |
| :--- | :--- | :--- | :--- |
| `00 - Dashboard.md` | 2,336 | Navigation / Telemetry | Central dashboard with Dataview telemetry table, bedrock links, and vault index. |
| `Checklist.md` | 8,446 | Curriculum Tracking | Checkbox list of all phases, blocks, habits, and deliverables. |
| `how-i-study.md` | 6,071 | Methodology | Cognitive study manifesto (Feynman, retrieval, spacing, weekly schedule). |
| `log.md` | 1,631 | Habit / Daily Log | Daily study log in git. Currently on Day 1 (2026-09-25). |
| `ORIGINAL_REQUEST.md` | 2,022 | Project Specs | Teamwork prompt defining R1, R2, R3, and acceptance criteria. |
| `Telemetry Log.md` | 317 | Automated Data | Apple Shortcuts logging wake-up and work departure times. |
| `Your Shelf.md` | 4,434 | Book Tracker | Inventory of 15 owned books and prioritized acquisition list. |
| `01 - Curriculum/Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit.md` | 6,018 | Curriculum Block | Detailed guide to 8 cognitive learning systems. |
| `01 - Curriculum/Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics.md` | 5,398 | Curriculum Block | Arithmetic first principles (Lockhart, Khan Academy). |
| `01 - Curriculum/Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar.md` | 5,485 | Curriculum Block | Grammar architecture, de-nominalization, sentence diagrams. |
| `01 - Curriculum/Phase 0 - Prerequisites/P1 - Learning How to Learn.md` | 3,083 | Curriculum Block | Oakley, Make It Stick, Dunlosky. |
| `01 - Curriculum/Phase 0 - Prerequisites/P2 - Reading, Thinking, and Writing.md` | 3,054 | Curriculum Block | Adler, Keshav, Pólya, Hermans, McEnerney, Winston. |
| `01 - Curriculum/Phase 0 - Prerequisites/P3 - Math Prerequisites.md` | 2,150 | Curriculum Block | High school math refresh, Velleman (ch 1-3), proof transition. |
| `01 - Curriculum/Phase 0 - Prerequisites/P4 - Programming On-Ramp.md` | 1,544 | Curriculum Block | Harvard CS50x. |
| `01 - Curriculum/Phase 0 - Prerequisites/P5 - Tooling.md` | 1,993 | Curriculum Block | MIT Missing Semester, Linux CLI, Git, Vim, LaTeX. |
| `01 - Curriculum/Year 1 - Fundamentals/01 - CS61A.md` | 1,653 | Curriculum Block | Berkeley CS61A (Structure and Interpretation of Computer Programs in Python). |
| `01 - Curriculum/Year 1 - Fundamentals/02 - Calculus I.md` | 1,906 | Curriculum Block | MIT 18.01SC Single Variable Calculus (Strang). |
| `01 - Curriculum/Year 1 - Fundamentals/03 - Physics I.md` | 1,589 | Curriculum Block | MIT 8.01SC Classical Mechanics (Feynman Six Easy Pieces). |
| `01 - Curriculum/Year 1 - Fundamentals/04 - Nand2Tetris.md` | 2,248 | Curriculum Block | Nisan & Schocken (Hardware & Software from gates to Jack OS). |
| `01 - Curriculum/Year 1 - Fundamentals/05 - SICP.md` | 1,946 | Curriculum Block | MIT 6.001 SICP (Scheme, Metacircular Evaluator). |
| `01 - Curriculum/Year 1 - Fundamentals/06 - C Fluency.md` | 2,047 | Curriculum Block | K&R, Zingaro, Linux memory model, pointer arithmetic. |
| `01 - Curriculum/Year 1 - Fundamentals/07 - Multivariable Calculus.md` | 1,628 | Curriculum Block | MIT 18.02SC Multivariable Calculus (Auroux). |
| `01 - Curriculum/Year 1 - Fundamentals/08 - Physics II.md` | 1,503 | Curriculum Block | MIT 8.02SC Electricity and Magnetism. |
| `01 - Curriculum/Year 2 - Systems/09 - Computer Systems.md` | 2,533 | Curriculum Block | CMU 15-213 / CS:APP (Bryant & O'Hallaron, 7 labs). |
| `01 - Curriculum/Year 2 - Systems/10 - Math for CS.md` | 1,972 | Curriculum Block | MIT 6.042J / 6.1200 Discrete Math for CS (Lehman, Leighton). |
| `01 - Curriculum/Year 2 - Systems/11 - Linear Algebra.md` | 1,988 | Curriculum Block | MIT 18.06 (Strang) + Axler LADR 4e (applied & theoretical). |
| `01 - Curriculum/Year 2 - Systems/12 - Interpreters.md` | 1,853 | Curriculum Block | Ball (Monkey in Go) + Nystrom (clox in C). |
| `01 - Curriculum/Year 2 - Systems/13 - Algorithms I.md` | 1,961 | Curriculum Block | MIT 6.006 (Demaine), CLRS, Zingaro II, Codeforces ≥1200. |
| `01 - Curriculum/Year 2 - Systems/14 - Computer Architecture.md` | 2,017 | Curriculum Block | ETH Zürich DDCA (Mutlu), Harris & Harris RISC-V on FPGA. |
| `01 - Curriculum/Year 2 - Systems/15 - Probability.md` | 1,986 | Curriculum Block | MIT 6.041 / 6.3700 (Tsitsiklis), Bertsekas text. |
| `01 - Curriculum/Year 3 - Depth/16 - Operating Systems.md` | 2,007 | Curriculum Block | MIT 6.1810 (xv6 RISC-V) + OSTEP (Arpaci-Dusseau). |
| `01 - Curriculum/Year 3 - Depth/17 - Software Construction.md` | 2,146 | Curriculum Block | MIT 6.031 / 6.1020 + Ousterhout (Philosophy of Software Design). |
| `01 - Curriculum/Year 3 - Depth/18 - Real Analysis.md` | 2,288 | Curriculum Block | Stephen Abbott (Understanding Analysis), MIT 18.100A. |
| `01 - Curriculum/Year 3 - Depth/19 - Networking.md` | 1,968 | Curriculum Block | Stanford CS144 (TCP in C++) + Kurose & Ross. |
| `01 - Curriculum/Year 3 - Depth/20 - Algorithms II.md` | 2,164 | Curriculum Block | MIT 6.046J + Kleinberg & Tardos (Codeforces ≥1600). |
| `01 - Curriculum/Year 3 - Depth/21 - Databases.md` | 2,193 | Curriculum Block | CMU 15-445 (BusTub in C++, Andy Pavlo) + Kleppmann DDIA. |
| `01 - Curriculum/Year 3 - Depth/22 - Statistics.md` | 2,191 | Curriculum Block | Wasserman (All of Statistics) + McElreath (Statistical Rethinking). |
| `01 - Curriculum/Year 4 - Specialization/23 - Distributed Systems.md` | 1,991 | Curriculum Block | MIT 6.5840 / 6.824 (Morris, Raft, KV in Go) + Kleppmann. |
| `01 - Curriculum/Year 4 - Specialization/24 - Theory of Computation.md` | 1,918 | Curriculum Block | Hopcroft/Motwani/Ullman + MIT 6.045 / 6.1400. |
| `01 - Curriculum/Year 4 - Specialization/25 - Convex Optimization.md` | 2,079 | Curriculum Block | Boyd & Vandenberghe + Stanford EE364A. |
| `01 - Curriculum/Year 4 - Specialization/26 - Specialization A1.md` | 1,277 | Curriculum Block | Placeholder slot for chosen Track A Course 1. |
| `01 - Curriculum/Year 4 - Specialization/27 - Intensive Cryptopals or TLA+.md` | 1,874 | Curriculum Block | January Intensive: Cryptopals sets 1-8 OR TLA+ Raft spec. |
| `01 - Curriculum/Year 4 - Specialization/28 - Specialization A2.md` | 1,363 | Curriculum Block | Placeholder slot for chosen Track A Course 2. |
| `01 - Curriculum/Year 4 - Specialization/29 - Specialization B1.md` | 1,251 | Curriculum Block | Placeholder slot for chosen Track B Course 1. |
| `01 - Curriculum/Year 5 - MEng/30 - Capstone.md` | 2,140 | Curriculum Block | 400-hr Capstone project, 15k-25k word thesis, recorded talk. |
| `01 - Curriculum/Year 5 - MEng/31 - Specialization B2.md` | 1,257 | Curriculum Block | Placeholder slot for chosen Track B Course 2. |
| `01 - Curriculum/Year 5 - MEng/32 - Information Theory.md` | 1,911 | Curriculum Block | David MacKay (Information Theory, Inference, Learning Alg). |
| `01 - Curriculum/Specializations/Specializations Hub.md` | 501 | Specialization | 11-line list of extra math topics (Abstract Algebra, Durrett, etc.). |
| `01 - Curriculum/Specializations/Track 1 - AI and Machine Learning.md` | 1,136 | Specialization | Stanford CS229, Karpathy Zero to Hero, CS231n/CS224n, DL Systems. |
| `01 - Curriculum/Specializations/Track 2 - Systems and Performance.md` | 1,167 | Specialization | MIT 6.172, CMU 15-721, Herlihy & Shavit, Linux kernel patches. |
| `01 - Curriculum/Specializations/Track 3 - Security and Cryptography.md` | 1,105 | Specialization | Dan Boneh Crypto I, MIT 6.858, pwn.college, Cryptopals. |
| `01 - Curriculum/Specializations/Track 4 - Graphics and Vision.md` | 1,152 | Specialization | GAMES101, CMU 15-462, PBRT 4e path tracer, Vulkan/WebGPU. |
| `01 - Curriculum/Specializations/Track 5 - Programming Languages and Compilers.md` | 1,271 | Specialization | Dan Grossman, Cornell CS 6120, TAPL, Software Foundations (Coq). |
| `01 - Curriculum/Specializations/Track 6 - Computer Engineering.md` | 1,414 | Specialization | ETH Mutlu Grad Arch, MIT 6.003 Signals, RISC-V OOO core, ASIC tapeout. |
| `02 - Notes/Hardware/Hardware Index.md` | 572 | Concept Index | Index for digital logic, Hack CPU, RISC-V, EDA/tapeout. (0 notes) |
| `02 - Notes/Languages/Languages Index.md` | 610 | Concept Index | Index for C, Python, Go, Scheme, Rust, assembly. (0 notes) |
| `02 - Notes/Math/Math Index.md` | 722 | Concept Index | Index for Calculus, Discrete Math, Linear Algebra, Probability. (0 notes) |
| `02 - Notes/Systems/Systems Index.md` | 743 | Concept Index | Index for Architecture, OS, Concurrency, Storage, Distributed. (0 notes) |
| `02 - Notes/Theory/Theory Index.md` | 650 | Concept Index | Index for Automata, Complexity, NP-completeness, Algorithms. (0 notes) |
| `03 - Papers/Paper Reading Hub.md` | 1,051 | Research Hub | 10 classic computer systems papers (Lamport, Ritchie, Brooks, etc.). (0 notes) |
| `04 - Writing/Writing Hub.md` | 2,145 | Writing Hub | Milestone deliverables, 9 assigned writing books, style guides. (0 drafts) |
| `05 - Projects/Projects Hub.md` | 1,651 | Project Hub | Checklist of major builds across blocks. (0 specs) |
| `06 - Breadth/Breadth and Humanities Hub.md` | 1,071 | Breadth Hub | Foreign language tracker (to B1) + 8 HASS subjects schedule. |
| `07 - Reference/Appendix E - Failure Modes.md` | 1,655 | Reference | 11 failure modes in order of frequency and their exact fixes. |
| `07 - Reference/Appendix F - Curated URLs.md` | 2,885 | Reference | Table of authoritative web URLs for all primary courses and books. |
| `07 - Reference/The Independent EECS Program.pdf` | 157,489 | Core Document | 32-page original PDF laying out the entire curriculum philosophy and schedule. |
| `08 - Templates/500-Word Essay Template.md` | 545 | Template | Daily writing template. |
| `08 - Templates/Blank-Sheet Retrieval Template.md` | 734 | Template | 15-minute zero-hint recall dump template. |
| `08 - Templates/Block Note Template.md` | 1,139 | Template | Master template for curriculum course blocks. |
| `08 - Templates/Daily Log Entry Template.md` | 614 | Template | Daily reflection and log entry template. |
| `08 - Templates/Feynman Technique Note Template.md` | 1,021 | Template | Jargon-free explanation and friction-point isolation template. |
| `08 - Templates/Franklin Copywork Template.md` | 982 | Template | Sentence-by-sentence prose reverse-engineering template. |
| `08 - Templates/Paper Summary (3-Pass) Template.md` | 1,264 | Template | Keshav (2007) three-pass research paper analysis template. |
| `08 - Templates/Project Build Spec Template.md` | 1,489 | Template | Engineering architecture, rep invariants, test plan template. |
| `08 - Templates/Weekly Review Template.md` | 892 | Template | End-of-week retrospective template. |
| `08 - Templates/Zettelkasten Atomic Note Template.md` | 499 | Template | Atomic concept note template (`Concept`, `Why It Matters`, `Source`). |
| `09 - Mindset & Habits/Mindset Hub.md` | 1,073 | Mindset | Angela Duckworth (Grit), Carol Dweck (Growth), Cal Newport (Deep Work). |

### Obsidian Plugin Configuration (`.obsidian/`)
The vault is configured with the following active community plugins:
1. `dataview`: Query metadata, frontmatter, and list items (actively used in `00 - Dashboard.md`).
2. `templater-obsidian`: Dynamic template interpolation.
3. `obsidian-git`: Automated git commits and backups for study logs.
4. `obsidian-excalidraw-plugin`: Visual architecture diagrams, circuit schematics, and geometric reasoning.
5. `obsidian-advanced-uri`: Enables automated appending via external URI calls (e.g., Apple Shortcuts logging).
6. `quickadd`: Rapid capture of notes and study entries.
7. `opencode`: Code snippet execution and integration.

---

## 3. Detailed EECS Curriculum Architecture

The curriculum in `01 - Curriculum` is derived from `The Independent EECS Program.pdf` and expanded with "Phase -1 Bedrock Foundations".

### Phase Breakdown

```text
Phase -1: Bedrock Foundations ──► Rebuild numbers, grammar, and cognitive tools
Phase 0: Prerequisites        ──► Learn how to learn, read/think/write, math transition, CS50x, tooling
Year 1: Fundamentals          ──► CS61A, Calc I, Physics I, Nand2Tetris, SICP, C Fluency, Multivariable, Physics II
Year 2: Systems Year          ──► CS:APP, Math for CS, Linear Algebra (twice), Interpreters, Algorithms I, Architecture, Probability
Year 3: Depth                 ──► xv6 OS, Software Construction, Real Analysis, Networking, Algorithms II, BusTub DB, Statistics
Year 4: Advanced Core & Spec  ──► Distributed Systems, Theory of Computation, Convex Opt, Spec A1, Cryptopals/TLA+, Spec A2, Spec B1
Year 5: MEng Year             ──► 400-hr Capstone Thesis, Spec B2, Information Theory (MacKay)
```

### The 5 Always-On Habits
1. **Habit 1: Write 500 words a day** (5 days/week; 1 technical writing book per term; annual writing deliverables).
2. **Habit 2: Daily Anki** (Recall cards for complexity classes, syscall semantics, TCP states, distributions).
3. **Habit 3: Breadth & Language** (1 HASS subject per term across 8 terms + 1 foreign language to B1 at 30 min/day).
4. **Habit 4: Daily Log in Git (`log.md`)** (What was done, what was stuck, what to do tomorrow; 2 min/day).
5. **Habit 5: Pleasure Reading Nightly** (20–30 min fiction/non-fiction before bed; Weir, Feynman, etc.).
*Additional:* 1 Codeforces rated contest per month from Year 2; 2 recorded technical presentations per year.

### The 6 Predefined Specialization Tracks
Each track is structured as **Course 1 + Course 2 + Substantial Build Deliverable**:
- **Track 1: AI and Machine Learning**
  - Course 1: Stanford CS229 (Andrew Ng) + Bishop *Deep Learning*.
  - Course 2: Andrej Karpathy *Neural Networks: Zero to Hero* → Stanford CS231n or CS224n.
  - Deliverable: Transformer from scratch + CMU 10-414 *Deep Learning Systems* PyTorch-like framework.
- **Track 2: Systems and Performance**
  - Course 1: MIT 6.172 *Performance Engineering of Software Systems* (Leiserson).
  - Course 2: CMU 15-721 *Advanced Database Systems* (Andy Pavlo) OR Herlihy & Shavit *Art of Multiprocessor Programming*.
  - Deliverable: Merged patches to Linux kernel, PostgreSQL, LLVM, or language runtime.
- **Track 3: Security and Cryptography**
  - Course 1: Dan Boneh *Cryptography I* + Boneh & Shoup *Graduate Course in Applied Cryptography*.
  - Course 2: MIT 6.858 *Computer Systems Security* + pwn.college.
  - Deliverable: Cryptopals sets 1–8 + competitive CTF placement.
- **Track 4: Graphics and Vision**
  - Course 1: GAMES101 *Introduction to Computer Graphics* (Lingqi Yan).
  - Course 2: CMU 15-462 / Berkeley CS184 + Pharr, Jakob & Humphreys *Physically Based Rendering (PBRT 4e)*.
  - Deliverable: Monte Carlo path tracer with BVH + Vulkan/WebGPU real-time renderer.
- **Track 5: Programming Languages and Compilers**
  - Course 1: Dan Grossman *Programming Languages* (UW) + Benjamin Pierce *Types and Programming Languages (TAPL)*.
  - Course 2: Cornell CS 6120 *Advanced Compilers* (Adrian Sampson) + Cooper & Torczon *Engineering a Compiler*.
  - Deliverable: Optimizing SSA compiler for x86-64/RISC-V + Pierce *Software Foundations* Vol 1–2 in Coq.
- **Track 6: Computer Engineering (Deep Hardware)**
  - Course 1: Onur Mutlu *Graduate Computer Architecture* (ETH Zürich) + Hennessy & Patterson *CA:AQA 6e*.
  - Course 2: MIT 6.003 / 6.3000 *Signals and Systems* (Alan Oppenheim).
  - Deliverable: Out-of-order RISC-V core in gem5 + physical ASIC tapeout via Tiny Tapeout.

---

## 4. Note Conventions, Frontmatter Schemas & Formatting

### Standard Frontmatter Schema
Curriculum block notes (`01 - Curriculum/`) adhere strictly to the following YAML frontmatter schema:

```yaml
---
block_id: "Block 9"                     # Short unique identifier (B0, BM, BW, P1-P5, Block 1-32)
title: "Computer Systems (CS:APP)"      # Full descriptive title
term: "Year 2 Fall"                     # Term/Phase placement
status: not-started                     # Status enum: not-started | in-progress | done
hours_estimate: 200                     # Expected workload in hours (~150-220 hrs/block)
hours_actual: 0                         # Actual logged time
primary_resource: "Bryant & O'Hallaron, CS:APP, 3e & CMU 15-213 Lectures"
milestone: "All 7 CS:APP labs pass; malloc lab score ≥90; objdump decoded cold"
date_started: ""                        # YYYY-MM-DD
date_completed: ""                      # YYYY-MM-DD
---
```

### Standard Structural Sections within a Block Note
Each block note is divided into standardized Markdown sections:
1. `> [!INFO] Block Overview` — Callout repeating metadata.
2. `## 🎯 Why This Block Matters` — Concrete rationale, intuition, and downstream dependencies.
3. `## 📖 Primary Syllabus & Core Content` — Chapter-by-chapter reading checklist and lecture mapping.
4. `## 🛠️ Build Requirement` — Concrete project or lab with verifiable output.
5. `## 🏁 Done When` — An uncompromising, objective gatekeeping criterion in an `[!IMPORTANT]` callout.
6. `## 📝 Study Notes, Psets & Proofs` — Placeholder section for user's atomic notes, proofs, and solutions.
7. `## 🔄 Appendix A Alternatives (Failover)` — Secondary courses/books if the primary source fails after two weeks.

### Wikilinks, Callouts, and Tag Usage
- **Wikilinks:** Notes link directly by filename (`[[09 - Computer Systems]]`, `[[00 - Dashboard]]`) or with piped aliases (`[[Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics|Bedrock Math]]`).
- **Callouts:** Heavily utilized Obsidian callouts:
  - `> [!INFO]` for block summaries.
  - `> [!IMPORTANT]` for gatekeeping criteria.
  - `> [!QUOTE]` for mindset anchors.
  - `> [!TIP]` for template recommendations.
- **Tags:** Current notes have minimal tag usage (`tags: [specialization, curriculum]` in track notes). Tags are under-utilized; frontmatter properties and directory hierarchy currently carry the organizational weight.

---

## 5. Baseline Gap Analysis (Requirement R1)

To create a **gap-free curriculum that significantly exceeds the rigor and breadth of a standard MIT undergraduate degree**, we audited the current vault against:
1. **MIT Course 6-1 (Electrical Science and Engineering)**
2. **MIT Course 6-2 (Electrical Engineering and Computer Science)**
3. **MIT Course 6-3 (Computer Science and Engineering)**
4. **MIT Course 6-4 (Artificial Intelligence and Decision Making)**
5. **ACM/IEEE Computer Science Curricula 2023 (CS2023 Guidelines)**

### Major Foundational Knowledge Areas Missing from the Core Curriculum

| Missing Knowledge Area | Canonical Benchmark Course | Why It Is Essential & How Current Vault Fails |
| :--- | :--- | :--- |
| **Circuits & Electronics** | MIT 6.002 / 6.2000; Berkeley EECS 16A/16B | **Missing from Core.** Nand2Tetris (Block 4) begins at ideal digital logic gates ($0/1$). The physical reality of RC/RLC circuits, diode conduction, MOSFET transistor operation, small-signal models, and op-amps is omitted entirely. A student cannot interface hardware with real physical signals. |
| **Signals & Systems** | MIT 6.003 / 6.3000; Oppenheim & Willsky | **Missing from Core.** Continuous-time and discrete-time Fourier series/transforms, Laplace transforms, Z-transforms, convolution, filtering, and the Nyquist-Shannon sampling theorem. (Currently only an elective option in Track 6). Crucial for DSP, communications, audio/video processing, control theory, and continuous ML. |
| **Differential Equations & Dynamical Systems** | MIT 18.03; Strogatz *Nonlinear Dynamics* | **Missing from Math Sequence.** The math sequence jumps from Multivariable Calculus (Block 7) directly to Real Analysis (Block 18). Missing: first/second-order ODEs, systems of linear differential equations, matrix exponentials, phase portraits, stability analysis, and Fourier/Laplace solutions. Vital for physics, circuits, control systems, and diffusion models in AI. |
| **Complex Variables & Transforms** | MIT 18.04; Brown & Churchill | **Missing.** Complex integration, Cauchy's integral theorem, Laurent series, residue calculus, conformal mapping. Foundational for frequency-domain analysis, electromagnetic wave propagation, and quantum mechanics. |
| **Core Computer Security Fundamentals** | MIT 6.1600 / 6.858; CMU 18-730 | **Missing from Mandatory Core.** Security is currently relegated to an elective (Track 3) or a January elective (Block 27 Cryptopals). Every elite EECS graduate must master threat modeling, buffer overflows, memory safety, web security, TLS, side-channels, and defense-in-depth as a core requirement. |
| **Embedded Systems & Microcontroller Interfacing** | MIT 6.08 / 6.115; Valvano *Embedded Systems* | **Missing from Core.** The current systems track has Nand2Tetris and xv6, but skips real bare-metal embedded engineering: ARM Cortex-M/RISC-V firmware, interrupts, DMA, timers, I2C/SPI/UART buses, ADC/DAC, FreeRTOS, and low-power modes. |
| **Human-Computer Interaction (HCI) & UI Engineering** | MIT 6.813 / 6.831; Stanford CS147; Dix et al. | **Missing entirely.** Required by ACM/IEEE CS2023. UI software architecture, event dispatch loops, accessibility (WCAG), information visualization, user testing, mental models, and frontend systems design. |
| **Numerical Methods & Scientific Computing** | MIT 18.330; Trefethen & Bau | **Missing from Core.** Floating-point arithmetic error propagation (IEEE 754), condition numbers, stability, iterative linear system solvers (Conjugate Gradient, GMRES), numerical optimization, and numerical integration. |
| **Modern Software Engineering Lifecycle & DevOps** | MIT 6.S194; Google SRE; Fowler | **Weakly Covered.** MIT 6.031 covers types and specifications, but modern large-scale testing (fuzzing, property-based testing, mutation testing), CI/CD workflows, infrastructure-as-code, and distributed tracing are absent. |

---

## 6. Vertical Expansion Audit: Graduate-Level Depth (Requirement R2)

The prompt requires: *"Inject graduate-level rigor into the core tracks. This includes adding advanced mathematical prerequisites, foundational PhD-level papers, and rigorous textbook proofs to existing syllabi."*

### Current Deficiencies in Depth:
1. **Shallow Syllabus Outlines:** Most current block notes are only 50–70 lines long. They list bullet points of topics without providing worked derivations, formal definitions, lecture notes, or proof sketches.
2. **The "Specialization Placeholder" Void:**
   - `26 - Specialization A1.md` (54 lines): Placeholder slot.
   - `28 - Specialization A2.md` (54 lines): Placeholder slot.
   - `29 - Specialization B1.md` (54 lines): Placeholder slot.
   - `31 - Specialization B2.md` (54 lines): Placeholder slot.
   - These notes do not contain curriculum; they merely say *"Refer to the chosen Track note"*.
3. **Specialization Tracks Lack Rigor:** Tracks 1 through 6 are only ~36 lines each, listing two courses and a high-level build. They lack detailed reading schedules, weekly problem set definitions, and paper reading lists.
4. **Missing Seminal PhD-Level Papers:** While `03 - Papers/Paper Reading Hub.md` lists 10 classic papers (Lamport, Ritchie, Brooks, etc.), the core course blocks themselves do not have required paper reading lists attached to them.
5. **Missing Advanced Mathematical Prerequisites for Graduate Depth:**
   - **Measure-Theoretic Probability** (Durrett, Billingsley): Required for rigorous continuous-time stochastic processes, advanced diffusion models, and theoretical statistics.
   - **Abstract Algebra** (Artin, Dummit & Foote): Groups, rings, fields, Galois theory, polynomial rings, elliptic curves. Essential for modern cryptography (post-quantum lattice cryptography, zero-knowledge proofs) and algebraic coding theory.
   - **Spectral Graph Theory & Graph Laplacians** (Spielman): Essential for modern network science, graph neural networks, and combinatorial optimization.
   - **Category Theory & Formal Semantics** (Milewski, Harper, Pierce): Functors, monads, adjunctions, type theory, Curry-Howard isomorphism, domain theory for programming languages.
   - **Differential Geometry & Lie Groups** (Spivak, Hall): Manifolds, tangent spaces, Lie algebras. Essential for modern robotics kinematics, computer vision, and geometric deep learning (SE(3) equivariance).

---

## 7. Horizontal Expansion Audit: Modern Paradigms (Requirement R3)

The prompt requires: *"Design and integrate new specialization tracks covering cutting-edge engineering disciplines not typically found in standard undergraduate programs (e.g., TinyML/Edge AI, Rust for Systems Engineering, Hardware-in-the-Loop Virtualization)."*

### Proposed New Specialization Tracks & Specifications

To exceed MIT undergraduate standards and meet acceptance criteria, the vault requires the creation of dedicated, complete tracks with graduate textbooks, seminal papers, and defined lab builds:

### Track 7: TinyML, Edge AI & Neuromorphic Computing
- **Core Focus:** Running deep learning models under extreme compute, memory (tens of kilobytes), and power (milliwatts) constraints.
- **Key Texts & Courses:**
  - MIT 6.5940 *TinyML and Efficient Deep Learning Computing* (Song Han).
  - Warden & Situnayake, *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers*.
  - Sze et al., *Efficient Processing of Deep Neural Networks*.
- **Seminal / Graduate Papers:**
  - Han et al. (2015), *"Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding"*.
  - Jacob et al. (2018), *"Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference"*.
  - Howard et al. (2017), *"MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications"*.
  - Lin et al. (2020), *"MCUNet: Tiny Deep Learning on IoT Devices"*.
- **Lab & Build Requirement:**
  - Build a custom INT8 tensor inference engine in pure C from scratch with zero dynamic memory allocation.
  - Deploy an end-to-end keyword-spotting or vision model onto a bare-metal ARM Cortex-M4 (STM32 or RP2040) micro-controller with real-time latency under 50ms.

### Track 8: Rust for Systems Engineering & Formal Verification
- **Core Focus:** Memory safety without garbage collection, modern concurrency, type-driven design, and mathematical proof of software correctness.
- **Key Texts & Courses:**
  - Blandy, Orendorff & Tindall, *Programming Rust, 2nd ed.*
  - Mara Bos, *Rust Atomics and Locks*.
  - Chlipala, *Certified Programming with Dependent Types* / Pierce et al., *Software Foundations*.
- **Seminal / Graduate Papers:**
  - Jung et al. (2017), *"RustBelt: Securing the Foundations of the Rust Programming Language"* (POPL).
  - Matsushita et al. (2021), *"RustHorn: CHC-based Verification for Rust Programs"*.
  - Levy et al. (2015), *"Ownership is Freedom: Sound Interlocks for Computer Systems"* (Tock OS).
- **Lab & Build Requirement:**
  - Implement a multi-threaded, asynchronous actor-based network engine or key-value storage engine in safe Rust, using `tokio` or custom io_uring.
  - Formally verify the memory-safety and absence of panics for a critical unsafe data structure using the **Kani Rust Verifier** (model checking) or **Creusot / Prusti**.

### Track 9: Hardware-in-the-Loop (HIL) Virtualization, Emulation & Digital Twins
- **Core Focus:** Co-simulation of hardware and software, real-time bus virtualization (CAN, SPI, PCIe), QEMU virtual platform modeling, and physical environment injection.
- **Key Texts & Courses:**
  - Fabrice Bellard, *QEMU, a Fast and Portable Dynamic Translator*.
  - Lee & Seshia, *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*.
  - IEEE standards on hardware emulation and SystemC / TLM 2.0.
- **Seminal / Graduate Papers:**
  - Bellard (2005), *"QEMU, a Fast and Portable Dynamic Translator"* (USENIX ATC).
  - Chiueh et al., *"Hardware-in-the-loop Simulation for Cyber-Physical Systems"*.
  - Eom et al., *"Virtual Platform Co-Simulation for Automotive ECU Verification"*.
- **Lab & Build Requirement:**
  - Create a custom QEMU virtual peripheral device in C/Rust (e.g., a virtual CAN controller or cryptoprocessor) and connect it via socket to a real-time Python/C++ physical dynamical system model (Digital Twin).
  - Write an operating system device driver in xv6 or Linux that communicates with the virtual hardware under fault-injection conditions.

### Track 10: Quantum Information Science & Quantum Computing
- **Core Focus:** Quantum algorithms, quantum circuit synthesis, quantum error correction, and NISQ vs fault-tolerant architectures.
- **Key Texts & Courses:**
  - Nielsen & Chuang, *Quantum Computation and Quantum Information* (10th Anniversary Edition).
  - MIT 8.370 / 18.435 Quantum Information Science (Peter Shor, Isaac Chuang).
- **Seminal / Graduate Papers:**
  - Shor (1994), *"Algorithms for Quantum Computation: Discrete Logarithms and Factoring"*.
  - Grover (1996), *"A Fast Quantum Mechanical Algorithm for Database Search"*.
  - Fowler et al. (2012), *"Surface Codes: Towards Practical Large-Scale Quantum Computation"*.
- **Lab & Build Requirement:**
  - Implement a full quantum circuit state-vector simulator in C++ or Rust from scratch (matrix-vector multiplication of $2^n$ state vectors).
  - Implement Shor's algorithm and quantum phase estimation in Qiskit/Cirq, running against IBM Quantum hardware or noise simulators.

### Track 11: Autonomous Robotics, Cyber-Physical Systems & Sensor Fusion
- **Core Focus:** State estimation, probabilistic robotics, perception, optimal control, and real-time motion planning.
- **Key Texts & Courses:**
  - Thrun, Burgard & Fox, *Probabilistic Robotics*.
  - Lynch & Park, *Modern Robotics: Mechanics, Planning, and Control*.
  - Stanford CS223A / CS287 *Advanced Robotics*.
- **Seminal / Graduate Papers:**
  - Mur-Artal et al. (2015), *"ORB-SLAM: A Versatile and Accurate Monocular SLAM System"*.
  - Karaman & Frazzoli (2011), *"Sampling-based Algorithms for Optimal Motion Planning (RRT*)"*.
  - Kalman (1960), *"A New Approach to Linear Filtering and Prediction Problems"*.
- **Lab & Build Requirement:**
  - Implement an Extended Kalman Filter (EKF) and Factor Graph SLAM algorithm fusing IMU, wheel odometry, and LiDAR/Camera data in C++ / ROS2.
  - Implement an end-to-end model predictive controller (MPC) for trajectory tracking in simulation.

---

## 8. Summary of Actionable Recommendations for Multi-Agent Team

Based on this inventory and audit, the following structured tasks should be executed by subsequent specialized agents in the team:

1. **Curriculum Architecture Expansion (Phase Restructuring):**
   - Insert **Circuits & Electronics** (MIT 6.002) into Year 2 Spring.
   - Insert **Signals & Systems** (MIT 6.003) into Year 2/3.
   - Insert **Differential Equations** (MIT 18.03) into Year 1/2 Mathematics sequence.
   - Insert a mandatory **Computer Systems Security Core** module.
2. **De-anonymize & Expand Specialization Slots:**
   - Replace generic placeholder cards (`26`, `28`, `29`, `31`) with concrete course pathways tied to chosen tracks.
   - Flesh out all specialization tracks from 36-line summaries into full, comprehensive course syllabi with assigned problem sets, reading milestones, and build specifications.
3. **Inject Graduate Rigor (Seminal Papers & Advanced Proofs):**
   - Attach at least 3–5 foundational graduate/PhD-level papers to every single block note and specialization track.
   - Populate mathematical theorems with explicit definitions, lemmas, and proof requirements.
4. **Synthesize New Cutting-Edge Tracks:**
   - Author complete specification notes for **Track 7 (TinyML/Edge AI)**, **Track 8 (Rust Systems & Formal Verification)**, **Track 9 (Hardware-in-the-Loop Virtualization)**, and **Track 10 (Quantum Information)**.
5. **Populate Core Notes Scaffold:**
   - Begin creating atomic concept notes in `02 - Notes/` (Math, Systems, Hardware, Languages, Theory) linking to curriculum blocks to transform the vault from an empty scaffold into a living repository of knowledge.

---

*Survey completed by Vault Inventory Explorer. Detailed handoff documented in `handoff.md`.*
