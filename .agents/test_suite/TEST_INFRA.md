# Comprehensive Vault Quality Pass — Test Infrastructure Specification (TEST_INFRA)

**Document Version:** 2.0.0  
**Author:** E2E Test Writer (`test_writer_e2e`)  
**Target Repository:** `/home/noblixy/The Noblett Repository` (The Noblett Repository Obsidian Vault)  
**Test Suite Path:** `/home/noblixy/The Noblett Repository/.agents/test_suite/run_e2e_tests.py`  
**Master Project Plan:** `/home/noblixy/The Noblett Repository/.agents/PROJECT.md`  
**Authoritative Mission Reference:** `/home/noblixy/The Noblett Repository/.agents/ORIGINAL_REQUEST.md`  
**Date:** 2026-09-25  

---

## 1. Executive Overview & Testing Philosophy

The Noblett Repository is a multi-year, graduate-expanded EECS curriculum and personal knowledge base structured under the Johnny.Decimal classification system. Following its massive curriculum expansion (11 specialization tracks, 39 proofs, 35 landmark papers, bridge syllabi), the vault requires a comprehensive quality pass to ensure professional polish, perfect link resolution, 100% graph reachability, structural consistency, and elimination of stubs or duplication.

To enforce these quality standards with absolute mathematical and forensic rigor, the **E2E Test Suite** provides an **opaque-box, requirement-driven automated test harness**. The test harness treats every markdown note, frontmatter property, table, list item, wikilink, and code block as compile-time artifacts subject to strict syntactic, semantic, and relational validation.

### Core Testing Principles:
1. **Opaque-Box Verification:** The runner inspects observable artifacts (file paths, YAML frontmatter keys/values, heading sequences, interactive wikilinks, table column boundaries, list indentation depths, LaTeX proof derivations) without assuming internal implementation shortcuts.
2. **Progressive Testability:** The test suite evaluates features across milestones (M1: Graph & Link Integrity; M2: Formatting, Frontmatter & Structural Consistency; M3: Deduplication, Sanitization & Bidirectionality; M4: Stub Resolution & Proof Completion; M5: 100% E2E Quality Pass). Tests can be executed globally or scoped to individual milestones.
3. **Deterministic & Zero-Dependency Execution:** The runner is implemented entirely in standard Python 3.8+ using `pathlib`, `re`, `json`, `argparse`, `time`, and `dataclasses`. No external packages (`pip`) are required.
4. **Adversarial & Boundary Verification:** The suite verifies edge conditions including escaped table pipes (`\|`), uninstantiated template placeholders (`{{block_id}}`), empty files, unbalanced code/math fences, odd-space list indents, disconnected subgraphs, and case sensitivity.

---

## 2. The 4-Tier Test Architecture

The verification suite comprises **53 automated test cases** structured into four progressive verification tiers:

