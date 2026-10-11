---
title: "Review — Ultimate Curriculum"
type: reference
tags: [system, review]
---

# Review — Ultimate Curriculum

*Phase 1 of the "best self-taught education" pass: research and review only, no curriculum edits. Inputs: the whole active vault (every course note, the Atlas, `04 - System/`), the external canon (`~/eecs-canon.md`, used as input, not copied), live fetches of the benchmark curricula, and re-fetches of the canon's courses, papers and book contents. Later phases add their results to the end of this note (§8).*

**How to read this note.** §1 traces the capstone back to what teaches it and lists the gaps. §2 compares the curriculum with the best-known programmes. §3 audits the shelf and the canon. §4 and §5 score each course. §6 is the change plan with proposed `order` and `prerequisites`. §7 lists what could not be verified and the questions for Joseph.

**Scores** run from 1 to 5 (5 = excellent). *Integration* means reuse of earlier work, callbacks and later reuse. *Study method* means protocols tied to concrete steps rather than tags. *Usability* means you can always tell where to start, what's next and when you're done.

---

## 1. Gap analysis, working back from the capstone and the canon

### 1.1 The capstone's needs, traced

The capstone ([overview](<../13-capstone/overview.md>), [spec](<../13-capstone/projects/the-whole-stack/spec.md>)) asks every path for: integration of 3+ projects through documented interfaces; end-to-end tests; failure injection; a performance evaluation with statistics; a security review with a threat model; operational docs; a design review; a final report; a recorded talk.

