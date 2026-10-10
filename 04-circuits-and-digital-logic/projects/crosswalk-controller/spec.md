---
title: "Project: Crosswalk Controller"
module: "04-circuits-and-digital-logic"
hours: 26
artifact: "One finite-state machine, three implementations that must agree: a Python model with property tests, a Gatesmith gate-level design, and a running Pico with real LEDs and a button"
deliverable: "Design note with state diagram and safety invariants + 4-minute demo with the real hardware + short verification report"
---

# Project: Crosswalk Controller

| | |
| :-- | :-- |
| **Module** | 04 Circuits and Digital Logic |
| **Time** | About 26 hours |
| **Prerequisites** | Lab 04 (Pico); [Gatesmith](../gatesmith/spec.md) Milestone 4 (flip-flops); Module 03 Unit 1 (logic) |
| **You build** | The controller for a pedestrian crossing: car lights, a WALK signal, and a request button. You design it as a **finite-state machine**, state its **safety rules**, and implement it three ways — as a Python model that is tested against thousands of random event sequences, as a gate-level circuit in Gatesmith, and on a real Pico with LEDs — and show all three behave identically |
| **Deliverable** | Design note, demo, and a short verification report |

---

## Why this matters

A **finite-state machine** (FSM) is a system that is always in one of a fixed set of **states**, and moves between them on **events** (a button press, a timer expiring). FSMs are everywhere: traffic lights, vending machines, the button debouncer you wrote in Lab 04, network protocols (Courier in Module 09 is one), text parsers (your browser's HTML tokenizer in Module 10 is one), and the control unit of the CPU you'll build in Module 06.

A crossing is also **safety-critical**: a bug can hurt someone. So this project introduces how engineers make that kind of system trustworthy: write the safety rules down as **invariants**, test them against huge numbers of random scenarios, and build the same design in different ways that must agree.

**Real-world analogs:** traffic controllers, elevator and railway signalling logic, protocol state machines, hardware control units.

---

## The requirements

Lights:
- **Cars:** GREEN, YELLOW, RED.
- **Pedestrians:** WALK (white figure), DONT_WALK (red hand), and a **flashing** DONT_WALK warning.

Input: a pedestrian **request button** (debounced).

Behaviour (times are for real use; use a `SPEED` factor so tests and demos run 10× faster):
1. Default: cars GREEN, pedestrians DONT_WALK.
2. Cars get at least **20 s** of GREEN before a request is served.
3. When a request has been made and the minimum green has passed: cars YELLOW for **3 s**, then cars RED.
4. After cars have been RED for **1 s** ("all-red" clearance): WALK for **7 s**.
5. Then flashing DONT_WALK for **5 s** (flash at 2 Hz).
6. Then DONT_WALK steady, and after **1 s** all-red, cars GREEN again.
7. Button presses at any time are **remembered** (latched) and served at the next opportunity; presses during WALK are ignored (the pedestrian is already crossing). [W] Is ignoring them right? What would a real pedestrian expect?
8. A request indicator LED shows that a request is waiting.

### Safety invariants (must hold at every moment)

- **S1:** cars GREEN or YELLOW ⇒ pedestrians DONT_WALK (steady).
- **S2:** WALK or flashing ⇒ cars RED.
- **S3:** cars never go directly from RED to YELLOW, or from GREEN to RED.
- **S4:** every request is served within a bounded time (no starvation) — work out the maximum.
- **S5:** cars get at least 20 s GREEN between pedestrian phases (traffic must flow too).

Add any you think are missing [W].

---

## Milestones

### Milestone 1 — Design (paper first)

**Subgoal labels [S] for designing any FSM:**
1. **List the states** (name each, say what every light shows in it).
2. **List the inputs/events** (button, timer done).
3. **Draw the state diagram:** circles for states, arrows for transitions labelled with the event that causes them.
4. **Write the transition table:** current state × event → next state, plus outputs.
5. **Check every state handles every event** (even if "stay here"). Missing cells are bugs.
6. **Check the invariants** against the table, state by state.

Draw the diagram (paper, then Mermaid in your design note). Write the **design note** (2 pages): states, table, timing, invariants, and two decisions with reasons (e.g. how you latch the request; whether flashing is its own state or a sub-behaviour).

**Done when:** the table has no empty cells, and every invariant is checked by hand for every state.

### Milestone 2 — The Python model and property testing

1. Implement the FSM in Python as **data** (the transition table as a dictionary) plus a small engine — not as a pile of `if` statements. [W] Why is table-driven better here?
2. Time is a **fake clock** (Module 02 Lab 02): the engine is advanced with `tick(ms)` and `press()` calls, so tests run instantly.
3. **Scenario tests (golden traces):** "press at t = 5 s" → expected light sequence with times. Write five scenarios covering early presses, late presses, presses during WALK, repeated presses, and no presses.
4. **Invariant checker:** a function that checks S1–S3 and S5 on the current outputs; call it after **every** tick in every test.
5. **Random testing:** generate 10,000 random event sequences (random presses at random times over 10 minutes of simulated time, seeded). For each, run the model with the invariant checker on, and check S4 (every press served within your maximum).

**Done when:** scenarios pass and 10,000 random runs find no invariant violation. Then **plant a bug** (e.g. skip the all-red) and confirm random testing catches it.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why test invariants on random sequences rather than only on scenarios you wrote?* (What kind of bugs do humans fail to imagine?)

### Milestone 3 — The gate-level design in Gatesmith

Now build it as hardware.

1. **Timing:** a `Counter8`-style timer that counts clock ticks (at 1 tick per second for real time, or per 100 ms for SPEED) and signals `done` when it reaches the current state's duration. Each state loads its duration on entry.
2. **State encoding:** choose how to store the state in flip-flops:
   - **binary** (e.g. 6 states → 3 flip-flops), or
   - **one-hot** (one flip-flop per state; exactly one is 1).
   Try both on paper. [W] Which needs fewer flip-flops? Which makes next-state logic simpler? Which is easier to check for "impossible" states?
3. **Next-state and output logic:** write each next-state bit and each light as a Boolean formula of (state bits, `done`, `request`). Simplify them (Truth Engine can check that your simplified version is equivalent).
4. **The request latch:** a flip-flop that is set by the (debounced) button and cleared when the WALK phase starts.
5. Build it in Gatesmith. Drive it with test vectors generated **from your Python model**: same inputs, cycle by cycle; the outputs must match exactly. This is **equivalence checking by simulation** between two implementations.

**Done when:** the Gatesmith design matches the Python model on all five scenarios and 100 random sequences, and you've viewed a full cycle in GTKWave.

### Milestone 4 — The Pico

1. Wire: three car LEDs, two pedestrian LEDs (or one red + one white/green), a request-waiting LED, and the button. (Resistors for 3.3 V — Lab 04.)
2. Port the **table-driven** model to MicroPython. Same table, real clock (`time.ticks_ms()` and `time.ticks_diff()`, which handle the counter wrapping around — [W] why do they need to?), your debouncer from Lab 04.
3. Log every transition to serial as `millis,from_state,to_state,lights`.
4. Run the five scenarios by hand (with SPEED = 10). Capture the logs.
5. **Check the real logs** with your Python invariant checker: write a script that replays a captured log through the checker.

**Done when:** all five scenarios behave correctly on the Pico, and the invariant checker passes on the captured logs.

---

## Testing guidance

- **One table, three engines:** Python, Gatesmith, and MicroPython all use the same transition table (generate the Gatesmith logic and the MicroPython table from one source file if you can — a stretch goal).
- **Invariants everywhere:** in unit tests, random tests, hardware simulation, and on real logs.
- **Plant bugs** to prove your tests can fail.

## Common pitfalls

- **Forgetting a transition** (an empty table cell) → the machine gets stuck. Step 5 of the design subgoals catches it.
- **Time arithmetic that breaks at wrap-around** on the Pico (`ticks_ms` overflows after about 12 days in MicroPython's small-int range). Always use `ticks_diff`.
- **Button handled outside the FSM** with ad-hoc flags. Make the request latch a proper part of the state.
- **One-hot designs reaching "impossible" states** (two flip-flops on at once) after a glitch or power-up. Add a reset, and decide what an impossible state does (go to a safe state: cars RED, DONT_WALK).

## Communication deliverable

1. **Design note** (2 pages) with the state diagram (Mermaid), the transition table, the invariants, and the encoding comparison.
2. **Verification report** (1 page, E10 level): how you checked the design (scenarios, 10,000 random runs, planted bugs caught, equivalence with Gatesmith, real-log checking) — and what you'd still worry about if this controlled a real road.
3. **Demo (4 minutes):** the Pico running a full cycle with the button, the GTKWave trace, and the random tester catching a planted bug.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 3, redraw the state diagram from memory |
| **F** | What an FSM is; why invariants plus random tests build trust |
| **W** | Ignoring presses during WALK; table-driven design; binary vs one-hot; `ticks_diff`; missing invariants |
| **S** | The six FSM design subgoals |
| **I** | Software, logic design, and hardware alternate |
| **T** | Design note, report, demo |

## Stretch goals

- **Single source of truth:** write the FSM once in a small text format and generate the Python table, the MicroPython table, and the Gatesmith netlist from it.
- **74HC build:** implement a simplified 4-state version (no flashing) with 74HC74 flip-flops and gates, clocked by your 555. Compare its behaviour with the model.
- **Model checking:** instead of random testing, explore **every** reachable (state, latch, timer) combination exhaustively with BFS and prove the invariants hold in all of them. (This is how real safety-critical designs are verified.)
- **Night mode:** flashing yellow after a configurable hour.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Design | Complete table, invariants, encoding comparison | Diagram only | Incomplete |
| Python model | Table-driven, fake clock, scenarios, 10,000 random runs, planted bug caught | Scenarios only | Fragile |
| Gatesmith | Matches model cycle-by-cycle; viewed in GTKWave | Partial | Missing |
| Pico | Five scenarios; real logs pass the checker | Runs | Missing |
| Communication | Note, report, demo | Two | One |

**Done when:** every area at least 2; Python model at 3.

## Connections

- **Back:** Lab 04's debouncer (a small FSM), Gatesmith (flip-flops, counters), Truth Engine (simplification and equivalence), Module 02 (fake clocks, golden traces).
- **Forward:** Module 06 (the CPU control unit is an FSM), Module 09 (Courier's connection states), Module 10 (the HTML tokenizer is an FSM), Module 11 (transaction states).

> **Originality note:** the requirements, invariants, and three-implementation verification plan were designed for this curriculum.
