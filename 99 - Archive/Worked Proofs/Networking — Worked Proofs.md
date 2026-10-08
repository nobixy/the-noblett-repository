---
title: "19 - Networking — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 19 - Networking — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Networking]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Networking]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **TCP Sliding Window & Flow Control:** Sequence number wraparound ($2^{32}-1$), receive window ($\text{rcv\_wnd}$) advertisements, zero-window probing, and silly window syndrome avoidance (Nagle's algorithm).
- **TCP Congestion Control Dynamics (AIMD):** Additive-Increase Multiplicative-Decrease stability derivation, slow start exponential threshold, Fast Retransmit via triple duplicate ACKs, and Fast Recovery.
- **Distance-Vector vs Link-State Routing Invariants:** Bellman-Ford count-to-infinity problem and split horizon with poison reverse vs Dijkstra link-state flood convergence and routing loop avoidance.
- **End-to-End Argument in System Design:** Saltzer, Reed, and Clark principle: functions placed at low levels of a distributed system may be redundant or of little value compared to providing them at the end points.

---

### 1. The Chiu-Jain Convergence and Stability Theorem for AIMD Congestion Control
**Theorem (Chiu & Jain, 1989):** Let $N$ independent network senders share a bottleneck link of capacity $C > 0$. Let $x_i(t) \ge 0$ denote the transmission rate (or congestion window) of sender $i$ at discrete time round $t$, and let $X(t) = \sum_{i=1}^N x_i(t)$ represent aggregate network demand.
The network provides binary feedback $y(t) \in \{0, 1\}$:
$$y(t) = 0 \iff X(t) \le C \quad (\text{underutilized}); \qquad y(t) = 1 \iff X(t) > C \quad (\text{congested})$$
Consider the class of linear distributed control policies:
$$x_i(t+1) = \begin{cases} 
x_i(t) + \alpha_I & \text{if } y(t) = 0 \quad (\text{Additive Increase}, \alpha_I > 0) \\
\beta_D \cdot x_i(t) & \text{if } y(t) = 1 \quad (\text{Multiplicative Decrease}, 0 < \beta_D < 1)
\end{cases}$$
**Theorem Statement:**
1. **Global Convergence to Fairness:** Under Additive-Increase Multiplicative-Decrease ($\text{AIMD}$), for any non-zero initial rate allocation $\mathbf{x}(0) \in \mathbb{R}_{\ge 0}^N \setminus \{\mathbf{0}\}$, the Jain Fairness Index:
$$J(\mathbf{x}) = \frac{\left( \sum_{i=1}^N x_i \right)^2}{N \sum_{i=1}^N x_i^2}$$
converges asymptotically to 1:
$$\lim_{t \to \infty} J(\mathbf{x}(t)) = 1$$
2. **Uniqueness:** Linear alternative policies—Multiplicative-Increase Multiplicative-Decrease ($\text{MIMD}$) and Additive-Increase Additive-Decrease ($\text{AIAD}$)—fail to converge to both efficiency and fairness.

#### Step-by-Step Derivation & Proof:
1. **Vector Space and Phase-Plane Representation:**
   Represent the system state in $N$-dimensional Euclidean space $\mathbf{x} = (x_1, \dots, x_N) \in \mathbb{R}_{\ge 0}^N$.
  - **The Efficiency Hyperplane:** $\sum_{i=1}^N x_i = C$. Points on this line achieve 100% capacity utilization without packet drop.
  - **The Fairness Ray:** The line where all senders have equal rates: $x_1 = x_2 = \dots = x_N$, directed along unit vector $\mathbf{u} = \frac{1}{\sqrt{N}}[1, 1, \dots, 1]^T$.
  - **Optimal Operating Point:** $\mathbf{x}^* = \left(\frac{C}{N}, \dots, \frac{C}{N}\right)$, the intersection of the efficiency line with the fairness ray.