| Need (all paths) | Taught where today | Status |
| :-- | :-- | :-- |
| Interfaces, specs, formats | Pagelet PML, Relay PROTOCOL.md, Crate format spec, Courier RFC-style spec, Stratum on-disk spec | ✔ strong |
| End-to-end and differential testing | 01 Lab 02, 02 Lab 02 (golden, fake clock), Ember and Stratum differential tests, Crate fuzzing | ✔ strong; **no CI** anywhere |
| Failure injection | Relay gremlin, Gremlin 2, Tagfs 500 kills, Stratum 5,000 crashes, 11 Lab 02 torn pages | ✔ strong |
| Performance evaluation with statistics | 12 P3 + Chance Lab (CIs, bootstrap, permutation) | **Thin.** No CI for a *difference between two systems*, no tail-latency (p99) intervals, no run-count/independence guidance; Courier and Lantern report "3 runs, medians". **MOD13 does not even list MOD12 as a prerequisite.** |
| Security review and threat model | RSA toy (03), Crate path traversal + fuzzing, Seedling user-pointer checks, Lantern traversal/slowloris, Courier cookies | **Gap.** All defensive; no adversary model, no threat-modelling method, no exploitation, no access control, no TLS mechanics. Anderson (owned, the canon's primary) is cited nowhere. |
| Operational docs + usability test | E09 (README, instructions, usability test), every project's README | ✔ |
| Design docs and design review | E10, First Design Doc → Copydiff; design notes in 02 | ✔; 02 design notes don't use the template; no Parnas/Ousterhout prompts |
| Code review | — | **Gap** (never taught; `Engineering Practice.md` claims rebase is taught, it isn't) |
| Final report (5–8k words) | E10 report and lab-report forms | ✔, but the lab report is taught in E10 while required from Phase A |
| Recorded talk | E10 Part 5 demo script (5 beats, 4 tips) | **Thin**: no audience analysis, slides, Q&A or rhetoric; E10's only speaking course is a dead Coursera link |

**Path A — Your Own Web** (Glimpse, Courier, Lantern, Stratum, Vault Search, Study Deck)

| Skill | Where | Status |
| :-- | :-- | :-- |
| HTTP over a custom transport | Courier, Lantern, Glimpse | ✔ |
| Search | Vault Search | ✔ |
| Storage + recovery under load | Stratum | ✔; **isolation/concurrency control is stretch-only** (DSCB ch. 18–19 owned, unused) |
| Caching across layers | Cache Sim, Stratum buffer pool, Glimpse HTTP cache | ✔ |
| Concurrency in the server | Lantern's three models, 08 Lab 01 | ✔; no memory model, semaphores, RW locks, event loops in depth |
| Network security (TLS, spoofing) | Lab 01 observes TLS only | **Gap** |

**Path B — Down to the Metal** (Ember → RV64 on Seedling, SeedFS journal, Sprout in Ember, FPGA stretch)

| Skill | Where | Status |
| :-- | :-- | :-- |
| Compiler front end and codegen | Ember (lex, parse, check, interpret, stack-machine codegen, peephole) | ✔; register allocation stretch-only; **no compiler video course**; no IR/linking |
| RISC-V ABI, `ecall`, toolchain, linking | 08 Lab 03, Seedling; 06 targets Kestrel only | **Thin**: no RISC-V codegen practice before the capstone; **no linking step anywhere** (CS:APP ch. 7 uncited, though Heapsmith's `LD_PRELOAD` depends on it) |
| Kernel: traps, Sv39, syscalls, scheduler | Seedling | ✔ but **Lab 03 and Seedling were never run** (DR-010), and a desk check finds likely bugs (stack in `.bss` zeroed by `kmain`; `.sbss/.sdata` missing; implicit `memset/memcpy`; boot hart assumption) |
| Journaled FS + crash tests | Tagfs (logical op-log over host files), Stratum WAL | ✔; no block-level FS (OSTEP 40–42 unexercised); Tagfs has an unlocked multithreaded FUSE hazard |
| FPGA (stretch) | Stretch lines only in Gatesmith/Datapath | **Gap**: no HDL, board, constraints, clocking or UART — Path B's stretch stands on an untaught stretch |

**Path C — Field Station** (Pico W sensors, flash journal, Courier-lite over Wi-Fi, Stratum, Lantern, Glimpse, Chance Lab, field run)

| Skill | Where | Status |
| :-- | :-- | :-- |
| Sensors and calibration | Pico Thermostat (TMP36, ADC noise, averaging) | ✔ analog only; no I²C/SPI |
| FSMs | Crosswalk | ✔ |
| Flash logging that survives power cuts | — | **Gap** (Lab 04 logs over USB serial only) |
| Wi-Fi, reconnect | Thermostat stretch only; **the shopping list buys a Pico H (no Wi-Fi)** | **Gap** |
| Wireless physical layer, noise, framing | — (Kurose ch. 7 owned, unused) | **Gap** |
| Clock sync and drift | `ticks_ms` wrap only | **Gap** (no NTP-style offset estimation, no Lamport) |
| Power, batteries, bench safety | 04 safety covers low voltage, fuses, polarity; **no soldering, flux, Li-ion, ESD** (the canon wrongly says it exists) | **Gap** |
| Analog front end, filtering | Lab 01 Fourier by Ear analyses a moving average only | **Gap**: no filter *design*, no op-amps |
| The physics of the sensors | — | **Gap** |

### 1.2 The specific checks

| Check | Verdict (from the files) |
| :-- | :-- |
| Security and threat modelling | **Confirmed gap.** See 1.1. Anderson, OSTEP 53–57, Kurose ch. 8, CS:APP §3.10 are all owned and unused. |
| Software-engineering practice | Testing ✔✔. Git ✔ (no rebase, no remotes/PR flow). **Code review and CI: gap.** Design docs ✔. |
| Concurrency and distributed systems | Concurrency ✔ basics (08 Lab 01, Lantern, Seedling); missing memory models, semaphores/RW locks, CSP. **Distributed systems: confirmed gap** (no replication, logical clocks, consensus, clock sync). |
| Compilers (Ember) | Strong project; **no video course** (confirmed: `06/overview.md` says so); codegen gap-fill should be Wirth (register-machine), not *Crafting Interpreters* Part III (bytecode VM). Ball (owned) unused for the front end. |
| Embedded, wireless, clock sync (Path C) | **Confirmed gaps** (see Path C). |
| FPGA (Path B stretch) | **Confirmed gap.** |
| Statistics for performance evaluation | **Partly confirmed.** Chance Lab has CIs and resampling but not two-system comparisons or tail latency; nothing downstream requires it. |
| Technical writing and presenting | Writing ✔✔ (best in class). Presenting **thin**; dead E10 link confirmed (`E10:209`, plain text, no URL). Lab report taught too late. |
| Physics for engineers | **Confirmed gap.** No physics anywhere; 04 assumes almost none (charge and "energy per charge" get one sentence each). Math Index line 28 and DR-010 line 52 exclude it. |
| Multivariable calculus and analytic ODEs | **Confirmed gap.** No partial derivatives, gradients, div/curl; C3 is numerics only (the RC solution is *given*, never derived). No optimisation at all. |
| Circuit analysis and signals | **Confirmed gap.** 04 covers about 3 of 10 6.002-level topics (no KVL/KCL by name, nodal, Thevenin, RLC, MOSFET, op-amps, phasors). Signals stop at DFT/FFT; no LTI framing, Laplace, z, filter design. |
| Rhetoric and great reading | **Confirmed gap.** E10 has claim–reason–evidence, no ethos/pathos/logos, no Aristotle, Heinrichs or *They Say / I Say* (only in the Writing Hub). No great-reading list anywhere. |
| "No chemistry course" | **Confirmed in substance, with a correction.** No module or path needs a chemistry *course*. But the canon's supporting claim is half wrong: MIT *does* require chemistry of every undergraduate (GIR: one of 3.091 / 5.111 / 5.112; the 6-3 department adds nothing). Berkeley EECS and CMU make it one science option among several. And the canon's other support (bench chemical safety "already in 04") is false. See §6.1 (A9) for the call. |

### 1.3 Gaps the canon did not name (found in the files)

1. **Theory of computation** (automata, computability, intractability): absent; required at CMU (15-251), one-of-two at MIT. HMU (owned) is unused. The capstone doesn't need it, but Module 10's tokenizer and Truth Engine's SAT both lean on it.
2. **Functional abstraction** (higher-order functions, closures, SICP-style): absent; core at CMU, Berkeley, OSSU, TYCS.
3. **Undefined checkpoints.** `MOD03-U1…U8` and `MOD12-C1…S1` are table rows with no pass rule, yet five modules list them as prerequisites.
4. **Ordering bugs** that make Start Here (which follows `order`) contradict module sequences: 06 (labs before Kestrel ISA, though Lab 03 needs ISA, Datapath and Ember output), 08 (labs before Arena/Tagfs), 12 (Lab 01 before Motion Lab), 03 (Proof Journal at the end, though it starts in Lab 01), foundations (stage "Done when" lists require projects ordered after them; both track assessments are circular).
5. **Unmet objectives**: 05 promises BSTs and topological sort (never built); 12 promises "design a simple filter" (only analyses one).

---

## 2. Benchmark against the best

Fetched 2026-10-10: OSSU README, teachyourselfcs.com, MIT 6-3 degree chart + GIR page, Berkeley EECS lower/upper-division pages, CMU BS-CS catalog, Nand2Tetris course page.

| Topic | Vault | OSSU | TYCS | MIT 6-3 | Berkeley EECS | CMU | N2T |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Intro programming | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | — |
| Functional/SICP abstraction | — | ✔ | ✔ | partial | ✔ | ✔ | — |
| Data structures, algorithms | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | — |
| Theory of computation | — | partial | — | partial | partial | ✔ | — |
| Discrete math | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | — |
| Calculus, single | partial (numerical) | ✔ | — | ✔ GIR | ✔ | ✔ | — |
| Calculus, multivariable | — | — | — | ✔ GIR | ✔ | ✔ | — |
| Linear algebra | ✔ | partial | partial | option | ✔ | ✔ | — |
| Probability/statistics | ✔ | partial | partial | option | ✔ | ✔ | — |
| Differential equations | partial | — | — | — | ✔ | — | — |
| Physics (mechanics, E&M) | — | — | — | ✔ GIR | ✔ | option | — |
| Chemistry | — | — | — | ✔ GIR | option | option | — |
| Circuits | partial | — | — | partial | ✔ (16A/B) | — | — |
| Signals and systems | partial | — | — | — | partial | — | — |
| Digital logic, architecture | ✔ (real hardware) | ✔ | ✔ | ✔ | ✔ | partial | ✔ |
| Compilers | ✔ (Ember) | ✔ | ✔ | elective | elective | elective | ✔ |
| Systems programming, OS | ✔✔ (own kernel) | ✔ | ✔ | ✔ | elective | ✔ | partial |
| Networking, databases | ✔✔ (own transport, engine) | ✔ | ✔ | partial | elective | elective | — |
| Distributed systems | — | — | ✔ | partial | elective | elective | — |
| Security | partial | ✔ | — | partial | elective | elective | — |
| Software engineering | ✔ (solo) | ✔ | — | ✔ 6.1020 | partial | partial | — |
| Writing/communication | ✔✔ | — | — | ✔ CI-H/CI-M | ✔ | ✔ | — |
| Humanities | optional | partial | — | ✔ 8 HASS | ✔ | ✔ | — |

**What they teach that this lacks** (ranked by how many require it): theory of computation; multivariable calculus; physics; functional abstraction; distributed systems; security; humanities; parallel algorithms (CMU 15-210); signals/AC circuits (Berkeley 16A/B); team-scale software construction (MIT 6.1020). ML/AI appears as an elective everywhere; it is out of scope here (archived v1 track; would need its own DR).

**What it repeats.** The spirals are deliberate (DR-010): Nib → Kestrel, Burrow Jr. → Burrow → Sprout (→ capstone B shell), Relay → Courier, Pagelet → Glimpse. Keep them, but each later spec should *say* it is the full-size version and call back the earlier artifact. Real overlaps to trim: 06's alternate video is the same Ben Eater playlist as 04's primary; Start Here "Section 1" and `first-sections.md` both define the first sessions; probability expectation appears in 03 U8 and 12 P2 (small; turn P2's into a callback).

**What it does better.** Writing taught from spelling up; real hardware (breadboards, 555, Pico, feedback control); building whole systems (own transport with congestion control, browser engine, database with WAL/ARIES-style recovery, RISC-V kernel); an integration capstone over your own artifacts; measurement-first labs; learning science built in; numerical, computing-tied math (RK4, SVD/PageRank, bootstrap, FFT).

**MIT 6-3 facts (verified on catalog.mit.edu):** 8.01, 8.02, 18.01, 18.02, chemistry and biology are Institute-wide GIRs; 18.06 is one of five math options; **18.03 is not required** for 6-3 (Berkeley EECS does require a linear-algebra-and-ODE course, Math 54). Physics and multivariable calculus are therefore the strongest benchmark-backed additions; analytic ODEs are justified by the EE course, not by MIT's chart.

---

## 3. Shelf and canon audit

### 3.1 The §0 map against the courses

**Bottom line:** 13 of the 20 owned books are cited nowhere; most of the other seven appear only in a `resources.md` list, not in a lab step. Every owned book has a confirmed home. Shelf-first is violated in 01, 04, 05, 06, 07 (steps), 08 (steps), 09, 10, 11 and 12: each cites unowned or free texts where an owned book covers the need.

**Corrections to the map** (from the course files and from re-fetched tables of contents):

| Map row | Correction |
| :-- | :-- |
| 01 Relay | Add Kurose ch. 3 §3.4 (reliable data transfer, stop-and-wait) — fits Relay M4 exactly. |
| 03 U2–U5 | The module calls MCS "the main text"; make Velleman primary for U1–U5 (map is right; the course is wrong). BoP fallback for U5 is wrong: BoP ch. 7 is "Proving Non-Conditional Statements"; congruence is ch. 5 §5.2 and ch. 11. |
| 03 U8 / 12 P1 | AIMA ch. 12 "Quantifying Uncertainty" is *discrete* (joint distributions, independence, Bayes), not "continuous-heavy". Still partial. |
| 04 Gates/Gatesmith | Split: full for Lab 03, **partial for Gatesmith** (event-driven timing, carry-lookahead are beyond Justice; Harris & Harris ch. 5). |
| 04 FSMs | HMU ch. 2 covers acceptors, not Moore/Mealy controllers: keep it as a [W] "formal view" only; Harris & Harris §3.4 is the real gap-fill. |
| 04 missing rows | Add **bench safety** (none), **embedded storage and Wi-Fi** (none), **transistor switching** (Justice ch. 4, partial). |
| 05 Sorting | Partial, not none: Zingaro ch. 8 (heaps/heapsort), ch. 10 (randomization). |
| 05 Trees | Partial: Zingaro ch. 2 has no BSTs or balancing. |
| 05 DP | Full for DP; partial for LCS/edit distance (Erickson). |
| 06 Datapath | **Partial**, not full: CS:APP has SEQ and PIPE but no multi-cycle FSM control (Harris & Harris §7.4). |
| 06 Ember | CS:APP ch. 7 fits Path B and 07, not Ember (Ember has no linker). Codegen gap-fill → Wirth, not Crafting Interpreters Part III. |
| 06 missing row | **FPGA/HDL** (none) → Harris & Harris ch. 4. |
| 07 toolchain | **Ward ch. 15 is "Development Tools"** (gcc, linking, make); cite it, with ch. 16 secondary. Add CS:APP §7.13 (interpositioning) for Heapsmith M7. |
| 07 allocator | Cite CS:APP §9.9 "Dynamic Memory Allocation" and K&R §8.7 "A Storage Allocator". |
| 08 file systems | Full on paper, **partial in practice**: no item exercises OSTEP 40–42. |
| 09 Lantern | Add CS:APP ch. 12 "Concurrent Programming" (thread-per-connection, prethreaded pool, I/O multiplexing = Lantern's three models). |
| 11 Lab 01 | Ch. 2, 3 (design theory), 5 (relational algebra), 6 (SQL), 8 (views and indexes). |
| 11 recovery/concurrency | Ch. 17 is full; **ch. 18–19 "full" is wrong in practice** — the course makes concurrency a stretch. |
| Security rows | OSTEP security is **ch. 53–57** (incl. 56 Cryptography, 57 Distributed system security), not 53–55. Anderson 2e numbering differs from 3e; since every 3e chapter is free on the author's site, read 3e whatever you own. |
| Capstone distributed row | **OSTEP ch. 48 has nothing on clocks or consensus** (communication/RPC only) — weak. DSCB ch. 20 carries more. |
| Ellenberg | Ch. 2 "I Vote for Euclid"; **ch. 8 "Artificial Intelligence as Mountaineering"** (not "AI as…"). |
| Strogatz | Numbers confirmed; add ch. 16 "Take It to the Limit" for 12 C1. |
| Extra fits found | OSTEP ch. 17 Free-Space Management (Heapsmith); HMU ch. 3 Regular Expressions (10 tokenizer); *Algorithms to Live By* ch. 4 Caching (07 Lab 04), ch. 5 Scheduling (Arena), ch. 10 Networking (09 backoff); Oakley ch. 7–8; Kurose ch. 5 (routing) for 09 Lab 03. |

### 3.2 Every owned book's home

| Book | Home(s) after this pass |
| :-- | :-- |
| Lockhart, *Arithmetic* | M01–M07 per stage by chapter title |
| Oakley, *A Mind for Numbers* | first-sections, E01 Part 3, the D/R/I protocol rows, self-checks (ch. 2, 4, 5–6, 9, 10–11, 16–17) |
| Velleman, *How to Prove It* | 03 U1–U5 primary (ch. 1–7 incl. §7.5) — **edition to confirm** |
| Courant & Robbins | 12 C1–C5 second pass (ch. VI–VIII), C4 optimisation (ch. VII); Breadth |
| Strogatz, *The Joy of x* | M07–M11 motivation reads; 12 (ch. 16–18, 20–24); 14 opener (ch. 21) |
| Ellenberg, *Shape* | M10 (ch. 2); 12 C4 gradient descent (ch. 8); Breadth |
| K&R 2e | 07 Lab 01 per session (ch. 1–7), Lab 03 (ch. 8), Heapsmith (§8.7) |
| Zingaro 2e | 05 throughout (App. A, ch. 1–10); 02 Lab 01 (ch. 2) |
| CS:APP 3e | 06 (ch. 2–4, 6), 07 (ch. 3.10, 7–10), 08 Lab 01 (ch. 12), 09 Lantern (ch. 11–12), 07 security lab |
| Ball, *Writing an Interpreter in Go* | 02 Worldfile (ch. 1–2), 06 Ember M1–M3, 10 Glimpse CSS parser |
| HMU, *Automata Theory* | **03 new U9** (ch. 2–3, 8–10), 04 Crosswalk [W], 10 Lab 01 |
| Justice, *How Computers Really Work* | 01 primary (ch. 1, 2, 7, 8, 10–12), 04 Labs (ch. 3–6), 06 Kestrel ISA (ch. 7–8) |
| Christian & Griffiths, *Algorithms to Live By* | 05 Lab 02 (ch. 3), 07 Lab 04 (ch. 4), 08 Arena (ch. 5), 09 Courier (ch. 10), 12 P3 (ch. 6–7), Breadth |
| OSTEP | 08 per lab by chapter number; security labs (53–57); 07 Heapsmith (ch. 17) |
| Russell & Norvig, AIMA 4e | 03 Truth Engine M5 (§7.6), 05 Route Planner M4 (§3.5.2), 12 P1 (ch. 12), Breadth (ch. 27) |
| Garcia-Molina, Ullman & Widom, DSCB 2e | 11 primary (ch. 2–3, 5–6, 8, 13–20) |
| Kurose & Ross | 01 Relay/Pagelet (ch. 1–3), 09 (ch. 1–8), 15 comms lab (ch. 7), security labs (ch. 8) |
| Anderson, *Security Engineering* 3e | 07/08/09 security labs, capstone review (ch. 2, 4–6, 21, 27–28) |
| Ward, *How Linux Works* 3e | 01 Lab 00/Burrow Jr. (ch. 1, 2, 8), 07 (ch. 8, 11, 15), 08 Lab 03 (ch. 5), Tagfs (ch. 4), 09 Lab 03 (ch. 9–10) |
| Feynman, *Six Easy Pieces* | 14 opener and units (ch. 1, 2, 4, 5, 6); bench-chemistry unit (ch. 1) |

**No owned book stays unused.**

### 3.3 Canon Core items: adopt, swap or reject

"Verified" means the URL and contents were re-fetched on 2026-10-10 (details in §3.5).

| Canon Core item | Decision | Exact home | Replaces |
| :-- | :-- | :-- | :-- |
| MCS + 6.042J | **Adopt** (gap-fill, already in) | 03 U3 invariants, U6–U8 | — (demoted from "main text" for U1–U5) |
| Hammack, *Book of Proof* | **Adopt** as Velleman's parallel (answers to odd exercises) | 03 U1–U6 practice; U6 primary | — |
| OpenStax *Calculus* + 18.01SC | **Adopt** (override of Courant: level) | 12 C1–C3 reading spine + unit-check problems | — |
| MIT 18.02SC | **Adopt** | 12 new C4 | — |
| MIT 18.03SC | **Adopt** | 12 new C5 | — |
| Strang + 18.06SC | **Adopt the course**; book → Reference (paid, not owned) | 12 L1–L4 | — |
| VMLS (Boyd & Vandenberghe) | **Adopt** | 12 L3, Matrix Studio M2 | Strang book as L3 text |
| Blitzstein & Hwang + Stat 110 | **Adopt** | 12 P1–P3, Chance Lab | Grinstead & Snell as primary (→ Reference) |
| *Composing Programs* (SICP in Python) | **Adopt** | 02 Lab 01 (ch. 1), Lab 03 (ch. 2), new Lab 04 (§1.6 higher-order functions, §2.3–2.4) | — |
| Ousterhout (acquire) | **Adopt**; Parnas 1972 carries the idea until bought | 02 design notes, 13 design review | — |
| Missing Semester | **Adopt** (in) | 02 Lab 02 | — |
| Erickson + MIT 6.006 | **Adopt** for analysis, sorting, lists, BSTs | 05 Labs 01–03; 6.006 becomes **primary video** | NeetCode Pro as primary (→ alternate + problem source) |
| Skiena | **Reject as Core** → Reference (Zingaro covers the problem chapters) | 05 resources | — |
| *Crafting Interpreters* | **Swap**: Reference only | 06 resources | codegen gap-fill → Wirth *Compiler Construction* (register-machine codegen) |
| Nand2Tetris 2e (acquire) | **Reject as Core** (Kestrel replaces Hack by DR-010's originality rule); keep as alternate reading | 04 Gatesmith M1–M4, 06 Kestrel (resources) | — |
| CS:APP + 15-213 | **Adopt** (owned) | 06–09 steps (§3.2) | — |
| Harris & Harris (RISC-V) | **Adopt** as gap-fill (acquire) | 04 Gatesmith/Crosswalk, 06 Datapath multi-cycle, FPGA milestone (ch. 4) | — |
| OSTEP + xv6/6.1810 | **Adopt** (owned) | 08 steps by chapter | — |
| Kurose & Ross | **Adopt** (owned) | 01, 09, 15, security | — |
| Kleppmann (acquire) + 6.5840 | **Adopt** | 11 new Lab 03 (ch. 5, 8, 9), capstone | — |
| Red Book | **Reject** (only if shelf lacks; DSCB owned) | — | — |
| MIT 6.858 | **Adopt lectures only** as the security labs' video; our labs stay original | 07/08/09 security labs | — |
| Anderson 3e | **Adopt** (owned; read free 3e chapters) | security labs, capstone | — |
| *Learning the Art of Electronics* | **Adopt** (paid gap-fill) | 04 Labs 01–02, 15 bench labs | — |
| MIT 6.002 | **Adopt** | 15 Part 1 primary video | — |
| MIT RES.6-007 | **Adopt** | 15 Part 2 primary video | — |
| Smith, *DSP Guide* | **Adopt** (in) | 12 S1 (add ch. 3, 5, 6, 19), 15 Part 2 | — |
| MIT 6.02 | **Adopt notes as reading** | 15 Lab 05 (bits over sound), Path C | — |
| OpenStax *University Physics* 1–2 | **Adopt** | 14 reading spine | — |
| MIT 8.01SC / 8.02 / 8.03SC | **Adopt** | 14 primary video series | — |
| *Feynman Lectures* I–II | **Adopt** for [F] passes | 14 units | — |
| Williams & Bizup (acquire) | **Adopt** | E08 (named lessons), lab-report checklist, 13 report | — |
| Pinker (acquire) | **Adopt** | E08 (ch. 3, 5), E10 | — |
| Orwell essay | **Adopt** | E08 copywork + clarity rewrites | — |
| Sainani + Google TW One/Two | **Adopt** (in); re-flag Coursera's preview-only status | E08–E10 | — |
| Winston, *How to Speak* | **Adopt** | E10/E11, capstone talk | the dead "Successful Presentation" link |
| Heinrichs, *Thank You for Arguing* | **Adopt** (acquire) | E11 | — |
| *They Say / I Say* | **Adopt** (acquire) | E10 Part 1 (naysayer moves), E11 | — |
| Aristotle, *Rhetoric* Bk I | **Adopt** (free) | E11 | — |
| Core papers (§9 rungs 0–4, 6–9, 11, 13–15, 17–22, 25, 27) | **Adopt**, each at one step (§6.3) | see §6.3 | — |

**Reference** goes to the owning course's `resources.md` (Axler, Concrete Mathematics, Spivak, Pólya, Kleinberg & Tardos, CLRS, Sipser + 18.404J, Dragon book, H&P, 6.033, Horowitz & Hill, Oppenheim & Willsky, Åström & Murray, Berkeley 16A/B, Purcell & Morin, Yale PHYS 200/201 (as 14's alternate video), OpenStax Chemistry 2e, Zinsser, Huddleston & Pullum, Booth/Zobel, HarvardX Rhetoric). Books to buy go on Your Shelf's acquire list only if a course step uses them (Williams, Pinker, Heinrichs, Graff & Birkenstein, Ousterhout, Kleppmann, Harris & Harris, LAoE, CLRS as reference).

**Enrichment** → Breadth and Humanities Hub (18.100A, Barak, TAOCP, Theoretical Minimum, 8.04/Feynman III, 3.091, 5.111SC, 7.01SC, MacKay, 6.004/6.012/6.013/EE261, Cryptopals/pwn.college/6.172, Strunk, Hamming talk and book, Cargo Cult Science, Euclid I, Plato *Apology*, Kidder, Brooks MMM, Petzold, GEB) or the Paper Reading Hub (Turing, EDVAC, McCarthy, Hoare CSP, GFS, MapReduce, Nakamoto, Backus, Attention).

### 3.4 Owned books with no course

None after this pass (see §3.2). Edition questions remain for Velleman (3rd needed for §7.5), Anderson (read free 3e), Kurose (8e assumed) — see §7.

### 3.5 Verification of canon items

**Papers (§9):** 29 of 30 rows load and are the right paper. Cooley–Tukey's AMS page is Cloudflare-blocked to scripts (DOI confirmed via Crossref; working mirror at ucdavis.edu). Lampson's site refuses short user agents but loads in a browser. Patterson & Ditzel: DOI 10.1145/641914.641917 + utexas mirror. The ACM Digital Library has been open access since January 2026, so Parnas, both Hoare papers, Trusting Trust, Codd and Backus have publisher DOIs (verified via Crossref; the PDFs themselves are blocked to scripts — **unverified as downloads**). Rung 3's URL is the 1978 BSTJ revision of the UNIX paper, not the 1974 CACM original. Gutenberg's Strunk is the 1920 printing.

**Courses and books:** *(added when the course-verification pass finishes — see below)*

---

## 4. Integration audit (scores 1–5)

| Course | Integration | Study method | Evidence and main weakness |
| :-- | :-: | :-: | :-- |
| English E01–E10 | 4 | 4 | Spelling Engine → Study Deck; First Design Doc → Copydiff. No cross-stage review sets (the overview claims them); flashcards not routed to Study Deck; no per-stage V prompt. |
| Math M01–M11 | 4 | 4 | Concrete R/W/F per stage; error logs. Same Study Deck and V gaps. |
| 01 Intro CS | 4 | 4 | Feynman/why-ladder per milestone, subgoal comments verbatim. Flashcards "3–5 per session" with no format or destination. |
| 02 Programming | 5 | 4 | Lab 01 adventure → Worldfile; parse/render callbacks. Labs 02–03 have no card step; C only in Worldfile. |
| 03 Discrete | 5 | 4 | Reuses Prime Factory, Worldfile parser, Study Deck replay proof. Cards point at a Study Deck that may not exist yet. |
| 04 Circuits | 5 | 4 | Truth Engine, Nib flags, Tone Loom on the buzzer, fake clock. No C; cards not routed; no earlier-module review. |
| 05 DSA | 4 | 4 | `bench.py`, MinHeap, Levenshtein reused. [I] is a tag; problems unnamed; C only in Copydiff. |
| 06 Architecture | 4 | 4 | Two-implementations-per-arrow diagram is a standout. Order bug breaks the chain; Gatesmith → Digital reuse is only a stretch. |
| 07 Systems | 5 | 4 | Strongest module: ports from 05, feeds 08. Labs 02–04 have no cards; C only in the overview table. |
| 08 OS | 4 | 3 | Heapsmith → kmalloc, Burrow → Sprout. Labs have no cards (Lab 03's "[I]" mis-tag), no C, no lab deliverable. |
| 09 Networking | 5 | 4 | Relay → Courier, Crate fuzzing everywhere. No C (RFCs are ideal copywork), no T beyond demos. |
| 10 Browser | 4 | 4 | Only module with copywork from specs. No Module 12 reuse (Matrix Studio transforms for zoom). |
| 11 Databases | 5 | 4 | Queries your own Study Deck/journal data; Tagfs journal → WAL. No Chance Lab reuse; cards overview-only. |
| 12 Math for Eng. | 4 | **2** | Strong back-reuse (Tone Loom, Thermostat, Study Deck, Courier). Units are tags only: no worked examples, problems, Feynman targets or checks. Nothing downstream requires it. |
| 13 Capstone | 5 | 4 | Integration is its purpose. Security/statistics/talk rest on thin foundations. |

**Cross-cutting.** (1) **Study Deck has no card conventions** (deck path, file per module, `@tags modNN`, `@id modNN-…`), so "add cards" in later modules has no destination; the Blank-Sheet template's §3 uses `**Q:**`, which `deck` won't parse; there is no migration from paper/Anki. (2) **[V] lives only in resources maps**, never at a lab step. (3) **[C] copywork is absent from 04, 06 (except one step), 08, 09, 11, 12.** (4) **[I] interleaving is a tag**, never a named problem set spanning modules. (5) **Method texts contradict each other** (from the Atlas audit): LM02 calls R the warm-up and builds a countdown timer the protocol forbids; LM06 says "a few days" (DR-011 says "a later session"); two Feynman audiences (12-year-old vs smart friend) and two jargon rules; the Paper Hub's pass 2 includes proofs and its pass lengths disagree with LM13 and Keshav; two card counts per miss (1–3 vs one); `how-i-study` points to LM09 for intervals that live only in `study-protocols`; intervals are 1-3-7-21 in some notes and 1-3-7-21-60 in others; `study-protocols` cites the wrong `how-i-study` items for T; no DR records protocol V.

## 5. Usability audit

| Course | Usability | Where you get stuck |
| :-- | :-: | :-- |
| English | 3 | Stage/project deadlock in `order`; circular assessment; "stop at first fail" placement can't skip later parts; E09/E10 can't be placed out of; lab report required before taught. |
| Math | 3 | Same deadlock; no whole-track placement; most diagnostics have no skip rule. |
| 01 | 4 | Prereq text mentions E02/M03/M07 not in frontmatter; 3-vs-4 projects for MOD01-CLOSE. |
| 02 | 4 | "Pólya" claimed, absent; M05 vs M07 for Tone Loom. |
| 03 | 3 | Unit checks undefined; which text to open per unit unclear; Proof Journal order; hidden Worldfile and Growth Lab dependencies. |
| 04 | 4 | E10-level deliverables before E10; Thermostat missing Crosswalk prereq; duplicate Done-when; Pico H vs W. |
| 05 | 4 | Objectives promise BSTs/topo sort; project specs lack Next links. |
| 06 | 3 | `order` contradicts the sequence; Lab 02/03 depend on later projects; Cache Sim silently needs Ember. |
| 07 | 3 | No Next links on Labs 02–04; "Lab 04 any time" vs the chain; lab bug count wrong; no linking item. |
| 08 | 3 | `order` vs sequence; no Next links; unverified Lab 03 with likely bugs; Seedling has no warning. |
| 09 | 4 | Some milestones lack "Done when"; Lab 03 promises a three-host network it never builds. |
| 10 | 4 | Glimpse M4–M5, M8 lack "Done when"; Lab 02 points to references that don't exist. |
| 11 | 4 | Many milestones lack "Done when". |
| 12 | **2** | You can't tell what "pass C1" means, what to read, or which problems to do; Lab 01 order vs suggested order. |
| 13 | 4 | Clear, but its prereqs omit MOD12 although it requires Chance Lab statistics. |

Start Here's checklist is hand-written; it claims to follow `order` and lacks `MOD02-CLOSE`/`MOD03-CLOSE` lines. Root notes point to DR-011 as "latest" (DR-012 exists).

---

## 6. Prioritized change plan

### 6.1 Additions (with place in the sequence)

**Ordering approach.** `order` is the one recommended sequence; "alongside" tracks (as Module 12 already is) take their position where their prerequisites are met. New items take free values in existing gaps. Whole new courses don't fit a 10-gap anywhere before the capstone, so **one block move**: the capstone's three items go from 1370/1380/1390 to 1700/1710/1720 (their ids never change); the freed range 1370–1690 takes the new science courses. All renumbering (this move and the bug fixes in §6.2) is recorded in DR-013.

| # | Addition | New ids → `order` | `prerequisites` | Why (evidence) |
| :-- | :-- | :-- | :-- | :-- |
| A1 | **Module 12 expansion: C4 multivariable and vector calculus; C5 linear ODEs, Laplace, Fourier series**; define every unit check C1–C5, L1–L4, P1–P3, S1 with a Read column, named problems, R/F/W prompts and cards; extend S1 to filter *design* and LTI/convolution; optimisation in C1 and C4. New labs: **Lab 02 Field Explorer** (C4: gradients, gradient descent on Matrix Studio's least squares, numerical flux = divergence, Lagrange check; Ellenberg ch. 8; Courant VII) and **Lab 03 Springs, Circuits and Laplace** (C5: derive RC/RLC/spring solutions, damping, resonance, transfer functions; checks against Motion Lab's RK4 and 04 Lab 02 data). Fix Lab 01 → 885. | checkpoints `MOD12-C4`, `MOD12-C5`; `MOD12-LAB02` → 1370, `MOD12-LAB03` → 1380 | LAB02: [MOD12-C4, MOD12-PRJ-matrix-studio]; LAB03: [MOD12-C5, MOD12-PRJ-motion-lab, MOD04-LAB02] | §1.2; 18.02SC/18.03SC; E&M and circuits need them; benchmark |
| A2 | **New course 14 — Physics for Engineers** (`14-physics-for-engineers/`, phase D). Labs: 01 Measuring motion (phone sensors via phyphox, uncertainty; SEP ch. 1–2), 02 Forces, energy, momentum (SEP ch. 4), 03 Gravity and orbits (SEP ch. 5), 04 Oscillations and waves (with Tone Loom; 8.03SC), 05 Charge, field, potential, 06 Current, magnetism, induction (coil + magnet drop on the Pico ADC), 07 Atoms, semiconductors and batteries (the chemistry call, A9; SEP ch. 1, 6). Projects: **Orbit Sandbox** (2D physics engine reusing Motion Lab's integrators; energy/momentum conservation tests; reused by the capstone's evaluation habits) and **Field Probe** (Pico W magnetometer/Hall + coil current sensing with a calibrated sensor library and uncertainty budget → Path C sensors). Primary video: MIT 8.01SC → 8.02 → 8.03SC series; alternate: Yale PHYS 200/201. | `MOD14` 1400; LAB01–07 1410–1470; `MOD14-PRJ-orbit-sandbox` 1480 (after LAB04 by prereq, placed after labs); `MOD14-PRJ-field-probe` 1490; `MOD14-RES` 1495 | MOD14: [MOD12-C1, MOD12-C2, MOD12-C3, MOD04, M10]; LAB05: [MOD12-C4]; LAB04: [MOD12-C5]; Orbit Sandbox: [MOD14-LAB03, MOD12-PRJ-motion-lab]; Field Probe: [MOD14-LAB06, MOD04-PRJ-pico-thermostat] | §1.2; MIT/Berkeley require it; Path C sensors |
| A3 | **New course 15 — Circuits and Signals** (`15-circuits-and-signals/`, phase D). Part 1 Circuits: Lab 01 Nodal analysis and Thevenin (KCL/KVL matrices solved with Matrix Studio), Lab 02 First- and second-order circuits (RC/RLC on the bench vs Laplace), Lab 03 MOSFETs and op-amps. Part 2 Signals: Lab 04 LTI systems and convolution (impulse and frequency response, Bode), Lab 05 Sampling, filters and bits over sound (FIR/IIR design; FSK modem with noise and bit-error rate; 6.02 notes; Kurose ch. 7). Projects: **Spice Jr.** (modified-nodal-analysis simulator: DC, transient, AC sweep; validated against bench and ngspice; reuses Matrix Studio's solver and Motion Lab's integrators) and **Sensor Front End** (op-amp gain + anti-alias filter + digital filter on the Pico for Field Probe's sensor, with a noise budget → Path C). Primary video: 6.002 (Part 1) and RES.6-007 (Part 2); alternates per part. | `MOD15` 1500; LAB01–05 1510–1550; `MOD15-PRJ-spice-jr` 1560; `MOD15-PRJ-sensor-front-end` 1570; `MOD15-RES` 1580 | MOD15: [MOD14-LAB06, MOD12-C5, MOD12-S1, MOD12-L3, MOD04]; Spice Jr.: [MOD15-LAB02]; Sensor Front End: [MOD15-LAB05, MOD14-PRJ-field-probe] | §1.2; 04 audit (new course, not extension); Paths B/C |
| A4 | **Security thread.** **07 Lab 05 Memory-safety attacks** (stack smash on your own vulnerable program with protections off, then on one at a time; CS:APP §3.10.3–4; Trusting Trust). **08 Lab 04 Isolation and threat models** (Anderson ch. 2 threat-model method; uid/gid, mode bits, setuid, capabilities, a seccomp filter; OSTEP 53–55; threat model of Seedling's syscall boundary). **09 Lab 04 Attack and defend your network** (in namespaces on your own machine: ARP spoofing, DNS poisoning race against your Lab 02 resolver, HELLO flood vs Courier cookies, TLS handshake and a rejected MITM; Kurose ch. 8, Anderson ch. 21, OSTEP 56–57). Threat-model write-ups added to Crate M6 and Seedling M6. Capstone security requirement cites them. | `MOD07-LAB05` 1065; `MOD08-LAB04` 1145; `MOD09-LAB04` 1225 | [MOD07-LAB03]; [MOD08-LAB02, MOD08-PRJ-seedling-kernel]; [MOD09-PRJ-courier, MOD09-PRJ-lantern] | §1.1; canon §10 |
| A5 | **Distributed systems and clocks.** **11 Lab 03 Replicas and clocks**: WAL shipping to a follower, failover, a split-brain demo, Lamport clocks on log records, NTP-style four-timestamp offset estimation over netem (Lamport 1978; DSCB ch. 20; Kleppmann ch. 5, 8, 9; Raft §5 as the capstone pre-read; 6.5840 lectures). Also: make basic isolation (2PL) a core Stratum milestone (DSCB ch. 18–19). | `MOD11-LAB03` 1355 | [MOD11-PRJ-stratum-query-and-recovery, MOD09-LAB03] | §1.1–1.2 |
| A6 | **Theory of computation.** 03 **U9 Machines and limits** (DFA/NFA/regex, Turing machines, the halting problem, P vs NP via reductions to your Truth Engine's SAT; HMU ch. 2–3, 8–10) + **03 Lab 03 Automata workshop** (regex → NFA → DFA matcher; feeds Glimpse's tokenizer). | checkpoint `MOD03-U9`; `MOD03-LAB03` 555 | [MOD03-U1, MOD03-U4, MOD03-PRJ-truth-engine] | benchmark; owned HMU |
| A7 | **Functional abstraction.** **02 Lab 04 Functions as values** (higher-order functions, closures, lambda, generators/lazy streams, a tiny evaluator; *Composing Programs* §1.6, §2.3–2.4; Dijkstra's GOTO letter as a contrast). | `MOD02-LAB04` 455 | [MOD02-LAB03] | benchmark; canon Core |
| A8 | **English E11 — Rhetoric and speaking** (`00-foundations/english/E11-…`): the appeals (Aristotle Bk I, Heinrichs), entering an argument (*They Say / I Say*), Winston's *How to Speak*, slides and Q&A, a recorded "defend your design" talk; plus a **great-reading list** in the Breadth Hub (shelf first). Also: move the lab-report form from E10 to E08; Orwell into E08; Winston replaces the dead E10 link. | `E11` 715 | [E10] | canon §8; §1.2 |
| A9 | **Chemistry call: no course; one bench unit.** Lab 07 of course 14 ("Atoms, semiconductors and batteries"): bonding → band picture → why a diode conducts (measure an I–V curve); Li-ion electrochemistry, charging and failure; solder, flux and lead safety. OpenStax *Chemistry 2e* chapters as reference; MIT 3.091 as enrichment. **Plus a real bench-safety section in 04.** | part of A2 | — | Path C power, safety; MIT GIR noted but not needed by any module |
| A10 | **Path C and Path B readiness.** 04: shopping list → **Pico WH**; Lab 04 **Session 5 Flash files and Wi-Fi** (append/flush, power-cut test, connect/reconnect); name KVL/KCL and Thevenin as hooks. 06: an optional **FPGA milestone** in Kestrel Datapath (Yosys/nextpnr flow, a supported board, pin constraints, UART; Harris & Harris ch. 4). 07: a **linking** session (CS:APP ch. 7, Ward ch. 15) before Heapsmith M7. 09 Lab 03: build the promised three-host routed network (Kurose ch. 4–5, Ward ch. 9). | no new ids (sessions/milestones) | — | §1.1 |
| A11 | **Placement.** A whole-track math placement; English placement parts made independent with a "placed out" path per stage. | `FND-MA-PLACEMENT` 135 | [] | foundations audit |
| A12 | **Engineering practice.** 02 Lab 02 gains a code-review checklist on your own branch diff and a CI step (pre-commit hook; GitHub Actions optional); design notes use the template with a Parnas [W] ("what does each module hide?"). 05 Lab 03 gains a BST session and a topological sort step (Route Planner or Vault Search link graph). | no new ids | — | §1.2; unmet objectives |

**Capstone prerequisites** become `[MOD01 … MOD12, MOD14, MOD15, E11]` (adds MOD12, which it already uses, and the new courses). See open question Q1.

**Schema changes:** add `E11`, `FND-MA-PLACEMENT`, `MOD03-U9`, `MOD12-C4`, `MOD12-C5`, `MOD14-*`, `MOD15-*` to the ID tables; generalise `unit`/`units` beyond Module 12; note that module folders past 13 are placed by `order`, not folder number.

### 6.2 Merges, cuts and fixes to existing structure

| Change | Reason |
| :-- | :-- |
| **Renumber 06**: Lab 01 910, ISA 920, Lab 02 930, Datapath 940, Lab 03 950, Ember 960, Cache 970; Lab 02 needs ISA, Lab 03 needs Datapath, Cache Sim needs Ember | `order` contradicts the sequence |
| **Renumber 08**: Lab 01 1090, Arena 1100, Lab 02 1110, Tagfs 1120, Lab 03 1130, Seedling 1140 | same |
| 03 Proof Journal 560 → 515 with `[MOD03-LAB01]`; 12 Lab 01 860 → 885 | same |
| Capstone 1370/1380/1390 → 1700/1710/1720 | make room for 14/15 (§6.1) |
| Foundations: stage "Done when" lists keep only the milestones tied to that stage; project completion is its own checklist item; assessments come *after* E10/M11, not inside them | deadlock + circularity |
| **Merge** Start Here "Section 1" and `first-sections.md` Section 1 into one (Start Here keeps it; first-sections starts at Section 2) | duplicate onboarding |
| **Swap** 06's alternate video (Ben Eater duplicates 04's primary) for a verified compiler lecture series | fills the Ember gap |
| **Swap** 05's primary video to MIT 6.006; NeetCode Pro becomes alternate + problem lists while access lasts | access ends before Phase C |
| **Cut** "historical, not part of this curriculum" lists and "physics/distributed/crypto not core" lines from Math, Hardware, Systems and Theory indexes; replace with pointers to the courses that now own them | contradict current picks |
| **Cut** v1 fields (Tier, Prerequisites) from Your Shelf; regenerate every **Used in** | stale |
| **Rebuild** the Paper Reading Hub around the canon ladder (After / Tier / URL columns; Core papers marked "read inside module X at step Y"; keep existing entries as Enrichment) | canon §9 |
| Reword `OSS Project – Embeddable Typing Test` to drop employer/portfolio framing (see Q5) | DR-011 no job track |
| Fix the Lab 03 RISC-V desk-check bugs and add an "unverified until run" banner to Seedling | correctness |
| Remove every rule-breaking time word (list in §6.4) | DR-011 |

Nothing else is cut: every module serves the capstone or a core EECS/science/English need, and the spirals are deliberate.

### 6.3 Integration work (Phase 3)

1. **Study Deck card conventions** (deck path `~/workbench/deck/`, one file per module/track, `@tags modNN <lab>`, `@id modNN-<slug>`), a migration step for paper/Anki cards, deck syntax in the Blank-Sheet and Milestone Checkpoint templates. Every lab then ends with "add these cards to `modNN.md`".
2. **Per-course study kit**: blank-sheet prompts, Feynman targets, why-ladders, a subgoal-labelled worked example, a card list, a copywork or writing task on the topic, a teach-back — written into labs, not just overviews. Priority: 12, 08, 09, 11, 04.
3. **[V] at the step**: each lab names its lecture(s) and the after-lecture task.
4. **Interleaved review sets** spanning courses (e.g. after 09: a mixed set from 03 U5, 07 syscalls, 08 locks, 12 P3), one per module close.
5. **Core papers at fixed steps**: Keshav before the first paper (02); Dijkstra → 02 Lab 01 S1; Parnas → Study Deck design note; Ritchie–Thompson → Burrow Jr. M4; Hoare 1969 → 03 Lab 02 S2 (triples); DH/RSA → Toy Cipher M3; Hamming 1950 → Gatesmith stretch; Shannon Part I → 12 P1 + Chance Lab entropy; Patterson–Ditzel → Kestrel ISA M1; Cooley–Tukey → 12 Lab 01; Trusting Trust → 07 Lab 05; Lampson → 07 close; Cerf–Kahn + Clark → Courier M1; Jacobson → Courier M5; Saltzer–Reed–Clark → Courier M7; Codd → 11 Lab 01; Lamport → 11 Lab 03; Raft → capstone; Brooks → capstone design review.
6. **Callbacks and the artifact chain** into the capstone (each spec gets "Reuses / Reused by"); 10 picks up Matrix Studio transforms; 11 uses Chance Lab intervals; Courier/Lantern evaluations require `MOD12-P3`.
7. **Make the method texts agree** (all the contradictions in §4) and record V in a DR.

### 6.4 Time words to remove

"Sequence and time" headings (01, 02, 04–11 overviews); pace lines (01 overview, foundations "Pace" headings, first-sections); "Timed problem set" (03, 05, 12); timed drills as Done-when items and wpm targets (M02, M03, first-sections, Start Here tally → accuracy/level); "five-minute stranger test" (02, Study Deck); "a week later", "a month ago" prompts; sample dates in Proof Journal and Terminal Field Notes; "30 seconds" (Nib), "save hours" (Lab 00), "afternoon" (Gatesmith), "1950s" (Ember), "runs for hours" (Burrow), "while you sleep" (Crate), "30-day chart" (Copydiff), "lasts several sections" (08), "thousands of times a day" (09 Lab 02), "decades" (Stratum), "few days"/"an hour"/"30 seconds"/timer (LM02, LM06); capstone **"week-long field run"** (overview and spec) → "an extended field run of at least N readings / M planned failures"; DR-010's review date and DR-012's access date → move to the journal or mark as record metadata.

---

## 7. Unverified items and open questions

**Unverified:** see §3.5 and the course-verification results. Also: which editions Joseph owns; Courant ch. VIII's elementary-ODE section (not confirmed from a TOC); Lockhart/Strogatz/Ellenberg numbering is catalog order; Kurose 8e section titles; the RISC-V lab code (never run).

**Questions for Joseph** (Phase 2 can proceed on the defaults in brackets):

1. Should physics (14) and circuits/signals (15) be required for **every** capstone path, or only B and C? *[Default: required for all — you asked for EECS plus the science under it.]*
2. Which editions do you own of Velleman (3rd?), Anderson (3rd?), Kurose (8th?)? *[Default: 3e/3e/8e; Anderson's 3e is free online regardless.]*
3. Buy list: Harris & Harris, *Learning the Art of Electronics*, Heinrichs, *They Say / I Say* join Williams, Pinker, Ousterhout, Kleppmann. OK? *[Default: yes, each marked "when acquired" with a free fallback.]*
4. Hardware: a Pico WH (replacing the Pico H) and, for 14/15, a magnetometer/Hall breakout, a small coil, op-amps, inductors. OK? *[Default: yes.]*
5. The Monkeytype OSS note: reword to drop the employer framing, or archive it? *[Default: reword.]*

---

## 8. Results of later phases

*(Phase 2–4 results and the before/after check table go here.)*
