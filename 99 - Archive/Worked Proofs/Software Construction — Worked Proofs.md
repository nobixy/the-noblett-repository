---
title: "17 - Software Construction — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 17 - Software Construction — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[B17 - Software Construction|Software Construction]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[B17 - Software Construction|Software Construction]] · [[Worked Proofs Index]]

---

### 1. Static Single Assignment (SSA) Form & Dominance Frontiers
**Objective:** Construct minimal SSA form where every variable is assigned exactly once, and $\phi$-functions are placed at join points in the Control Flow Graph (CFG) $G = (V, E, s_0)$.

#### Formal Dominance Hierarchy:
1. **Dominance ($d \text{ dom } n$):** Node $d$ dominates $n$ if every directed path from entry node $s_0$ to $n$ in $G$ contains $d$.
2. **Strict Dominance ($d \text{ sdom } n$):** $d \text{ dom } n$ and $d \ne n$.
3. **Immediate Dominator ($idom(n)$):** The unique node $d$ that strictly dominates $n$ without strictly dominating any other strict dominator of $n$. The set of edges $\{(idom(n), n) \mid n \ne s_0\}$ forms the *dominator tree*.
4. **Dominance Frontier ($DF(X)$):** The set of all nodes $Y \in V$ such that $X$ dominates a predecessor of $Y$, but $X$ does not strictly dominate $Y$:
   $$DF(X) = \{ Y \in V \mid \exists P \in Pred(Y): X \text{ dom } P \land \neg(X \text{ sdom } Y) \}$$

#### Iterated Dominance Frontier ($IDF$) & Minimal $\phi$-Placement:
For a set of definition nodes $S \subseteq V$ for variable $v$:
$$DF(S) = \bigcup_{X \in S} DF(X), \quad DF^1(S) = DF(S), \quad DF^{i+1}(S) = DF(S \cup DF^i(S))$$
The *Iterated Dominance Frontier* is the fixed point: $IDF(S) = \lim_{i \to \infty} DF^i(S)$.
- **Theorem (Cytron et al. 1991):** In minimal SSA form, a $\phi$-function for variable $v$ is required at node $Z$ if and only if $Z \in IDF(Def(v))$, where $Def(v)$ is the set of basic blocks containing assignments to $v$.

#### Efficient Computation Algorithm via Dominator Tree:
The dominance frontier can be partitioned into local and up-tree components:
$$DF(X) = DF_{local}(X) \cup \bigcup_{Z \in Children(X)} DF_{up}(Z)$$
where:
$$DF_{local}(X) = \{ Y \in Succ(X) \mid idom(Y) \ne X \}$$
$$DF_{up}(Z) = \{ Y \in DF(Z) \mid idom(Y) \ne X \}$$
This bottom-up traversal on the dominator tree computes $DF$ for all nodes in linear time $\mathcal{O}(|V| + |E|)$ for structured CFGs. $\blacksquare$

---

### 2. Register Allocation via Chordal Graph Coloring
**Formulation (Chaitin 1982):** Register allocation maps an unbounded number of program variables to $k$ physical machine registers by computing a $k$-coloring of the *interference graph* $G = (V, E)$, where vertices are variable live ranges and edges represent simultaneous liveness.

#### The Chordal Property in SSA Form:
While general graph coloring is NP-complete, the interference graph of programs in SSA form exhibits special mathematical structure:
1. **Definition (Chordal Graph):** A graph $G$ is *chordal* (or triangulated) if every induced cycle of length $\ge 4$ contains a chord (an edge connecting two non-consecutive vertices of the cycle).
2. **Subtree Intersection Theorem (Gavril 1974):** A graph is chordal if and only if it is the intersection graph of a family of subtrees of a tree.
3. **Theorem (Pereira & Palsberg 2005, Hack et al. 2006):** In SSA form, because each variable is defined at a unique dominator node, the live range of any variable is a connected subtree of the CFG dominator tree. Therefore, the interference graph of an SSA program is a **chordal graph**.

