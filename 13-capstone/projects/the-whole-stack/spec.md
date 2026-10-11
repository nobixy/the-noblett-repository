---
title: "Capstone: The Whole Stack"
id: "MOD13-PRJ-the-whole-stack"
type: "project"
module: "13-capstone"
phase: "E"
order: 1380
prerequisites: []
artifact: "An integrated system built from at least three of your earlier projects (Path A, B, or C), with end-to-end tests, failure injection, a performance evaluation, and a security review"
deliverable: "Proposal (design doc) + review notes + final report (5,000–8,000 words) + recorded talk + outside review and response"
---

# Capstone: The Whole Stack

| | |
| :-- | :-- |
| **Module** | 13 Capstone |
| **You build** | One of the three integrated systems in the [capstone overview](../../overview.md#choose-one-path) — or a system of your own design that meets every requirement below (write a Decision Record to choose it) |
| **Deliverable** | Proposal, review notes, final report, recorded talk, outside review with your response |

---

## Why this matters

Real engineering is rarely "build a component from a spec." It's making components that were built separately — with different assumptions, formats, and failure modes — work together reliably, and then convincing other people that it works. That requires everything at once: design, testing, measurement, judgement about scope, and clear communication. The capstone is where you practise all of it on systems you know better than anyone, because you built them.

---

## Requirements (all paths)

1. **Integration:** at least **three** of your earlier projects, connected through **documented interfaces** (protocols, file formats, APIs). Changes to old projects are expected; record each in a change log with its reason.
2. **A measurable goal** and success criteria, set in the proposal (e.g. "a page with 20 search results renders within 1 second over Courier at 2% loss and 100 ms RTT"; "the station loses no committed reading across 50 random power cuts").
3. **End-to-end tests** run with one command, exercising the whole system from the user's side.
4. **Failure injection:** at least three kinds of failure tested deliberately (e.g. packet loss and reordering, process crashes, power loss, full disks, malformed input), each with defined expected behaviour.
5. **Performance evaluation** with uncertainty (Chance Lab: intervals, repeated runs), compared against a meaningful baseline (e.g. the same pages over TCP; Ember-compiled vs hand-written programs; your protocol vs MQTT or HTTP polling).
6. **Security review:** a threat model (who might attack what, how), the defences you have, the ones you don't, and at least one test of a defence.
7. **Operational docs:** how to build, run, test, and troubleshoot the system — a README a stranger can follow (E09 usability test with one real person).

---

## Phase 1 — Proposal and design review (sections 1–3)

**The proposal** is a design doc (6–10 pages, [template](<../../../04 - System/Design Doc Template.md>)) plus:
- **Goals and non-goals**, with the measurable success criteria.
- **Architecture:** a diagram of every component and every interface; for each interface, its format or protocol and which document specifies it.
- **What changes in each earlier project**, and why.
- **Alternatives considered** (at least three decisions).
- **Risk register:** at least eight risks (technical, time, knowledge), each with likelihood, impact, an early warning sign, and a mitigation. ("Courier too slow for page loads" — sign: < 1 MB/s in section 2 — mitigation: fall back to TCP for images.)
- **Milestone plan:** increments of about two sections each, each ending with something demonstrably working and an end-to-end test proving it.
- **Test, failure, performance, and security plans.**

**Design review:** get at least one reviewer (study partner, mentor, online community — E10 Part 6). Ask specific questions. Record every comment and your decision (accept / clarify / decline with reason). Revise to v2.

**Done when:** v2 is committed with review notes.

## Phase 2 — Integration milestones (sections 4–17)

Every two sections:
1. A **working increment** (something more works end to end than before).
2. The **end-to-end test** for it, added to the one-command suite.
3. A **Milestone Checkpoint** ([template](<../../../04 - System/Milestone Checkpoint Template.md>)) plus a one-paragraph **status note**: done, not done, risks that changed, scope decisions.
4. A **blank-sheet architecture drawing** compared with the code [R].

**Scope rule:** if a milestone slips twice, cut scope (move a feature to "future work") rather than extending the schedule. Record each cut with its reason. Shipping a smaller system that works beats an unfinished bigger one — and deciding what to cut is itself an engineering skill [W].

### Path-specific milestone suggestions

**A. Your Own Web**
1. Lantern serves vault pages as HTML (a Markdown → HTML converter, reusing Pagelet/Glimpse ideas); Glimpse browses them over TCP.
2. HTTP over Courier: a Courier transport in both Glimpse's client and Lantern (messages carry HTTP bytes; define how a response spans many messages). Same pages, new transport.
3. Search page backed by Vault Search; results rendered in Glimpse.
4. Stratum-backed dashboard: your review and copywork history as tables and simple charts (SVG generated server-side — Glimpse can show SVG as an image, or render charts as styled boxes).
5. Caching across the stack (HTTP cache in Glimpse; buffer pool in Stratum) measured end to end.
6. Failure runs: Gremlin 2 between browser and server; Lantern killed and restarted; Stratum crash recovery under load.

**B. Down to the Metal**
1. Ember codegen for RV64 (registers, calling convention per the RISC-V ABI, `ecall` for syscalls); a test suite of Ember programs running on Seedling and on your Ember interpreter (differential testing, as in Module 06).
2. An Ember runtime library for Seedling (printing, strings, memory).
3. Sprout rewritten in Ember, with pipes (new kernel feature: pipe syscalls) and redirection to SeedFS.
4. Writable SeedFS with a journal; crash tests by killing QEMU mid-write and remounting.
5. Performance: Ember vs C user programs; syscall and context-switch costs.
6. Stretch: Kestrel on an FPGA running the same Ember sources through the Kestrel backend.

**C. Field Station**
1. Pico W reads sensors and logs to flash with a journal that survives power cuts (test by cutting power 50 times).
2. Courier-lite (a smaller CP/1 subset suitable for a microcontroller: stop-and-wait or a tiny window) over Wi-Fi to the home server; resends buffered readings after outages.
3. Server stores readings in Stratum; Lantern serves live and historical pages; Glimpse displays them.
4. Time synchronisation and clock drift handling (the Pico has no battery clock — how do readings get correct timestamps?).
5. A week-long field run with planned failures (unplug the router for an hour; pull power at random), with Chance Lab statistics on data completeness and latency.

## Phase 3 — Hardening (sections 18–20)

1. **Failure injection campaign** for every failure type in your plan; results tabulated.
2. **Performance evaluation** against the success criteria and the baseline, with intervals.
3. **Security review:** threat model; tests of defences (e.g. path traversal against Lantern; malformed CP/1 packets; hostile Ember programs against Seedling's syscalls); known gaps listed honestly.
4. **Usability test** of your README with one person.

## Phase 4 — Communication (sections 21–23)

### Final report (5,000–8,000 words)

Structure (E10):
1. Abstract (150 words).
2. Introduction: the problem, why it's interesting, what you built, the headline results.
3. Background: what the reader needs to know; the earlier projects in one paragraph each.
4. Design: architecture, interfaces, key decisions with alternatives.
5. Implementation: what changed in each component; the hardest integration problems and how you solved them.
6. Evaluation: methods, results with uncertainty, comparison with goals and baselines, failure-injection results.
7. Security.
8. Lessons learned: technical and personal. What would you do differently?
9. Future work.
10. Appendices: interface specifications, test inventory.

Revise it at least twice, with a cooling-off period before each revision [D]. Use the E08 checklist. Run spell checking last; log every caught word in your spelling log one final time.

### The talk (short, recorded)

Slides (simple ones: diagrams and plots, few words) and a script (E10 Part 5): the problem, a live demo, the architecture in one diagram, the hardest problem, the evaluation, what you learned. Rehearse three times. Record. Watch it once and note three improvements; re-record if you want — or don't; one good take is enough.

### Outside review

Send the report (or the talk) to at least one outside reviewer: a working engineer, a study partner, an online community that reviews projects, or a mentor. Ask specific questions. Write a **response document**: each comment and what you did about it.

---

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Proposal and review | Complete, measurable goals, 8+ risks, review notes acted on | Complete, light review | Thin |
| Integration | 3+ projects, documented interfaces, change log | 3 projects, interfaces implicit | Fewer |
| Testing | One-command end-to-end suite covering every increment | Partial | Manual |
| Failure injection | 3+ failure types with expected behaviours and results | Two | One |
| Evaluation | Goals vs results with intervals and a baseline | Results only | Missing |
| Security | Threat model, tested defences, honest gaps | Model only | Missing |
| Report | 5,000–8,000 words, structured, revised twice | Complete | Draft |
| Talk | Focused, live demo, clear | Recorded | Missing |
| Outside review | Reviewed, response written | Reviewed | None |

**Done when:** every area at least 2; Testing, Report, and Outside review at 3.

## Connections

Everything. That's the point.
