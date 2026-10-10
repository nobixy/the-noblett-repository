---
title: "Project 2: Relay, Talking Programs"
module: "01-intro-cs-taste"
hours: 16
artifact: "relay_server.py, relay_client.py (TCP chat); gremlin.py (lossy link); a reliable UDP messenger"
deliverable: "One-page protocol spec + 4-minute demo + small results table"
---

# Project 2: Relay, Talking Programs

| | |
| :-- | :-- |
| **Module** | 01 Intro CS Taste |
| **Time** | About 16 hours |
| **Prerequisites** | Labs 00–02; Math M01–M03 (you'll use `%` and timing); English E03+ |
| **You build** | A chat system: a server and clients that talk over TCP using a protocol **you** define. Then you break the network on purpose with a "gremlin" that drops, duplicates, and delays messages — and make your messages arrive anyway, using sequence numbers, acknowledgments, and timeouts |
| **Deliverable** | A one-page protocol specification, a recorded demo, and a small table of measurements |

---

## Why this matters

Every networked program — chat, email, games, the web — is two or more programs exchanging messages according to an agreement called a **protocol**. And every one of them must deal with an uncomfortable fact: **networks lose things.** Packets get dropped, duplicated, delayed, and arrive out of order.

In this project you feel both truths directly. First, you'll design a tiny protocol and build a working chat. Then you'll build a tool that sabotages your messages, watch your chat fall apart, and fix it with the three ideas that make the internet reliable: **number every message, confirm what arrived, and resend what wasn't confirmed.**

In [Module 09](../../../09-networking/overview.md), you'll build **Courier**, a full reliable transport protocol with sliding windows, connection setup, and adaptive timeouts. Relay is the small, real version.

**Real-world analogs:** IRC and chat servers, TCP's acknowledgments and retransmissions, network testing tools that inject faults.

---

## Background (read before Milestone 1)

- An **IP address** names a computer on a network. `127.0.0.1` (also called `localhost`) always means *this* computer. All of this project runs on one machine, in several terminals.
- A **port** is a number (0–65,535) that names one program on a computer. Your server will listen on a port like 5555.
- A **socket** is the program's end of a network conversation. Python's `socket` module gives you sockets.
- **TCP** gives you a reliable **stream of bytes** between two programs: everything you send arrives, in order, or the connection breaks. But it's a *stream*, not a sequence of messages: two `send`s can arrive as one chunk, and one `send` can arrive as two. (You'll see this in Milestone 1.)
- **UDP** sends separate **datagrams** (packets). Each one arrives whole — or not at all. No ordering, no retries. You'll use it in Milestones 3–5, where you build reliability yourself.

---

## Milestones

### Milestone 1 — Echo, and the stream surprise (TCP)

**Build** `echo_server.py`: listen on port 5555; accept one client; read data; send it straight back; repeat until the client disconnects.

**Build** `echo_client.py`: connect to localhost:5555; read lines you type; send each; print what comes back.

**Experiment 1:** in a third terminal, run `ss -tlnp | grep 5555` (shows listening TCP sockets) while the server runs. Connect with `nc localhost 5555` instead of your client (netcat: a general-purpose network tool). It works — because your server only speaks bytes.

**Experiment 2 — the stream surprise:** change the client to send `"one\n"` and `"two\n"` in two separate `sendall` calls, immediately one after the other. Change the server to print `repr()` of every chunk it receives *before* echoing. Run it 10 times. Sometimes you'll see `b'one\ntwo\n'` arrive as **one chunk**. (If it never happens on your machine, add `time.sleep(0.05)` in the server before each `recv`.)

**Done when:** echo works with your client and with `nc`, and you've seen two messages arrive as one chunk.

**[W]:** If TCP can merge or split your messages, how can the receiver know where one message ends and the next begins? Write two possible answers before reading Milestone 2.

### Milestone 2 — The Relay chat protocol (TCP)

First **write the spec**, then build it. Writing first is the habit you'll use for every protocol in this curriculum.

**Relay v1 (starting point — you may change it, but document every change and why):**

- Messages are lines of UTF-8 text ending in `\n`. **The receiver keeps a buffer** and only processes a message when it has a complete line. (That's the answer to Milestone 1's question: a **delimiter**. The other common answer is a **length prefix**.)
- Client → server:
  - `HELLO <nick>` — must be the first message. Nick: 1–16 letters, digits, or `_`.
  - `SAY <text>` — send a message to everyone.
  - `WHO` — ask who's online.
  - `BYE` — leave.
