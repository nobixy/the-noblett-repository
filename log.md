# Master Daily Study Log
*Habit 4: What you did, what you got stuck on, what you'll do tomorrow. Two minutes. Fifteen years from now this is the most valuable file you own.*

> [!TIP] How to log
> Click the **Open today's daily note** calendar icon in the left ribbon (or run *Daily notes: Open today's daily note*). It creates `03 - Journal/YYYY-MM-DD.md` from the [[Daily Log Entry Template|Daily Log Template]]. End-of-week synthesis uses the [[Weekly Review Template|Weekly Review Template]].

---

## Totals

```dataview
TABLE WITHOUT ID length(rows) AS "Days logged", sum(rows.study_hours) AS "Study hours", length(filter(rows.anki, (a) => a)) AS "Anki days", length(filter(rows.words_500, (w) => w)) AS "500-word days"
FROM "03 - Journal"
WHERE type = "daily-log"
GROUP BY true
```

## Entries

```dataview
TABLE WITHOUT ID file.link AS Day, block AS Block, study_hours AS Hours
FROM "03 - Journal"
WHERE type = "daily-log"
SORT file.name DESC
```

First entry: [[2026-09-25]]
