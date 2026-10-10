---
title: "09 — Networking"
module: "09-networking"
hours: 200
tags: [module, networking, protocols]
---

# 09 — Networking

**How computers talk — and how to make talk reliable over a network that loses, delays, duplicates, and scrambles messages.** You'll decode real packets from your own network byte by byte, resolve domain names by talking to the internet's root servers yourself, build a virtual lab of networked machines inside your laptop, and then write two serious protocols implementations: **Courier**, your own reliable transport protocol over UDP, with connection setup, sliding windows, selective acknowledgments, adaptive timeouts, flow control, and congestion control; and **Lantern**, an HTTP/1.1 web server that your browser engine (Module 10) will talk to.

---

## Prerequisites

- [Relay](../01-intro-cs-taste/projects/relay-chat/spec.md) (reread it: Courier is its grown-up form).
- [07 Systems Programming](../07-systems-programming/overview.md) (C, system calls, Crate's binary formats and CRCs); [08 OS](../08-operating-systems/overview.md) (concurrency).
- [05 DSA](../05-data-structures-and-algorithms/overview.md) (ring buffers, hash tables, heaps for timers).
- Math M11 (logs, growth); Module 03 Unit 8 (probability) for loss models.

## Objectives

By the end you will be able to:
1. Explain the layers of the internet (link, network, transport, application) and identify each in a real packet capture.
2. Parse Ethernet, IPv4/IPv6, UDP, TCP, and DNS headers from raw bytes.
3. Resolve a domain name iteratively from the root servers.
4. Build virtual networks with namespaces and impose delay, loss, and bandwidth limits.
5. Design and specify a protocol in RFC style, and implement a reliable, flow- and congestion-controlled transport over UDP.
6. Implement an HTTP/1.1 server with correct framing, keep-alive, conditional and range requests, concurrency, and defences against malformed and slow clients.
7. Measure throughput, latency, and fairness, and explain the results with simple models.

## Sequence and time

| Order | Item | Hours | Concepts |
| :-- | :-- | --: | :-- |
| 1 | [Lab 01 — Wireshark Field Trip](labs/lab-01-wireshark-field-trip.md) | 8 | layers, encapsulation, ARP, DNS, TCP handshake, TLS, traceroute |
| 2 | [Lab 02 — DNS by Hand](labs/lab-02-dns-by-hand.md) | 8 | binary formats in network byte order, UDP, name compression, iterative resolution |
| 3 | **[Packet Telescope](projects/packet-telescope/spec.md)** | 30 | pcap format, header parsing, checksums, flows, TCP analysis |
| 4 | [Lab 03 — A Network in Your Laptop](labs/lab-03-a-network-in-your-laptop.md) | 10 | namespaces, veth, netem, iperf3, the Mathis model |
| 5 | **[Courier](projects/courier/spec.md)** | 90 | protocol design, handshakes, sliding windows, SACK, RTO estimation, flow and congestion control, fairness |
| 6 | **[Lantern](projects/lantern/spec.md)** | 55 | HTTP/1.1 framing, keep-alive, caching headers, ranges, concurrency models, robustness |
| | **Total** | **~200** | |

At about 12 hours a week, about 17 weeks. Courier is the heart of the module; give it time.

## How the projects map to the layers

| Layer | What you do |
| :-- | :-- |
| Link (Ethernet, Wi-Fi) | Read frames in Packet Telescope; ARP in Lab 01 |
| Network (IP) | Parse IPv4/IPv6; traceroute; virtual networks in Lab 03 |
| Transport (UDP, TCP, **Courier**) | Analyse TCP in Packet Telescope; **build** Courier over UDP |
| Application (DNS, HTTP) | DNS by hand; **build** Lantern |

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Draw header layouts (IPv4, UDP, TCP, Courier) and state diagrams from memory. Study Deck cards for port numbers, header fields, and formulas (RTO, Mathis). |
| **F** | Recorded explanations: how a sliding window keeps the pipe full; why exponential backoff; how a web page request travels (your [Explain-a-System](../00-foundations/english/projects/explain-a-system/spec.md) explainer 4, rewritten). |
| **W** | The Courier spec's rationale section: every header field and every timer defended against an alternative. |
| **S** | Sender and receiver event handlers as subgoal comments; HTTP request parsing steps. |
| **I** | Packet analysis, protocol building, and measurement alternate. |
| **D** | Protocol bugs depend on timing: seeded gremlins and captured traces make them reproducible; stuck notes for the rest. |
| **T** | RFC-style protocol specification (Courier), design docs, measurement reports, demos. |

## Environment

`wireshark-qt` (or `tshark`), `tcpdump`, `iproute2` (`ip`, `tc`), `iperf3`, `curl`, `dig` (from `bind` or `ldns`), and optionally `wrk` for HTTP benchmarks. Some labs need `sudo` for namespaces and `tc` — **only on your own machine**, and Lab 03 shows how to undo everything.

**Network etiquette:** query public servers (root DNS servers, public resolvers) politely — a handful of requests while learning, never floods; capture only your own traffic.

## Connections

- **Back:** Relay (protocols, the gremlin, stop-and-wait), Crate (CRC32, binary formats), Tone Loom (byte order — networks are **big-endian**), Ratio Workshop and Fare Detective (bandwidth and latency models), Scheduler Arena (fairness), Seedling (what's under the sockets), M11 (logs and the Mathis formula's square root).
- **Forward:** [10 Browser Engine](../10-browser-engine/overview.md) — Glimpse fetches pages from Lantern; [13 Capstone](../13-capstone/overview.md) — HTTP over Courier.

## Module close

1. **Cumulative retrieval [R] (60 min):** the four layers with an example protocol each; IPv4, UDP, TCP, and Courier header layouts; the RTO formulas; HTTP request and response framing.
2. **Rewrite [Explain-a-System](../00-foundations/english/projects/explain-a-system/spec.md) explainer 4** ("loading a web page") from scratch, with a packet capture as evidence.
3. **Showcase [T]:** a 6-minute recording: Packet Telescope on a capture of Courier transferring a file through the gremlin, then Lantern serving a page.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Next:** [10 Browser Engine](../10-browser-engine/overview.md) and [11 Databases](../11-databases/overview.md).
