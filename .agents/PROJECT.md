# Project: Vault Comprehensive Quality Pass
Target Vault: `/home/noblixy/The Noblett Repository`

## Architecture
The vault is organized following the Johnny.Decimal information architecture:
- `00 - Dashboard.md`: Top-level navigational hub, current status, telemetry, master subsystem links.
- `01 - Curriculum/`: Complete EECS curriculum (Phase -1 Bedrock, Phase 0 Prerequisites, Years 1–5 Blocks 01–32, 3 Bridge Syllabi, Specializations Hub + 11 Tracks, Baseline Gap Analysis).
- `02 - Notes/`: Zettelkasten domain atomic note indices (Hardware, Languages, Math, Systems, Theory).
- `03 - Papers/`: Paper Reading Hub (35 landmark PhD papers mapped to curriculum blocks).
- `04 - Writing/`: Writing Hub (writing deliverables, protocols).
- `05 - Projects/`: Projects Hub (course and track engineering builds).
- `06 - Breadth/`: Breadth and Humanities Hub (HASS subjects and language acquisition).
- `07 - Reference/`: Curated reference appendices (Appendix E Failure Modes, Appendix F Curated URLs, Reference PDF).
- `08 - Templates/`: Reusable note, study, log, and project templates.
- `09 - Mindset & Habits/`: Mindset Hub (behavioral protocols and mental models).
- Root files: `Checklist.md`, `Your Shelf.md`, `how-i-study.md`, `log.md`, `Telemetry Log.md`.

## Feature Inventory
Every defect, requirement, and quality standard identified during the Phase 0 Survey is inventoried below and mapped to a specific milestone.

