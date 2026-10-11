---
title: "Project 3: Burrow Jr., a Mini Shell"
id: "MOD01-PRJ-shell-sketch"
type: "project"
module: "01-intro-cs-taste"
phase: "A"
order: 280
prerequisites: [MOD01-LAB02]
artifact: "burrow_jr.py: a shell that runs programs as real processes, with built-ins, redirection, one pipe, and a trace mode"
deliverable: "README + 6–8 sentence explanation of fork/exec/wait + short demo"
---

# Project 3: Burrow Jr., a Mini Shell

| | |
| :-- | :-- |
| **Module** | 01 Intro CS Taste |
| **Prerequisites** | Labs 00–02; you've used the terminal regularly across your first sections |
| **Platform** | Linux, macOS, or WSL2 (it uses `fork`, which native Windows doesn't have) |
| **You build** | A small shell — the program that reads your commands and runs them — using the same operating-system calls real shells use: `fork`, `exec`, `wait`, `pipe`, and `dup2`. Plus a trace mode that shows every process being born and dying |
| **Deliverable** | README, a short explanation, and a demo |

---

## Why this matters

You've typed hundreds of commands into a shell. What actually happens when you press Enter? The shell asks the operating system to make a **copy of itself** (`fork`), the copy **replaces itself** with the program you named (`exec`), and the shell **waits** for it to finish. Every program you've ever launched from a terminal was born this way.

In this project you write that loop yourself, in Python, using the real system calls. You'll see your shell's processes appear in `ps`, you'll discover why `cd` can't be a normal program, and you'll connect two programs with a pipe.

In [Module 07](../../../07-systems-programming/overview.md) you'll build **Burrow**, a full shell in C with job control and scripting, and in [Module 08](../../../08-operating-systems/overview.md) you'll see how the kernel creates and schedules these processes. Burrow Jr. is the small, real version.

**Real-world analogs:** `bash`, `zsh`, `fish`, `dash`.

---

## Background (read before Milestone 1)

- A **process** is a running program: its code, its memory, and its open files. Each has a number, the **PID**. Run `ps -ef | head` and `pstree -p | head` to see yours.
- **`os.fork()`** makes an almost-exact copy of the current process. Both copies continue from the same line. In the **parent**, `fork()` returns the child's PID; in the **child**, it returns 0. That's how each copy knows which one it is.
- **`os.execvp(program, args)`** replaces the current process's program with a new one (searching the `PATH` for it). If it succeeds, it **never returns** — the old code is gone.
- **`os.waitpid(pid, 0)`** makes the parent wait until the child finishes, and tells it the child's **exit status** (0 usually means success).
- **File descriptors:** every process has numbered open files. 0 = standard input (keyboard), 1 = standard output (screen), 2 = standard error. Redirection and pipes work by changing what these numbers point to, using **`os.dup2`**.

```python
import os
pid = os.fork()
if pid == 0:
    # child
    os.execvp("ls", ["ls", "-l"])
else:
    # parent
    _, status = os.waitpid(pid, 0)
    print("child exited with", os.waitstatus_to_exitcode(status))
```

Run this tiny program before starting. Read it line by line until you can explain every line [F].

---

## Milestones

### Milestone 1 — The loop

**Build `burrow_jr.py`:**
1. Print a prompt showing the current directory and the last exit status: `[0] ~/workbench $ `.
2. Read a line. Split it into words with `shlex.split` (handles quotes: `echo "hello world"` → `["echo", "hello world"]`).
3. Empty line → prompt again. End of input (`Ctrl+D`, which makes `input()` raise `EOFError`) → exit cleanly.
4. `fork`; in the child, `execvp`. If `execvp` fails (command not found), print `burrow: command not found: <name>` to standard error and end the child with `os._exit(127)`.
5. In the parent, `waitpid` and remember the exit status for the next prompt.
6. `Ctrl+C` should stop the running *child*, not the shell. (Hint: the shell can ignore `SIGINT` while waiting — `signal.signal(signal.SIGINT, signal.SIG_IGN)` — and the child should restore the default with `signal.SIG_DFL` before `exec`.)
7. In the child, before `exec`, also restore **`SIGPIPE`** to its default: `signal.signal(signal.SIGPIPE, signal.SIG_DFL)`. Python quietly ignores `SIGPIPE` when it starts, and an *ignored* signal stays ignored across `exec`. Without this line, programs you launch behave differently than in a real shell (you'll see exactly how in Milestone 5).

**Experiment:** run `sleep 30` in Burrow Jr. In another terminal: `pstree -p | grep -A2 burrow` (or `ps -ef | grep sleep`). Find your shell and its child. Note the PIDs.

**Done when:** `ls -l`, `echo "two words"`, `false` (status 1 shown in the next prompt), and a nonexistent command (status 127) all work; Ctrl+C stops `sleep 30` but not the shell.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *fork, exec, and wait*, in plain words. (Analogy suggestion: photocopying a recipe card, then rewriting the copy into a different recipe.)

### Milestone 2 — Built-ins

Some commands **must** run inside the shell itself.

**Build:**
- `cd <dir>` (and `cd` alone → home) using `os.chdir`.
- `exit [n]` — exit the shell with status n.
- `history` — the numbered list of commands this session; `!n` reruns command n.

**Experiment first:** before writing `cd`, try running `cd /tmp` the normal way (fork + exec). On most systems there's a `/usr/bin/cd`, or `exec` fails. Either way, the prompt's directory doesn't change. Why? [W]

**Done when:** all three built-ins work, and you've written the answer to the why-ladder below.

**[W] Why-ladder (write it in the README):** *Why must `cd` be a built-in?* (1) Each process has its own current directory. (2) A forked child that changes *its* directory doesn't affect the parent… (3) …so what would `exit` have the same problem with?

### Milestone 3 — Redirection

**Build:** `>` (write output to a file, replacing it), `>>` (append), `<` (read input from a file).

```
[0] ~ $ echo hello > greeting.txt
[0] ~ $ wc -c < greeting.txt
6
```

In the child, **before** `exec`: open the file with `os.open` (flags: `O_WRONLY | O_CREAT | O_TRUNC` for `>`; `O_APPEND` instead of `O_TRUNC` for `>>`; `O_RDONLY` for `<`), then `os.dup2(fd, 1)` (or 0), then close the original fd. The program you exec never knows its output is going to a file. **[W]** Why is that the whole trick, and why is it elegant?

**Done when:** all three operators work, together too (`sort < in.txt > out.txt`).

### Milestone 4 — One pipe

**Build:** `command1 | command2` — command1's output becomes command2's input.

**Subgoal labels [S]:**
```python
# 1. Create a pipe: r, w = os.pipe()  (bytes written to w can be read from r)
# 2. Fork child 1: dup2(w, 1) so its output goes into the pipe; close r and w; exec command1
# 3. Fork child 2: dup2(r, 0) so its input comes from the pipe; close r and w; exec command2
# 4. Parent: close BOTH r and w; wait for both children
```

**Experiment — the hang:** deliberately forget step 4's closing in the parent. Run `ls | wc -l`. It hangs. Why? (Hint: `wc` keeps reading until *every* write end of the pipe is closed. Who still holds one?) Fix it and write the explanation down. This is one of the most common real bugs in systems programming; you'll meet it again in C.

**Done when:** `ls -l | wc -l`, `cat burrow_jr.py | grep def`, and `yes | head -3` all work and exit cleanly.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: the hang.

### Milestone 5 — Trace mode

`python3 burrow_jr.py --trace` prints every process event to standard error, with a timestamp in milliseconds since the shell started:

```
[    0.0] shell pid 41200
[ 1532.4] fork -> child 41231
[ 1532.9] child 41231: exec ls -l
[ 1540.1] wait: 41231 exited 0  (7.7 ms)
[ 3001.2] fork -> child 41240   (pipe stage 1)
[ 3001.6] fork -> child 41241   (pipe stage 2)
[ 3002.0] child 41240: exec yes
[ 3002.3] child 41241: exec head -3
[ 3004.9] wait: 41241 exited 0
[ 3005.1] wait: 41240 killed by signal SIGPIPE
```

**Experiment:** run `yes | head -3` in trace mode. `yes` prints `y` forever — so how does it ever stop? Find the answer in your trace (look up `SIGPIPE`) and explain it.

**Done when:** trace mode shows forks, execs, and waits with exit codes or signals, and you've explained the `yes | head` result.

---

## Testing guidance

Write `test_burrow_jr.py` that runs your shell as a subprocess, feeds it commands on standard input, and checks its output:

```python
import subprocess
def run_shell(script):
    return subprocess.run(["python3", "burrow_jr.py"], input=script,
                          capture_output=True, text=True, timeout=10)

def test_echo_redirect(tmp_path):
    out = run_shell(f"cd {tmp_path}\necho hi > f.txt\ncat f.txt\n")
    assert "hi" in out.stdout
```

Test: plain commands, quoting, exit statuses, not-found (127), `cd`, `history` and `!n`, each redirection, a pipe, and that the shell exits on end of input. (Tip: print the prompt only when input is a terminal — `sys.stdin.isatty()` — so tests don't see prompts.)

## Common pitfalls

- **Code after `execvp` running in the child.** If exec fails and you don't `os._exit`, the child keeps running *your shell's* loop — now you have two shells reading the same keyboard. Very confusing. Always `os._exit(127)` after a failed exec.
- **`exit` vs `os._exit` in the child:** use `os._exit` in a forked child, so it doesn't run the parent's cleanup code twice.
- **Not closing pipe ends** (Milestone 4).
- **Inherited signal settings:** signals the shell ignores stay ignored in the programs it execs. Restore `SIGINT` and `SIGPIPE` to `SIG_DFL` in the child. (Try Milestone 5's `yes | head -3` without the `SIGPIPE` line: `yes` prints a "Broken pipe" error and exits 1 instead of being quietly stopped by the signal.)
- **Zombies:** a child that has finished but hasn't been `wait`ed for stays in the process table as a "zombie" (`<defunct>` in `ps`). Wait for every child.
- **Parsing the operators naively:** `echo a>b` (no spaces) — decide whether you support it and document it.

## Communication deliverable

Sized for E04–E06:
1. **README.md:** what Burrow Jr. supports, how to run it and the tests, and the two why-ladders (`cd` as a built-in; the pipe hang).
2. **"How a shell runs a command" (6–8 sentences):** fork, exec, wait, in simple sentences.
3. **Demo:** run commands, a redirect, a pipe; show the trace for `yes | head -3`; show your shell and its child in `pstree`.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 3, draw fork/exec/wait as a timeline from memory |
| **F** | Fork/exec/wait in plain words |
| **W** | `cd` as built-in; dup2 as the trick; the pipe hang; SIGPIPE |
| **S** | Pipe subgoals as comments |
| **D** | Pipe hangs are confusing; stuck notes |
| **T** | README, explanation, demo |

## Stretch goals

- **Many pipes:** `a | b | c | d`.
- **Background jobs:** `sleep 5 &` returns to the prompt immediately; report when it finishes.
- **Environment variables:** `export NAME=value` and `$NAME` expansion.
- **Tab completion** with the `readline` module.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Process loop | fork/exec/wait, statuses, 127, Ctrl+C handled | Runs commands | Bugs with failed exec |
| Built-ins | cd, exit, history, !n; why-ladder written | Some | Missing |
| Redirection | >, >>, <, combined | Some | Missing |
| Pipe | Works, no hangs, no zombies, hang explained | Works | Hangs |
| Trace | Forks, execs, waits, signals; SIGPIPE explained | Partial | Missing |
| Tests and communication | Subprocess tests; clear README and demo | One | Neither |

**Done when:** every area at least 2; Process loop and Pipe at 3.

## Connections

- **Back:** [Lab 00](../../labs/lab-00-machine-setup.md) (terminal), [Terminal Field Notes](../../../00-foundations/english/projects/terminal-field-notes/spec.md) (processes, `ps`).
- **Forward:** [07](../../../07-systems-programming/overview.md) — **Burrow**, the full shell in C (job control, scripting, a test harness, and a trace timeline). [08](../../../08-operating-systems/overview.md) — what `fork` and `exec` do inside the kernel, and how your own kernel creates processes.

> **Originality note:** Burrow Jr.'s milestones (including the trace mode and the deliberate pipe-hang experiment) were written for this curriculum.
