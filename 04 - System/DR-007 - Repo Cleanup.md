---
title: "DR-007: Repo Cleanup"
type: decision-record
status: superseded
superseded_by: [DR-010, DR-011]
date: 2026-10-10
accepted: 2026-10-10
tags:
  - adr
  - decision-record
---

# DR-007: Repo Cleanup

> [!WARNING] Superseded
> Superseded by [[DR-010 - Project-First Original Curriculum|DR-010]] and [[DR-011 - Sectioned Curriculum and Frontmatter Schema|DR-011]]. Kept as a historical record: its dates, hours, weeks, phases and links into `99 - Archive/` describe the v1 plan and are not current instructions.

*Uses the [[Decision Record]] template. Follows [[DR-006 - Digital Twin, EW Resilience and Fun Prerequisites|DR-006]]. Accepted and applied 2026-10-10. Checkpoint before this change: git commit `67bd081`.*

## Context
"Go ahead and refactor the whole repo, I see a bunch of unnecessary stuff." The vault had 11 top-level folders, five of them holding one note each, six decision records loose in the root, and a large archive of AI-generated material (39 unverified answer keys, a 47 KB gap report, 17 one-off scripts, two redirect stubs) that nothing on The Path used.

## Decision
**Removed (61 files, all recoverable from `67bd081`; the full list was in the Removed 2026-10-10 Manifest, since removed; see git history):**
- `99 - Archive/Worked Proofs/` (39 notes): AI-generated answer keys, never verified. Each block's *Check your work* callout already points at the course's own solutions.
- `99 - Archive/Scripts/` (17 scripts + README): one-off migration scripts marked "do not re-run"; `verify_curriculum.py` replaced the checkers.
- `99 - Archive/Redirects/` (2 stubs) and the 2026-09-25 *Baseline Gap Analysis* report.
- Two plugin installer zips under `.obsidian/plugins/` (Advanced URI, Templater). The plugins themselves are untouched.

**Merged:** the Mindset Hub into [[how-i-study]] §7A, word for word. It repeated what how-i-study already said.

**New layout (11 → 8 top-level folders):**
- `02 - Notes/`: the five topic indexes (no more one-note subfolders) + Paper Reading, Writing and Breadth hubs.
- `03 - Projects/`: Projects Hub.
- `04 - Reference/`: source PDF, Appendices E and F, Your Shelf.
- `05 - Decisions/`: DR-001 … DR-007.
- `06 - Templates/`, `07 - Daily Log/` (renumbered; Obsidian's daily-notes and templates settings updated).
- `99 - Archive/`: cut blocks + `Removed 2026-10-10/` (the manifest).
- Root: Start Here, README, how-i-study, log, Calendar, Telemetry Log, verify script.

**Kept on purpose:**
- Calendar and Telemetry Log stay in the root: the iPhone Shortcut automation writes to them by path.
- `99 - Archive/Cut Content/` (7 notes): live notes still link to them as sources (Rust, digital twins, formal verification).
- All 11 templates are linked from somewhere.
- The disabled Google Sync plugin: its settings file holds a credential and was not opened.

Note names did not change, so every wikilink still resolves. Links to the deleted Checklist and Dashboard stubs now point at Start Here.

## Consequences
**Hours:** unchanged, **6,005 h** core. `verify_curriculum.py` passes. No curriculum content changed.

**Flags:**
- Restart Obsidian after this change, so the new daily-notes and templates folders load.
- Older DRs mention old paths (`10 - Daily Log`, `99 - Archive/Scripts/`) as history; they are left as written.

**Undo:**
- If not yet committed: `git checkout -- . && git clean -fd` (back to `67bd081`).
- If Obsidian Git already committed it: `git revert <that commit>`.

> [!WARNING] Do not run this Undo line now
> It was written for the moment right after this change, before it was committed. Today `git checkout -- . && git clean -fd` would throw away **all** uncommitted edits and delete every untracked file in the vault (new notes, today's log). To undo this decision now, use `git revert <commit>` or restore single files with `git checkout <commit> -- "<path>"`.