2. **Dynamics of Additive Increase:**
   When $X(t) \le C$, each sender increments rate by fixed constant $\alpha_I > 0$:
   $$\mathbf{x}(t+1) = \mathbf{x}(t) + \alpha_I \mathbf{1}, \qquad \mathbf{1} = [1, 1, \dots, 1]^T$$
   The state moves in direction $\mathbf{1}$, parallel to the fairness ray.
   For any two users $i$ and $j$, consider the difference between their allocations:
   $$x_i(t+1) - x_j(t+1) = (x_i(t) + \alpha_I) - (x_j(t) + \alpha_I) = x_i(t) - x_j(t)$$
   The absolute disparity $|x_i - x_j|$ remains invariant during additive increase.
   However, their ratio converges toward 1:
   $$\frac{x_i(t+1)}{x_j(t+1)} = \frac{x_i(t) + \alpha_I}{x_j(t) + \alpha_I} \xrightarrow{\alpha_I \to \infty} 1$$

3. **Dynamics of Multiplicative Decrease:**
   When $X(t) > C$, each sender multiplies rate by $\beta_D \in (0, 1)$:
   $$\mathbf{x}(t+1) = \beta_D \mathbf{x}(t)$$
   The state moves along the ray connecting $\mathbf{x}(t)$ to the origin $\mathbf{0}$.
   Evaluating the difference between users $i$ and $j$:
   $$|x_i(t+1) - x_j(t+1)| = |\beta_D x_i(t) - \beta_D x_j(t)| = \beta_D |x_i(t) - x_j(t)|$$
   Because $\beta_D < 1$, the absolute discrepancy contracts by a factor of $\beta_D$ upon every congestion event.

4. **Limit Cycle and Asymptotic Convergence:**
   Consider an execution trajectory experiencing $k$ successive congestion events at times $t_1, t_2, \dots, t_k$.
   Because additive increase leaves $|x_i - x_j|$ unchanged while each multiplicative decrease contracts it by $\beta_D$:
   $$|x_i(t_k) - x_j(t_k)| = (\beta_D)^k |x_i(0) - x_j(0)|$$
   Since $0 < \beta_D < 1$:
   $$\lim_{k \to \infty} |x_i(t_k) - x_j(t_k)| = \lim_{k \to \infty} (\beta_D)^k |x_i(0) - x_j(0)| = 0$$
   All rates converge to equality: $x_i(t) \to x_j(t)$.

5. **Evaluation of the Jain Fairness Index:**
   Let $\mu = \frac{1}{N}\sum x_i$ and $\sigma^2 = \frac{1}{N}\sum (x_i - \mu)^2$. Expanding the fairness index:
   $$J(\mathbf{x}) = \frac{(N\mu)^2}{N \sum x_i^2} = \frac{N^2 \mu^2}{N (N\mu^2 + N\sigma^2)} = \frac{1}{1 + \frac{\sigma^2}{\mu^2}}$$
   Since $|x_i - x_j| \to 0$, the variance $\sigma^2 \to 0$ while mean throughput $\mu > 0$.
   Therefore:
   $$\lim_{t \to \infty} J(\mathbf{x}(t)) = \frac{1}{1 + 0} = 1$$

6. **Instability and Divergence of Other Linear Policies:**
  - **MIMD ($\beta_I > 1, 0 < \beta_D < 1$):** Both increase and decrease trajectories lie along rays emanating from the origin. The ratio $\frac{x_i(t)}{x_j(t)} = \frac{x_i(0)}{x_j(0)}$ is a constant invariant. If $x_i(0) \ne x_j(0)$, $J(\mathbf{x}(t)) = J(\mathbf{x}(0)) < 1$ for all $t$. Fairness never improves.
  - **AIAD ($\alpha_I > 0, \alpha_D < 0$):** Both increase and decrease trajectories move parallel to $\mathbf{1}$. The difference $x_i(t) - x_j(t) = x_i(0) - x_j(0)$ is an invariant, leading to oscillating limit cycles that never contract toward the fairness ray.
   Hence, $\text{AIMD}$ is the unique linear policy that guarantees convergence to both maximum efficiency and optimal fairness. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[Paper Reading Hub|Paper Reading Hub]])

The following foundational paper from the [[Paper Reading Hub|Paper Reading Hub]] is assigned to Block 19. Analyze using the Keshav Three-Pass Methodology:

1. **"The Design Philosophy of the DARPA Internet Protocols"** (David D. Clark, 1988)
    - *Venue:* SIGCOMM '88 (Paper 3 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Fate-sharing state distribution model; packet switching resilience where intermediate router crashes do not drop connection state.
    - *Reading Guidance:* Focus Pass 2 on the ordered hierarchy of architectural goals (survivability, multiple service types, variety of networks) and why fate-sharing was chosen over distributed state replication.
