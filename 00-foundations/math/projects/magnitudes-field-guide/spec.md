---
title: "Project: Magnitudes Field Guide"
id: "FND-MA-PRJ-magnitudes-field-guide"
type: "project"
module: "00-foundations"
track: "math"
phase: "B"
order: 400
prerequisites: [M06]
stages: "M07"
artifact: "A measured, illustrated field guide to the sizes and speeds inside your own computer; measure.py and bits.py"
deliverable: "The guide itself (poster or one-page Markdown) + short recorded tour"
---

# Project: Magnitudes Field Guide

| | |
| :-- | :-- |
| **You build** | A field guide — like a bird-watcher's guide, but for the sizes and speeds inside your own computer — from the nanosecond of a CPU cycle to the 100-millisecond trip across an ocean, measured on your machine, written in scientific notation, and scaled to human time |
| **Deliverable** | The guide (a poster, or a one-page Markdown/HTML page) and a short recorded tour of it |

---

## Why this matters

Experienced engineers carry a mental map of how big and how fast things are. They know, without looking it up, that reading from memory is about a hundred times slower than adding two numbers, that reading from a disk is thousands of times slower than memory, and that a network trip across a continent takes tens of milliseconds. With that map, they can predict whether a design will be fast *before writing it*.

This project builds that map from your own measurements. It's pure M07: powers of 2 and 10, scientific notation, orders of magnitude. And you'll keep using the guide in every systems module.

