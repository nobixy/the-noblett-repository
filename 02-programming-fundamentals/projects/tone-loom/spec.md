---
title: "Project: Tone Loom"
id: "MOD02-PRJ-tone-loom"
type: "project"
module: "02-programming-fundamentals"
phase: "B"
order: 470
prerequisites: [MOD02-LAB03, M07, FND-MA-PRJ-base-workshop]
artifact: "loom: a synthesizer that writes WAV files byte by byte, with waveforms, envelopes, mixing, and a text song format; two songs; an aliasing experiment"
deliverable: "Design note, README, a song-format reference, short demo with audio, 1-page aliasing lab report"
---

# Project: Tone Loom

| | |
| :-- | :-- |
| **Module** | 02 Programming Fundamentals |
| **Prerequisites** | Labs 01–03 of this module; Math M05–M07 (fractions, ratios, exponents; the pitch formula is explained below); [Base Workshop](../../../00-foundations/math/projects/base-workshop/spec.md)'s `minihex.py` |
| **You build** | `loom`, a music synthesizer with no audio libraries: it computes every sample of a sound wave itself and writes the WAV file's bytes by hand. Waveforms, notes, envelopes, mixing, a song language, and an experiment that makes a famous sampling effect audible |
| **Deliverable** | Design note, README, song-format reference, recorded demo, and a lab report |

---

## Why this matters

Sound on a computer is just numbers: tens of thousands of them per second, each saying how far the speaker cone should be pushed at that instant. A WAV file is a short header followed by those numbers as bytes. When you write both yourself, three big ideas become concrete:

1. **Binary file formats.** Exact byte layouts, sizes, and **byte order** (little-endian). You'll do this again with archives in Module 07, packets in Module 09, and database pages in Module 11.
2. **Sampling.** A continuous wave becomes a list of numbers taken at regular times. Sample too slowly and high sounds turn into wrong, lower sounds — an effect you'll *hear* in Milestone 5. This is the heart of signals (Module 12) and of every digital radio, camera, and microphone.
3. **Math you can hear.** Ratios are musical intervals; exponents are octaves; sine waves are pure tones; adding waves is mixing.

And at the end you have something fun: a program that plays songs you wrote in a text file.

**Real-world analogs:** software synthesizers, trackers, the WAV/RIFF format, audio drivers, DSP code in phones and radios.

---

## Background

### Sampling

A **sample rate** of 44,100 Hz means 44,100 numbers per second (the CD standard). Sample n is taken at time t = n ÷ 44,100 seconds.

