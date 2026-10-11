---
title: "Project: Seedling Kernel"
id: "MOD08-PRJ-seedling-kernel"
type: "project"
module: "08-operating-systems"
phase: "D"
order: 1140
prerequisites: [MOD08-LAB03, MOD07-PRJ-heapsmith, MOD07-PRJ-burrow, MOD06-PRJ-kestrel-isa]
artifact: "Seedling: a small RISC-V (RV64) kernel for QEMU virt — console, trap handling, timer interrupts, a flight recorder, physical page allocator and kernel heap, kernel threads with preemptive scheduling, Sv39 virtual memory, user mode with system calls, a ramdisk file system (SeedFS), user programs and a tiny shell, and an automated test runner"
deliverable: "Design doc (grown milestone by milestone) + SEEDFS.md + syscall reference + automated test report + recorded kernel walkthrough"
---

# Project: Seedling Kernel

| | |
| :-- | :-- |
| **Module** | 08 Operating Systems |
| **Prerequisites** | Labs 01–03 of this module; Heapsmith; Burrow; Kestrel ISA (the ideas of traps and privilege) |
| **You build** | **Seedling**, an operating-system kernel for 64-bit RISC-V, running on QEMU's `virt` machine. It grows in eight milestones, and boots at every step: it prints, handles exceptions and timer interrupts, records its own recent history, allocates memory, runs several threads with preemptive scheduling, gives each program its own address space, runs programs in user mode with system calls, reads files from a ramdisk, and finally runs **Sprout**, a tiny shell that launches programs |
| **Deliverable** | A growing design doc, a file-system spec, a syscall reference, a test report, and a recorded walkthrough |

---

## Why this matters

An operating system is the most important program on every computer, and it's usually invisible. Writing one, even a small one, answers questions you've carried since Module 01: How does `fork` really create a process? What happens on a key press? How can two programs use the same address? How does the computer switch between programs dozens of times a second? Why does one bad pointer crash a program but not the whole machine?

And RISC-V is a real, open architecture used in real chips. The skills transfer directly to embedded systems, to Linux kernel work, and to understanding every system above the kernel.

**Real-world analogs:** Linux, the BSDs, xv6, seL4, Zephyr and other embedded kernels.

> **Originality and independence:** Seedling is designed for this curriculum and built from scratch. It is not a port of xv6 or of any course's kernel labs, and it uses no starter code. When stuck, you may read the **RISC-V privileged specification**, the **OpenSBI/SBI specification**, and QEMU's documentation — the same primary sources any kernel developer uses. Reading other teaching kernels' code is a last resort for a specific question, after a stuck note and a night's sleep; never copy it.

---

## Ground rules

- **Language:** C (C17, freestanding) plus small assembly files. Toolchain and QEMU from Lab 03.
- **Single core** (hart 0). Other harts, if started by OpenSBI, should park in a `wfi` loop. (Multicore is a stretch goal.)
- **Every milestone ends with a kernel that boots** and passes the automated tests so far.
- **Commit after every working step.** Kernels break in ways that make `git bisect` (Module 02 Lab 02) your best friend.
- **The design doc grows** with each milestone: add a section describing what you built, a diagram, and the decisions you made with their alternatives [W].

---

## Milestones

### Milestone 1 — Boot, console, panic

Start from Lab 03's kernel.
1. Clean layout: `kernel/` (C and assembly), `user/` (later), `tools/` (host-side scripts), `Makefile`.
2. **Console:** UART `putc`/`getc` and `kprintf` (Lab 03).
3. **`panic(fmt, …)`:** print `PANIC: message` with the file and line (a macro using `__FILE__` and `__LINE__`), then halt in a `wfi` loop.
4. **Clean shutdown:** use the SBI **System Reset** extension (`sbi_system_reset`) so the kernel can power off QEMU (needed for automated tests). Write a tiny `sbi_call(ext, fid, a0, a1, a2)` helper in C with inline assembly (`ecall` from S-mode goes to OpenSBI) — read the SBI spec's calling convention first.
5. **Automated test runner (host side):** a script that runs QEMU with a timeout, captures serial output, checks for expected lines, and fails if `PANIC` appears or QEMU doesn't shut down. Every later milestone adds tests here.

**Done when:** `make test` boots, prints, shuts QEMU down, and passes.

### Milestone 2 — Traps, the timer, and the flight recorder

