---
title: "Project: Lantern"
module: "09-networking"
hours: 55
artifact: "lantern: an HTTP/1.1 server written from sockets up — request parsing with strict limits, static files with MIME types and directory listings, keep-alive, conditional and range requests, chunked responses, three concurrency models compared, logging, slow-client defences, a fuzzed parser, and a small dynamic endpoint"
deliverable: "Design doc + conformance and robustness report + benchmark report (concurrency models) + 5-minute demo"
---

# Project: Lantern

| | |
| :-- | :-- |
| **Module** | 09 Networking |
| **Time** | About 55 hours |
| **Prerequisites** | Pagelet (the client side of HTTP/1.0); Module 08 Lab 01 (threads); Lab 03 of this module (bench); Crate (fuzzing) |
| **Language** | C (recommended — real systems practice) or Python. Targets below are for C; halve throughput targets for Python. |
| **You build** | **Lantern**, a web server. It accepts connections, parses HTTP/1.1 requests defensively, serves files with the right headers, keeps connections open for many requests, answers "not modified" and "here's just the part you asked for," streams generated content, logs every request, survives slow or malicious clients — and you build it three different ways for concurrency and measure which is best |
| **Deliverable** | Design doc, conformance and robustness report, benchmark report, and demo |

---

## Why this matters

HTTP carries most of the world's traffic, and the web server is the classic network service. Writing one teaches **protocol framing** (where does one request end?), **defensive parsing** (servers face the whole internet), **resource limits** (a slow client mustn't tie up your server), and **concurrency models** (threads vs event loops — a debate that has shaped real servers like Apache and nginx). Your browser engine in Module 10 will fetch its pages from Lantern.

**Real-world analogs:** nginx, Apache httpd, lighttpd, Python's `http.server` (now you'll know what it does inside).

---

## Requirements

**HTTP/1.1 subset** (read RFC 9112 "HTTP/1.1" message syntax and the relevant parts of RFC 9110 "HTTP Semantics" — skim, then look things up as needed):
- Methods: **GET** and **HEAD** (others → **405** with an `Allow` header).
- **Request parsing:** request line, headers (case-insensitive names), `Host` required for HTTP/1.1 (missing → 400), a body only if `Content-Length` (accepted and ignored for GET, or rejected — decide).
- **Limits:** request line ≤ 8 KiB (else **414**); total headers ≤ 16 KiB and ≤ 100 lines (else **431**); a header read timeout (slow clients → close).
- **Static files** from a document root: correct `Content-Type` by extension (a table: html, css, js, png, jpg, svg, txt, pml for your Pagelet pages, …), `Content-Length`, `Last-Modified`; **directory listings** as HTML when there's no `index.html`.
- **Path safety:** decode `%xx` escapes, normalise the path, and **never serve anything outside the document root** (`/../../etc/passwd`, encoded variants like `%2e%2e/`) — Crate's path-traversal lesson, on the network.
- **Keep-alive:** HTTP/1.1 connections stay open for more requests until `Connection: close`, an idle timeout, or a per-connection request limit.
- **Conditional requests:** `If-Modified-Since` → **304 Not Modified** when appropriate.
- **Range requests:** `Range: bytes=start-end` → **206 Partial Content** with `Content-Range`; invalid ranges → **416**.
- **Chunked transfer encoding** for a dynamic endpoint whose length isn't known in advance.
- **Errors** with small HTML bodies: 400, 403, 404, 405, 414, 416, 431, 500, 503.
- **Access log** in the Common Log Format.

---

## Milestones

### Milestone 1 — Design doc and a one-request server

