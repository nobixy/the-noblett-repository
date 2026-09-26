---
title: "P4 - Programming On-Ramp — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# P4 - Programming On-Ramp — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[P4 - Programming On-Ramp]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[P4 - Programming On-Ramp]] · [[Worked Proofs Index]]

---

- **BST Invariant & Complexity:** For every node $x$, all keys in the left subtree are $< \text{key}(x)$ and all keys in the right subtree are $> \text{key}(x)$. Search, insertion, and deletion complexity $\mathcal{O}(h)$ where $h$ is tree height.
- **Hash Table Collision Bounds:** Expected search time under Simple Uniform Hashing is $\mathcal{O}(1 + \alpha)$ where load factor $\alpha = n/m$.