```text
┌────────────────────────────────────────────────────────────────────────┐
│             VAULT COMPREHENSIVE QUALITY PASS E2E TEST SUITE            │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 1: FEATURE COVERAGE (35 Tests Across 7 Feature Areas)              │
│  - Area 1.1: Wikilink Resolution (T1.1–T1.5: Standard, Aliased,        │
│              Bedrock paths, Un-backticked, Zero-broken census)         │
│  - Area 1.2: Graph Reachability & Orphans (T1.6–T1.10: 0 orphans,      │
│              Dashboard traversal, Root notes, Notes indices, Tracks)   │
│  - Area 1.3: Header Hierarchy & Titles (T1.11–T1.15: Level continuity, │
│              Single H1, Course block H1, Blocks 31/32 sync, Tracks)   │
│  - Area 1.4: YAML Frontmatter Schemas (T1.16–T1.20: Course block keys, │
│              Status/hours types, Track keys, Track prereqs, Hubs)      │
│  - Area 1.5: List Formatting & Tables (T1.21–T1.25: Hyphen markers,    │
│              Indentation hierarchy, Telemetry Log, Table columns, MD040)│
│  - Area 1.6: Stub Absence & Proofs (T1.26–T1.30: Zero TODOs, 13 core  │
│              proofs, Bridge proof derivations, THT proof, Q.E.D.)      │
│  - Area 1.7: Content Deduplication (T1.31–T1.35: Prompt file removal,  │
│              Gap analysis sanitization, Matrix dedup, Mindset, Bounds) │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 2: BOUNDARY & CORNER CASES (7 Tests)                              │
│  - T2.1: Escaped Table Pipes Boundary (`\|` in `Your Shelf.md`)        │
│  - T2.2: Template Dummy Placeholders Escaping (`{{...}}`, `Related`)   │
│  - T2.3: Empty Files & Degenerate Notes Boundary (0 bytes / <100 B)    │
│  - T2.4: Malformed Fences & Unclosed Delimiters (```, $$, $)           │
│  - T2.5: Odd-Space Indentation Boundary (1/3/5/7 space sublist indents)│
│  - T2.6: Isolated Subgraph Detection (Graph island / cluster analysis) │
│  - T2.7: Case Sensitivity & Basename Collision (Exact disk matching)   │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 3: CROSS-FEATURE INTERACTIONS (6 Tests)                           │
│  - T3.1: Dataview Query Compatibility (Frontmatter + Telemetry items)  │
│  - T3.2: Bidirectional Specialization Graph Connectivity (Tracks <->)  │
│  - T3.3: Curriculum Blocks to Landmark Papers Reciprocity (Papers <->) │
│  - T3.4: Curriculum Blocks to Topic Note Indices Reciprocity (02/ <->) │
│  - T3.5: Course Block Sinks Elimination & Breadcrumb Traversal         │
│  - T3.6: Prerequisite DAG Acyclicity & Chronological Order (DFS DAG)  │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 4: REAL-WORLD WORKFLOWS (5 Tests)                                 │
│  - T4.1: Student Navigation Simulation (Dashboard -> All areas)        │
│  - T4.2: Degree Pathways Completion Simulation (4 career tracks)       │
│  - T4.3: Daily Study Routine Simulation (how-i-study -> log -> shelf)  │
│  - T4.4: Project Build Progression Simulation (Projects Hub builds)   │
│  - T4.5: Master Curriculum Audit Simulation (Dashboard/Checklist sync) │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Test Specification Matrix

