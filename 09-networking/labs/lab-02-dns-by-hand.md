---
title: "Lab 02 — DNS by Hand"
id: "MOD09-LAB02"
type: "lab"
module: "09-networking"
phase: "D"
order: 1180
prerequisites: [MOD09-LAB01]
---

# Lab 02 — DNS by Hand

**Goal:** build DNS query packets byte by byte, send them over UDP, decode the replies (including name compression), and resolve a name **iteratively** starting from a root server — doing by hand what your computer's resolver does thousands of times a day.

**Sessions:** three. Python with `socket` and `struct`; no DNS libraries.

**Etiquette:** a few dozen queries while learning are fine; don't loop queries against public servers.

---

## Session 1 — Build a query

A DNS message has a 12-byte **header**, then sections. All numbers are **big-endian** ("network byte order") — the opposite of Tone Loom's WAV files. In `struct`, use `!` (network order): `struct.pack("!HHHHHH", …)`.

**Header (12 bytes):** ID (16 bits, random — matches replies to queries), flags (16 bits: QR, opcode, AA, TC, RD, RA, rcode), QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT (16 bits each).

**Question:** the name as **labels** — each part preceded by its length, ending with a zero byte: `example.com` → `07 65 78 61 6d 70 6c 65 03 63 6f 6d 00` — then QTYPE (A = 1, NS = 2, CNAME = 5, AAAA = 28) and QCLASS (IN = 1).

1. Write `build_query(name, qtype, recursion_desired)` returning bytes.
2. Print it with your `minihex.py`; check it against a query captured in Wireshark (Lab 01).
3. Send it over UDP to your router's resolver or a public resolver (port 53) with recursion desired, and print the raw reply in hex.

---

## Session 2 — Parse the reply

Parse: the header; the question; and each **resource record** in the answer, authority, and additional sections: name, type, class, TTL (32 bits), RDLENGTH, RDATA (for A: 4 bytes of IPv4; for AAAA: 16 bytes; for NS and CNAME: a name).

**Name compression:** to save space, a name may end with (or be entirely) a **pointer** to an earlier name in the message: two bytes whose top two bits are `11`, and whose other 14 bits are an offset from the start of the message. So `c0 0c` means "the rest of this name is at offset 12" (often the question's name).

**Subgoal labels [S]** for `read_name(msg, offset)`:
```
# 1. Read a length byte
# 2. If it's 0: end of name
# 3. If its top two bits are 11: it's a pointer — read the 14-bit offset, read the name from there (recursively),
#    and the name ends here (remember: the caller continues after these 2 bytes, not after the target)
# 4. Otherwise: read that many bytes as a label; repeat
# 5. Guard against pointer loops (a hostile packet could point to itself): limit the number of jumps
```

Print replies in a `dig`-like format. Compare with `dig example.com` for three names.

**[W]:** step 5 — why must a parser defend itself against a pointer to itself? (Crate's lesson: never trust input.)

---

## Session 3 — Iterative resolution from the root

Your resolver normally does this for you. Now do it yourself, with **recursion desired = 0**:

1. Ask a **root server** (e.g. `a.root-servers.net`, 198.41.0.4) for `www.example.com` type A. It doesn't know the answer, but its **authority section** lists the name servers for `.com`, and its **additional section** usually gives their addresses ("glue").
2. Ask one of those `.com` servers. It refers you to `example.com`'s name servers.
3. Ask one of those. It answers (maybe with a CNAME to follow).

Write `resolve(name)` that follows these **referrals** automatically, printing each step:

```
asking 198.41.0.4 (a.root-servers.net) about www.example.com
  referral to com. servers: a.gtld-servers.net (192.5.6.30), …
asking 192.5.6.30 about www.example.com
  referral to example.com. servers: …
asking … about www.example.com
  ANSWER: www.example.com A 93.184.215.14 (TTL 3600)
```

(When a referral has no glue addresses, you must first resolve the name server's own name — recursion!)

Add a **cache** keyed by (name, type) that respects TTLs. Resolve 10 names in the same domain and count how many queries the cache saves.

---

## Done when

- [ ] Queries built and matching Wireshark captures; replies parsed with compression (and loop protection).
- [ ] `resolve()` follows referrals from the root for 5 names, including one with a CNAME and one needing glue-less recursion.
- [ ] Cache with TTLs; savings measured.

## Retrieval and reflection

1. **[R]:** the DNS header fields; label encoding; compression pointers; the root → TLD → authoritative chain.
2. **[F] (spoken):** "How does my computer find the address for a name it's never seen?"
3. **[W]:** why is DNS mostly over UDP rather than TCP? What happens when a reply is too big (look up the TC flag)?
