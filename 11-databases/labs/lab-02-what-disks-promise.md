---
title: "Lab 02 — What Disks Promise"
id: "MOD11-LAB02"
type: "lab"
module: "11-databases"
phase: "D"
order: 1330
prerequisites: [MOD11-LAB01]
---

# Lab 02 — What Disks Promise

**Goal:** find out, by experiment, what is and isn't guaranteed when a program writes to disk — so that Stratum's recovery design rests on facts, not hope.

**Sessions:** three.

**Deliverable:** a short lab report: *"What survives a crash?"*

---

## Session 1 — The write path

When a program calls `write`, the data usually goes into the operating system's **page cache** (memory), not to the disk. The OS writes it to the device later. `fsync(fd)` asks the OS to push a file's data (and metadata) to the device and wait until the device says it's stored.

1. **Latency:** measure (in C or Python with `os.write` and `os.fsync`) the time for 1,000 writes of 100 bytes: (a) no fsync, (b) fsync after every write, (c) fsync after every 100 writes. Compute per-write cost. (This is the cost behind every "COMMIT" — and why databases batch commits: **group commit**.)
2. **Read the man pages** `fsync(2)`, `fdatasync(2)`, `rename(2)`, `open(2)` (`O_DIRECT`, `O_SYNC`) and write down, in your own words, exactly what each promises.
3. **The directory too:** after creating a new file and fsyncing it, the file's *name* lives in its directory, which is another file. To make the creation durable, fsync the **directory** as well (open it with `O_RDONLY` and fsync). [W] Why? (What does a crash right after the fsync of the file, but before the directory is written, leave behind?)

---

## Session 2 — Simulating crashes

You can't easily pull the plug on your laptop safely. Instead, simulate what a crash *can* leave behind:

1. **A fault-injecting file layer** (Python): a class that wraps a file and keeps a list of writes not yet "synced." On `sync()`, they become durable. On `crash()`, every un-synced write is **dropped** — or, with some probability, **partially applied** (only some 512-byte sectors of a 4 KiB page written: a **torn page**). Write the durable state to a real file so you can inspect it.
2. **Test three update strategies** for a small "settings" file under 1,000 random crashes each:
   - (a) overwrite in place;
   - (b) write a new temp file, then rename (without fsync);
   - (c) write temp, **fsync**, rename, **fsync the directory**.
   Count how often each leaves the file empty, torn (mixed old and new), or correct (old or new).
3. Which strategy did the Spelling Engine, Study Deck, and Crate use? Were they right?

---

## Session 3 — How SQLite does it

1. With `strace -f -e trace=openat,write,pwrite64,fsync,fdatasync,rename,unlink`, run a small Python program that does one `INSERT` and `COMMIT` in SQLite with `PRAGMA journal_mode=DELETE` (the default **rollback journal**). Find: the journal file being written, the fsyncs, the database file update, and the journal deletion.
2. Repeat with `PRAGMA journal_mode=WAL` (**write-ahead log**). Compare: which files are written, how many fsyncs per commit?
3. Read the SQLite documentation pages "Atomic Commit In SQLite" and "Write-Ahead Logging" (sqlite.org). They're among the clearest explanations of crash safety ever written — and good Level 4 copywork.

**[W]:** in WAL mode, a commit appends to the log and fsyncs it, but the main database file is updated later. Why is that safe? Why is it faster?

---

## Lab report

*"What survives a crash?"* — fsync costs, the man-page guarantees in your own words, the three-strategy fault-injection results, and how SQLite's two modes order their writes.

## Done when

- [ ] Timings measured; guarantees written; directory-fsync experiment explained.
- [ ] Fault-injection layer built (you'll reuse it in Stratum); three strategies tested.
- [ ] SQLite traces annotated; report written.

## Retrieval and reflection

1. **[R]:** page cache; what fsync guarantees; the safe replace recipe (temp, fsync, rename, fsync dir); torn pages; rollback journal vs WAL.
2. **[F] (spoken):** "Why does a database write its intentions to a log before changing the data?"
