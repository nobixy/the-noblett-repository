---
title: "09 — Resources"
module: "09-networking"
---

# 09 — Resources

*Pointers only. The labs and projects are the course.*

## Textbooks
- **Kurose & Ross, *Computer Networking: A Top-Down Approach*** (book) — chapters 1–4 match this module; chapter 3 (transport: reliable data transfer, TCP, congestion control) is the best second explanation for Courier.
- **Larry Peterson & Bruce Davie, *Computer Networks: A Systems Approach*** (free online at book.systemsapproach.org) — clear and systems-minded; its "TCP Congestion Control" book in the same series goes deeper.

## Standards (primary sources)
- **RFC 768** (UDP) — read in full; it's three pages and a model of concise specification.
- **RFC 9293** (TCP, 2022) — skim for structure and the state diagram.
- **RFC 6298** (computing TCP's retransmission timer) — the RTO formulas.
- **RFC 2119 / RFC 8174** — what MUST, SHOULD, and MAY mean.
- **RFC 1035** (DNS) — sections 4.1 (message format) and 4.1.4 (compression).
- **RFC 9110 / RFC 9112** (HTTP semantics and HTTP/1.1) — look things up as Lantern needs them.
- **RFC 9000** (QUIC) — sections on connection IDs and loss detection, for Courier's stretch goals.

## Tools
- **Wireshark User's Guide** and `man tshark`, `man tcpdump`, `man pcap-savefile` (the pcap file format), `man tc-netem`, `man ip-netns`.
- **iperf3**, **wrk** documentation.

## Further
- **Julia Evans, "Networking! ACK!" and "How DNS Works"** zines — friendly visual explanations.
- **Jacobson, "Congestion Avoidance and Control" (1988)** — the classic paper behind slow start and AIMD; readable and historically important. Try the three-pass reading method (LM13) on it.
- **Mathis, Semke, Mahdavi, Ott, "The Macroscopic Behavior of the TCP Congestion Avoidance Algorithm" (1997)** — the model tested in Lab 03.

## Video and course companions
Free YouTube series and Coursera/edX/MIT OCW courses for this module are listed in [courses-and-videos.md](../courses-and-videos.md#modules-0113). Use them with the [V protocol](../study-protocols.md#v--watch-actively): lectures and quizzes as second explanations; this module's own projects, not the courses' assignments.
