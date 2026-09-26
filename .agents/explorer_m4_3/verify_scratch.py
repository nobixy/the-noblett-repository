import re
import sys
from pathlib import Path

# Add test suite path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "test_suite"))
import run_e2e_tests

runner = run_e2e_tests.VaultQualityTestSuite(Path(__file__).resolve().parent.parent.parent)

orig_f24 = runner.context.md_files["01 - Curriculum/Year 4 - Specialization/24 - Theory of Computation.md"]

proposed_proof = """#### The Deterministic Time Hierarchy Theorem (Hartmanis & Stearns 1965; Hennie & Stearns 1966):

**Theorem (Deterministic Time Hierarchy Theorem):**
Let $t_1, t_2 : \\mathbb{N} \\to \\mathbb{N}$ be functions such that $t_2$ is time-constructible and:
$$t_1(n) \\log_2 t_1(n) = o(t_2(n)) \\quad \\left(\\lim_{n \\to \\infty} \\frac{t_1(n) \\log_2 t_1(n)}{t_2(n)} = 0\\right)$$
where $t_1(n) \\ge n$ and $t_2(n) \\ge n$. Then:
$$\\text{DTIME}(t_1(n)) \\subsetneq \\text{DTIME}(t_2(n))$$

---

##### 1. Mathematical Preliminaries & Time-Constructibility
- **Deterministic Multi-Tape Turing Machine Model:**
  A deterministic Turing machine (DTM) $M = (Q, \\Sigma, \\Gamma, \\delta, q_0, q_{accept}, q_{reject})$ has $k \\ge 1$ two-way read/write work tapes, each with an independent read/write head.
  The transition function is:
  $$\\delta : (Q \\setminus \\{q_{accept}, q_{reject}\\}) \\times \\Gamma^k \\to Q \\times \\Gamma^k \\times \\{L, R, S\\}^k$$
  $M$ decides language $L \\subseteq \\Sigma^*$ in time $\\mathcal{O}(t(n))$ if on any input $w \\in \\Sigma^*$ of length $n = |w|$, $M$ halts in $q_{accept}$ if $w \\in L$ and halts in $q_{reject}$ if $w \\notin L$ within at most $c \\cdot t(n)$ steps for some constant $c > 0$.
  The class $\\text{DTIME}(t(n))$ denotes all languages decidable by some deterministic multi-tape TM in $\\mathcal{O}(t(n))$ steps.
- **Time-Constructibility:**
  A function $t : \\mathbb{N} \\to \\mathbb{N}$ is *time-constructible* if $t(n) \\ge n$ and there exists a deterministic Turing machine that, given input $1^n$, halts in exactly $t(n)$ steps (or computes the binary representation of $t(n)$ in $\\mathcal{O}(t(n))$ steps).
  Time-constructibility ensures the machine can clock itself without exceeding its own time bound. All standard complexity bounds ($n, n \\log n, n^2, 2^n$) are time-constructible.
- **Encoding Scheme & Padding:**
  Every deterministic multi-tape TM $M$ has a binary representation $\\langle M \\rangle \\in \\{0, 1\\}^*$. Every binary string encodes some Turing machine (strings with invalid syntax default to a canonical machine that immediately rejects).
  To ensure every TM is represented by infinitely many strings of arbitrarily large length, we consider inputs of the form:
  $$w = \\langle M \\rangle 1 0^k \\quad (k \\ge 0)$$
  where $1 0^k$ serves as a padding suffix. The length $n = |w| = |\\langle M \\rangle| + 1 + k$ can be made arbitrarily large while keeping the simulated machine $M$ fixed.

---

##### 2. Universal Multi-Tape Simulation Overhead (The Hennie-Stearns Theorem)
Simulating an arbitrary $k$-tape Turing machine on a machine with a fixed number of tapes introduces an unavoidable logarithmic time overhead.

**Theorem (Hennie & Stearns, 1966):**
There exists a fixed 4-tape deterministic Turing machine $U$ that can simulate any deterministic Turing machine $M$ having $k$ tapes for $T$ steps in at most:
$$\\mathcal{T}_{sim}(T) \\le C_M \\cdot T \\log_2 T$$
steps, where $C_M$ is a positive constant depending only on the simulated machine $M$ (its alphabet size $|\\Gamma|$ and number of tapes $k$), and is strictly independent of $T$ and the input length $n$.

- *Mechanism of the Logarithmic Overhead:*
  1. *Zone Doubling / Block Hierarchy:* To avoid traversing unbounded tape lengths between multiple simulated heads, the simulator stores all $k$ simulated tracks on a single multi-track tape organized into expanding concentric zones $B_0, B_1, B_2, \\dots, B_m$ centered at the simulator head, where zone $B_i$ has capacity $2^i$ cells for each simulated track.
  2. *Buffer State Invariant:* Each block $B_i$ is maintained such that it is either completely empty, half-full, or completely full of data cells.
  3. *Amortized Data Migration:* When head motion requires shifting data symbols into or out of zone $B_i$, the shift operation sweeps over zone $B_i$ in $\\mathcal{O}(2^i)$ steps. However, by virtue of the half-full buffer invariant, a shift at zone $B_i$ can occur at most once every $2^{i-1}$ simulated steps of $M$.
  4. *Telescoping Amortization Sum:*
     Over a total execution of $T$ simulated steps, the maximum zone level required is $m = \\lceil \\log_2 T \\rceil$.
     The total work spent shifting data at level $i$ across all $T$ steps is:
     $$\\sum_{\\text{shifts at level } i} \\mathcal{O}(2^i) \\le \\frac{T}{2^{i-1}} \\cdot \\mathcal{O}(2^i) = \\mathcal{O}(T)$$
     Summing across all $m = \\lceil \\log_2 T \\rceil$ levels yields the total simulation time:
     $$\\mathcal{T}_{sim}(T) = \\sum_{i=0}^{\\lceil \\log_2 T \\rceil} \\mathcal{O}(T) = \\mathcal{O}(T \\log_2 T)$$
     Incorporating the constant overhead of decoding transitions for machine $M$ yields the bound $\\mathcal{T}_{sim}(T) \\le C_M \\cdot T \\log_2 T$.

---

##### 3. Construction of the Diagonalizing Turing Machine $D$
We construct a deterministic Turing machine $D$ with 4 tapes:
- Tape 1: Input tape (read-only), containing input string $w \\in \\{0, 1\\}^*$ with length $n = |w|$.
- Tape 2: Clock counter tape, tracking the remaining time budget.
- Tape 3: Simulation work tape, containing the hierarchical zones for simulating the tapes and state transitions of $M$.
- Tape 4: Scratch tape, utilized for parsing, arithmetic, and data migration during zone shifts.

The algorithm for $D$ on input $w$ is defined as follows:

```text
Algorithm D(w):
1. Compute Input Length:
   Let n = |w|.
2. Syntactic Parsing & Extraction:
   Scan tape 1 to determine if w has the form w = <M> 1 0^k for some binary encoding <M>.
   If w does not contain '1' or <M> is invalid:
       REJECT immediately.
3. Clock Initialization (Time-Constructibility):
   Using the time-constructibility of t_2, execute the constructibility machine for t_2
   on input 1^n to write t_2(n) in binary onto Tape 2 (or lay down a track of t_2(n) cells).
   This step consumes at most c_clock * t_2(n) steps.
4. Universal Clocked Simulation:
   Initialize the Hennie-Stearns universal simulator U on Tape 3 with encoding <M> and input w.
   While M has not halted:
       a. Check Tape 2 (the clock counter tape). If the step budget t_2(n) is exhausted:
          ABORT and REJECT.
       b. Execute one simulation step of M on w using the Hennie-Stearns protocol.
       c. Decrement the clock counter by the number of steps consumed by D in step 4b.
5. Inversion (Diagonalization):
   If M halts within the allocated t_2(n) step budget:
       If M accepts w:
           REJECT.
       If M rejects w:
           ACCEPT.
```

---

##### 4. Complexity and Decidability Analysis of $D$
We verify that $D$ is a decider and determine its asymptotic time complexity:
1. **Parsing Phase (Steps 1–2):** Scanning the input $w$ requires $n$ head movements. Since $t_2(n) \\ge n$, this phase runs in $\\mathcal{O}(n) = \\mathcal{O}(t_2(n))$ steps.
2. **Clock Initialization (Step 3):** By the definition of time-constructibility, laying down or computing the $t_2(n)$ bound takes $\\mathcal{O}(t_2(n))$ steps.
3. **Simulation Phase (Step 4):** $D$ enforces an explicit clock abort condition: the total steps executed by $D$ during simulation cannot exceed $t_2(n)$. Decrementing the binary clock counter incurs an amortized cost of $\\mathcal{O}(1)$ steps per simulated step (or zero overhead if using a unary physical track).
4. **Inversion Phase (Step 5):** Checking acceptance and halting takes $\\mathcal{O}(1)$ steps.

Summing all phases, the total runtime of $D$ on any input $w$ of length $n$ is strictly bounded by:
$$\\mathcal{T}_D(n) \\le \\mathcal{O}(n) + \\mathcal{O}(t_2(n)) + t_2(n) + \\mathcal{O}(1) = \\mathcal{O}(t_2(n))$$
Because $D$ halts on all inputs within $\\mathcal{O}(t_2(n))$ steps, the language decided by $D$:
$$L(D) = \\{ w \\in \\{0, 1\\}^* \\mid D \\text{ accepts } w \\}$$
belongs to $\\text{DTIME}(t_2(n))$:
$$L(D) \\in \\text{DTIME}(t_2(n))$$

---

##### 5. Diagonal Contradiction: $L(D) \\notin \\text{DTIME}(t_1(n))$
To establish strict separation, we prove by contradiction that $L(D) \\notin \\text{DTIME}(t_1(n))$.

Suppose, for the sake of contradiction, that $L(D) \\in \\text{DTIME}(t_1(n))$.
Then there exists a deterministic multi-tape Turing machine $M^*$ that decides $L(D)$ and runs in time:
$$\\mathcal{T}_{M^*}(n) \\le c_1 \\cdot t_1(n)$$
for all $n \\ge n_0$, where $c_1 > 0$ is a constant.

- **Simulation Overhead on $M^*$:**
  By the Hennie-Stearns Theorem, machine $D$'s universal simulator simulates any $T$ steps of $M^*$ in at most $C_{M^*} \\cdot T \\log_2 T$ steps, where $C_{M^*}$ is a constant determined entirely by the alphabet and number of tapes of $M^*$.
  When $M^*$ is executed on an input $w$ of length $n = |w|$, it halts in at most $T \\le c_1 \\cdot t_1(n)$ steps.
  Therefore, the total simulation time required by $D$ to run $M^*$ to completion on input $w$ is bounded by:
  $$\\mathcal{T}_{D, sim}(n) \\le C_{M^*} \\cdot [c_1 t_1(n)] \\log_2 [c_1 t_1(n)] = c_1 C_{M^*} \\cdot t_1(n) \\left( \\log_2 t_1(n) + \\log_2 c_1 \\right)$$
  For sufficiently large $n$ such that $t_1(n) \\ge c_1$, we have $\\log_2 t_1(n) + \\log_2 c_1 \\le 2 \\log_2 t_1(n)$.
  Defining the composite constant $C^* = 2 c_1 C_{M^*} + c_{clock} + 1$:
  $$\\mathcal{T}_{D, total}(n) \\le C^* \\cdot t_1(n) \\log_2 t_1(n)$$

- **Asymptotic Dominance via $o(t_2(n))$:**
  We are given by hypothesis that $t_1(n) \\log_2 t_1(n) = o(t_2(n))$, which means:
  $$\\lim_{n \\to \\infty} \\frac{C^* \\cdot t_1(n) \\log_2 t_1(n)}{t_2(n)} = 0$$
  By the definition of the limit, there exists an integer $N_1 \\in \\mathbb{N}$ such that for all $n \\ge N_1$:
  $$\\frac{C^* \\cdot t_1(n) \\log_2 t_1(n)}{t_2(n)} < 1 \\iff C^* \\cdot t_1(n) \\log_2 t_1(n) < t_2(n)$$

- **Construction of the Diagonal Input:**
  Fix the padding length $k \\in \\mathbb{N}$ large enough such that:
  $$|w^*| = |\\langle M^* \\rangle 1 0^k| = |\\langle M^* \\rangle| + 1 + k \\ge \\max(n_0, N_1)$$
  Define the specific input string:
  $$w^* = \\langle M^* \\rangle 1 0^k, \\quad n^* = |w^*|$$

- **Execution Trace of $D$ on $w^*$:**
  We trace the execution of $D$ on input $w^*$:
  1. $D$ parses $w^*$, recognizes the valid prefix $\\langle M^* \\rangle$, and initializes the clock budget $t_2(n^*)$ on the clock counter tape.
  2. $D$ initiates the simulation of $M^*$ on input $w^*$.
  3. Because $n^* \\ge N_1$, the total steps needed to simulate $M^*$ to completion satisfy:
     $$\\mathcal{T}_{D, total}(n^*) \\le C^* \\cdot t_1(n^*) \\log_2 t_1(n^*) < t_2(n^*)$$
     Therefore, the simulation of $M^*$ completes strictly before the clock of budget $t_2(n^*)$ expires. The abort condition is never triggered.
  4. $M^*$ halts and enters either its accept state $q_{accept}$ or reject state $q_{reject}$.
  5. By Step 5 of Algorithm $D$, $D$ inverts the decision of $M^*$:
     $$D \\text{ accepts } w^* \\iff M^* \\text{ rejects } w^*$$
     In language membership notation:
     $$w^* \\in L(D) \\iff w^* \\notin L(M^*)$$

- **The Contradiction:**
  By our initial assumption, $M^*$ decides $L(D)$, meaning $L(M^*) = L(D)$. Therefore, for every input string $x \\in \\{0, 1\\}^*$:
  $$x \\in L(D) \\iff x \\in L(M^*)$$
  Instantiating this equivalence at $x = w^*$:
  $$w^* \\in L(D) \\iff w^* \\in L(M^*)$$
  Combining the two equivalences yields:
  $$w^* \\in L(D) \\iff w^* \\notin L(D)$$
  which is an impossible logical contradiction ($P \\iff \\neg P$).

Hence, no such decider $M^*$ running in $\\mathcal{O}(t_1(n))$ time can exist. Therefore:
$$L(D) \\notin \\text{DTIME}(t_1(n))$$
Because $L(D) \\in \\text{DTIME}(t_2(n))$ and $L(D) \\notin \\text{DTIME}(t_1(n))$, we conclude:
$$\\text{DTIME}(t_1(n)) \\subsetneq \\text{DTIME}(t_2(n)) \\quad \\blacksquare$$

---

##### 6. Theoretical Consequences & Corollaries
1. **Polynomial Separation:**
   For any constants $a, b \\in \\mathbb{R}$ with $1 \\le a < b$:
   $$\\text{DTIME}(n^a) \\subsetneq \\text{DTIME}(n^b)$$
   *Proof:* Since $a < b$, let $\\delta = \\frac{b - a}{2} > 0$. Then $n^a \\log_2(n^a) = \\mathcal{O}(n^a \\log n) = o(n^{a + \\delta}) = o(n^b)$. Applying the Time Hierarchy Theorem yields the strict inclusion. $\\blacksquare$

2. **Separation of $\\text{P}$ and $\\text{EXPTIME}$:**
   $$\\text{P} = \\bigcup_{k \\ge 1} \\text{DTIME}(n^k) \\subsetneq \\text{DTIME}(2^n) \\subseteq \\text{EXPTIME}$$
   *Proof:* For every fixed $k \\ge 1$, $n^k \\log(n^k) = o(2^n)$. Thus $\\text{DTIME}(n^k) \\subsetneq \\text{DTIME}(2^n)$. Since this holds for every $k$, no single machine running in time $2^n$ can be captured by polynomial time, proving $\\text{P} \\subsetneq \\text{EXPTIME}$. $\\blacksquare$

3. **Necessity of Time-Constructibility (Borodin's Gap Theorem):**
   The condition that $t_2$ is time-constructible cannot be eliminated.
   **Theorem (Borodin 1972):** For any computable function $g : \\mathbb{N} \\to \\mathbb{N}$ with $g(n) \\ge n$, there exists a computable, monotonically increasing function $f : \\mathbb{N} \\to \\mathbb{N}$ such that:
   $$\\text{DTIME}(f(n)) = \\text{DTIME}(g(f(n)))$$
   Setting $g(n) = 2^n$ yields a computable function $f$ such that $\\text{DTIME}(f(n)) = \\text{DTIME}(2^{f(n)})$, demonstrating an enormous computational complexity gap with zero intermediate languages. The Time Hierarchy Theorem succeeds precisely because time-constructibility prohibits such artificial non-constructible gaps. $\\blacksquare$"""

