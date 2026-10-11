---
title: "Lab 03 — Pipelines and Hazards on Paper"
id: "MOD06-LAB03"
type: "lab"
module: "06-computer-architecture"
phase: "C"
order: 930
prerequisites: [MOD06-LAB02]
---

# Lab 03 — Pipelines and Hazards on Paper

**Goal:** understand how real processors overlap instructions (**pipelining**), what goes wrong (**hazards**), and how hardware fixes it (**forwarding, stalls, branch prediction**) — on paper, then with a branch-predictor simulator driven by your own Kestrel traces.

**Sessions:** three.

---

## Session 1 — The idea of a pipeline

**Laundry analogy:** washing takes 30 min, drying 40, folding 20. One load at a time: 90 minutes per load. But you can start washing load 2 while load 1 dries. Once the pipeline is full, a load finishes every 40 minutes (the slowest stage). Each load still takes 90 minutes — **latency** is the same — but **throughput** is much higher.

A classic CPU pipeline has five stages:

| Stage | Does |
| :-- | :-- |
| **IF** | fetch the instruction |
| **ID** | decode; read registers |
| **EX** | ALU operation; compute addresses |
| **MEM** | load or store data memory |
| **WB** | write the result to the register file |

**Pipeline diagram** — draw this on graph paper for five independent instructions (time across, instructions down):

```
cycle:   1   2   3   4   5   6   7   8   9
I1       IF  ID  EX  MEM WB
I2           IF  ID  EX  MEM WB
I3               IF  ID  EX  MEM WB
I4                   IF  ID  EX  MEM WB
I5                       IF  ID  EX  MEM WB
```

Ideally, CPI → 1, and the clock period is the slowest **stage**, not the whole instruction (single-cycle datapath, Kestrel Datapath Milestone 5). [W] Why can't we make the pipeline 100 stages deep and get a 100× faster clock? (Registers between stages add delay; hazards get worse.)

---

## Session 2 — Hazards

### Data hazards

```
ADD r1, r2, r3     # writes r1 in WB (cycle 5)
SUB r4, r1, r5     # reads r1 in ID (cycle 3) — too early!
```

Draw the diagram. SUB reads the **old** r1.

**Fix 1 — stall:** insert bubbles (do nothing) until r1 is written. Count the lost cycles.
**Fix 2 — forwarding:** the ADD result exists at the end of EX (cycle 3). Route it straight to SUB's EX input in cycle 4. Draw the forwarding path on a datapath sketch.

**Load-use hazard:**
```
LD  r1, r2, 0      # data available at the end of MEM (cycle 4)
ADD r3, r1, r4     # needs it at the start of EX (cycle 4)
```
Even with forwarding, one bubble is needed. [W] Why? Draw it.

**Exercises:** for each of these sequences, draw the pipeline diagram (a) with no forwarding (stalls only) and (b) with full forwarding; count total cycles.

```
1)  ADD r1, r2, r3          2)  LD  r1, r7, 0          3)  ADDI r1, r1, 1
    ADD r4, r1, r1              ADD r2, r1, r1             ADDI r1, r1, 1
    ADD r5, r4, r1              ST  r2, r7, 1              ADDI r1, r1, 1
```

**Compiler connection:** a compiler can reorder independent instructions to fill load-use bubbles (**instruction scheduling**). Rearrange this so no stall is needed (with forwarding):
```
LD  r1, r7, 0
ADD r2, r1, r1
LD  r3, r7, 1
ADD r4, r3, r3
```

### Control hazards

A branch isn't resolved until EX. By then, the next two instructions are already fetched. If the branch is taken, they're wrong and must be **flushed**: a 2-cycle penalty per taken branch.

**Branch prediction** guesses the outcome early:
- **Always not taken:** keep fetching the next instruction.
- **Backward taken, forward not taken:** loops branch backward and are usually taken.
- **2-bit saturating counter** per branch: states "strongly not taken / weakly not taken / weakly taken / strongly taken"; one wrong guess doesn't flip a strong prediction. (Draw it as a 4-state FSM — Crosswalk again.)

---

## Session 3 — Simulate branch prediction on your traces

Add to your Kestrel emulator a **branch trace**: for every BR, its address, whether it was taken, and its target.

Write `bpsim.py` that replays the trace with each predictor:
1. always not taken;
2. always taken;
3. backward-taken/forward-not-taken;
4. a table of 2-bit counters indexed by (branch address mod table size), for table sizes 4, 16, 64.

Report the **accuracy** of each on your Life, Snake, `fib`, and Ember-compiled programs. Then estimate CPI with a 2-cycle misprediction penalty:

$$CPI \approx 1 + (\text{branches per instruction}) \times (\text{misprediction rate}) \times 2$$

**[W]:** why do the 2-bit counters do so well on loops? Where do they fail? (Hint: a branch that alternates taken/not-taken.)

---

## Done when

- [ ] All pipeline diagrams drawn (with and without forwarding), and the scheduling exercise solved.
- [ ] `bpsim.py` results table for four predictors on four programs, with the CPI estimates.

## Retrieval and reflection

1. **[R]:** the five stages; data hazard, load-use hazard, control hazard; forwarding vs stalling; the 2-bit predictor FSM.
2. **[F] (spoken):** "What is pipelining, and why does a load followed by its use still cost a cycle?"
3. Add a paragraph on pipelining to your [Kestrel Datapath](../projects/kestrel-datapath/spec.md) performance report.
