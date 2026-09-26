# Original User Request

## 2026-09-25T08:50:01Z

# Teamwork Project Prompt

> Status: Launched.
> Goal: Craft prompt → get user approval → delegate to teamwork_preview
> Requested team: Full multi-agent research team

Use a very large team of agents. Expand and rigorously audit the existing EECS curriculum in the Obsidian vault. The goal is to create a gap-free curriculum that significantly exceeds the rigor and breadth of a standard MIT undergraduate degree, incorporating both deep theoretical foundations (vertical) and cutting-edge paradigms (horizontal). Let the team independently determine the best baseline for achieving the most verbose, elite education possible.

Working directory: /home/noblixy/The Noblett Repository
Integrity mode: development

## Requirements

### R1. Baseline Gap Analysis
Audit the existing curriculum against top-tier global standards (e.g., MIT OCW, ACM/IEEE guidelines). Identify and explicitly list any missing foundational concepts in a gap analysis report.

### R2. Vertical Expansion (Graduate-Level Depth)
Inject graduate-level rigor into the core tracks. This includes adding advanced mathematical prerequisites, foundational PhD-level papers, and rigorous textbook proofs to existing syllabi.

### R3. Horizontal Expansion (Modern Paradigms)
Design and integrate new specialization tracks covering cutting-edge engineering disciplines not typically found in standard undergraduate programs (e.g., TinyML/Edge AI, Rust for Systems Engineering, Hardware-in-the-Loop Virtualization).

## Acceptance Criteria

### Curriculum Completeness
- [ ] An independent agent-as-judge verifies that the proposed curriculum contains 100% of the core knowledge areas required by standard elite CS/CE programs, plus additional advanced topics.

### Depth & Breadth
- [ ] Every specialization track includes at least 3 graduate-level theoretical papers or advanced textbooks.
- [ ] At least 2 new cutting-edge technology tracks are fully integrated with defined lab/project requirements.

## 2026-09-25T10:09:14Z

Perform a comprehensive quality pass on the Obsidian vault at `/home/noblixy/The Noblett Repository`. The vault recently underwent a massive curriculum expansion (11 specialization tracks, 39 proofs, 35 PhD papers, bridge syllabi). Many files were authored by automated agents and may have inconsistent formatting, broken wikilinks, orphaned notes, redundant content, or rough prose. Sweep the entire vault and bring every file up to a professional, cohesive standard.

Working directory: /home/noblixy/The Noblett Repository
Integrity mode: development

## Requirements

### R1. Wikilink & Graph Integrity
Verify that every `[[wikilink]]` in the vault resolves to an existing file. Fix or remove all dead links. Ensure no notes are orphaned (unreachable from the Dashboard or any Hub/Index).

### R2. Formatting Consistency & Readability
Ensure all markdown files follow a consistent style: uniform header hierarchy, consistent list formatting, proper YAML frontmatter where appropriate, clean table alignment, and no raw HTML or broken rendering artifacts.

### R3. Content Deduplication & Coherence
Identify and merge any duplicated content across notes. Ensure cross-references between related notes are bidirectional where appropriate. Remove any leftover agent artifacts, placeholder text, or TODO stubs that should have been filled in.

## Acceptance Criteria

### Link Integrity
- [ ] A programmatic scan of every `.md` file confirms 0 dead wikilinks across the entire vault.
- [ ] A programmatic scan confirms 0 orphaned notes (every `.md` file has at least 1 incoming link from another `.md` file, excluding templates).

### Formatting
- [ ] An independent agent-as-judge reviews a random sample of at least 10 files across different directories and confirms consistent header hierarchy, list formatting, and table alignment with no rendering artifacts.

### Content Quality
- [ ] An independent agent-as-judge confirms 0 placeholder/TODO stubs remain in any curriculum or hub file.
- [ ] No two files contain substantively duplicated content covering the same topic.

