# Dispatch: Worker M3 (Content Deduplication, Sanitization & Bidirectionality)

- Working directory: `/home/noblixy/The Noblett Repository/.agents/worker_m3`
- Original Request path: `/home/noblixy/The Noblett Repository/.agents/ORIGINAL_REQUEST.md`
- Master Project plan: `/home/noblixy/The Noblett Repository/.agents/PROJECT.md` (Features F17–F26)
- Survey Reports:
  - `/home/noblixy/The Noblett Repository/.agents/explorer_survey_3/handoff.md`
  - `/home/noblixy/The Noblett Repository/.agents/explorer_survey_1/handoff.md`
  - `/home/noblixy/The Noblett Repository/.agents/worker_m2/handoff.md`
- Test Runner:
  - `python3 .agents/test_suite/run_e2e_tests.py --milestone M3`

Scope / Tasks (Features F17–F26):
1. F17 (Sanitize Baseline Gap Analysis):
   - In `01 - Curriculum/Baseline Gap Analysis and Audit Report.md`:
     - Remove worker ID `teamwork_preview_worker_m1` (line 4).
     - Replace `.agents/PROJECT.md` cross-boundary link (line 8) with internal vault curriculum roadmap.
     - Sanitize ASCII roadmap labels (lines 241–264) from internal milestone names ("Milestone 1 — Current", etc.) to canonical phase titles ("Phase 1: Core Bridge Syllabi", "Phase 2: Specialization Tracks", "Phase 3: Graduate Depth", "Phase 4: Capstone & Verification").
     - Sanitize line 317 to remove internal milestone references.
2. F18 (Deduplicate Specialization Matrices):
   - In `26 - Specialization A1.md`, `28 - Specialization A2.md`, `29 - Specialization B1.md`, and `31 - Specialization B2.md`:
     Replace the duplicated 11-bullet track lists with a clean, unified reference delegating to `[[01 - Curriculum/Specializations/Specializations Hub|Specializations Hub]]`.
3. F19 (Deduplicate Mindset & Habit Definitions):
   - In `how-i-study.md` Section 7, retain the core study philosophy and link to `[[09 - Mindset & Habits/Mindset Hub|Mindset Hub]]` for detailed behavioral protocols, removing duplicate definitions of Grit, Growth Mindset, and Deep Work.
4. F20 (Deduplicate Generalization Bounds):
   - In `Track 1 - AI and Machine Learning.md`, cross-link Proof 2 with `[[22 - Statistics]]` (VC-dimension & generalization bounds), focusing Track 1 on neural network contractions.
5. F21 (Cross-Link FLP & Vector Clocks):
   - In `16 - Operating Systems.md`, add cross-reference to `[[23 - Distributed Systems]]` and `[[03 - Papers/Paper Reading Hub|Paper Reading Hub]]` (Papers 21 & 22) for FLP Impossibility and Vector Clocks.
6. F22 (Specialization Track Bidirectional Links):
   - In each of the 11 tracks (`01 - Curriculum/Specializations/Track *.md`), add a navigation header/footer linking back to `[[01 - Curriculum/Specializations/Specializations Hub|Specializations Hub]]` and specifying its assignment slots in Blocks 26/28 or 29/31.
7. F23 (Curriculum Block Landmark Paper Sections):
   - In all assigned curriculum blocks (`09`, `10`, `11`, `13`, `14`, `15`, `16`, `17`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `27`, `32`), add a dedicated subsection:
     `### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])`
     explicitly listing the assigned paper with reading guidance.
8. F24 (Curriculum Block Topic Index Links):
   - In curriculum blocks, add cross-links to their parent topic indices in `02 - Notes/` (e.g. `02 - Calculus I` -> `[[02 - Notes/Math/Math Index|Math Index]]`; `09 - Computer Systems` -> `[[02 - Notes/Systems/Systems Index|Systems Index]]`).
9. F25 (Projects Hub Wikilink Integration):
   - In `05 - Projects/Projects Hub.md`, upgrade all project headers/references with active wikilinks to their blocks (`[[01 - CS61A]]`, `[[04 - Nand2Tetris]]`, etc.), include the 3 bridge builds (`04a`, `08a`, `15a`), and link the 11 Specialization Track Capstones.
10. F26 (Eliminate Course Block Sinks):
    - In all 31 core course blocks with out-degree = 0, add navigation breadcrumb headers (`[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]]`) and sequential navigation footers (`[[Previous Block]] ← Overview → [[Next Block]]`) so no dead ends remain.

