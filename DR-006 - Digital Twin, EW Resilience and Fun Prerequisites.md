---
title: "DR-006: Digital Twin, EW Resilience and Fun Prerequisites"
type: decision-record
status: accepted
date: 2026-10-09
accepted: 2026-10-09
tags:
  - adr
  - decision-record
---

# DR-006: Digital Twin, EW Resilience and Fun Prerequisites

*Uses the [[Decision Record]] template. Follows [[DR-005 - Capstone and Maker Thread|DR-005]]. Accepted and applied 2026-10-09. Checkpoint before this change: git commit `c69a373`.*

## Context
Three requests:
1. Use real 3D map data to build video-game-quality environments for rerouting.
2. The biggest weakness of a swarm is electronic warfare: the link can be jammed and the electronics can be fried. Design for that, defensively.
3. Make the prerequisites more fun, use the Coursera Plus subscription, and use NeetCode Pro, which ends **Feb 6, 2027**.

The hour cap leaves ~25 h of margin (DR-005), so additions must be paid for by substitutions or trims. Every course, URL, license and price below was checked on 2026-10-09.

## Decision
**Capstone ([[B30 - Magnum Opus Capstone|Block 30]], 400 → 420 h):**
- New milestone **M2b, Digital twin and rerouting**: OpenStreetMap (ODbL) + USGS 3DEP (public domain) worlds in Gazebo, or Unreal Engine + Cesium for Unreal (Apache-2.0) + Cosys-AirSim or Project AirSim. Planning with A*, D* Lite and RRT* (OMPL), with live replanning around new obstacles, no-fly zones and radio-dead zones.
- Licensing notes:
  - Google Photorealistic 3D Tiles: 1,000 free events/month, then paid; streamed only, with attribution.
  - Cesium ion Community: free only for personal, non-commercial and unfunded-educational use.
  - Microsoft AirSim is no longer developed, and Colosseum was archived in July 2026: don't build on either.
- New **EW resilience** section, defensive and simulation only:
  - comms-denied autonomy: lost-link state machine, partitioned consensus, DTN store-and-forward per RFC 4838/9171
  - GPS-denied navigation: VIO, map matching against the twin, GNSS integrity checks
  - frequency diversity, hopping and spread spectrum; LPI/LPD awareness; multi-bearer fallback
  - hardware hardening as a design review: shielding, TVS, filtering, grounding; awareness of MIL-STD-461H (Apr 2026) and MIL-STD-464D
- EW criteria added to M3, M4 and M6. No jamming or spoofing transmissions and no EMP/HPM sources, ever: jamming is illegal under FCC rules.
- Thesis length trimmed from 15k–25k to 10k–15k words to help pay for this.

**[[B27a - Drone Lab - Flight Stack, ROS 2 and SITL|Drone Lab]]** (hours unchanged):
- Adds a digital-twin primer (OSM + 3DEP Gazebo world), a rerouting build and PX4 failure injection.
- The ArduPilot second stack becomes optional.
- Companions: the University of Toronto self-driving courses (Coursera Plus).

**[[B19a - Wireless, Mesh and Network Science|Block 19a]]** (120 → 130 h): a resilient-links module. Track 11 and Track 9 get notes.

**Fun prerequisites**, all as substitutions:

| Block | Fun build or extra | Replaces |
|---|---|---|
| B0 | Scratch quiz game | one written summary |
| BM | Scratch base/fraction visualizer; nandgame (free) or Turing Complete 💲 $19.99; 3Blue1Brown; *Code* optional early | one Khan practice set per pillar |
| BW | Twine branching story | 4 of the 14 copywork days |
| P1 | Learning How to Learn on Coursera Plus; Daily Code Streak starts | — |
| P2 | Human Resource Machine 💲 $14.99 | 2 of the 5 puzzle problems |
| P3 | Desmos art | one Khan practice set |
| P4 | CS50x final project as a game (LÖVE / Godot / p5.js free; PICO-8 💲 $14.99); Advent of Code in December | — |
| P5 | OverTheWire Bandit 0–20; Pico MicroPython blink | the Missing Semester shell exercises |

**NeetCode Pro sprint in [[P4 - Programming On-Ramp|P4]] (125 → 145 h), before Feb 6, 2027:**
- Python for Beginners
- Python for Coding Interviews
- Algorithms & Data Structures for Beginners
- NeetCode 150 easy problems as a daily streak

Free fallback after expiry: the neetcode.io roadmap, YouTube and LeetCode free. Block 13 and Block 20 point to the free lists; NeetCode Advanced Algorithms is optional and needs a renewal.

**Coursera Plus courses used** (each confirmed "included in Coursera Plus" on 2026-10-09):

| Course | Used in |
|---|---|
| Learning How to Learn | P1 |
| Programming for Everybody + Python Data Structures (UMich) | P4 failover |
| Nand to Tetris I & II (Hebrew Univ.) | B04 |
| Math for ML: Multivariate Calculus (Imperial) | B07 |
| Math for ML: Linear Algebra (Imperial) | B11 |
| Math for ML: PCA (Imperial) | B22a |
| Intro to Embedded Systems Software and Development Environments (CU Boulder) | B09a |
| Wireless Communications for Everybody (Yonsei) | B19a |
| Cryptography I (Stanford) | B24a |
| Intro to Self-Driving Cars; State Estimation and Localization; Motion Planning (U Toronto) | B27a and the capstone |
| Modern Robotics Course 1 (Northwestern) | Track 9 |
| Introduction to Game Design | optional after P4 |

Not used: UPenn Robotics/Aerial Robotics (no longer on Coursera); DeepLearning.AI's Machine Learning Specialization (not in Plus).

**Trims to pay for it:**
- [[P2 - Reading, Thinking, and Writing|P2]] 40 → 30 h (Adler Part 3 optional).
- [[B17 - Software Construction|Block 17]] 150 → 120 h: its build items 2–4 were already optional (DR-004) but still counted.

## Consequences
**Hours:** core 5,995 → **6,005 h** (+20 capstone, +10 Block 19a, +20 P4; −10 P2, −30 Block 17). With two tracks (800 h) and habits (≈1,000–1,500 h): **≈7,805–8,305 h**, under the ≈8,320 h cap with ~15 h margin. Any future addition needs an equal cut.

**Costs and flags:**
- Unreal / Isaac Sim need a strong GPU 💲; the Gazebo path runs on the current PC.
- Google 3D Tiles needs a billing account; stay under the free cap or skip it.
- Cesium ion's free plan does not cover funded or government work.
- The EW material is awareness and defensive design only.
- The NeetCode sprint depends on finishing it before Feb 6, 2027.
- The day-job weekly schedule was **not** changed.

**Undo:** `git checkout -- . && git clean -fd` (back to `c69a373`).