| Test ID | Tier | Milestone | Feature ID | Test Name | Target Requirements | Verification Method & Gate Criteria |
| :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **T1.1** | 1 | M1 | F01 | Standard Wikilink Resolution | Acceptance § 1 | Asserts every unaliased `[[Target]]` in non-template notes resolves to an existing file. |
| **T1.2** | 1 | M1 | F02 | Aliased Wikilink Resolution | Acceptance § 1 | Asserts every `[[Target\|Alias]]` resolves accurately to target note. |
| **T1.3** | 1 | M1 | F01 | Bedrock Foundations Path Resolution | F01, Survey 1 | Scans `00 - Dashboard`, `Checklist`, `log`, `Your Shelf` for Bedrock links. Asserts 0 missing folder prefix errors. |
| **T1.4** | 1 | M2 | F09 | Un-backticked Wikilink Syntax | F09, Survey 2 | Scans vault notes for backticked `` `[[...]]` ``. Asserts 0 backticked wikilinks. |
| **T1.5** | 1 | M1 | F01 | Zero Broken Links Vault Census | Acceptance § 1 | Programmatic scan across all 84 notes outside templates. Asserts 0 broken wikilinks. |
| **T1.6** | 1 | M1 | F05 | Non-Template Orphan Notes Prohibition | Acceptance § 1 | Computes in-degree for all notes. Asserts in-degree $\ge 1$ for all non-template notes. |
| **T1.7** | 1 | M1 | F07 | Dashboard Directed Graph Reachability | Acceptance § 1 | Executes BFS from `00 - Dashboard.md`. Asserts 100% of non-template notes reachable. |
| **T1.8** | 1 | M1 | F05 | Root Notes Inbound Dashboard Linkage | F05, Survey 1 | Asserts `Checklist`, `Your Shelf`, `how-i-study`, `log`, `Telemetry Log` linked from Dashboard. |
| **T1.9** | 1 | M1 | F05 | Domain Notes Indices Dashboard Linkage | F05, Survey 1 | Asserts all 5 indices in `02 - Notes/` linked directly from `00 - Dashboard.md`. |
| **T1.10** | 1 | M1 | F07 | Specialization Tracks Directed Reachability | F07, Survey 1 | Asserts all 11 Specialization Tracks linked from `Specializations Hub.md`. |
| **T1.11** | 1 | M2 | F08 | Header Level Continuity | Acceptance § 2 | Scans heading level transitions in every note. Asserts 0 heading level skips. |
| **T1.12** | 1 | M2 | F08 | Single H1 Rule | Acceptance § 2 | Asserts exactly one H1 per non-template markdown document. |
| **T1.13** | 1 | M2 | F08 | Curriculum Block H1 & Title Convention | F08, Contracts | Asserts all curriculum notes have H1 matching `# <block_id> — <title>`. |
| **T1.14** | 1 | M2 | F08 | Blocks 31 & 32 Header & ID Synchronization | F08, Survey 2 | Asserts Block 31 has `block_id: "Block 31"` and H1 `Block 31`; Block 32 has `Block 32`. |
| **T1.15** | 1 | M2 | F08 | Specialization Track H1 Convention | Contracts | Asserts all 11 track notes have H1 conforming to `# Track <N>: <title>`. |
| **T1.16** | 1 | M2 | F12 | Curriculum Frontmatter Required Keys | Contracts | Asserts presence of `block_id`, `title`, `term`, `status`, `hours_estimate`, `primary_resource`, `milestone`. |
| **T1.17** | 1 | M2 | F12 | Curriculum Status & Hours Values | Contracts | Asserts `status` in `['not-started', 'in-progress', 'done']` and `hours_estimate > 0`. |
| **T1.18** | 1 | M2 | F12 | Track Frontmatter Required Keys | Contracts | Asserts presence of `track_id`, `title`, `term`, `status`, `target_profile`, `prerequisites`. |
| **T1.19** | 1 | M2 | F12 | Track Prerequisites YAML Schema | Contracts, F12 | Asserts `prerequisites` in all 11 tracks is formatted as a valid YAML list of wikilinks. |
| **T1.20** | 1 | M2 | F12 | Hub & Index Frontmatter Standardization | Contracts, F12 | Asserts navigation hubs and `02 - Notes/` indices contain `title`, `type`, and `tags`. |
| **T1.21** | 1 | M2 | F15 | List Bullet Marker Uniformity | Acceptance § 2 | Asserts all unordered list items use hyphen `-` marker (no `*` or `+`). |
| **T1.22** | 1 | M2 | F15 | List Indentation Normalization | F15, Survey 2 | Asserts all list indentations are even multiples (2 or 4 spaces; 0 odd-space lines). |
| **T1.23** | 1 | M2 | F11 | Telemetry Log Table Syntax Integrity | F11, Survey 2 | Asserts absence of orphaned table header preceding Dataview list items in `Telemetry Log.md`. |
| **T1.24** | 1 | M2 | F11 | Markdown Table Structural Validation | Acceptance § 2 | Asserts all markdown tables have matching column counts across header and rows. |
| **T1.25** | 1 | M2 | F13 | Fenced Code Block Language Tagging | F13, Survey 2 | Asserts all fenced code blocks (```) specify language identifiers (MD040). |
| **T1.26** | 1 | M3 | F27 | Zero Placeholder & TODO Directives | Acceptance § 3 | Asserts 0 `TODO`, `TBD`, or parenthetical proof stubs across vault notes. |
| **T1.27** | 1 | M4 | F27 | Core Course Blocks Proof Population | F27, Survey 3 | Asserts 13 course blocks contain substantive proof derivations in `Study Notes & Proofs`. |
| **T1.28** | 1 | M4 | F28 | Bridge Course Rigorous Proof Expansions | F28, Survey 3 | Asserts bridge courses `04a`, `08a`, `15a` contain full mathematical derivations. |
| **T1.29** | 1 | M4 | F29 | Time Hierarchy Theorem Proof Completion | F29, Survey 3 | Asserts `24 - Theory of Computation.md` contains full diagonalization reduction proof. |
| **T1.30** | 1 | M2 | F16 | Proof Q.E.D. Tombstone Consistency | F16, Survey 2 | Asserts formal mathematical proofs terminate with Q.E.D. marker `$\blacksquare$`. |
| **T1.31** | 1 | M1 | F04 | Root Agent Prompt File Elimination | F04, Survey 1 | Asserts redundant `/home/noblixy/The Noblett Repository/ORIGINAL_REQUEST.md` is removed. |
| **T1.32** | 1 | M3 | F17 | Baseline Gap Analysis Note Sanitization | F17, Survey 3 | Asserts `Baseline Gap Analysis` contains no worker IDs, `.agents` paths, or phase labels. |
| **T1.33** | 1 | M3 | F18 | Specialization Matrix Deduplication | F18, Survey 3 | Asserts Blocks 26, 28, 29, 31 reference `Specializations Hub` rather than duplicate matrix. |
| **T1.34** | 1 | M3 | F19 | Mindset & Habit Definitions Deduplication | F19, Survey 3 | Asserts definitions of Grit, Mindset, Deep Work consolidated between `how-i-study` and `Mindset Hub`. |
| **T1.35** | 1 | M3 | F20 | Generalization Bounds Proof Deduplication | F20, Survey 3 | Asserts Rademacher/McDiarmid proofs cross-referenced between `22 - Statistics` and `Track 1`. |
| **T2.1** | 2 | M1 | F02 | Escaped Table Pipes Boundary | F02, Survey 1 | Asserts 0 escaped backslashes in wikilinks (`\|`) in `Your Shelf.md` and tables. |
| **T2.2** | 2 | M1 | F03 | Template Dummy Placeholders Escaping | F03, Survey 1 | Asserts template dummy variables (`{{block_id}}`, `Related Note`) are escaped in code. |
| **T2.3** | 2 | M2 | F11 | Empty Files & Degenerate Notes Boundary | Boundary | Asserts 0 empty notes (0 bytes) and 0 degenerate notes (< 100 bytes). |
| **T2.4** | 2 | M2 | F13 | Malformed Fences & Unclosed Delimiters | Boundary | Asserts all code block fences (```) and math delimiters ($$) are balanced. |
| **T2.5** | 2 | M2 | F15 | Odd-Space Indentation Boundary | Boundary | Asserts 0 occurrences of 1, 3, 5, or 7-space odd indentation across vault. |
| **T2.6** | 2 | M1 | F07 | Isolated Subgraph Detection | Boundary | Traverses undirected graph across all notes. Asserts 0 isolated subgraphs / note islands. |
| **T2.7** | 2 | M1 | F01 | Case Sensitivity & Basename Collision | Boundary | Asserts exact case-sensitive wikilink matches and 0 basename collisions. |
| **T3.1** | 3 | M2 | F11 | Dataview Query Compatibility | Contracts | Validates frontmatter and list formatting required for Dataview dashboard queries. |
| **T3.2** | 3 | M3 | F22 | Bidirectional Specialization Connectivity | F22, Contracts | Asserts reciprocal linking between `Specializations Hub` and all 11 tracks. |
| **T3.3** | 3 | M3 | F23 | Curriculum to Landmark Papers Reciprocity | F23, Contracts | Asserts reciprocal cross-referencing between course blocks and `Paper Reading Hub.md`. |
| **T3.4** | 3 | M3 | F24 | Curriculum to Topic Notes Reciprocity | F24, Contracts | Asserts reciprocal linking between course blocks and `02 - Notes/` domain indices. |
| **T3.5** | 3 | M3 | F26 | Course Block Sinks Elimination & Breadcrumbs | F26, Survey 1 | Asserts all 31 previously zero-out-degree course blocks have outgoing navigation. |
| **T3.6** | 3 | M2 | F12 | Prerequisite DAG Acyclicity & Chronological Order | Acceptance § 1 | DFS cycle detection over prerequisite graph. Asserts 0 cycles and chronological order. |
| **T4.1** | 4 | M5 | F30 | Student Navigation Simulation | Acceptance § 1 | Simulates continuous student navigation path from Dashboard to all hubs and appendices. |
| **T4.2** | 4 | M5 | F30 | Degree Pathways Completion Simulation | Acceptance § 1, 2 | Simulates 4 career tracks; verifies prerequisite resolution and workload (3k–7.5k hrs). |
| **T4.3** | 4 | M5 | F30 | Daily Study Routine Simulation | Acceptance § 3 | Simulates study routine cross-referencing (`how-i-study`, `log`, `Checklist`, templates). |
| **T4.4** | 4 | M3 | F25 | Project Build Progression Simulation | F25, Survey 3 | Validates `05 - Projects/Projects Hub.md` course links, toolchains, and acceptance criteria. |
| **T4.5** | 4 | M5 | F30 | Master Curriculum Audit Simulation | Acceptance § 1 | Asserts synchronization across `00 - Dashboard.md`, `Checklist.md`, and `Gap Analysis`. |

