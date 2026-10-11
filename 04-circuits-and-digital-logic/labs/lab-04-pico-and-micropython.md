---
title: "Lab 04 — Pico and MicroPython"
id: "MOD04-LAB04"
type: "lab"
module: "04-circuits-and-digital-logic"
phase: "B"
order: 620
prerequisites: [MOD04-LAB03]
kind: "maker"
---

# Lab 04 — Pico and MicroPython

**Goal:** program a real microcontroller: blink and read pins, debounce a button in software, read an analog value, make sound with PWM (your Tone Loom songs on a buzzer), and stream measurements to your computer.

**Sessions:** four. Start in the **Wokwi** simulator (wokwi.com/pi-pico) if your board hasn't arrived.

---

## Session 1 — Setup and blink

### What a microcontroller is

The **Raspberry Pi Pico** is a tiny computer on one chip (the RP2040): two processor cores, 264 KB of RAM, 2 MB of flash storage, and 26 general-purpose input/output (**GPIO**) pins. No operating system — your program is the only thing running. (Compare with your Linux machine, where the OS runs hundreds of programs at once — Module 08.)

### Install MicroPython

1. Download the MicroPython **UF2** file for the Pico from micropython.org.
2. Hold the **BOOTSEL** button while plugging the Pico in. It appears as a USB drive.
3. Copy the UF2 file onto it. The Pico reboots running MicroPython.
4. Install `mpremote` on your computer (`pip install mpremote`, or your package manager). Run `mpremote` — you get a `>>>` REPL running **on the Pico**.

(Thonny is an alternative editor with Pico support built in, if you prefer a GUI.)

### Blink

```python
from machine import Pin
import time

led = Pin("LED", Pin.OUT)      # the on-board LED ("LED" works on Pico and Pico W)
while True:
    led.toggle()
    time.sleep(0.5)
```

Run a file with `mpremote run blink.py`. Save it as `main.py` on the Pico (`mpremote cp blink.py :main.py`) to run automatically at power-up.

**External LED:** GPIO 15 → 330 Ω → LED → GND. **The Pico runs at 3.3 V, not 5 V.** Recompute the LED resistor from Lab 01 for 3.3 V (≈ 130 Ω for 10 mA with a 2.0 V red LED; 150 Ω is fine). **Never connect 5 V to a GPIO pin.** GPIO pins can supply only a small current (keep under ~10 mA per pin); for anything bigger you'll use a transistor (Pico Thermostat).

**[W]:** your Python on the PC and MicroPython on the Pico look the same. What's different underneath? (Memory size, no OS, direct pin access, speed.)

---

## Session 2 — Inputs and software debouncing

### Reading a button

```python
button = Pin(14, Pin.IN, Pin.PULL_DOWN)   # internal pull-down: no external resistor needed
print(button.value())                       # 0 or 1
```

Wire the button between GPIO 14 and **3V3** (pin 36).

### See the bounce in software

Count rising edges in a tight loop for 10 seconds while you press the button 10 times. The count is usually more than 10 (Lab 03's bounce, now in code).

### Debounce it

**Subgoal labels [S]:**
```python
# 1. Read the raw pin every millisecond
# 2. If the reading differs from the current stable state, start (or keep) a timer
# 3. If the new reading has stayed the same for 20 ms, accept it as the new stable state
# 4. A "press" is a stable change from 0 to 1
```

This is a tiny **state machine** (a preview of the Crosswalk project). Test it: 20 presses → exactly 20 counts.

**[W]:** why 20 ms? Measure: what's the longest bounce you saw in Lab 03? What happens if you choose 2 ms? 200 ms?

### Interrupts (a look)

Instead of checking the button constantly (**polling**), you can ask the hardware to run a function when the pin changes (an **interrupt**):

```python
def pressed(pin):
    print("edge!")
button.irq(trigger=Pin.IRQ_RISING, handler=pressed)
```

Bounces trigger it repeatedly too. Interrupts come back in a big way in Module 08 (your kernel's timer interrupt) and in your [Explain-a-System](../../00-foundations/english/projects/explain-a-system/spec.md) key-press explainer.

---

## Session 3 — Analog in, PWM out

### Analog input (ADC)

An **ADC** (analog-to-digital converter) turns a voltage into a number. The Pico's ADC reports 0–65,535 for 0–3.3 V (`read_u16()`).

1. Wire your 10 kΩ potentiometer as a divider (Lab 01) between 3V3 and GND, middle to **GP26 (ADC0)**. Print `ADC(26).read_u16() * 3.3 / 65535` as you turn it. Compare with your multimeter.
2. **Internal temperature sensor:** `ADC(4)`. From the RP2040 datasheet:
   ```python
   v = ADC(4).read_u16() * 3.3 / 65535
   temp_c = 27 - (v - 0.706) / 0.001721
   ```
   Print it once a second. Breathe on the chip. (It's the chip's own temperature — a little above room temperature.)

**[W]:** the ADC turns a smooth voltage into steps. How big is one step, in volts? (M06: 3.3 ÷ 65,536 … but the RP2040's ADC really has 12 bits, scaled up to 16. Look it up: what's the *real* step size?)

### PWM: fake analog out, and sound

**PWM** (pulse-width modulation) switches a pin on and off very fast. The fraction of time it's on (the **duty cycle**) controls the average power: an LED at 25% duty looks dimmer.

```python
from machine import PWM
pwm = PWM(Pin(15))
pwm.freq(1000)
pwm.duty_u16(16384)     # about 25%
```

Fade an LED smoothly up and down.

**Play your songs:** connect a passive piezo buzzer between a GPIO pin and GND. Set `pwm.freq(f)` to a note's frequency (Tone Loom's `440 × 2^((n − 69)/12)`) with 50% duty, for each note's duration. Port a simplified Tone Loom song player to the Pico. (Square waves only — and now you know why they sound buzzy.)

---

## Session 4 — Logging to your computer

The Pico's `print()` output travels over USB as a **serial** stream. Your computer can read it as a file-like device.

1. On the Pico: every second, print one CSV line: `millis,temp_c,pot_volts`.
2. On your computer: read it with `mpremote` and redirect to a file, or write a small Python script with `pyserial` that reads lines from `/dev/ttyACM0` (Linux; on macOS `/dev/tty.usbmodem…`) and appends them to a CSV.
3. Log for 10 minutes while you warm the chip with your finger, then let it cool. Plot temperature against time. Does the cooling look like Lab 02's exponential?

**Done when:** you have a 10-minute CSV and a plot.

---

## Done when

- [ ] Blink, button with software debounce (20 presses → 20), ADC readings matching the meter, PWM fade, and a song on the buzzer.
- [ ] A logged and plotted temperature run.

## Retrieval and reflection

1. **[R]:** setting a pin as output/input with pull-down; the debounce state machine's steps; ADC scaling; the internal temperature formula; what PWM duty means; 3.3 V and current limits.
2. **[F] (spoken):** "What is PWM, and how can a digital pin dim an LED?"
3. **[W]:** polling vs interrupts — when would each be better?

**Next:** the projects — [Gatesmith](../projects/gatesmith/spec.md) (if not started), then [Crosswalk Controller](../projects/crosswalk-controller/spec.md) and [Pico Thermostat](../projects/pico-thermostat/spec.md).