1. **Design doc v1** (4 pages): the request parser as a state machine (request line → headers → done; FSM again), the response builder, resource limits, the three concurrency models you'll compare, and the test plan.
2. **One connection at a time:** accept, read until the end of the headers (`\r\n\r\n` — buffer across `recv` calls: Relay's framing lesson), parse, serve a file, close.

**Done when:** `curl -v http://localhost:8080/README.md` works, and your Pagelet (from Module 01) browses a folder of PML pages served by Lantern (Pagelet speaks HTTP/1.0; Lantern must answer 1.0 requests too — and close after each).

### Milestone 2 — Correct HTTP/1.1

All requirements above: methods, Host, limits, MIME types, directory listings, path safety, keep-alive (with pipelined requests: several requests sent in one packet must each get a response, in order), conditional, range, chunked, errors, logging.

**Conformance tests** (a Python test suite using raw sockets — not just `curl`, because you need to send broken and tricky requests):
- every status code above triggered on purpose;
- two pipelined requests in one `send`;
- a request split into 1-byte sends with delays (framing!);
- header names in mixed case; repeated headers;
- traversal attempts (at least 10 encodings);
- ranges: first 100 bytes, last 100 (`bytes=-100`), past the end, malformed;
- HEAD returns headers identical to GET's, without a body.

**Done when:** all conformance tests pass.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: request and response framing rules from memory. Why-ladder target: *why does keep-alive require `Content-Length` or chunked encoding?*

### Milestone 3 — Three concurrency models

Implement the same server three ways (sharing the parser and response code):
1. **Thread per connection** (with a cap on threads).
2. **Thread pool** with a bounded queue of accepted connections (Module 08 Lab 01's bounded buffer!).
3. **Event loop** with `epoll` (C) or `selectors` (Python): non-blocking sockets, each connection a small state machine (reading headers → sending response → keep-alive wait), timers for idle connections.

[W] Predict which wins for (a) many small files and few clients, (b) thousands of idle keep-alive connections, (c) a few clients downloading huge files.

### Milestone 4 — Robustness

1. **Slow clients:** a "slowloris" test client that opens 500 connections and sends one header byte every 10 seconds. Your server must keep serving normal clients (per-connection timeouts; connection limits; the event loop handles this best — does your measurement agree?).
2. **Fuzzing the parser:** feed the request parser millions of mutated requests (in-process, under ASan if in C) — no crashes, no hangs, no reads past buffers.
3. **Resource exhaustion:** open connections until the server's limit; it must answer **503** (or refuse cleanly), not crash.

### Milestone 5 — Benchmarks

Use `wrk` (or `ab`, or your own load generator) in the namespace bench:
- requests per second and latency percentiles (p50, p99) for a 1 KiB file with 1, 10, 100, 1,000 concurrent connections, for each concurrency model;
- throughput for a 100 MiB file;
- the effect of keep-alive on vs off;
- compare with `python3 -m http.server` and (if installed) nginx serving the same folder — not to win, but to understand the gap.

**Targets (C):** ≥ 10,000 requests/s for a small file with keep-alive on your machine (one core is fine); no failed requests under the slowloris test. If you miss a target, explain with evidence.

### Milestone 6 — A little dynamic content

Add one dynamic endpoint, e.g. `/search?q=…` that calls your **Vault Search** index (as a library in Python, or by running the `vs` command and capturing its output in C) and returns an HTML or PML results page using **chunked** encoding. Decode query strings properly (`%20`, `+`).

---

## Common pitfalls

- **Assuming one `recv` = one request** (or one request = one `recv`).
- **Blocking `sendfile`/`write` on a slow client** in the event loop — use non-blocking writes and track progress.
- **Off-by-one in ranges** (`bytes=0-99` is 100 bytes, inclusive).
- **Path checks before decoding** (attackers encode `..`).
- **Forgetting HEAD** must not send a body but must send the same `Content-Length`.
- **SIGPIPE** killing the server when a client disconnects mid-response (Burrow Jr.'s signal again): ignore it and handle `EPIPE`.

## Communication deliverable

1. **Design doc** v1 → v2.
2. **Conformance and robustness report** (2 pages): the test suite, traversal tests, slowloris and fuzzing results.
3. **Benchmark report** (2 pages): the three models across scenarios, keep-alive effect, comparison with other servers, and a recommendation.
4. **Demo (5 minutes):** Pagelet browsing your site from Lantern, `curl -v` showing 304 and 206, a traversal attempt refused, and the benchmark plots.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | HTTP framing and status codes from memory |
| **F** | Threads vs event loops in plain words |
| **W** | Keep-alive framing; predictions for the three models; decode-then-check |
| **S** | Parser FSM states; the event loop's per-connection states |
| **I** | Protocol, concurrency, security, and performance together |
| **T** | Design doc, two reports, demo |

## Stretch goals

- **Lantern over Courier:** serve HTTP over your own transport (a capstone building block).
- **TLS** with OpenSSL or a small TLS library — carefully, using the library's recommended settings.
- **Compression:** `Content-Encoding: gzip` (zlib) for text files, negotiated via `Accept-Encoding`.
- **HTTP/1.1 client** in C to replace `curl` in your tests.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| HTTP correctness | All requirements; raw-socket conformance suite passes | Most | Basics only |
| Security | Traversal blocked (10+ encodings); limits enforced; fuzzed | Some | Vulnerable |
| Concurrency | Three models, shared core | Two | One |
| Robustness | Slowloris survived; 503 under exhaustion | Partial | Falls over |
| Benchmarks | Full matrix with percentiles; comparisons | Partial | Missing |
| Communication | Doc, reports, demo | Most | Few |

**Done when:** every area at least 2; HTTP correctness and Security at 3.

## Connections

- **Back:** Pagelet (client), Relay (framing), Module 08 (threads, bounded buffers), Crate (fuzzing, traversal), Vault Search (dynamic content).
- **Forward:** [10 Browser Engine](../../../10-browser-engine/overview.md) (Glimpse fetches from Lantern), Module 11 (a database-backed endpoint), Module 13 (the integrated stack).

> **Originality note:** Lantern's requirement set, three-model comparison, and test plan were designed for this curriculum.
