---
block_id: "Block 27"
stage: "05 - Year 4"
title: "January Intensive: Cryptopals"
category: "core"
subject: "Computer Science"
term: "Year 4 January Intensive"
status: not-started
prerequisites:
  - "B24a - Applied Cryptography and Protocol Security"
  - "B10 - Math for CS"
hours_estimate: 100
hours_actual: 0
primary_resource: "Cryptopals (cryptopals.com), sets 1–6 required, 7–8 stretch"
milestone: "Cryptopals sets 1–6 solved from scratch with tests; sets 7–8 attempted"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
aliases: ["Intensive Cryptopals"]
---

# Block 27 — January Intensive: Cryptopals

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 January Intensive
> - **Estimated Hours:** ~100 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Cryptopals (cryptopals.com), sets 1–6 required, 7–8 stretch
> - **Key Milestone:** Cryptopals sets 1–6 solved from scratch with tests; sets 7–8 attempted
> - **Rewritten by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09): Cryptopals required; TLA+ moved to Track 5

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
Block 24a taught how protocols are built; Cryptopals makes you break them: ECB and CBC oracles, padding oracles, MAC forgeries, Diffie–Hellman man-in-the-middle, RSA and DSA mistakes. The capstone's red-team milestone is this skill pointed at your own swarm. Required since DR-005 (the TLA+ option moved to Track 5).

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B24a - Applied Cryptography and Protocol Security|Applied Cryptography and Protocol Security]]
- [[B10 - Math for CS|Math for CS]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Sets 1–2: encodings, XOR, AES-ECB/CBC, byte-at-a-time ECB decryption, padding.
- [ ] Set 3: CBC padding oracle, CTR mode, Mersenne Twister cloning.
- [ ] Set 4: CTR bit-flipping, SHA-1 / MD4 length extension, HMAC timing leaks.
- [ ] Set 5: Diffie–Hellman and MITM, SRP, RSA basics and the e=3 broadcast attack.
- [ ] Set 6: RSA parity oracle, Bleichenbacher's PKCS#1 v1.5 attack, DSA key recovery from nonce reuse.
- [ ] Stretch, sets 7–8: CBC-MAC forgery, compression oracles (CRIME), hash multicollisions, elliptic-curve and GCM attacks.

---

## 🛠️ Build Requirement
Solve each challenge in Python or Rust with no high-level crypto library for the attacked primitive, each with an automated test.
1. **Sets 1–6** required.
2. **Sets 7–8** stretch.
3. **Link to your swarm:** for each attack, one line in your Block 24a threat model on whether your secure link is exposed.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Sets 1–6 solved with passing tests; the threat-model cross-reference is written.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- cryptopals.com (free, 8 sets).
- Boneh–Shoup (toc.cryptobook.us) for the theory behind each break.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Cryptopals checks itself: you recover the plaintext or forge the message, or you don't.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- pwn.college crypto modules (free) for more guided practice.
- TLA+ (learntla.com, Lamport's course) moved to Track 5; use it in the capstone to specify the swarm's task-allocation protocol if you want a stretch.

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[Specialization Branches|← Specialization A, Course 1]] | [[00 - Start Here|Start Here]] | [[B27a - Drone Lab - Flight Stack, ROS 2 and SITL|Drone Lab →]]
