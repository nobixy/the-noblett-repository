---
title: "Lab 01 — Wireshark Field Trip"
module: "09-networking"
hours: 8
---

# Lab 01 — Wireshark Field Trip

**Goal:** see the internet's layers in real packets from your own machine: ARP, DNS, a TCP handshake, a plain HTTP request, a TLS handshake, and the trick behind `traceroute`.

**Time:** about 8 hours, in three sessions.

**Tools:** Wireshark (`wireshark-qt`; add yourself to the `wireshark` group to capture without root: `sudo usermod -aG wireshark $USER`, then log out and in), `tcpdump`, `curl`, `dig`, `traceroute` (or `tracepath`).

**Etiquette:** capture only your own traffic on your own network.

---

## Session 1 — Layers and encapsulation (3 hours)

Every packet is **nested**: application data inside a transport header (UDP/TCP), inside a network header (IP), inside a link frame (Ethernet or Wi-Fi). Each layer only reads its own header.

```
[ Ethernet | IP | TCP | HTTP data ............ ]
  14 bytes  20+  20+
```

1. Start a capture on your main interface. In a terminal: `curl http://example.com/` (plain HTTP — unencrypted, so you can read it). Stop the capture.
2. Filter: `http`. Select the GET request. In the middle pane, expand each layer: Ethernet (MAC addresses), IPv4 (source and destination addresses, TTL, protocol = 6 for TCP), TCP (ports, sequence number, flags), HTTP (the request text).
3. In the bottom pane (raw bytes), click each field and see which bytes it is. Find the IPv4 header's first byte (`0x45`): version 4, header length 5 × 4 = 20 bytes. [R] Draw the IPv4 header layout from what you see, then compare with a reference.
4. **Follow the TCP stream** (right-click → Follow → TCP Stream): the whole request and response as text.

**Find and write down:** your machine's IP and MAC address; the router's MAC address; example.com's IP address; the TCP ports used (which one is 80, and where does the other come from?).

---

## Session 2 — Handshakes and lookups (3 hours)

### DNS

Capture while running `dig example.com` (or `curl` to a site you haven't visited). Filter `dns`. Find the query and the response; which transport (UDP), which port (53), which server? Expand the answer section. (Lab 02 builds these packets by hand.)

### ARP

Clear your ARP cache entry for the router (`sudo ip neigh flush dev <iface>`), capture, and `ping -c 1 <router-ip>`. Filter `arp`. "Who has 192.168.1.1? Tell 192.168.1.23" — and the reply. [W] Why does a machine need ARP before it can send an IP packet on a local network?

### The TCP handshake and teardown

Filter `tcp.port == 80` on the curl capture. Find the **three-way handshake** — SYN, SYN-ACK, ACK — and the sequence numbers in each (use *Edit → Preferences → Protocols → TCP → Relative sequence numbers* on and off). Then the FIN/ACK teardown. Draw the time diagram with both sides as vertical lines and packets as diagonal arrows [R]. Measure the **round-trip time**: the time between SYN and SYN-ACK.

### TLS

Capture `curl https://example.com/`. Filter `tls`. You'll see a **ClientHello** (which includes the site name in plain text — the "SNI" field: find it), a ServerHello, then encrypted "Application Data." [W] What can someone watching your network still learn from an HTTPS connection, and what can't they?

---

## Session 3 — traceroute (2 hours)

Each IP packet has a **TTL** (time to live): every router decrements it, and a router that decrements it to zero discards the packet and sends back an **ICMP "time exceeded"** message. `traceroute` exploits this: it sends packets with TTL = 1, 2, 3, … and each router along the way reveals itself by complaining.

1. Capture while running `traceroute example.com` (or `tracepath`). Filter `icmp`.
2. Match each "time exceeded" reply to the TTL of the probe that caused it.
3. Run `traceroute` to a server on another continent. Look at the jump in round-trip time at the ocean crossing. Compare with the speed-of-light minimum you computed in the [Magnitudes Field Guide](../../00-foundations/math/projects/magnitudes-field-guide/spec.md).

---

## Done when

- [ ] Annotated screenshots of each layer of an HTTP request.
- [ ] Notes on DNS, ARP, the handshake (with your time diagram), TLS, and traceroute.

## Retrieval and reflection

1. **[R]:** the four layers and one header field you saw at each; the three-way handshake; what TTL does; what ARP does.
2. **[F] (spoken, 3 min):** "What happens on the wire when I type an address and press Enter?" — using your captures.
