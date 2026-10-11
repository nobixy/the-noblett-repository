---
title: "Project: Vault Search"
id: "MOD05-PRJ-vault-search"
type: "project"
module: "05-data-structures-and-algorithms"
phase: "C"
order: 810
prerequisites: [MOD05-LAB03]
artifact: "vs: a full-text search engine for your own notes — your own hash table, an on-disk inverted index with positions, Boolean and phrase queries, TF-IDF ranking, trie autocomplete with spelling correction, and an evaluation with relevance judgements"
deliverable: "Design doc + evaluation report (precision@5, timings) + short demo"
---

# Project: Vault Search

| | |
| :-- | :-- |
| **Module** | 05 Data Structures and Algorithms |
| **Prerequisites** | Labs 01–03; Module 03's [Counting Verifier](../../../03-discrete-math/projects/counting-verifier/spec.md) (birthday bound) helpful |
| **You build** | `vs`, a search engine for this vault and your workbench: thousands of Markdown notes, specs, and journal entries. You write the tokenizer, your own hash table (no `dict` for the index), an inverted index stored on disk, queries with AND/OR/NOT and exact phrases, relevance ranking, autocomplete with a trie, "did you mean…?" spelling suggestions, and an evaluation that measures how good your results are |
| **Deliverable** | Design doc, evaluation report, and demo |

---

## Why this matters

Every search box you've used — web, email, code, this vault's own search — is built on the same core structure: an **inverted index**, mapping each word to the list of documents that contain it. Building one makes you use almost every structure in this module at once: hashing to find words fast, sorted lists merged with two pointers for AND queries, positions for phrases, tries for prefixes, edit distance for typos, and a heap for the top results.

It's also a tool you'll actually use: by the end of this curriculum your notes will be large, and a search that knows your own vocabulary is genuinely useful.

**Real-world analogs:** Lucene/Elasticsearch, SQLite's FTS, `ripgrep` (for comparison: no index), Obsidian's search, spell suggestion in search engines.

---

## Milestones

### Milestone 1 — Design doc and the corpus

