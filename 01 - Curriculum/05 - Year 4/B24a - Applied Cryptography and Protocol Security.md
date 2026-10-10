---
block_id: "Block 24a"
title: "Applied Cryptography and Protocol Security (Stanford Crypto I + Boneh–Shoup)"
category: "core"
subject: "Computer Science"
term: "Year 4 Fall"
status: not-started
prerequisites:
  - "B10 - Math for CS"
  - "B15 - Probability"
  - "B19 - Networking"
hours_estimate: 120
hours_actual: 0
primary_resource: "Dan Boneh, Cryptography I (Coursera, free audit) + Boneh–Shoup, A Graduate Course in Applied Cryptography (free)"
milestone: "Crypto I assignments done; your Noise-based secure link interoperates with a reference implementation and fails closed under replay and tampering; MAVLink 2 signing on in SITL"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 24a — Applied Cryptography and Protocol Security (Stanford Crypto I + Boneh–Shoup)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 Fall
> - **Estimated Hours:** ~120 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Dan Boneh, Cryptography I (Coursera, free audit) + Boneh–Shoup, A Graduate Course in Applied Cryptography (free)
> - **Key Milestone:** Crypto I assignments done; your Noise-based secure link interoperates with a reference implementation and fails closed under replay and tampering; MAVLink 2 signing on in SITL
> - **Added by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
The capstone swarm's radio links are its attack surface: anyone can listen, replay, inject or jam. Applied cryptography and protocol design are therefore core, not optional. This block teaches what each primitive guarantees and, more importantly, how protocols built from them fail. Block 27 (Cryptopals) then has you break them by hand.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B10 - Math for CS|Math for CS]]
- [[B15 - Probability|Probability]]
- [[B19 - Networking|Networking]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Security definitions and attack models; one-time pad to stream ciphers; PRGs and PRFs.
- [ ] Block ciphers and modes; MACs; authenticated encryption (AES-GCM, ChaCha20-Poly1305) and nonce misuse.
- [ ] Hash functions; key derivation (HKDF); passwords vs keys.
- [ ] Key exchange: Diffie–Hellman, X25519; public-key encryption and signatures (Ed25519); certificates vs pre-shared keys for a closed fleet.
- [ ] Protocols: TLS 1.3 (RFC 8446); the Noise Protocol Framework handshake patterns (XX, IK, KK); the WireGuard design paper.
- [ ] Fleet key management: provisioning, rotation, revocation of a captured node, replay windows, forward secrecy.
- [ ] Embedded crypto: libsodium, constant-time code, randomness on microcontrollers, secure boot and flash encryption (ESP32).
- [ ] Drone link security: MAVLink 2 message signing (authenticates, does not encrypt) and what it leaves open.
- [ ] Threat modeling (STRIDE) and writing a threat model; post-quantum awareness (NIST FIPS 203 ML-KEM, FIPS 204 ML-DSA, 2024).

---

## 🛠️ Build Requirement
1. **Crypto I programming assignments** in Python or Rust.
2. **Swarm secure-link library:** Noise (XX or IK) over UDP or ESP-NOW between Pi and ESP32 nodes, using libsodium or the `snow` Rust crate; key provisioning and rotation; a replay window.
3. **MAVLink 2 signing** enabled between PX4 SITL and your ground-control script; show unsigned and replayed commands rejected.
4. **Threat model** (STRIDE) for a 5-drone swarm's comms, then attack your own link: replay, tamper, key reuse, downgrade.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Crypto I assignments and quizzes complete; your link interoperates with a reference Noise implementation; every attack in your threat model fails closed or is documented as residual risk.

---

## 🎓 Companion Courses (DR-006, 2026-10-09)
- **Coursera Plus:** *Cryptography I* (Stanford, Boneh) is included, so you get the graded programming assignments and certificate with your subscription.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- Dan Boneh, Cryptography I (Coursera; audit free, certificate 💲): coursera.org/learn/crypto.
- Boneh & Shoup, *A Graduate Course in Applied Cryptography* (free): toc.cryptobook.us.
- Noise Protocol Framework spec (free): noiseprotocol.org/noise.html. WireGuard paper (free): wireguard.com/papers/wireguard.pdf.
- TLS 1.3, RFC 8446: rfc-editor.org/rfc/rfc8446. NIST FIPS 203 / 204: csrc.nist.gov/pubs/fips/203/final, …/204/final.
- libsodium docs: doc.libsodium.org; `snow` (Rust Noise): github.com/mcginty/snow; ESP32 Secure Boot v2 docs (docs.espressif.com, …/security/secure-boot-v2.html).
- MAVLink 2 message signing: mavlink.io/en/guide/message_signing.html; PX4: docs.px4.io/main/en/mavlink/message_signing.html.
- 💲 Jean-Philippe Aumasson, *Serious Cryptography*, 2nd ed. (No Starch; library copy works). Kit: none, reuses your boards.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Coursera's autograded quizzes; interop with a reference implementation; your own attack scripts from Block 27 later.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- MIT 6.5660 / E2 Computer Security lectures for the systems side.
- Christof Paar's *Understanding Cryptography* lectures (free on YouTube).

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B24 - Theory of Computation|← Theory of Computation]] | [[00 - Start Here|Start Here]] | [[B25 - Convex Optimization|Convex Optimization →]]
