---
title: "OSS Project: Embeddable Typing Test (Monkeytype)"
type: project
tags:
  - project
  - open-source
  - portfolio
status: not-started
license_upstream: "GPL-3.0"
counts_toward: "Employability Portfolio items 2–3 / T10 capstone"
---

# OSS Project — Embeddable Typing Test (Monkeytype)
*Open-source portfolio project. On the [[Projects Ladder]]; feeds the [[Employability Portfolio and Review|Employability Portfolio]]. Facts checked 2026-10-10.*

**Goal:** a typing test any website can drop in with one tag: job-skill tests (data entry, support, transcription), class warm-ups, onboarding. Learn from Monkeytype, contribute to it, then build the embeddable version with results an employer can trust.

> [!WARNING] Not legal advice. The license notes below are a summary of the GPL text and common readings of it. If a company wants to ship this commercially, they should check with their own lawyer.

---

## 🔎 What I checked (2026-10-10)

**Monkeytype** — github.com/monkeytypegame/monkeytype (~20.8k ⭐, active, pushed 2026-10-09)
- **License: GPL-3.0** (the LICENSE file, and GitHub's detection).
- **Stack:** TypeScript monorepo (pnpm workspaces + Turborepo), Node 24 (`>=24 <25`), pnpm 11.
  - `frontend/`: Vite, SolidJS for new components (legacy code is vanilla TS), Tailwind, Chart.js.
  - `backend/`: Node + Express with ts-rest contracts, MongoDB, Redis (BullMQ), Firebase Auth.
  - `packages/`: shared `contracts`, `schemas`, `funbox`, `challenges`, `util`.
- **Contributing:**
  - Basic guide (`docs/CONTRIBUTING_BASIC.md`): themes, quotes, languages and layouts are JSON. No local server needed.
  - Advanced guide (`docs/CONTRIBUTING_ADVANCED.md`): Node + pnpm. Docker is recommended for MongoDB and Redis. Firebase is optional, but accounts won't work without it.
  - PR titles use Conventional Commits with your handle at the end, e.g. `impr(quotes): add english quotes (@you)`.
  - Questions go to the `#development` channel on Discord or to GitHub Discussions.
  - There is no "good first issue" label. Use `help wanted` instead, and check `hacktoberfest-accepted` in October.
- **Embedding today:** monkeytype.com sends `X-Frame-Options: DENY` and `frame-ancestors 'none'`, so **you cannot iframe the live site**. You have to host your own build.
  - I found no upstream issue or discussion about an embed or widget mode. Search again before S5, and ask on Discord before you build anything you hope to upstream.
- **Self-hosting:** `docs/SELF_HOSTING.md` exists. An open PR (#8441, Oct 2026) adds offline local auth for self-hosters.

**Alternatives (so you don't duplicate)**

| Project | License | What it is | Gap |
| :--- | :--- | :--- | :--- |
| `typing-test-element` (24webcomponents) | MIT | a `<typing-test>` web component on npm | tiny demo: 1 ⭐, no results API or anti-cheat |
| `react-typing-test` | MIT | a React component | last updated 2023, React-only |
| Eletypes | GPL-3.0 | a full typing site (React + Vite), inspired by Monkeytype | a site, not an embed |

None of them offers trusted, signed results for hiring. **That gap is the project.**

---

## ⚖️ License: what GPL-3.0 means here
1. **Forking or copying Monkeytype code** (including its word lists and quotes from the repo) makes your widget a derivative work. It must be **GPL-3.0**, with source available.
2. **Serving JavaScript to a browser counts as "conveying"** under GPL-3.0. Whoever hosts the widget has to offer the source: a link to your public repo at the same version is enough (GPL-3.0 §6(d)).
3. **Iframe vs bundling:**
   - **Iframe + `postMessage`:** the employer's page and your widget stay *separate programs* that pass data. The common reading is that this is an "aggregate", so the host page doesn't become GPL.
   - **An npm package bundled into their JS:** much closer to a combined work. The employer's front-end bundle could then fall under GPL.
   - So **ship the iframe as the main embed**, and make the web component a thin loader that only creates the iframe.
4. **Clean-room alternative:** write your own engine from scratch, without copying Monkeytype code or data. Then you can choose MIT. It takes more work and teaches more. Decide at S2 and write the choice in your design doc.
5. **Name and branding:** call it something of your own, e.g. "an embeddable typing test, built on Monkeytype". Don't present it as official Monkeytype unless the maintainers agree.
6. GPL (not AGPL): a server-only change that never sends code to users carries no source obligation. Publish it anyway; it's a portfolio piece.

---

## 🧑‍💼 The job-skill-test angle (design rules)
- **Trust model:** the browser is the candidate's machine, so **never trust a score the client computes**.
  - The widget sends the **raw keystroke log** (key + timestamp).
  - The **server replays it** and computes WPM and accuracy itself.
- **Signed results:** the server signs the result (JWS with Ed25519 / EdDSA). Employers verify it with your **public key**, so no shared secret is handed out.
  - HMAC only fits if the employer runs the verifying server themselves.
  - Never put a secret key in front-end code: anyone can read it.
  - Include the test ID, a nonce, the time issued and the config hash in the signed payload, so a result can't be replayed for a different test.
- **Anti-cheat (raise the cost; it can't be perfect):**
  - Block paste and drop.
  - Ignore events where `isTrusted` is false (synthetic input).
  - Track `visibilitychange` and blur, and report them; don't auto-fail.
  - Use one-time server-generated passages.
  - Flag keystroke timing that is too regular (bots) or impossibly fast.
  - Rate-limit and use single-use test tokens.
  - Report flags to the employer as **signals for a human to review**, not an automatic verdict.
- **Accessibility and fairness** (US-focused; check local law elsewhere):
  - **ADA:** employers must give reasonable accommodations on pre-employment tests, e.g. extra time or another format, unless the test is designed to measure that skill. Typing speed can be a legitimate skill to measure, but only if it is really *job-related* (EEOC guidance; 29 CFR 1630.11 appendix).
  - **Build accommodations in:** an employer-set time multiplier (1.5×, 2×), an untimed accuracy-only mode, no flashing, and adjustable font, contrast and motion.
  - **WCAG 2.2:** SC 2.2.1 Timing Adjustable lets a timed test claim the "essential" exception. Still offer the adjustment, because it's how employers meet the ADA.
  - Keyboard-only flow, a screen-reader-friendly start screen and results, announced status changes (live regions), and contrast ≥ 4.5:1.
- **Privacy:**
  - Keystroke timing can identify a person (keystroke dynamics). Treat the raw log as sensitive.
  - Keep it only as long as scoring needs, then store the score and aggregate features.
  - Get clear consent, collect no tracking or ads in the widget, delete on request, and publish a short privacy note.
  - In the EU, using it to *identify* people would make it special-category data (GDPR Art. 9), so don't.

---

## 🛠️ Stages (each has a done-when)

### S1 — Learn the codebase, first upstream PR
*When:* the basic PR after [[P4 - Programming On-Ramp|P4]]'s CS50 Week 8 (HTML, CSS, JS); the local run after CS50 Week 9 or Full Stack Open Part 0–1. *Hours:* ~8 h, from weekly mini-build slots ([[how-i-study#2b. Weekly Mini-Build|§2b]]).
- [ ] Fork, then make one **basic contribution** (a theme, quotes or a word list) following the PR naming rule.
- [ ] Run the frontend locally (Node 24 + pnpm; Firebase skipped) and trace one test run: input → WPM → result screen. Write a one-page map of the code.
- [ ] Pick a `help wanted` issue or a small bug you found, and ask on Discord before you start.

**Done when:** one PR merged upstream (any type), and the frontend runs locally with your one-page map in the repo's notes.

### S2 — Minimal embeddable widget
*When:* after Full Stack Open Parts 0–2 + 9 (TypeScript). *Hours:* ~20 h.
- [ ] Choose the license path in your design doc: GPL fork, or clean-room MIT.
- [ ] `<typing-test mode="time" duration="60" lang="english">` web component. It creates a sandboxed iframe you host (e.g. GitHub Pages or Cloudflare Pages, free).
- [ ] `postMessage` API: `ready`, `start`, `progress`, `finish {wpm, acc, raw}`. Check `event.origin` on both sides.
- [ ] Demo page on a different domain.

**Done when:** a page on another origin embeds the test with one script tag + one element, gets a `finish` event with the score, and the origin checks reject a message from an unknown site.

### S3 — Results API, signed results, employer dashboard
*When:* after [[B19 - Networking|B19]] (HTTP, CORS, TLS) and during [[B24a - Applied Cryptography and Protocol Security|B24a]] (signatures, replay). Use Full Stack Open Parts 4–5 + 13 for auth and Postgres. *Hours:* ~35 h.
- [ ] Backend: an employer creates a test (config + single-use tokens), the widget submits the keystroke log, and the server replays it and scores it.
- [ ] Signed result: JWS (EdDSA), a published public key, and a tiny `verify` CLI or page.
- [ ] Simple dashboard: log in, create a test, copy the embed snippet, see the results table with flags.

**Done when:** a result changed by one character fails verification, a replayed result for another test ID fails, and a friend can create a test and see your score on the dashboard.

### S4 — Anti-cheat and accessibility audit
*When:* with [[B17 - Software Construction|B17]]'s HCI and accessibility material and [[B24a - Applied Cryptography and Protocol Security|B24a]]'s threat modeling. *Hours:* ~15 h.
- [ ] STRIDE threat model of the widget + API (same method as B24a), then attack it yourself: paste, a synthetic-event bot, editing the request, replay, token reuse.
- [ ] Accessibility: `axe-core` or `pa11y` in CI with zero serious violations, a keyboard-only run, a screen-reader pass (Orca on Linux, free), and accommodation settings (time multiplier, untimed mode, reduced motion).

**Done when:** the threat model is written and every attack you tried is either blocked or reported as a flag. The audit is in CI and green, and an untimed accessible run works from start to signed result without a mouse.

### S5 — Publish
*When:* before the [[Employability Portfolio and Review|Employability Portfolio]] review (end of Year 4). *Hours:* ~15 h.
- [ ] npm package for the loader, a docs site with a live demo, and CI/CD (Full Stack Open Part 11).
- [ ] License compliance: LICENSE file, source link in the widget footer, and attribution to Monkeytype if you forked.
- [ ] Privacy note and an accessibility statement.
- [ ] Write-up: design doc + a postmortem of one wrong assumption. If the maintainers showed interest in S1/S2, open a Discussion upstream with a link to it.

**Done when:** `npm install` + two lines embeds it on a fresh site, the docs and demo are live, one person other than you has used it, and the write-up is published.

---

## 🔗 Prerequisites → blocks
| Stage | Uses |
| :--- | :--- |
| S1 | [[P4 - Programming On-Ramp\|P4]] (CS50 Weeks 8–9), Git basics from [[Engineering Practice]] |
| S2 | [[T10 - Full-Stack and Product Engineering\|T10]] Full Stack Open Parts 0–2, 9 |
| S3 | [[B19 - Networking\|B19]], [[B24a - Applied Cryptography and Protocol Security\|B24a]], T10 Parts 4–5, 13 |
| S4 | [[B17 - Software Construction\|B17]] (HCI, accessibility), B24a (STRIDE) |
| S5 | T10 Part 11 (CI/CD), [[Employability Portfolio and Review\|Employability Portfolio]] |

## ⏱️ Hours (no hours added)
About 93 h total, all swapped for existing hours:
- **S1:** ~8 h from weekly mini-build slots.
- **S2, S3, S5:** ~70 h. These *are* the Employability Portfolio's item 2 (full-stack app with auth + database) and item 3 (an API with CI/CD and tests). If Track 10 is one of your two tracks, they also count toward its capstone.
- **S4:** ~15 h, taken from Track 10 build time, or from the portfolio items' polish if Track 10 isn't chosen.

The core stays at 6,005 h.

*Back to [[Projects Ladder]] · [[Projects Hub]] · [[00 - Start Here|Start Here]]*
