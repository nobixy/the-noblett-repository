---
title: "30 - Capstone — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 30 - Capstone — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[30 - Capstone]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[30 - Capstone]] · [[Worked Proofs Index]]

---

### 1. Empirical Usability Evaluation Framework & WCAG 2.1 Verification Protocol

#### 1. Cognitive Walkthrough Analysis Methodology
A cognitive walkthrough is a task-centered inspection method where evaluators walk through each user action required to complete a critical task, answering four psychological questions:
1. **User Goal Alignment:** *Will the user try to achieve the right effect?* (Does the user's mental model anticipate that this step is necessary to reach their goal?)
2. **Action Visibility:** *Will the user notice that the correct action is available?* (Is the button, menu option, CLI flag, or link visible and prominent, avoiding hidden affordances?)
3. **Semantic Association:** *Will the user associate the correct action with the desired effect?* (Do signifiers, labels, and iconography clearly communicate the operation according to real-world conventions?)
4. **Progress Feedback:** *If the correct action is performed, will the user see that progress is being made?* (Does the system provide immediate, unambiguous feedback confirming the state transition?)

#### 2. Severity Rating Scale for Usability Heuristics
Heuristic violations are categorized using Jakob Nielsen's severity metric to drive remediation prioritization:
- **0 - Not a usability problem:** Subjective design variance with no measurable impact on task execution.
- **1 - Cosmetic problem only:** Minor aesthetic flaw; low priority fix unless extra development bandwidth exists.
- **2 - Minor usability problem:** Low-frequency issue that slows user workflow but has an obvious workaround; should be resolved in normal sprint cadence.
- **3 - Major usability problem:** High-frequency or high-severity obstacle that causes user confusion, significant delay, or frequent errors; must be prioritized and resolved before release.
- **4 - Usability catastrophe:** Imperative blocker that prevents users from completing primary tasks or induces irreversible data corruption; release-blocking critical defect.

#### 3. W3C WCAG 2.1 Level AA Compliance Matrix for Engineering Artifacts
All user-facing interactive surfaces must satisfy the four POUR principles:
- **Perceivable:** Text alternatives for non-text content (`alt` attributes, ARIA labels); minimum 4.5:1 luminance contrast ratio for regular text and 3:1 for large text; interface elements adapt to user zoom up to 200% without loss of content.
- **Operable:** 100% functionality accessible via keyboard interface; no keyboard traps (`tabindex` order is cyclical and logical); skip links provided to bypass repetitive navigational headers; sufficient time provided for interactions.
- **Understandable:** Predictable UI operation; input error identification and descriptive suggestion text provided automatically; human-readable labels and instructions for all inputs.
- **Robust:** Valid, well-formed semantic markup; full compatibility with assistive technologies via correct platform Accessibility Tree (AXTree) exposure.
