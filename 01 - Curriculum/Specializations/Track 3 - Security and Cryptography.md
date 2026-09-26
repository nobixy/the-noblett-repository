---
track_id: "Track 3"
title: "Security and Cryptography"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "[[06 - C Fluency]]"
  - "[[09 - Computer Systems]]"
  - "[[10 - Math for CS]]"
  - "[[16 - Operating Systems]]"
  - "[[19 - Networking]]"
  - "[[27 - Intensive Cryptopals or TLA+]]"
target_profile: "Cryptographic Engineer, Security Researcher, Binary Exploitation Specialist, High-Assurance Systems Auditor"
aliases: [Track 3 - Security and Cryptography, Track 3 - Cryptography and Systems Security]
---

# Track 3: Security and Cryptography

> [!INFO] Track Overview
> - **Track ID:** Track 3
> - **Prerequisites:** [[06 - C Fluency]], [[09 - Computer Systems]], [[10 - Math for CS]], [[16 - Operating Systems]], [[19 - Networking]], [[27 - Intensive Cryptopals or TLA+]]
> - **Target Profile:** Cryptographic Engineer, Security Researcher, Binary Exploitation Specialist, High-Assurance Systems Auditor
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Security is not a feature that can be bolted onto software post-hoc; it is an adversarial engineering discipline that requires reasoning about the entire computational stack—from quantum and algebraic number theory down to microarchitectural silicon side-channels and operating system memory layouts. In a world where critical national infrastructure, global financial systems, and private communication rely on cryptographic code, an amateur understanding of security leads to catastrophic exploits.

This track bridges rigorous mathematical cryptography (provable security reductions, game-hopping proofs, lattice-based post-quantum cryptography, and zero-knowledge proof systems) with low-level systems vulnerability exploitation (binary analysis, Return-Oriented Programming, heap layout manipulation, kernel exploitation, and timing side-channel attacks). Students develop the adversarial mindset and engineering rigor needed to design, implement, and formally audit cryptographic systems that withstand attack by sophisticated adversaries.

---

## 📚 Core Courses

### Course 1: Applied Cryptography & Provable Security (Boneh & Shoup / Stanford CS255 Equivalent)

This course develops modern provable cryptography, reductionist security proofs, public-key primitives, and post-quantum algebraic constructions.

#### Module 1: Symmetric Foundations, Pseudorandomness & Block Ciphers
- Mathematical definitions of security: Perfect Secrecy, Shannon's Theorem, and One-Time Pads.
- Pseudorandom Generators (PRGs) and Pseudorandom Functions (PRFs): computational indistinguishability and next-bit unpredictability.
- Block ciphers: Feistel networks, Substitution-Permutation Networks (SPN), AES algebraic design (Rijndael S-box, Galois field $\mathbb{F}_{2^8}$ arithmetic).
- Modes of operation: ECB insecurity, CBC mode (and IV reuse vulnerabilities), CTR mode, and Galois/Counter Mode (GCM).

#### Module 2: Message Authentication & Authenticated Encryption
- Message Authentication Codes (MACs): existential unforgeability under chosen-message attacks (EUF-CMA).
- Hash functions and collision resistance: Merkle-Damgård construction, length-extension attacks, HMAC proofs, and SHA-3 (Keccak sponge functions).
- Authenticated Encryption with Associated Data (AEAD): IND-CPA vs IND-CCA2 security definitions; Encrypt-then-MAC (EtM) security composition theorem.

#### Module 3: Public-Key Cryptography & Discrete Logarithms
- Computational number theory: prime generation, Miller-Rabin primality testing, extended Euclidean algorithm, and Chinese Remainder Theorem (CRT).
- RSA cryptosystem: Trapdoor permutations, RSA assumption, padding schemes (OAEP, PSS), and Bleichenbacher's chosen-ciphertext padding attack.
- Diffie-Hellman key exchange and ElGamal encryption: Computational Diffie-Hellman (CDH) and Decisional Diffie-Hellman (DDH) assumptions in cyclic groups.

#### Module 4: Elliptic Curves & Pairing-Based Cryptography
- Elliptic curve mathematics: Weierstrass curves over finite fields $\mathbb{F}_p$, group addition law, chord-and-tangent formulas, and order calculation via Schoof's algorithm.
- Twisted Edwards curves and Curve25519 (Ed25519 signatures, X25519 key exchange); constant-time ladder implementations.
- Bilinear pairings: Weil and Tate pairings over pairing-friendly curves (BN254, BLS12-381); Identity-Based Encryption (IBE) and short BLS signatures.

