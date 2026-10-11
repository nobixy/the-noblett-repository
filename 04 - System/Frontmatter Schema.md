---
title: "Frontmatter Schema"
type: reference
tags: [system, schema]
---

# Frontmatter Schema

*The one place that defines the YAML frontmatter of curriculum notes. Decided in [DR-011](<DR-011 - Sectioned Curriculum and Frontmatter Schema.md>). Every module overview, stage, lab, project spec and resources file uses it. Notes outside the curriculum folders (Atlas, templates, decision records, journal) have their own small field sets, listed at the end.*

## Curriculum notes

Fields appear in this order. Required fields are marked ✔.

| Field | Req. | Type | Meaning |
| :-- | :-- | :-- | :-- |
| `title` | ✔ | string | Display title (same as the `#` heading). |
| `id` | ✔ | string | Stable identifier, unique across the vault (patterns below). Journal entries, dashboards and `prerequisites` refer to items by `id`. |
| `type` | ✔ | enum | `overview` · `lesson` · `lab` · `project` · `reference` |
| `module` | ✔ | string | The top-level folder the note lives in, e.g. `00-foundations`, `05-data-structures-and-algorithms`. |
| `track` | foundations only | enum | `english` · `math` |
| `stage` | stages only | string | The stage code, `E01`–`E10` or `M01`–`M11` (same as `id`). |
| `phase` | ✔ | enum | `A` · `B` · `C` · `D` · `E` — the five phases of the curriculum. Phases are groupings, not durations. |
| `order` | ✔ | integer | Position in the one recommended sequence, in steps of 10 (10, 20, 30…) so a new item can be slotted in without renumbering. The checklist in [Start Here](<../00 - Start Here.md>) follows `order`. |
| `prerequisites` | ✔ | list of ids | What must be done before this item starts (semantics below). `[]` if none. |
| `checkpoints` | overviews | list of ids | The checkpoint ids that close this module or track (unit tests, track assessments, module close). |

**Optional fields** (only where they apply):

| Field | Used on | Meaning |
| :-- | :-- | :-- |
| `kind` | labs | `maker` for hands-on hardware labs (Module 04). Replaces the old `type: maker-lab`. |
| `sessions` | labs | Number of sessions the lab is written as (a count, not a duration). |
| `unit` / `units` | Module 12 lab / projects | The Module 12 unit(s) the item belongs to or needs. |
| `stages` | foundation projects | Human-readable note of the stages the project runs alongside. |
| `artifact` | projects | What you build. |
| `deliverable` | projects | The written or spoken deliverable. |
| `tags` | any | Obsidian tags. |

**Removed:** `hours`, `weeks` and every other time estimate (see DR-011 — the curriculum has no durations). Also the v1 fields `block_id`, `associated_block`, `tier`, `term`, `job_ready`, `hours_estimate`, `hours_actual`, `date_started`, `date_completed`; these survive only in `99 - Archive/`.

## ID patterns

| Pattern | Example | What it is |
| :-- | :-- | :-- |
| `FND`, `FND-EN`, `FND-MA` | `FND-EN` | Foundations overview; English and Math track overviews |
| `FND-EN-PLACEMENT` | | English placement diagnostic |
| `E01`–`E10`, `M01`–`M11` | `E05` | Foundation stages (`type: lesson`) |
| `FND-EN-PRJ-<slug>`, `FND-MA-PRJ-<slug>` | `FND-EN-PRJ-spelling-engine` | Foundation projects |
| `FND-FIRST-SECTIONS`, `FND-EN-PROMPTS`, `FND-MA-PUZZLES` | | Foundation reference pages |
| `FND-EN-RES`, `FND-MA-RES` | `FND-MA-RES` | Foundation track resources (`type: reference`), with the track's **Video course** section ([DR-012](<DR-012 - Video Course Picks.md>)) |
| `MODnn` | `MOD06` | Module overview |
| `MODnn-LABnn` | `MOD01-LAB00` | Lab |
| `MODnn-PRJ-<slug>` | `MOD02-PRJ-study-deck` | Project (slug = the project folder name) |
| `MODnn-RES` | `MOD09-RES` | Module resources (`type: reference`); each has the full **Video course** section with the lecture-to-vault map, and the module overview names the picks ([DR-012](<DR-012 - Video Course Picks.md>)) |

**Checkpoint ids** (listed in an overview's `checkpoints`; they have no note of their own — they are sections of the overview):

| Pattern | Example | What it is |
| :-- | :-- | :-- |
| `FND-EN-ASSESS`, `FND-MA-ASSESS` | | Track assessments (after E10 and M11) |
| `MOD03-U1` … `MOD03-U8` | `MOD03-U5` | Module 03 unit checks |
| `MOD12-C1`–`C3`, `L1`–`L4`, `P1`–`P3`, `S1` | `MOD12-L2` | Module 12 units (calculus, linear algebra, probability, signals) |
| `MODnn-CLOSE` | `MOD07-CLOSE` | Module close (cumulative retrieval, showcase, reflection) |

## Prerequisite semantics

- An id in `prerequisites` means **that item is done** by its own "Done when" list:
  - a stage id (`E07`) — the stage's self-check is passed (or placed out);
  - a lab or project id — its "Done when" list is true;
  - a checkpoint id (`MOD03-U1`, `FND-MA-ASSESS`) — that check is passed;
  - a **module overview id** (`MOD02`) — the **whole module** is done, i.e. its `MODnn-CLOSE` checkpoint.
- **Effective prerequisites** of a lab, project or resources file = its own list **plus** its module overview's list. Overview prerequisites are not repeated in every lab.
- Labs inside a module chain in order (each lab lists the previous one) unless the lab says otherwise.
- `prerequisites` says what must be *finished*. It does not override [Start Here](<../00 - Start Here.md#operating-rules>) rule 2 (one build project at a time).

## Other note families

| Family | `type` | Fields |
| :-- | :-- | :-- |
| Session log entry (`03 - Journal/`) | `daily-log` | `worked_on` (list of ids), `sessions` (count), `flashcards` (bool), `copywork` (bool). The file name is the date — record metadata, kept. |
| Section Review | `section-review` | `section`, `sessions`, `english_stage`, `math_stage`, `build`, `flashcard_sessions`, `copywork_sessions` |
| Build log ([Project Build Spec Template](<Project Build Spec Template.md>)) | `build-log` | `project` (id), `spec`, `repo_link`, `status`, `tests_pass` |
| Milestone Checkpoint / Demo Script / Lab Report / Design Doc templates | `milestone-checkpoint` · `demo-script` · `lab-report` · `design-doc` | `project` or `lab`, plus a `date` stamp (record metadata) |
| Decision records | `decision-record` | `title`, `status` (`accepted` · `superseded`), `superseded_by`, `amended_by`, `date`, `accepted` |
| Atlas, hubs and root notes | `hub` · `index` · `reference` · `learning-method` · … | `title`, `type`, `tags` (+ `evidence`, `method_id` on learning-method notes) |

> [!NOTE] Older journal entries
> Entries written under the v1 plan (2026-09-25 to 2026-10-06) use the v1 fields `block`, `study_hours`, `anki`, `words_500`. They are historical records and were left as written; the [log](<../log.md>) dashboards read only the v2 fields, so those entries appear in the entry count but add nothing to the session, flashcard and copywork totals.