1. **Trap entry (assembly):** set `stvec` to your handler. On a trap, save **all 31 general registers** plus `sepc`, `sstatus`, `scause`, `stval` into a **trap frame** on the kernel stack; call `trap_handler(struct trapframe *tf)` in C; restore everything; `sret`. Write the subgoals first [S]; draw the trap frame layout [R].
2. **Exceptions:** decode `scause` and print a useful report for illegal instructions, misaligned accesses, and page faults (with `sepc` and `stval`), then panic. Test each deliberately (e.g. execute `.word 0`; read from address 0 once paging is on).
3. **Timer interrupts:** read the time with the `time` CSR (`rdtime`); program the next timer interrupt with the SBI **TIME** extension (`sbi_set_timer`); enable supervisor timer interrupts (`sie.STIE`) and interrupts globally (`sstatus.SIE`). On each timer interrupt, increment a `ticks` counter and set the next deadline (e.g. every 10 ms; QEMU `virt`'s timer runs at 10 MHz — verify this from the device tree or the docs).
4. **The flight recorder** — an original Seedling feature: a ring buffer (Module 05!) of the last 256 kernel events (trap type and cause, `sepc`, time, current thread later), cheap enough to record always. `panic` dumps it. [W] Why is a cheap, always-on trace worth more than a detailed one you have to switch on?

**Done when:** the kernel prints "tick" every second for 5 seconds; deliberate exceptions produce clear reports with a flight-recorder dump; tests cover both.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *what happens between a timer firing and your C handler running — and how the interrupted code continues as if nothing happened*.

### Milestone 3 — Physical memory and the kernel heap

1. **Physical page allocator:** manage all 4 KiB pages from `__kernel_end` (rounded up) to the end of RAM (128 MiB unless you pass `-m`; parse the device tree for the real size as a stretch). A free list threaded through the free pages themselves (Heapsmith's trick) is simple: `page_alloc()` and `page_free(p)`. Fill freed pages with a junk pattern (catches use-after-free).
2. **Kernel heap:** `kmalloc`/`kfree` on top of the page allocator — port a small version of Heapsmith (size classes for small objects; whole pages for large ones).
3. **Tests (in-kernel):** allocate and free every page, check the count is restored; random `kmalloc`/`kfree` sequences with payload checks (Heapsmith's driver idea, inside the kernel).

**Done when:** in-kernel memory tests pass under the automated runner.

### Milestone 4 — Kernel threads and preemptive scheduling

1. **Thread structure:** id, state (RUNNABLE, RUNNING, SLEEPING, ZOMBIE — an FSM [S]), its own kernel stack (one page), saved **context** (the callee-saved registers `s0`–`s11`, `ra`, `sp` — the calling convention tells you why only these [W]).
2. **Context switch** in assembly: `switch(old_ctx, new_ctx)` saves the current callee-saved registers into `old`, loads `new`'s, and returns — *into the other thread*. Draw two stacks and walk through a switch [R].
3. **Cooperative first:** `thread_create(fn, arg)`, `yield()`, a round-robin run queue (a queue from Module 05). Three threads printing A, B, C in turn.
4. **Preemptive:** on the timer interrupt, if the current thread has used its time slice, call the scheduler. Now threads that never yield still share the CPU.
5. **Locking inside the kernel:** a **spinlock** that also disables interrupts while held (`sstatus.SIE`), so an interrupt handler can't deadlock waiting for a lock its own CPU already holds (Lab 01's question answered). Use it for the run queue and the allocators.
6. **`sleep(ticks)`** and a sleeping list woken by the timer.
7. **Deterministic test mode:** a build option where time slices are counted in instructions or fixed tick counts, so a test of three busy threads gives the same interleaving every run — scheduler bugs become reproducible.

**Done when:** three busy threads interleave fairly with no yields; sleeping threads wake on time; tests pass in deterministic mode.

**Checkpoint:** Milestone Checkpoint. Feynman target: *how a context switch "returns" into a different thread*. Why-ladder target: *why must the spinlock disable interrupts?*

### Milestone 5 — Virtual memory (Sv39)

1. **Sv39:** 39-bit virtual addresses, three levels of page tables, each a 4 KiB page of 512 eight-byte entries (PTEs). Each PTE has a physical page number and flags: V (valid), R, W, X, U (user-accessible), G, A, D. Read the privileged spec's Sv39 section; then draw the translation of one address through all three levels by hand [S] [R].
2. **`map(pagetable, va, pa, size, flags)`** and **`walk(pagetable, va, create)`** — allocate intermediate tables as needed.
3. **The kernel's own mapping:** map the kernel's code (R+X), read-only data (R), data and BSS (R+W), all remaining RAM (R+W) — all at their physical addresses ("identity mapping") — and the UART. Then write `satp` (mode 8 = Sv39, plus the root table's page number) and `sfence.vma`. If anything is wrong, the next instruction faults — your Milestone 2 reports will tell you where.
4. **Guard pages:** leave an unmapped page below each kernel thread's stack. A stack overflow now faults cleanly instead of silently corrupting memory. Prove it with a deliberately deep recursion.
5. **Per-process address spaces:** a function that creates a new page table containing the kernel mappings (without the U flag) plus a user region (with U) — ready for Milestone 6.

**Done when:** the kernel runs with paging on, W^X holds (no page is both writable and executable — check by walking your tables), and the guard-page test faults as expected.

### Milestone 6 — User mode and system calls

1. **User programs:** written in C, compiled separately for RISC-V with their own linker script (load address e.g. 0x1000 in their own address space), a tiny `crt0.S` (sets up and calls `main`, then calls `exit`), and syscall stubs.
2. **Loading:** for now, embed user program binaries in the kernel image (`.incbin` in an assembly file) — or load them with QEMU's `-device loader,file=…,addr=…`. Copy each into fresh pages mapped at its load address with U+R+X (code) and U+R+W (data, stack).
3. **Entering user mode:** set `sepc` to the entry point, clear `sstatus.SPP` (return to user mode), set the user stack pointer, switch `satp` to the process's page table, and `sret`.
4. **System calls:** user code executes `ecall` with the syscall number in `a7` and arguments in `a0`–`a5`; the trap handler sees `scause = 8` (environment call from U-mode), dispatches, puts the result in `a0`, and advances `sepc` past the `ecall` (by 4 — [W] why?).
5. **Your syscall table** (document every one in `SYSCALLS.md`: number, arguments, return value, errors): `write(fd, buf, len)`, `read(fd, buf, len)` for the console, `exit(status)`, `getpid()`, `yield()`, `sleep(ms)`, `spawn(name)` (start a new process from an embedded program), `wait(&status)`.
6. **Validate every user pointer:** a syscall must never trust a user address. Check that the whole buffer is mapped with U permission in the caller's page table, and copy data in and out with `copyin`/`copyout` helpers. Write a user test program that passes kernel addresses, NULL, and unmapped addresses to every syscall — the kernel must return errors, never crash. (Crate's fuzzing lesson, at the kernel boundary.)
7. **Processes** are threads plus an address space plus a parent; `exit` makes a zombie until the parent `wait`s (Burrow's view, now from the inside).

**Done when:** two user programs run at once, printing; a user program that dereferences NULL is killed with a report while the kernel keeps running; the hostile-pointer test passes.

**Checkpoint:** Milestone Checkpoint. Feynman target: *why a user program can't read the kernel's memory, even though it's mapped in the same page table* (the U bit). Retrieval target: the full path of a `write` syscall from user code to the UART and back.

### Milestone 7 — SeedFS: a ramdisk file system

1. **Design `SeedFS`** and write `SEEDFS.md` (E10 spec, like Crate's): a superblock (magic, version, sizes), an inode table (type, size, block pointers — direct only, or one indirect block), a data region, and directories as files of (name, inode number) entries. Fixed 4 KiB blocks.
2. **`mkseedfs`** (a host tool, in Python or C): builds an image from a folder on your Linux machine (your user programs, a `README`, some text files).
3. **Load** the image into RAM with QEMU's loader device (`-device loader,file=seedfs.img,addr=0x84000000` — pick an address beyond your kernel and tell the page allocator not to use it).
4. **Kernel FS layer:** path lookup (`/bin/cat` → walk directories), a per-process **file descriptor table**, and syscalls `open(path)`, `read(fd, …)`, `close(fd)`, `readdir(fd, …)`. `spawn(path)` now loads programs from SeedFS (parse a flat binary, or — stretch — a minimal ELF loader).
5. **User programs:** `ls`, `cat`, `echo`, `uptime` (ticks), `hello`.

**Done when:** `cat /README` works from a user program, and `ls /bin` lists your programs.

### Milestone 8 — Sprout, and the final test suite

1. **Sprout:** a user-mode shell (Burrow Jr.'s level): prompt, read a line, `spawn` the program from `/bin`, `wait`, print its status. Built-ins: `exit`, `ps` (a syscall listing processes with their states and ticks used — your scheduler's view).
2. **Init:** the kernel's first user process is Sprout.
3. **Final automated tests:** the host runner feeds Sprout commands through QEMU's serial input and checks outputs: running each program, a program that crashes (kernel survives), a CPU-hungry program running alongside an interactive one (Sprout stays responsive — preemption works), and `exit` shutting the machine down cleanly.
4. **Measurements:** context switch time (`rdtime` before and after many switches), syscall round-trip time (a user loop of `getpid`), and process spawn time. Compare with Linux numbers you can measure on your machine (a `getpid` loop in C). Record them in the design doc — and add them to your [Magnitudes Field Guide](../../../00-foundations/math/projects/magnitudes-field-guide/spec.md).

**Done when:** the full suite passes from a clean build with one command.

---

## Debugging guidance (read before you start)

- **QEMU's `-d int,guest_errors -D qemu.log`** logs every trap QEMU sees — invaluable when your own trap handler is the thing that's broken.
- **`info registers` and `info mem`** in the QEMU monitor (start with `-monitor stdio` instead of `-nographic` while debugging) show CSRs and page mappings.
- **GDB** with `-s -S` (Lab 03): break on `trap_handler`, `panic`, or any address; `x/10i $pc`; `p/x $scause`.
- **The flight recorder** tells you what happened just before a panic.
- **One change at a time**, test, commit. When it breaks, `git bisect`.
- **Triple-check bit positions** in CSRs and PTEs against the spec. Most "impossible" kernel bugs are one wrong bit.

## Common pitfalls

- **Trap entry clobbering a register before saving it** — use `sscratch` to get a safe kernel stack pointer when trapping from user mode.
- **Forgetting `sfence.vma`** after changing page tables.
- **Missing the A and D bits:** some implementations fault if they're not set; setting them up front avoids a confusing fault.
- **Stack too small** for a kernel thread that calls `kprintf` with big buffers.
- **Interrupts enabled while holding a lock** → deadlock in the timer handler.
- **Returning to `sepc` instead of `sepc + 4`** after a syscall → the same `ecall` runs forever.

## Communication deliverable

1. **Design doc** — grows one section per milestone (with diagrams: trap frame, thread states, context switch, page-table walk, address-space layout, SeedFS layout) and a final "What I would do next" section.
2. **`SEEDFS.md`** and **`SYSCALLS.md`** — reference documents.
3. **Test report** — what the automated suite covers, and three bug stories (symptom, how you found it, cause, fix).
4. **Kernel walkthrough (short, recorded):** boot to Sprout, then a source tour following one syscall and one timer interrupt.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before each milestone: draw the relevant structure (trap frame, context, page table walk, inode) from memory |
| **F** | Trap entry; context switch; U-bit protection; one syscall end to end |
| **W** | A design-doc decision per milestone: cheap recorder; callee-saved context; spinlocks disabling interrupts; sepc + 4; user pointers; direct vs indirect blocks |
| **S** | Subgoals for trap entry/exit, switch, walk, syscall dispatch, path lookup |
| **D** | Kernel bugs: QEMU logs, GDB, the recorder, a stuck note — and never more than three honest attempts before a break |
| **I** | Each milestone mixes hardware detail, data structures, and testing |
| **T** | Growing design doc, references, test report, walkthrough |

## Stretch goals

- **Multicore:** start the other harts with the SBI HSM extension; per-CPU run queues; proper locking.
- **virtio-blk driver:** a real disk device on QEMU instead of the ramdisk; then a writable SeedFS with a journal (Tagfs's design, in your kernel).
- **ELF loader** for user programs.
- **Copy-on-write `fork`:** implement `fork` with COW (Lab 02, from the inside).
- **Real hardware:** run Seedling on an inexpensive RISC-V board (several exist with OpenSBI support). Expect to learn about device trees and real UARTs.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Boot, traps, timer | Full trap frame; clear exception reports; flight recorder | Works | Fragile |
| Memory | Page allocator + kernel heap with in-kernel tests | Works | Leaks or corruption |
| Threads and scheduling | Preemptive, spinlocks with interrupt masking, sleep, deterministic mode | Cooperative only | Missing |
| Virtual memory | Sv39, W^X, guard pages, per-process spaces | Kernel mapping only | Missing |
| User mode and syscalls | Isolation, validated pointers, hostile tests pass, processes and wait | Basic | Missing |
| File system and shell | SeedFS spec + tool + syscalls; Sprout runs programs | Partial | Missing |
| Testing | One-command automated suite, measurements | Manual tests | None |
| Communication | Doc, references, test report, walkthrough | Most | Few |

**Done when:** every area at least 2; Testing and User mode at 3.

## Connections

- **Back:** Lab 03 (bare metal), Kestrel (traps, privilege ideas), Heapsmith (heaps), Burrow (processes from outside), Crate (on-disk formats), Module 05 (queues, ring buffers), Crosswalk (state machines).
- **Forward:** Module 09 (a network stack is the next big kernel subsystem — Seedling could grow one), Module 11 (crash-consistent storage), Module 13 (the "down to the metal" capstone option).
