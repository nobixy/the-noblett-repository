---
title: "Dashboard"
type: hub
tags:
  - hub
  - navigation
---

# 00 - Dashboard

## 🧭 North Star
**Goal:** Earn, by self-study, the working knowledge of an MIT Course 6-3 SB + MEng — proven by passing the real final exams, shipping the builds, and writing the thesis — starting from rebuilt arithmetic and grammar.

**Budget:** ~6,300 planned hours (sum of block estimates) + Phase −1/0. At ~20 hrs/wk that is roughly **7 years**. Below 15 hrs/wk, cut scope; do not stretch past 8 years.

**The five rules** (from [[07 - Reference/The Independent EECS Program.pdf|the source program]]):
1. No lecture without its problem set the same week.
2. A block is done when its *Done when* line is true. Not before.
3. Never start a new block until the current one is done.
4. Math and writing are daily habits and are never paused.
5. Keep a daily log, in git.

**Guardrails for this vault:**
- The *Study Notes, Psets & Proofs* section of every block is written by me, from a blank page. Reference derivations live in [[Worked Proofs Index|Worked Proofs]] and are opened only after my own attempt.
- Specializations: pick **two** of the 11 tracks, not more. Decide at the end of Year 3 ([[Specializations Hub]]).
- The vault serves the study, not the other way round. No new structure until the current block needs it.

**Now:** Phase −1 → [[BM - Bedrock Mathematics|Bedrock Math]] + [[BW - Bedrock English and Grammar|Bedrock English]] · **Next block:** [[B0 - The Deep Learner's Toolkit|B0]] → [[P1 - Learning How to Learn|P1]] · **Schedule:** [[Calendar]]

---

> - **Daily Study Log:** [[log.md]]
> - **Living Study Manifesto:** [[how-i-study.md]]
> - **Telemetry Log:** [[Telemetry Log.md]]
> - **Degree Progress Checklist:** [[Checklist]]
> - **Book Acquisition Tracker:** [[Your Shelf]]

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

- **Habit 1 — Arithmetic First Principles:** [[BM - Bedrock Mathematics|Bedrock Math]]
- **Habit 2 — Structural Grammar:** [[BW - Bedrock English and Grammar|Bedrock English]]
- **Habit 3 — Cognitive Tooling:** [[B0 - The Deep Learner's Toolkit|Deep Learner's Toolkit]]

### Daily Routines
- **Feynman Technique:** Jargon-free child-level explanation ([[08 - Templates/Feynman Technique Note Template|Feynman Template]])
- **Benjamin Franklin Copywork:** Reverse-engineering master prose ([[08 - Templates/Franklin Copywork Template|Franklin Template]])
- **Spaced Blank-Sheet Retrieval:** 15-minute zero-hint recall dumps ([[08 - Templates/Blank-Sheet Retrieval Template|Blank-Sheet Template]])

---

## 📈 The Vault
- 🧠 **Mindset & Habits**: [[09 - Mindset & Habits/Mindset Hub|Mindset Hub]]
- 📑 **Curriculum**: [[Checklist|Degree Checklist]] · [[01 - Curriculum/Specializations/Specializations Hub|Specializations Hub]]
- 📓 **Topic Notes**: [[02 - Notes/Hardware/Hardware Index|Hardware]] · [[02 - Notes/Languages/Languages Index|Languages]] · [[02 - Notes/Math/Math Index|Math]] · [[02 - Notes/Systems/Systems Index|Systems]] · [[02 - Notes/Theory/Theory Index|Theory]]
- 📄 **Paper Summaries**: [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] (Three-pass method)
- ✍️ **Writing Repository**: [[04 - Writing/Writing Hub|Writing Hub]] (Daily 500 words, Franklin copywork & technical essays)
- 🛠️ **Project Specs & Lab Builds**: [[05 - Projects/Projects Hub|Projects Hub]]
- 🌍 **Breadth & Languages**: [[06 - Breadth/Breadth and Humanities Hub|Breadth Hub]]
- 📚 **Reference & Appendices**: [[07 - Reference/Appendix E - Failure Modes|Appendix E (Failure Modes)]] · [[07 - Reference/Appendix F - Curated URLs|Appendix F (Curated URLs)]] · [[07 - Reference/Baseline Gap Analysis and Audit Report|Curriculum Audit & Gap Report]] · [[Worked Proofs Index|Worked Proofs]]
