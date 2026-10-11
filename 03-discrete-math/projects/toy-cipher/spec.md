---
title: "Project: Toy Cipher"
id: "MOD03-PRJ-toy-cipher"
type: "project"
module: "03-discrete-math"
phase: "B"
order: 540
prerequisites: [MOD03-U5, FND-MA-PRJ-prime-factory, MOD02-LAB01]
artifact: "postcard: a toy public-key system (key generation, encryption, signatures) built from your own number theory — and three working attacks on it"
deliverable: "Proofs of correctness in the Proof Journal + 'Why textbook RSA is broken' report (2 pages) + short demo"
---

# Project: Toy Cipher

| | |
| :-- | :-- |
| **Module** | 03 Discrete Math |
| **Prerequisites** | Unit 5 (modular arithmetic); [Prime Factory](../../../00-foundations/math/projects/prime-factory/spec.md); Module 02 Lab 01 (fast exponentiation) |
| **You build** | `postcard`, a toy version of RSA public-key cryptography, built entirely from number theory you implement and prove yourself: extended Euclid, modular inverses, fast modular powers, prime generation, key pairs, encryption, and signatures. Two characters, Ada and Bram, send each other postcards. Then **you play the attacker** and break the system three different ways |
| **Deliverable** | Proofs in your Proof Journal, a 2-page report, and a demo |

> ⚠️ **This is a learning toy, not real cryptography.** Never use it — or any cryptography you wrote yourself — to protect real secrets. Real systems use carefully reviewed libraries, large keys, padding schemes, and defences against attacks far subtler than the ones here. Part of this project is seeing *why*.

---

## Why this matters

Public-key cryptography is one of the most surprising ideas in computing: you can publish a key that lets *anyone* lock a message that *only you* can unlock. It protects nearly every connection your browser makes. And underneath, it's Unit 5: modular arithmetic, inverses, and one theorem from 1640 (Fermat's little theorem).

You'll build every piece, **prove** it correct, and then break it — which teaches more about security than building alone ever could. In [Module 09](../../../09-networking/overview.md) you'll meet the real thing (TLS) from the outside; in your capstone you might use real cryptographic libraries correctly.

**Real-world analogs:** RSA, digital signatures, certificate checks in browsers, SSH keys.

---

## Milestones

### Milestone 1 — The number-theory core

Write `ntheory.py`:

```python
def egcd(a, b) -> tuple[int, int, int]:   # returns (g, x, y) with a*x + b*y == g == gcd(a, b)
def modinv(a, m) -> int:                  # x with (a * x) % m == 1; raise ValueError if gcd(a, m) != 1
def modpow(b, e, m) -> int:               # b**e % m by square-and-multiply, never computing b**e itself
```

- **Extended Euclid** keeps track of how each remainder is a combination of the original a and b. Work three examples **by hand** first in a table (one row per step: quotient, remainder, x, y) [S]. The final row gives **Bézout's identity**: gcd(a, b) = ax + by.
- **Modular inverse:** if gcd(a, m) = 1, then ax + my = 1, so ax ≡ 1 (mod m): x is the inverse.
- **Modular exponentiation:** the iterative square-and-multiply loop. Keep numbers small by reducing mod m after every multiplication. Write its **loop invariant** (Lab 02) in a comment and as an `assert` in test mode.

**Tests:** compare with Python's built-ins as second witnesses — `pow(b, e, m)` and `pow(a, -1, m)` — on 10,000 random cases; Bézout's identity holds for every `egcd` result; `modinv` raises for non-coprime inputs.

**Proof Journal entries (required):** (1) correctness of extended Euclid (invariant: at every step, each remainder equals a·x + b·y for the tracked x, y); (2) "a has an inverse mod m if and only if gcd(a, m) = 1" (both directions!); (3) correctness of square-and-multiply.

**Done when:** tests pass and the three proofs are written.

### Milestone 2 — Primes, Fermat, and a liar

**Fermat's little theorem:** if p is prime and p doesn't divide a, then a^(p−1) ≡ 1 (mod p).

