---
title: "Project: Packet Telescope"
id: "MOD09-PRJ-packet-telescope"
type: "project"
module: "09-networking"
phase: "D"
order: 1200
prerequisites: [MOD09-LAB02, MOD07-PRJ-crate, MOD02-PRJ-tone-loom]
artifact: "scope: a packet-capture analyser written from scratch — pcap reader; Ethernet, ARP, IPv4/IPv6, ICMP, UDP, TCP, and DNS decoders with checksum verification; one-line summaries; flow tables; TCP connection analysis; and a dissector for your own protocols"
deliverable: "Design doc + accuracy report (compared with tshark) + short demo"
---

# Project: Packet Telescope

| | |
| :-- | :-- |
| **Module** | 09 Networking |
| **Prerequisites** | Labs 01–02 of this module; Crate and Tone Loom (binary formats); Module 05 (hash tables) |
| **You build** | `scope`, your own packet analyser. It reads capture files written by `tcpdump`, decodes every layer by hand from the raw bytes, verifies checksums, prints a one-line summary per packet, groups packets into flows, reconstructs TCP connections (handshakes, retransmissions, round-trip times), and decodes your own protocols (Relay and Courier). Its output is checked against Wireshark's command-line twin, `tshark` |
| **Deliverable** | Design doc, accuracy report, and demo |

---

## Why this matters

Wireshark showed you packets (Lab 01). Now you'll *be* Wireshark. Writing the decoders forces you to know every header field, every byte order, and every checksum — knowledge you'll use when building Courier and Lantern, and whenever a network misbehaves in real life ("the packets don't lie"). It's also a substantial exercise in parsing untrusted binary data safely — every capture is someone else's bytes.

**Real-world analogs:** Wireshark/tshark, tcpdump, Zeek, intrusion-detection systems.

---

## Milestones

### Milestone 1 — Design doc and the pcap reader

1. **Design doc v1** (3 pages): the decoder architecture (one decoder per protocol, each returning a structured result and the remaining payload — so layers chain), how unknown or malformed packets are handled, the flow key, the outputs.
2. **pcap format:** a 24-byte global header (magic number — which also tells you the file's **byte order** and timestamp precision —, version, snap length, link type) then, per packet, a 16-byte record header (timestamp seconds, microseconds or nanoseconds, captured length, original length) and the bytes. Look up the format (it's short) and implement it. Capture files with `tcpdump -w file.pcap` (classic pcap format). Handle both byte orders and both timestamp precisions.

**Done when:** `scope info file.pcap` prints the link type and the number of packets and bytes, matching `capinfos` (from Wireshark's tools).

### Milestone 2 — Link and network layers

1. **Ethernet II:** destination and source MAC, EtherType (0x0800 IPv4, 0x86DD IPv6, 0x0806 ARP), 802.1Q VLAN tags (decode or skip — decide).
2. **ARP** requests and replies.
3. **IPv4:** every header field; options length; **verify the header checksum** (the 16-bit one's-complement sum — look up the algorithm; implement it; [W] why does adding up 16-bit words with end-around carry make a checksum that's easy to update when TTL changes?); fragmentation fields.
4. **IPv6:** fixed header; follow simple extension headers to the next protocol.
5. **ICMP / ICMPv6:** type and code names (echo, time exceeded, destination unreachable).

### Milestone 3 — Transport and DNS

1. **UDP** (with checksum over the **pseudo-header** — source and destination IP, protocol, length — plus the UDP header and data).
2. **TCP:** ports, sequence and acknowledgment numbers, flags, window, options (MSS, window scale, SACK permitted, timestamps), checksum (pseudo-header again).
3. **DNS** over UDP 53: reuse your Lab 02 parser (with its compression-loop protection).
4. **One-line summaries**, like tcpdump:
   ```
   0.000123 10.0.0.1:51234 → 93.184.215.14:80 TCP [S] seq=0 win=64240 mss=1460
   0.020456 10.0.0.1:53211 → 1.1.1.1:53 DNS query A example.com
   ```
   With relative sequence numbers per connection (like Wireshark).

**Accuracy test:** for three captures you made (a web page load, a DNS-heavy session, a big download), compare your fields with `tshark -T fields -e …` output for the same packets (a second witness) — automate the comparison in a script.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: draw the IPv4, UDP, and TCP headers from memory with field widths.

### Milestone 4 — Flows and TCP analysis

1. **Flow table:** group packets by 5-tuple (protocol, source IP and port, destination IP and port — treat both directions as one flow) in a hash map. Report packets, bytes, duration, and average rate per flow, sorted by bytes.
2. **TCP connection analysis:** for each connection, the handshake (with SYN → SYN-ACK RTT), data bytes each way, **retransmissions** (a segment whose sequence range was already seen), **duplicate ACKs**, **zero windows**, and how it ended (FIN or RST).
3. **Try it on a lossy transfer:** run `iperf3` through your Lab 03 bench with 2% loss, capture it, and check your retransmission count against `tshark -z` statistics or Wireshark's "Expert Info."

**Done when:** flow and TCP reports agree with Wireshark's on three captures.

### Milestone 5 — Dissect your own protocols

1. **Relay** (text over TCP and UDP) and **Courier** (CP/1 over UDP): when a UDP packet is on your chosen port, decode it with your CP/1 header layout, verify its CRC32, and print type, connection ID, sequence, ack, SACK bits, window.
2. **Courier flow analysis:** per connection, the handshake, retransmissions, fast retransmits (visible from SACK patterns), and the sender's in-flight count over time (plot it — it's cwnd seen from outside).