| # | Feature / Work Item | Description | Milestone | Source |
|---|---------------------|-------------|-----------|--------|
| F01 | Repair Bedrock Path Errors | Fix 12 dead wikilinks in `00 - Dashboard.md`, `Checklist.md`, `log.md`, `Your Shelf.md` omitting `01 - Curriculum/` | M1 | Survey 1 |
| F02 | Repair Escaped Table Pipes | Fix 14 dead wikilinks in `Your Shelf.md` containing `\|` table escaping artifacts | M1 | Survey 1 |
| F03 | Fix Template Dummy Placeholders | Format or escape `[[{{block_id}}]]`, `[[{{associated_block}}]]`, `[[Related Note 1]]`, `[[Related Note 2]]` in `08 - Templates/` | M1 | Survey 1 |
| F04 | Remove Root Agent Prompt File | Delete redundant `/home/noblixy/The Noblett Repository/ORIGINAL_REQUEST.md` (removes dead `[[wikilink]]` and root orphan) | M1 | Survey 1, 3 |
| F05 | Eliminate Non-Template Orphan Notes | Connect all 10 unlinked domain notes (`Checklist`, `Your Shelf`, `Baseline Gap Analysis`, 5 `02 - Notes/` indices, Appendices E & F) to `00 - Dashboard.md` | M1 | Survey 1, 3 |
| F06 | Link Templates from Parent Hubs | Connect templates to `how-i-study.md`, `log.md`, `Checklist.md`, and `02 - Notes/` | M1 | Survey 1, 3 |
| F07 | Full Dashboard Graph Reachability | Ensure 100% of non-template notes are reachable from `00 - Dashboard.md` | M1 | Survey 1 |
| F08 | Fix Blocks 31 & 32 Header & ID Desync | Correct `block_id` and H1 in `31 - Specialization B2.md` and `32 - Information Theory.md` to prevent stutter title | M2 | Survey 2 |
| F09 | Un-backtick Wikilinks Across Vault | Replace 95 backticked wikilinks `` `[[...]]` `` with active interactive `[[...]]` across 16 files | M2 | Survey 2 |
| F10 | Synchronize Block Note Template | Align H2 headings in `08 - Templates/Block Note Template.md` with the 35 core course notes | M2 | Survey 2 |
| F11 | Repair Telemetry Log Table Syntax | Remove orphaned table header on lines 7–8 in `Telemetry Log.md` to restore valid list formatting for Dataview | M2 | Survey 2, 3 |
| F12 | Frontmatter Schema Standardization | Standardize YAML frontmatter schemas across Tracks (list prerequisites, status: not-started), Hubs, and Indices | M2 | Survey 2 |
| F13 | Fenced Code Block Language Tagging | Tag 18 bare code blocks (ASCII architecture diagrams, terminal logs) with `text` or `bash` | M2 | Survey 2 |
| F14 | Clean Raw HTML Tags | Remove or replace 35 `<br>` tags in `03 - Papers/Paper Reading Hub.md` table cells | M2 | Survey 2 |
| F15 | List Indentation Normalization | Normalize 3-space and 5-space indents to standard 2/4-space hierarchy across 17 files | M2 | Survey 2 |
| F16 | Mathematical Proof Q.E.D. Consistency | Ensure all formal derivations conclude with standard $\blacksquare$ tombstone marker (adding to Blocks 22, 25) | M2 | Survey 2 |
| F17 | Sanitize Baseline Gap Analysis Note | Remove worker ID (`teamwork_preview_worker_m1`), link to `.agents/PROJECT.md`, and milestone roadmap labels | M3 | Survey 3 |
| F18 | Deduplicate Specialization Matrices | In Blocks 26, 28, 29, 31, replace repeated 11-track matrices with reference to `[[Specializations Hub]]` | M3 | Survey 3 |
| F19 | Deduplicate Mindset & Habit Definitions | Consolidate duplicate Grit, Growth Mindset, Deep Work definitions between `how-i-study.md` and `Mindset Hub.md` | M3 | Survey 3 |
| F20 | Deduplicate Generalization Bounds | Cross-reference Rademacher/McDiarmid proofs between `22 - Statistics.md` and `Track 1 - AI and Machine Learning.md` | M3 | Survey 3 |
| F21 | Relocate & Cross-Link FLP & Vector Clocks | Cross-reference FLP Impossibility and Vector Clocks in `16 - Operating Systems` with `23 - Distributed Systems` and `Paper Reading Hub` | M3 | Survey 3 |
| F22 | Specialization Track Bidirectional Links | Add bidirectional navigation headers/footers in all 11 tracks linking back to `Specializations Hub` and Blocks 26/28/29/31 | M3 | Survey 3 |
| F23 | Curriculum Block Landmark Paper Sections | In all assigned curriculum blocks, add dedicated `### 📄 Landmark Research Papers` linking to `Paper Reading Hub` | M3 | Survey 3 |
| F24 | Curriculum Block Topic Index Links | In curriculum blocks, add links to corresponding `02 - Notes/` topic indices (Math, Systems, Theory, Hardware, Languages) | M3 | Survey 3 |
| F25 | Projects Hub Wikilink Integration | Upgrade `05 - Projects/Projects Hub.md` with active wikilinks for all 32 blocks + 3 bridge blocks + 11 track capstones | M3 | Survey 3 |
| F26 | Eliminate Course Block Sinks | Add breadcrumb headers and sequential navigation footers to all 31 out-degree=0 course blocks | M3 | Survey 1, 3 |
| F27 | Populate 13 Empty Proof Stubs | Replace empty placeholder lines in Blocks 01–09, 12, 14, 19, 27 with authentic derivations and concept checklists | M4 | Survey 3 |
| F28 | Expand Bridge Block Proof Prompts | Expand homework prompts in `04a`, `08a`, `15a` into full, rigorous textbook proof derivations | M4 | Survey 3 |
| F29 | Complete Time Hierarchy Theorem Proof | Provide full diagonalization reduction proof for Time Hierarchy Theorem in `24 - Theory of Computation.md` | M4 | Survey 3 |
| F30 | 100% E2E Quality Suite Pass | Pass 100% of tests in the E2E quality test suite (Tiers 1–4) covering links, orphans, formatting, and stubs | M5 | Acceptance Criteria |
| F31 | Adversarial Coverage Hardening | Run Tier 5 white-box challenger analysis and verify 0 remaining gaps | M5 | Project Pattern |

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Vault Graph & Link Integrity | F01, F02, F03, F04, F05, F06, F07 | None | DONE |
| M2 | Formatting, Frontmatter & Structural Consistency | F08, F09, F10, F11, F12, F13, F14, F15, F16 | M1 | DONE |
| M3 | Content Deduplication, Sanitization & Bidirectionality | F17, F18, F19, F20, F21, F22, F23, F24, F25, F26 | M1, M2 | DONE |
| M4 | Stub Resolution & Proof Completion | F27, F28, F29 | M2, M3 | DONE |
| M5 | E2E Quality Pass & Hardening (Final Milestone) | F30, F31 (Pass 100% E2E test suite + Tier 5 adversarial hardening) | M1, M2, M3, M4, TEST_READY | DONE |
| E2E | E2E Testing Track (Parallel) | Design test harness & runner; implement Tiers 1–4 test cases; publish TEST_READY.md | Survey (Phase 0) | DONE |

