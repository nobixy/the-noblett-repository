---
title: "Project: Crate"
module: "07-systems-programming"
hours: 40
artifact: "crate: an archive tool in C with a chunked, checksummed binary format; pack, list, extract, verify, and rescue commands; RLE and LZ-style compression; corruption injection tests; a fuzzing campaign; and path-traversal defences"
deliverable: "CRATE_FORMAT.md specification + design doc + robustness report (corruption and fuzzing) + 4-minute demo"
---

# Project: Crate

| | |
| :-- | :-- |
| **Module** | 07 Systems Programming |
| **Time** | About 40 hours |
| **Prerequisites** | Labs 01–03 of this module; Tone Loom (binary formats, endianness); Module 05 (hash tables for compression) |
| **You build** | `crate`, a tool that packs a folder tree into one archive file and gets it back exactly — and that **notices and survives damage**. Your own binary format, with CRC32 checksums you implement, compression you implement, a recovery mode that rescues what it can from a broken archive, and a fuzzer that throws a million mangled files at your code without one crash |
| **Deliverable** | Format specification, design doc, robustness report, and demo |

---

## Why this matters

File formats outlive the programs that write them. A good format is precisely specified, portable across machines, versioned, and **robust**: it detects corruption instead of silently returning garbage, and its reader never crashes or misbehaves on hostile input. Archive readers (zip, tar) have a long history of security bugs — especially "**path traversal**," where an archive entry named `../../.bashrc` overwrites files outside the target folder. You'll defend against it deliberately.

You'll also meet two classic algorithms — **CRC** for error detection and **LZ-style** compression — and **fuzzing**, one of the most effective bug-finding techniques ever invented.

**Real-world analogs:** zip, tar + gzip, 7z, zstd's frame format, PNG's chunks with CRCs, backup tools.

---

## The format (starting point — refine it in `CRATE_FORMAT.md`)

All integers **little-endian**. All offsets from the start of the file.

```
+--------------------------+
| Header (32 bytes)        |  magic "CRATE\0\x01\0", version u16, flags u16,
|                          |  entry_count u32, dir_offset u64, dir_length u32, header_crc u32
+--------------------------+
| Chunk 0                  |  chunk header (28 bytes): magic "CHNK", file_index u32, seq u32,
| Chunk 1                  |    raw_len u32, stored_len u32, method u8, pad[3], crc32_of_raw u32
| …                        |  then stored_len bytes of (maybe compressed) data
+--------------------------+
| Directory                |  per entry: path_len u16, path (UTF-8, '/' separators, relative),
|                          |    mode u32, mtime_sec u64, size u64, first_chunk_offset u64, chunk_count u32
|                          |  then dir_crc u32
+--------------------------+
```

- Files are split into **chunks** of at most 64 KiB raw. [W] Why chunk? (A damaged byte ruins one chunk, not the whole file; chunks can be checked and decompressed independently.)
- `method`: 0 = stored, 1 = RLE, 2 = LZ.
- The header is fixed-size and comes first; the directory comes last (so `pack` can stream data before it knows every offset). [W] What are the costs of putting the directory at the end? (Think: reading a damaged file; appending.)

---

## Milestones

### Milestone 1 — The specification and design doc

