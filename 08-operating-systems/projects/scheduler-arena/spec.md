---
title: "Project: Scheduler Arena"
module: "08-operating-systems"
hours: 30
artifact: "arena: a discrete-event CPU scheduling simulator with workload files, seven policies (including one you design), metrics, Gantt charts, property tests, and a reality check against Linux"
deliverable: "Lab report: which scheduler for which workload? (with your own policy argued for) + 4-minute demo"
---

# Project: Scheduler Arena

| | |
| :-- | :-- |
| **Module** | 08 Operating Systems |
| **Time** | About 30 hours |
| **Prerequisites** | Module 05 (queues, heaps, measurement); Module 03 (probability helps); Lab 01 of this module |
| **You build** | A simulator that plays out how an operating system shares one CPU among many jobs, under different scheduling rules. You feed it workloads, it produces timelines and metrics, and you run a tournament between policies — including one of your own design. Then you check one idea against the real Linux scheduler |
| **Deliverable** | A lab report and a demo |

---

## Why this matters

Your laptop runs hundreds of processes on a handful of cores. The **scheduler** decides who runs next, many times a second, and its choices decide whether your music stutters while a compile runs, whether a server answers quickly under load, and whether a background job ever finishes. There is no perfect policy — only trade-offs between **response time**, **throughput**, and **fairness**. A simulator lets you see those trade-offs clearly and quickly, before you write the real scheduler in Seedling (Milestone 4).

**Real-world analogs:** Linux's CFS/EEVDF schedulers, Windows' priority scheduler, batch schedulers on supercomputers, Kubernetes pod scheduling.

---

## The model

A **job** arrives at a time and alternates **CPU bursts** and **I/O bursts**:

```
# workload: name arrival bursts (CPU and I/O alternating, in ms; always starts and ends with CPU)
editor   0    2 30 2 30 2 30 2
compile  5    400
backup   10   50 200 50 200 50
music    0    1 9 1 9 1 9 1 9 1 9 1
```

