---
title: "Lab 00 — Machine Setup"
module: "01-intro-cs-taste"
hours: 6
---

# Lab 00 — Machine Setup

**Goal:** a working setup for the whole curriculum: a terminal you're comfortable in, an editor, Python, git, and your **workbench** — the git repository where every project, note, and log you make will live.

**Time:** about 6 hours, in three sessions.

**You'll finish with:** `~/workbench/` under git, with your first commit; Python running; an editor set up; and the commands you'll use every day in your fingers.

> This repository (the curriculum) is your *map*. `~/workbench/` is your *territory*: your code and your writing. Keep them separate. The map changes rarely; the territory grows every day.

---

## Session 1 — The terminal (2 hours)

The **terminal** is a window where you type commands and the computer answers in text. The program that reads your commands is called the **shell** (on Arch it's probably `zsh` or `bash`). You'll build your own shell in this module ([Burrow Jr.](../projects/shell-sketch/spec.md)) and a real one in Module 07.

### The ten commands

Open a terminal. Type each command, press Enter, and read the result. Say out loud what you think it did *before* reading the explanation.

| Command | What it does | Try |
| :-- | :-- | :-- |
| `pwd` | **p**rint **w**orking **d**irectory: where am I? | `pwd` |
| `ls` | **l**i**s**t what's in this directory | `ls`, then `ls -l`, then `ls -la` |
| `cd` | **c**hange **d**irectory | `cd /tmp`, `pwd`, `cd ~`, `pwd`, `cd ..`, `pwd` |
| `mkdir` | **m**a**k**e a **dir**ectory | `mkdir ~/practice` |
| `touch` | create an empty file (or update its time) | `touch ~/practice/notes.txt` |
| `echo` | print text; with `>` writes it to a file | `echo "hello" > ~/practice/hi.txt` |
| `cat` | print a file's contents | `cat ~/practice/hi.txt` |
| `cp` | **c**o**p**y | `cp ~/practice/hi.txt ~/practice/hi2.txt` |
| `mv` | **m**o**v**e or rename | `mv ~/practice/hi2.txt ~/practice/hello.txt` |
| `rm` | **r**e**m**ove (delete) — **no undo, no trash** | `rm ~/practice/hello.txt` |

Plus: `man <command>` shows the manual (press `q` to quit, `/word` to search). `less <file>` shows a long file one screen at a time.

### Paths

- A **path** says where a file is. `/home/you/practice/hi.txt` is an **absolute** path (starts at `/`, the root of everything).
- `practice/hi.txt` is a **relative** path (starts from where you are now).
- `~` means your home directory. `.` means "here." `..` means "one level up."

### Habits that save hours

- **Tab completion:** type the first few letters of a file or command and press `Tab`. It completes it. Press `Tab` twice to see choices. Use it constantly; it prevents typos.
- **History:** the up arrow brings back earlier commands. `Ctrl+R` then type part of a command searches your history.
- **Stop a running command:** `Ctrl+C`.
- **Clear the screen:** `Ctrl+L`.
- **Be careful with `rm`**, especially `rm -r` (deletes folders and everything in them). Read the command twice before pressing Enter. Never paste an `rm` command from the internet you don't fully understand.

### Practice [R]

1. Close all notes. In a fresh terminal: make a folder `~/practice/lab00`, create three files in it, copy one, rename one, delete one, and list the result with `ls -l`. Write down the commands you used *from memory*, then check them with the up arrow.
2. Play [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) levels 0–5 (free; a game where you log in to a remote machine and use these commands to find passwords). It's excellent practice. Levels 6–15 are a good weekend later.

**[W]:** Why does `rm` have no undo, when your desktop has a trash can? (Hint: the trash can is a feature of a program on top; `rm` asks the operating system directly. You'll see what that means in Module 07.)

---

## Session 2 — Editor and Python (2 hours)

### Choose an editor

| | VS Code | Neovim |
| :-- | :-- | :-- |
| Learning curve | gentle | steep (but fast once learned) |
| Install on Arch | `sudo pacman -S code` | `sudo pacman -S neovim` |
| Recommended for | starting now | later, if you enjoy the keyboard |

**Recommendation:** start with **VS Code**. Install the **Python** extension (by Microsoft). Optional: the **Code Spell Checker** extension for code comments and Markdown, but **turn it off for spelling practice and copywork files** (rule from the English track).

Settings to change (File → Preferences → Settings):
- **Auto Save:** `afterDelay`.
- **Render Whitespace:** `boundary` (so you can see tabs vs spaces — matters for `.tsv` files and Python).
- **Font size:** big enough to read without leaning in.

### Python

Check what you have:

```bash
python3 --version
```

You need 3.12 or newer. On Arch: `sudo pacman -S python python-pytest`. (macOS: `brew install python`. WSL/Ubuntu: `sudo apt install python3 python3-pytest`.)

**The REPL:** type `python3` with nothing after it. You get a `>>>` prompt. Type `2 + 3` and Enter. This is the **REPL** (read–eval–print loop): Python reads what you type, evaluates it, prints the result, and loops. Use it as a calculator and a place to experiment. Leave with `exit()` or `Ctrl+D`.

**Running a file:** make `~/practice/hello.py` in your editor containing `print("Hello from my machine")`. In the terminal: `python3 ~/practice/hello.py`.

That's all you need for now. [Lab 01](lab-01-python-first-steps.md) teaches the language.

### Optional tools (install now, use later)

```bash
sudo pacman -S espeak-ng hunspell hunspell-en_us tk
```

- `espeak-ng`: text-to-speech (Spelling Engine, dictation tests).
- `hunspell`: a command-line spell checker (`hunspell -l file.txt` lists unknown words).
- `tk`: needed for Python's `turtle` graphics (Floor Plan and Turtle).

---

## Session 3 — Git and your workbench (2 hours)

**Git** keeps a history of every version of your files. Each saved version is a **commit**. With git you can see what changed, when, and why, and go back if you break something. Every professional software project uses it.

### Set up git

```bash
sudo pacman -S git            # if not installed
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

### Create the workbench

```bash
mkdir -p ~/workbench/{english,math,01-nib,01-relay,01-burrow-jr,01-pagelet}
cd ~/workbench
git init
```

Create `~/workbench/README.md`:

```markdown
# Workbench

My code, notes, and writing for the Noblett Repository curriculum.
Each folder is one track or project.
```

Create `~/workbench/.gitignore` (files git should never track):

```
__pycache__/
*.pyc
.venv/
.pytest_cache/
*.tmp
```

### Your first commit

```bash
git status                  # what has changed?
git add README.md .gitignore
git commit -m "Create workbench with folders for each track"
git log --oneline           # see your history
```

**Commit messages use the imperative** (E05 Part 6): *"Add …", "Fix …", "Create …"*. They complete the sentence "If applied, this commit will…". Start the habit now; it's daily writing practice.

### The daily git loop

```bash
git status                       # see what changed
git diff                         # see exactly how
git add <files>                  # choose what to save
git commit -m "Imperative summary of the change"
```

**Rule:** commit at least once every study session. Your commit history is your proof of work and your safety net.

### Optional: a private remote backup

You can push your workbench to a **private** repository on GitHub, GitLab, or Codeberg for backup. That's a choice, not a requirement. If you do: keep it **private** at first, and never commit passwords, keys, or personal financial or health information.

---

## Done when

- [ ] You can do the ten commands, paths, tab completion, and history without looking them up.
- [ ] Bandit levels 0–5 done.
- [ ] Your editor is set up and shows whitespace.
- [ ] `python3 --version` shows 3.12+, and `python3 hello.py` works.
- [ ] `~/workbench/` exists, is a git repository, and has at least one commit with an imperative message.

## Retrieval and reflection [R] [F]

1. **Blank sheet (10 min):** the ten commands and what each does; what `~`, `.`, `..` mean; the daily git loop.
2. **Feynman (spoken, 1 min):** "What is git, and why would a single person working alone use it?"
3. **Log:** today's journal entry (two minutes): what you set up, what was confusing, what's next.

**Next:** [Lab 01 — Python First Steps](lab-01-python-first-steps.md).
