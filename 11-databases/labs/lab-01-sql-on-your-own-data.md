---
title: "Lab 01 — SQL on Your Own Data"
id: "MOD11-LAB01"
type: "lab"
module: "11-databases"
phase: "D"
order: 1320
prerequisites: []
---

# Lab 01 — SQL on Your Own Data

**Goal:** learn SQL by asking real questions about your own learning: your Study Deck review log, your journal, your copywork and spelling logs. Design a schema, load the data, query it with joins and aggregates, and watch indexes change query plans.

**Sessions:** four. Tool: **SQLite** (`sqlite3` command, and Python's built-in `sqlite3` module).

---

## Session 1 — Schema design

A **relational database** stores data in **tables** (relations — Module 03 Unit 4: a relation is a set of tuples). Each table has columns with types and a **primary key** that identifies each row. Tables refer to each other with **foreign keys**.

Design a schema for your learning data. A starting point:

```sql
CREATE TABLE card (
    id        TEXT PRIMARY KEY,      -- Study Deck @id
    deck_file TEXT NOT NULL,
    kind      TEXT NOT NULL CHECK (kind IN ('qa', 'cloze', 'spelling'))
);
CREATE TABLE tag (
    card_id TEXT NOT NULL REFERENCES card(id),
    tag     TEXT NOT NULL,
    PRIMARY KEY (card_id, tag)
);
CREATE TABLE review (
    id       INTEGER PRIMARY KEY,
    card_id  TEXT NOT NULL REFERENCES card(id),
    reviewed TEXT NOT NULL,          -- ISO timestamp
    grade    TEXT NOT NULL CHECK (grade IN ('again', 'hard', 'good', 'easy'))
);
CREATE TABLE journal_entry (
    day         TEXT PRIMARY KEY,    -- the entry's file name (YYYY-MM-DD, set by the daily-notes plugin)
    sessions    INTEGER,
    flashcards  INTEGER,             -- 0/1
    copywork    INTEGER              -- 0/1
);
CREATE TABLE copywork (
    id INTEGER PRIMARY KEY, day TEXT, passage TEXT, level INTEGER,
    words INTEGER, spelling_errors INTEGER, word_changes INTEGER, punct_diffs INTEGER
);
```

**[W]:** why is `tag` its own table instead of a comma-separated `tags` column in `card`? (Look up **first normal form**; then think about the query "all cards tagged m04".) Why does `review` reference `card` instead of copying the question text into every review row? (Look up **normalisation** and **update anomalies**.)

Write a Python loader that reads your real files (Study Deck cards and `reviews.tsv`, journal frontmatter from `03 - Journal/*.md`, Copydiff's `copywork-log.tsv`) and inserts them inside **one transaction** (`BEGIN … COMMIT`; time it with and without the transaction — why the huge difference? Lab 02 explains).

---

## Session 2 — Queries

Write each query, predict roughly what the answer should be, run it, and save it in `queries.sql` [R]:

1. How many reviews per day for the last 30 days?
2. Retention (fraction not `again`) per tag, for tags with at least 20 reviews, sorted worst first. (Join `review` → `card` → `tag`, `GROUP BY tag`, `HAVING`.)
3. The 10 cards you've failed most often, with their deck files.
4. Journal entries that cover 2 or more sessions but have no copywork. (Entries written before DR-011 use older fields; skip or map them, and say which.)
5. Copywork spelling errors per 100 words, per block of 10 passages in order, as a trend.
6. For each card, its first and latest review dates and the number of reviews.
7. Cards that have **never** been reviewed (a `LEFT JOIN` with `IS NULL`, or `NOT EXISTS`).
8. Your longest run of consecutive journal entries with flashcards done (harder: window functions, or a clever self-join — or do it in Python and explain why SQL made it awkward).

**[F]:** explain to yourself, out loud, what `GROUP BY` does to rows before `HAVING` filters them, using query 2.

---

## Session 3 — Indexes and plans

1. Make the data big: generate 1,000,000 synthetic reviews (random cards and dates) in a copy of the database.
2. Run `EXPLAIN QUERY PLAN` on queries 1, 2, and 3. Read the plans: `SCAN review` (read every row) vs `SEARCH review USING INDEX`.
3. Time each query. Then create indexes: `CREATE INDEX review_card ON review(card_id);`, `CREATE INDEX review_time ON review(reviewed);`. Re-check plans and times.
4. **[W]:** indexes speed reads. What do they cost? Measure the time to insert 100,000 rows with zero, one, and two indexes. When would you **not** add an index?
5. Find a query where SQLite does **not** use your index even though one exists (e.g. a function applied to the column: `WHERE substr(reviewed, 1, 7) = '2026-11'`). Rewrite the query so it can use the index.

---

## Session 4 — Relational algebra, briefly

Every SQL query is a combination of a few operations on relations: **selection** σ (filter rows), **projection** π (choose columns), **join** ⋈, **union**, **difference**, **grouping/aggregation**. Rewrite queries 2, 3, and 7 as relational-algebra expressions (trees of operators). Then draw them as **operator trees** — this is exactly the plan tree your Stratum executor will run (iterator model: each operator asks its child for the next row).

**[W]:** the same query can be computed by many equivalent trees (filter before or after the join?). Which is cheaper, and why? This choice is the job of a **query planner**.

---

## Done when

- [ ] Schema with keys and constraints; loader with one transaction; your real data loaded.
- [ ] Eight queries written and saved with results.
- [ ] Index experiments: plans, read timings, insert costs, and the un-indexable query fixed.
- [ ] Three operator trees drawn.

## Retrieval and reflection

1. **[R]:** primary and foreign keys; normalisation in one sentence; JOIN kinds; GROUP BY vs HAVING; what an index costs and buys.
2. **[F] (spoken):** "How does a database answer 'reviews for this card' without reading every review?"
3. Add the eight queries' results to your Section Review: what did your own data teach you about your studying?
