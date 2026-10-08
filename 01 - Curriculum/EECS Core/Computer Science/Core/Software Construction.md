---
block_id: "Block 26"
title: "Software Construction (MIT 6.1020 / 6.031)"
category: "core"
term: "Year 3 Fall"
status: not-started
prerequisites:
  - "CS61A"
  - "C Fluency"
hours_estimate: 150
hours_actual: 0
primary_resource: "MIT 6.1020 / 6.031 Readings & Ousterhout, A Philosophy of Software Design"
milestone: "Rebuilt interpreter under spec, rep invariants, AF, and test strategy"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 26 — Software Construction (MIT 6.1020 / 6.031)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Languages Index|Languages Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Fall
> - **Estimated Hours:** ~150 hrs
> - **Status:** `not-started`
> - **Primary Resource:** MIT 6.1020 / 6.031 Readings & Ousterhout, A Philosophy of Software Design
> - **Key Milestone:** Rebuilt interpreter under spec, rep invariants, AF, and test strategy

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
The most under-appreciated course in the MIT degree. How to write complex code that does not rot, and how to construct software systems that humans can understand, navigate, and operate reliably. Software construction encompasses two fundamental interfaces: the internal software interface (abstract data types, representation invariants, thread safety contracts) and the human-computer interaction (HCI) interface (mental models, usability heuristics, cognitive walkthroughs, and accessibility standards).

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[CS61A]]
- [[C Fluency]]


## 📖 Primary Syllabus & Core Content

### Part 1: Robust Software Architecture & Contracts (MIT 6.1020 Core)
- [ ] Specifications and behavioral contracts (preconditions, postconditions, frame conditions, exceptions)
- [ ] Testing strategies, glass-box vs black-box, input domain partition coverage, boundary value analysis
- [ ] Abstract Data Types (ADTs), Representation Invariants (RI), Abstraction Functions (AF), checkRep()
- [ ] Immutability, defending against representation exposure, defensive copying
- [ ] Recursive data types, context-free grammars, AST traversal, and parser generators
- [ ] Concurrency, thread safety arguments, race conditions, deadlocks, locks, and synchronized monitors
- [ ] Ousterhout, *A Philosophy of Software Design* (deep vs shallow modules, information hiding, error handling)

### Part 2: Human-Computer Interaction (HCI) & Usability Engineering (ACM/IEEE CS2023 HCI Core)
- [ ] **User-Centered Design (UCD) & Interaction Engineering:**
  - Iterative design lifecycle: Discover, Define, Design, Prototype, and Evaluate.
  - Don Norman's Action Cycle: The 7 stages of action (Goal, Plan, Specify, Perform, Perceive, Interpret, Compare); Gulf of Execution and Gulf of Evaluation.
  - Mental models vs. implementation models: Designer's conceptual model, system image, and user's mental model (Don Norman, *The Design of Everyday Things*).
  - Interaction primitives: Affordances, signifiers, mapping (natural mappings), feedback, constraints (physical, logical, semantic, cultural), and error resilience.
- [ ] **Quantitative Usability & Cognitive Laws:**
  - Fitts's Law for target acquisition time ($MT = a + b \log_2(2D/W)$); derivation of Index of Difficulty ($ID$) in bits and human psychomotor throughput ($TP = ID / MT$) in bits/second; screen boundaries and infinite virtual target width.
  - Hick-Hyman Law for cognitive decision time ($T = b \log_2(n + 1)$); Shannon information entropy in decision-making and menu hierarchy organization.
  - Steering Law for constrained movement along tunnels and trajectories.
- [ ] **Heuristic Usability Evaluation & Inspection Methods:**
  - Jakob Nielsen's 10 Usability Heuristics:
    1. Visibility of system status
    2. Match between system and the real world
    3. User control and freedom (emergency exits, undo/redo)
    4. Consistency and standards
    5. Error prevention
    6. Recognition rather than recall
    7. Flexibility and efficiency of use (accelerators, keyboard shortcuts)
    8. Aesthetic and minimalist design
    9. Help users recognize, diagnose, and recover from errors
    10. Help and documentation
  - Cognitive Walkthrough method: Four-question structured task analysis (Will the user try to achieve the right effect? Will the user notice that the correct action is available? Will the user associate the correct action with the desired effect? If the correct action is performed, will the user see that progress is being made?).
  - Discount usability testing, Think-Aloud protocol, formative vs. summative usability evaluations.
