---
title: "14 - Computer Architecture — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 14 - Computer Architecture — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[14 - Computer Architecture]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[14 - Computer Architecture]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **5-Stage RISC-V Pipeline Hazards:** Data hazards (RAW, WAR, WAW), structural hazards, and control hazards. Forwarding path logic equations ($F_A, F_B$) and load-use interlock stall conditions.
- **Branch Prediction Architecture:** 1-bit/2-bit saturating counters, Yeh-Patt two-level adaptive branch predictors, and branch target buffer (BTB) misprediction penalty derivations.
- **Cache Geometry & Average Memory Access Time (AMAT):** $\text{AMAT} = t_{\text{hit}} + \text{Miss Rate} \times t_{\text{miss}}$. Multi-level inclusion vs exclusion invariants and non-blocking caches with miss status holding registers (MSHRs).
- **Out-of-Order Execution & Tomasulo's Algorithm:** Register renaming, reservation stations, common data bus (CDB) broadcasting, and precise interrupt recovery via reorder buffers (ROB).

---

### 1. Hazard Resolution & Forwarding Logic Completeness in a 5-Stage RISC-V Pipeline
**Theorem (Hennessy & Patterson):** Consider a canonical 5-stage RISC-V in-order pipelined datapath ($\text{IF}, \text{ID}, \text{EX}, \text{MEM}, \text{WB}$) with register file write occurring in the first half of the clock cycle and read in the second half.
1. **ALU Forwarding Sufficiency:** For any instruction $I_{\text{curr}}$ in stage $\text{EX}$ having source register inputs $\text{Rs1}_{\text{EX}}$ and $\text{Rs2}_{\text{EX}}$, Read-After-Write (RAW) data hazards caused by previous ALU instructions at instruction distance $\delta \in \{1, 2\}$ are resolved without pipeline stalls if and only if the forwarding multiplexer control signal $F_A$ (for operand $A$) implements the prioritized Boolean equations:
$$F_A = \begin{cases} 
10_2 & \text{if } \text{RegWrite}_{\text{MEM}} \land (\text{Rd}_{\text{MEM}} \ne 0) \land (\text{Rd}_{\text{MEM}} = \text{Rs1}_{\text{EX}}) \\
01_2 & \text{if } \text{RegWrite}_{\text{WB}} \land (\text{Rd}_{\text{WB}} \ne 0) \land (\text{Rd}_{\text{WB}} = \text{Rs1}_{\text{EX}}) \land \neg\left(\text{RegWrite}_{\text{MEM}} \land (\text{Rd}_{\text{MEM}} \ne 0) \land (\text{Rd}_{\text{MEM}} = \text{Rs1}_{\text{EX}})\right) \\
00_2 & \text{otherwise}
\end{cases}$$
(and symmetrically for operand $B$ substituting $\text{Rs2}_{\text{EX}}$).
2. **Load-Use Interlock Delay Bound:** When instruction $I_{\text{curr}-1}$ in $\text{EX}$ is a memory load ($\text{MemRead}_{\text{EX}} = 1$), and instruction $I_{\text{curr}}$ in $\text{ID}$ reads $\text{Rd}_{\text{EX}}$:
$$\text{Stall}_{\text{LoadUse}} = \text{MemRead}_{\text{EX}} \land \left( (\text{Rd}_{\text{EX}} = \text{Rs1}_{\text{ID}}) \lor (\text{Rd}_{\text{EX}} = \text{Rs2}_{\text{ID}}) \right) \land (\text{Rd}_{\text{EX}} \ne 0)$$
then exactly one bubble stall cycle is strictly necessary and sufficient to preserve sequential program semantics.

#### Step-by-Step Derivation & Proof:
1. **Temporal Datapath Schedule:**
   Let $t \in \mathbb{N}$ denote discrete processor clock cycles.
  - For instruction $I_i$, execution stage $\text{EX}$ occurs during cycle $t_i$.
  - Its ALU result is computed during cycle $t_i$ and stored in pipeline register $\text{EX/MEM}$ at cycle $t_i + 1$.
  - Its memory access occurs during cycle $t_i + 1$, and data is latched into $\text{MEM/WB}$ at cycle $t_i + 2$.
  - Register write-back occurs during cycle $t_i + 2$.

2. **Resolution of RAW Hazard at Distance $\delta = 1$:**
   Instruction $I_{i-1}$ computes a result in $\text{EX}$ at cycle $t-1$. At cycle $t$, $I_{i-1}$ is in stage $\text{MEM}$, while dependent instruction $I_i$ enters stage $\text{EX}$.
   $I_i$ requires source operand $\text{Rs1}_{\text{EX}}$ at the input of the ALU at cycle $t$.
   The required value resides in the $\text{EX/MEM}$ pipeline register ($\text{ALUOut}_{\text{MEM}}$).
   Multiplexer setting $F_A = 10_2$ selects $\text{ALUOut}_{\text{MEM}}$ and routes it to the ALU operand port with propagation delay $t_{\text{mux}} + t_{\text{ALU}} < T_{\text{clk}}$.
   Thus, distance $\delta = 1$ is resolved in zero stall cycles.

