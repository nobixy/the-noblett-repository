---
title: "Project: Worldfile"
id: "MOD02-PRJ-worldfile"
type: "project"
module: "02-programming-fundamentals"
phase: "B"
order: 480
prerequisites: [MOD02-LAB03]
artifact: "wf: a text-adventure engine whose worlds are data files — a parser with precise errors, a recursive condition language, events, save/load, a linter, golden playthrough tests — plus one full world you wrote"
deliverable: "Design note, WORLD_FORMAT.md reference, README, a playtested world, short demo"
---

# Project: Worldfile

| | |
| :-- | :-- |
| **Module** | 02 Programming Fundamentals |
| **Prerequisites** | Labs 01–03 of this module (recursion especially); Lab 01's adventure from Module 01 |
| **You build** | `wf`, an engine that plays text adventures described entirely in data files. You design the file format, write its parser with precise error messages, build a small **condition language** with a recursive parser and evaluator, add events, puzzles, save and load, a **linter** that finds broken worlds, and a test runner that replays scripted playthroughs. Then you write a real world and have someone play it |
| **Deliverable** | Design note, a format reference, README, your world (playtested), and a demo |

---

## Why this matters

In Module 01's last Python session you wrote a tiny adventure with the rooms in your code. That doesn't scale: every new room means editing the program. Real software separates **engine** (the code) from **content** (the data): game engines and levels, browsers and web pages, compilers and source code. Once you do that, you need a **file format**, a **parser** that turns text into structure, and helpful **error messages** for the humans who write the data.

The condition language (`when has(key) and not flag(door_open)`) is your first real **expression language**: you'll parse it into a tree with a recursive parser and evaluate the tree recursively. That's exactly how interpreters and compilers work at their core. In Module 06, you'll use the same technique to compile a small language to your own CPU's machine code.

And the linter is your first **static analysis** tool — finding bugs without running the program — using a graph search to find unreachable rooms.

**Real-world analogs:** game engines with level/data files (and text-adventure systems like Inform and Twine), configuration languages, rule engines, linters.

---

## The world format (starting point)

You may change any of this; document every change and why in `WORLD_FORMAT.md`.

```
# lighthouse.wf
world "The Lighthouse"
start dock

room dock
  title "The Dock"
  text  "Waves slap the old boards. A path climbs north toward a lighthouse."
  exit north -> path
  item rope "a coil of wet rope"

room path
  title "Cliff Path"
  text  "Wind tugs at your coat. The dock is south; a door stands north."
  exit south -> dock
  exit north -> base  when flag(door_open)

room base
  title "Lighthouse Base"
  text  "A spiral stair winds up into darkness."
  exit south -> path
  exit up -> top      when has(lamp)
  item lamp "a brass oil lamp"

room top
  title "The Lamp Room"
  text  "The great lens waits, cold and dark."
  exit down -> base

on enter top when not flag(seen_top)
  say "Through the salt-stained glass you can see the whole coast."
  set seen_top

action open door when here(path) and not flag(door_open)
  say "The door groans open."
  set door_open

action light lens when here(top) and has(lamp) and has(matches)
  say "The lens blazes. Far out at sea, a ship turns toward safety."
  set lens_lit

goal "Light the lighthouse" when flag(lens_lit)
```

*This example has a deliberate bug that makes it impossible to win. Can you find it? (Your linter in Milestone 6 should find it automatically.)*

**Pieces:**
- `world`, `start` — the title and the starting room.
- `room <id>` with indented `title`, `text`, `exit <direction> -> <room> [when <condition>]`, and `item <id> "<description>"`.
- `on enter <room> [when <condition>]` followed by indented **effects**.
- `action <verb> <noun> [when <condition>]` followed by indented effects. The player types `open door`.
- `goal "<text>" when <condition>` — the game is won when the condition becomes true.
- **Effects:** `say "<text>"`, `set <flag>`, `unset <flag>`, `give <item>` (into inventory), `take <item>` (remove from inventory), `move <room>` (teleport the player).
- **Built-in commands** the player always has: `look`, `go <direction>` (or just the direction), `take <item>`, `drop <item>`, `inventory` (or `i`), `save <name>`, `load <name>`, `help`, `quit`.

### The condition language

```
condition := term ("or" term)*
term      := factor ("and" factor)*
factor    := "not" factor | "(" condition ")" | atom
atom      := has(<item>) | flag(<flag>) | here(<room>) | visited(<room>) | true | false
```

This little grammar says: `not` binds tightest, then `and`, then `or` — the same precedence as in Python (Discrete Math, Module 03, uses the same rules). `not flag(a) or has(b) and here(c)` means `(not flag(a)) or (has(b) and here(c))`.