**Real-world analogs:** the "latency numbers every programmer should know" lists that circulate among engineers (you're making your own, measured, version), capacity-planning estimates, back-of-the-envelope calculations in system design interviews.

---

## Milestones

### Milestone 1 — Collect your machine's numbers

Run these commands and record every number **with its unit, in ordinary form and in scientific notation**:

| Find | Command | Example of what to record |
| :-- | :-- | :-- |
| CPU clock speed | `lscpu` (look for "MHz") | 3,600 MHz = 3.6 × 10⁹ Hz |
| One CPU cycle (time) | compute: 1 ÷ clock speed | 1 ÷ 3.6 × 10⁹ ≈ 2.8 × 10⁻¹⁰ s ≈ 0.28 ns |
| Cache sizes (L1, L2, L3) | `lscpu` | L1d 48 KiB = 48 × 2¹⁰ B ≈ 4.9 × 10⁴ B |
| Memory (RAM) | `free -h` | 15 GiB ≈ 1.6 × 10¹⁰ B |
| Disk size | `df -h /` | 931 GiB ≈ 1.0 × 10¹² B |
| Memory page size | `getconf PAGESIZE` | 4,096 B = 2¹² B |
| Round trip to your router | `ip route` (the "default via" address), then `ping -c 10 <that address>` | average 1.2 ms = 1.2 × 10⁻³ s |
| Round trip to a nearby server | `ping -c 10 example.com` | |
| Round trip to a far-away server | ping a server on another continent (e.g. a university website abroad) | |

**Done when:** at least 10 measured numbers, each in two forms, with units.

**[W]:** Why do memory sizes come in powers of 2 (2¹² bytes per page) while clock speeds come in powers of 10 (3.6 GHz)?

### Milestone 2 — `measure.py`: time things yourself

Write a Python script that measures, using `time.perf_counter()`:

1. **One addition:** time a loop of 10,000,000 additions; divide. (Python is slow compared with the bare CPU — that's a finding, not a bug. Note how many CPU cycles one Python addition seems to take.)
2. **Reading memory:** create a list of 10,000,000 integers and time summing it; divide by the count.
3. **Reading a file from disk:** write a 200 MB file of random bytes (`os.urandom`), then time reading it back. (The second read will be faster: the operating system **caches** it in memory. Measure both and explain.)
4. **Starting a program:** time `subprocess.run(["true"])` 100 times; divide.

Report each result as a time per operation in scientific notation.

**Done when:** the script runs and prints a table; results recorded in your guide.

### Milestone 3 — Scale it to human time

Times like 2.8 × 10⁻¹⁰ s mean nothing to a human brain. Rescale: **pretend one CPU cycle takes one second.** Multiply every measured time by the same factor (1 ÷ cycle time) and express the result in human units (seconds, minutes, hours, days, years).

| Thing | Real time | If 1 cycle = 1 second |
| :-- | :-- | :-- |
| 1 CPU cycle | 0.28 ns | 1 second |
| ping to router | 1.2 ms | ≈ 4.3 × 10⁶ s ≈ 50 days |
| … | | |

**Done when:** every measured time has a human-scale equivalent, computed with scientific notation (show one calculation in full).

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: explain to a friend why "make the network call fewer times" is often the best way to make a program faster.

### Milestone 4 — `bits.py`: the two's complement explorer

A short script that makes M07 Part 7 visible:
- `python3 bits.py 8` prints every 8-bit pattern from `00000000` to `11111111` with its **unsigned** value and its **two's complement** value (sample every 16th row to keep it short, plus the interesting edges: 0, 1, 127, 128, 255).
- `python3 bits.py 8 --add 127 1` shows the addition bit by bit and reports **overflow** when the signed result is wrong.
- `python3 bits.py 8 --neg 5` shows "flip and add 1" step by step.

**Done when:** all three modes work and your output for 127 + 1 shows 10000000 = −128.

### Milestone 5 — The guide

Make the final field guide. Either a **poster** (paper, A3 or bigger) or a **one-page Markdown/HTML document**. It must contain:
1. **A size ladder** from 1 bit to your disk size, on a **powers-of-2** scale, with your measured cache, RAM, page, and disk sizes marked.
2. **A time ladder** from 1 CPU cycle to a cross-ocean ping, on a **powers-of-10** (log) scale, with your measured times marked. (Each step up the ladder is ×10. Draw it by hand if it's a poster: equal spacing per power of 10.)
3. **The human-time table** from Milestone 3.
4. **Three rules of thumb** you learned, each in one sentence. (Example: "Memory is about 100× slower than arithmetic; disk is about 1,000× slower than memory.")
5. A small **"bits" corner**: the 8-bit two's complement range and one overflow example.

**Done when:** the guide exists, every number is from your own machine (or labelled as looked-up), and every number has a unit.

---

## Common pitfalls

- **Missing units.** "1.2" means nothing. "1.2 ms" means something.
- **Mixing KB and KiB.** Use the unit the tool printed, and convert carefully (M06 Part 6).
- **Measuring caching by accident.** The second read of a file is from memory, not disk. That's not an error, it's a lesson; label it.
- **Linear scales for huge ranges.** On a normal scale, everything except the biggest number squashes into a dot at zero. That's why the time ladder must be logarithmic.

## Communication deliverable

The guide itself, plus a **short recorded tour**: walk through the time ladder from bottom to top, saying each step in human time. End with your three rules of thumb.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 5, write the time ladder from memory, then check against your measurements |
| **F** | "Make fewer network calls," explained plainly |
| **W** | Powers of 2 vs powers of 10; why the second file read was faster |
| **S** | The scientific-notation calculation in Milestone 3, written as labelled steps |
| **T** | The tour |

## Stretch goals

- **Cache cliff:** time summing lists of size 1 KiB, 2 KiB, 4 KiB, … up to 1 GiB (use the `array` module for compact storage). Plot time per item against size. Do you see jumps near your L1, L2, and L3 sizes? (This is a classic experiment you'll redo in C in Module 06, where the effect is much clearer.)
- **Speed of light check:** look up the distance to your far-away ping target. Light in fibre travels about 2 × 10⁸ m/s. What's the minimum possible round-trip time? How close is your measurement?

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Measurements | 10+ measured, both notations, units everywhere | Some units missing | Few numbers |
| Scripts | `measure.py` and `bits.py` work, overflow shown | One works | Neither |
| Human scale | Every time converted; one calculation shown in full | Most converted | Missing |
| Guide | Both ladders on correct scales; rules of thumb | Ladders present | Missing |
| Tour | Clear, under 2:30 | Recorded | Missing |

**Done when:** every area at least 2.

## Connections

- **Back:** M06 (units, prefixes), M07 (powers, scientific notation, two's complement).
- **Forward:** Module 06 (caches and memory), Module 07 (system calls, disk), Module 09 (network latency) — each module overview asks you to update your guide with new measurements.
