---
block_id: "Block 30"
title: "Capstone: Autonomous Drone Swarm Prototype (MEng Year)"
category: "core"
subject: "Capstone"
term: "Year 5 (Two Semesters)"
status: not-started
prerequisites:
  - "B19a - Wireless, Mesh and Network Science"
  - "B23 - Distributed Systems"
  - "B24a - Applied Cryptography and Protocol Security"
  - "B25 - Convex Optimization"
  - "B25a - Deep Learning"
  - "B27 - Intensive Cryptopals"
  - "B27a - Drone Lab - Flight Stack, ROS 2 and SITL"
hours_estimate: 400
hours_actual: 0
primary_resource: "Your own research prototype: PX4/ArduPilot SITL + Gazebo + ROS 2 + Crazyswarm2, then 3+ small real drones"
milestone: "M0–M6 done: sim swarm, secure mesh, onboard perception, 3-drone indoor flight, red-team report; thesis 15k–25k words + 30-min talk + outside review"
date_started: ""
date_completed: ""
tier: "Tier 3 - Depth"
aliases: ["Magnum Opus Capstone"]
---

# Block 30 — Capstone: Autonomous Drone Swarm Prototype (MEng Year)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Projects Hub|Projects Hub]]

> [!INFO] Block Overview
> - **Term / Position:** Year 5 (Two Semesters)
> - **Estimated Hours:** ~400 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Your own research prototype: PX4/ArduPilot SITL + Gazebo + ROS 2 + Crazyswarm2, then 3+ small real drones
> - **Key Milestone:** M0–M6 done: sim swarm, secure mesh, onboard perception, 3-drone indoor flight, red-team report; thesis 15k–25k words + 30-min talk + outside review
> - **Redesigned by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 3 - Depth

## 🎯 Why This Block Matters
The capstone pulls the whole degree into one artifact: a small swarm of drones that coordinates without a central computer, senses with on-board learning, talks over an encrypted, authenticated mesh, navigates without GPS, and fails safe.

> [!IMPORTANT] Scope and framing
> A **civilian research prototype with dual-use relevance**: area survey and search-and-rescue coverage (ISR-style sensing), and a resilient communications relay. The work is **autonomy, sensing, networking and security only. Weapons, targeting and payload delivery are permanently out of scope.** Anything near them needs a Decision Record and a legal check (see Regulations & Ethics) before any work, not a build task.

It uses: control and estimation (Blocks 4a, 15a, Track 9), embedded and Linux (Maker Labs 2 and 4), mechanical and PCB (Maker Labs 3 and 5), networks and consensus (19, 19a, 23), cryptography (24a, 27), ML/DL and GPUs (22a, 23a, 25a, Track 7), optimization (25), information theory (32).

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B19a - Wireless, Mesh and Network Science|Wireless, Mesh and Network Science]]
- [[B23 - Distributed Systems|Distributed Systems]]
- [[B24a - Applied Cryptography and Protocol Security|Applied Cryptography]]
- [[B25 - Convex Optimization|Convex Optimization]]
- [[B25a - Deep Learning|Deep Learning]]
- [[B27 - Intensive Cryptopals|Cryptopals]]
- [[B27a - Drone Lab - Flight Stack, ROS 2 and SITL|Drone Lab]]

---