---

## 4. Test Runner CLI Usage & Execution Options

The test runner script is located at:
```bash
/home/noblixy/The Noblett Repository/.agents/test_suite/run_e2e_tests.py
```

### 4.1 Global Test Execution (All 53 Test Cases)
To run the complete verification suite in strict enforcement mode:
```bash
python3 .agents/test_suite/run_e2e_tests.py
```
*Note: Exits with code 0 on full success; exits with code 1 if any evaluated test fails.*

### 4.2 Progressive Milestone Gate Evaluation
To evaluate whether a specific milestone's deliverables satisfy acceptance criteria:
```bash
# Evaluate Milestone 1 (Graph & Link Integrity: F01–F07)
python3 .agents/test_suite/run_e2e_tests.py --milestone M1

# Evaluate Milestone 2 (Formatting, Frontmatter & Consistency: F08–F16)
python3 .agents/test_suite/run_e2e_tests.py --milestone M2

# Evaluate Milestone 3 (Deduplication & Bidirectionality: F17–F26)
python3 .agents/test_suite/run_e2e_tests.py --milestone M3

# Evaluate Milestone 4 (Proofs & Stubs: F27–F29)
python3 .agents/test_suite/run_e2e_tests.py --milestone M4
```

### 4.3 Tier-Scoped Execution
```bash
# Execute only Tier 1 (Feature Coverage)
python3 .agents/test_suite/run_e2e_tests.py --tier 1

# Execute only Tier 2 (Boundary & Corner Cases)
python3 .agents/test_suite/run_e2e_tests.py --tier 2

# Execute only Tier 3 (Cross-Feature Interactions)
python3 .agents/test_suite/run_e2e_tests.py --tier 3

# Execute only Tier 4 (Real-World Workflows)
python3 .agents/test_suite/run_e2e_tests.py --tier 4
```

