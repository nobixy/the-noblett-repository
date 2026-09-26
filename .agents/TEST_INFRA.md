# EECS Curriculum Test Infrastructure Specification (TEST_INFRA)

**Document Version:** 1.0.0  
**Author:** E2E Curriculum Test Writer (`teamwork_preview_test_writer_e2e`)  
**Target Architecture:** The Noblett Repository Obsidian Vault  
**Test Suite Path:** `/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py`  
**Master Project Plan:** `/home/noblixy/The Noblett Repository/.agents/PROJECT.md`  
**Mission Reference:** `/home/noblixy/The Noblett Repository/.agents/ORIGINAL_REQUEST.md`  

---

## 1. Executive Overview & Test Philosophy

The Noblett Repository is a multi-year, elite, self-directed curriculum benchmarked against MIT Course 6 (Courses 6-1, 6-2, 6-3, 6-4, 6-5, and MEng 6-P), ACM/IEEE CS2023, and IEEE CE2016.

To ensure that the vault achieves 100% gap-free completeness, unyielding mathematical rigor, and flawless internal consistency, this automated test suite provides an **opaque-box E2E curriculum test harness**. The test harness treats curriculum notes, syllabi, link graphs, problem set proofs, and project build specifications as code artifacts subjected to compiler-level syntactic and semantic checks.

### Core Testing Principles:
1. **Opaque-Box Verification:** The test runner inspects only observable artifacts (markdown files, frontmatter properties, section headings, wikilinks, citations, prerequisite graphs, and mathematical proofs) without assuming internal implementation shortcuts.
2. **Progressive Testability:** The test suite evaluates features across milestones (M1: Baseline Gap Analysis & Core Bridges; M2: Horizontal Tracks 7–11; M3: Vertical Depth & Proofs; M4: Dual-Track Certification). Tests can be invoked globally or scoped by milestone.
3. **Deterministic & Zero-Dependency Execution:** The runner is implemented entirely in standard Python 3 (3.8+) using `pathlib`, `re`, `json`, `argparse`, and `dataclasses`. No external packages (`pip`) are required.
4. **Adversarial & Boundary Verification:** The suite tests for broken wikilinks, malformed YAML, prerequisite circular dependencies (cycles in the DAG), missing bibliographic metadata, and vague or unfalsifiable project specifications.

---

## 2. The 4-Tier Test Architecture

The verification suite is structured into four distinct, progressive verification tiers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   4-TIER CURRICULUM VERIFICATION SUITE                 │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 1: FEATURE COVERAGE & SCHEMA VALIDATION                           │
│  - Core Blocks (Phase -1, 0, Years 1–5, Bridges 04a, 08a, 15a)         │
│  - Baseline Gap Analysis Report (MIT Course 6, CS2023, CE2016)         │
│  - Specialization Tracks 1–11 & Specializations Hub                    │
│  - YAML Frontmatter Schema (block_id, hours_estimate, milestone, etc.)  │
│  - Structural Section Headers (Overview, Syllabus, Builds, Proofs)     │
│  - Track Interface Contract (Core Courses, Papers, Labs, Capstone)     │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 2: BOUNDARY & CORNER CASES                                        │
│  - Vault-Wide Wikilink Integrity (0 broken links across all notes)     │
│  - Graduate Literature Citations (>=3 full citations per track)        │
│  - Modern Paradigms Lab Specs (>=3 labs + 1 capstone with metrics)     │
│  - Paper Reading Hub Cross-Linkage                                     │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 3: CROSS-FEATURE COMBINATIONS                                     │
│  - Prerequisite Graph DAG Validation (DFS cycle detection: 0 cycles)   │
│  - Prerequisite Topological Chronological Ordering                     │
│  - ACM/IEEE CS2023 17 Knowledge Areas Audit (100% coverage)            │
│  - MIT Course 6 Foundational Pillars Audit (100% coverage)             │
│  - R2 Vertical Graduate Proofs Injection (>=5 proofs verified)         │
├────────────────────────────────────────────────────────────────────────┤
│ TIER 4: REAL-WORLD SCENARIOS                                           │
│  - Student Degree Pathways Simulation (4 career tracks, 3k-5k hours)   │
│  - Toolchain & Build Deliverable Validation (compilers, emulators)     │
│  - Master Checklist & Dashboard Alignment                              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Test Specification Matrix

