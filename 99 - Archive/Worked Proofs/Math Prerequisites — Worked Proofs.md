---
title: "P3 - Math Prerequisites — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# P3 - Math Prerequisites — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Math Prerequisites]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Math Prerequisites]] · [[Worked Proofs Index]]

---

- **Proof of the Irrationality of $\sqrt{2}$ (Proof by Contradiction):**
  Assume for contradiction that $\sqrt{2} \in \mathbb{Q}$. Then $\sqrt{2} = \frac{p}{q}$ for coprime integers $p, q \in \mathbb{Z}$ with $q \ne 0$ and $\gcd(p, q) = 1$.
  Squaring both sides yields $2 = \frac{p^2}{q^2} \implies p^2 = 2q^2$.
  Thus $p^2$ is even, which implies $p$ is even (since if $p = 2k+1$, $p^2 = 4k^2+4k+1 = 2(2k^2+2k)+1$, which is odd).
  Let $p = 2m$ for some $m \in \mathbb{Z}$. Substituting gives $(2m)^2 = 2q^2 \implies 4m^2 = 2q^2 \implies q^2 = 2m^2$.
  Thus $q^2$ is even, which implies $q$ is even.
  Since both $p$ and $q$ are even, $2 \mid \gcd(p, q)$, contradicting $\gcd(p, q) = 1$.
  Therefore, $\sqrt{2} \notin \mathbb{Q}$. $\blacksquare$
