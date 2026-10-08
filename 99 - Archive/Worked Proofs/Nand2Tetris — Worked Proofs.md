---
title: "04 - Nand2Tetris — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 04 - Nand2Tetris — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Nand2Tetris]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Nand2Tetris]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Boolean Completeness of NAND:** Constructive proof that $\{\text{NAND}\}$ forms a functionally complete set of Boolean operators: $\text{NOT}(x) = x \text{ NAND } x$, $\text{AND}(x, y) = \text{NOT}(x \text{ NAND } y)$, $\text{OR}(x, y) = (\text{NOT } x) \text{ NAND } (\text{NOT } y)$.
- **ALU Control Line Semantics:** Derivation of 16-bit Hack ALU truth table mapping 6 control bits $(zx, nx, zy, ny, f, no)$ to fundamental operations $(0, 1, -1, x, y, -x, -y, x+y, x-y, x\&y, x|y)$.
- **Sequential Feedback & D-Flip-Flop Invariant:** State storage via master-slave clocking, race-condition elimination, and synchronous register load semantics.
- **Two-Tier VM Architecture:** Translation of high-level procedural syntax into stack-based VM operations (`push`, `pop`, `add`, `call`, `return`) and target assembly sequences.

---

### 1. Functional Completeness of the Sheffer Stroke ($\{\text{NAND}\}$)
**Theorem:** The singleton Boolean operator set consisting solely of the NAND gate ($\uparrow$, where $x \uparrow y = \neg(x \land y)$) is functionally complete. That is, for every $n \ge 1$, any arbitrary Boolean function $f: \{0, 1\}^n \to \{0, 1\}$ can be synthesized exclusively from finite compositions of NAND gates.

#### Step-by-Step Derivation & Proof:
1. **Basis of Functional Completeness (DNF Construction):**
   By the fundamental theorem of Boolean algebra, any Boolean function $f(x_1, \dots, x_n)$ can be expressed in Disjunctive Normal Form (DNF):
   $$f(x_1, \dots, x_n) = \bigvee_{\substack{\mathbf{a} \in \{0, 1\}^n \\ f(\mathbf{a}) = 1}} \left( \bigwedge_{j=1}^n x_j^{a_j} \right)$$
   where $x_j^1 = x_j$ and $x_j^0 = \neg x_j$.
   Consequently, the standard logical signature $\mathcal{S}_0 = \{\neg, \land, \lor\}$ is functionally complete.

2. **Reduction from $\{\neg, \land, \lor\}$ to $\{\neg, \land\}$:**
   By De Morgan's duality laws, disjunction ($\lor$) can be directly synthesized from negation ($\neg$) and conjunction ($\land$):
   $$x \lor y = \neg(\neg x \land \neg y)$$
   Thus, the reduced set $\mathcal{S}_1 = \{\neg, \land\}$ is functionally complete.

3. **Constructive Synthesis of $\mathcal{S}_1$ via $\{\text{NAND}\}$:**
   We construct $\neg$ and $\land$ using solely the Sheffer stroke operation $\uparrow$:
  - **Synthesis of NOT Gate ($\neg x$):**
    By idempotence of Boolean conjunction, $x \land x = x$. Therefore:
    $$x \uparrow x = \neg(x \land x) = \neg x$$
  - **Synthesis of AND Gate ($x \land y$):**
    By double negation, $x \land y = \neg(\neg(x \land y))$. Substituting the NAND definition:
    $$(x \uparrow y) \uparrow (x \uparrow y) = \neg(x \uparrow y) = \neg(\neg(x \land y)) = x \land y$$
  - **Synthesis of OR Gate ($x \lor y$):**
    Substitute the synthesized NOT gates into De Morgan's identity:
    $$x \lor y = \neg(\neg x \land \neg y) = (\neg x) \uparrow (\neg y) = (x \uparrow x) \uparrow (y \uparrow y)$$

4. **Algebraic Confirmation via Post's Functional Completeness Theorem:**
   By Emil Post's criterion (1941), a set of Boolean operators is functionally complete if and only if it is not a subset of any of the five maximal closed clones:
  - **$T_0$ (0-preserving):** $0 \uparrow 0 = \neg(0 \land 0) = 1 \ne 0 \implies \uparrow \notin T_0$.
  - **$T_1$ (1-preserving):** $1 \uparrow 1 = \neg(1 \land 1) = 0 \ne 1 \implies \uparrow \notin T_1$.
  - **$S$ (Self-dual):** $f^*(x, y) = \neg f(\neg x, \neg y) = \neg(\neg x \uparrow \neg y) = \neg(x \lor y) = x \land y \ne x \uparrow y \implies \uparrow \notin S$.
  - **$M$ (Monotone):** Consider ordered tuples $(0, 0) \le (1, 1)$. But $0 \uparrow 0 = 1 > 0 = 1 \uparrow 1 \implies \uparrow \notin M$.
  - **$L$ (Affine / Linear):** In the Galois field $\mathbb{F}_2$, the algebraic normal form of NAND is:
    $$x \uparrow y = 1 \oplus (x \cdot y)$$
    which contains the nonlinear second-degree monomial $x \cdot y \implies \uparrow \notin L$.
   Since $\{\uparrow\}$ belongs to none of the five maximal clones, it generates the full clone of all Boolean functions $\mathcal{BF}$, proving functional completeness. $\blacksquare$