1. **Check it** with `modpow` for every a from 1 to p − 1, for every prime p < 200 (your sieve).
2. **The Fermat test:** to test whether n is prime, pick random a and check a^(n−1) ≡ 1 (mod n). If not, n is definitely composite. If so, n is *probably* prime.
3. **Meet a liar:** 561 = 3 × 11 × 17 is not prime, yet a^560 ≡ 1 (mod 561) for **every** a coprime to 561. It's a **Carmichael number**. Find all Carmichael numbers below 100,000 by brute force (there are 16). [W] What does this tell you about the Fermat test?
4. **Miller–Rabin** (the test real systems use) fixes the liar problem. Read its description (MCS or any number-theory text), implement it, and verify it correctly rejects every Carmichael number you found.
5. `random_prime(bits)`: random odd numbers of the given size until Miller–Rabin says prime (with 40 rounds).

**Done when:** Fermat checked, Carmichael list found, Miller–Rabin rejects all of them, and `random_prime(512)` returns quickly. (Compare: your trial-division `is_prime` from Prime Factory on a 512-bit number would take longer than the age of the universe — M07's scientific notation will tell you by how much.)

**Proof Journal entry:** Fermat's little theorem. (A readable proof: the numbers a, 2a, …, (p−1)a mod p are just 1, …, p−1 in some order — prove that — so their product gives a^(p−1)(p−1)! ≡ (p−1)! (mod p); cancel (p−1)!, which is allowed because it's coprime to p.)

### Milestone 3 — Keys, encryption, and postcards

**Key generation [S]:**
1. Pick two random primes p and q of the same size (start with 16 bits each; later 512).
2. n = p·q. φ = (p − 1)(q − 1).
3. Choose e with gcd(e, φ) = 1 (65,537 is the common choice; if it fails, pick another prime).
4. d = modinv(e, φ).
5. **Public key:** (n, e). **Private key:** (n, d). Keep p, q, φ secret (and in a real system, destroy them).

**Encrypt** a number m < n: c = mᵉ mod n. **Decrypt:** m = cᵈ mod n.

**Postcards:** text → bytes (UTF-8) → split into blocks small enough that each block, read as a number, is less than n → encrypt each block. A postcard file:

```
POSTCARD v1
from: ada
to: bram
blocks: 3
3a9f0c…
b81e44…
07dd2a…
```

CLI: `postcard keygen ada --bits 512`, `postcard send ada bram "Meet at the lighthouse at dawn."`, `postcard read bram card.txt`.

**Tests:** for 1,000 random m < n, decrypt(encrypt(m)) = m; postcards round-trip text including non-English characters; small hand-computed example: p = 61, q = 53 (n = 3233, φ = 3120), e = 17 → d = 2753; encrypt m = 65 → c = 2790; decrypt back to 65. (Do this one entirely by hand first, using your modpow table method.)

