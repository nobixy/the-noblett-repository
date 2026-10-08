---
title: "27 - Intensive Cryptopals or TLA+ — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 27 - Intensive Cryptopals or TLA+ — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Intensive Cryptopals or TLA+]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Intensive Cryptopals or TLA+]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **CBC Bit-Flipping & Padding Oracle Invariants:** Block cipher feedback mechanics ($C_i = E_K(P_i \oplus C_{i-1})$) and mathematical derivation of plaintext byte leakage from PKCS#7 validity error oracles.
- **Bleichenbacher's RSA Padding Oracle:** Multi-interval refinement of secret message $m = c^d \pmod N$ under PKCS#1 v1.5 compliance oracles using conforming multiplier intervals $[s_{\min}, s_{\max}]$.
- **Temporal Logic of Actions (TLA+):** State predicate invariants ($\text{Init} \land \Box[\text{Next}]_v \land \text{Fairness}$), safety proofs via inductive step verification ($\text{Inv} \land \text{Next} \implies \text{Inv}'$), and liveness verification via leadsto ($\leadsto$).
- **Learning With Errors (LWE) Lattice Hardness:** Reduction from Shortest Vector Problem (SVP) over lattices to search/decision LWE in post-quantum cryptography.

---

### 1. Vaudenay's CBC Mode Chosen-Ciphertext Padding Oracle Decryption Theorem
**Theorem (Vaudenay, Eurocrypt 2002):** Let $(E_K, D_K)$ be a symmetric block cipher with block size $B$ bytes operating in Cipher Block Chaining (CBC) mode with PKCS#7 padding:
$$P_i = D_K(C_i) \oplus C_{i-1} \quad (i \ge 1, \text{ with } C_0 = \text{IV})$$
Let $\mathcal{O}: (\{0, 1\}^B)^+ \to \{0, 1\}$ be a chosen-ciphertext padding oracle that decrypts arbitrary ciphertext blocks and returns $1$ if the resulting plaintext terminates in valid PKCS#7 padding, and $0$ otherwise.
**Theorem Statement:** An active adversary with black-box query access to $\mathcal{O}$, without knowledge of the cryptographic secret key $K$, can decrypt any ciphertext block $C_i$ byte-by-byte using at most:
$$Q \le 256 \times B$$
oracle queries, completely breaking semantic confidentiality in linear time $\mathcal{O}(B)$ per block.

#### Step-by-Step Derivation & Proof:
1. **PKCS#7 Padding Specification:**
   For a cipher with block size $B$ bytes, padding appends $p$ bytes, each having value $p$, where $1 \le p \le B$:
   $$\text{Valid endings} \in \{ [0x01], \; [0x02, 0x02], \; [0x03, 0x03, 0x03], \; \dots, \; [\underbrace{B, B, \dots, B}_{B \text{ bytes}}] \}$$

2. **Decomposition via Intermediate State ($I_i$):**
   Define the intermediate decryption state $I_i = D_K(C_i)$.
   Under standard CBC decryption, the plaintext is:
   $$P_i = I_i \oplus C_{i-1}$$
   Because $C_{i-1}$ is transmitted publicly, recovering $I_i$ is strictly equivalent to recovering $P_i$.

3. **Chosen-Ciphertext Attack Prefix Construction:**
   To decrypt target block $C_i$, the adversary crafts a synthetic two-block ciphertext:
   $$C' = R \parallel C_i, \qquad R = [r_1, r_2, \dots, r_B] \in \{0, 1\}^B$$
   The oracle decrypts $C'$:
   $$P'_2 = D_K(C_i) \oplus R = I_i \oplus R$$
   The adversary controls $R$ directly, modifying individual bytes of $P'_2$.

4. **Inductive Byte-by-Byte Decryption (Backward from byte $B$ to 1):**
   We prove by induction that each byte $I_{i, j}$ for $j \in \{B, B-1, \dots, 1\}$ can be uniquely determined in at most 256 queries.
  - **Base Case (Recovering last byte $j = B$, targeting padding $p = 1$):**
    Choose arbitrary prefix bytes $r_1, \dots, r_{B-1}$.
    Vary candidate byte $r_B \in \{0, 1, \dots, 255\}$ and query $\mathcal{O}(R \parallel C_i)$.
    The oracle returns $\mathcal{O} = 1$ when the decrypted plaintext ends with a valid pad, almost certainly $P'_{2, B} = 0x01$.
    (To eliminate accidental multi-byte padding like $0x02, 0x02$, perturb byte $r_{B-1}$; if the oracle still returns 1, the pad is guaranteed to be $0x01$).
    Since $P'_{2, B} = I_{i, B} \oplus r_B = 0x01$, solving for the intermediate byte gives:
    $$I_{i, B} = r_B \oplus 0x01$$
    The original plaintext byte is immediately recovered:
    $$P_{i, B} = I_{i, B} \oplus C_{i-1, B} = (r_B \oplus 0x01) \oplus C_{i-1, B}$$
  - **Inductive Step (Recovering byte $j$ from $B-1$ down to 1):**
    Assume intermediate bytes $I_{i, j+1}, I_{i, j+2}, \dots, I_{i, B}$ have been recovered.
    To isolate byte $j$, target padding value $p = B - j + 1$.
    Configure the known suffix bytes of $R$ so that the decrypted suffix equals $p$:
    $$r_k = I_{i, k} \oplus p \quad \forall k \in \{j+1, \dots, B\}$$
    Now sweep candidate byte $r_j \in \{0, 1, \dots, 255\}$ while querying $\mathcal{O}(R \parallel C_i)$.
    The oracle returns $1$ if and only if byte $j$ decrypts to $p$:
    $$P'_{2, j} = I_{i, j} \oplus r_j = p \implies I_{i, j} = r_j \oplus p$$
    The original plaintext byte is then:
    $$P_{i, j} = I_{i, j} \oplus C_{i-1, j} = (r_j \oplus p) \oplus C_{i-1, j}$$

5. **Query Complexity Bound:**
   Each byte $j$ requires searching a space of $2^8 = 256$ possible values.
   For a block of $B$ bytes:
   $$Q_{\text{block}} = \sum_{j=1}^B 256 = 256 \cdot B$$
   For standard AES ($B = 16$), decrypting an entire block requires at most $256 \times 16 = 4096$ queries (on average $128 \times 16 = 2048$ queries).
   For a message consisting of $M$ ciphertext blocks, total decryption requires at most $256 B M = \mathcal{O}(|C|)$ queries without brute-forcing the $2^{128}$ or $2^{256}$ keyspace. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[Paper Reading Hub|Paper Reading Hub]])

The following foundational paper from the [[Paper Reading Hub|Paper Reading Hub]] is assigned to Block 27. Analyze using the Keshav Three-Pass Methodology:

1. **"On Lattices, Learning with Errors, Random Linear Codes, and Cryptography"** (Oded Regev, 2005)
    - *Venue:* STOC '05 (Paper 33 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Reduction from worst-case lattice problems (GapSVP, SIVP) to average-case Learning With Errors (LWE), foundational to post-quantum cryptography.
    - *Reading Guidance:* Focus Pass 2 on the quantum reduction step between discrete Gaussian distributions on the dual lattice and continuous Gaussian perturbations.