| ID | Tier | Test Name | Target Requirements | Verification Method & Gate Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **T1.1** | 1 | Core Blocks Existence | R1, Project Plan § 2 | Scans vault for 38 mandatory files: Phase -1 (B0, BM, BW), Phase 0 (P1–P5), Year 1 (Blocks 01–08, 04a, 08a), Year 2 (Blocks 09–15, 15a), Year 3 (Blocks 16–22), Year 4 (Blocks 23–29), Year 5 (Blocks 30–32). Gate: 38/38 present. |
| **T1.2** | 1 | Baseline Gap Analysis Report | R1, Acceptance § 1 | Asserts `Baseline Gap Analysis and Audit Report.md` exists, size $\ge 10\,\text{KB}$, and contains audits for MIT Course 6, CS2023, CE2016, and core bridge course specifications. |
| **T1.3** | 1 | Specialization Tracks Existence | R3, Project Plan § 2 | Verifies existence of `Specializations Hub.md` and all 11 Specialization Tracks (Tracks 1 through 6 classical, Tracks 7 through 11 modern paradigms). |
| **T1.4** | 1 | Core Block Frontmatter Schema | Project Plan § Interface Contracts | Parses YAML frontmatter in all curriculum blocks. Asserts presence of `block_id`, `title`, `term`, `status`, `hours_estimate`, `primary_resource`, `milestone`. Asserts `hours_estimate > 0` and `status` in `[not-started, in-progress, done]`. |
| **T1.5** | 1 | Core Block Section Headers | `08 - Templates/Block Note Template.md` | Asserts presence of 7 standard Markdown section headings: Overview, Why This Matters, Primary Syllabus, Build Requirement, Done When, Study Notes & Proofs, and Appendix A Alternatives. |
| **T1.6** | 1 | Specialization Track Interface Schema | Project Plan § Interface Contracts | Validates that every specialization track note implements: Overview/Motivation, Core Courses (Course 1 & 2), Seminal Papers & Advanced Textbooks, Progressive Labs, and Capstone Build Deliverable. |
| **T2.1** | 2 | Vault-Wide Wikilink Integrity | Acceptance § 1 | Extracts all `[[wikilinks]]` across the entire vault. Resolves targets using Obsidian relative path, stem, and suffix rules. Asserts **0 broken links**. Reports line numbers and source files for broken targets. |
| **T2.2** | 2 | Graduate Literature Citations | Acceptance § 2 | Inspects every Specialization Track note. Asserts each contains **at least 3 graduate-level theoretical papers or advanced textbooks** with full bibliographic citations (Author, Year, Title, Venue/Publisher). |
| **T2.3** | 2 | Modern Paradigms Lab & Project Specs | Acceptance § 2 | Evaluates modern paradigm tracks (Tracks 7–11). Asserts that **at least 2 modern paradigm tracks** have $\ge 3$ progressive labs and 1 capstone build with quantitative, measurable acceptance criteria (latency, jitter, memory, proof checks). |
| **T2.4** | 2 | Paper Reading Hub Cross-Linkage | R2, Project Plan § 2 | Audits `03 - Papers/Paper Reading Hub.md`. Verifies it links research papers to curriculum blocks via active wikilinks. |
| **T3.1** | 3 | Prerequisite Graph DAG Validation | Acceptance § 1 | Constructs the directed prerequisite graph across all blocks. Executes cycle detection via Depth-First Search. Asserts graph is a strictly acyclic Directed Acyclic Graph (DAG) with **0 cycles**. |
| **T3.2** | 3 | Prerequisite Topological Ordering | Acceptance § 1 | Verifies chronological ordering: Every prerequisite course must belong to an academic term earlier than or equal to the dependent course. Asserts zero prerequisite time inversions. |
| **T3.3** | 3 | ACM/IEEE CS2023 17 KAs Audit | Acceptance § 1 | Cross-references curriculum against all 17 ACM/IEEE CS2023 Knowledge Areas: AL, AR, AI, DM, FPL, GIT, HCI, MSF, NC, OS, PDC, SEC, SEP, SDF, SE, SPD, SF. Asserts 100% formal coverage. |
| **T3.4** | 3 | MIT Course 6 Canonical Pillars Audit | R1, Acceptance § 1 | Audits vault coverage of canonical MIT EECS pillars: 6.2000 Circuits, 6.3000 Signals, 18.03 Differential Equations, 6.1910 Computation Structures, 6.1810 OS, 6.1210 Algorithms, 6.5840 Distributed Systems, 6.1020 Software Construction, 6.1400 Theory of Computation, 6.3900 ML, 18.06 Linear Algebra, 6.3700 Probability. Asserts 100% coverage. |
| **T3.5** | 3 | Graduate Proofs & Derivations Injection | R2 | Scans core blocks for foundational graduate proofs (Carathéodory, Radon-Nikodym, KKT, Baire Category, Yoneda, Cook-Levin, Cheeger, LWE, FLP, Picard-Lindelöf). Asserts presence of step-by-step mathematical proofs. |
| **T4.1** | 4 | Student Degree Pathways Simulation | Acceptance § 1, 2 | Simulates 4 diverse student career specialization trajectories through the 5-year sequence. Verifies prerequisite satisfaction, workload pacing ($3,000 \le \text{total hours} \le 7,500$), and capstone integration. |
| **T4.2** | 4 | Toolchain & Build Deliverable Validation | Acceptance § 2 | Audits all build requirements and lab specifications. Asserts that $\ge 60\%$ specify concrete engineering tools, compilers, simulators, or hardware instruments (gcc, clang, rustc, cargo, qemu, renode, pytest, lean, verilog, ltspice, etc.). |
| **T4.3** | 4 | Master Checklist & Dashboard Alignment | Project Plan § 2 | Validates that `Checklist.md` and `00 - Dashboard.md` are synchronized with curriculum blocks, telemetry data, and navigation hubs. |

