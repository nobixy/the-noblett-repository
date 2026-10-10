---
title: "Project: Courier"
module: "09-networking"
hours: 90
artifact: "Courier (CP/1): a message-oriented reliable transport protocol over UDP — your RFC-style specification, a library implementation with cookie handshake, sliding windows, selective acknowledgments, adaptive retransmission timeouts, flow control, AIMD congestion control, keepalive and teardown — plus Gremlin 2 (an impairment proxy), a file-transfer tool, and a measurement campaign"
deliverable: "CP/1 specification (RFC style) + design doc + evaluation report (correctness, throughput, fairness, vs TCP) + 6-minute demo"
---

# Project: Courier

| | |
| :-- | :-- |
| **Module** | 09 Networking |
| **Time** | About 90 hours (8–10 weeks) |
| **Prerequisites** | [Relay](../../../01-intro-cs-taste/projects/relay-chat/spec.md) (stop-and-wait, the gremlin); Labs 01–03 of this module (the namespace test bench); Crate (CRC32); Module 05 (ring buffers, heaps) |
| **Language** | Python is recommended (clarity; performance targets are set accordingly). C is allowed if you want the challenge — targets then double. |
| **You build** | **Courier**, your own reliable transport protocol, specified like an internet standard and implemented as a library with a socket-like API. It delivers **messages** (not a byte stream) reliably and in order over UDP — through loss, duplication, reordering, corruption, and limited bandwidth — while sharing the network fairly. You also build **Gremlin 2**, the hostile network it must survive, a file-transfer tool on top, and a campaign of measurements comparing it with TCP |
| **Deliverable** | Protocol specification, design doc, evaluation report, and demo |

---

## Why this matters

Reliable delivery over an unreliable network is one of the central achievements of computer science. TCP does it for nearly every connection you've ever made, but its machinery is hidden in the kernel. In Relay you built the simplest version (stop-and-wait) and measured why it's slow. Courier is the full idea: many messages in flight, acknowledgments that say exactly what arrived, timers that adapt to the network, a receiver that can say "slow down, I'm full," and a sender that backs off when the network itself is congested.

You'll also write the protocol **specification first**, in the style of the internet's RFCs — the most precise kind of engineering writing, where every MUST and SHOULD matters, because two independent implementations must work together using only the document.

**Real-world analogs:** TCP, QUIC (which also runs over UDP, with connection IDs and selective acknowledgments), SCTP (message-oriented), reliable UDP layers in games.

> **Originality:** CP/1's packet format, handshake, message semantics, and this milestone and test plan were designed for this curriculum. It teaches the same core ideas as TCP and as university transport labs, but it is not modelled on any course's framework, starter code, or test harness: you write the protocol, the impairment proxy, and the tests yourself.

---

## CP/1 at a glance (your starting point)

### Service