#### Polynomial-Time Optimal Coloring Algorithm:
1. **Maximum Cardinality Search (MCS):**
   Compute a *Perfect Elimination Ordering* (PEO) $\pi = (v_1, v_2, \dots, v_n)$ in $\mathcal{O}(|V| + |E|)$ time. In a PEO, for each vertex $v_i$, its neighbors that appear earlier in the ordering form a clique.
2. **Greedy Reverse Coloring:**
   Iterate from $v_n$ down to $v_1$, assigning each vertex the smallest available color not assigned to its already-colored neighbors.
3. **Optimality Guarantee:**
   For any chordal graph, the chromatic number $\chi(G)$ equals the clique number $\omega(G)$ (size of the maximum clique, i.e., peak register pressure):
   $$\chi(G) = \omega(G) = \max_{p \in \text{Program}} |\text{Live}(p)|$$
   Hence, register allocation on SSA form can be solved optimally in polynomial time without heuristic backtracking. $\blacksquare$

---

### 3. Soundness of Hindley-Milner Type Inference (Algorithm W)
**Theorem (Damas & Milner 1982):** Let $\Gamma$ be a typing context and $e$ a core ML expression. If $\text{Algorithm W}(\Gamma, e)$ succeeds and produces substitution $\sigma$ and type $\tau$, then the inferred typing is sound:
$$\sigma \Gamma \vdash e : \tau$$
Furthermore, $\tau$ is the *principal type*: any other valid type $\tau'$ for $e$ under $\sigma' \Gamma$ is a substitution instance of $\tau$.

#### Structural Induction Proof on Expression Syntax:
1. **Variable ($e = x$):**
   If $(x : \forall \alpha_1 \dots \alpha_n. \tau_0) \in \Gamma$, Algorithm W creates fresh type variables $\beta_1, \dots, \beta_n$ and returns $(id, \tau_0[\alpha_i \mapsto \beta_i])$.
   By the instantiation rule ($\forall\text{-elim}$), $\Gamma \vdash x : \tau_0[\vec{\alpha} \mapsto \vec{\beta}]$ holds immediately.
2. **Abstraction ($e = \lambda x. e_1$):**
   Algorithm W introduces a fresh type variable $\beta$, sets $\Gamma' = \Gamma \cup \{x : \beta\}$, and calls $\text{W}(\Gamma', e_1) = (\sigma_1, \tau_1)$.
   By the induction hypothesis, $\sigma_1(\Gamma \cup \{x : \beta\}) \vdash e_1 : \tau_1$.
   Expanding: $\sigma_1 \Gamma \cup \{x : \sigma_1 \beta\} \vdash e_1 : \tau_1$.
   Applying the $\to\text{-intro}$ rule yields:
   $$\sigma_1 \Gamma \vdash \lambda x. e_1 : \sigma_1 \beta \to \tau_1$$
   which matches the output of Algorithm W.
3. **Application ($e = e_1 \, e_2$):**
  - $\text{W}(\Gamma, e_1) = (\sigma_1, \tau_1)$. By induction, $\sigma_1 \Gamma \vdash e_1 : \tau_1$.
  - $\text{W}(\sigma_1 \Gamma, e_2) = (\sigma_2, \tau_2)$. By induction, $\sigma_2(\sigma_1 \Gamma) \vdash e_2 : \tau_2$.
  - By the Substitution Lemma, applying $\sigma_2$ to the first derivation preserves validity: $\sigma_2 \sigma_1 \Gamma \vdash e_1 : \sigma_2 \tau_1$.
  - Algorithm W computes the Most General Unifier (Robinson MGU) $\mu = \text{mgu}(\sigma_2 \tau_1, \tau_2 \to \beta)$ for fresh $\beta$.
  - Applying $\mu$: $\mu(\sigma_2 \tau_1) = \mu(\tau_2 \to \beta) = \mu \tau_2 \to \mu \beta$.
  - By $\to\text{-elim}$ (Modus Ponens):
     $$\frac{\mu \sigma_2 \sigma_1 \Gamma \vdash e_1 : \mu \tau_2 \to \mu \beta \quad \mu \sigma_2 \sigma_1 \Gamma \vdash e_2 : \mu \tau_2}{\mu \sigma_2 \sigma_1 \Gamma \vdash e_1 \, e_2 : \mu \beta}$$
   Thus the composed substitution $\sigma = \mu \circ \sigma_2 \circ \sigma_1$ soundly types $e_1 \, e_2$ with type $\mu \beta$.
