---
title: "13 — Resources"
id: "MOD13-RES"
type: "reference"
module: "13-capstone"
phase: "E"
order: 1390
prerequisites: []
---

# 13 — Resources

*Pointers only.*

## Engineering practice
- **Ousterhout, *A Philosophy of Software Design*** — reread before your proposal: interfaces and "deep modules" matter most at integration time.
- **Google's "Design Docs at Google"** (search the title; Industrial Empathy blog) and **the Rust and Go RFC/proposal repositories** — real design documents to model yours on.
- **Michael Nygard, *Release It!*** — stability patterns (timeouts, circuit breakers, bulkheads) for systems that must survive failures.
- **"The Twelve-Factor App"** (12factor.net) — short principles for running services; useful for Path A and C operational docs.

## Testing and failure
- **Jepsen analyses** (jepsen.io) — real-world failure-injection reports on distributed databases; superb examples of rigorous, honest evaluation writing.
- **"Simple Testing Can Prevent Most Critical Failures"** (Yuan et al., OSDI 2014) — what actually breaks in production.

## Writing and speaking
- **Joseph Williams, *Style*** (your English-track companion) — for the final report's revisions.
- **Simon Peyton Jones's paper and talk advice** — this module's video pick; see [Video course](#video-course).

## Path-specific
- **A:** RFC 9110 (HTTP semantics) for carrying HTTP over a new transport; your Courier spec.
- **B:** the RISC-V ELF psABI specification (calling convention for RV64); your Ember and Seedling docs.
- **C:** MicroPython network docs for the Pico W; NTP basics (RFC 5905's introduction) for time synchronisation.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

The capstone has no lectures of its own: it reuses your path's module. What it adds is a design review, a final report and a talk, so the pick here is about those.

**Primary — How to Write a Great Research Paper and How to Give a Great Research Talk**, Simon Peyton Jones (Microsoft Research). Free:
- Paper: [YouTube](https://www.youtube.com/watch?v=VK51E3gHENc) · [Microsoft Research page](https://www.microsoft.com/en-us/research/video/how-to-write-a-great-research-paper/) · [slides and notes](https://simon.peytonjones.org/great-research-paper/)
- Talk: [YouTube](https://www.youtube.com/watch?v=ot_McoYlwUo) · [slides and notes](https://simon.peytonjones.org/great-research-talk/)
- **Why it fits:** two of the most widely recommended talks on technical writing and speaking, by a researcher who is famous for clear explanations. The advice (lead with your one key idea, use examples, tell a story) applies directly to the design review, the final report and the talk.

**Alternate — none.** For the technical work, rewatch your path's module course:

| Path | Go back to |
| :-- | :-- |
| A — Your Own Web | [09](../09-networking/resources.md#video-course) (Kurose & Ross) · [10](../10-browser-engine/resources.md#video-course) (Chrome University) · [11](../11-databases/resources.md#video-course) (CMU 15-445) |
| B — Down to the Metal | [06](../06-computer-architecture/resources.md#video-course) (ETH DDCA) · [08](../08-operating-systems/resources.md#video-course) (MIT 6.S081) |
| C — Field Station | [04](../04-circuits-and-digital-logic/resources.md#video-course) (Ben Eater; Understanding PID Control) · [09](../09-networking/resources.md#video-course) (Kurose & Ross) · [11](../11-databases/resources.md#video-course) (CMU 15-445) |

### Lecture-to-vault map

| Vault item | Watch |
| :-- | :-- |
| [The Whole Stack](projects/the-whole-stack/spec.md): proposal and design review | How to Write a Great Research Paper |
| The Whole Stack: integration and hardening | your path's module course (table above) |
| The Whole Stack: final report | How to Write a Great Research Paper |
| The Whole Stack: talk and demo | How to Give a Great Research Talk |
