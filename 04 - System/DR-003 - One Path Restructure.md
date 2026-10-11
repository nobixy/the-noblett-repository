---
title: "DR-003: One Path Restructure"
type: decision-record
status: superseded
superseded_by: [DR-010, DR-011]
date: 2026-10-09
accepted: 2026-10-09
tags:
  - adr
  - decision-record
---

# DR-003: One Path Restructure

> [!WARNING] Superseded
> Superseded by [[DR-010 - Project-First Original Curriculum|DR-010]] and [[DR-011 - Sectioned Curriculum and Frontmatter Schema|DR-011]]. Kept as a historical record: its dates, hours, weeks, phases and links into `99 - Archive/` describe the v1 plan and are not current instructions.

*Uses the [[Decision Record]] template. Follows [[DR-002 - Vault Refactor and Canonical Numbering|DR-002]]. Accepted and applied 2026-10-09. Checkpoint before the restructure: git commit `0c7e704`.*

## Context
After DR-002 the content was consistent, but the structure was hard to follow:
1. **Folders by subject, study by order.** Block notes sat in `Foundations/…/Core` and `EECS Core/<subject>/Core|Advanced`. The next block was never in the same folder as the current one, and the subject folders said nothing about when to study a note.
2. **Three hubs for one job.** The Dashboard (progress, North Star, now/next), the Checklist (the ordered list) and Start Here (system overview, Core Spine, rules) overlapped and linked to each other. The 5-phase Core Spine was a second ordering on top of the Checklist's 7 stages.
3. **No obvious root.** Nothing told a reader (or GitHub) which note to open first.

## Decision
1. **Folders follow study order.** `01 - Curriculum/` holds one folder per stage, in Checklist order: `00 - Phase -1 Bedrock`, `01 - Phase 0 Prerequisites`, `02 - Year 1` … `06 - Year 5`, `07 - Optional Electives`, `08 - Specialization Tracks`, plus `09 - Supporting Systems` ([[Engineering Practice]], [[Human Systems]]). The Year 1–5 split follows the Checklist, by block number (1–8a, 9–15a, 16–22, 23–29, 30–32). The [[Employability Portfolio and Review|Employability Portfolio]] sits in Year 4 (due by its end) and [[Specialization Branches]] with the tracks.
2. **File names carry the canonical number** (DR-002): `B0/BM/BW`, `P1`–`P5`, `B01`–`B32` (bridges `B04a/B08a/B15a`), `E1`–`E4`, `T01`–`T15`, then a short name (e.g. `B01 - CS61A`). The three supporting hubs drop their `03/04/05 -` prefixes. Every wikilink, prerequisite and Sequential Flow link was rewritten; links that had no alias keep their old display text as an alias. Each note's old name is kept in `aliases` for search.
3. **Subject becomes metadata.** Every block note has `subject:` (English, Mathematics, Meta-Learning, Computer Science, Software Engineering, Computer Engineering, Electrical Engineering; Specialization for tracks; Capstone). The empty subject folders were removed.
4. **One hub: [[00 - Start Here]]** at the vault root. It merges the Dashboard (now/next, quick links, progress by status and by stage, telemetry, Phase −1 routines, vault index), the Checklist (the full ordered list by stage with checkboxes, deliverables, habits tally) and Start Here (system architecture, maintenance tracks, North Star, budget, five rules, guardrails, Operating Rules 1–10). Wording was kept; only cross-references between the old hubs were changed.
5. **The Core Spine becomes markers on The Path.** Each job-ready block gets 💼1–💼5 on its Path line and `job_ready: <phase>` in frontmatter. Phase 1: P3, P4, Block 1. Phase 2: Block 10. Phase 3: Blocks 4, 6, 9, 14. Phase 4: Blocks 12, 13, 16, 19. Phase 5: Blocks 17, 21, 23, closed by the Employability Portfolio. SICP (Block 5, "optional depth" in the old spine) stays unmarked. Study order is the list order.
6. **Old hubs are retired as redirect stubs** in `99 - Archive/Redirects/` (`00 - Dashboard`, `Checklist`), each pointing to [[00 - Start Here]]. Their full last versions are in commit `0c7e704`. DR-001 and DR-002 keep their original hub links, which now land on those stubs, so the records still read as written.
7. **A root `README.md`** names the hub for GitHub and new readers.
8. `verify_curriculum.py` also checks that every block note is in its stage folder, that its file name starts with its number, and that `subject` is set.

## Status
**Accepted**: 2026-10-09. **Superseded** by DR-010 and DR-011.

## Consequences
**Easier:** open one note to see where you are, what's next and how the system works. A folder listing is the study order. Subject views are a Dataview query (`WHERE subject = "Computer Engineering"`) instead of a folder.

**Harder / costs:** every block file was renamed, so links in anything outside the vault (bookmarks, external notes, Obsidian's open tabs in `workspace.json`) point to old paths. Any new block note must follow the file-name and folder rule, or verify fails. Planned hours are unchanged at **5,125 h**.

**Undo:** `git checkout -- . && git clean -fd` before committing, or revert the restructure commit after.
