---
type: design-doc
project: ""
version: 1
date: "{{date}}"
status: draft # draft | built | revised
---

# Design Doc: {{project}}

*Write version 1 **before** the main build, even if it is short and partly wrong. Update it after. The diff between v1 and the final version is one of the most useful things you will ever read about your own thinking.*

*Size guide: early modules 1–2 pages; later modules 3–6 pages. Short sentences. One idea per paragraph. Lead with the point.*

## 1. Summary (3–5 sentences)
What is it, who is it for, and what does it do? A reader who stops here should know what you built.

## 2. Goals and non-goals
- **Goals** (what it must do; testable):
- **Non-goals** (what it will not do, on purpose):

## 3. Background
What does the reader need to know first? Define every technical word you use later. (Two paragraphs maximum.)

## 4. Design
- **Big picture:** one diagram (boxes and arrows is fine) and a paragraph walking through it.
- **Data:** the main data structures, file formats, or message formats. Show one real example of each.
- **Flow:** what happens, step by step, for the most important operation.
- **Errors:** what can go wrong, and what the system does about each.

## 5. Alternatives considered [W]
For each big choice: what else could you have done, and why did you not? (At least two choices.)

| Choice | Picked | Rejected | Why |
| :-- | :-- | :-- | :-- |
|  |  |  |  |

## 6. Testing plan
How will you know it works? List the tests before writing them. Include at least one test for something going wrong.

## 7. Risks and open questions
What are you unsure about? What would you ask an expert?

## 8. After the build (fill in at the end)
- What changed from v1 of this doc, and why?
- What surprised you?
- What would you do differently next time?