1. **`CRATE_FORMAT.md`** (E10 quality — your second binary-format specification after Tone Loom's, now with integrity checks): every field with offset, size, type, and meaning; the CRC definition; the compression formats (Milestone 5); versioning rules (what a reader must do with an unknown version or method); and a hex dump of a tiny example archive, annotated byte by byte.
2. **Design doc v1** (3–5 pages): architecture, error-handling strategy (every read checked; every error reported with offset and reason), the robustness goals ("no input file can crash `crate` or make it write outside the target folder"), test plan.

### Milestone 2 — CRC32 and the store-only round trip

1. **CRC32** (the same one used by zip, PNG, and Ethernet): table-driven, reflected polynomial 0xEDB88320, initial value 0xFFFFFFFF, final XOR 0xFFFFFFFF. Test vector: the CRC32 of the ASCII string `123456789` is **0xCBF43926**. Also compare with Python's `zlib.crc32` on random data (a second witness from a test script).
2. **`crate pack out.crate DIR`**, **`crate list`**, **`crate extract ARCHIVE DEST`** with method 0 (stored). Preserve relative paths, permissions (mode), and modification times. Write all integers with explicit little-endian helpers (Lab 01 Session 8).
3. **Round-trip test:** pack a varied tree (empty files, empty folders — decide how to represent them —, a 10 MB file, deep nesting, non-ASCII file names, a symlink — decide: store as a link, follow it, or skip with a warning [W]); extract to a new place; compare with `diff -r` and check modes and times.

**Done when:** round trips are exact; the CRC test vector passes.

**[F] Feynman target:** *how a CRC detects errors* — explain with polynomial division by hand on a tiny example (search "CRC by hand"), or at least explain why it catches every single-bit error and every burst shorter than 32 bits.

### Milestone 3 — Verify, and corruption injection

1. **`crate verify ARCHIVE`:** check the header CRC, every chunk's magic and CRC, the directory CRC, that every offset and length is within the file, that chunk sequences are complete — report **every** problem with its byte offset, without crashing.
2. **Every read is bounds-checked.** Before reading a length-prefixed field, check that the length fits in the remaining file. (This one rule prevents most archive-reader vulnerabilities.)
3. **Corruption injection tests:** a test script that takes a good archive and, for each region (header, a chunk header, chunk data, the directory, the final CRC), flips a random bit, then runs `verify` and checks that the right error is reported **for that region**. Also: truncate the file at 20 random places; append garbage; set `entry_count` to 4,000,000,000.

**Done when:** every injected corruption is detected and correctly located, and nothing crashes (run the tests under ASan).

### Milestone 4 — Rescue

When the directory is damaged, the data may still be there. **`crate rescue ARCHIVE DEST`:** scan the file for chunk magic numbers, validate each candidate chunk with its CRC, group valid chunks by file index and sequence, and extract complete files (and partial files with a `.partial` suffix and a report of missing chunks). File names are lost if the directory is gone — name them `file_<index>`; [W] how could the format be changed so names survive? (Hint: put each file's name in its first chunk too — and then argue about the cost.)

**Done when:** after destroying the directory of a 20-file archive, `rescue` recovers every file whose chunks are intact.

### Milestone 5 — Compression

1. **RLE** (run-length encoding): your own token format (e.g. a control byte meaning "the next byte repeats n times" or "n literal bytes follow"). Great on images with flat areas; useless (or harmful) on text. Never let a chunk get *bigger*: if compressed ≥ raw, store it raw (method 0).
2. **LZ-style** (the family behind gzip, zip, zstd): replace repeated byte sequences with **back-references** (distance, length) to an earlier occurrence within a sliding window (e.g. 32 KiB). Find matches with a **hash table** of 3-byte sequences → recent positions (Module 05!). Design your own token encoding (literals vs matches) and document it in `CRATE_FORMAT.md`.
3. **Measure** compression ratio and speed (MB/s) for stored, RLE, and LZ on: your vault (text), a folder of PNGs (already compressed — expect no gain), a WAV from Tone Loom, and a large log file. Compare with `gzip -6` and `zstd` (if installed) on the same inputs.

**Done when:** round trips stay exact with every method, and the comparison table is done.

### Milestone 6 — Fuzzing and path traversal

1. **Path traversal defence:** on extract, reject (with a clear error) any entry whose path is absolute, contains `..` components, or would resolve outside DEST after normalisation; refuse to follow symlinks inside DEST that point outside it. Test with hand-crafted malicious archives (write a tiny script that produces them).
2. **Your own fuzzer:** a mutation fuzzer that takes valid archives (a corpus of 10–20 small ones), mutates them (flip bits, change bytes to 0x00/0xFF/random, duplicate or delete ranges, truncate, splice two files), and runs `crate list`, `verify`, and `extract` (into a temporary folder) on each mutant under **ASan + UBSan**. Any crash, sanitizer report, hang (use a timeout), or file written outside the temp folder is a bug: save the input, shrink it, fix, add as a regression test.
3. Run **1,000,000** mutants (it's fast — it runs while you sleep).
4. **Stretch:** run **AFL++** (a coverage-guided fuzzer) on the same targets and compare what it finds.

**Done when:** a million mutants with zero crashes, zero sanitizer reports, and zero escapes, and every bug found along the way has a regression test.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why does fuzzing find bugs that careful hand-written tests miss?*

---

## Testing guidance

- **Round trips** on varied trees (the most important correctness test).
- **Test vectors** for CRC and for each compression method's token format (tiny hand-made inputs with known outputs).
- **Corruption injection** by region; **fuzzing** at scale; **malicious archives** by hand.
- **Durable writing:** `pack` writes to `out.crate.tmp`, `fsync`s, and renames (Lab 03); test by killing `pack` mid-way (the old archive must survive).

## Common pitfalls

- **Writing structs directly to disk** (padding and byte order leak into the format).
- **Integer overflow in size checks:** `offset + length > file_size` can overflow; write it as `length > file_size - offset` after checking `offset <= file_size`.
- **Trusting `path_len` or `chunk_count`** from the file to size an allocation (a fuzzer will hand you 4 GB requests) — cap and validate.
- **Following symlinks on extract** — the classic escape.
- **LZ matches that overlap their own output** (distance < length): legal and useful (it's how runs are encoded), but your decoder must copy byte by byte.

## Communication deliverable

1. **`CRATE_FORMAT.md`** — the specification, with an annotated hex dump.
2. **Design doc** v1 → v2.
3. **Robustness report** (2 pages): corruption-injection results by region, rescue results, the fuzzing campaign (number of executions, bugs found, each bug's class), and path-traversal tests.
4. **Demo (4 minutes):** pack your vault, corrupt a byte, verify pinpoints it, destroy the directory, rescue the files, and show the fuzzer running.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | The file layout, drawn from memory; the CRC parameters |
| **F** | How CRC detects errors; how LZ finds repeats |
| **W** | Chunking; directory at the end; symlinks; names in chunks; why fuzzing works |
| **S** | Bounds-checked read helpers; pack/extract subgoals |
| **I** | Formats, algorithms, and security together |
| **T** | Specification, design doc, report, demo |

## Stretch goals

- **Encryption** with a real library (libsodium) — correctly — as an optional method, with a note on why you didn't invent your own.
- **Deduplication:** identical chunks stored once (hash each chunk; Module 05).
- **Append mode:** add files to an existing archive by writing new chunks and a new directory at the end.
- **A Python reader** written only from your `CRATE_FORMAT.md` — a test of whether the spec is complete.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Specification | Complete, versioned, annotated hex dump; a second reader could be written from it | Mostly | Vague |
| Round trip | Exact for varied trees; modes and times; symlink decision | Mostly | Lossy |
| Integrity | CRC with test vectors; verify locates every injected error | Most | Weak |
| Rescue | Recovers intact files after directory loss | Partial | Missing |
| Compression | RLE + LZ; never expands; measured vs gzip/zstd | RLE only | Missing |
| Security and fuzzing | Traversal blocked; 1,000,000 mutants clean; regressions saved | Fewer runs | None |
| Communication | Spec, doc, report, demo | Most | Few |

**Done when:** every area at least 2; Integrity and Security at 3.

## Connections

- **Back:** Tone Loom (binary formats), Base Workshop (`minihex.py` for debugging archives), Lab 03 (fsync, rename), Module 05 (hash tables), Module 03 (probability that a CRC misses an error: about 1 in 2³² for random corruption).
- **Forward:** Module 08 (file systems: on-disk structures and crash consistency), Module 09 (checksums in packets: Courier uses a CRC), Module 11 (database pages with checksums and recovery).

> **Originality note:** the Crate format, rescue design, and robustness plan were written for this curriculum. CRC32 and LZ77-style compression are classic published techniques used here as components.