## Interface Contracts

### Navigation Hub ↔ Note Resolution Contract
- All cross-note links must use wikilink format: `[[Basename]]` or `[[Basename|Custom Alias]]`.
- Folder paths inside wikilinks are permitted only if necessary, but bare basenames are preferred because all 85 note basenames are globally unique.
- Wikilinks MUST NEVER be wrapped in backticks (e.g. `[[Note]]` NOT `` `[[Note]]` ``).
- In markdown tables, pipes inside wikilinks must NOT be escaped with backslashes (use `[[Target|Alias]]` NOT `[[Target\|Alias]]`).
- Every non-template note must be reachable from `00 - Dashboard.md` via directed wikilink traversal.

### YAML Frontmatter Schema Contract
- **Curriculum Block Notes (`01 - Curriculum/`)**:
  Required keys: `block_id`, `title`, `term`, `status` (`not-started` | `in-progress` | `done`), `hours_estimate`, `hours_actual`, `primary_resource`, `milestone`, `date_started`, `date_completed`.
  Header H1 MUST match: `# <block_id> — <title>` (e.g. `# Block 31 — Specialization Track B — Course 2`).
- **Specialization Tracks (`01 - Curriculum/Specializations/`)**:
  Required keys: `track_id`, `title`, `term`, `status` (`not-started`), `target_profile`, `prerequisites` (YAML list of wikilinks), `aliases` (YAML list of string titles).
  Header H1 MUST match: `# Track <N>: <title>`.
- **Hub & Index Notes (`00 - Dashboard`, `02 - Notes/`, `03 - Papers/`, etc.)**:
  Required keys: `title`, `type` (`hub` | `index`), `tags` (`[hub, navigation]` or `[index, navigation]`).

### Content Quality & Proof Contract
- No section may contain empty placeholder text, TODO stubs, or parenthetical directives (`*(Atomic notes, problem set proofs...)*`).
- Every proof section (`## 📝 Study Notes, Psets & Proofs`) must provide complete, step-by-step mathematical or architectural derivations.
- Every formal proof must conclude with a standard Q.E.D. tombstone: `$\blacksquare$`.
- No raw agent artifacts, internal orchestrator IDs (`teamwork_preview_worker_*`), or `.agents/` paths may appear in vault markdown files.

## Code Layout
- Vault Root: `/home/noblixy/The Noblett Repository/`
- Markdown notes: All `.md` files outside `.agents/`
- Agent metadata: `/home/noblixy/The Noblett Repository/.agents/` (strictly metadata and tests)
- E2E Test Suite: `/home/noblixy/The Noblett Repository/.agents/test_suite/`
