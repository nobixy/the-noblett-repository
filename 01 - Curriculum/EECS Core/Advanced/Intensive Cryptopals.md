---
block_id: "Block 53"
title: "January Intensive: Cryptopals or TLA+"
category: "advanced"
term: "Year 4 January Intensive"
status: not-started
prerequisites: []
hours_estimate: 130
hours_actual: 0
primary_resource: "Cryptopals (cryptopals.com) OR Lamport TLA+ Course + Wayne Practical TLA+"
milestone: "All 8 Cryptopals sets solved OR formal TLA+ Raft spec finding a real bug"
date_started: ""
date_completed: ""
tier: "Tier 3 - Depth"
---

# Block 53 — January Intensive: Cryptopals or TLA+

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 January Intensive
> - **Estimated Hours:** ~130 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Cryptopals (cryptopals.com) OR Lamport TLA+ Course + Wayne Practical TLA+
> - **Key Milestone:** All 8 Cryptopals sets solved OR formal TLA+ Raft spec finding a real bug

---

## 🎯 Why This Block Matters
Hands-on mastery of cryptographic vulnerabilities OR formal mathematical specification of distributed concurrency.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- *None. This is a foundational block.*


## 📖 Primary Syllabus & Core Content
- [ ] Option A: Cryptopals Crypto Challenges (Sets 1–8: AES, padding oracles, Diffie-Hellman, RSA, DSA, zero-knowledge)
- [ ] Option B: Leslie Lamport's free TLA+ Video Course + Hillel Wayne, Practical TLA+

---

## 🛠️ Build Requirement
Complete hands-on security and formal verification engineering in `python`, `rust`, or TLA+ using `pytest`, `cargo`, `bash`, and `git`:
1. **Option A (Cryptopals Crypto Challenges)**: Solve challenge sets 1–8 from scratch without external crypto libraries; implement CBC padding oracle exploits, Bleichenbacher RSA signature forgery, DSA parameter tampering, and Diffie-Hellman MITM attacks in `python` or `rust` with automated test suites run via `pytest` or `cargo test`.
2. **Option B (TLA+ Formal Verification)**: Write a comprehensive, executable TLA+ / PlusCal specification of your Raft implementation from Block 23; run TLC model checker across state space with $> 10^7$ distinct states to verify State Machine Safety and uncover edge-case concurrency deadlocks.
3. **Verification & Delivery**: Shell test runner orchestrated in `bash`, mathematical security invariants documented in `latex`, and version-controlled with `git`.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Option A: All 8 Cryptopals challenge sets solved. Option B: TLA+ specification models Raft correctly and detects an injected or subtle race condition.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Cryptopals checks itself: you recover the plaintext or you don't. For TLA+, the TLC model checker checks your spec.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- pwn.college for security track; Formal Methods courses.

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Advanced Security and Cryptography|← Advanced Security and Cryptography]] | [[00 - Dashboard|Dashboard]] | [[Quantum Information and Computing|Quantum Information and Computing →]]