### 4.4 Diagnostic & Export Options
```bash
# Verbose diagnostic failure inspection (shows exact files, line numbers, and snippets)
python3 .agents/test_suite/run_e2e_tests.py -v

# Non-blocking baseline audit (prints full report, exits with code 0)
python3 .agents/test_suite/run_e2e_tests.py --baseline

# Export machine-readable JSON telemetry
python3 .agents/test_suite/run_e2e_tests.py --baseline --json-out .agents/test_suite/test_report.json

# Print complete 53-test catalog
python3 .agents/test_suite/run_e2e_tests.py --list-tests
```

---

## 5. Verification & Invalidation Conditions

### Verification Commands:
1. Verify the runner executes cleanly and exports valid JSON:
   ```bash
   python3 .agents/test_suite/run_e2e_tests.py --baseline --json-out .agents/test_suite/test_report.json
   ```
2. Verify Milestone 1 passes 100%:
   ```bash
   python3 .agents/test_suite/run_e2e_tests.py --milestone M1
   ```

### Invalidation Conditions:
- Any broken wikilink in a non-template note reported as passing.
- Any orphaned non-template note remaining undetected by T1.6.
- Any unclosed code fence or math block delimiter remaining undetected by T2.4.
- Any cyclical prerequisite dependency remaining undetected by T3.6.
- Any failure of the runner to execute without external pip dependencies installed.
