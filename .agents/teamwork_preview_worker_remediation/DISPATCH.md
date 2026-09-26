## 2026-09-25T09:47:26Z

You are the Standards & Test Remediation Worker.
Your Working Directory: /home/noblixy/The Noblett Repository/.agents/teamwork_preview_worker_remediation
Original Request Path: /home/noblixy/The Noblett Repository/.agents/ORIGINAL_REQUEST.md
Master Project Plan: /home/noblixy/The Noblett Repository/.agents/PROJECT.md
Reviewer 1 Evidence Report: /home/noblixy/The Noblett Repository/.agents/teamwork_preview_reviewer_1/handoff.md

MANDATORY: You MUST read /home/noblixy/The Noblett Repository/.agents/ORIGINAL_REQUEST.md before starting work.
Study the detailed evidence and critique in /home/noblixy/The Noblett Repository/.agents/teamwork_preview_reviewer_1/handoff.md.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Your Remediation Scope & Exclusive File Ownership:
1. Integrate comprehensive Human-Computer Interaction (HCI) into `/home/noblixy/The Noblett Repository/01 - Curriculum/Year 3 - Depth/17 - Software Construction.md`:
   - Add explicit syllabus modules covering: User-Centered Design (UCD), mental models vs implementation models (Don Norman), Fitts's law, Hick-Hyman law, Nielsen's 10 usability heuristics, cognitive walkthroughs, W3C WCAG 2.1 AA/AAA accessibility standards, accessibility tree, keyboard navigation, contrast ratios.
   - Enhance build requirements to include heuristic evaluation and automated accessibility auditing.
2. Integrate HCI requirements into `/home/noblixy/The Noblett Repository/01 - Curriculum/Year 5 - MEng/30 - Capstone.md`:
   - Add mandatory usability testing, cognitive walkthrough, and WCAG accessibility compliance verification to capstone requirements.
3. Update `/home/noblixy/The Noblett Repository/01 - Curriculum/Baseline Gap Analysis and Audit Report.md`:
   - Update Section 1.1 (line 52) and remediation summary to document the exact HCI modules in `17 - Software Construction.md` and `30 - Capstone.md`.
4. Harden the test harness `/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py`:
   - In `test_tier3_cs2023_knowledge_areas_coverage`: Remove the self-certifying check on `Baseline Gap Analysis and Audit Report.md`. Search ONLY genuine curriculum course blocks in `01 - Curriculum/` (excluding the gap report itself).
   - Add `test_tier3_ce2016_knowledge_areas_coverage`: Verify all 12 IEEE CE2016 Knowledge Areas (CE-CAE, CE-CSG, CE-DIG, CE-CAO, CE-ESY, CE-CAL, CE-SWD, CE-NWK, CE-VLS, CE-SEC, CE-SPE, CE-FND) across genuine course blocks (excluding the gap report).
5. Run the test harness: `python3 "/home/noblixy/The Noblett Repository/.agents/test_suite/test_curriculum.py" -v` and confirm all tests pass cleanly.
6. Write your detailed handoff report in `/home/noblixy/The Noblett Repository/.agents/teamwork_preview_worker_remediation/handoff.md`.
7. Send a message to parent notifying that remediation is complete.
