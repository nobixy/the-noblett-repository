---
title: "Project: Stratum Storage"
module: "11-databases"
hours: 70
artifact: "The storage half of Stratum: a page file format, slotted pages with variable-length records, a buffer pool with LRU and CLOCK, heap files, a catalog, and a B+tree index with search, inserts with splits, deletes, range scans, and an invariant checker — benchmarked against SQLite"
deliverable: "STRATUM_FORMAT.md (on-disk spec) + design doc + benchmark report + 4-minute demo with a B+tree visualisation"
---

# Project: Stratum Storage

| | |
| :-- | :-- |
| **Module** | 11 Databases |
| **Time** | About 70 hours |
| **Prerequisites** | Labs 01–02 of this module; Crate (binary formats); Cache Simulator (replacement policies); Module 05 (trees, hash maps) |
| **Language** | Python recommended (C allowed) |
| **You build** | The storage engine of **Stratum**, your database: a single file divided into fixed-size **pages**; **slotted pages** that pack variable-length rows; a **buffer pool** that keeps hot pages in memory and decides which to evict; **heap files** for tables; a **catalog** describing tables and indexes; and a **B+tree** index — the data structure inside nearly every database — with an invariant checker and a visualiser |
| **Deliverable** | On-disk format spec, design doc, benchmark report, and demo |

---

## Why this matters

Databases are built in layers, and this is the bottom one: how rows become bytes in pages, and how pages move between disk and memory. The ideas are everywhere — file systems, key-value stores, search engines, even your Edit Buffer's piece table. The **B+tree** in particular is one of the most important data structures ever invented: it keeps millions of keys sorted with only 3–4 levels, so any key is found with a handful of page reads, and ranges come out in order.

**Real-world analogs:** SQLite's B-tree file format, PostgreSQL heap files and B-tree indexes, InnoDB pages, LMDB.

---

## Milestones

### Milestone 1 — Format spec, design doc, and the page file

1. **`STRATUM_FORMAT.md`** (Crate-quality): page size (4,096 bytes — [W] why a power of two, and why match the OS page size?), page types, the file header page (magic, version, page count, free-page list head, catalog root page), byte order, checksums per page (a CRC32 in each page header — detects torn pages from Lab 02!), and every page layout below, with a diagram.
2. **Design doc v1** (4–5 pages): layers and their interfaces, the buffer pool's policy, B+tree node layout and invariants, test strategy, and benchmarks planned.
3. **`PageFile`:** `allocate_page()`, `free_page(n)` (free list), `read_page(n) → bytes`, `write_page(n, bytes)`, with checksum verification on read. Use Lab 02's fault-injecting layer underneath (so later crash tests can use it).

### Milestone 2 — Slotted pages and records

1. **Record format:** for a table schema (column names and types: INT 64-bit, TEXT, maybe REAL), encode a row as a null bitmap + fixed-size fields + length-prefixed text. Round-trip property tests.
2. **Slotted page:** header (type, slot count, free-space pointer), a **slot array** growing from the front (each slot: offset and length of a record, or "deleted"), records packed from the back. Operations: insert (returns slot number), read, delete (tombstone), update (in place if it fits, else move within the page), **compaction** (squeeze out holes). A row's address is a **RID** = (page number, slot number) — stable even when records move inside the page [W: why does that matter for indexes?].
3. **Heap file** for a table: a chain (or list) of slotted pages; insert finds a page with space (keep a small free-space map); a full scan iterates over every live record.

**Tests:** randomised insert/delete/update sequences on a page checked against a Python dict model; compaction preserves every live record; scans return exactly the live records.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: draw a slotted page after three inserts and one delete, with every offset.

### Milestone 3 — The buffer pool

1. **Frames:** a fixed number of in-memory page buffers; a **page table** (hash map: page number → frame).
2. **`fetch(page) → frame`** (pin count +1; read from disk on a miss), **`unpin(page, dirty)`**, **`flush(page)`**, `flush_all()`.
3. **Replacement:** evict only unpinned frames; write dirty victims first. Implement **LRU** and **CLOCK** (an approximation of LRU with a reference bit and a sweeping hand). [W] Why do real databases often prefer CLOCK (or variants) over exact LRU?
4. **Experiment:** the "sequential flooding" problem — a full scan of a table larger than the pool evicts everything, destroying a hot set used by other queries. Demonstrate it (hit rate before/after a big scan) with LRU and CLOCK. Then try a fix (e.g. scans use a small ring of frames of their own) and measure.

**Tests:** pin counts never negative; a pinned page is never evicted; dirty pages are always written before reuse; hit rates on synthetic access patterns match your Cache Simulator's predictions for the same policy.

### Milestone 4 — The B+tree

Index keys (start with 64-bit integers; strings as a stretch) to RIDs.

- **Leaf nodes:** sorted keys with their RIDs, plus a pointer to the **next leaf** (for range scans).
- **Internal nodes:** sorted separator keys and child page pointers (n keys, n + 1 children).
- Each node is one page; compute your **fan-out** (how many keys fit) and the tree height for 1 million keys (M11: log base fan-out).

