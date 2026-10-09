---
title: "05 - SICP — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 05 - SICP — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Cut - B05 - SICP|SICP]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Cut - B05 - SICP|SICP]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Substitution Model vs Environment Model:** Formal limitations of functional substitution under mutable assignment; introduction of explicit frame chains and mutable binding pairs.
- **Church-Turing Thesis & Metacircular Evaluation:** Equivalence of lambda calculus and Turing computability; self-interpreter expressibility and universal evaluation.
- **Normal-Order vs Applicative-Order Reduction:** Church-Rosser theorem implications, confluence of evaluation pathways, and delayed thunk memoization in the lazy evaluator.
- **Stream Processing & Infinite Data Structures:** Invariant preservation of coinductive stream generators ($S = s_0 \mathbin{::} \text{delay}(S')$) and lazy sieve of Eratosthenes.

---

### 1. The Church-Rosser Confluence Theorem for $\lambda$-Calculus
**Theorem (Church & Rosser, 1936):** Let $\to_\beta$ denote the one-step $\beta$-reduction relation on terms in untyped $\lambda$-calculus, and let $\to_\beta^*$ denote its reflexive-transitive closure. The relation $\to_\beta^*$ is confluent (satisfies the Diamond Property):
$$\forall M, M_1, M_2. \quad (M \to_\beta^* M_1 \land M \to_\beta^* M_2) \implies \exists M'. \quad (M_1 \to_\beta^* M' \land M_2 \to_\beta^* M')$$

**Corollary (Uniqueness of Normal Forms):** If a $\lambda$-term $M$ reduces to a $\beta$-normal form (a term containing no further $\beta$-redexes), that normal form is unique up to $\alpha$-equivalence. Consequently, applicative-order (eager) evaluation and normal-order (lazy) evaluation produce identical results whenever both terminate.

#### Step-by-Step Derivation & Proof (Tait & Martin-Löf Parallel Reduction):
1. **Parallel Reduction Definition ($\Rightarrow$):**
   One-step reduction $\to_\beta$ does not satisfy the one-step diamond property due to redex duplication. We define the *parallel reduction* relation $\Rightarrow$ inductively:
   $$\frac{}{x \Rightarrow x} \quad (\text{Var}) \qquad \frac{M \Rightarrow M'}{\lambda x. M \Rightarrow \lambda x. M'} \quad (\text{Abs})$$
   $$\frac{M \Rightarrow M' \quad N \Rightarrow N'}{M N \Rightarrow M' N'} \quad (\text{App}) \qquad \frac{M \Rightarrow M' \quad N \Rightarrow N'}{(\lambda x. M) N \Rightarrow M'[x \mapsto N']} \quad (\beta\text{-Parallel})$$

2. **Equivalence of Transitive Closures:**
   It is immediate that $M \to_\beta M' \implies M \Rightarrow M'$, and $M \Rightarrow M' \implies M \to_\beta^* M'$.
   Taking the reflexive-transitive closure of both relations:
   $$\Rightarrow^* \;=\; \to_\beta^*$$
   Therefore, proving confluence of $\Rightarrow$ guarantees confluence of $\to_\beta^*$.

3. **Maximal Parallel Reduct Function ($M^*$):**
   Define the complete development term $M^*$ recursively over term structure:
   $$x^* = x$$
   $$(\lambda x. M)^* = \lambda x. M^*$$
   $$(M N)^* = M^* N^* \quad (\text{if } M \text{ is not an abstraction})$$
   $$((\lambda x. M) N)^* = M^*[x \mapsto N^*]$$

4. **Lemma (Strong Parallel Diamond Property):**
   We claim that for any terms $M, M'$, if $M \Rightarrow M'$, then $M' \Rightarrow M^*$.
   We proceed by structural induction on the derivation of $M \Rightarrow M'$:
  - **Case Var ($x \Rightarrow x$):** $x^* = x$, so $x \Rightarrow x^*$.
  - **Case Abs ($M = \lambda x. P \Rightarrow \lambda x. P' = M'$):** By induction, $P' \Rightarrow P^*$. By rule (Abs), $\lambda x. P' \Rightarrow \lambda x. P^* = M^*$.
  - **Case App ($M = P Q \Rightarrow P' Q' = M'$ where $P$ is not an abstraction):** By induction, $P' \Rightarrow P^*$ and $Q' \Rightarrow Q^*$. By rule (App), $P' Q' \Rightarrow P^* Q^* = M^*$.
  - **Case $\beta$-Parallel ($M = (\lambda x. P) Q \Rightarrow P'[x \mapsto Q'] = M'$):**
    By inductive hypothesis, $P' \Rightarrow P^*$ and $Q' \Rightarrow Q^*$.
    By the Substitution Lemma for parallel reduction, if $P' \Rightarrow P^*$ and $Q' \Rightarrow Q^*$, then:
    $$P'[x \mapsto Q'] \Rightarrow P^*[x \mapsto Q^*] = M^*$$
   Hence, the condition $M' \Rightarrow M^*$ holds universally.

5. **Diamond Property & Transitive Confluence:**
   If $M \Rightarrow M_1$ and $M \Rightarrow M_2$, the lemma establishes that $M_1 \Rightarrow M^*$ and $M_2 \Rightarrow M^*$.
   Thus, $\Rightarrow$ satisfies the diamond property.
   By the classic Strip Lemma, if a relation satisfies the diamond property, its reflexive-transitive closure $\Rightarrow^*$ is confluent.
   Since $\Rightarrow^* = \to_\beta^*$, the reduction relation $\to_\beta^*$ is confluent.

6. **Uniqueness of Normal Forms:**
   Suppose $M \to_\beta^* N_1$ and $M \to_\beta^* N_2$ where $N_1$ and $N_2$ are normal forms.
   By confluence, $\exists M'$ such that $N_1 \to_\beta^* M'$ and $N_2 \to_\beta^* M'$.
   Because $N_1$ and $N_2$ contain zero $\beta$-redexes, no reduction steps can be taken from either term, requiring $N_1 = M' = N_2$. $\blacksquare$
