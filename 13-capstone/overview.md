---
title: "13 — Capstone"
id: "MOD13"
type: "overview"
module: "13-capstone"
phase: "E"
order: 1370
prerequisites: [MOD01, MOD02, MOD03, MOD04, MOD05, MOD06, MOD07, MOD08, MOD09, MOD10, MOD11, E10]
checkpoints: [MOD13-CLOSE]
tags: [module, capstone, integration]
---

# 13 — Capstone

**Connect your systems into one working whole — and prove it works.** Over Modules 01–12 you built a CPU and its compiler, an allocator, a shell, an archive format, a kernel, a file system, a transport protocol, a web server, a browser engine, and a database. The capstone joins several of them into one system that does something useful, then treats it like real engineering: a proposal, a design review, end-to-end tests, failure injection, measurements, a long report, a recorded talk, and an outside review.

---

## Prerequisites

Modules 01–11 complete (Module 12 may still be finishing). English: the full E10 skill set, and many design docs behind you.

## Objectives

1. Integrate independently built components through clear interfaces, and handle the mismatches.
2. Define success with measurable goals and test the whole system end to end, including under failures.
3. Manage a long project with milestones, risks, and scope decisions.
4. Write a long technical report and give a technical talk that a stranger can follow.
5. Seek, receive, and act on outside review.

## Choose one path

| Path | The system | Built from |
| :-- | :-- | :-- |
| **A. Your Own Web** | A personal learning web: **Glimpse** fetches pages over **Courier** (HTTP carried over CP/1 instead of TCP) from **Lantern**, which serves your vault as HTML, a search page powered by **Vault Search**, and a learning dashboard whose data lives in **Stratum** (your Study Deck reviews, copywork logs, and journal). | Glimpse, Courier, Lantern, Stratum, Vault Search, Study Deck |
| **B. Down to the Metal** | **Ember for RISC-V on Seedling:** retarget your Ember compiler to RV64; write Seedling's user programs (including a new shell) in Ember; add a writable SeedFS with a journal (Tagfs's design, in your kernel); run it all in QEMU with an automated test suite — and, as a stretch, Kestrel on an FPGA running Ember programs too. | Ember, Seedling, Tagfs ideas, Heapsmith, Burrow, Kestrel |
| **C. Field Station** | A **Pico W sensor station** (Pico Thermostat's sensing, power-safe logging to flash with a journal) reporting over Wi-Fi with a compact **Courier-lite** protocol to a home server that stores readings in **Stratum** and serves live and historical dashboards through **Lantern**, viewed in **Glimpse**; then a week-long field test with deliberate failures (power cuts, Wi-Fi loss). | Pico Thermostat, Crosswalk (FSMs), Courier, Stratum, Lantern, Glimpse, Chance Lab (statistics) |

All three are full-stack integrations of your own work. Pick the one that excites you most — your [Module 01 reflection](../01-intro-cs-taste/overview.md#module-close) and your logs will tell you which kind of work gives you energy.

> **Beyond this curriculum** *(historical reference; the v1 plan was superseded by DR-010)*: the [archived v1 plan](<../99 - Archive/v1 - Course-Based Curriculum/>) contains an ambitious drone-swarm capstone and advanced tracks (machine learning, robotics, security, signals). They're excellent next steps after this core, when you choose them deliberately — write a [Decision Record](<../04 - System/Decision Record.md>) if you do.

## Sequence

| Phase | Output |
| :-- | :-- |
| Proposal and design review | Proposal (design doc, 6–10 pages); review notes; v2 |
| Integration milestones | Working increments every two sections, each with end-to-end tests |
| Hardening | Failure injection, performance evaluation, security review |
| Communication | Final report, talk, outside review, revisions |

The full requirements are in **[the capstone spec](projects/the-whole-stack/spec.md)**.

## How the study methods run through the capstone

| Protocol | In the capstone |
| :-- | :-- |
| **R** | At each milestone, a one-page blank-sheet architecture drawing — then compare with the code. Where they differ, something is undocumented or misunderstood. |
| **F** | The recorded talk is a Feynman pass on your whole system. |
| **W** | The proposal's alternatives section, the risk register, and every scope cut — defended in writing. |
| **S** | Integration milestones as subgoals; each with a test that proves it. |
| **I** | Every skill you have, used together. |
| **D** | Integration bugs live between components. Trace logs from every layer, a stuck note, a walk. |
| **T** | Proposal, report, talk, outside review — the heaviest communication load of the curriculum, on purpose. |

## Video course

- **Primary:** **How to Write a Great Research Paper** and **How to Give a Great Research Talk** (Simon Peyton Jones) — [paper advice](https://www.youtube.com/watch?v=VK51E3gHENc) · [talk advice](https://www.youtube.com/watch?v=ot_McoYlwUo).
- **Alternate:** None. For the technical work, rewatch the video course of the modules your path is built from.
- **Which lectures go with which lab and project:** the map in [resources](<resources.md#lecture-to-vault-map>). Watch with the [V protocol](../study-protocols.md#v--watch-actively) and [use courses as companions](../study-protocols.md#using-video-courses).

---

## Module close (the end of the core curriculum)

1. **The final retrieval [R]:** on one large sheet, draw every system you've built and how they connect. Then look at the [README](../README.md)'s module table and check you didn't forget one.
2. **Then-vs-now [T]:** reread your E01 baseline note, your first journal entries, your first Feynman recording, and your Nib README. Write two pages about who you were as a learner then and who you are now. ([LM15](<../02 - Atlas/LM15 - Growth Mindset and Grit.md>)'s "then vs now" project, at full scale.)
3. **Plan what's next** with a Decision Record: an advanced track, open-source contribution, a job search, a research direction.
4. Tick it in [Start Here](<../00 - Start Here.md>). Then celebrate properly.

**Resources:** books, docs, and tools for this module are in [resources.md](resources.md) (pointers only — the projects are the course).