#### Module 5: Post-Quantum Cryptography & Lattice Foundations
- The quantum threat to classical public-key cryptography (Shor's algorithm).
- Geometry of numbers: lattices, Shortest Vector Problem (SVP), and Closest Vector Problem (CVP); the LLL basis reduction algorithm.
- Learning With Errors (LWE) and Ring-LWE: average-case to worst-case lattice reductions.
- NIST post-quantum standardization algorithms: ML-KEM (Kyber) and ML-DSA (Dilithium).

---

### Course 2: Systems Security, Binary Exploitation & Protocol Verification (MIT 6.1600/6.858 + pwn.college)

This course explores memory corruption vulnerabilities, binary exploitation, operating system isolation mechanisms, microarchitectural side-channels, and secure protocol design.

#### Module 1: Memory Corruption & Binary Exploitation
- The x86-64 runtime stack: stack frames, calling conventions, return addresses, and buffer overflows.
- Defeating stack protections: stack canaries, non-executable stack (DEP/NX), and Address Space Layout Randomization (ASLR).
- Return-Oriented Programming (ROP) and Jump-Oriented Programming (JOP): gadget discovery, gadget chaining, and constructing arbitrary shellcode execution without code injection.

#### Module 2: Heap Internals & Advanced Heap Exploitation
- Modern dynamic memory allocators (glibc `ptmalloc`): chunks, bins (fastbins, tcache, unsorted bin, small/large bins), and free lists.
- Heap exploitation techniques: Use-After-Free (UAF), double free, fastbin dup, tcache poisoning, overlapping chunks, and House-of-Force techniques.
- Format string vulnerabilities: arbitrary memory read and write primitives via `%n`.

#### Module 3: Kernel Exploitation & Hardware Isolation
- Privilege boundaries: User mode (Ring 3) vs Kernel mode (Ring 0); syscall entry/exit pathways.
- Kernel vulnerability patterns: NULL pointer dereference in kernel space, kernel heap pool spraying, and dirty COW/pipe vulnerabilities.
- Bypassing kernel mitigations: SMEP (Supervisor Mode Execution Prevention), SMAP (Supervisor Mode Access Prevention), and KASLR.
- Hardware isolation: ARM TrustZone, Intel SGX secure enclaves, and confidential computing primitives.

#### Module 4: Microarchitectural Side-Channels & Hardware Attacks
- CPU cache architecture side-channels: Flush+Reload, Prime+Probe, and Evict+Time.
- Speculative execution attacks: Spectre (branch target injection, bounds check bypass) and Meltdown (rogue data cache load).
- Power analysis and fault injection: Differential Power Analysis (DPA), clock glitching, and rowhammer DRAM disturbance attacks.
- Constant-time software engineering: branchless arithmetic, avoiding secret-dependent memory indexing, and automated verification with `ctgrind` / `dudect`.

#### Module 5: Modern Cryptographic Protocols & Zero-Knowledge Systems
- Transport Layer Security (TLS 1.3): cryptographic handshake, 0-RTT mode, forward secrecy, and session ticket security.
- End-to-End Encrypted Messaging: The Double Ratchet algorithm (Signal protocol), header encryption, and out-of-order message handling.
- Zero-Knowledge Proofs: interactive proofs, Fiat-Shamir heuristic, zk-SNARKs (Groth16, PLONK), and arithmetization over Rank-1 Constraint Systems (R1CS).

---

## 📑 Seminal Papers & Advanced Textbooks

- **Diffie, W., & Hellman, M. (1976).** *New Directions in Cryptography*. IEEE Transactions on Information Theory, 22(6), 644–654.
- **Goldwasser, S., & Micali, S. (1984).** *Probabilistic Encryption*. Journal of Computer and System Sciences, 28(2), 270–299.
- **Boneh, D., & Shoup, V. (2023).** *A Graduate Course in Applied Cryptography*. Version 0.6 (Free Monograph).
- **Katz, J., & Lindell, Y. (2020).** *Introduction to Modern Cryptography, 3rd Edition*. CRC Press.
- **Anderson, R. (2020).** *Security Engineering: A Guide to Building Dependable Distributed Systems, 3rd Edition*. Wiley.

---

## 🛠️ Progressive Labs

### Lab 1: CBC Bit-Flipping, Padding Oracle & Bleichenbacher Attacks
- **Objective:** Implement practical cryptographic attacks against vulnerable symmetric and asymmetric implementations (solving Cryptopals Sets 1 through 4).
- **Deliverables:**
  - Automated Python / C script exploiting CBC byte-flipping to forge admin session cookies.
  - Side-channel padding oracle exploit decrypting ciphertext without the key.
  - Chosen-ciphertext Million-Message attack against PKCS#1 v1.5 RSA encryption.
- **Acceptance Criteria:**
  - The test suite executes automated exploit attacks against mock server endpoints, recovering 100% of encrypted plaintexts within 10,000 oracle queries.
  - All exploits must run with zero false-negative failures across 100 randomized session keys.

### Lab 2: Return-Oriented Programming (ROP) and Kernel Privilege Escalation
- **Objective:** Construct a multi-stage binary exploit against an x86-64 binary hardened with full ASLR, NX, and stack canaries, followed by a local kernel privilege escalation exploit in a QEMU VM.
- **Deliverables:**
  - Exploit script leaking memory addresses via format string or buffer over-read to defeat ASLR.
  - ROP chain invoking `mprotect` or popping registers to execute `execve("/bin/sh")`.
  - Kernel module vulnerability exploit overwriting `cred` structure to gain UID 0.
- **Acceptance Criteria:**
  - Exploit must successfully spawn an interactive root shell deterministically across 50 consecutive runs without crashing the parent operating system kernel.
  - Binary analysis verified using GDB, `pwntools`, and `checksec`.

### Lab 3: Zero-Knowledge Range Proof Implementation via Bulletproofs
- **Objective:** Implement a non-interactive zero-knowledge range proof in Rust/Python using inner-product arguments, proving $v \in [0, 2^{64}-1]$ without revealing the secret value $v$.
- **Deliverables:**
  - Cryptographic module computing Pedersen commitments $V = vG + \gamma H$.
  - Bulletproof prover and verifier utilizing the Fiat-Shamir transformation over the Ristretto group.
- **Acceptance Criteria:**
  - Verifier successfully accepts valid proofs and rejects out-of-range commitments ($v \ge 2^{64}$) with false-acceptance probability $< 2^{-128}$.
  - Range proof generation must complete in $< 15 \text{ ms}$ and verification in $< 5 \text{ ms}$ on single-thread CPU.

---

## 🏆 Capstone Build Deliverable

### End-to-End Audited Encrypted Messaging Protocol with Post-Quantum Hybrid KEM

A secure, multi-party end-to-end encrypted messaging engine written in Rust or C99 implementing the Double Ratchet protocol combined with a post-quantum hybrid key encapsulation mechanism (X25519 + ML-KEM/Kyber-768).

```text
+-----------------------------------------------------------------------------------+
|                        AUDITED SECURE MESSAGING STACK                             |
|                                                                                   |
|  [ Alice Identity Key ] + [ ML-KEM Keypair ] <== Public Directory ==> [ Bob Keys ]|
|            |                                                               |      |
|            v                                                               v      |
|  [ Hybrid X3DH / Kyber Handshake ] ------------ Network ------------> [ Handshake ]
|            |                                                               |      |
|            v                                                               v      |
|  [ Double Ratchet DH Engine ] <--- Constant-Time Crypto ---> [ Double Ratchet DH ]|
|            |                                                               |      |
|            v                                                               v      |
|  [ Symmetric KDF Chain ] ---------> [ AES-256-GCM / ChaCha20 ] ---> [ Plaintext ] |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Hybrid Key Exchange:** Extended Triple Diffie-Hellman (X3DH) augmented with NIST FIPS 203 ML-KEM (Kyber-768), guaranteeing post-quantum forward secrecy against harvest-now-decrypt-later adversaries.
2. **Double Ratchet Engine:** Continuous Diffie-Hellman ratchet step per message turn coupled with a symmetric-key KDF ratchet generating single-use ephemeral message encryption keys.
3. **High-Assurance Hardening:** Strict constant-time cryptographic primitives verified via `dudect` (zero timing side-channels); zero dynamic memory leaks verified via AddressSanitizer/Valgrind; out-of-order packet replay protection via sliding-window bitmasks.

#### Verification & Acceptance Criteria
- **Protocol Test Vectors:** Must successfully pass all official Signal Double Ratchet test vectors and NIST ML-KEM known-answer test (KAT) vectors.
- **Constant-Time Verification:** Statistical hypothesis testing via `dudect` over $10^6$ sample iterations confirms failure to reject the null hypothesis ($t$-statistic $|t| < 4.5$), proving absence of timing side-channels in cryptographic operations.
- **Test Commands:**
  ```bash
  # Execute unit tests and known answer test (KAT) vectors
  cargo test --release
  # Verify constant-time execution properties
  cargo bench --bench dudect_constant_time
  # Run memory safety checks under Miri
  cargo miri test
  ```

---

## 🧭 Navigation & Degree Pathway
- **Curriculum Hub:** [[01 - Curriculum/Specializations/Specializations Hub|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[01 - Curriculum/Year 4 - Specialization/26 - Specialization A1|Block 26 - Specialization A1]] and Course 2 binds to [[01 - Curriculum/Year 4 - Specialization/28 - Specialization A2|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[01 - Curriculum/Year 4 - Specialization/29 - Specialization B1|Block 29 - Specialization B1]] and Course 2 binds to [[01 - Curriculum/Year 5 - MEng/31 - Specialization B2|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]]
