# 00 - Dashboard

> - **Daily Study Log:** [[log.md]]
> - **Living Study Manifesto:** [[how-i-study.md]]
> - **Telemetry Log:** [[Telemetry Log.md]]

---

## 🚦 Automation Telemetry
*Aggregated automatically from your iPhone Shortcuts & Amazon Smart Plug*

```dataview
TABLE 
  filter(rows, (r) => r.Event = "Wake Up")[0].Time AS "Wake Up Time",
  filter(rows, (r) => r.Event = "Left Work")[0].Time AS "Left Work At",
  filter(rows, (r) => r.Event = "Arrived Home")[0].Time AS "Arrived Home At"
FROM "Telemetry Log"
WHERE type = "telemetry"
FLATTEN file.lists AS item
WHERE contains(item.text, "TELEMETRY:")
GROUP BY regexreplace(item.text, ".*TELEMETRY: ([0-9]{4}-[0-9]{2}-[0-9]{2}).*", "$1") AS Date
SORT Date DESC
LIMIT 7
```

---

## 🎯 Phase -1: Bedrock Foundations
*Rebuilding the operating system of the mind.*

- **Habit 1 — Arithmetic First Principles:** `[[Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics|Bedrock Math]]`
- **Habit 2 — Structural Grammar:** `[[Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar|Bedrock English]]`
- **Habit 3 — Cognitive Tooling:** `[[Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit|Deep Learner's Toolkit]]`

### Daily Routines
- **Feynman Technique:** Jargon-free child-level explanation (`[[08 - Templates/Feynman Technique Note Template|Feynman Template]]`)
- **Benjamin Franklin Copywork:** Reverse-engineering master prose (`[[08 - Templates/Franklin Copywork Template|Franklin Template]]`)
- **Spaced Blank-Sheet Retrieval:** 15-minute zero-hint recall dumps (`[[08 - Templates/Blank-Sheet Retrieval Template|Blank-Sheet Template]]`)

---

## 📈 The Vault
- 📑 **Curriculum**: 01 - Curriculum/
- 📄 **Paper Summaries**: [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] (Three-pass method)
- ✍️ **Writing Repository**: [[04 - Writing/Writing Hub|Writing Hub]] (Daily 500 words, Franklin copywork & technical essays)
- 🛠️ **Project Specs & Lab Builds**: [[05 - Projects/Projects Hub|Projects Hub]]
- 🌍 **Breadth & Languages**: [[06 - Breadth/Breadth and Humanities Hub|Breadth Hub]]