4. **Let-Binding ($e = \text{let } x = e_1 \text{ in } e_2$):**
   Algorithm W infers $(\sigma_1, \tau_1)$ for $e_1$, computes the closure $\forall \vec{\alpha}. \tau_1$ by generalizing all type variables in $\tau_1$ not free in $\sigma_1 \Gamma$, binds $x$ to this polymorphic type scheme in context $\Gamma_2 = \sigma_1 \Gamma \cup \{x : \forall \vec{\alpha}. \tau_1\}$, and infers $(\sigma_2, \tau_2)$ for $e_2$. Soundness follows directly by the $\text{Let-Rule}$. $\blacksquare$

---

### 4. Mathematical Modeling in Human-Computer Interaction: Fitts's Law, Hick-Hyman Law & WCAG Contrast Metrics

#### 1. Fitts's Law (Information-Theoretic Psychomotor Pointing Model):
**Formulation (Paul Fitts 1954, Scott MacKenzie 1992):** The time required to rapidly move to a target area is a function of the distance to the target ($D$) and the width of the target along the axis of motion ($W$).

Using the Shannon formulation (MacKenzie 1992), the *Index of Difficulty* ($ID$) in bits is:
$$ID = \log_2 \left( \frac{D}{W} + 1 \right)$$
The *Movement Time* ($MT$) is modeled as a linear regression:
$$MT = a + b \cdot ID = a + b \log_2 \left( \frac{D}{W} + 1 \right)$$
where $a$ is the empirical start/stop reaction intercept and $b$ is the slope (seconds per bit, the reciprocal of human processing bandwidth).

- **Human Motor Throughput ($TP$):**
  $$TP = \frac{ID_e}{MT_e} \quad [\text{bits/second}]$$
  where $ID_e = \log_2(D / W_e + 1)$ uses the effective target width $W_e = 4.133 \times \sigma$ ($96\%$ accuracy boundary under Gaussian error distribution).
- **Engineering Corollaries:**
  - *Edge and Corner Target Infinity Property:* Targets pinned to the screen boundary have infinite virtual width ($W \to \infty$) because cursor movement cannot overshoot the physical display boundary. Hence $D/W \to 0$ and $ID = \log_2(1) = 0$, making screen edges and corners the fastest accessible interactive targets.
  - *Pie Menus vs Linear Menus:* Circular pie menus equalize target distance $D$ and maximize wedge width $W$, minimizing $ID$ compared to linear cascading dropdown menus.

#### 2. The Hick-Hyman Law (Cognitive Choice Reaction Time):
**Formulation (William Hick 1952, Ray Hyman 1953):** Given $n$ equally probable stimuli, the cognitive decision time $T$ required for a human to select an alternative is proportional to the Shannon information entropy of the stimulus set:
$$T = b \cdot H = b \log_2(n + 1)$$
where $H = \sum_{i=1}^n p_i \log_2(1/p_i)$ is the information entropy in bits, and $b$ is an empirically determined cognitive processing constant ($\approx 150 \text{ ms/bit}$).

- **Unequal Probabilities Formulation:**
  For $n$ alternatives with distinct transition probabilities $p_1, p_2, \dots, p_n$:
  $$T = b \sum_{i=1}^n p_i \log_2 \left( \frac{1}{p_i} + 1 \right)$$