- One CPU. While a job does I/O, it doesn't need the CPU (other jobs can run). I/O completes after its time and the job becomes ready again.
- A **context switch** costs a configurable overhead (default 0.1 ms).
- **Discrete-event simulation:** keep a priority queue (your Module 05 heap) of future events — arrivals, burst completions, I/O completions, time-slice expirations — ordered by time; repeatedly take the next event and update the state. (Same structure as Gatesmith's event-driven mode.)

## The policies

1. **FIFO** (first come, first served).
2. **SJF** (shortest job first — uses the *true* next burst length, which a real OS can't know; an "oracle" baseline).
3. **STCF** (shortest time-to-completion first, preemptive version of SJF).
4. **Round robin** with time quantum q (try 1, 10, 100 ms).
5. **MLFQ** (multi-level feedback queue): several priority levels; new jobs start at the top; a job that uses its whole quantum moves down; a job that gives up the CPU early (for I/O) stays; every S ms, **boost** everyone to the top (so long jobs can't starve). Write your exact rules in the design doc.
6. **Stride scheduling** (proportional share): each job has tickets; each has a "pass" value that advances by (big constant ÷ tickets) each time it runs; always run the lowest pass. Deterministic fairness by weight.
7. **Your own policy.** Design a scheduler for a specific goal you state up front (e.g. "keep the music job's response under 5 ms while finishing compiles as fast as possible," or "be fair and still interactive without knowing burst lengths"). Argue for it [W], then measure it in the tournament.

## The metrics

For each job: **turnaround** (finish − arrival), **response** (first run − arrival), **waiting** (time ready but not running). Overall: averages and 95th percentiles of each; **throughput** (jobs per second); **CPU utilisation**; **Jain's fairness index** of the CPU share each job got relative to its fair share: (Σxᵢ)² ÷ (n·Σxᵢ²), which is 1 when perfectly fair. Plus number of context switches.

---

## Milestones

### Milestone 1 — Design doc, workload format, generator

1. **Design doc v1** (3 pages): the event model, the policy interface (e.g. `on_arrival`, `on_ready`, `pick_next`, `on_tick`), the metrics with exact definitions, and your own policy's goal.
2. Workload parser with clear errors; **generator** (seeded) for classes of jobs: interactive (tiny CPU bursts, frequent I/O), CPU-bound (one huge burst), mixed; and three standard workloads: "desktop" (interactive + a couple of CPU hogs), "server" (many similar requests arriving randomly — exponentially distributed gaps, Module 12 preview), "batch" (all CPU-bound, all at time 0).

### Milestone 2 — The simulator and FIFO, SJF, RR

1. Event loop, I/O handling, context switch overhead.
2. **Gantt chart** output: ASCII (`|editor|compile....|music|…`) and SVG (one row per job, coloured run/ready/I/O segments).
3. FIFO, SJF, STCF, RR.

**Property tests** (true for **every** policy; run them on 1,000 random workloads):
- **conservation:** each job's total CPU time equals the sum of its CPU bursts;
- **no time travel:** no job runs before it arrives or during its own I/O;
- **one at a time:** at most one job runs at any instant;
- **work-conserving:** the CPU is never idle while some job is ready (for these policies);
- every job finishes.

**Hand-checked tests:** three tiny workloads worked out on paper for FIFO and RR (q = 2) — draw the Gantt chart by hand first [S], then compare.

**Done when:** property and hand-checked tests pass.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *why round robin improves response time but can hurt turnaround*.

### Milestone 3 — MLFQ, stride, and your policy

Implement them. For MLFQ, show (with a Gantt chart) a workload where a CPU-bound job would starve **without** the boost, and is rescued with it. For stride, show shares tracking ticket ratios (e.g. 3 : 2 : 1) over time.

### Milestone 4 — The tournament

Run every policy on every standard workload (several seeds each). Tables for each metric; one chart per workload comparing policies on response p95 vs turnaround average (a trade-off scatter). Then answer:
- Which policy wins for interactive response? For throughput? For fairness?
- How does RR's quantum change things? Is there a sweet spot?
- How does your own policy do on its stated goal? Where does it lose?
- What does context-switch overhead do at q = 1 ms?

### Milestone 5 — Reality check on Linux

Linux's scheduler gives CPU shares by **weight** (set with `nice`). Test it:
1. Pin two CPU-bound processes to **one** core: `taskset -c 0 ./spin & taskset -c 0 nice -n 5 ./spin &` (where `spin` is a C busy loop that counts iterations and prints its count every second).
2. Measure each one's share of iterations for nice differences of 0, 5, 10.
3. Compare with stride scheduling in your simulator with tickets in the same ratio. (Linux's weights grow about 1.25× per nice level — look up the exact weight table in the kernel source or documentation, and use those numbers for your stride tickets.)

**Done when:** a table of measured vs simulated shares, with an explanation of differences.

---

## Testing guidance

- **Properties over random workloads** (the strongest tests here).
- **Hand-computed Gantt charts** for tiny cases.
- **Seeds everywhere.**

## Common pitfalls

- **Simultaneous events:** an arrival and a quantum expiry at the same time — define the tie-breaking order and test it.
- **Off-by-one in quanta** (does the slice include the context switch?).
- **Response-time definition:** first time scheduled, not first time it *could* have been. Be exact.
- **Comparing averages only:** p95 tells the story of the worst-off jobs.

## Communication deliverable

1. **Design doc** v1 → v2.
2. **Lab report** (3 pages, E10): the tournament results, the MLFQ starvation story with Gantt charts, your policy's argument and verdict, and the Linux reality check.
3. **Demo (4 minutes):** the same workload under four policies, side by side as Gantt charts.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Each policy's rule from memory before implementing; the metric definitions |
| **F** | Response vs turnaround; why MLFQ needs a boost |
| **W** | Your own policy's argument; tie-breaking; quantum choice |
| **S** | Hand Gantt charts as worked examples |
| **I** | Simulation, statistics, and real-system measurement |
| **T** | Report and demo |

## Stretch goals

- **Multiple CPUs** with per-CPU queues and work stealing.
- **Real-time:** EDF (earliest deadline first) for jobs with deadlines; count missed deadlines.
- **Trace replay:** record real process activity with `perf sched` and replay it in the arena.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Simulator | Event-driven; I/O; overhead; Gantt ASCII + SVG | Works | Time-step hacks |
| Policies | All 7 incl. your own, with exact rules | 5 | Fewer |
| Tests | Properties on 1,000 workloads + hand charts | Hand only | Few |
| Tournament | All metrics incl. p95 and fairness; trade-off charts | Averages only | Partial |
| Linux check | Measured vs simulated shares, explained | Measured only | Missing |
| Communication | Doc, report, demo | Two | One |

**Done when:** every area at least 2; Tests at 3.

## Connections

- **Back:** Module 05 (heaps, queues), Gatesmith (event-driven simulation), Crosswalk (job states).
- **Forward:** Seedling M4 (your real scheduler), Module 09 (packet scheduling and fairness between flows in Courier), Module 12 (queueing and probability).

> **Originality note:** the workload format, policy tournament, your-own-policy requirement, and Linux reality check were designed for this curriculum.