3. **Resolution of RAW Hazard at Distance $\delta = 2$:**
   Instruction $I_{i-2}$ is in stage $\text{WB}$ at cycle $t$.
   Its computed value is latched in pipeline register $\text{MEM/WB}$ ($\text{Result}_{\text{WB}}$).
   Multiplexer setting $F_A = 01_2$ selects $\text{Result}_{\text{WB}}$ and routes it to the ALU input port at cycle $t$.
   Thus, distance $\delta = 2$ is resolved in zero stall cycles.

4. **Proof of the Priority Ordering Invariant:**
   Suppose both preceding instructions write to the same register: $\text{Rd}_{\text{MEM}} = \text{Rd}_{\text{WB}} = \text{Rs1}_{\text{EX}}$.
   By sequential execution semantics, instruction $I_i$ must observe the write of the most recent instruction ($I_{i-1}$).
   Because the activation condition for $F_A = 01_2$ includes the inhibitory clause:
   $$\neg\left(\text{RegWrite}_{\text{MEM}} \land (\text{Rd}_{\text{MEM}} \ne 0) \land (\text{Rd}_{\text{MEM}} = \text{Rs1}_{\text{EX}})\right)$$
   stage $\text{MEM}$ strictly overrides stage $\text{WB}$.
   Hence, the datapath guarantees observation of the chronologically latest value.
   (The clause $\text{Rd} \ne 0$ enforces the RISC-V architectural invariant that register `x0` is hardwired to zero and never forwarded).

5. **Necessity and Sufficiency of the 1-Cycle Load-Use Stall:**
   Consider a load instruction $I_{i-1} = \text{lw } \text{Rd}, \text{offset}(\text{Rs})$.
   The target memory word is read from SRAM cache during stage $\text{MEM}$ and is not physically stable until the conclusion of cycle $t_{\text{MEM}}$.
   If dependent instruction $I_i$ is in $\text{EX}$ concurrently with $I_{i-1}$ in $\text{MEM}$, the ALU of $I_i$ requires the operand at the beginning of cycle $t_{\text{MEM}}$, before memory access completes.
   Forwarding without delay would require data propagation backward in time ($\Delta t < 0$), which violates causality.
   By asserting $\text{Stall}_{\text{LoadUse}}$ when $I_{i-1}$ is in $\text{EX}$ and $I_i$ is in $\text{ID}$:
  - The Program Counter ($\text{PC}$) and $\text{IF/ID}$ register writes are disabled, freezing instruction $I_i$ in $\text{ID}$ for 1 cycle.
  - Synchronous control signals in $\text{ID/EX}$ are zeroed, inserting a `NOP` bubble into $\text{EX}$.
  - In cycle $t+1$, $I_{i-1}$ advances to stage $\text{WB}$ while $I_i$ enters stage $\text{EX}$.
   Data is now available in $\text{MEM/WB}$ and forwarded via $F_A = 01_2$ with zero functional corruption.
   Therefore, exactly 1 stall cycle is necessary and sufficient. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])

The following foundational papers from the [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] are assigned to Block 14. Analyze each using the Keshav Three-Pass Methodology:

1. **"The Case for the Reduced Instruction Set Computer"** (David A. Patterson & David R. Ditzel, 1980)
    - *Venue:* ACM SIGARCH Computer Architecture News (Paper 6 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Quantified execution efficiency of simplified instruction sets with single-cycle register-to-register datapaths and compiler-driven scheduling.
    - *Reading Guidance:* Focus Pass 2 on the empirical compiler code-generation measurements and the argument against microcoded CISC instructions.
2. **"A Case for Redundant Arrays of Inexpensive Disks (RAID)"** (David A. Patterson, Garth Gibson, Randy H. Katz, 1988)
    - *Venue:* SIGMOD '88 (Paper 7 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Formalization of RAID levels 0 through 5; parity calculations and mean-time-to-data-loss (MTTDL) reliability derivations.
    - *Reading Guidance:* Trace the MTTDL derivation comparing independent disks against mirrored and parity-protected arrays.
3. **"In-Datacenter Performance Analysis of a Tensor Processing Unit"** (Norman P. Jouppi et al., 2017)
    - *Venue:* ISCA '17 (Paper 8 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Microarchitecture of Google TPU v1: 2D matrix multiply unit (systolic array) optimizing roofline operational intensity for deep learning inference.
    - *Reading Guidance:* Analyze the roofline model chart comparing TPU, CPU, and GPU memory bandwidth vs compute throughput.
4. **"Simultaneous Multithreading: Maximizing On-Chip Parallelism"** (Dean M. Tullsen, Susan J. Eggers, Henry M. Levy, 1995)
    - *Venue:* ISCA '95 (Paper 10 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Dynamic hardware sharing of out-of-order execution pipelines across multiple hardware thread contexts to eliminate horizontal and vertical stalls.
    - *Reading Guidance:* Examine how SMT converts underutilized issue slots into thread-level throughput without replicating execution units.