Each line of the grammar becomes one **function** in a **recursive-descent parser**: `parse_condition` calls `parse_term`, which calls `parse_factor`, which may call `parse_condition` again for brackets. That's recursion following the shape of the language.

---

## Milestones

### Milestone 1 — Design note and the format

1. **Design note v1** (2 pages): engine vs content; the data model (classes for World, Room, Exit, Item, Action, Event, GameState, and their **invariants** — e.g. "every exit points to a room that exists", "an item is in exactly one place: a room, the inventory, or nowhere yet"); the parse → validate → play pipeline; two design choices with reasons.
2. Write `WORLD_FORMAT.md` v1 and a tiny 3-room test world.

**Done when:** both documents exist and you can explain the pipeline briefly.

### Milestone 2 — The world parser, with precise errors

Parse the world file into objects. Every error reports **file, line, column**, and shows the line with a caret:

```
lighthouse.wf:14:8: expected "->" after the exit direction
  exit north base
         ^
```

**Approach [S]:** read lines; track indentation to know which room or block you're in; split each line into tokens (words, quoted strings, `->`, brackets); dispatch on the first word. Keep the original text of each condition for now (Milestone 4 parses it).

After parsing, **validate** the whole world: the start room exists; every exit's target exists; no duplicate room ids; every `on enter` names a real room.

**Tests:** one fixture per error message (at least 10), each checking the exact line and column; a valid world parses into the expected objects.

**Done when:** all error tests pass, and a typo anywhere in your test world gives a message you'd be happy to receive.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why validate the whole world after parsing instead of checking each exit as you read it?* (Hint: what if an exit points to a room defined later in the file? It's the assembler's two-pass problem from Nib again.)

### Milestone 3 — The engine and golden playthroughs

1. `GameState`: current room, inventory, flags, visited rooms, where every item is.
2. The command loop: built-in commands, exits (ignore `when` conditions for now — treat them as always true), item handling, `look` describing exits and items.
3. **Golden playthrough tests:** a `.play` file is a list of player commands; the runner feeds them to the engine (no keyboard needed — input and output are passed in, as with the fake clock in Lab 02) and compares the full transcript with a golden `.out` file.

```
# tests/basic.play
look
take rope
north
inventory
```

**Done when:** three golden playthroughs pass.

### Milestone 4 — The condition language

1. **Tokenizer** for conditions: words, `(`, `)`, `and`, `or`, `not`, `true`, `false`, and calls like `has(lamp)`.
2. **Recursive-descent parser** producing a tree, for example with small dataclasses: `Or(left, right)`, `And(left, right)`, `Not(inner)`, `Atom(kind="has", arg="lamp")`.
3. **Evaluator** `evaluate(tree, state) -> bool`, recursive: `Or` evaluates its sides and combines them, and so on down to atoms that look at the game state.
4. A debugging helper: `wf explain "<condition>"` prints the tree with indentation and the value of every node in a sample state.
5. Hook conditions into exits, events, actions, and goals.
6. Condition errors point to the exact column *inside the world file*.

**Tests:**
- precedence: `not a or b and c` parses as `Or(Not(a), And(b, c))`;
- brackets: `not (a or b)` parses as `Not(Or(a, b))`;
- evaluation of every operator against a hand-built truth table (8 combinations of three flags — Module 03 will make truth tables your main tool);
- errors: `has(lamp and`, `and flag(x)`, `has()`, unknown atom `fly(x)`.

**Done when:** all tests pass and `wf explain` shows correct trees.

**Checkpoint:** Milestone Checkpoint. Feynman target: *how a recursive-descent parser follows the grammar*, explained with `wf explain` output. Why-ladder target: *why does `and` bind tighter than `or`?* (What would a world writer expect `a or b and c` to mean? What do Python and logic textbooks do?)

### Milestone 5 — Events, actions, goals, save and load

1. `on enter` events run their effects when the player enters the room and the condition holds.
2. `action` verbs: when the player types `<verb> <noun>`, find a matching action whose condition holds and run its effects; otherwise a helpful "You can't do that here." (Which message, if two actions match? Decide and document.)
3. Goals: after every command, check whether the goal condition is now true; if so, print the win message and end.
4. **Save/load:** write the game state to a JSON file (`save <name>`), including a **format version number** and the world's title. Loading checks both and refuses with a clear message if they don't match. [W] Why a version number?

**Tests:** golden playthroughs that win your test world; a save/load round trip (save mid-game, load, continue; the transcript matches an uninterrupted run).

**Done when:** your test world can be won, and save/load round-trips.

### Milestone 6 — The linter, and a real world

