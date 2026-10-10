---
block_id: "Block 15b"
title: "Maker Lab 3: CAD and 3D Printing"
category: "core"
subject: "Mechanical Design"
term: "Year 2 Spring (after Signals)"
status: not-started
prerequisites:
  - "B08b - Maker Lab 1 - Electronics Bench"
  - "B09a - Maker Lab 2 - Embedded C"
hours_estimate: 40
hours_actual: 0
primary_resource: "Onshape Free or FreeCAD 1.0 + PrusaSlicer + Prusa Knowledge Base (free); library or makerspace printers"
milestone: "Board enclosure, vibration-isolated IMU mount and a prop guard designed, printed and fitted by revision 3"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 15b — Maker Lab 3: CAD and 3D Printing

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Hardware Index|Hardware Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 2 Spring (after Signals)
> - **Estimated Hours:** ~40 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Onshape Free or FreeCAD 1.0 + PrusaSlicer + Prusa Knowledge Base (free); library or makerspace printers
> - **Key Milestone:** Board enclosure, vibration-isolated IMU mount and a prop guard designed, printed and fitted by revision 3
> - **Added by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
Every drone, sensor pod and test rig you build needs a body. Parametric CAD and design for 3D printing let you go from idea to part in an evening. You do not need to own a printer: public libraries and makerspaces often have them. **Sim first, then buy:** every lab below starts in a free simulator; buy parts only once the simulated version works.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B08b - Maker Lab 1 - Electronics Bench|Maker Lab 1]]
- [[B09a - Maker Lab 2 - Embedded C|Maker Lab 2]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Parametric CAD: sketches, constraints, extrudes and revolves, part studios, assemblies, configurations, drawings with tolerances.
- [ ] Design for FDM printing: overhangs and supports, bridging, print orientation and layer-line strength, wall thickness, holes and fits (clearance vs press fit), heat-set threaded inserts.
- [ ] Materials: PLA, PETG, TPU (vibration dampers); when to use each.
- [ ] Slicing: layer height, infill, perimeters, supports; reading a slicer preview before printing.
- [ ] Measure and iterate: calipers, test coupons for fit, revision control of CAD files (FreeCAD files in git; Onshape versions).
- [ ] Drone-specific mechanics: weight budget, stiffness and vibration (why the IMU needs soft mounting), propeller guards for indoor safety.
- [ ] Access: find a library makerspace or community makerspace; learn its induction rules.

---

## 🛠️ Build Requirement
1. **Enclosure** for your Block 9a board with mounting bosses and a cable exit.
2. **Vibration-isolated IMU mount** (TPU dampers or a soft-mount design); measure the vibration reduction with your Block 9a logger.
3. **Prop guard** for a small quad or for the Block 9a see-saw. Each part goes through ≥3 measured revisions.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Revision 3 of each part fits without filing; a drawing with tolerances exists; you can justify each print orientation; measured vibration drops with the isolating mount.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- Onshape Learning Center (free): learn.onshape.com. Onshape Free plan: onshape.com/en/pricing. **Free-plan documents are public**, so keep anything sensitive in FreeCAD.
- FreeCAD 1.0 docs (free, open source): wiki.freecad.org/Getting_started.
- PrusaSlicer (free): prusa3d.com/page/prusaslicer_424/; Prusa Knowledge Base (free, printer-agnostic): help.prusa3d.com.
- Thingiverse (free models to study): thingiverse.com.
- **Kit (💲, approx.):** $0 at a library or makerspace; calipers ≈$15–25; filament ≈$15–25/kg; TPU for dampers. Optional own printer: entry-level models ≈$200–300; only buy if you print weekly.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Fit tests and calipers are the check; post a print to the makerspace or a forum for critique.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- FreeCAD if Onshape's public documents are a problem; OpenSCAD for code-based parametric parts.

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B15a - Signals and Systems Bridge|← Signals and Systems Bridge]] | [[00 - Start Here|Start Here]] | [[B16 - Operating Systems|Operating Systems →]]