Mandatory Integrity Warning:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## 2026-09-25T10:55:15Z
You are Worker M3 (Content Deduplication, Sanitization & Bidirectionality Worker) in the comprehensive quality pass for `/home/noblixy/The Noblett Repository`.
Your working directory is: `/home/noblixy/The Noblett Repository/.agents/worker_m3`.
You MUST read the authoritative request at: `/home/noblixy/The Noblett Repository/.agents/ORIGINAL_REQUEST.md`.
You MUST read the master project plan at: `/home/noblixy/The Noblett Repository/.agents/PROJECT.md` (Features F17–F26).
You MUST read the survey handoffs:
- `/home/noblixy/The Noblett Repository/.agents/explorer_survey_3/handoff.md` (authoritative deduplication, boilerplate & bidirectionality inventory)
- `/home/noblixy/The Noblett Repository/.agents/explorer_survey_1/handoff.md`
- `/home/noblixy/The Noblett Repository/.agents/worker_m2_remediation/handoff.md`

Test Runner:
- `python3 .agents/test_suite/run_e2e_tests.py --milestone M3`

Scope / Tasks (Features F17–F26):
1. F17 (Sanitize Baseline Gap Analysis):
   - In `01 - Curriculum/Baseline Gap Analysis and Audit Report.md`:
     - Line 4: Remove `teamwork_preview_worker_m1` (replace with formal author credit e.g. `Curriculum Working Group & Audit Committee`).
     - Line 8: Replace `.agents/PROJECT.md` cross-boundary link with `[[00 - Dashboard|Dashboard]]` or link to curriculum roadmap.
     - Lines 241–264: In the ASCII roadmap, replace internal milestone labels ("Milestone 1 — Current", "Milestone 2", "Milestone 3", "Milestone 4") with standard curriculum phase names ("Phase 1: Core Bridge Syllabi", "Phase 2: Specialization Tracks", "Phase 3: Graduate Mathematical Foundations & PhD Seminars", "Phase 4: Capstone Engineering & Independent Verification").
     - Line 317: Sanitize sentence to remove internal milestone references.
2. F18 (Deduplicate Specialization Matrices):
   - In `01 - Curriculum/Year 4 - Specialization/26 - Specialization A1.md`, `28 - Specialization A2.md`, `29 - Specialization B1.md`, and `01 - Curriculum/Year 5 - MEng/31 - Specialization B2.md`:
     Replace the repeated, identical 11-bullet specialization lists with a clean, cohesive track-binding section delegating the catalog to `[[01 - Curriculum/Specializations/Specializations Hub|Specializations Hub]]`. Specify each block's distinct role (A1 = Primary Track Course 1; A2 = Primary Track Course 2; B1 = Secondary Track Course 1; B2 = Secondary Track Course 2).
3. F19 (Deduplicate Mindset & Habit Definitions):
   - In `how-i-study.md` Section 7, retain the core high-level philosophy and cross-link to `[[09 - Mindset & Habits/Mindset Hub|Mindset Hub]]` for the full behavioral protocols, removing word-for-word duplicated definitions of Grit, Growth Mindset, and Deep Work.
4. F20 (Deduplicate Generalization Bounds):
   - In `01 - Curriculum/Specializations/Track 1 - AI and Machine Learning.md`, cross-link Proof 2 with `[[22 - Statistics]]` (VC-dimension & generalization bounds), focusing Track 1 on deep neural network contraction bounds (Talagrand's lemma) rather than repeating the tabular Rademacher bound derivation.
5. F21 (Cross-Link FLP & Vector Clocks):
   - In `01 - Curriculum/Year 3 - Depth/16 - Operating Systems.md`, add cross-reference to `[[23 - Distributed Systems]]` and `[[03 - Papers/Paper Reading Hub|Paper Reading Hub]]` (Papers 21 & 22) for the distributed consensus and logical clock derivations.
6. F22 (Specialization Track Bidirectional Links):
   - In each of the 11 tracks (`01 - Curriculum/Specializations/Track *.md`), add a navigation header or footer linking back to `[[01 - Curriculum/Specializations/Specializations Hub|Specializations Hub]]` and specifying its assignment slots in Blocks 26/28 or 29/31.
7. F23 (Curriculum Block Landmark Paper Sections):
   - In all assigned curriculum blocks (Blocks 09, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 27, 32), add a dedicated subsection:
     `### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])`
     explicitly listing the assigned paper with reading guidance per `Paper Reading Hub.md`.
8. F24 (Curriculum Block Topic Index Links):
   - In curriculum blocks, add cross-links to their parent topic indices in `02 - Notes/` (e.g. `02 - Calculus I` -> `[[02 - Notes/Math/Math Index|Math Index]]`; `09 - Computer Systems` -> `[[02 - Notes/Systems/Systems Index|Systems Index]]`).
9. F25 (Projects Hub Wikilink Integration):
   - In `05 - Projects/Projects Hub.md`, upgrade all project references with active wikilinks to their blocks (`[[01 - CS61A]]`, `[[04 - Nand2Tetris]]`, etc.), include the 3 bridge builds (`04a`, `08a`, `15a`), and link the 11 Specialization Track Capstones.
10. F26 (Eliminate Course Block Sinks):
    - In all 31 core course blocks with out-degree = 0, add navigation breadcrumb headers (`[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]]`) and sequential navigation footers (`[[Previous Block]] ← Overview → [[Next Block]]`) so that 0 sink nodes remain.

