---
title: "DR-002: Vault Refactor and Canonical Numbering"
type: decision-record
status: accepted
date: 2026-10-09
accepted: 2026-10-09
tags:
  - adr
  - decision-record
---

# DR-002: Vault Refactor and Canonical Numbering

*Uses the [[Decision Record]] template. Follows [[DR-001 - Program Scope, Phases, and Timeline|DR-001]]. Accepted and applied 2026-10-09. Checkpoint before the refactor: git commit `46f92ca`.*

## Context
After the DR-001 review, four structural problems were left:
1. **Two numbering systems.** The [[Checklist]], the source PDF, [[how-i-study]] ("Apply after Block 12") and the Projects Hub used the program's numbering (CS61A = Block 1). Note titles and `block_id` used a second numbering from a migration script (CS61A = Block 10, tracks = Blocks 42–56). The Checklist also skipped Block 31.
2. **Inconsistent frontmatter.** Category values were `core`, `advanced` and `specialization`. 13 notes lacked `primary_resource`/`milestone`, three tracks lacked `track_id` and used "Track N - …" titles, prerequisites used aliases, and the Capstone and Cryptopals listed no prerequisites.
3. **Four blocks outside the plan.** AI, Intro ML, Computer Security and Parallel Computing were marked Tier 1 Core and counted in the hours, but the source program never schedules them. Two of them were stubs.
4. **Thin hubs and a missing branch.** Engineering Practice, Human Systems and the Employability Portfolio were bare outlines. The portfolio required a full-stack web app that no note taught.

Also, 16 one-off scripts in the vault root could silently undo fixes if re-run.

## Decision
1. **The Checklist/PDF numbering is canonical.** `block_id` and every note title (`# {id} — …`) now use: `B0`, `BM`, `BW` (Phase −1); `P1`–`P5` (Phase 0); `Block 1`–`Block 30` as in the source; bridges `Block 4a/8a/15a`; `Block 27` = January intensive; `Block 30` = Capstone; `Block 32` = Information Theory; `E1`–`E4` = optional electives; `Track 1`–`Track 15` = specializations (with `track_id` equal to `block_id`). File names are unchanged, so no links moved.
2. **Block 31 is Specialization B, Course 2.** The source program describes it in Year 5 alongside the Capstone, but never gives it a number. The Projects Hub and the track notes already called it Block 31, so the Checklist now labels it that way. Information Theory stays Block 32 (Year 5 reading).
3. **One frontmatter schema** for every block note: `block_id, title, category, term, status, prerequisites, hours_estimate, hours_actual, primary_resource, milestone, date_started, date_completed, tier`. Optional extras are `optional`, plus `track_id`, `target_profile` and `aliases` for tracks.
   - `category` is one of `core`, `elective` or `specialization`.
   - Missing `primary_resource`/`milestone` values were filled from each note's own Core Courses and Capstone Build sections, never invented.
   - Prerequisites use exact note names.
   - Cryptopals (Block 27) now requires Math for CS and Distributed Systems (the TLA+ option specs the Block 23 Raft).
   - The Capstone (Block 30) requires the Year 4 core blocks (23, 24, 25, 27).
   - The [[Block Note Template]] matches this schema.
4. **AI, Intro ML, Computer Security and Parallel Computing become optional electives E1–E4** (`optional: true`, Tier 3), because the source program doesn't schedule them. They sit in their own Checklist section and are left out of the hour budget. Computer Security is rebuilt around MIT 6.1600 (Foundations of Computer Security) and Intro ML around MIT 6.036/6.3900, both checked against the official course pages.
5. **Track 15, [[Full-Stack and Product Engineering]]**, is added: Full Stack Open (Helsinki) plus Berkeley CS169A or MIT 6.1040. Its Parts 0–5 are the minimum for the portfolio's web-app project, whether or not it's one of the two chosen tracks. [[03 - Engineering Practice]], [[04 - Human Systems]] and [[Employability Portfolio and Review]] are fleshed out. Each skill is tied to the block that teaches it, Human Systems stays generic (Rule 9), and the portfolio has a "Done when".
6. **One-off scripts move to `99 - Archive/Scripts/`** with a do-not-run warning. `verify_curriculum.py` is rewritten as the single read-only checker (links, numbering, schema, prerequisites, headings, Sequential Flow chain, planned hours).

## Status
**Accepted**: 2026-10-09.

## Consequences
**Easier:** a block number now means the same thing everywhere (Checklist, notes, Projects Hub, how-i-study, DRs). `python3 verify_curriculum.py` gives a pass/fail for the whole curriculum. The Dashboard total is a real budget.

**Harder / costs:** old block numbers in `99 - Archive` (Worked Proofs, gap report) and in git history no longer match the notes. Any new block note must follow the schema, or verify fails.

**Hours:** with E1–E4 out of the budget, the Dashboard's planned total is **5,125 h** today. That's ≈5,925 h once two tracks are chosen, and the habits bring it to ≈6,500–8,000 h. This updates the ≈6,485 figure in DR-001, which counted the electives.
