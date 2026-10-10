---
title: "DR-010: KISS Vault Restructure"
type: decision-record
status: accepted
date: 2026-10-10
accepted: 2026-10-10
tags:
  - adr
  - decision-record
---

# DR-010: KISS Vault Restructure

*Uses the [[Decision Record]] template. Follows [[DR-009 - Learning Method Deep Dives|DR-009]]. Accepted and applied 2026-10-10.*

## Context
"I just want it to make more sense. right now it seems very messy still. Remember KISS."
Despite the cleanup in DR-007, the vault still had 8 top-level folders and a fragmented `01 - Curriculum` directory containing 10 sub-folders. This created a lot of folder bloat and cognitive friction, hiding notes away in deep, nested structures.

## Decision
Flatten and simplify the entire vault architecture to a bare minimum **KISS** (Keep It Simple, Stupid) structure:
1. **Flatten Curriculum**: Dropped the 10 subfolders in `01 - Curriculum/`. All 62 blocks are now flatly listed. Added a `stage:` property to the frontmatter of all blocks to keep the Dataview queries (like Degree Progress) functional without needing folders.
2. **Four Top-Level Folders**:
   - `01 - Curriculum`: The learning path blocks.
   - `02 - Atlas`: Merged `Notes`, `Projects`, `Reference`, and the `Supporting Systems/Learning Methods` out of curriculum into one unified knowledge base.
   - `03 - Journal`: Renamed `Daily Log`.
   - `04 - System`: Merged `Decisions` and `Templates` into a single admin folder.
3. Updated `verify_curriculum.py`, `00 - Start Here.md`, and Obsidian settings (`daily-notes.json`, `templates.json`) to accommodate these changes natively.

## Consequences
**Easier:** Much cleaner file explorer (4 folders instead of 8 top-level and 10 nested).
**Hours:** unchanged, **6,005 h** core.

**Undo:**
Use `git checkout` or `git revert` to the commit prior to this change.
