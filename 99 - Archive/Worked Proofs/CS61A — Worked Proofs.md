---
title: "01 - CS61A — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 01 - CS61A — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[B01 - CS61A|CS61A]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[B01 - CS61A|CS61A]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Environment Model of Evaluation:** Frame trees, lexical scoping invariants, parent pointers, and variable lookup semantics under mutable assignment (`nonlocal`).
- **Higher-Order Function Composition:** Currying, Church numerals, and combinators ($Y = \lambda f.(\lambda x.f(x\,x))(\lambda x.f(x\,x))$).
- **Tree Recursion & Memoization:** Recurrence relations for tree traversal, memoization tables, and state-space pruning.
- **Eval/Apply Mutual Recursion:** The fundamental interpreter cycle where `scheme_eval` evaluates expressions within an environment and dispatches to `scheme_apply`, which binds parameters and creates child frames.

---

### 1. Curry's Paradoxical Fixed-Point Combinator Theorem ($Y$-Combinator)
**Theorem (Fixed-Point Theorem of $\lambda$-Calculus):** In the untyped lambda calculus, every term $F$ has a fixed point. That is, there exists a closed lambda term (the Curry $Y$-combinator):
$$Y = \lambda f. (\lambda x. f (x \, x)) (\lambda x. f (x \, x))$$
such that for any lambda term $F$:
$$Y F \equiv_\beta F (Y F)$$
Consequently, any recursive function definition $f = F f$ can be solved without primitive recursion features.

#### Step-by-Step Derivation & Proof:
1. **Application of Combinator:**
   Apply $Y$ to an arbitrary lambda term $F$:
   $$Y F = \left( \lambda f. (\lambda x. f (x \, x)) (\lambda x. f (x \, x)) \right) F$$

2. **First $\beta$-Reduction:**
   Substitute argument $F$ for formal parameter $f$ in the outer abstraction body:
   $$Y F \to_\beta (\lambda x. F (x \, x)) (\lambda x. F (x \, x))$$

3. **Defining the Self-Application Generator:**
   Let $\omega_F = \lambda x. F (x \, x)$. The expression is then:
   $$\omega_F \omega_F = (\lambda x. F (x \, x)) \omega_F$$

4. **Second $\beta$-Reduction:**
   Evaluating the application $(\lambda x. F (x \, x)) \omega_F$ by substituting $\omega_F$ for $x$:
   $$(\lambda x. F (x \, x)) \omega_F \to_\beta F (\omega_F \omega_F)$$

5. **Equivalence Synthesis:**
   Expanding $\omega_F \omega_F$ back to its definition yields:
   $$\omega_F \omega_F = (\lambda x. F (x \, x)) (\lambda x. F (x \, x))$$
   which is the exact reduct of $Y F$. Thus:
   $$Y F \to_\beta (\lambda x. F (x \, x)) (\lambda x. F (x \, x)) \to_\beta F ((\lambda x. F (x \, x)) (\lambda x. F (x \, x))) \equiv_\beta F (Y F)$$
   Therefore, $Y F \equiv_\beta F (Y F)$, and $Y F$ is a fixed point of $F$.

6. **Call-by-Value Adaptation (The Applicative-Order $Z$-Combinator):**
   In strict applicative-order languages (such as Python or standard Scheme), evaluating $Y F$ directly causes an infinite evaluation loop because arguments are evaluated prior to function application.
   By applying $\eta$-expansion to delay the self-application, we define the call-by-value fixed-point combinator ($Z$):
   $$Z = \lambda f. (\lambda x. f (\lambda v. x \, x \, v)) (\lambda x. f (\lambda v. x \, x \, v))$$
   For any term $F$ and argument $v$:
   $$Z F v \to_\beta (\lambda x. F (\lambda v. x \, x \, v)) (\lambda x. F (\lambda v. x \, x \, v)) v \to_\beta F (\lambda v. (\omega_Z \omega_Z) v) v \equiv_\beta F (Z F) v \quad \blacksquare$$