---

## 4. Test Runner CLI Usage & Options

The test runner script is located at:
```bash
/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py
```

### 4.1 Global Test Execution (All 4 Tiers)
To run the complete verification suite across all 18 test cases:
```bash
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py"
```

### 4.2 Verbose Diagnostic Execution
To view granular per-file line numbers, broken link details, citation counts, and proof locations:
```bash
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" -v
```

### 4.3 Tier-Specific Execution
To execute specific tiers during incremental development:
```bash
# Run only Tier 1 (Feature Coverage)
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" --tier 1

# Run Tier 1 and Tier 2
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" --tier 1,2

# Run Tier 3 (Cross-Feature Combinations & Standards)
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" --tier 3
```

### 4.4 Milestone Progressive Mode
To validate features delivered in specific implementation milestones:
```bash
# Evaluate Milestone 1: Baseline Gap Analysis & Core Bridge Syllabi
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" --milestone M1

# Evaluate Milestone 2: Modern Paradigm Tracks 7–11
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" --milestone M2

# Evaluate Milestone 3: Vertical Graduate Injections & Proofs
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" --milestone M3

# Evaluate Milestone 4: Dual-Track Independent Verification
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" --milestone M4
```

### 4.5 Machine-Readable JSON Export
To generate a machine-readable JSON report for downstream auditor agents, the independent judge, or CI pipelines:
```bash
python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" --json-out "/home/noblixy/The Noblett Repository/.agents/test_suite/test_results.json"
```

---

## 5. Defect Escalation & QA Protocols

As the E2E Test Writer, our role is strictly confined to test code, test infrastructure, and test execution reports. We do **not** modify curriculum vault implementation files directly.

When the test runner reports failures:
1. **Milestone Progress Deficiencies:** Expected failures for components currently in progress by other workers are categorized by milestone (e.g., M2 tracks, M3 proofs).
2. **Implementation Bugs in Delivered Files:** If an already delivered file contains defects (e.g. broken wikilinks in bridge courses, missing frontmatter fields), the issue is documented in the test diagnostics and escalated directly to the implementing worker or orchestrator.
3. **Certification Gate:** A milestone or the complete curriculum cannot be declared `TEST_READY` or certified by the independent judge until all targeted test cases produce a green `[PASS]` verdict with exit code 0.
