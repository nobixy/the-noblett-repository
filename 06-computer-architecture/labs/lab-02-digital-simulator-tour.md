---
title: "Lab 02 — A Tour of the Digital Simulator"
module: "06-computer-architecture"
hours: 6
---

# Lab 02 — A Tour of the Digital Simulator

**Goal:** become fluent in **Digital**, the graphical logic simulator recommended for the Kestrel datapath: components, buses, subcircuits, memories loaded from files, test cases, and a terminal.

**Time:** about 6 hours, in two sessions.

**Install:** Digital is a free Java program by H. Neemann (github.com/hneemann/Digital). On Arch it's in the AUR (`digital`); elsewhere, download the release ZIP and run `Digital.jar` with Java 11+ (`sudo pacman -S jre-openjdk`). If you choose Logisim Evolution instead, the same exercises apply with different menus.

---

## Session 1 — Components, buses, subcircuits (3 hours)

Build each, test it, and save it in `~/workbench/06-datapath/digital/`.

1. **Half adder** from an XOR and an AND, with two inputs and two outputs (LEDs). Click the inputs to test all four rows.
2. **Buses and splitters:** a 4-bit input, split into bits, recombined in reverse order. Digital's **Splitter** component converts between a bus and its bits. (Bit order again: decide, and check the splitter's labels.)
3. **A subcircuit:** save the half adder as its own file; build a full adder by placing two half adders (as subcircuits) and an OR. **Hierarchy**, exactly as in Gatesmith.
4. **Test cases:** Digital's **Test** component holds a truth table that it checks automatically. Write one for the full adder (all 8 rows) and run it (*Run all tests*). This is how you'll test every datapath block.
5. **A register with enable:** use Digital's **Register** component (or build from D flip-flops) with a clock, data in, enable, and data out. Clock it with the **Clock** component and step it manually.

**[W]:** in Gatesmith you wrote text; here you draw. List two advantages of each for building a CPU.

---

## Session 2 — Memories and I/O (3 hours)

1. **ROM loaded from a hex file:** Digital's ROM component can load its contents from a file (in the component's properties). Find which file formats it accepts (it supports simple hex formats); write a tiny converter from your Kestrel `.khex` format if needed. Load 8 words and display the output of each address on a hex display while stepping an address counter.
2. **RAM:** a RAM component with address, data in, data out, write-enable, and clock. Write a value, read it back.
3. **Terminal:** Digital has a **Terminal** component that prints a character when its clock input rises with data present. Wire: an 8-bit constant (`'H'` = 0x48) → terminal, and a button as the clock. Print "HI".
4. **Mini machine:** combine a counter (as a program counter), a ROM, and the terminal so that the ROM's contents (a string) print one character per clock tick. This is a tiny "computer" with only one instruction: *print the next byte*.
5. **Export:** look at *File → Export → Verilog*. Export your full adder and read the Verilog it produces. You won't use it now, but it's the path to an FPGA (the datapath's stretch goal).

---

## Done when

- [ ] Five Session 1 circuits built, with passing test cases.
- [ ] ROM-from-file, RAM, terminal, and the mini machine working.
- [ ] You've seen your circuit as Verilog.

## Retrieval and reflection

1. **[R]:** how to make a subcircuit, a test case, a ROM from a file, and a terminal output in Digital.
2. **[W]:** what's the difference between your mini machine and Nib? (What would it take to add a second instruction?)

**Next:** [Kestrel Datapath](../projects/kestrel-datapath/spec.md).
