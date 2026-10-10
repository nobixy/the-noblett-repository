---
title: "DR-005: Capstone and Maker Thread"
type: decision-record
status: accepted
date: 2026-10-09
accepted: 2026-10-09
tags:
  - adr
  - decision-record
---

# DR-005: Capstone and Maker Thread

*Uses the [[Decision Record]] template. Follows [[DR-004 - Content Overhaul|DR-004]]. Accepted and applied 2026-10-09. Checkpoint before this change: git commit `ff49dea`.*

## Context
The capstone goal is now fixed: **prototype AI drone-swarm technology with defense applicability**, using everything the program teaches. That needs more hands-on "maker" skill (breadboards, soldering, microcontrollers, Raspberry Pi, 3D printing, PCBs, robotics), much more network theory (graphs, consensus, wireless mesh), and cryptography as a core skill rather than an option. The constraints stay the same: ~20 h/week, free resources first (paid items marked 💲 with the cheapest path and a sim-first alternative), and the DR-001 ~8-year cap (≈8,320 h including habits). Every URL in the new notes was checked on 2026-10-09; prices are approximate unless a store page was checked that day (Pi, Crazyflie, Pinecil, RTL-SDR).

## Decision
**Capstone redesigned:** [[B30 - Magnum Opus Capstone|Block 30]] is now *Autonomous Drone Swarm Prototype*. Framing: a civilian research prototype with dual-use relevance: search-and-rescue/area survey (ISR-style sensing) and a resilient comms relay. Scope: decentralized coordination (consensus, formation, task allocation), multi-agent RL vs a classical baseline, on-board TinyML perception, encrypted and authenticated mesh (Noise/WireGuard, MAVLink 2 signing), GPS-denied navigation, fail-safes, threat model and red team. **Weapons, targeting and payload delivery are permanently out of scope.** Sim first (PX4/ArduPilot SITL, Gazebo, ROS 2 Lyrical, Crazyswarm2), then 3+ small drones indoors. Staged milestones M0–M6, each with a *done when*. New sections: Regulations & Ethics (TRUST, Part 107, 107.35 multi-drone waiver, Remote ID, FCC jamming ban, ITAR/EAR awareness, DoDD 3000.09 awareness, ACM ethics) and Career Path (defense-tech companies, SBIR/STTR, DIU, open-source contributions). The old generic HCI audit shrinks to a ground-station usability check.

**Added (8 core blocks, 590 h):**
- 🔧 [[B08b - Maker Lab 1 - Electronics Bench|Block 8b]] Maker Lab 1: Electronics Bench, Soldering and Arduino (Year 1, 40 h).
- 🔧 [[B09a - Maker Lab 2 - Embedded C|Block 9a]] Maker Lab 2: Embedded C on RP2350/ESP32 (Year 2, 80 h).
- 🔧 [[B15b - Maker Lab 3 - CAD and 3D Printing|Block 15b]] Maker Lab 3: CAD and 3D Printing (Year 2, 40 h).
- 🔧 [[B16a - Maker Lab 4 - Raspberry Pi and Embedded Linux|Block 16a]] Maker Lab 4: Raspberry Pi and Embedded Linux (Year 3, 50 h).
- [[B19a - Wireless, Mesh and Network Science|Block 19a]] Wireless, Mesh and Network Science (Year 3, 120 h): Bullo's *Lectures on Network Systems*, Barabási's *Network Science*, Kurose ch. 7, batman-adv/802.11s/ESP-NOW, receive-only SDR.
- 🔧 [[B21a - Maker Lab 5 - PCB Design|Block 21a]] Maker Lab 5: PCB Design with KiCad (Year 3, 40 h).
- [[B24a - Applied Cryptography and Protocol Security|Block 24a]] Applied Cryptography and Protocol Security (Year 4, 120 h): Boneh Crypto I + Boneh–Shoup, Noise, WireGuard, TLS 1.3, MAVLink 2 signing, fleet key management.
- 🔧 [[B27a - Drone Lab - Flight Stack, ROS 2 and SITL|Block 27a]] Drone Lab: PX4/ArduPilot SITL, Gazebo, ROS 2, Crazyswarm2, one real micro-drone (Year 4, 100 h).

The 🔧 Maker thread sits inside the stage folders where its prerequisites are met (lettered blocks, so the main numbering is unchanged); robotics coordinates with Track 9 and RF/SDR with Track 11.

**Changed:**
- [[B27 - Intensive Cryptopals|Block 27]]: Cryptopals is required (sets 1–6; 7–8 stretch), 130 → 100 h because Block 24a now carries the theory. The TLA+ option moved to Track 5.
- [[B19 - Networking|Block 19]] adds Kurose ch. 7 (wireless) and points to 19a; [[B32 - Information Theory|Block 32]] and [[E2 - Computer Security|E2]] gain capstone links.
- [[B23 - Distributed Systems|Block 23]] no longer requires Databases.
- Tracks 3, 5, 7, 9, 11 gain a Capstone Link section; Track 3 also requires Block 24a.
- `verify_curriculum.py` accepts any one-letter block suffix (8b, 15b).

**Made optional (outside the hour budget, 370 h):** [[B21 - Databases|Block 21 Databases]] (200 h) and [[B24 - Theory of Computation|Block 24 Theory of Computation]] (170 h): the least capstone-relevant core blocks. Replication and partitioning stay in Block 23; NP-completeness basics stay in Algorithms. Do them before Tracks 2/10 (Databases) or 5/8 (Theory), or after the capstone.

**Recommended tracks (not chosen):** Specialization A = [[T09 - Autonomous Robotics|Track 9 Robotics, Control and CPS]]; Specialization B = [[T07 - TinyML and Edge AI|Track 7 TinyML and Edge AI]]. Alternatives for B: Track 3 (security) or Track 11 (signals and comms).

## Consequences
**Hours:** core 5,805 → **5,995 h** (+590 new, −30 Cryptopals, −370 made optional). Plus two tracks (800 h) and habits (≈1,000–1,500 h) = **≈7,800–8,300 h**, under the ≈8,320 h cap with only ~25 h margin at the top of the habit range, so any future addition needs an equal cut. Stage loads (core blocks): Phase −1 120, Phase 0 325, Year 1 1,340, Year 2 1,510, Year 3 1,190, Year 4 990, Year 5 520. "Years" remain stages, not calendar years.

**Starter hardware (💲, cheapest path):** Maker Lab 1 bench ≈$95–125; Maker Lab 2 parts ≈$50–70; Maker Lab 3 $0 at a library/makerspace; Maker Lab 4 Pi Zero 2 W path ≈$60; Block 19a extra ESP32s ≈$20–30 + RTL-SDR $39.95; Maker Lab 5 ≈$30–55; Drone Lab DIY ESP-Drone ≈$40–70 (or Crazyflie 2.1+ $240). Through Year 4 ≈$350–450 total on the cheapest path; the capstone fleet adds ≈$150–200 (DIY) or ≈$800–900 (Crazyflie). Everything has a free simulator path.

**Harder / costs:** Databases leaves the 💼5 set (Employability keeps B23 Distributed Systems and B17 Software Construction). Defense-related work raises export-control and clearance questions that this vault can't answer; the capstone notes say where to ask. The day-job weekly schedule was **not** changed. Old notes in DR-001–004 and `99 - Archive` still describe the old capstone paths and the Cryptopals-or-TLA+ choice.

**Undo:** `git checkout -- . && git clean -fd` (back to `ff49dea`).
