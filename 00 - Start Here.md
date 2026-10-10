---
title: "Start Here: The Noblett Repository"
type: hub
tags:
  - hub
  - navigation
  - curriculum
aliases: [Dashboard, Checklist, The Path]
---

# 00 - Start Here

Welcome to the **Noblett Repository**. This is a lifelong education and life-management system designed to build structural competence across computer science, practical engineering, and adult responsibilities. It is built on evidence, active practice, and sustainable maintenance.

*This one note is the dashboard, the checklist, and the map ([[DR-003 - One Path Restructure|DR-003]]). Block notes live in `01 - Curriculum/`, one folder per stage, in study order.*

**Now:** [[#🚀 Week 1 — Do This Today|Week 1: do this today]] → Starter Sprint builds for [[BM - Bedrock Mathematics|Bedrock Math]] + [[BW - Bedrock English and Grammar|Bedrock English]] · **Block order:** [[B0 - The Deep Learner's Toolkit|B0]] → [[BM - Bedrock Mathematics|BM]] → [[BW - Bedrock English and Grammar|BW]] → [[P1 - Learning How to Learn|P1]] · **Schedule:** [[Calendar]]

> - **Daily Study Log:** [[log.md]] (entries in `03 - Journal/`)
> - **Living Study Manifesto:** [[how-i-study.md]]
> - **Telemetry Log:** [[Telemetry Log.md]]
> - **Book Acquisition Tracker:** [[Your Shelf]]
> - **Every build, in order:** [[Projects Ladder]]

---

## 🚀 Week 1 — Do This Today
*Build first, read later ([[DR-008 - Project-First Start and Projects Ladder|DR-008]]). Each day is about an hour. Log each day in today's daily note (two minutes).*

- [ ] **Day 1 (today):** Make a 10-question **Scratch quiz game** at scratch.mit.edu (free, no install). Done when someone else can play it start to finish. Then do one lesson of NeetCode *Python for Beginners*: that starts your 🎮 Daily Code Streak (NeetCode Pro ends Feb 6, 2027).
- [ ] **Day 2:** Blink an LED on a simulated **Raspberry Pi Pico** at wokwi.com/pi-pico (free; use the MicroPython Blink template). Change it to flash SOS.
- [ ] **Day 3:** **Desmos art** at desmos.com/calculator: draw a face or a house using at least 10 equations.
- [ ] **Day 4:** **OverTheWire Bandit**, levels 0–3, from your own terminal (overthewire.org/wargames/bandit).
- [ ] **Day 5:** Add a timer and a high score to your Scratch game. Write a 5-line Feynman note on how the score works ([[Feynman Technique Note Template|template]]); the [[LM01 - Feynman Technique|LM01 project]] grows it into a short video or post.
- [ ] **Day 6 (Saturday build):** **nandgame.com**: build gates up to a half adder.
- [ ] **Day 7 (Sunday, 30 min):** Weekly review: what was fun, what was boring. Pick next week's build from the [[Projects Ladder#🪜 Starter Sprint (Weeks 1–12)|Starter Sprint]].
- [ ] **Every day:** one streak item (a NeetCode lesson or an easy problem, 20 min). Reading this week is optional: 10–15 min of Lockhart, *Arithmetic*, if you feel like it.

*After Week 1, follow the [[Projects Ladder]]: one fun build a week for 12 weeks, and the [[how-i-study#2a. Reading Ramp|Reading Ramp]] adds reading slowly.*

---

## 📊 Degree Progress
*Driven by each block's `status` and `hours_actual` frontmatter: update those, and this updates itself. Blocks flagged `optional: true` (Block 18 Real Analysis, the E1–E2 electives, and any specialization track not yet chosen) are left out.*

```dataview
TABLE WITHOUT ID status AS Status, length(rows) AS Blocks, sum(rows.hours_actual) AS "Hours logged", sum(rows.hours_estimate) AS "Hours planned"
FROM "01 - Curriculum"
WHERE block_id AND optional != true
GROUP BY status
```

```dataview
TABLE WITHOUT ID file.link AS "In progress", term AS Term, hours_actual + " / " + hours_estimate AS Hours, date_started AS Started
FROM "01 - Curriculum"
WHERE block_id AND status = "in-progress"
```

```dataview
TABLE WITHOUT ID key AS Stage, length(rows) AS Blocks, length(filter(rows.status, (s) => s = "done")) AS Done, sum(rows.hours_actual) AS "Hours logged", sum(rows.hours_estimate) AS "Hours planned"
FROM "01 - Curriculum"
WHERE block_id AND optional != true
GROUP BY stage
SORT key ASC
```

---

## The Path
*Print it or check boxes digitally only when the "Done when" line is true. Course notes follow the [[Block Note Template|Block Note Template]].*

> **Rule:** Do not skip prerequisites. Progress requires verifiable evidence (code, projects, problem sets), not just reading.

> [!NOTE] Legend
> **💼1–💼5** mark the **job-ready path**, the employability path through the stages (the source program's §5.3 "get employable" sequence; formerly the separate Core Spine): 💼1 Foundations & Programming Intro · 💼2 Data, Logic, and Proof · 💼3 Hardware & Systems Architecture · 💼4 Core Software Engineering · 💼5 Employability & Scale, closed by the [[Employability Portfolio and Review|Employability Portfolio]]. The numbers group blocks by phase; study order is still the list order. Each 💼 block note carries `job_ready: <phase>`. SICP was optional depth in Phase 1 and stays unmarked.
> Numbering is canonical ([[DR-002 - Vault Refactor and Canonical Numbering|DR-002]]): B0/BM/BW (Phase −1), P1–P5 (Phase 0), Blocks 1–30 from the source program, bridges 4a/8a/15a (core since DR-004), new core blocks 22a/23a/25a (DR-004), Block 31 = Specialization B Course 2, Block 32 = Information Theory, E1–E2 = optional electives, Tracks 1–11 = specializations. Block 5 (SICP) was cut by DR-004. Each note's `block_id` and title match this list.

---

### Phase -1: Bedrock Foundations (The Ground Floor)
*🚀 **Build first ([[DR-008 - Project-First Start and Projects Ladder|DR-008]]):** Phase −1 starts with the [[#🚀 Week 1 — Do This Today|Week 1 checklist]] and a 12-week Starter Sprint of fun builds ([[Projects Ladder]]). The books are 10–30 min companions that ramp up slowly ([[how-i-study#2a. Reading Ramp|Reading Ramp]]), not the starting line. Every block on The Path has at least one build with a done-when line.*
*🎮 Every Phase −1/0 block now has a fun build (Scratch, Twine, Desmos, OverTheWire, a game for CS50) and the 🎮 Daily Code Streak ([[DR-006 - Digital Twin, EW Resilience and Fun Prerequisites|DR-006]]). **NeetCode Pro ends Feb 6, 2027**: do the NeetCode sprint in [[P4 - Programming On-Ramp|P4]] before then; the free fallback is the neetcode.io roadmap + YouTube + LeetCode free. Coursera Plus courses are listed in each block's Companion section.*
- [ ] **[[B0 - The Deep Learner's Toolkit|B0]]:** The Deep Learner's Toolkit — *Mastery of Feynman Technique, Elaborative Interrogation, Franklin Copywork, Subgoal Labeling, and Blank-Sheet Retrieval.*
- [ ] **[[BM - Bedrock Mathematics|BM]]:** Bedrock Mathematics (builds first: Scratch, Desmos, nandgame, Python primes; Khan Academy Pre-Alg → Alg I; ✓ *Lockhart, Arithmetic* as a 15-min companion) — *Complete conceptual understanding of counting, base-10, fractions, negative multiplication, and algebraic balance scales.*
- [ ] **[[BW - Bedrock English and Grammar|BW]]:** Bedrock English & Grammar (builds first: Twine story, Python sentence machine; Williams *Style* as a companion from Week 5; Huddleston & Pullum for lookups only) — *Sentence diagramming, de-nominalization fluency, and 14 consecutive days of Franklin Copywork completed.*

---

### Phase 0: Prerequisites (0–5 months)
- [ ] **[[P1 - Learning How to Learn|P1]]:** Learning how to learn (*Learning How to Learn* course + a Python flashcard app; ✓ *Mind for Numbers* as a companion; *Make It Stick* moved to Year 1 reading) — *Study system written in [[how-i-study]], weekly template created, 20 Anki cards created.*
- [ ] **[[P2 - Reading, Thinking, and Writing|P2]]:** Reading, thinking, writing (Adler, Keshav, Pólya, Hermans, McEnerney, Winston) — *Four builds exist in [[Writing Hub|Writing Hub]] & [[Paper Reading Hub|Paper Reading Hub]].*
- [ ] **[[P3 - Math Prerequisites|P3]]:** 💼1 Math prerequisites (✓ *Velleman* 1–3; *Arithmetic* is read in BM) — *Cold test passed; clean induction & contradiction proofs.*
- [ ] **[[P4 - Programming On-Ramp|P4]]:** 💼1 Programming on-ramp (*CS50x* + NeetCode Pro sprint before Feb 6, 2027; CS50 final project as a game) — *300-line valgrind-clean C program; hash table & BST from scratch.*
- [ ] **[[P5 - Tooling|P5]]:** Tooling + notes repo (*Missing Semester*, OverTheWire Bandit 0–20, ✓ *How Linux Works* 1–7) — *[[log]] has 14 consecutive daily entries & headless Linux mastery.*

---

### Year 1: Learn to Program. Learn to Prove.
*🔧 = Maker thread (Labs 1–5 + Drone Lab), the hands-on track that runs beside the theory and feeds the capstone ([[DR-005 - Capstone and Maker Thread|DR-005]]).*
- [ ] **[[B01 - CS61A|Block 1]]:** 💼1 Berkeley CS61A (*Composing Programs*, Scheme interpreter + extension) — *Past CS61A final timed & closed-book ≥70%.*
- [ ] **[[B02 - Calculus I|Block 2]]:** Calculus I (MIT 18.01SC, Strang) — *18.01 final, timed, closed-book, passed.*
- [ ] **[[B03 - Physics I|Block 3]]:** Physics I (MIT 8.01SC, ✓ *Six Easy Pieces*) — *8.01 final passed.*
- [ ] **December Prep:** ✓ *How Computers Really Work* — hardware half.
- [ ] **[[B04 - Nand2Tetris|Block 4]]:** 💼3 Nand2Tetris (Hardware & software) — *A Jack program you wrote runs on the CPU you built.*
- [ ] **[[B04a - Differential Equations Bridge|Block 4a]]:** Differential Equations Bridge (MIT 18.03SC, Strogatz) — *Construct adaptive RK4/RKF45 chaos simulator; 18.03 final passed.*
- ~~Block 5: SICP~~ — *cut by [[DR-004 - Content Overhaul|DR-004]]: CS61A and Block 12 already cover it; chapters 1–3 are optional reading in Block 1 ([[Cut - B05 - SICP|archived note]]).*
- [ ] **[[B06 - C Fluency|Block 6]]:** 💼3 C Fluency (✓ *K&R*, ✓ *Zingaro* 1–5, ✓ *How Linux Works* 8–17) — *Valgrind-clean builds; whiteboard explanation of pointer arithmetic, struct padding, stack frame.*
- [ ] **[[B07 - Multivariable Calculus|Block 7]]:** Multivariable Calculus (MIT 18.02SC) — *18.02 final passed.*
- [ ] **[[B08 - Physics II|Block 8]]:** Physics II (MIT 8.02) — *8.02 final passed.*
- [ ] **[[B08a - Circuits and Electronics Bridge|Block 8a]]:** Circuits & Electronics Bridge (MIT 6.002 / 6.2000, Agarwal & Lang) — *Design & test 4th-order Sallen-Key Butterworth filter in SPICE & breadboard.*
- [ ] **[[B08b - Maker Lab 1 - Electronics Bench|Block 8b]]:** 🔧 Maker Lab 1: Electronics Bench, Soldering & Arduino (SparkFun/Adafruit, Wokwi sim first) — *Soldered kit, sensor logger, MOSFET motor driver all work.* *(new, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **Year 1 Companion Reading:** ✓ *What Is Mathematics?* ch. 1–2, 6–8 · *Make It Stick* (moved from P1) · Adler, *How to Read a Book* Part 2 (moved from P2) ([[DR-008 - Project-First Start and Projects Ladder|DR-008]]).
- [ ] **Year 1 Writing Deliverable:** 12 published technical blog posts + one 2,000-word essay with visible revision history.

---

### Year 2: The Systems Year
- [ ] **[[B09 - Computer Systems|Block 9]]:** 💼3 Computer Systems (✓ *CS:APP*, CMU 15-213) — *All 7 labs pass; malloc lab score ≥90.*
- [ ] **[[B09a - Maker Lab 2 - Embedded C|Block 9a]]:** 🔧 Maker Lab 2: Embedded C on RP2350/ESP32 (Pico SDK, ESP-IDF/FreeRTOS, Valvano) — *Own IMU driver; propeller see-saw holds ±3° with PID.* *(new, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **[[B10 - Math for CS|Block 10]]:** 💼2 Mathematics for Computer Science (MIT 6.1200J / 6.042J, ✓ *Velleman* 4–7, ✓ *What Is Math?* 3–5) — *6.042 final passed, timed.*
- [ ] **[[B11 - Linear Algebra|Block 11]]:** Linear Algebra (MIT 18.06 + Axler *LADR* 4e) — *18.06 final passed & Axler ch. 1–5 exercises done; NumPy builds.*
- [ ] **[[B12 - Interpreters|Block 12]]:** 💼4 Interpreters (✓ *Ball* Go Monkey → Nystrom *clox*) — *clox passes book's full test suite.*
- [ ] **[[B13 - Algorithms I|Block 13]]:** 💼4 Algorithms I (MIT 6.006, CLRS, ✓ *Zingaro* 6–10, ✓ *Algorithms to Live By*) — *6.006 final passed; Codeforces rating ≥1200.*
- [ ] **[[B14 - Computer Architecture|Block 14]]:** 💼3 Computer Architecture (ETH Zürich DDCA Mutlu, Harris & Harris RISC-V) — *Pipelined RISC-V core runs compiled C program.*
- [ ] **[[B15 - Probability|Block 15]]:** Probability (MIT 6.041 / 6.3700) — *Final passed; derive standard distributions/moments & solve Markov chains.*
- [ ] **[[B15a - Signals and Systems Bridge|Block 15a]]:** Signals & Systems Bridge (MIT 6.003 / 6.3000, Oppenheim & Willsky) — *Implement real-time audio FFT DSP filterbank in C or Rust.*
- [ ] **[[B15b - Maker Lab 3 - CAD and 3D Printing|Block 15b]]:** 🔧 Maker Lab 3: CAD & 3D Printing (Onshape/FreeCAD, PrusaSlicer, makerspace) — *Enclosure, IMU damper mount, prop guard fit by revision 3.* *(new, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **Year 2 Breadth (HASS):** Petzold, *Code, 2nd ed.* / Sandel, *Justice*.
- [ ] **Year 2 Writing Deliverable:** 12 posts + 5,000-word technical design doc (CPU or interpreter) + monthly paper summaries (3-pass).

---

### Year 3: Depth
- [ ] **[[B16 - Operating Systems|Block 16]]:** 💼4 Operating Systems (✓ *How Linux Works* reread, OSTEP, MIT 6.1810 xv6) — *All xv6 labs pass make grade + minimal bootable kernel.*
- [ ] **[[B16a - Maker Lab 4 - Raspberry Pi and Embedded Linux|Block 16a]]:** 🔧 Maker Lab 4: Raspberry Pi & Embedded Linux (Bootlin, libgpiod, Buildroot) — *Companion computer survives 50 power cycles + 1 h UART fuzzing.* *(new, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **[[B17 - Software Construction|Block 17]]:** 💼5 Software Construction (MIT 6.102 readings + 6.005 psets, Ousterhout *Philosophy of Software Design*) — *Rebuilt clox/Monkey under spec, rep invariants, AF.*
- [ ] **[[B18 - Real Analysis|Block 18]]** *(optional since [[DR-004 - Content Overhaul|DR-004]], outside the hour budget)*: Real Analysis (Abbott *Understanding Analysis*, MIT 18.100A) — *Prove Bolzano–Weierstrass, EVT, uniform-continuity from definitions unaided.*
- [ ] **[[B19 - Networking|Block 19]]:** 💼4 Networking (Stanford CS144, Kurose & Ross) — *All 8 labs pass; TCP stack fetches real web page.*
- [ ] **[[B19a - Wireless, Mesh and Network Science|Block 19a]]:** Wireless, Mesh & Network Science (Bullo *Network Systems*, Barabási, Kurose ch. 7, batman-adv/802.11s) — *Consensus on a real mesh matches the λ2 prediction within 2x.* *(new, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **[[B20 - Algorithms II|Block 20]]:** Algorithms II (MIT 6.046J, Kleinberg & Tardos) — *6.046 final passed; Codeforces ≥1600; 45-min unseen problem.*
- [ ] **[[B21 - Databases|Block 21]]** *(optional since [[DR-005 - Capstone and Maker Thread|DR-005]], outside the hour budget)*: Databases (CMU 15-445, BusTub, DDIA) — *All four BusTub projects pass Gradescope; DDIA read cover to cover.*
- [ ] **[[B21a - Maker Lab 5 - PCB Design|Block 21a]]:** 🔧 Maker Lab 5: PCB Design (KiCad) — *Own 2-layer MCU + IMU board passes DRC and brings up.* *(new, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **[[B22 - Statistics|Block 22]]:** Statistics (Wasserman *All of Statistics*, McElreath *Statistical Rethinking*) — *Real dataset MLE, CI, hypothesis tests, MCMC Bayesian inference.*
- [ ] **[[B22a - Machine Learning|Block 22a]]:** Machine Learning (MIT 6.390 + MITx 6.036 OLL autograder, Stanford CS229 notes) — *All OLL exercises pass; regression, classifiers, a neural net and k-means built from scratch in NumPy.* *(new, DR-004)*
- [ ] **Year 3 Breadth (HASS):** MIT 14.01 Microecon / MIT 5.111 / 7.01SC Science.
- [ ] **Year 3 Writing Deliverable:** 8,000-word survey of one subfield (30+ cited sources, adhering to PRISMA guidelines) + reproducible environments (e.g., Docker) for all code + 2 public recorded talks.

---

### Year 4: Advanced Core and Specializations
*Specialization A opens at Block 26, once Blocks 23–25a are done. Choose both tracks before Block 26 and clear `optional: true` on those two notes (DR-001). Employability Portfolio due by end of Year 4.*
- [ ] **[[B23 - Distributed Systems|Block 23]]:** 💼5 Distributed Systems (MIT 6.5840 / 6.824, Kleppmann) — *All labs pass 500 consecutive runs under `go test -race`.*
- [ ] **[[B23a - Parallel Computing|Block 23a]]:** Parallel Computing (Stanford CS149: SIMD, threads, CUDA) — *Assignments 1–3 correct and fast; thread pool clean under ThreadSanitizer.* *(was elective E4; core since DR-004)*
- [ ] **[[B24 - Theory of Computation|Block 24]]** *(optional since [[DR-005 - Capstone and Maker Thread|DR-005]], outside the hour budget)*: Theory of Computation (MIT 18.404J Sipser videos, ✓ *Hopcroft*) — *18.404J final passed; prove NP-completeness and undecidability by reduction.*
- [ ] **[[B24a - Applied Cryptography and Protocol Security|Block 24a]]:** Applied Cryptography & Protocol Security (Boneh Crypto I, Boneh–Shoup, Noise/WireGuard, MAVLink 2 signing) — *Crypto I done; secure swarm link fails closed under replay/tamper.* *(new, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **[[B25 - Convex Optimization|Block 25]]:** Convex Optimization (Boyd & Vandenberghe, Stanford EE364A) — *EE364A homework 1–8 done; CVXPY project + manual KKT.*
- [ ] **[[B25a - Deep Learning|Block 25a]]:** Deep Learning (Karpathy *Zero to Hero*, Stanford CS231n, Prince *UDL*) — *Autograd engine + GPT from scratch; CS231n assignments 1–3 pass their checks.* *(new, DR-004)*
- [ ] **[[Specialization Branches|Block 26]]:** Specialization A — Course 1.
- [ ] **[[B27 - Intensive Cryptopals|Block 27]]:** January Intensive: Cryptopals (required since [[DR-005 - Capstone and Maker Thread|DR-005]]) — *Sets 1–6 solved with tests; 7–8 stretch.*
- [ ] **[[B27a - Drone Lab - Flight Stack, ROS 2 and SITL|Block 27a]]:** 🔧 Drone Lab: PX4/ArduPilot SITL, Gazebo, ROS 2, Crazyswarm2 — *10/10 SITL missions (3 vehicles); one micro-drone flies indoors; failsafes logged.* *(new, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **[[Specialization Branches|Block 28]]:** Specialization A — Course 2.
- [ ] **[[Specialization Branches|Block 29]]:** Specialization B — Course 1.
- [ ] **[[Employability Portfolio and Review|Employability Portfolio]]** 💼5 — *Due by end of Year 4: three public projects, resume, outside review ([[DR-001 - Program Scope, Phases, and Timeline|DR-001]]).*
- [ ] **Year 4 Breadth (HASS):** MIT 6.805 Ethics / Hofstadter *Gödel, Escher, Bach*.
- [ ] **Year 4 Writing Deliverable:** Capstone proposal = Capstone milestone M0 (3,000 words: problem, related work, plan, evaluation criteria, threat model, safety case).

---

### Year 5: The MEng Year
- [ ] **[[B30 - Magnum Opus Capstone|Block 30]]:** Capstone: Autonomous Drone Swarm Prototype (decentralized coordination, secure mesh, on-board perception, GPS-denied nav, digital-twin rerouting, EW resilience in simulation; sim first, then 3+ small drones; no weapons) — *Milestones M0–M6 (+ M2b digital twin) met.* *(redesigned, [[DR-005 - Capstone and Maker Thread|DR-005]])*
- [ ] **Capstone Artifact:** Public artifact with documentation.
- [ ] **Capstone Thesis:** 10,000–15,000 words (trimmed by DR-006).
- [ ] **Capstone Talk:** 30-minute recorded presentation.
- [ ] **Capstone Outside Review:** Written critique from external reviewer.
- [ ] **[[Specialization Branches|Block 31]]:** Specialization B — Course 2 (alongside the Capstone).
- [ ] **[[B32 - Information Theory|Block 32]]:** Information Theory (David MacKay, Cover & Thomas) — *Derive Shannon entropy, channel capacity, Huffman/Arithmetic encoders, and LDPC codes.*
- [ ] **Year 5 Breadth (HASS):** Yale Open Course (History) + Great-books sequence / Prose *Reading Like a Writer*.

---

### Optional Electives (E1–E2)
*Outside the year plan and the hour budget ([[DR-002 - Vault Refactor and Canonical Numbering|DR-002]]). Take one only when its prerequisites are done and it doesn't displace a block on The Path (Operating Rule 2).*
- [ ] **[[E1 - Artificial Intelligence|E1]]:** Berkeley CS188, Russell & Norvig. Needs Math for CS, Probability, Algorithms I.
- [ ] **[[E2 - Computer Security|E2]]:** MIT 6.1600, Anderson *Security Engineering*. Needs Computer Systems, Networking, Math for CS.

---

## Specialization Branches (Elective)
*Specialization A starts at Block 26, after every 💼5 course is done (Year 4 in [[#The Path|The Path]]). Pick two tracks for the Program and run them one at a time; the rest are Lifelong Continuation. Entering early "when professionally required" needs a Decision Record.*

**Recommended for the drone-swarm capstone ([[DR-005 - Capstone and Maker Thread|DR-005]]; a recommendation, not a choice):** Specialization A = [[T09 - Autonomous Robotics|Track 9 Robotics, Control and CPS]]; Specialization B = [[T07 - TinyML and Edge AI|Track 7 TinyML and Edge AI]]. Alternatives for B: Track 3 Security or Track 11 Signals and Communications.

- [[T01 - Deep AI and Machine Learning|Track 1 - AI and Machine Learning]]
- [[T02 - Advanced Systems and Performance|Track 2 - Systems and Performance (incl. Rust)]]
- [[T03 - Advanced Security and Cryptography|Track 3 - Security and Cryptography]]
- [[T04 - Advanced Graphics and Vision|Track 4 - Graphics and Vision]]
- [[T05 - Advanced Programming Languages and Compilers|Track 5 - PL, Compilers and Verification]]
- [[T06 - Advanced Computer Engineering|Track 6 - Computer Engineering]]
- [[T07 - TinyML and Edge AI|Track 7 - TinyML and Edge AI]]
- [[T08 - Quantum Information and Computing|Track 8 - Quantum Information]]
- [[T09 - Autonomous Robotics|Track 9 - Robotics, Control and CPS]]
- [[T10 - Full-Stack and Product Engineering|Track 10 - Full-Stack and Product]]
- [[T11 - Signal Processing and Communications|Track 11 - Signal Processing and Communications]]

---

## Habits — Running Tally
- [ ] 500 words/day streak: `0` days
- [ ] Anki: daily since `____`
- [ ] Breadth subjects completed: `0` / 8
- [ ] Codeforces rating: `____` (Target: ≥1200 by Y2, ≥1600 by Y3)
- [ ] Talks given: `0` / 8 (from Year 2)
- [ ] Foreign language level: `____` (Target: B1)
- [ ] Books read for pleasure this year: `0`
- [ ] [[how-i-study]] last revised: `2026-10-10`

---

## How This System Works

### System Architecture

The repository operates on five integrated tracks. Do not attempt to run multiple high-intensity tracks simultaneously. 

1. **[[#The Path|The Path]]**: The linear, dependency-aware sequence of every block, in study order. 💼 marks the job-ready path.
2. **[[#Maintenance Tracks|Maintenance Tracks]]**: Continuous, low-friction daily habits for mathematics, reading, and writing.
3. **[[Engineering Practice|Engineering Practice]]**: Applied tooling, building, testing, and operational skills that run parallel to theory.
4. **[[Human Systems|Human Systems]]**: The infrastructure of adult life (money, health, time, relationships) required to sustain long-term intellectual work.
5. **[[Specialization Branches|Specialization Branches]]**: Deep elective domains unlocked only after reaching baseline employability.

### Maintenance Tracks

Continuous, low-friction daily habits:
- **Mathematics**: Daily proofs, discrete math, or linear algebra practice.
- **Reading**: Seminal papers and technical literature.
- **Writing**: Daily technical writing or reflections.

### 🧭 North Star
**Goal:** Complete the equivalent of a rigorous MIT Course 6-3 SB + MEng, and then continue executing an infinite, lifelong learning sequence bridging post-doc level depth across quantum computing, computational biology, formal verification, and pure mathematics. This is a magnum opus of self-education.

**Budget:** The *Program* (Phase −1 → Year 5 Capstone: core blocks + two specialization tracks + habits, ≈7,800–8,300 h; see [[DR-006 - Digital Twin, EW Resilience and Fun Prerequisites|DR-006]]) is timeboxed at ~8 years; below 15 hrs/wk, cut scope (Physics → Statistics → second track) instead of extending. After the Capstone, *Lifelong Continuation* (remaining tracks and beyond) has no deadline. Structure: 7 stages (Phase −1, Phase 0, Years 1–5) in [[#The Path|The Path]]; the 💼1–💼5 markers there are the employability path through them. See [[DR-001 - Program Scope, Phases, and Timeline|DR-001]].

**The five rules** (from [[The Independent EECS Program.pdf|the source program]]):
1. No lecture without its problem set the same week.
2. A block is done when its *Done when* line is true. Not before.
3. Never start a new block until the current one is done.
4. Math and writing are daily habits and are never paused.
5. Keep a daily log, in git.

**Guardrails for this vault:**
- The *Study Notes, Psets & Proofs* section of every block is written by me, from a blank page. Each block's **Check your work** callout names the course's own solutions, autograder, or test suite; I open it only after my own attempt.
- The vault serves the study, not the other way round. No new structure until the current block needs it.


### Operating Rules

1. **Objective Completion:** A block is only complete when its defined output (project, pset, artifact) is finished and verified. Consumption does not equal completion.
2. **One Primary Challenge:** Run only one high-intensity block or Specialization course at a time.
3. **Daily Maintenance:** Math and writing are continuous, low-friction habits. Do not pause them, but scale their volume to fit the day.
4. **Continuous Engineering Practice:** Theory must be immediately paired with practical tooling (Git, Linux, testing).
5. **Spaced Retrieval:** Rely on spaced review and active recall, not rereading.
6. **Missed-Week Recovery:** Systems break. When you miss a week, execute a clean reset without guilt or compensatory binge-studying.
7. **Scope Control:** Timebox exploration. Do not let elective curiosity indefinitely stall core dependencies.
8. **Evidence over Feeling:** Trust your test suites, proofs, and peer feedback over the illusion of understanding.
9. **Personal Data Privacy:** Keep private financial, health, identity, and relationship data entirely out of public version control.
10. **Versioning the System:** The repository is versioned. If a process fails consistently, write a [[Decision Record]] to change it. Do not rebuild the system impulsively.

---

## 🎯 Phase -1: Bedrock Foundations
*Rebuilding the operating system of the mind.*

- **Habit 1 — Arithmetic First Principles:** [[BM - Bedrock Mathematics|Bedrock Math]]
- **Habit 2 — Structural Grammar:** [[BW - Bedrock English and Grammar|Bedrock English]]
- **Habit 3 — Cognitive Tooling:** [[B0 - The Deep Learner's Toolkit|Deep Learner's Toolkit]]

### Daily Routines
- **Feynman Technique:** Jargon-free child-level explanation ([[Feynman Technique Note Template|Feynman Template]])
- **Benjamin Franklin Copywork:** Reverse-engineering master prose ([[Franklin Copywork Template|Franklin Template]])
- **Spaced Blank-Sheet Retrieval:** 15-minute zero-hint recall dumps ([[Blank-Sheet Retrieval Template|Blank-Sheet Template]])

---

## 🚦 Automation Telemetry
*Aggregated automatically from your iPhone Shortcuts & Amazon Smart Plug*

```dataview
TABLE 
  filter(rows, (r) => contains(r.Event, "Wake Up"))[0].Time AS "Wake Up Time",
  filter(rows, (r) => contains(r.Event, "Left Work"))[0].Time AS "Left Work At",
  filter(rows, (r) => contains(r.Event, "Arrived Home"))[0].Time AS "Arrived Home At"
FROM "Telemetry Log"
FLATTEN file.lists AS item
WHERE contains(item.text, "TELEMETRY:")
FLATTEN trim(split(item.text, "\|")[1]) AS Time
FLATTEN trim(split(item.text, "\|")[2]) AS Event
GROUP BY trim(replace(split(item.text, "\|")[0], "TELEMETRY:", "")) AS Date
SORT Date DESC
LIMIT 7
```

---

## 📈 The Vault
- 🧠 **Mindset & Habits**: [[how-i-study#A. Mindset and Habits|how-i-study §7A]]
- 📑 **Curriculum** (`01 - Curriculum/`, one folder per stage): [[#The Path|The Path]] · [[Specialization Branches|Specializations Hub]] · [[Employability Portfolio and Review|Employability Portfolio]]
- 🧠 **Learning methods** (deep dive + project each): [[LM00 - Learning Methods Hub|Learning Methods Hub]] · [[Learning Styles Myth]]
- 🔧 **Supporting notes**: [[Engineering Practice]] (tooling, testing, operations) · [[Human Systems]] (money, health, time, relationships)
- 🗂️ **Decisions** (`04 - System/`): [[DR-001 - Program Scope, Phases, and Timeline|DR-001]] · [[DR-002 - Vault Refactor and Canonical Numbering|DR-002]] · [[DR-003 - One Path Restructure|DR-003]] · [[DR-004 - Content Overhaul|DR-004]] · [[DR-005 - Capstone and Maker Thread|DR-005]] · [[DR-006 - Digital Twin, EW Resilience and Fun Prerequisites|DR-006]] · [[DR-007 - Repo Cleanup|DR-007]] · [[DR-008 - Project-First Start and Projects Ladder|DR-008]] · [[DR-009 - Learning Method Deep Dives|DR-009]] · [[DR-010 - KISS Vault Restructure|DR-010]] - Learning Method Deep Dives|DR-009]] · template: [[Decision Record]]
- 📓 **Topic Notes**: [[Hardware Index|Hardware]] · [[Languages Index|Languages]] · [[Math Index|Math]] · [[Systems Index|Systems]] · [[Theory Index|Theory]]
- 📄 **Paper Summaries**: [[Paper Reading Hub|Paper Reading Hub]] (Three-pass method)
- ✍️ **Writing Repository**: [[Writing Hub|Writing Hub]] (Daily 500 words, Franklin copywork & technical essays)
- 🛠️ **Project Specs & Lab Builds**: [[Projects Hub|Projects Hub]] · [[Projects Ladder]] (every build in order, with done-when lines)
- 🌍 **Breadth & Languages**: [[Breadth and Humanities Hub|Breadth Hub]]
- 📚 **Reference & Appendices**: [[Appendix E - Failure Modes|Appendix E (Failure Modes)]] · [[Appendix F - Curated URLs|Appendix F (Curated URLs)]] · [[Your Shelf]] (books) · Cut blocks and the removal list: `99 - Archive/` ([[Removed 2026-10-10 Manifest|what was removed on 2026-10-10]])
