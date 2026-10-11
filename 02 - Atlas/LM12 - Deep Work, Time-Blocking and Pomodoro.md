---
title: "LM12: Deep Work, Time-Blocking and Pomodoro"
type: learning-method
method_id: LM12
evidence: "Weak to moderate; mostly practitioner advice"
---

# LM12 — Deep Work, Time-Blocking and Pomodoro
*Deep dive + project ([[DR-009 - Learning Method Deep Dives|DR-009]]). Hub: [[LM00 - Learning Methods Hub|Learning Methods]] · Method in practice: [[how-i-study]] §1*

> [!NOTE] Evidence: **Weak to moderate; mostly practitioner advice**

## In plain words
Protect blocks of time for hard work with no distractions, plan your day in blocks, and use timed sessions (Pomodoro: 25 minutes on, 5 off) to start and to rest.

## The evidence, honestly
*Deep Work* (Newport 2016) is a well-argued book, not a study.
What is well established is that switching tasks has a cost (Rubinstein, Meyer & Evans 2001).
Pomodoro itself is barely studied. Biwer et al. (2023) found that Pomodoro-style planned breaks gave better concentration and motivation than self-chosen breaks, but no difference in how much work got done.
Use the timer if it helps you start. Don't treat it as magic.

## Using it in EECS
- Hard proofs, kernel labs and debugging need long, unbroken blocks; a focused build session is the deep-work block.
- Shallow work (email, setup, admin) goes outside your study sessions, or at the end of one.

## Common mistakes
- Counting time at the desk instead of focused time.
- Phone in the room.
- Pomodoro breaks that turn into 40 minutes of scrolling.

## 🔨 Project: Focus Timer CLI
A Python terminal timer with a choice of 25/5 or 50/10 sessions. It appends a line like `- 🍅 25 min: <task>` to the current session log entry and a row to a CSV, and prints your total per section.
- **Done when:** you used it for 10 sessions, the per-section total prints, and it never breaks a note (test it on a copy of the vault first).
- **Level:** Beginner-to-intermediate Python (time, files, dates).
- **Fits with:** No protocol code; it informs how you protect a focused session (see [the session loop](<../study-protocols.md#the-session-loop>)).

## Sources
- Newport, *Deep Work* (2016).
- Rubinstein, Meyer & Evans (2001), "Executive control of cognitive processes in task switching", *Journal of Experimental Psychology: Human Perception and Performance* 27(4).
- Biwer et al. (2023), "Understanding effort regulation: comparing 'Pomodoro' breaks and self-regulated breaks", *British Journal of Educational Psychology*.