A pure tone of frequency f (cycles per second, Hz) at full volume is the sine wave sin(2πft) (M10: the circle picture, going round f times per second). Each sample is stored as a **16-bit signed integer** from −32,768 to 32,767 (M07: two's complement):

```python
sample = round(volume * 32767 * math.sin(2 * math.pi * f * n / 44100))
```

### Pitch: ratios and exponents

- Going up one **octave** **doubles** the frequency. A4 = 440 Hz, A5 = 880 Hz, A3 = 220 Hz.
- The octave is split into **12 equal steps** (semitones). Equal *steps* in pitch are equal *ratios* in frequency (M11: this is why pitch is logarithmic), so each semitone multiplies by 2^(1/12) ≈ 1.0595.
- Number the notes as MIDI does: A4 = 69, C4 (middle C) = 60, one number per semitone. Then

$$f = 440 \times 2^{(n - 69)/12}$$

  So C4 = 440 × 2^(−9/12) ≈ **261.63 Hz**.
- **Intervals are ratios** (M05–M06): a perfect fifth (C to G) is close to 3 : 2; a major third close to 5 : 4. Equal temperament makes them *almost* those fractions — a compromise you can hear.

### The WAV file (16-bit mono PCM)

All multi-byte numbers are **little-endian**: least significant byte first (so 44,100 = 0x0000AC44 is stored as `44 AC 00 00`).

| Offset | Size | Field | Value for 16-bit mono, 44,100 Hz |
| :-- | :-- | :-- | :-- |
| 0 | 4 | `"RIFF"` | ASCII |
| 4 | 4 | chunk size | 36 + data size |
| 8 | 4 | `"WAVE"` | ASCII |
| 12 | 4 | `"fmt "` | ASCII (note the space) |
| 16 | 4 | fmt size | 16 |
| 20 | 2 | audio format | 1 (PCM) |
| 22 | 2 | channels | 1 |
| 24 | 4 | sample rate | 44,100 |
| 28 | 4 | byte rate | sample rate × channels × 2 = 88,200 |
| 32 | 2 | block align | channels × 2 = 2 |
| 34 | 2 | bits per sample | 16 |
| 36 | 4 | `"data"` | ASCII |
| 40 | 4 | data size | number of samples × channels × 2 |
| 44 | … | samples | 16-bit signed, little-endian |

Python's `struct` module packs these: `struct.pack("<4sI4s", b"RIFF", 36 + data_size, b"WAVE")` (`<` means little-endian, `I` a 4-byte unsigned int, `H` a 2-byte one, `h` a 2-byte signed one).

**Rule for this project:** you may *not* use Python's `wave` module, numpy, or any audio library to **write** files. You **may** use `wave` in your tests, as an independent reader that checks your files (a second witness).

---

## Milestones

### Milestone 1 — One second of A4, by hand

1. **Design note v1** (1–2 pages): modules (wave generation, envelopes, mixing, song parsing, WAV writing), the data passed between them (a list of floats from −1.0 to 1.0 is a good internal format; convert to integers only when writing), and two choices with reasons.
2. `write_wav(path, samples, rate=44100)`: header + samples, using `struct`.
3. Generate 1 second of silence and 1 second of a 440 Hz sine. Play them (`aplay a4.wav`; macOS `afplay`).
4. **Inspect the bytes** with your `minihex.py` (or `xxd a4.wav | head`). Find each header field and check its value by hand: `RIFF`, the chunk size, `44 AC 00 00`, and so on.

**Tests:**
- the header of a 1-second mono file is exactly the 44 bytes you computed by hand (write the expected bytes out in the test as a hex string);
- the file size is 44 + 88,200 bytes;
- Python's `wave` module reads it back with the right rate, channels, sample width, and frame count.

**Done when:** you heard A4, and your hand-decoded header matches.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why does the file say its own size at offset 4 and 40?* (What would a player have to do otherwise? What could go wrong if the sizes are wrong? Try it: write a wrong size and see what your player does.)

### Milestone 2 — Waveforms and notes

1. Oscillators, each a function of phase (0 to 1 over one cycle): **sine**, **square** (+1 for the first half, −1 for the second), **sawtooth** (rises from −1 to +1), **triangle**, and **noise** (random values; use a seeded `random.Random`).
2. `note_to_freq("C#4")` and back: parse note names (letter, optional `#` or `b`, octave number) to MIDI numbers and frequencies.
3. Play a C major scale (C4 D4 E4 F4 G4 A4 B4 C5) in each waveform. Listen to how they differ.

**Tests:** A4 = 440; A5 = 880; C4 ≈ 261.63 (to 2 decimals); `"Db4"` and `"C#4"` are the same note; one cycle of each waveform has the expected minimum, maximum, and average (square averages 0; sawtooth starts at −1).

**Done when:** you can play the scale in all five waveforms.

**[W]:** square and sawtooth sound "buzzier" than sine. Why? (Hint: their sharp corners contain many higher frequencies. Module 12's Fourier ideas make this exact; for now, write your guess.)

### Milestone 3 — Envelopes, mixing, and clipping

1. **ADSR envelope:** a note's volume over time: **attack** (rise from 0 to 1), **decay** (fall to the sustain level), **sustain** (hold), **release** (fall to 0 after the note ends). Each segment is a straight line (M09: a piecewise linear function). Multiply each sample by the envelope.
2. Play a note with no envelope and with one. The click at the start and end of the plain note is a sudden jump in the wave; the envelope removes it.
3. **Mixing:** to play two sounds at once, **add** their samples. Play a C major chord (C4 + E4 + G4).
4. **Clipping:** three notes at volume 0.5 each can add to 1.5, beyond the range. Detect when samples exceed ±1.0, report how many, and offer two fixes: **normalise** (scale everything so the loudest sample is just under 1.0) or **hard clip** (cut at ±1.0). Listen to both.

**Tests:** envelope values at the start, at the end of attack, during sustain, and at the end of release; mixing silence with a signal leaves it unchanged; normalising leaves the loudest sample at the target level.

**Done when:** a clean chord plays, and you've heard the difference between clipped and normalised versions.

### Milestone 4 — The song language

Design a text format for songs. Starting point (change it if you like, and document every change):

```
# ode.loom — a public-domain melody
tempo 100
track melody  wave=triangle  volume=0.6  adsr=0.01,0.1,0.7,0.2
  E4 1/4  E4 1/4  F4 1/4  G4 1/4
  G4 1/4  F4 1/4  E4 1/4  D4 1/4
  C4 1/4  C4 1/4  D4 1/4  E4 1/4
  E4 3/8  D4 1/8  D4 1/2
track bass  wave=sine  volume=0.5
  C3 1  G2 1  C3 1  G2 1
```

- `tempo` is beats per minute; a quarter note (`1/4`) is one beat. So a note of length L (a fraction of a whole note) lasts **L × 4 × 60 ÷ tempo** seconds. (M05: keep L as an exact fraction until the very end.)
- `r` is a rest. Tracks play at the same time and are mixed.
- Errors must name the file, line, and column, and say what was expected: `ode.loom:7:12: expected a duration like 1/4, got "1/x"`.

Write `loom play song.loom` (renders to a temporary WAV and plays it) and `loom render song.loom out.wav`.

**Write two songs:** one public-domain melody (folk songs, classical themes) and one of your own (even 8 bars). Put a header comment saying where the melody comes from.

**Tests:** parser tests including every error; duration math with exact fractions; a **golden test** on a tiny song (render it, compare the samples' checksum to a stored value; regenerate only on purpose, Lab 02).

**Done when:** both songs render and play correctly; all parser errors are clear.

**Checkpoint:** Milestone Checkpoint. Feynman target: *how a text file becomes sound*, all the way from parsing to bytes.

### Milestone 5 — The aliasing experiment

Sampling can only capture frequencies up to **half the sample rate** (the **Nyquist frequency**: 22,050 Hz at 44,100). What happens above it?

1. Generate 2-second sine tones at 1,000; 5,000; 15,000; 20,000; 25,000; and 30,000 Hz at a **44,100** Hz sample rate.
2. Before listening, **predict** what you'll hear for each [lab report step 2].
3. Listen (carefully — keep the volume low; 15,000 Hz and up may be inaudible to you, which is normal). Then open the files in Audacity (free) and use *Analyze → Plot Spectrum* to see which frequency is *actually* present.
4. You'll find that 30,000 Hz shows up as **14,100 Hz** (= 44,100 − 30,000), and 25,000 Hz as 19,100 Hz. A frequency above the Nyquist limit "folds back" below it. This is **aliasing**.
5. Repeat at an 8,000 Hz sample rate with tones of 1,000; 3,000; 5,000; and 7,000 Hz. Now you can easily hear the folding.

**Done when:** a lab report with predictions, observed frequencies, and the rule you found.

**[W]:** why do a car's wheels sometimes look like they're spinning backwards in a film? (Same effect, in time instead of sound.)

---

## Testing guidance

- **Byte-exact headers**, with expected bytes written by hand.
- **A second witness:** the `wave` module reads every file you write.
- **Pure functions** for oscillators and envelopes (inputs → list of floats); easy to test with known values.
- **Golden checksums** for whole songs, regenerated only deliberately.
- **Listen.** Your ears are a real test instrument. A click, a buzz, or silence is a bug report.

## Common pitfalls

- **Big-endian by mistake:** `struct.pack(">…")` writes bytes the wrong way round; players will refuse the file or play noise.
- **Signed vs unsigned:** 16-bit WAV samples are **signed** (`h`), not unsigned (`H`).
- **Integer overflow in samples:** a value of 32,768 doesn't fit; clamp before packing.
- **Floating-point time drift:** compute each sample's time as `n / rate`, not by adding `1/rate` repeatedly (M06 Part 7: errors accumulate).
- **Phase jumps between notes:** starting each note at phase 0 can click. Envelopes hide this; a stretch goal fixes it properly.
- **Loud sounds:** keep test volumes modest and your headphones low. Pure high tones are unpleasant.

## Communication deliverable

1. **Design note** v1 and v2.
2. **`SONG_FORMAT.md`:** the song language reference, every keyword with an example (your second language specification after PML).
3. **README** with how to render and play, and how to run tests.
4. **Demo:** play your two songs, show the WAV header in `minihex.py`, and play the aliasing tones while showing their spectra.
5. **Lab report** on aliasing ([template](<../../../04 - System/Lab Report Template.md>)).

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 1, write the WAV header table from memory (after reading it twice); before Milestone 4, write the duration formula from memory |
| **F** | Text → sound; aliasing in plain words |
| **W** | Why the file stores its sizes; why square waves buzz; why wheels spin backwards |
| **S** | Header writing as labelled steps; song parsing subgoals |
| **I** | Math (ratios, exponents, sine, piecewise lines) interleaved with binary formats and parsing |
| **T** | Note, format reference, README, demo, report |

## Stretch goals

- **Stereo:** two channels, with panning per track (block align and byte rate change — update the header math).
- **Drums:** noise bursts with fast envelopes for hi-hats and snares; a pitch-dropping sine for a kick.
- **Echo:** a delay line (a **ring buffer** — `%` again!) that feeds a quieter copy of the signal back in.
- **Read WAVs:** parse any 16-bit PCM WAV, print its header, and draw its waveform in the terminal.
- **Continuous phase** across notes to remove clicks without envelopes.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| WAV writing | Byte-exact header tests, verified by `wave`, decoded by hand | Plays | Broken files |
| Synthesis | Five waveforms, notes, ADSR, mixing, clipping handled | Most | Sine only |
| Song language | Two songs; precise errors with line and column; exact fractions | Songs play | Fragile parser |
| Aliasing | Predictions, spectra, rule found, report written | Partial | Missing |
| Communication | Note, format reference, README, demo, report | Most | Few |

**Done when:** every area at least 2; WAV writing and Song language at 3.

## Connections

- **Back:** M05–M07 (fractions, ratios, exponents, two's complement), M10 (sine as a circle), M11 (pitch is logarithmic), Base Workshop (bytes, hex).
- **Forward:** Module 04 (a microcontroller can play your songs through a buzzer), Module 07 (binary formats in C), Module 09 (byte order in packet headers — networks use **big**-endian), Module 12 (signals, frequency, the Fourier idea).

> **Originality note:** Tone Loom's song language, milestone structure, and aliasing experiment were designed for this curriculum. The WAV format and MIDI note numbering are public standards, used here as specified.