## 📖 Primary Syllabus & Core Content
- [ ] **Decentralized coordination:** average consensus, rendezvous and formation control on a graph (Bullo); distributed task allocation (auction / consensus-based bundle algorithm, CBBA) for area coverage.
- [ ] **Multi-agent planning and learning:** a classical baseline (coverage planning + allocation) vs a multi-agent RL policy trained in simulation (MARL book, PettingZoo, gym-pybullet-drones); honest comparison with confidence intervals.
- [ ] **Onboard perception (TinyML / edge AI):** a quantized person/object detector on the companion computer or an AI deck; latency, accuracy and power measured on the device.
- [ ] **Mesh networking:** ESP-NOW, 802.11s or batman-adv mesh between vehicles and the ground station; behavior under loss, partition and rejoin.
- [ ] **Encrypted, authenticated comms:** Noise or WireGuard links between nodes, MAVLink 2 signing on the flight link, fleet key provisioning, rotation and revocation of a captured node.
- [ ] **GPS-denied navigation:** optical flow + range sensing indoors; visual-inertial odometry in simulation (MIT VNAV).
- [ ] **Safety:** geofence, link-loss and low-battery behaviors, collision avoidance between agents, an independent kill switch, flight-test cards and a hazard log.
- [ ] **Threat model and red team** of the swarm's comms: eavesdropping, replay, injection, a compromised node, jamming and GPS spoofing **in simulation only**.
- [ ] **Write-up:** thesis, talk, public reproducible sim repo, outside review.

---

## 🛠️ Build Requirement
Staged deliverables, each with a *done when*. Sim first: M1–M4 need no drone hardware.

1. **M0 — Proposal, threat model, safety case** (the Year 4 Writing Deliverable). *Done when:* 3,000-word proposal with requirements and evaluation metrics; STRIDE threat model of the comms; hazard analysis and flight-test plan; TRUST passed; one outside reviewer has signed off on scope.
2. **M1 — Single-vehicle sim baseline.** PX4 (or ArduPilot) SITL + Gazebo + your ROS 2 nodes; Crazyswarm2 sim in parallel. *Done when:* a scripted survey mission succeeds 10/10 headless in CI with logs archived.
3. **M2 — Decentralized swarm in sim (N ≥ 5).** Consensus/formation + CBBA-style task allocation for area coverage. *Done when:* coverage completes with 20% injected packet loss and one agent killed mid-mission; measured convergence vs the graph's λ2 matches Block 19a theory; no central planner in the loop.
4. **M3 — Secure mesh.** Real ESP32/Pi nodes on the bench plus the sim. *Done when:* all inter-agent traffic is Noise/WireGuard-encrypted and authenticated, MAVLink 2 signing is on, a revoked node is locked out within one rotation period, and the overhead (latency, bandwidth, CPU) is measured.
5. **M4 — Perception and learning.** *Done when:* the on-board detector reports measured accuracy, latency and power on the target device; the MARL policy is compared with the classical baseline on coverage time over ≥30 seeded runs; GPS-denied navigation holds position within a stated error in sim and indoors.
6. **M5 — Hardware swarm, indoors.** 3+ Crazyflies or DIY ESP32/Pi micro-quads in a netted indoor area. *Done when:* 10 consecutive coverage flights with no unplanned manual intervention; every failsafe proven by fault injection (link cut, battery, geofence, node loss) and logged.
7. **M6 — Red team, evaluation, write-up.** *Done when:* the red-team report covers every threat-model item (replay, injection, compromised node; jamming and spoofing in simulation only); thesis 15,000–25,000 words with replication scripts; 30-minute recorded talk; written critique from an outside reviewer; public repo with a one-command sim demo. Ground-station UI only: a short usability check (5 users, SUS score), not the old full HCI audit.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> M0–M6 each meet their *done when*; the public repo reproduces the sim results with one command; thesis, talk and outside review delivered; the Regulations & Ethics checklist below is complete.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- Bullo, *Lectures on Network Systems* (free): fbullo.github.io/lns/. Albrecht, Christianos & Schäfer, *Multi-Agent Reinforcement Learning* (free PDF): marl-book.com. PettingZoo (free): pettingzoo.farama.org.
- PX4: docs.px4.io/main/en/ (multi-vehicle sim, ROS 2, message signing). ArduPilot SITL: ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html. ROS 2: docs.ros.org.
- Crazyswarm2: imrclab.github.io/crazyswarm2/; CrazySim: github.com/gtfactslab/CrazySim; gym-pybullet-drones: utiasdsl.github.io/gym-pybullet-drones/.
- MIT VNAV: vnav.mit.edu. MAVLink 2 signing: mavlink.io/en/guide/message_signing.html. Noise: noiseprotocol.org. batman-adv: open-mesh.org.
- **Hardware (💲, verified Oct 2026, store.bitcraze.io):** Crazyflie 2.1+ $240 each, Crazyradio 2.0 needed once; STEM drone bundle $320 (with Flow deck v2 for GPS-denied indoor flight); 3 drones ≈$800–900. Cheapest path: 3 DIY ESP-Drones ≈$40–70 each (≈$150–200) + printed frames and guards from Maker Lab 3, or a mixed fleet (1 real + simulated agents) if money is tight. A full swarm in simulation is a legitimate capstone result.