**Proof Journal entry:** RSA correctness: for m with gcd(m, n) = 1, (mᵉ)ᵈ ≡ m (mod n). (Use ed = 1 + kφ and Euler's theorem — or prove it mod p and mod q separately with Fermat, then combine. Note the gcd(m, n) = 1 assumption; the full result holds for all m, and the Chinese Remainder Theorem is the tool for that — a stretch proof.)

**Done when:** Ada and Bram exchange postcards with 512-bit primes, and the hand example checks out.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *how a public key can lock something only the private key opens* — plain words first, then the math.

### Milestone 4 — Signatures

A **signature** proves who wrote a message and that it wasn't changed.
1. Hash the postcard text (`hashlib.sha256` — allowed; hashing is Module 05 and beyond) and read the hash as a number h mod n.
2. **Sign** with the private key: s = hᵈ mod n.
3. **Verify** with the public key: check sᵉ mod n = h.
4. Demonstrate tampering: change one character of a signed postcard; verification fails.

**Done when:** signed postcards verify, and tampered ones don't.

### Milestone 5 — Break it (three attacks)

Now play Eve, the eavesdropper. Write each attack as a script, and explain it in the report.

1. **Factor the key.** With 16-bit primes, n has about 32 bits. Use your Prime Factory `crack(n)` to find p and q, compute d, and read every postcard. Time it for 16, 20, 24, 28, 32-bit primes. Extrapolate to 512 bits (and compare with the age of the universe). Then implement **Pollard's rho** factoring and see how much further you get.
2. **Guess the message.** Bram only ever replies `YES` or `NO`. Textbook RSA is **deterministic**: the same message always encrypts to the same block. Eve encrypts both possible answers with Bram's public key and compares. She reads the reply without breaking anything. [W] Why does adding random padding before encryption stop this?
3. **The cube-root attack.** Generate keys with **e = 3** (when gcd(3, φ) = 1). Encrypt a short message m without padding, where m³ < n. Then c = m³ exactly — the "mod n" never wrapped around — so Eve takes the ordinary integer cube root of c. Write an **integer cube root by binary search** (Growth and Halving Lab) and recover the message.

**Done when:** all three attacks work, with a timing table for attack 1.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *the system was mathematically correct (you proved it). So why was it insecure?* (Correctness ≠ security: this is one of the deepest lessons in engineering.)

---

## Testing guidance

- **Second witnesses:** Python's `pow` for modpow and inverses; `sympy.isprime` (optional) for primality.
- **Small hand-computed keys** (p = 61, q = 53) as fixtures.
- **Property tests:** round trips for random messages; Bézout for random pairs; signatures fail for random tampering.

## Common pitfalls

- **Computing `b**e` then `% m`.** For big e that's a number with millions of digits. Always reduce as you go.
- **Message bigger than n.** Encryption silently loses information. Check and split.
- **Leading zero bytes** lost when converting blocks to numbers and back. Store each block's byte length, or use a fixed block size.
- **Bad randomness.** For this toy, `random.SystemRandom()` or the `secrets` module — never a seeded `random.Random` — for key generation (but *do* use seeds in tests).

## Communication deliverable

1. **Proof Journal entries:** extended Euclid, inverse iff coprime, square-and-multiply, Fermat's little theorem, RSA correctness.
2. **Report (2 pages, E10 level): "Why textbook RSA is broken."** For each attack: what Eve does, why it works, and what real systems do instead (padding, large keys, careful parameter choice). End with the correctness-vs-security lesson.
3. **Demo:** Ada sends Bram a signed postcard; Eve breaks a small key and reads it; Eve reads a YES/NO reply without factoring.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 3, write the keygen steps from memory |
| **F** | Public-key locking in plain words |
| **W** | Carmichael numbers and the Fermat test; padding; correctness vs security |
| **S** | Extended Euclid tables; keygen subgoals |
| **I** | Proofs, code, and attacks interleaved |
| **T** | Proofs, report, demo |

## Stretch goals

- **Chinese Remainder Theorem:** implement CRT, use it to decrypt 3–4× faster (real libraries do), and prove RSA correct for *all* m.
- **Diffie–Hellman key exchange:** Ada and Bram agree on a shared secret over a public channel. Then show why an attacker in the middle breaks it without authentication.
- **Real tools:** generate an RSA key with `openssl genrsa` and inspect its numbers with `openssl rsa -text`. Find n, e, d, p, q.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Number theory core | All three functions, witnessed tests, invariants | Works | Fails on big numbers |
| Primality | Fermat checked, Carmichaels found, Miller–Rabin | Fermat only | Trial division only |
| RSA and postcards | 512-bit keys, hand example, round trips, signatures | Small keys | Missing |
| Attacks | All three, with timing and extrapolation | Two | One |
| Proofs | Five proofs, clear and complete | Three | Fewer |
| Communication | Report and demo | One | Neither |

**Done when:** every area at least 2; Proofs and Attacks at 3.

## Connections

- **Back:** M04 (primes, GCD), M07 (exponents, scientific notation), M11 (log of key size vs work), Prime Factory, Growth and Halving Lab (binary search).
- **Forward:** Module 05 (hash functions), Module 09 (TLS in practice; checksums vs signatures), and any later security work.

> **Originality note:** the postcard system, milestone order, and attack set were designed for this curriculum. RSA, Fermat, Miller–Rabin, and Pollard's rho are classic published methods.