- **Connections** between two endpoints, identified by a 32-bit **connection ID** chosen by the server (so a connection survives the client's address changing — a QUIC idea, as a stretch goal).
- **Messages**: the application sends and receives whole messages of 0–1,200 bytes. **Boundaries are preserved** (unlike TCP's byte stream — Relay's framing problem disappears). Messages are delivered **reliably, exactly once, in order**.
- **Full duplex:** both sides send and receive at once.

### Packet format (32-byte header, big-endian)

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-------+-------+---------------+-------------------------------+
|  Ver  | Type  |     Flags     |        Payload Length         |
+-------+-------+---------------+-------------------------------+
|                         Connection ID                         |
+---------------------------------------------------------------+
|                    Sequence Number (message #)                |
+---------------------------------------------------------------+
|              Cumulative Ack (next message # expected)         |
+---------------------------------------------------------------+
|                 SACK Bitmap (ack+1 … ack+32)                  |
+-------------------------------+-------------------------------+
|        Receive Window         |           Reserved            |
+-------------------------------+-------------------------------+
|                    Timestamp (sender, ms)                     |
+---------------------------------------------------------------+
|                   CRC32 (header + payload)                    |
+---------------------------------------------------------------+
|                    Payload (0–1,200 bytes) …                  |
```

- **Ver** = 1. **Type:** HELLO, CHALLENGE, CONFIRM, DATA, ACK, CLOSE, CLOSE_ACK, PING, RESET.
- **Sequence numbers count messages**, starting from a random initial value chosen in the handshake (why random? [W]).
- **Cumulative Ack** = the next message number the receiver expects (everything before it has arrived). **SACK bitmap:** bit i set means message (ack + 1 + i) has also arrived — so the sender knows exactly which gaps to fill.
- **Receive Window:** how many more messages the receiver can buffer (flow control).
- **Timestamp:** the sender's clock; the receiver **echoes** it in ACKs so the sender can measure RTT precisely — even for retransmitted messages (Karn's problem, solved [W]).
- **CRC32** over header (with this field zero) and payload: a corrupted packet is silently dropped (and later retransmitted).

### Handshake: a three-step cookie exchange

```
client                                   server
  | ---- HELLO (client nonce) ------------> |   server keeps NO state yet
  | <--- CHALLENGE (cookie) --------------- |   cookie = hash(client addr, nonce, server secret, time slot)
  | ---- CONFIRM (cookie, client ISN) ----> |   server checks cookie; NOW creates the connection
  | <--- ACK (connection ID, server ISN) -- |
```

**[W] Why a cookie?** A server that allocates memory on every HELLO can be exhausted by an attacker sending millions of forged HELLOs (TCP's "SYN flood"). With a cookie, the server only commits memory once the client proves it can receive packets at its claimed address.

### Reliability, timers, flow, congestion

- **Sliding window:** the sender may have up to `min(send window, receiver window, congestion window)` unacknowledged messages in flight.
- **Retransmission timeout (RTO):** estimated from RTT samples with the standard smoothed estimator (as in RFC 6298): SRTT ← (7/8)·SRTT + (1/8)·R; RTTVAR ← (3/4)·RTTVAR + (1/4)·|SRTT − R|; RTO = SRTT + 4·RTTVAR, clamped to [200 ms, 60 s]; **double the RTO** on each timeout (exponential backoff).
- **Fast retransmit:** when the SACK bitmap shows 3 later messages arrived but message n hasn't, resend n immediately without waiting for the timer.
- **Congestion control (AIMD):** a congestion window `cwnd` (in messages) starting at 2; **slow start** (+1 per ACKed message, doubling per RTT) until a threshold; then **additive increase** (+1 per RTT); on loss detected by fast retransmit, **halve** `cwnd`; on timeout, reset to 2.
- **Teardown:** CLOSE / CLOSE_ACK after all data is acknowledged; a lingering period to absorb late duplicates; **PING** keepalives and an idle timeout; **RESET** for unknown connection IDs.

You may change any of this — but every change goes into the specification with a rationale.

---

## Milestones

### Milestone 1 — The specification (before any code)

Write **`CP1.md`** in RFC style (read RFC 768 — UDP, 3 pages — and skim RFC 9293 — TCP — for tone and structure):
1. **Introduction and terminology**, with the RFC 2119 keywords (MUST, SHOULD, MAY) defined and used precisely.
2. **Packet format** (the diagram and every field).
3. **Connection state machine:** states (e.g. CLOSED, HELLO_SENT, ESTABLISHED, CLOSING, LINGER) and every transition, as a diagram and a table (Crosswalk's method).
4. **Sender and receiver rules**, step by step.
5. **Timers** (RTO, keepalive, idle, linger) with exact formulas.
6. **Flow and congestion control.**
7. **Error handling:** bad CRC, unknown connection, duplicate packets, packets for a closed connection, window violations.
8. **Security considerations** (the cookie; what CP/1 does *not* protect against: eavesdropping, tampering by a party who can recompute the CRC — and why CRC is not a security mechanism [W]).
9. **Design rationale** — at least eight decisions with rejected alternatives.

**Done when:** the spec is complete enough that a stranger could implement a compatible endpoint. Get a review if you can (E10).

### Milestone 2 — Gremlin 2 and the test bench

Upgrade Relay's gremlin into **Gremlin 2**, a UDP proxy (runs between namespaces, or on one machine):
- drop (independent probability) and **burst loss** (a two-state model: a "good" state with low loss and a "bad" state with high loss, switching randomly — the Gilbert–Elliott model; Module 12 makes it precise);
- duplicate; reorder (random delay with jitter); **corrupt** (flip random bits — the CRC must catch it);
- **rate limit** with a **token bucket** (bytes per second, burst size) and a **queue limit** (packets beyond it are dropped — this is how real routers create the loss that congestion control reacts to);
- **seeded**, with a log of every decision; separate settings for each direction.

Also script the Lab 03 namespace setup with netem as a second, independent impairment source.

**Done when:** Gremlin 2's measured behaviour matches its settings (e.g. 10% drop configured → 10% ± 1% observed over 100,000 packets; rate limit within 5%).

### Milestone 3 — Packets, CRC, handshake, and stop-and-wait

1. **Encode/decode** packets with `struct` (`!` = big-endian) and CRC32; property test: decode(encode(p)) == p for 10,000 random packets; any single flipped bit is detected.
2. **Event-driven core:** one loop using `selectors` (or `asyncio`) handling incoming packets and **timers** kept in a heap (Module 05) ordered by deadline.
3. **Handshake** with cookies; connection table keyed by connection ID; RESET for unknown IDs.
4. **Stop-and-wait data transfer** (window = 1) — Relay's design, now on CP/1 packets.
5. **API:**
   ```python
   server = courier.listen(("10.0.0.2", 7000))
   conn = server.accept()
   msg = conn.recv()            # blocks until a whole message arrives
   conn.send(b"hello")          # may block if the window is full
   conn.close()
   ```

**Done when:** 1,000 messages pass through Gremlin 2 at 20% loss + 10% duplication + reordering + 1% corruption, delivered exactly once in order.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: the handshake and the connection state machine from memory.

### Milestone 4 — Sliding window, SACK, adaptive RTO

1. **Sender buffer:** a ring buffer (Module 05 Lab 03) of unacknowledged messages, each with its send time and retransmission count.
2. **Receiver buffer:** out-of-order messages held until the gap fills; deliver in order; build the SACK bitmap.
3. **RTO estimator** with timestamp echo; exponential backoff; fast retransmit on 3 SACKed-later messages.
4. **Fixed window size W** (no congestion control yet). Measure throughput for W = 1, 4, 16, 64 at 100 ms RTT and 0% loss. Compare with the theoretical maximum: W messages per RTT. (Relay's Milestone 5 question, answered.)

**Tests:** unit tests for the receiver's buffer and SACK construction (feed message numbers in random orders); the RTO estimator against hand-computed sequences; integration: 10,000 messages at each Gremlin 2 setting; **a deterministic simulation mode** where time is simulated (fake clock, Module 02) and packets pass through an in-memory gremlin — so a whole transfer under loss runs in milliseconds and is exactly repeatable.

**Done when:** correctness across settings, and the window throughput table matches the W/RTT model.

**Checkpoint:** Milestone Checkpoint. Feynman target: *how a sliding window keeps the pipe full*. Why-ladder targets: *why echo timestamps instead of timing the original send?* and *why exponential backoff?*

### Milestone 5 — Flow control and congestion control

1. **Flow control:** the receiver's application reads slowly (sleep between `recv` calls); the advertised window shrinks to 0; the sender stops and sends **window probes**; when the app reads, the window reopens. No message may be dropped for lack of buffer space.
2. **Congestion control:** AIMD with slow start, as specified. Log `cwnd` over time; plot it (the classic **sawtooth**).
3. **Fairness:** two Courier flows through one rate-limited Gremlin 2 bottleneck (e.g. 10 Mbit/s, queue of 50 packets). Measure each flow's throughput over 60 s and Jain's fairness index (Scheduler Arena). Then a Courier flow against a TCP flow (`iperf3`) through a netem/tbf bottleneck in your namespaces: who wins? [W] Why might your AIMD be more or less aggressive than Linux's TCP?

**Done when:** flow-control test passes; sawtooth plotted; fairness ≥ 0.9 between two Courier flows.

### Milestone 6 — Teardown, keepalive, robustness

1. CLOSE/CLOSE_ACK with linger; PING keepalives; idle timeout; RESET handling.
2. **Hostile input:** fuzz the packet parser (Crate's mutation fuzzer, adapted): random and mutated packets at an established connection must never crash it, never deliver bad data, and never create state for a forged connection ID.
3. **Kill tests:** kill one endpoint mid-transfer; the other must detect it (keepalive/idle timeout) and report an error to its application within the specified time.

### Milestone 7 — The evaluation campaign

Build **`cpost`**, a file-transfer tool on Courier (`cpost send FILE HOST:PORT`, `cpost recv DIR`), which verifies a SHA-256 of every file.

Measure, in the namespace bench (3 runs each, medians):
1. **Correctness matrix:** 50 MB files at every combination of loss {0, 1, 5, 20%}, reorder {off, on}, duplication {0, 5%}, corruption {0, 1%} — every transfer verified.
2. **Throughput vs loss** at 10 Mbit/s and 100 ms RTT, compared with `iperf3` TCP on the same path and with the Mathis prediction (Lab 03).
3. **Throughput vs RTT** at 1% loss.
4. **cwnd and RTO traces** for one lossy transfer, plotted over time.
5. **Fairness** results from Milestone 5.

**Targets** (Python implementation): every correctness transfer verified; at 0% loss, ≥ 70% of a 10 Mbit/s link; at 1% loss and 100 ms RTT, within a factor of 2 of TCP. (C implementation: ≥ 90% and within 1.5×.) If you miss a target, the report must explain why with evidence — that's a valid result too.

---

## Testing guidance

- **Deterministic simulation mode** (fake clock + in-memory gremlin) for fast, repeatable tests of every protocol rule; **namespace bench** for real-world runs.
- **Invariant checks** in debug mode: the receiver never delivers out of order or twice; the sender never has more in flight than the effective window; sequence numbers only move forward.
- **Packet captures:** extend Packet Telescope to decode CP/1 (a dissector for your own protocol!) and inspect real transfers.

## Common pitfalls

- **Sequence-number wrap-around** after 2³² messages: compare with modular arithmetic ("is a before b?" = `(b - a) mod 2³² < 2³¹`) — M03 and M07 again.
- **Timer storms:** retransmitting every message on every timeout instead of the oldest; or resetting the timer on every ACK incorrectly.
- **Retransmitted packets used as RTT samples** without timestamps (Karn's problem).
- **Flow-control deadlock:** receiver window 0 and the window update is lost — that's why window probes exist.
- **Busy-waiting** in the event loop: use timeouts on `select` computed from the next timer deadline.

## Communication deliverable

1. **`CP1.md`** — the RFC-style specification (v1 before code; final with a change log). This is the most demanding document in the curriculum so far; revise it at least twice.
2. **Design doc** (implementation architecture: event loop, buffers, timers, the simulation mode).
3. **Evaluation report** (4 pages, E10): the correctness matrix, throughput plots vs TCP and the model, cwnd/RTO traces, fairness — with honest explanations.
4. **Demo (6 minutes):** a file crossing a hostile Gremlin 2 with live stats (cwnd, RTO, retransmissions), a Packet Telescope view of CP/1 packets, and the fairness experiment.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Header layout, state machine, RTO formulas, AIMD rules — from memory before each milestone |
| **F** | Sliding windows; why a cookie; why congestion control is needed at all ("tragedy of the commons") |
| **W** | Eight+ rationales in the spec; random ISNs; timestamp echo; backoff; CRC vs security; AIMD aggressiveness |
| **S** | Sender and receiver event handlers as subgoals; the spec's step-by-step rules |
| **I** | Protocol design, data structures, measurement, and writing |
| **D** | Timing bugs: reproduce in the deterministic simulator first |
| **T** | The specification, design doc, report, demo |

## Stretch goals

- **Connection migration:** the client's address changes mid-transfer (move it to a new namespace address); the connection continues by connection ID.
- **Priority lanes:** two message classes per connection (e.g. control vs bulk) with separate in-order streams, so a lost bulk message doesn't delay control messages (QUIC's "head-of-line blocking" fix).
- **Authenticated encryption** using a real library (e.g. libsodium or Python `cryptography`): encrypt payloads and replace the CRC with a MAC. Read about why "encrypt-then-MAC" matters.
- **Interoperability:** if you have a study partner, implement each other's specs from the documents alone, and connect your implementations.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Specification | RFC-quality, precise keywords, full state machine, 8+ rationales | Mostly complete | Vague |
| Gremlin 2 | All impairments incl. burst loss and token bucket, verified | Most | Basic |
| Reliability | Sliding window, SACK, fast retransmit, adaptive RTO; correctness matrix all green | Window without SACK | Stop-and-wait only |
| Flow and congestion | Window probes; AIMD sawtooth; fairness ≥ 0.9 | One of the two | Neither |
| Robustness | Fuzzed parser; kill tests; cookie handshake | Some | None |
| Evaluation | Full campaign with TCP and model comparisons; targets met or explained | Partial | Missing |
| Communication | Spec, doc, report, demo | Most | Few |

**Done when:** every area at least 2; Specification and Reliability at 3.

## Connections

- **Back:** Relay (everything started there), Crate (CRCs and fuzzing), Module 05 (ring buffers, heaps), Scheduler Arena (fairness), Lab 03 (bench and Mathis), Module 03 (probability of loss), Crosswalk (state machines).
- **Forward:** [Lantern](../lantern/spec.md) can run over Courier; [13 Capstone](../../../13-capstone/overview.md) — your browser fetching pages over your own transport.