1. **Design doc v1** (3–5 pages, E10): goals with numbers (e.g. "index the vault in under 30 s; answer a 2-word query in under 50 ms; precision@5 ≥ 0.7 on my 20 test queries"); the data structures and their invariants; the on-disk format; alternatives (at least: hash table design; storing postings as lists vs bitmaps; whether to stem words).
2. **Corpus:** walk the vault and `~/workbench` for `.md` files (reuse `treesize.py`'s walker). Each document gets an integer id; store path, title (first heading or file name), and modification time.

### Milestone 2 — Tokens and your own hash table

**Tokenizer:** lowercase; split into words; strip punctuation; keep each word's **position** (its index in the document); skip a short list of **stop words** (the, of, and, a, to, …) — optional, decide [W]. **Stemming:** a few suffix rules so *running*, *runs*, and *run* match (you know these rules from E02–E03! drop *-ing*, *-ed*, *-s*, undo doubling…). Test it on 50 words; note where it fails.

**`HashMap`** — implement it yourself; you may not use `dict` or `set` inside the index (you may use them in tests, as witnesses):
- **Open addressing with linear probing:** an array of slots; hash the key (`hash(key)` is fine, or write FNV-1a for strings as a stretch), take `% capacity`, and if the slot is taken, try the next one, wrapping around.
- **Deletion** with tombstones (a marker meaning "something was here; keep probing past me"). [W] Why can't you just empty the slot?
- **Resize** (double, re-insert everything) when the load factor (items ÷ capacity) exceeds 0.7.
- Operations: `get`, `put`, `delete`, `__contains__`, `__len__`, iteration.

**Tests:** differential testing against `dict` with 100,000 random operations; invariants checked after each operation in a slower test mode.

**Experiment:** measure the **average probe length** for successful lookups at load factors 0.1, 0.3, 0.5, 0.7, 0.9, 0.95. The classic analysis predicts about ½(1 + 1/(1 − α)) for load factor α. Plot yours against it. Then implement **separate chaining** (each slot holds a small list) and compare. Which degrades more gracefully as the table fills?

**Done when:** `HashMap` passes differential tests; the probe-length plot is done.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why does probing get so much worse near a full table?* Feynman target: *how a hash table finds a key without searching*.

### Milestone 3 — The inverted index, on disk

1. **Postings:** for each term, a list of `(doc_id, [positions])`, **sorted by doc_id**.
2. **Build** the index for the whole corpus in memory (your `HashMap` from term to postings).
3. **Persist** it: design a file format (documented in the design doc). A simple, good choice: a **lexicon** file (term → offset and length in the postings file) and a **postings** file. JSON is acceptable for a first version; a compact binary format with `struct` (Tone Loom skills) is the stretch. Measure the size of each.
4. **Incremental update:** on re-run, only re-index documents whose modification time changed; handle deleted files.

**Done when:** indexing the full vault meets your time goal; reloading the index is fast; changing one note updates only that note.

### Milestone 4 — Queries

1. **Single term:** look up its postings.
2. **AND:** intersect two sorted postings lists with the **two-pointer merge** (Lab 02's merge, adapted): O(a + b). For many terms, intersect the **shortest lists first** [W].
3. **OR** (union by merge) and **NOT** (difference by merge).
4. **Phrase queries** `"loop invariant"`: documents containing both words where some position of the second word is exactly one after a position of the first.
5. **Query parser:** `invariant AND (loop OR recursion) NOT python`, quotes for phrases — your third recursive-descent parser (Worldfile, Truth Engine). Reuse the pattern.

**Tests:** on a small fixture corpus, every query's results checked against a brute-force scan of all documents.

### Milestone 5 — Ranking

Boolean results aren't ordered. Rank them:

- **TF-IDF:** a term is more important in a document the more often it appears there (**term frequency**), and less important overall the more documents contain it (**inverse document frequency**: log(N ÷ df), M11!). Score = sum over query terms of tf × idf. [W] Why the log in idf? (What would happen to a word that appears in every note?)
- Normalise by document length (longer notes shouldn't win just by being long) — choose a method and justify it.
- **Top-k with a heap:** keep the best 10 scores in a min-heap of size 10 (your Lab 02 `MinHeap`) — O(n log k) instead of sorting everything. [W] Why a *min*-heap for the *top* results?
- **Snippets:** show 1–2 lines from each result with the matched words highlighted (terminal colour).
- **Stretch:** BM25, a widely used refinement of TF-IDF.

### Milestone 6 — Autocomplete and "did you mean?"

1. **Trie** of every term in the index, each node storing the count of documents below it. `vs complete inv` lists the top 5 completions by frequency (`invariant`, `inverted`, `investigate`…).
2. **Spelling suggestions:** when a query term isn't in the index, find terms within edit distance 1 or 2 (Copydiff's Levenshtein). Brute force over all terms works; a smarter way walks the trie while computing one row of the edit-distance table per node, pruning branches whose best possible distance is already too big. Implement the brute-force version, then the trie walk, and compare speeds.
3. Show "Did you mean *invariant*?" — and record your own typos into your spelling log (it's your vault, after all).

### Milestone 7 — Evaluation

How good is your search? Measure it the way search engineers do.

1. **Write 20 test queries** you'd really type, and for each, list the notes that are actually relevant (your **judgements**, written *before* looking at results).
2. **Precision@5:** for each query, the fraction of the top 5 results that are relevant. Average over queries.
3. Compare three configurations: no stemming vs stemming; TF-IDF vs plain term counts; with vs without stop words.
4. **Timing:** index build time; query time for 1-, 2-, and 5-term queries (median over 100 runs); index size on disk. Compare with `ripgrep` (or `grep -r`) for the same single terms: when does an index beat scanning?

**Done when:** the evaluation table and timings are done.

---

## Testing guidance

- **Brute-force oracle:** every Boolean and phrase query checked against a scan of the fixture corpus.
- **Differential testing** for the hash table and the trie (against `dict` and sorted lists).
- **Golden ranking tests** on a small fixture corpus whose scores you computed by hand.

## Common pitfalls

- **Unsorted postings** break every merge. Assert sortedness after building.
- **Tombstones that never get cleaned up** fill the table; resizing should drop them.
- **Positions off by one** after removing stop words: decide whether positions count stop words (they should, or phrases break).
- **Evaluating on queries you tuned for.** Write judgements first, tune on 15 queries, test on the other 5.

## Communication deliverable

1. **Design doc** v1 → v2 with section 8 completed.
2. **Evaluation report** (2 pages, E10): goals vs results, precision@5 per configuration, timings, the index-vs-grep comparison, and the probe-length experiment.
3. **Demo:** Boolean, phrase, ranked, and misspelled queries on your real vault; autocomplete; the evaluation table.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 2, write the linear-probing insert/lookup/delete steps from memory; before Milestone 4, the merge |
| **F** | Hash table lookup; why idf uses a log |
| **W** | Tombstones; shortest-first intersection; length normalisation; min-heap for top-k; stemming yes/no — all decided with measurements |
| **S** | Subgoal comments for every structure operation |
| **I** | Hashing, merging, trees, DP, and parsing in one project |
| **T** | Design doc, evaluation report, demo |

## Stretch goals

- **Compressed postings:** store doc-id **gaps** (differences) as variable-length integers. Measure the size reduction.
- **Bloom filter** to skip documents that certainly don't contain a term (and measure its false-positive rate against the formula).
- **Web front-end:** serve search results over HTTP (preview of Module 09's Lantern).
- **Obsidian-aware ranking:** boost notes that many other notes link to (a tiny PageRank — Module 12's linear algebra explains it).

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Hash table | Open addressing + chaining; tombstones; resize; differential tests; probe plot vs theory | One method | Uses `dict` |
| Index | On-disk format documented; incremental updates; meets time goal | In memory only | Slow or wrong |
| Queries | Boolean + phrase + parser; brute-force tested | Boolean only | Fragile |
| Ranking | TF-IDF with normalisation; heap top-k; snippets | Unnormalised | Unranked |
| Autocomplete and suggestions | Trie + edit-distance trie walk; compared with brute force | Brute force only | Missing |
| Evaluation | Judgements first; precision@5 for 3 configs; held-out queries; timings | Partial | Missing |
| Communication | Doc lifecycle, report, demo | Most | Few |

**Done when:** every area at least 2; Hash table and Evaluation at 3.

## Connections

- **Back:** E02–E03 (stemming rules from spelling rules!), M11 (logs), Module 03 (birthday bound and hashing), Copydiff (Levenshtein), Labs 01–02 (merge, heap, measurement).
- **Forward:** Module 07 (the hash table in C), Module 11 (indexes inside a database; your Stratum engine's B+tree vs this hash index).

> **Originality note:** the project scope (your own vault), milestones, and evaluation design were written for this curriculum.
