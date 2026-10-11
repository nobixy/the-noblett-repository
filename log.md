---
title: "Session Log"
type: hub
tags: [hub, log]
---

# Session Log
*At the end of every session: what you worked on, what you did, where you got stuck, what comes next. A few lines. This file is the evidence that the work happened.*

> [!TIP] How to log
> Click the **Open today's daily note** calendar icon in the left ribbon (or run *Daily notes: Open today's daily note*). Obsidian's daily-notes plugin names the file by date (`03 - Journal/YYYY-MM-DD.md`) and fills it from the [[Daily Log Entry Template|session log template]]. Several sessions on one date go in the same file (bump `sessions`). Each section closes with the [[Section Review Template|Section Review]].

---

## Totals

```dataview
TABLE WITHOUT ID length(rows) AS "Entries", sum(rows.sessions) AS "Sessions", length(filter(rows.flashcards, (a) => a)) AS "Flashcard entries", length(filter(rows.copywork, (c) => c)) AS "Copywork entries"
FROM "03 - Journal"
WHERE type = "daily-log"
GROUP BY true
```

## Entries

```dataview
TABLE WITHOUT ID file.link AS Entry, worked_on AS "Worked on", sessions AS Sessions
FROM "03 - Journal"
WHERE type = "daily-log"
SORT file.name DESC
```

*Entries written before [DR-011](<04 - System/DR-011 - Sectioned Curriculum and Frontmatter Schema.md>) use the older fields (`block`, `study_hours`, `words_500`) and show blanks above. They are kept unchanged as historical records:* [[2026-09-25]] · [[2026-09-26]] · [[2026-09-29]] · [[2026-10-06]]