- **Engineering Corollary:**
  Hierarchical navigation structures and command palettes (e.g. fuzzy search or Huffman-encoded command groupings) compress stimulus entropy $H$, drastically reducing user decision latency compared to flat unorganized choice sets.

#### 3. W3C WCAG 2.1 Relative Luminance & Contrast Ratio Derivation:
**Mathematical Specification (W3C WCAG 2.1 Section 1.4.3 / 1.4.6):**
The relative luminance $L$ of any sRGB color is defined as:
$$L = 0.2126 \cdot R + 0.7152 \cdot G + 0.0722 \cdot B$$
where the linear color components $C \in \{R, G, B\}$ are transformed from non-linear 8-bit sRGB channels $C_{srgb} = c / 255$:
$$C = \begin{cases} \frac{C_{srgb}}{12.92} & \text{if } C_{srgb} \le 0.04045 \\ \left( \frac{C_{srgb} + 0.055}{1.055} \right)^{2.4} & \text{if } C_{srgb} > 0.04045 \end{cases}$$

The **Contrast Ratio ($CR$)** between two colors with luminances $L_1$ (lighter color) and $L_2$ (darker color, $L_1 \ge L_2$) is:
$$CR = \frac{L_1 + 0.05}{L_2 + 0.05}$$
- **WCAG Compliance Thresholds:**
  - Level AA: Normal text requires $CR \ge 4.5:1$; large text ($\ge 18\text{pt}$ or bold $\ge 14\text{pt}$) requires $CR \ge 3.0:1$.
  - Level AAA: Normal text requires $CR \ge 7.0:1$; large text requires $CR \ge 4.5:1$.
  - Non-text UI components and graphical objects require $CR \ge 3.0:1$. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[Paper Reading Hub|Paper Reading Hub]])

The following foundational papers from the [[Paper Reading Hub|Paper Reading Hub]] are assigned to Block 17. Analyze each using the Keshav Three-Pass Methodology:

1. **"A Theory of Type Polymorphism in Programming"** (Robin Milner, 1978)
    - *Venue:* Journal of Computer and System Sciences (Paper 16 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Hindley-Milner type system and Algorithm W; provable type soundness and principal type inference without explicit type annotations.
    - *Reading Guidance:* Focus Pass 2 on the syntactic unification algorithm and the induction steps proving principal types.
2. **"Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs"** (Patrick Cousot & Radhia Cousot, 1977)
    - *Venue:* POPL '77 (Paper 17 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Galois connections between concrete trace semantics and abstract property lattices; sound static program analysis via widening operators.
    - *Reading Guidance:* Trace the Galois connection $(\alpha, \gamma)$ definitions and fixpoint convergence over complete lattices.
3. **"Efficiently Computing Static Single Assignment Form and the Control Dependence Graph"** (Ron Cytron, Jeanne Ferrante, Barry K. Rosen, Mark N. Wegman, F. Kenneth Zadeck, 1991)
    - *Venue:* ACM TOPLAS (Paper 18 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Dominance frontier algorithm for optimal $\phi$-function placement in SSA intermediate representation, transforming compiler optimization pipelines.
    - *Reading Guidance:* Verify the proof that iterated dominance frontiers ($IDF$) are necessary and sufficient for minimal $\phi$-placement.
4. **"RustBelt: Securing the Foundations of the Rust Programming Language"** (Ralf Jung, Jacques-Henri Jourdan, Robbert Krebbers, Derek Dreyer, 2017)
    - *Venue:* POPL 2018 (Paper 20 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Machine-checked semantic model (Iris separation logic in Coq) proving memory safety of Rust's type system and encapsulated unsafe abstractions.
    - *Reading Guidance:* Analyze how lifetime logic and borrow-checker invariants are formalized via Iris higher-order concurrent separation logic.