---

## ⚖️ Regulations & Ethics (checked 2026-10-09; not legal advice)
- **FAA, recreational flying:** pass the free **TRUST** test and carry proof; register if the drone weighs 250 g or more; registered drones must broadcast **Remote ID** (or fly in an FAA-Recognized Identification Area). Crazyflies (≈29 g) are under 250 g. faa.gov/uas/recreational_flyers, faa.gov/uas/getting_started/remote_id.
- **Is it recreational?** The FAA says compensation is not the test, and "when in doubt, assume Part 107". Research or portfolio flights outdoors may count as non-recreational. **Part 107** needs a Remote Pilot Certificate (knowledge test, 💲 fee): faa.gov/uas/commercial_operators/become_a_drone_pilot.
- **Swarms outdoors:** under 14 CFR 107.35 one person may not fly more than one drone at a time without a waiver (ecfr.gov, Part 107). This is another reason M5 is **indoors in a netted area**.
- **Radio law:** never jam or spoof GPS or radio signals on real airwaves; operating, making or selling jammers is illegal in the US (fcc.gov/enforcement/areas/jammers). The red team does that **only in simulation** or on wired/shielded bench setups.
- **Export control (awareness):** defense-related technical data can fall under **ITAR** (State Dept, pmddtc.state.gov) or **EAR** (Commerce, bis.gov). Keep this project to openly published, fundamental-research-style work in a public repo, and never post anything an employer or sponsor marks controlled; if you join a defense program, its export-compliance office decides.
- **DoD Directive 3000.09, Autonomy in Weapon Systems (reissued Jan 25, 2023)**, awareness only: it sets policy and senior review for autonomous and semi-autonomous *weapon* systems and requires appropriate levels of human judgment over the use of force. This capstone is not a weapon system and stays out of that scope. esd.whs.mil (DoDD 3000.09).
- **Ethics:** a dual-use reflection chapter in the thesis (who could misuse this, what you chose not to build and why), checked against the ACM Code of Ethics (acm.org/code-of-ethics).

## 🧭 Career Path (pointers, not endorsements)
- **Defense-tech and autonomy companies** build exactly this stack (autonomy, edge AI, mesh comms, security): e.g. Anduril (anduril.com/careers), Shield AI (shield.ai/careers), Skydio (skydio.com/careers). Many defense roles need a security clearance, which usually requires US citizenship; read each posting.
- **Small-business R&D:** DoD SBIR/STTR topics (dodsbirsttr.mil) and sbir.gov list funded problems; reading them shows what the field wants. Defense Innovation Unit (diu.mil) bridges commercial tech to DoD.
- **Public proof of skill:** merged contributions to PX4, ArduPilot, Crazyswarm2 or ROS 2 count more than certificates. Link them in the [[Employability Portfolio and Review|Employability Portfolio]].
- **Benchmarks:** the SUAS student competition rules (suas-competition.org) are a good external spec even if you can't enter.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Your outside reviewer's written critique; the sim CI and flight logs; the red-team report.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- If hardware money isn't there: a hardware-in-the-loop swarm (real ESP32 mesh + radios on the bench, simulated vehicles) still exercises everything except real flight.

---

## ➡️ Next Steps
- **Topic Hub:** [[Projects Hub|Projects Hub]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[Specialization Branches|← Specialization B, Course 1]] | [[00 - Start Here|Start Here]] | [[B32 - Information Theory|Information Theory →]]
