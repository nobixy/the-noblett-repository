---
title: "Dashboard"
type: hub
tags:
  - hub
  - navigation
---

# 00 - Dashboard

> **[👉 START HERE: The Master Curriculum Map]([[00 - Start Here]])**


## 🧭 North Star
**Goal:** Complete the equivalent of a rigorous MIT Course 6-3 SB + MEng, and then continue executing an infinite, lifelong learning sequence bridging post-doc level depth across quantum computing, computational biology, formal verification, and pure mathematics. This is a magnum opus of self-education.

**Budget:** This is a lifelong endeavor. There is no longer an 8-year completion constraint. The curriculum spans 17 sequential phases (from Arithmetic to advanced Computational Biology and Quantum Information). The only metric that matters is continuous, disciplined forward progress.

**The five rules** (from [[The Independent EECS Program.pdf|the source program]]):
1. No lecture without its problem set the same week.
2. A block is done when its *Done when* line is true. Not before.
3. Never start a new block until the current one is done.
4. Math and writing are daily habits and are never paused.
5. Keep a daily log, in git.

**Guardrails for this vault:**
- The *Study Notes, Psets & Proofs* section of every block is written by me, from a blank page. Each block's **Check your work** callout names the course's own solutions, autograder, or test suite; I open it only after my own attempt.
- The vault serves the study, not the other way round. No new structure until the current block needs it.

**Now:** Phase −1 → [[Bedrock Mathematics|Bedrock Math]] + [[Bedrock English and Grammar|Bedrock English]] · **Next block:** [[The Deep Learner's Toolkit|B0]] → [[Learning How to Learn|P1]] · **Schedule:** [[Calendar]]

---

> - **Daily Study Log:** [[log.md]] (entries in `10 - Daily Log/`)
> - **Living Study Manifesto:** [[how-i-study.md]]
> - **Telemetry Log:** [[Telemetry Log.md]]
> - **Degree Progress Checklist:** [[Checklist]]
> - **Book Acquisition Tracker:** [[Your Shelf]]

---

## 📊 Degree Progress
*Driven by each block's `status` and `hours_actual` frontmatter: update those, and this updates itself. Blocks flagged `optional: true` (the 04a/08a/15a bridges) are left out.*

```dataview
TABLE WITHOUT ID status AS Status, length(rows) AS Blocks, sum(rows.hours_actual) AS "Hours logged", sum(rows.hours_estimate) AS "Hours planned"
FROM "01 - Curriculum"
WHERE block_id AND optional != true
GROUP BY status
```

```dataview
TABLE WITHOUT ID file.link AS "In progress", term AS Term, hours_actual + " / " + hours_estimate AS Hours, date_started AS Started
FROM "01 - Curriculum"
WHERE block_id AND status = "in-progress"
```

---

## 🚦 Automation Telemetry
*Aggregated automatically from your iPhone Shortcuts & Amazon Smart Plug*

```dataview
TABLE 
  filter(rows, (r) => contains(r.Event, "Wake Up"))[0].Time AS "Wake Up Time",
  filter(rows, (r) => contains(r.Event, "Left Work"))[0].Time AS "Left Work At",
  filter(rows, (r) => contains(r.Event, "Arrived Home"))[0].Time AS "Arrived Home At"
FROM "Telemetry Log"
FLATTEN file.lists AS item
WHERE contains(item.text, "TELEMETRY:")
FLATTEN trim(split(item.text, "\|")[1]) AS Time
FLATTEN trim(split(item.text, "\|")[2]) AS Event
GROUP BY trim(replace(split(item.text, "\|")[0], "TELEMETRY:", "")) AS Date
SORT Date DESC
LIMIT 7
```

---

## 🎯 Phase -1: Bedrock Foundations
*Rebuilding the operating system of the mind.*

- **Habit 1 — Arithmetic First Principles:** [[Bedrock Mathematics|Bedrock Math]]
- **Habit 2 — Structural Grammar:** [[Bedrock English and Grammar|Bedrock English]]
- **Habit 3 — Cognitive Tooling:** [[The Deep Learner's Toolkit|Deep Learner's Toolkit]]

### Daily Routines
- **Feynman Technique:** Jargon-free child-level explanation ([[Feynman Technique Note Template|Feynman Template]])
- **Benjamin Franklin Copywork:** Reverse-engineering master prose ([[Franklin Copywork Template|Franklin Template]])
- **Spaced Blank-Sheet Retrieval:** 15-minute zero-hint recall dumps ([[Blank-Sheet Retrieval Template|Blank-Sheet Template]])

---

## 📈 The Vault
- 🧠 **Mindset & Habits**: [[Mindset Hub|Mindset Hub]]
- 📑 **Curriculum**: [[Checklist|Degree Checklist]] · [[Specializations Hub|Specializations Hub]]
- 📓 **Topic Notes**: [[Hardware Index|Hardware]] · [[Languages Index|Languages]] · [[Math Index|Math]] · [[Systems Index|Systems]] · [[Theory Index|Theory]]
- 📄 **Paper Summaries**: [[Paper Reading Hub|Paper Reading Hub]] (Three-pass method)
- ✍️ **Writing Repository**: [[Writing Hub|Writing Hub]] (Daily 500 words, Franklin copywork & technical essays)
- 🛠️ **Project Specs & Lab Builds**: [[Projects Hub|Projects Hub]]
- 🌍 **Breadth & Languages**: [[Breadth and Humanities Hub|Breadth Hub]]
- 📚 **Reference & Appendices**: [[Appendix E - Failure Modes|Appendix E (Failure Modes)]] · [[Appendix F - Curated URLs|Appendix F (Curated URLs)]] · Archived AI material (unverified answer keys, 2026-09-25 gap report): `99 - Archive/`
