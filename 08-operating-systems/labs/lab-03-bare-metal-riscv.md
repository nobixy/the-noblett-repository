---
title: "Lab 03 — Bare-Metal RISC-V"
module: "08-operating-systems"
hours: 10
---

# Lab 03 — Bare-Metal RISC-V

**Goal:** run code with **no operating system at all** on an emulated 64-bit RISC-V machine: cross-compile, write a linker script, boot through OpenSBI, print to the UART, and step through it with GDB. This is the launch pad for Seedling.

**Time:** about 10 hours, in three sessions.

---

## Session 1 — The toolchain and the machine (3 hours)

### Install

On Arch: `sudo pacman -S riscv64-elf-gcc riscv64-elf-binutils riscv64-elf-gdb qemu-system-riscv`. (Elsewhere, look for `gcc-riscv64-unknown-elf` or a `riscv64-linux-gnu` cross-compiler, and `qemu-system-misc`.) Check: `riscv64-elf-gcc --version`, `qemu-system-riscv64 --version`.

A **cross-compiler** runs on your x86-64 machine but produces RISC-V machine code.

### The machine: QEMU `virt`

QEMU's `virt` board is a simple, well-documented virtual machine:
- RAM starts at physical address **0x8000_0000** (128 MiB by default; `-m` changes it).
- An **NS16550A UART** (serial port) at **0x1000_0000**.
- **OpenSBI**, a small firmware, runs first in the most privileged mode (**M-mode**), sets up the machine, then jumps to your kernel at **0x8020_0000** in **supervisor mode (S-mode)**, with the hart (CPU core) ID in register `a0` and a pointer to the device tree in `a1`.

```bash
qemu-system-riscv64 -machine virt -nographic -bios default
```

With no kernel, you'll see the OpenSBI banner. Exit QEMU with **Ctrl+A then X**.

### Read the spec, briefly

Skim the **RISC-V Instruction Set Manual, Volume I** chapter "RV32I Base Integer Instruction Set" (registers `x0`–`x31`, `x0` always zero — like Kestrel's r0!) and the ABI register names (`ra`, `sp`, `a0`–`a7`, `t0`–`t6`, `s0`–`s11`). Make flashcards [I].

---

## Session 2 — Hello from nothing (4 hours)

### The entry point (assembly)

```asm
# entry.S — the first instructions your kernel runs
    .section .text.entry
    .globl _start
_start:
    la   sp, stack_top        # set up a stack (C needs one)
    call kmain                # jump to C
1:  wfi                       # if kmain returns, sleep forever
    j    1b

    .section .bss
    .align 12
stack:
    .space 4096 * 4
stack_top:
```

### The linker script

A **linker script** tells the linker where each section goes in memory:

```ld
/* kernel.ld */
OUTPUT_ARCH(riscv)
ENTRY(_start)
SECTIONS {
    . = 0x80200000;
    .text : { *(.text.entry) *(.text .text.*) }
    .rodata : { *(.rodata .rodata.*) }
    .data : { *(.data .data.*) }
    .bss : { __bss_start = .; *(.bss .bss.*) *(COMMON) __bss_end = .; }
    __kernel_end = .;
}
```

[W] Why must `.text.entry` come first? Why does C code need `.bss` zeroed before it runs, and who would normally zero it?

### The UART, in C

```c
// kmain.c
#include <stdint.h>
#define UART 0x10000000UL
static volatile uint8_t *const uart = (volatile uint8_t *)UART;

static void putc(char c) {
    while ((uart[5] & 0x20) == 0) { }   // LSR (offset 5), bit 5: transmit holding register empty
    uart[0] = (uint8_t)c;               // THR (offset 0)
}
static void puts(const char *s) { while (*s) putc(*s++); }

void kmain(void) {
    puts("Hello from Seedling's seed\n");
}
```

- **`volatile`** tells the compiler every read and write really matters (it's a device, not normal memory — don't optimise them away or reorder them).
- This is **memory-mapped I/O**: exactly Kestrel's TTY_OUT, but on a real architecture.

### Build and run

```bash
riscv64-elf-gcc -march=rv64gc -mabi=lp64d -mcmodel=medany -ffreestanding -nostdlib \
    -O1 -g -Wall -Wextra -T kernel.ld entry.S kmain.c -o kernel.elf
qemu-system-riscv64 -machine virt -nographic -bios default -kernel kernel.elf
```

- `-ffreestanding -nostdlib`: there is no C library here. No `printf`, no `malloc` — until you write them.
- `-mcmodel=medany`: lets code run at a high address like 0x80200000.

You should see the OpenSBI banner, then your message. **You just ran code on a machine with no operating system.**

Put the commands in a `Makefile` with `make run`.

---

## Session 3 — GDB on bare metal (3 hours)

Start QEMU paused, waiting for a debugger:

```bash
qemu-system-riscv64 -machine virt -nographic -bios default -kernel kernel.elf -s -S
# in another terminal:
riscv64-elf-gdb kernel.elf -ex "target remote :1234"
(gdb) break kmain
(gdb) continue
(gdb) info registers a0 a1 sp pc
(gdb) stepi
(gdb) x/4i $pc          # disassemble the next 4 instructions
```

**Exercises:**
1. Break at `_start`: what are `a0` and `a1`? (Hart ID and device tree address.)
2. Step through `putc` and watch the loop polling the UART status.
3. **Read input:** extend the UART code with `getc` (wait for LSR bit 0 = data ready, then read RBR at offset 0). Make an echo loop: every key you type is printed back, uppercased.
4. **A minimal `kprintf`:** support `%s`, `%d`, `%x`, `%p`, `%c`, `%%` using `<stdarg.h>` (it's provided by the compiler even with `-ffreestanding`). Print `a0`, `a1`, and the addresses of `__bss_start` and `__kernel_end`.
5. **Zero the BSS** in `entry.S` (or at the start of `kmain`) and prove it matters: put a global `int x;` and print it before and after you add the zeroing (QEMU's RAM is often zero anyway — so also deliberately write junk to it from GDB first).

---

## Done when

- [ ] The kernel prints, echoes typed characters in uppercase, and `kprintf` works.
- [ ] You can start, break, step, and inspect registers in GDB.
- [ ] `make run` and `make debug` targets exist.

## Retrieval and reflection

1. **[R]:** the `virt` memory map (RAM base, UART, kernel load address); what OpenSBI does; what the linker script and `entry.S` each do; the UART polling loop.
2. **[F] (spoken, 2 min):** "What happens between pressing Enter on the QEMU command and seeing your message?"
3. **[W]:** compare with Kestrel: where does each keep its I/O devices, and how does each start running a program?

**Next:** [Seedling Kernel](../projects/seedling-kernel/spec.md).
