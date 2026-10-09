---
block_id: "Block 32"
title: "Information Theory, Inference, and Learning Algorithms"
category: "core"
subject: "Computer Science"
term: "Year 5"
status: not-started
prerequisites:
  - "B15 - Probability"
hours_estimate: 120
hours_actual: 0
primary_resource: "David MacKay, Information Theory, Inference, and Learning Algorithms (free)"
milestone: "Derive Shannon entropy, source coding, channel capacity, and error-correcting codes"
date_started: ""
date_completed: ""
tier: "Tier 3 - Depth"
aliases: ["Information Theory"]
---

# Block 32 — Information Theory, Inference, and Learning Algorithms

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Math Index|Math Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 5
> - **Estimated Hours:** ~120 hrs
> - **Status:** `not-started`
> - **Primary Resource:** David MacKay, Information Theory, Inference, and Learning Algorithms (free)
> - **Key Milestone:** Derive Shannon entropy, source coding, channel capacity, and error-correcting codes

---

## 📚 Curriculum Tier: Tier 3 - Depth
> **Tier 3 - Depth**: Optional deep dive for specialized mastery.

## 🎯 Why This Block Matters
Unifies information theory, statistics, coding theory, and machine learning into a single profound conceptual framework.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B15 - Probability|Probability]]


## 📖 Primary Syllabus & Core Content
- [ ] Introduction to Information Theory: Shannon entropy, mutual information, Kullback-Leibler divergence
- [ ] Data Compression: Source coding theorem, Huffman codes, arithmetic coding
- [ ] Noisy Channels: Channel capacity, noisy-channel coding theorem, error-correcting codes
- [ ] Probabilistic Inference & Monte Carlo methods
- [ ] Neural networks and sparse graph codes (LDPC codes)

---

## 🛠️ Build Requirement
Implement an information theory and coding suite in `python` and `c++` using `numpy`, `scipy`, `pytest`, and `latex`:
1. **Entropy Encoders**: Construct optimal Huffman and high-precision Arithmetic Encoders/Decoders in Python and C++; evaluate compression bitrates against empirical Shannon entropy across binary, text, and synthetic Markov sources.
2. **Channel Capacity & Blahut-Arimoto**: Code the Blahut-Arimoto alternating optimization algorithm to compute channel capacity $C = \max_{p(x)} I(X; Y)$ for arbitrary discrete memoryless channels (BSC, BEC, and asymmetric Z-channels).
3. **Low-Density Parity-Check (LDPC) Codes**: Build a belief propagation (sum-product algorithm) decoder on Tanner graphs; simulate bit error rate (BER) curves across varying SNR on an AWGN channel, demonstrating near-Shannon-limit performance within 0.5 dB.
4. **Toolchain & Verification**: Automated unit test suites run via `pytest`, build pipelines managed with `cmake` and `make`, automated verification scripts executed in `bash`, and mathematical derivations compiled in `latex`.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Read cover to cover (~4 hrs/wk reading) and solve key theoretical problems. Custom LDPC belief-propagation simulator passes test suites with zero block errors above channel threshold. Proofs below are derived and mastered.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> MacKay's book includes worked solutions to many of its exercises.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Cover & Thomas, Elements of Information Theory.

---

## ➡️ Next Steps
- **Topic Hub:** [[Math Index|Math Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B30 - Magnum Opus Capstone|← Magnum Opus Capstone]] | [[00 - Start Here|Start Here]] | [[00 - Start Here|Start Here →]]
