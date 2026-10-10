---
block_id: "Block 16a"
title: "Maker Lab 4: Raspberry Pi and Embedded Linux"
category: "core"
subject: "Computer Engineering"
term: "Year 3 Fall (after Operating Systems)"
status: not-started
prerequisites:
  - "B16 - Operating Systems"
  - "B09a - Maker Lab 2 - Embedded C"
hours_estimate: 50
hours_actual: 0
primary_resource: "Bootlin Embedded Linux training materials + Raspberry Pi docs + libgpiod (free)"
milestone: "Pi companion computer survives 50 power cycles and an hour of fuzzed serial input while streaming camera and telemetry"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 16a — Maker Lab 4: Raspberry Pi and Embedded Linux

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Hardware Index|Hardware Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Fall (after Operating Systems)
> - **Estimated Hours:** ~50 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Bootlin Embedded Linux training materials + Raspberry Pi docs + libgpiod (free)
> - **Key Milestone:** Pi companion computer survives 50 power cycles and an hour of fuzzed serial input while streaming camera and telemetry
> - **Added by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
Real drones split work: a microcontroller flies, a Linux companion computer sees, plans and talks. You just learned how an OS works (Block 16); now run Linux on small hardware, talk to sensors and microcontrollers, and make it robust enough to fly. **Sim first, then buy:** every lab below starts in a free simulator; buy parts only once the simulated version works.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B16 - Operating Systems|Operating Systems]]
- [[B09a - Maker Lab 2 - Embedded C|Maker Lab 2]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Headless setup, SSH keys, cross-compiling for arm64, remote debugging with gdbserver.
- [ ] Device tree and overlays; GPIO through the character device with libgpiod (not the deprecated sysfs interface); I2C (i2c-dev) and SPI (spidev) from user space.
- [ ] UART link to a Pico/ESP32: design a framed protocol with length, sequence numbers and CRC; handle resync and corruption.
- [ ] Camera pipeline (libcamera / rpicam-apps); frame capture to your own program.
- [ ] systemd services, journald logging, watchdogs, read-only root filesystems for power-loss safety.
- [ ] Real-time limits of Linux; PREEMPT_RT awareness; why the flight loop stays on the microcontroller.
- [ ] Build your own image: Buildroot (Bootlin labs); boot time and image size.
- [ ] ROS 2 on small boards: Lyrical Luth (LTS, May 2026) is Tier 1 on Ubuntu 26.04 arm64; on Raspberry Pi OS use a container.

---

## 🛠️ Build Requirement
Start in QEMU (Bootlin's labs work there), then on hardware:
1. **Companion computer:** Pi reads an IMU over I2C, exchanges your CRC-framed protocol with the Block 9a board over UART, and streams camera frames + telemetry over Wi-Fi; runs as a systemd service.
2. **Robustness:** 50 hard power cycles without corruption (read-only root); a fuzzer throws random bytes at the UART for 1 hour without a crash.
3. **Buildroot image** with only what you need.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> All three pass; you can explain the device-tree overlay you wrote and why the control loop does not run on Linux.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- Bootlin Embedded Linux training (slides + labs, free): bootlin.com/training/embedded-linux/.
- Raspberry Pi computer docs (free): raspberrypi.com/documentation/computers/. Ubuntu for Raspberry Pi: ubuntu.com/download/raspberry-pi.
- libgpiod docs (free): libgpiod.readthedocs.io.
- ROS 2 docs (free): docs.ros.org (Lyrical Luth LTS, supported to May 2031; Jazzy LTS still supported).
- **Kit (💲, prices verified Oct 2026; Pi prices rose with memory costs):** Pi Zero 2 W $15 (cheapest); Pi 5 1GB $45 for headless work; Pi 5 4GB $110 only if you need a ROS 2 desktop on the board. Camera module ≈$25, microSD ≈$10, 5 V supply ≈$10. Cheapest path ≈$60.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Your fuzz and power-cycle logs are the check; Bootlin's lab instructions say what each lab's result should be.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Yocto Project instead of Buildroot (heavier, industry-standard).

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B16 - Operating Systems|← Operating Systems]] | [[00 - Start Here|Start Here]] | [[B17 - Software Construction|Software Construction →]]
