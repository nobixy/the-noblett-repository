---
block_id: "Block 19"
title: "Computer Networking (Stanford CS144)"
category: "core"
subject: "Computer Engineering"
term: "Year 3 January Intensive"
status: not-started
prerequisites:
  - "B16 - Operating Systems"
hours_estimate: 150
hours_actual: 0
primary_resource: "Stanford CS144 (cs144.github.io) & Kurose & Ross"
milestone: "Custom TCP stack fetches a real web page over the live internet"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
job_ready: 4 # job-ready path, phase 4 (DR-003)
aliases: ["Networking"]
---

# Block 19 — Computer Networking (Stanford CS144)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 January Intensive
> - **Estimated Hours:** ~150 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Stanford CS144 (cs144.github.io) & Kurose & Ross
> - **Key Milestone:** Custom TCP stack fetches a real web page over the live internet

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
The internet is the nervous system of modern software. Build the protocols hands-on to understand latency, reliability, congestion, and packet routing.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B16 - Operating Systems|Operating Systems]]


## 📖 Primary Syllabus & Core Content
- [ ] Application Layer: HTTP, DNS, CDN
- [ ] Transport Layer: UDP, TCP principles, reliable transport, flow control, congestion control
- [ ] Network Layer: IP, routing algorithms (Dijkstra, distance vector, BGP)
- [ ] Link Layer: Ethernet, ARP, switching
- [ ] Stanford CS144 Lab Sequence (Labs 0 through 7)

---

## 🛠️ Build Requirement
All eight Stanford CS144 labs: implement a complete, working TCP stack in modern C++ (byte stream, reassembler, TCP receiver, TCP sender, TCP connection, network interface, router).

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Your custom C++ TCP stack connects to a remote server and successfully fetches a real web page over the real internet.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** KEEP. Labs ship with tests.
- **Stanford CS144**: cs144.github.io. 💲 Kurose & Ross; free alternative: Peterson & Davie, *Computer Networks: A Systems Approach* (book.systemsapproach.org).

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The test suite that comes with each CS144 checkpoint.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Berkeley CS168; Peterson & Davie, Computer Networks: A Systems Approach; Stevens, TCP/IP Illustrated Vol 1; Beej's Guide.

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B18 - Real Analysis|← Real Analysis]] | [[00 - Start Here|Start Here]] | [[B20 - Algorithms II|Algorithms II →]]
