---
title: "13 — Resources"
module: "13-capstone"
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
- **Simon Peyton Jones, "How to Write a Great Research Paper"** and **"How to Give a Great Research Talk"** (free videos and slides) — excellent, practical, and applicable to engineering reports and talks.

## Path-specific
- **A:** RFC 9110 (HTTP semantics) for carrying HTTP over a new transport; your Courier spec.
- **B:** the RISC-V ELF psABI specification (calling convention for RV64); your Ember and Seedling docs.
- **C:** MicroPython network docs for the Pico W; NTP basics (RFC 5905's introduction) for time synchronisation.

## Video and course companions
Free YouTube series and Coursera/edX/MIT OCW courses for this module are listed in [courses-and-videos.md](../courses-and-videos.md#modules-0113). Use them with the [V protocol](../study-protocols.md#v--watch-actively): lectures and quizzes as second explanations; this module's own projects, not the courses' assignments.