**`wf lint world.wf`** finds problems without playing:
- **Unreachable rooms:** do a **breadth-first search** from the start room over exits (ignoring conditions — a room is unreachable if *no* exit path leads there at all). Report rooms the search never visits. (This is your first graph algorithm; Module 05 goes much deeper.)
- **Flags read but never set** (in any `set` effect), and flags set but never read.
- **Items never obtainable** (not placed in any room and never given).
- **Goals that reference flags nobody sets.**

Then **write a real world**: at least **12 rooms**, **3 puzzles** that use conditions, and an ending. Lint it clean. Write room text at your current English level — this is creative writing practice, and clear description is the skill from E09.

**Playtest it:** give it to someone (or post it online with instructions). Watch silently, or ask them for a transcript. Log every place they got stuck or confused (just like the Machine Manual's usability test), and fix the text or the puzzle.

**Done when:** the world lints clean, a playtester finished it, and you've fixed what they struggled with.

---

## Testing guidance

- **Golden playthroughs** are your main safety net. Every bug found while playing becomes a new `.play` file.
- **Parser error fixtures:** one tiny broken file per error message.
- **Condition truth tables:** exhaustive for small numbers of flags.
- **Separate parsing from playing:** a world that parses and validates should never crash during play. If it does, add a validation check.

## Common pitfalls

- **Indentation confusion:** tabs vs spaces. Reject tabs with a clear message, or define exactly how they count.
- **Recursion without progress in the parser:** if `parse_factor` calls `parse_condition` without consuming a `(` first, it recurses forever. Every recursive call must consume at least one token.
- **Mutable state shared between tests:** create a fresh `GameState` for each test.
- **Over-flexible parsing of player input:** `take the brass lamp` vs `take lamp`. Decide what you support, document it, and keep it simple.
- **Error messages for the developer instead of the world writer:** "KeyError: 'base'" is a crash, not a message. "lighthouse.wf:9: exit north leads to unknown room 'base'" is a message.

## Communication deliverable

1. **Design note** v1 and v2.
2. **`WORLD_FORMAT.md`** — the complete language reference, including the condition grammar.
3. **README:** play, lint, explain, test.
4. **Your world** and its **playtest log**.
5. **Demo:** play a short stretch of your world, show a parser error, `wf explain` on a condition, and the linter catching a planted problem.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 4, write the condition grammar and the three parser functions' outlines from memory |
| **F** | Recursive descent; BFS for reachability |
| **W** | Two-pass validation; operator precedence; version numbers in saves; message choice when two actions match |
| **S** | One subgoal per grammar rule; the parse → validate → play pipeline |
| **I** | Parsing, recursion, graph search, and writing interleaved |
| **C** | Copywork during this project: descriptive passages (Level 3 essays with strong description) — then apply it to your room text |
| **T** | Note, format reference, README, world, playtest, demo |

## Stretch goals

- **Variables and numbers:** `set coins = coins + 1` and conditions like `coins >= 3`. Your condition language becomes an expression language with arithmetic precedence (Module 03 and Module 06 both build on this).
- **Containers:** items inside items (`put rope in bag`).
- **Map export:** `wf map world.wf` writes a Graphviz `.dot` file of rooms and exits. Render it (`dot -Tpng`).
- **Shortest solution:** a search over game states that finds the fewest commands to win (BFS over (room, inventory, flags) — watch the state space explode, M11).

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Parser and errors | File:line:col with caret for 10+ errors; whole-world validation | Most errors | Crashes |
| Condition language | Correct precedence and brackets; recursive evaluator; `explain`; truth-table tests | Works, few tests | Wrong precedence |
| Engine | Exits, items, events, actions, goals, save/load with versioning | Most | Basics |
| Tests | Golden playthroughs incl. save/load round trip | Some | None |
| Linter | Reachability by BFS + three other checks | Two checks | Missing |
| World and playtest | 12+ rooms, 3 puzzles, lint-clean, playtested and fixed | Smaller | Missing |
| Communication | Note, reference, README, demo | Most | Few |

**Done when:** every area at least 2; Parser and Condition language at 3.

## Connections

- **Back:** Module 01 Lab 01 Session 10 (the adventure), Pagelet (parse/render split), Nib's assembler (two passes), Lab 01 (recursion), Lab 03 (invariants).
- **Forward:** Module 03 (truth tables, logic, precedence — your evaluator becomes a full logic engine in Truth Engine), Module 05 (graphs and search), Module 06 (Ember: a recursive-descent compiler for a small language that targets your own CPU).

> **Originality note:** the world format, condition language, linter, and milestone structure were designed for this curriculum.