target_snippet = """#### The Time Hierarchy Theorem (Hartmanis & Stearns 1965):
**Theorem:** For any time-constructible function $f : \\mathbb{N} \\to \\mathbb{N}$ with $f(n) \\ge n$, if $g(n) \\log g(n) = o(f(n))$, then:
$$\\text{DTIME}(g(n)) \\subsetneq \\text{DTIME}(f(n))$$
*(The $\\log g(n)$ factor represents the universal simulation slowdown of simulating an arbitrary multi-tape TM on a fixed 2-tape TM).* $\\blacksquare$"""

assert target_snippet in orig_f24.raw_content, "target snippet not found in Block 24"
new_content = orig_f24.raw_content.replace(target_snippet, proposed_proof)

# Monkeypatch Path.read_text for Block 24
old_read_text = Path.read_text

def mocked_read_text(self, *args, **kwargs):
    if "24 - Theory of Computation.md" in str(self):
        c = old_read_text(self, *args, **kwargs)
        assert target_snippet in c, "target snippet not found"
        return c.replace(target_snippet, proposed_proof)
    return old_read_text(self, *args, **kwargs)

Path.read_text = mocked_read_text

# Re-run context collection
runner.context._discover_and_parse()
runner.context._build_graph()

print("Re-parsed context with mocked Block 24!")
res_t1_29 = runner.test_t1_29_time_hierarchy_theorem_proof_completion()
print("test_t1_29:", res_t1_29.passed, res_t1_29.message)

res_t1_30 = runner.test_t1_30_proof_qed_tombstone_consistency()
print("test_t1_30:", res_t1_30.passed, res_t1_30.message)

res_t1_21 = runner.test_t1_21_list_bullet_marker_uniformity()
print("test_t1_21:", res_t1_21.passed, res_t1_21.message)

res_t1_22 = runner.test_t1_22_list_indentation_hierarchy()
print("test_t1_22:", res_t1_22.passed, res_t1_22.message)
if not res_t1_22.passed:
    for d in res_t1_22.details:
        if "24 - Theory" in d:
            print("  Indentation issue:", d)

res_t1_25 = runner.test_t1_25_fenced_code_block_language_tagging()
print("test_t1_25:", res_t1_25.passed, res_t1_25.message)

res_t2_4 = runner.test_t2_4_malformed_fences_and_unclosed_delimiters()
print("test_t2_4:", res_t2_4.passed, res_t2_4.message)

res_t2_5 = runner.test_t2_5_odd_space_indentation_boundary()
print("test_t2_5:", res_t2_5.passed, res_t2_5.message)
if not res_t2_5.passed:
    for d in res_t2_5.details:
        if "24 - Theory" in d:
            print("  Odd space issue:", d)
