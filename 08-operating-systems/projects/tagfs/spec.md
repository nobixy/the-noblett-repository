---
title: "Project: Tagfs"
module: "08-operating-systems"
hours: 50
artifact: "tagfs: a FUSE file system for Linux where folders are tags — files live once and appear under every tag they carry — with a journaled metadata store, crash recovery, a differential test suite against a model, and crash tests"
deliverable: "TAGFS.md semantics spec + design doc + robustness report (differential and crash tests) + 5-minute demo"
---

# Project: Tagfs

| | |
| :-- | :-- |
| **Module** | 08 Operating Systems |
| **Time** | About 50 hours |
| **Prerequisites** | Module 07 (C, system calls, Crate's on-disk thinking); Lab 02 of this module; Study Deck's append-only log idea |
| **Platform** | Linux with FUSE 3 (`fuse3` package and headers). WSL2 can work with extra setup; a Linux VM works everywhere |
| **You build** | A real file system you can mount and use with any program — `ls`, your editor, `cp` — in which **folders are tags**. A file is stored once and appears under every tag it has: `/tags/linux/rust/` lists files tagged both `linux` and `rust`. Moving a file into a tag folder adds the tag. The metadata is kept crash-safe with a journal, and you test that by killing the file system in the middle of operations |
| **Deliverable** | A semantics spec, design doc, robustness report, and demo |

---

## Why this matters

File systems are where operating systems meet permanent data. They have to map names to data, keep metadata consistent, behave the way every program expects (POSIX semantics), and **survive crashes** without corrupting themselves. **FUSE** (Filesystem in Userspace) lets you write one as an ordinary program: the kernel forwards file operations (`getattr`, `readdir`, `open`, `read`, …) to your process. You get a real mounted file system without kernel programming — and every tool on your system becomes a test client.

The tag idea makes it original and genuinely useful: your notes, photos, or study files, organised by many tags at once.

**Real-world analogs:** ext4, btrfs, and their journals; FUSE file systems like sshfs and rclone mount; tag-based organisers.

---

## Semantics (starting point — define them exactly in `TAGFS.md`)

Mount point layout:

```
/all/                 every file, flat (names must be unique across the file system)
/tags/                one folder per tag
/tags/rust/           files with the tag "rust"
/tags/rust/linux/     files with BOTH "rust" and "linux" (tags combine by nesting, in any order)
/untagged/            files with no tags
```

| Operation | Meaning |
| :-- | :-- |
| `cp notes.md /all/` | create a file (no tags) |
| `cp notes.md /tags/rust/` | create a file tagged `rust` |
| `mv /all/notes.md /tags/linux/` | add tag `linux` (a file "moved" into a tag folder gains the tag; it keeps its other tags) |
| `rm /tags/rust/notes.md` | remove the tag `rust` from the file (the file still exists in `/all/`) |
| `rm /all/notes.md` | delete the file entirely |
| `mkdir /tags/python` | create an (empty) tag |
| `rmdir /tags/python` | delete a tag (only if no file has it — or decide otherwise and document) |
| `ls /tags/rust/` | files with `rust`, **plus** sub-folders for every other tag that some `rust` file also has (so you can drill down) |
| reading and writing file contents | as normal, from any path the file appears under |

**[W] Decide and document:** what happens on `mv /tags/rust/a.md /tags/linux/` — add `linux` only, or move the tag (remove `rust`, add `linux`)? What does `ls -la` show as link counts? What if two tags have names that look like file names? Real users will try all of these.

---

## Storage design

- **Contents:** each file's data stored in a backing directory (e.g. `~/.tagfs/data/<file-id>`). Reads and writes pass through to it (`pread`/`pwrite`).
- **Metadata** (files: id, name, size, times, mode, tags; tags: names): kept **in memory** for speed, and made durable with a **journal** — an append-only log of operations (`CREATE id name`, `TAG id rust`, `UNTAG …`, `DELETE …`, `RENAME …`), each record with a length and a CRC32 (Crate!). On mount, **replay** the journal (Study Deck's idea). Periodically write a **checkpoint** (a full snapshot via temp file + fsync + rename) and truncate the journal.
- Every metadata change: append the record, `fsync` the journal (or batch for speed — measure the trade-off [W]), *then* apply in memory and reply to the kernel.

---

## Milestones

### Milestone 1 — Specs and a read-only tag view

1. **`TAGFS.md`** — the exact semantics above, every decision, and examples of each operation's effect.
2. **Design doc v1** (4 pages): FUSE operations you'll implement, data structures (hash maps from name to file, tag to set of files — Module 05), the journal format, the crash-safety argument, and the test plan.
3. **Hello FUSE:** with libfuse 3's high-level API in C (`fuse_main` with a `struct fuse_operations` — `getattr`, `readdir`, `open`, `read`), serve a fixed, hard-coded set of files and tags. Mount it (`./tagfs ~/mnt -f -d` — foreground with debug output, so you can watch every request the kernel sends). Browse with `ls` and `cat`.

**Done when:** you can `ls` nested tag folders and `cat` files from a hard-coded set.

### Milestone 2 — Full operations

Implement `create`, `write`, `truncate`, `unlink`, `mkdir`, `rmdir`, `rename`, `utimens`, `chmod` (store the mode), `release`, `flush`, `fsync` — following `TAGFS.md`. Check what `cp`, `mv`, `rm`, `touch`, `echo >>`, and your editor actually call (watch the `-d` debug output; editors often write a temporary file and rename it over the original — your semantics must handle that!).

**Done when:** a scripted session of everyday commands behaves exactly as `TAGFS.md` says.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: the sequence of FUSE calls for `echo hi > /tags/rust/a.md`. Feynman target: *how a program's `open()` reaches your code*.

### Milestone 3 — Durability: the journal

1. Journal records with lengths and CRCs; replay on mount; a torn final record (partially written) is detected by its CRC and ignored [W: why is ignoring it safe?].
2. Checkpointing and journal truncation.
3. Contents writes: decide what `fsync` on a file guarantees and implement it.

**Done when:** unmount and remount preserves everything.

### Milestone 4 — Differential testing against a model

1. A **model** in Python: a few dictionaries implementing `TAGFS.md`'s semantics directly (no FUSE).
2. A **random operation generator** (seeded): create, write, tag (mv), untag (rm in a tag), delete, rename, mkdir/rmdir, read, ls of random tag combinations.
3. Run each operation through the mounted Tagfs (using ordinary Python file operations on the mount point) **and** through the model; compare the results and the full visible tree after every step.
4. 10,000 operations per run, many seeds. Shrink failures (Module 05) and keep regression tests.

**Done when:** 20 seeds × 10,000 operations agree with the model.

### Milestone 5 — Crash tests

1. A test harness that runs random operations against the mount and **kills the Tagfs process with `SIGKILL`** at a random moment, unmounts (`fusermount3 -u`), remounts, and checks: the metadata replays without error; every operation that returned success before the kill is present; the file system's **invariants** hold (every file in `/all`; every tag listing consistent with file tags; no dangling data files — or a documented clean-up).
2. Run 500 kill-and-recover cycles.
3. **Fault injection (stretch-sized but valuable):** make the journal writer randomly write only part of a record before "crashing" (simulate a power cut mid-write); recovery must still succeed.

**Done when:** 500 cycles pass.

### Milestone 6 — Performance

Measure against a plain directory on your normal file system: create 10,000 files; `ls` a tag with 5,000 files; read and write throughput of a 1 GB file; metadata operations per second with `fsync` per record vs batched every 10 ms. Explain the costs (FUSE's kernel↔user round trips; fsync — Magnitudes Field Guide).

---

## Testing guidance

- **The model** is the oracle for semantics; **crash tests** check durability; **invariant checks** after recovery.
- Run Tagfs under ASan during tests (its daemon is just a C program).

## Common pitfalls

- **Editors' save patterns** (write temp, rename over) breaking tag semantics.
- **`readdir` performance** for big tags: don't scan every file per call; keep tag → file sets.
- **Inode numbers:** stable numbers per file help tools like `find` and `rsync`; decide how to assign them.
- **Unmount while busy:** `fusermount3 -u` fails if a shell's current directory is inside the mount.
- **fsync semantics** you didn't implement but promised.

## Communication deliverable

1. **`TAGFS.md`** — the semantics specification.
2. **Design doc** v1 → v2, including the crash-safety argument.
3. **Robustness report** (2 pages): differential testing (operations, seeds, bugs found), crash testing (cycles, failures found, fixes), performance table.
4. **Demo (5 minutes):** organise a folder of your notes by tags with ordinary commands; kill and recover; show the model test running.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | FUSE call sequences; journal record format |
| **F** | How a syscall reaches a FUSE daemon; why a journal makes crashes safe |
| **W** | Every semantic decision in `TAGFS.md`; fsync batching; ignoring torn records |
| **S** | Subgoals for each FUSE operation and for recovery |
| **I** | OS interfaces, data structures, durability, and testing |
| **T** | Spec, design doc, report, demo |

## Stretch goals

- **Tag expressions:** a `/query/` folder where `ls "/query/rust and not python"` uses your Truth Engine / Vault Search parser.
- **Full-text search** inside Tagfs, using Vault Search's index.
- **Content-addressed storage:** deduplicate identical files by hash.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Semantics spec | Exact, covers edge cases and editor patterns | Mostly | Vague |
| Operations | All listed ops; everyday tools work, including editors | Most | Read-only |
| Journal | CRC records, replay, checkpoints, torn-record handling | Basic log | Missing |
| Differential tests | 20 × 10,000 ops agree with the model | Fewer | None |
| Crash tests | 500 kill/recover cycles; invariants checked | Some | None |
| Performance | Measured and explained | Partial | Missing |
| Communication | Spec, doc, report, demo | Most | Few |

**Done when:** every area at least 2; Journal and Crash tests at 3.

## Connections

- **Back:** Study Deck (append-only log replay), Crate (CRCs, fsync, atomic rename), Module 05 (hash maps, sets), Burrow (processes and signals for the test harness).
- **Forward:** Seedling's SeedFS (a writable version would reuse this journal design), Module 11 (write-ahead logging and recovery in a database are the same idea, made rigorous).

> **Originality note:** the tag-folder semantics, journal design, and testing plan were created for this curriculum.