**Done when:** a capture of a Courier transfer through Gremlin 2 is fully decoded and its retransmission count matches Courier's own logs.

### Milestone 6 — Robustness

Captures are untrusted input. Fuzz `scope` with mutated pcap files (Crate's fuzzer, again): no crashes, no infinite loops (DNS pointers!), clear "malformed" annotations instead. Also handle truncated packets (captured length < original length: decode what's there).

---

## Common pitfalls

- **pcap byte order** (file header) vs **network byte order** (packet contents) — two different things.
- **IPv4 header length** is in 4-byte units; options exist.
- **TCP data offset** is also in 4-byte units.
- **Checksum offload:** packets captured on the *sending* machine often have wrong checksums because the network card computes them later. Wireshark marks these; so should you (as "unverified, likely offloaded"), not as errors.
- **Sequence number wrap** in TCP analysis (modular comparison, as in Courier).

## Communication deliverable

1. **Design doc** v1 → v2.
2. **Accuracy report** (2 pages): fields compared with tshark across captures, disagreements explained, the lossy-transfer analysis, and the fuzzing result.
3. **Demo:** summaries of a web page load, the flow table, a TCP connection analysis, and a decoded Courier transfer.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Header layouts from memory |
| **F** | How a checksum works; what a retransmission looks like on the wire |
| **W** | One's-complement checksum design; offload marking; per-protocol decoder chaining |
| **S** | Decoder subgoals: check length → read fields → verify → hand payload onward |
| **T** | Design doc, report, demo |

## Stretch goals

- **Live capture** with raw sockets (`AF_PACKET`, needs root — or `CAP_NET_RAW`) instead of files.
- **TLS ClientHello** decoding to show the server name (SNI).
- **HTTP/1.1 reassembly:** reconstruct requests and responses from TCP streams (handle out-of-order segments) — useful for testing Lantern.
- **pcapng** format support.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| pcap reader | Both byte orders and precisions; matches capinfos | One variant | Fragile |
| Decoders | Ethernet, ARP, IPv4/6, ICMP, UDP, TCP, DNS with checksums | Most | Few |
| Accuracy | Automated tshark comparison on 3 captures | Manual spot checks | None |
| Flows and TCP | Flow table + retransmissions + RTT, matching Wireshark | Flows only | Missing |
| Own protocols | Courier and Relay decoded; cwnd-from-outside plot | One | Neither |
| Robustness | Fuzzed; truncated packets handled | Some | Crashes |
| Communication | Doc, report, demo | Two | One |

**Done when:** every area at least 2; Decoders and Accuracy at 3.

## Connections

- **Back:** Lab 01 (Wireshark), Lab 02 (DNS parser), Crate (fuzzing, CRC), Relay (your first protocol).
- **Forward:** Courier (your debugging microscope), Lantern (seeing HTTP on the wire), the capstone.

> **Originality note:** this project's milestones and own-protocol dissection were designed for this curriculum.