- Server → client:
  - `WELCOME <nick>` — reply to a good HELLO.
  - `ERR <code> <reason>` — e.g. `ERR 409 nick-taken`, `ERR 400 unknown-command`, `ERR 401 say-hello-first`.
  - `FROM <nick> <text>` — someone said something.
  - `JOINED <nick>` / `LEFT <nick>`
  - `USERS <nick> <nick> ...`

**Write `PROTOCOL.md`** (one page, E05–E07 level): purpose; message format; every command with an example; what the server does with errors; one example conversation between two clients.

**Build:**
- `relay_server.py`: handles **many clients at once**. Use the `selectors` module (one loop that waits for whichever socket has data) or one thread per client. Each client has its own receive buffer and its own state (has it said HELLO yet? what's its nick?).
- `relay_client.py`: shows incoming messages while you type. (Simplest on Linux: use `selectors` to watch both the socket and standard input; or use one thread for receiving.)

**Tests:** a script that starts the server, connects three test clients with raw sockets, and checks: a nick collision gets `ERR 409`; SAY before HELLO gets `ERR 401`; every client receives every `FROM`; `BYE` makes the others see `LEFT`. Also test a **split message**: send `SA` then, 100 ms later, `Y hi\n` — the server must treat it as one `SAY hi`.

**Done when:** three clients chat in three terminals; tests pass; `PROTOCOL.md` matches what the code does.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *what a protocol is*, using Relay as the example. Why-ladder target: *why must every client have its own buffer?*

### Milestone 3 — The gremlin (UDP)

Now switch to **UDP** and meet an unreliable network. Real networks only misbehave occasionally and unpredictably, so you'll build a tool that misbehaves on purpose and **repeatably**.

**Build `gremlin.py`:** a UDP relay that sits between a sender and a receiver.

```
sender ──UDP──▶ gremlin (port 6000) ──UDP──▶ receiver (port 6001)
sender ◀──UDP── gremlin             ◀──UDP── receiver
```

- Every datagram that arrives is forwarded to the other side — unless the gremlin decides otherwise.
- Options: `--drop 0.2` (drop 20%), `--dup 0.1` (send 10% twice), `--delay 0-200` (hold each datagram a random 0–200 ms before forwarding, which causes **reordering**), and `--seed 42` (use `random.Random(42)` so a test run can be repeated exactly).
- It logs each decision: `#17 a→b DROP`, `#18 a→b DELAY 143ms`, `#19 b→a DUP`.

**Build** a naive `udp_send.py` that sends 100 datagrams `msg 0` … `msg 99`, and `udp_recv.py` that prints what arrives.

**Experiment:** run through the gremlin with `--drop 0.3 --dup 0.1 --delay 0-200 --seed 1`. Count: how many arrived? How many twice? How many out of order? Run with the same seed again: identical? (It should be — why does that matter for debugging? [W])

**Done when:** the gremlin works with all options, and you have a table of what went wrong in the naive run.

### Milestone 4 — Make it reliable (stop-and-wait)

Design and build **Relay-R**, a reliable message protocol over UDP. Write the design first, in `RELIABLE.md` (half a page).

**Datagram format (text, for readability):**
- `DATA <seq> <text>` — a message, numbered.
- `ACK <seq>` — "I received message `seq`."

**Sender (subgoal labels [S]):**
```python
# 1. Number each message: seq = 0, 1, 2, ...
# 2. Send DATA seq text
# 3. Wait for ACK seq, with a timeout (start with 300 ms)
# 4. If the timeout fires: resend the same DATA (count the retry)
# 5. If the right ACK arrives: move on to the next message
# 6. Ignore ACKs for old seq numbers (they're duplicates or late)
# 7. Give up after 20 retries of one message and report failure
```

**Receiver:**
```python
# 1. Keep `expected` = the next seq we want (starts at 0)
# 2. On DATA seq:
#    a. Always send ACK seq back (even for duplicates! Why? — see the why-ladder)
#    b. If seq == expected: deliver (print) the text, expected += 1
#    c. If seq < expected: it's a duplicate; don't deliver again
```

(With stop-and-wait, the sender never sends message n + 1 before n is acknowledged, so the receiver never sees seq > expected. Think about why.)

**Experiment:** send 100 messages through the gremlin with `--drop 0.3 --dup 0.1 --delay 0-200`. Requirements:
- all 100 delivered **exactly once**, **in order** (the receiver checks and reports);
- record the total time and the number of retransmissions.

**Done when:** three different seeds all deliver 100/100 correctly.

**Checkpoint:** Milestone Checkpoint. Why-ladder targets (answer all three in `RELIABLE.md`):
1. *Why must the receiver ACK a duplicate DATA?* (What if the first ACK was the one that got lost?)
2. *Why does the sender need a timer at all?*
3. *Why do messages need sequence numbers? What breaks without them?*

### Milestone 5 — Measure the cost

Stop-and-wait is reliable but slow: only **one** message is "in flight" at a time.

**Experiment:** with `--delay 50-50` (a fixed 50 ms each way, so the round trip is about 100 ms) and drop rates 0%, 10%, 20%, 30%, 40%, measure messages per second for 100 messages. Also try timeouts of 150 ms, 300 ms, and 1,000 ms at 20% drop.

Fill a table. Then answer:
- With 0% loss and a 100 ms round trip, what's the best possible messages-per-second for stop-and-wait? (Hint: M06 rates.) How close did you get?
- Why does a too-short timeout hurt? Why does a too-long one hurt?
- **The big question:** how could the sender go faster without losing reliability? (Write your idea. In Module 09 you'll build the standard answer: a **sliding window**, with many messages in flight at once.)

**Done when:** the table is filled and the three questions are answered.

---

## Testing guidance

- **Fixed seeds** make gremlin runs repeatable. A failing seed is a perfect bug report.
- **Check, don't eyeball:** the receiver should verify `msg 0` … `msg 99` arrived exactly once, in order, and print PASS/FAIL.
- **Test the parts alone:** the receiver's duplicate logic can be tested with no network at all — call its handler function with a list of fake datagrams.
- **Run long:** 1,000 messages at 40% drop. Rare bugs show up in long runs.

## Common pitfalls

- **Assuming one `recv` = one message** (TCP). Always buffer until the delimiter.
- **Forgetting to handle disconnects:** `recv` returning `b""` means the other side closed. Remove that client cleanly.
- **Blocking forever:** a `recv` without a timeout waits forever if the packet was lost. Use `sock.settimeout(...)` and catch `socket.timeout`.
- **Address already in use:** after a crash, the port can stay busy for a while. Set `sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)` before `bind`.
- **Text vs bytes:** sockets send bytes. `.encode("utf-8")` before sending, `.decode("utf-8")` after receiving.

## Communication deliverable

Sized for E03–E07:
1. **`PROTOCOL.md`** (Relay v1) and **`RELIABLE.md`** (Relay-R) — the protocol specs, including the three why-ladder answers.
2. **Demo (4 minutes, recorded):** three-client chat; the gremlin wrecking the naive UDP sender; Relay-R delivering 100/100 through the same gremlin. Explain the ACK-for-duplicates idea in one sentence.
3. **Results table** from Milestone 5, with two or three sentences on what it shows.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 4, write the sender and receiver rules from memory |
| **F** | What a protocol is; why acknowledgments work |
| **W** | Framing; per-client buffers; repeatable seeds; ACKing duplicates; timers; sequence numbers; timeout length |
| **S** | Sender and receiver subgoal comments |
| **I** | TCP stream ideas and UDP datagram ideas side by side |
| **D** | Network bugs are timing bugs: write stuck notes, sleep on them |
| **T** | Specs, demo, results |

## Stretch goals

- **Two machines:** run the server on one computer and clients on another on your home network. What changes? (Firewall? `0.0.0.0` vs `127.0.0.1`?)
- **Relay-R for chat:** carry the Relay v1 chat protocol over your reliable UDP layer instead of TCP. You've just built a protocol stack: an application protocol on top of a transport you wrote.
- **Go-back-N:** let the sender have up to 4 messages in flight. (This is a big step toward Module 09; it's fine to leave it for later.)
- **Wireshark:** capture your chat on the loopback interface (`lo`) and find your own messages in the packets.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| TCP chat | Many clients, buffering correct, all tests including split messages | Works, few tests | Breaks on split messages |
| Protocol spec | Matches the code; examples; errors documented | Mostly | Missing |
| Gremlin | Drop, dup, delay, seed, logging | Some options | Missing |
| Reliability | 100/100 exactly once in order, 3 seeds, 1,000-message run | 100/100 once | Fails |
| Measurements | Table + three answers | Table only | Missing |
| Communication | Specs, demo, results all clear | Two of three | One or none |

**Done when:** every area at least 2; Reliability at 3.

## Connections

- **Back:** [Lab 01](../../labs/lab-01-python-first-steps.md) (strings, dicts, loops), M06 (rates for Milestone 5).
- **Forward:** [09 Networking](../../../09-networking/overview.md) — Packet Telescope (see the real headers), **Courier** (a full reliable transport over UDP with connection setup, sliding windows, and adaptive timeouts, tested with an upgraded gremlin), and Lantern (an HTTP server). [08](../../../08-operating-systems/overview.md) — `selectors` and threads are your first taste of concurrency.

> **Originality note:** the Relay protocol, the gremlin tool, and these milestones were written for this curriculum. They are not based on any course's lab framework.
