---
title: "09 — Resources"
id: "MOD09-RES"
type: "reference"
module: "09-networking"
phase: "D"
order: 1230
prerequisites: []
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

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — Computer Networking: A Top-Down Approach (video lectures)**, Jim Kurose (with Keith Ross). Free on YouTube: [playlist](https://www.youtube.com/playlist?list=PLvFG2xYBrYASIUH_y2hYaMCro8KUe_yL8) · the authors' [lecture page](https://gaia.cs.umass.edu/kurose_ross/lectures.php).
- **Why it fits:** the lectures are the book's own sections taught by its author, and Kurose & Ross is this module's main text. They follow the book's numbering, so a section you read is a section you can watch. Chapter 3 (reliable data transfer, TCP, congestion control) is the theory behind Courier, step by step.

**Alternate — Networking tutorial**, Ben Eater (YouTube). Free: [playlist](https://www.youtube.com/playlist?list=PLowKtXNTBypH19whXTVoG3oKSuOcw_XeW).
- **Why:** bottom-up where Kurose is top-down. Ben Eater decodes real Ethernet frames, ARP, IP and TCP packets by hand, which is exactly the skill Packet Telescope and the Wireshark lab practise.

### Lecture-to-vault map

Kurose entries use the book section numbers shown in the video titles. Ben Eater numbers are playlist positions.

| Vault item | Kurose & Ross (primary) | Ben Eater (alternate) |
| :-- | :-- | :-- |
| [Lab 01 — Wireshark field trip](labs/lab-01-wireshark-field-trip.md) | 1.5 Layering, encapsulation · 2.2 The Web and HTTP (parts 1–2) | videos 7–10 (the OSI lower layers, IP, ARP, looking at ARP and ping packets) |
| [Lab 02 — DNS by hand](labs/lab-02-dns-by-hand.md) | 2.4 The Domain Name System (DNS) | — |
| [Lab 03 — A network in your laptop](labs/lab-03-a-network-in-your-laptop.md) | 1.4 Performance · 4.1 Introduction to the Network Layer · 4.3 The Internet Protocol (parts 1–2) | video 11 (hop-by-hop routing) |
| [Packet Telescope](projects/packet-telescope/spec.md) (pcap) | 1.5 Layering, encapsulation · 3.3 Connectionless Transport: UDP · 3.5 TCP (part 1) · 4.3 The Internet Protocol · 6.1 Introduction to the Link Layer | videos 5–6 (framing, frame formats) · 8–10 (IP, ARP) · 12–13 (TCP) |
| [Courier](projects/courier/spec.md) (reliable transport over UDP) | 3.4 Principles of Reliable Data Transfer (parts 1–2) · 3.5 TCP Reliability, Flow Control, and Connection Management (parts 1–2) · 3.6 Principles of Congestion Control · 3.7 TCP Congestion Control | video 13 (a TCP connection walkthrough) |
| [Lantern](projects/lantern/spec.md) (HTTP/1.1 server) | 2.1 Principles of the Application Layer · 2.2 The Web and HTTP (parts 1–2) · 2.7 Socket programming | — |