- [ ] **Accessibility & Inclusive Design (W3C WCAG 2.1 AA/AAA Standards):**
  - The W3C POUR Principles: Perceivable, Operable, Understandable, Robust.
  - W3C Web Content Accessibility Guidelines (WCAG 2.1 / 2.2 Level AA and AAA standards).
  - The Accessibility Tree (AXTree): Mapping DOM and UI elements to platform accessibility APIs (roles, states, properties, accessible names, accessible descriptions).
  - Keyboard navigation paradigms: Full non-mouse operability, logical tab order (`tabindex`), visible focus indicators, skip navigation links, and elimination of focus traps.
  - Contrast ratios: Relative luminance calculation ($L = 0.2126 R + 0.7152 G + 0.0722 B$), minimum 4.5:1 contrast for normal text and 3:1 for large text (Level AA), 7:1 contrast for Level AAA; non-text contrast ($\ge 3:1$ for UI controls and graphical indicators).
  - Screen reader semantics: ARIA roles, states, properties, live regions (`aria-live="polite"|"assertive"`), and assistive technology compatibility.

### Part 3: Professional Ethics & Responsible Engineering (ACM/IEEE CS2023 SEP Core)
- [ ] ACM/IEEE Software Engineering Code of Ethics and Professional Practice.
- [ ] Ethical implications of dark patterns, manipulative choice architecture, and algorithmic transparency.
- [ ] Accessibility as an ethical obligation and legal requirement (ADA Title III, Section 508, EN 301 549).
- [ ] Open-source licensing compliance, software bill of materials (SBOM), and supply chain security.

---

## 🛠️ Build Requirement
1. **Core Architecture & Optimizing Compiler IR:** Take your `clox` or Monkey interpreter from Block 12 and rebuild it in `c` using `clang` and `make`. Implement an optimizing compiler intermediate representation featuring Static Single Assignment (SSA) form with dominance frontier calculation, dead code elimination, and graph coloring register allocation. Formulate explicit representation invariants (`checkRep`), abstraction functions, and verify 100% unit test coverage and complete absence of memory leaks under `valgrind`.
2. **Interactive Developer Interface (CLI/TUI/Web GUI):** Construct an interactive debugging interface or visual AST/CFG inspector for your compiler/interpreter that exposes variable live ranges, register allocation graphs, and SSA dominance trees.
3. **Formal Heuristic Usability Evaluation:** Conduct an exhaustive heuristic evaluation of your developer interface against Nielsen's 10 Usability Heuristics. Document severity ratings (0: Not a problem, 1: Cosmetic, 2: Minor, 3: Major, 4: Catastrophe) and execute a structured 4-step cognitive walkthrough for primary developer workflows (inspecting SSA $\phi$-nodes, stepping through bytecode, diagnosing type errors).
4. **Automated Accessibility Auditing & Compliance:** Implement an automated accessibility auditing pipeline (integrating `axe-core`, `pa11y`, or a dedicated headless test harness in `pytest`/`node`) verifying strict W3C WCAG 2.1 Level AA compliance:
  - Zero critical or serious accessibility violations.
  - 100% keyboard accessibility: All interactive controls navigable and operable via Tab, Shift+Tab, Enter, Space, and Arrow keys, with zero focus traps and high-visibility focus indicators.
  - Strict contrast ratios: Automated verification that text-to-background contrast satisfies $\ge 4.5:1$ for standard text and $\ge 3:1$ for large text across light and dark themes.
  - Accessibility Tree verification: Ensure all interactive elements expose correct semantic roles, accessible names, and live region announcements for state changes.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> You write a formal rep invariant and abstraction function for any complex type you define, by reflex.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The built-in exercises in each 6.102 reading, and the tests you write under the course's testing strategy.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Refactoring 2e (Fowler); Feathers, Working Effectively with Legacy Code; The Pragmatic Programmer; Software Engineering at Google.

---

## ➡️ Next Steps
- **Topic Hub:** [[Languages Index|Languages Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Databases|← Databases]] | [[00 - Dashboard|Dashboard]] | [[Distributed Systems|Distributed Systems →]]