**Operations:**
1. **Search:** descend from the root to a leaf by binary search within each node.
2. **Insert:** into the right leaf; if it overflows, **split** it in two and push a separator up to the parent; splits can cascade to the root, which then splits and the tree grows one level taller. Write the subgoals first and work three examples on paper [S].
3. **Range scan:** find the first leaf, then follow next-leaf pointers.
4. **Delete:** remove from the leaf; first version may leave underfull nodes (**lazy** — many real systems do); then implement **redistribution and merging** to keep nodes at least half full.
5. **Invariant checker** `check_tree()`: keys sorted within every node; every key in a subtree is within its parent's separator bounds; all leaves at the same depth; leaf chain visits every leaf in key order; node fill ≥ 50% (if merging is implemented) except the root.
6. **Visualiser:** print the tree level by level (and/or write a Graphviz `.dot` file).

**Tests:** random insert/delete/search sequences (seeded) against a sorted Python list as model, with `check_tree()` after every operation for small trees; 1,000,000 sequential and random inserts with a final check; range scans compared with the model.

**Done when:** all tests pass and the visualiser shows a correct three-level tree.

**Checkpoint:** Milestone Checkpoint. Feynman target: *why a B+tree with a million keys is only three or four levels tall, and why that matters on disk*. Why-ladder target: *why do internal nodes hold only keys and pointers, not RIDs?*

### Milestone 5 — Catalog, tables, and indexes together

1. **Catalog:** system tables (stored in Stratum itself — a nice bootstrap problem [W]) listing tables (name, schema, heap file root) and indexes (name, table, column, B+tree root).
2. **API:** `create_table`, `insert_row` (also inserts into every index on that table), `delete_row`, `scan`, `index_lookup(key)`, `index_range(lo, hi)`.
3. **Persistence:** close and reopen the database; everything is found again via the catalog.

### Milestone 6 — Benchmarks

Against SQLite (via Python's `sqlite3`, with a matching table and index, `journal_mode=WAL`, inside one transaction for bulk loads):
- bulk insert of 1 million rows (with and without an index);
- 100,000 random point lookups by key;
- range scans of 1,000 and 100,000 keys;
- full table scans;
- your buffer pool's hit rate during each, for two pool sizes.

**Target (Python):** within 20× of SQLite on point lookups — SQLite is decades of optimised C, so a large gap is expected; your report must explain *where* the time goes (profile with `cProfile`).

---

## Testing guidance

- **Models everywhere:** dicts for pages, sorted lists for B+trees — every random operation compared.
- **Invariant checkers** run after every operation in test mode.
- **Reopen tests:** close and reopen between phases; checksums catch corruption on read.

## Common pitfalls

- **Forgetting to unpin** — the pool fills with pinned pages and deadlocks. Use a context manager (`with pool.page(n) as p:`) that unpins automatically.
- **Off-by-one in splits** (which key moves up; does it stay in the leaf too? — in a B+tree, leaf separators are **copied** up, internal separators **moved** up).
- **Modifying a page without marking it dirty** — changes vanish on eviction.
- **Endianness and struct padding** in page layouts (Crate's lessons).

## Communication deliverable

1. **`STRATUM_FORMAT.md`** — the on-disk specification.
2. **Design doc** v1 → v2.
3. **Benchmark report** (2 pages): results vs SQLite, profiles, buffer-pool hit rates, the flooding experiment.
4. **Demo (4 minutes):** insert a million keys while the visualiser shows the tree's height growing; a range scan; reopen and query.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Slotted page, buffer pool states, and B+tree splits drawn from memory |
| **F** | B+tree height; why buffer pools exist |
| **W** | Page size; RIDs; CLOCK vs LRU; copy-up vs move-up; catalog bootstrap |
| **S** | Insert-with-split and merge subgoals on paper first |
| **I** | Storage, data structures, and measurement interleaved |
| **T** | Format spec, design doc, report, demo |

## Stretch goals

- **String keys** with prefix compression in nodes.
- **Bulk loading** a B+tree from sorted data (much faster than repeated inserts — measure).
- **Hash index** (extendible hashing) and a comparison with the B+tree for point lookups vs ranges.
- **Overflow pages** for rows larger than a page.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Format and page file | Spec complete; free list; per-page CRC | Works | No spec |
| Records and pages | Slotted pages with compaction; model-tested | Works | Fragile |
| Buffer pool | Pins, dirty, LRU + CLOCK, flooding experiment | One policy | Leaky pins |
| B+tree | Search, insert/split, range, delete with merge, checker, visualiser | Lazy delete | Insert only |
| Catalog | Self-hosted catalog; reopen works | Hard-coded | Missing |
| Benchmarks | Full set vs SQLite with profiles | Partial | Missing |
| Communication | Spec, doc, report, demo | Most | Few |

**Done when:** every area at least 2; B+tree at 3.

## Connections

- **Back:** Crate, Cache Simulator, Module 05, Lab 02's fault injector.
- **Forward:** [Stratum Query and Recovery](../stratum-query-and-recovery/spec.md) builds on every layer here.

> **Originality note:** Stratum's format, layer boundaries, experiments, and milestones were designed for this curriculum. It is built from scratch rather than on any course's database skeleton.
