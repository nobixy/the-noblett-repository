---
title: "Lab 03 — System Calls and strace"
module: "07-systems-programming"
hours: 8
---

# Lab 03 — System Calls and strace

**Goal:** talk to the operating system directly — files, processes, pipes, and signals — handle errors properly, and watch any program's system calls with `strace`.

**Time:** about 8 hours, in three sessions.

---

## Session 1 — Files and file descriptors (3 hours)

A **system call** asks the kernel to do something a program can't do alone (Module 08 shows the inside). `stdio` (`fopen`, `printf`) is a library *on top of* system calls; here you use the calls themselves.

```c
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>

int fd = open("out.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
if (fd < 0) { fprintf(stderr, "open: %s\n", strerror(errno)); return 1; }
const char *msg = "hello\n";
ssize_t n = write(fd, msg, strlen(msg));   // may write FEWER bytes than asked!
close(fd);
```

- A **file descriptor** is a small integer naming an open file in your process (0, 1, 2 are stdin, stdout, stderr — Burrow Jr.).
- Every call can fail: check the return value, and read **`errno`** for the reason (`strerror(errno)` or `perror("open")`).
- `read` and `write` may transfer **fewer bytes than requested** (a "short" read or write). Robust code loops:

```c
ssize_t write_all(int fd, const void *buf, size_t len) {
    const char *p = buf;
    while (len > 0) {
        ssize_t n = write(fd, p, len);
        if (n < 0) { if (errno == EINTR) continue; return -1; }
        p += n; len -= (size_t)n;
    }
    return 0;
}
```

**Exercises:** (1) a `cp` clone with `open`/`read`/`write` and a 64 KiB buffer, handling every error with a clear message; (2) `lseek` to read the last 100 bytes of a file (a `tail -c` clone); (3) **durability:** write a file, then `fsync(fd)` before `close`. Time 1,000 small writes with and without `fsync` after each. [W] Why is the difference so big? (Hint: Magnitudes Field Guide: disk vs memory.)

**Atomic replace:** write to `file.tmp`, `fsync`, then `rename("file.tmp", "file")`. On Linux, `rename` within one file system replaces the target atomically: readers see the old file or the new one, never half of each. You've used this rule since the Spelling Engine; now you know which system calls make it true.

---

## Session 2 — strace (2 hours)

`strace` shows every system call a program makes, with arguments and results.

```bash
strace -f -o trace.txt ls /tmp
less trace.txt
strace -c ls /tmp          # a summary table: calls, counts, time
strace -e trace=openat,read,write cat /etc/hostname
```

**Explorations [W]:** for each, write what you see and one question it raises:
1. `strace -c python3 -c "print(1)"` — how many system calls does starting Python take? Which ones dominate?
2. Your Lab 01 `cp` clone vs `cp` vs `cat a > b` — compare the read/write sizes.
3. `strace -f` on your Burrow Jr. running `ls | wc -l` — find `clone`/`fork`, `execve`, `pipe2`, `dup2`, `wait4`. You'll recognise every one.
4. A program that prints 1,000 lines with `printf`, run with output to the terminal vs to a file. Why does the number of `write` calls change? (stdio buffering: line-buffered for terminals, fully buffered for files.)

---

## Session 3 — Processes, pipes, signals in C (3 hours)

Re-do Burrow Jr.'s core in C (this is the warm-up for Burrow):

```c
pid_t pid = fork();
if (pid < 0) { perror("fork"); exit(1); }
if (pid == 0) {
    execvp(argv[0], argv);
    perror("execvp");          // only reached if exec failed
    _exit(127);
}
int status;
if (waitpid(pid, &status, 0) < 0) perror("waitpid");
if (WIFEXITED(status))   printf("exit %d\n", WEXITSTATUS(status));
if (WIFSIGNALED(status)) printf("killed by signal %d\n", WTERMSIG(status));
```

**Exercises:**
1. A two-stage pipeline `cmd1 | cmd2` with `pipe` and `dup2`, closing every unused end (remember the Burrow Jr. hang).
2. **Signals:** install a handler for `SIGINT` with `sigaction` (not `signal`) that sets a `volatile sig_atomic_t` flag; the main loop checks the flag. [W] Why only set a flag? (Most functions, including `printf` and `malloc`, are **not async-signal-safe**: a handler that calls them can corrupt the program if the signal arrives in the middle of the same function. `man 7 signal-safety` lists the safe ones.)
3. **SIGCHLD:** start three background children that sleep for different times; reap each as it finishes using a SIGCHLD handler plus `waitpid(-1, &status, WNOHANG)` in a loop. Print which child finished when. (This is the heart of Burrow's job control.)

---

## Done when

- [ ] `cp` clone with full error handling and `write_all`; the fsync timing measured.
- [ ] Four strace explorations written up.
- [ ] Pipeline, SIGINT flag, and SIGCHLD reaping working, valgrind-clean.

## Retrieval and reflection

1. **[R]:** open flags; short reads/writes and the loop; errno; the atomic-replace recipe; fork/exec/wait in C; why signal handlers should only set flags.
2. **[F] (spoken, 2 min):** "What is a system call, and how is it different from a library function?"
