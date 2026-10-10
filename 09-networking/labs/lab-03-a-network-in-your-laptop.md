---
title: "Lab 03 — A Network in Your Laptop"
module: "09-networking"
hours: 10
---

# Lab 03 — A Network in Your Laptop

**Goal:** build a two-host (then three-host) network inside your Linux machine with **network namespaces**, impose real delay, loss, and bandwidth limits with **netem** and **tbf**, measure TCP with `iperf3`, and test a simple model of TCP throughput. This becomes Courier's test bench.

**Time:** about 10 hours, in three sessions.

**Needs:** Linux, `sudo` (on your own machine), `iproute2`, `iperf3`. Everything here is undone by deleting the namespaces (Session 1 shows how) or by rebooting.

---

## Session 1 — Two hosts and a cable (3 hours)

A **network namespace** is a separate copy of the network stack: its own interfaces, addresses, and routing table. A **veth pair** is a virtual cable: two interfaces connected end to end.

```bash
sudo ip netns add alice
sudo ip netns add bob
sudo ip link add veth-a type veth peer name veth-b
sudo ip link set veth-a netns alice
sudo ip link set veth-b netns bob
sudo ip netns exec alice ip addr add 10.0.0.1/24 dev veth-a
sudo ip netns exec bob   ip addr add 10.0.0.2/24 dev veth-b
sudo ip netns exec alice ip link set veth-a up
sudo ip netns exec bob   ip link set veth-b up
sudo ip netns exec alice ip link set lo up
sudo ip netns exec bob   ip link set lo up
sudo ip netns exec alice ping -c 3 10.0.0.2
```

Put this in a script `netlab-up.sh`, and the teardown in `netlab-down.sh` (`sudo ip netns del alice; sudo ip netns del bob` — deleting a namespace removes its interfaces too).

Run programs "on" each host with `sudo ip netns exec alice <command>`. (To avoid running your own code as root, use `sudo ip netns exec alice sudo -u $USER <command>`.) Run your Relay chat between alice and bob.

**[W]:** why is this better for testing protocols than using `127.0.0.1` on one machine? (Hint: with netem on loopback, *all* local traffic suffers; here only the test link does.)

---

## Session 2 — Delay, loss, bandwidth (4 hours)

**netem** adds impairments to an interface's outgoing traffic; **tbf** limits rate.

```bash
# 50 ms delay each way (so ~100 ms round trip), 1% loss, on alice's side
sudo ip netns exec alice tc qdisc add dev veth-a root netem delay 50ms loss 1%
# same on bob's side for a symmetric path
sudo ip netns exec bob tc qdisc add dev veth-b root netem delay 50ms loss 1%
# change or remove:
sudo ip netns exec alice tc qdisc change dev veth-a root netem delay 50ms 10ms loss 2%
sudo ip netns exec alice tc qdisc del dev veth-a root
```

netem can also **duplicate**, **reorder**, and **corrupt** packets, and add **jitter** (the `10ms` above). To limit bandwidth as well, chain netem with a token-bucket filter (look up "netem rate" or "tbf under netem" in the `tc-netem` man page — the man page has examples; reading it is part of the lab).

**Measure with ping and iperf3:**
1. `ping` under each setting: check the RTT and loss match what you configured.
2. `iperf3 -s` on bob; `iperf3 -c 10.0.0.2 -t 15` on alice. Record TCP throughput.

---

## Session 3 — Test a model (3 hours)

A well-known approximation for steady-state TCP throughput with random loss (Mathis et al., 1997):

$$\text{throughput} \approx \frac{MSS}{RTT} \cdot \frac{C}{\sqrt{p}}$$

where MSS is the segment size (about 1,448 bytes), RTT the round-trip time, p the loss probability, and C a constant near 1.22.

1. Fix RTT at 100 ms. Measure iperf3 throughput for p = 0.1%, 0.5%, 1%, 2%, 5% (3 runs each, median).
2. Fix p at 1%. Measure for RTT = 20, 50, 100, 200 ms.
3. Plot measured vs predicted (log-log plots, Module 05 Lab 01: the slope against p should be about −½; against RTT about −1).
4. Where does the model fit, and where not? (Modern Linux uses newer congestion control — CUBIC or BBR, check `sysctl net.ipv4.tcp_congestion_control` — so expect differences. Explain them as hypotheses.)

**Lab report:** *"How do delay and loss limit TCP throughput — and does the Mathis model predict it?"*

---

## Done when

- [ ] `netlab-up.sh` / `netlab-down.sh` work; Relay runs between namespaces.
- [ ] Impairments verified with ping; iperf3 measurements for both sweeps.
- [ ] Lab report with plots.

## Retrieval and reflection

1. **[R]:** namespaces and veth; the netem options; the Mathis formula and what each factor means.
2. **[W]:** why does throughput fall with the *square root* of loss, and *linearly* with RTT? (A sliding window needs about one RTT per window's worth of data, and loss shrinks the window.)
