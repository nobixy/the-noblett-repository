---
block_id: "Block 21a"
title: "Maker Lab 5: PCB Design with KiCad"
category: "core"
subject: "Electrical Engineering"
term: "Year 3 Spring"
status: not-started
prerequisites:
  - "B08a - Circuits and Electronics Bridge"
  - "B09a - Maker Lab 2 - Embedded C"
  - "B15b - Maker Lab 3 - CAD and 3D Printing"
hours_estimate: 40
hours_actual: 0
primary_resource: "KiCad docs + Phil's Lab videos (free); cheap 2-layer fab only after review"
milestone: "Your own 2-layer board (MCU + IMU + ToF + power) passes ERC/DRC, is assembled by hand, and every peripheral responds"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 21a — Maker Lab 5: PCB Design with KiCad

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Hardware Index|Hardware Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Spring
> - **Estimated Hours:** ~40 hrs
> - **Status:** `not-started`
> - **Primary Resource:** KiCad docs + Phil's Lab videos (free); cheap 2-layer fab only after review
> - **Key Milestone:** Your own 2-layer board (MCU + IMU + ToF + power) passes ERC/DRC, is assembled by hand, and every peripheral responds
> - **Added by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
Breadboards and dev boards stop scaling the moment something has to fly. Designing your own board, or a Crazyflie expansion deck, is the step from hobbyist to hardware engineer, and KiCad is free and professional-grade.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B08a - Circuits and Electronics Bridge|Circuits and Electronics Bridge]]
- [[B09a - Maker Lab 2 - Embedded C|Maker Lab 2]]
- [[B15b - Maker Lab 3 - CAD and 3D Printing|Maker Lab 3]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Schematic capture: symbols, footprints, nets, ERC; reading reference designs from datasheets.
- [ ] Layout: 2-layer stack-up, ground pour, decoupling placement, trace width for current, keeping I2C/SPI clean, mounting holes that match your CAD.
- [ ] Power: LDO vs buck converter, reverse-polarity protection, LiPo charging and protection awareness.
- [ ] Design for manufacture and hand assembly: 0805 parts, DRC rules from the fab, Gerbers, BOM, pick-and-place files.
- [ ] Bring-up: smoke test with a current-limited supply, then each peripheral in turn; keep an errata list.
- [ ] Crazyflie expansion decks: Bitcraze publishes a KiCad template for custom decks.

---

## 🛠️ Build Requirement
Design is free; ordering is the only cost.
1. **Board:** RP2350 or ESP32-S3 module + IMU + ToF + regulator + connectors (or a Crazyflie deck from the Bitcraze KiCad template).
2. **Review before ordering:** ERC/DRC clean, a self-review checklist, and one outside review (forum or makerspace).
3. **Order, assemble, bring up:** 5 boards from a low-cost fab; hand-solder; bring up every peripheral with your Block 9a drivers.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Board passes ERC/DRC; spin 1 or 2 works with documented errata; your drivers run on it; the board fits the enclosure from Maker Lab 3.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- KiCad (free, open source): kicad.org; docs: docs.kicad.org.
- Phil's Lab (free videos on KiCad and PCB design): youtube.com/@PhilsLab.
- Bitcraze Crazyflie 2.1+ page (deck expansion connector and KiCad deck template): bitcraze.io/products/crazyflie-2-1-plus/.
- **Kit (💲, approx.):** 5 bare 2-layer boards from a low-cost fab such as jlcpcb.com ≈$2–10 + shipping; parts ≈$15–30; fine-tip iron tip, flux, tweezers ≈$15. Free alternative: finish the full design and review without ordering.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The bring-up log is the check; compare your layout to the reference design in the IMU datasheet.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Contextual Electronics / other free KiCad courses if Phil's Lab doesn't click.

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B21 - Databases|← Databases]] | [[00 - Start Here|Start Here]] | [[B22 - Statistics|Statistics →]]
