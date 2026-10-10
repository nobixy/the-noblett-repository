---
block_id: "Block 19a"
title: "Wireless, Mesh and Network Science"
category: "core"
subject: "Computer Engineering"
term: "Year 3 Spring (after Networking)"
status: not-started
prerequisites:
  - "B19 - Networking"
  - "B11 - Linear Algebra"
  - "B15 - Probability"
  - "B13 - Algorithms I"
hours_estimate: 130
hours_actual: 0
primary_resource: "Bullo, Lectures on Network Systems + Barabási, Network Science + Kurose & Ross ch. 7 + batman-adv / 802.11s docs (all free)"
milestone: "3–5 node mesh runs distributed average consensus; measured convergence matches the algebraic-connectivity prediction within 2x; mesh heals after a node drops"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 19a — Wireless, Mesh and Network Science

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Spring (after Networking)
> - **Estimated Hours:** ~130 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Bullo, Lectures on Network Systems + Barabási, Network Science + Kurose & Ross ch. 7 + batman-adv / 802.11s docs (all free)
> - **Key Milestone:** 3–5 node mesh runs distributed average consensus; measured convergence matches the algebraic-connectivity prediction within 2x; mesh heals after a node drops
> - **Added by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
A swarm is a network first and a set of drones second. CS144 taught the wired internet; this block adds the three things a swarm needs: the mathematics of networks (graphs, robustness, the Laplacian), how agents agree over a network (consensus and formation control), and how radios form a network without infrastructure (wireless MAC, ad-hoc and mesh routing). It is also the bridge from Networking to Information Theory (Block 32) and Track 11.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B19 - Networking|Networking]]
- [[B11 - Linear Algebra|Linear Algebra]]
- [[B15 - Probability|Probability]]
- [[B13 - Algorithms I|Algorithms I]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Network science: degree distributions, random graphs (Erdős–Rényi), small-world and scale-free networks, robustness and percolation, centrality, communities (Barabási ch. 1–5, 8–9; Easley & Kleinberg ch. 1–5 optional).
- [ ] Algebraic graph theory: adjacency and Laplacian matrices, algebraic connectivity λ2, spectral intuition (uses Block 11).
- [ ] Multi-agent consensus: averaging over a network, convergence rate set by λ2, time-varying and lossy graphs; formation control and rendezvous basics (Bullo, *Lectures on Network Systems*).
- [ ] Distributed agreement link: how consensus (control-theory sense) differs from Raft/Paxos consensus (Block 23).
- [ ] Wireless and mobile networks: 802.11 MAC, CSMA/CA, hidden terminals, path loss and fading, link budgets (Kurose & Ross ch. 7).
- [ ] Ad-hoc and mesh networking: MANET routing (AODV, OLSR), B.A.T.M.A.N. advanced (layer 2), IEEE 802.11s in Linux, ESP-NOW, LoRa mesh (Meshtastic), delay-tolerant ideas.
- [ ] Radio basics, receive-only: an RTL-SDR and PySDR ch. 1–6 to see real signals (sets up Track 11).
- [ ] **Resilient links (DR-006):** link-loss behaviors, delay-tolerant networking (RFC 4838, RFC 9171), frequency hopping and spread spectrum (DSSS/FHSS) and processing gain, LPI/LPD ideas, multi-bearer fallback (Wi-Fi mesh → LoRa → optical). Emulate jamming as loss and SNR drops in simulation only. Primer: *Wireless Communications for Everybody* (Yonsei, Coursera Plus).
- [ ] Optional: graph neural networks (Stanford CS224W) for learned swarm policies.

---

## 🛠️ Build Requirement
Simulate first (NetworkX + a small Python discrete-event sim; Linux `tc netem` for loss and delay), then build:
1. **Network-science notebook:** analyze one real public graph and one random-geometric graph (a model of radio range); robustness to node removal vs theory.
2. **Mesh testbed:** 3–5 nodes (ESP32 with ESP-NOW, or Pi Zero 2 W with batman-adv or 802.11s); measure delivery, latency and recovery after a node is unplugged.
3. **Consensus on the mesh:** run distributed average consensus on the real nodes under injected loss; compare the measured convergence rate with the λ2 of the measured topology.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Measured consensus convergence within 2x of the λ2 prediction; the mesh heals after node removal and you report the time; from a blank page you can explain hidden terminals and why consensus needs a connected graph.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- Francesco Bullo, *Lectures on Network Systems* (free PDF + slides): fbullo.github.io/lns/.
- Albert-László Barabási, *Network Science* (free online): networksciencebook.com.
- Easley & Kleinberg, *Networks, Crowds, and Markets* (free draft): cs.cornell.edu/home/kleinber/networks-book/.
- Kurose & Ross companion site (free videos and labs): gaia.cs.umass.edu/kurose_ross/ (ch. 7 Wireless and Mobile Networks).
- B.A.T.M.A.N. advanced: open-mesh.org/projects/batman-adv/wiki; Linux 802.11s: wireless.docs.kernel.org (…/ieee80211/802.11s.html); OpenWrt 802.11s guide: openwrt.org/docs/guide-user/network/wifi/mesh/80211s.
- ESP-NOW (ESP-IDF docs); Meshtastic (open-source LoRa mesh): meshtastic.org.
- Stanford CS224W (free materials): web.stanford.edu/class/cs224w/. NetworkX: networkx.org. PySDR (free): pysdr.org.
- **Kit (💲):** reuse your ESP32 / Pi boards; add 1–3 more ESP32 boards ≈$10 each; RTL-SDR Blog V4 $39.95 (USB-C) / $44.95 (rtl-sdr.com), receive-only. Free alternative: everything in simulation plus Linux network namespaces.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Theory is the check: your measured rate vs the λ2 prediction. Bullo's and Barabási's chapters have exercises; work them before reading discussions.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Mesbahi & Egerstedt, *Graph Theoretic Methods in Multiagent Networks* 💲 (library).
- MIT 6.02 (Track 11) for the physical layer if Kurose ch. 7 feels thin.

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B19 - Networking|← Networking]] | [[00 - Start Here|Start Here]] | [[B20 - Algorithms II|Algorithms II →]]
