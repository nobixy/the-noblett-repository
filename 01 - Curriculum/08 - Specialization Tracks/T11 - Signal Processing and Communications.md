---
block_id: "Track 11"
track_id: "Track 11"
title: "Signal Processing, Communications and Electromagnetics"
category: "specialization"
subject: "Specialization"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "B15a - Signals and Systems Bridge"
  - "B08a - Circuits and Electronics Bridge"
  - "B15 - Probability"
  - "B11 - Linear Algebra"
target_profile: "DSP Engineer, Communications/Wireless Engineer, RF and Embedded Signal Engineer"
hours_estimate: 400
hours_actual: 0
primary_resource: "MIT 6.341 Discrete-Time Signal Processing + MIT 6.02/6.450 Digital Communications + PySDR (all free)"
milestone: "A working software-defined-radio receiver: real over-the-air signal captured, demodulated and decoded by your own DSP code"
date_started: ""
date_completed: ""
tier: "Tier 3 - Depth"
optional: true # specialization track not yet chosen (DR-001)
aliases: ["Signal Processing and Communications"]
---

# Track 11 — Signal Processing, Communications and Electromagnetics

[[00 - Start Here|Start Here]] / [[Specialization Branches|Specializations Hub]]

> [!INFO] Track Overview
> - **Track ID:** Track 11
> - **Prerequisites:** [[B15a - Signals and Systems Bridge|Signals and Systems]], [[B08a - Circuits and Electronics Bridge|Circuits and Electronics]], [[B15 - Probability|Probability]], [[B11 - Linear Algebra|Linear Algebra]]
> - **Structure:** Two core courses plus one capstone build.
> - **Added by:** [[DR-004 - Content Overhaul|DR-004]] (2026-10-09): the "EE" half of EECS had no specialization of its own.

---

## 📚 Curriculum Tier: Tier 3 - Depth
> **Tier 3 - Depth**: Optional deep dive for specialized mastery.

## 🎯 Why This Track Matters
Every wireless link, audio pipeline, radar, medical scanner and sensor front end is signal processing plus communications theory on top of electromagnetics. It is the classic electrical-engineering specialization (MIT's 6-5 Electrical Engineering with Computing lists signals and systems as required and builds its EE tracks on it). Blocks 8a, 15a and 32 give the foundation; this track turns it into the ability to build a radio.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B15a - Signals and Systems Bridge|Signals and Systems Bridge]]
- [[B08a - Circuits and Electronics Bridge|Circuits and Electronics Bridge]]
- [[B15 - Probability|Probability]]
- [[B11 - Linear Algebra|Linear Algebra]]

---

## 🌐 Real Courses (verified 2026-10-09, DR-004)
### Course 1: Discrete-Time Signal Processing and Inference
- **MIT 6.341 Discrete-Time Signal Processing** (OCW, free): ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/ — sampling, filter design, DFT/FFT algorithms, multirate, spectral estimation.
- **MIT 6.011 Signals, Systems and Inference** (OCW, Spring 2018, free): ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/ — random processes, Wiener filtering, detection and estimation.
- Free text: Smith, *The Scientist and Engineer's Guide to DSP* (dspguide.com). 💲 Oppenheim & Schafer, *Discrete-Time Signal Processing* (the 6.341 text); the free alternative is the 6.341 OCW notes plus dspguide.

### Course 2: Digital Communications, SDR and Electromagnetics
- **MIT 6.02 Introduction to EECS II: Digital Communication Systems** (OCW, Fall 2012, free): ocw.mit.edu/courses/6-02-introduction-to-eecs-ii-digital-communication-systems-fall-2012/ — coding, modulation, networks of links.
- **MIT 6.450 Principles of Digital Communications I** (OCW, free): ocw.mit.edu/courses/6-450-principles-of-digital-communications-i-fall-2006/ — the graduate-level theory.
- **PySDR** (free online textbook, Python): pysdr.org — IQ sampling, filters, synchronization, real-radio labs. **GNU Radio** (free): gnuradio.org.
- **MIT 6.013 Electromagnetics and Applications** (OCW, free): ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/ — waves, transmission lines, antennas.
- 💲 An RTL-SDR-class USB receiver (low cost). Free alternative: public IQ recordings and online WebSDR receivers; everything in PySDR can run on recorded files.

---

## 🛠️ Progressive Labs
1. **FIR/IIR filter designer** in Python: window and Parks–McClellan FIR, bilinear-transform IIR; verify frequency responses against `scipy.signal`.
2. **OFDM-lite modem** in simulation: QPSK/16-QAM, channel with noise and multipath, equalization; plot BER vs. SNR against theory.
3. **Over-the-air FM and digital decoding** with PySDR/GNU Radio: receive broadcast FM, then decode a digital signal (e.g. ADS-B or RDS) with your own demodulator and synchronization code.

---

## 🏆 Capstone Build Deliverable
A software-defined-radio receiver for a real over-the-air digital signal, written by you from the IQ samples up: filtering, timing and carrier recovery, demodulation, decoding and error correction (reuse your Block 32 LDPC or Hamming code where it fits). Ship measured BER or packet-success curves and a write-up comparing them to theory.

---

## 🛩️ Capstone Link (DR-005, 2026-10-09)
**Capstone link:** the physical layer under the swarm's mesh (modulation, coding, interference, SDR). Pick it as Specialization B instead of Track 7 if radio links interest you more than on-board ML; [[B19a - Wireless, Mesh and Network Science|Block 19a]] gives the receive-only SDR basics either way.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> 6.341 and 6.02 problem sets done; all three labs verified against reference tools; the capstone decodes real signals captured over the air (or from public recordings) with measured performance within a stated margin of theory.

---

## 📝 Study Notes, Psets & Proofs
*Your blank-page attempts, derivations, and atomic reflections.*

---

## ➡️ Next Steps & Degree Pathway
- **Curriculum Hub:** [[Specialization Branches|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[Specialization Branches|Block 26 - Specialization A1]] and Course 2 binds to [[Specialization Branches|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[Specialization Branches|Block 29 - Specialization B1]] and Course 2 binds to [[Specialization Branches|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]]

- **Sequential Flow:** [[T10 - Full-Stack and Product Engineering|← Full-Stack and Product Engineering]] | [[00 - Start Here|Start Here]] | [[Specialization Branches|Specialization Branches →]]
