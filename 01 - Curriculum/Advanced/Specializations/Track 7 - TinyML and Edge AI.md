---
block_id: "Block 48"
track_id: "Track 7"
title: "TinyML and Edge AI"
category: "advanced"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "C Fluency"
  - "Computer Systems"
  - "Computer Architecture"
  - "Signals and Systems Bridge"
  - "Track 1 - AI and Machine Learning"
target_profile: "Edge ML Engineer, Embedded Systems Architect, TinyML Researcher"
aliases: [Track 7 - TinyML and Edge AI, Track 7 - TinyML, Edge AI and Neuromorphic Computing]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
---

# Track 7: TinyML and Edge AI

> [!INFO] Track Overview
> - **Track ID:** Track 7
> - **Prerequisites:** [[C Fluency]], [[Computer Systems]], [[Computer Architecture]], [[Signals and Systems Bridge]], [[Track 1 - AI and Machine Learning]]
> - **Target Profile:** Edge ML Engineer, Embedded Systems Architect, TinyML Researcher
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Standard deep learning research presumes hyperscale cloud clusters, gigawatt power grids, and liquid-cooled datacenter GPUs with terabytes of high-bandwidth memory. However, the vast majority of physical computation occurs on the edge: billions of resource-constrained microcontrollers, smart sensors, industrial IoT nodes, medical wearables, and autonomous micro-robotics operating under extreme constraints (< 1 mW active power budgets, < 256 KB of SRAM, and < 1 MB of Flash storage).

TinyML is the rigorous discipline of executing deep neural network inference and adaptive on-device learning directly at the sensor boundary without round-trip network latency, cloud dependency, or privacy leakage. Mastering this field requires a dual mastery of machine learning algorithmic compression (mathematical quantization, second-order pruning, structural neural architecture search) and bare-metal systems engineering (ARM Cortex-M/RISC-V SIMD intrinsics, memory hierarchy cache scheduling, DMA double-buffering, and zero-allocation execution runtimes).

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[C Fluency]]
- [[Computer Systems]]
- [[Computer Architecture]]
- [[Signals and Systems Bridge]]
- [[Track 1 - AI and Machine Learning]]




## 📚 Core Courses

### Course 1: Foundations of Efficient Deep Learning (MIT 6.5940 Equivalent)

This course establishes the mathematical, algorithmic, and statistical foundations of neural network compression, pruning, and hardware-aware architecture search.

#### Module 1: Numeric Representations & Post-Training Quantization (PTQ)
- Mathematical analysis of numeric formats: IEEE 754 FP32, FP16, BF16, INT8, INT4, and microscopic FP4/microscaling formats (MXFP6/MXFP4).
- Uniform affine quantization formulas:
  $$q = \text{clip}\left(\left\lfloor \frac{r}{S} \right\rceil + Z, q_{\min}, q_{\max}\right)$$
  where $S$ is the scale factor and $Z$ is the zero-point integer.
- Symmetric vs asymmetric quantization schemes; per-tensor versus per-channel scaling factor derivations.
- Dynamic range calibration algorithms: MinMax calibration, MSE minimization, and Kullback-Leibler (KL) divergence histogram calibration.
- Fixed-point integer arithmetic pipelines: replacing floating-point multiply-accumulate (MAC) with 32-bit integer accumulation and bit-shift scaling multipliers ($S_{\text{mult}} = S_1 S_2 / S_3$).

#### Module 2: Quantization-Aware Training (QAT) & Fine-Tuning
- Simulating quantization noise during backpropagation using the Straight-Through Estimator (STE).
- Learned Step Size Quantization (LSQ) for dynamic parameter step learning.
- Second-order Taylor expansion for weight rounding optimization (AdaRound).
- Mixed-precision quantization: integer-linear programming (ILP) and Pareto frontier optimization across layers based on Hessian eigenvalue spectrum sensitivity.

#### Module 3: Sparsification, Pruning & Matrix Compression
- Unstructured magnitude pruning; iterative magnitude pruning with weight rewiring.
- Structured pruning: block pruning, channel pruning, and kernel-level tensor slicing.
- Theoretical foundations: The Lottery Ticket Hypothesis and iterative weight rewinding.
- Optimal Brain Surgeon (OBS) and Optimal Brain Damage (OBD) using empirical Fisher information matrices.
- Compression encodings: Compressed Sparse Row (CSR), Compressed Sparse Column (CSC), and run-length Huffman encoding.

#### Module 4: Compact Neural Architectures
- Depthwise separable convolutions: analytical breakdown of parameter and FLOP reduction ratios ($\frac{1}{N} + \frac{1}{D_k^2}$).
- Inverted residuals and linear bottlenecks (MobileNetV2, MobileNetV3).
- Channel shuffle operators for group convolutions (ShuffleNet v1/v2).
- Micro-architectures for audio keyword spotting (Temporal Convolutional Networks, Squeeze-and-Excitation blocks, Depthwise Dilated Convolutions).

#### Module 5: Hardware-Aware Neural Architecture Search (NAS)
- Multi-objective optimization: balancing accuracy against latency, SRAM footprint, and energy per inference.
- Once-for-All (OFA) networks: decoupled supernet training with progressive shrinking.
- Hardware latency modeling: building empirical Look-Up Tables (LUTs) across microcontrollers, DSPs, and edge NPUs.
- Evolutionary search algorithms and Bayesian optimization constrained by hard memory ceilings.

---

### Course 2: Embedded Edge Systems & Microcontroller Deployment

This course bridges compressed models to bare-metal hardware execution, focusing on memory allocation arenas, assembly-level vectorization, and sensor DMA interfaces.

#### Module 1: Microcontroller Architectures & Memory Hierarchy
- Hardware execution cores: ARM Cortex-M4, Cortex-M7, Cortex-M55, Cortex-M85 (Helium vector extensions), and RISC-V RV32IMAC / RV32-Xpulp.
- Memory subsystem constraints: Tightly-Coupled Memory (ITCM/DTCM), multi-bank SRAM, internal Flash memory wait states, and external QSPI/Octal-SPI XiP (eXecute-in-Place).
- Cache architecture: D-Cache clean/invalidate mechanics, cache-line bouncing, and non-cacheable DMA buffer placement.

#### Module 2: Bare-Metal SIMD Acceleration & Kernel Optimization
- ARM CMSIS-NN kernel internals: utilizing DSP instructions (`__SMLAD`, `__QADD8`, `__USAT`) for 4-way parallel 8-bit dot products.
- Loop unrolling, register tiling, and accumulator overflow prevention.
- Implementing fast im2col and memory-efficient patch-based direct convolution algorithms.
- Custom RISC-V vector extensions (RVV) and assembly hand-tuning for depthwise convolutions.

#### Module 3: Static Memory Management & Zero-Allocation Inference Runtimes
- Operating systems without heap allocators: static memory arena allocation patterns.
- Tensor lifetime analysis: constructing directed acyclic graphs of tensor lifespans to calculate optimal 2D memory packing without external fragmentation.
- In-place tensor computation: buffer reuse between non-overlapping activation buffers.
- Model graph compilation: translating ONNX / FlatBuffer models into pure static C code (TensorFlow Lite for Microcontrollers, microTVM, TinyEngine).

#### Module 4: Edge NPUs & Dedicated Accelerators
- Edge Neural Processing Units (NPUs): Arm Ethos-U55/U65, Google Coral Edge TPU, Kendryte K210.
- Dataflow architectures: weight-stationary, output-stationary, and row-stationary systolic execution.
- Command stream generation, weight streaming via DMA, and hardware-accelerated activation functions.

#### Module 5: Low-Power Sensor Pipelines & On-Device Learning
- Interfacing sensor peripherals: PDM digital microphones, I2S audio codecs, and DVP/MIPI-CSI camera interfaces.
- Continuous streaming with circular DMA double-buffering: achieving zero-CPU-overhead sensor acquisition.
- Tiny On-Device Transfer Learning (TinyTL): memory-efficient bias-only and lite-residual updates on microcontrollers.
- Streaming anomaly detection: unsupervised autoencoders and Gaussian mixture models for continuous industrial predictive maintenance.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Han, S., Mao, H., & Dally, W. J. (2016).** *Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding*. International Conference on Learning Representations (ICLR 2016, Best Paper Award).
- **Jacob, B., Kligys, S., Chen, B., Zhu, M., Tang, M., Howard, A., Adam, H., & Kalenichenko, D. (2018).** *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference*. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2018), 2704–2713.
- **Lin, J., Chen, W.-M., Cai, H., & Han, S. (2020).** *MCUNet: Tiny Deep Learning on IoT Devices*. Advances in Neural Information Processing Systems (NeurIPS 2020), 33, 11711–11722.
- **Frankle, J., & Carbin, M. (2019).** *The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks*. International Conference on Learning Representations (ICLR 2019, Best Paper Award).
- **Warden, P., & Situnayake, D. (2020).** *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers*. O'Reilly Media.

---

## 🛠️ Progressive Labs

### Lab 1: Fixed-Point Arithmetic & Quantization Kernel in C
- **Objective:** Implement a bit-exact INT8 2D convolution and fully-connected forward pass in ANSI C99 from first principles without floating-point instructions or standard library runtime dependencies.
- **Deliverables:**
  - C source module implementing per-channel scaled 8-bit convolution with 32-bit accumulation and integer multiplier bit-shifting.
  - Python verification script exporting PyTorch quantized weights and input tensors into raw C header byte arrays.
- **Acceptance Criteria:**
  - Automated test harness verifies bit-exact numerical parity (zero discrepancy across $10^6$ output activations) against PyTorch's native integer reference engine.
  - The C kernel must compile under `gcc -Wall -Wextra -Werror -O3 -m32` with zero dynamic allocations (`malloc` or `calloc`).

### Lab 2: CMSIS-NN Vectorized Acceleration & Benchmark
- **Objective:** Port the convolution kernel to an ARM Cortex-M target (or QEMU ARM Cortex-M4 emulator) utilizing CMSIS-NN DSP intrinsics (`__SMLAD` SIMD dual-multiply-accumulate).
- **Deliverables:**
  - Optimized kernel assembly / C code utilizing 4-way SIMD parallel packing.
  - Benchmarking harness reading the hardware DWT (Data Watchpoint and Trace) cycle counter register (`CYCCNT`).
- **Acceptance Criteria:**
  - Cycle-accurate execution demonstrates at least $4.0\times$ speedup in CPU cycle efficiency compared to the naive C99 baseline from Lab 1.
  - Total stack consumption for kernel execution must remain below $2.0 \text{ KB}$, verified via stack watermarking tests.

### Lab 3: Zero-Allocation Static Memory Arena Runtime
- **Objective:** Construct an automated offline model compiler and runtime scheduler in Python and C that ingests a serialized computation graph, performs lifetime interval analysis, and allocates an optimal non-overlapping tensor memory arena.
- **Deliverables:**
  - Python graph parser generating a static C execution plan and coordinate offset table for all intermediate activation buffers.
  - C engine executing complete multi-layer inference inside a single contiguous pre-allocated byte buffer.
- **Acceptance Criteria:**
  - Peak SRAM footprint reduction of at least $35\%$ compared to naive sequential buffer allocation across a 12-layer MobileNet backbone.
  - Zero heap usage verified via link-time symbol wrapper interception (`--wrap=malloc`), executing successfully within a strict $128 \text{ KB}$ SRAM budget.

---

## 🏆 Capstone Build Deliverable

### Autonomous Real-Time Keyword Spotting & Vision Anomaly Detection on Bare-Metal Microcontroller

An end-to-end, fully autonomous cyber-physical intelligence system deployed to a bare-metal microcontroller (ARM Cortex-M4/M7, e.g., STM32H7 or Raspberry Pi Pico 2 RISC-V) with real-time audio and vision anomaly detection.

```text
+-----------------------------------------------------------------------------------+
|                           BARE-METAL EMBEDDED SYSTEM                              |
|                                                                                   |
|  [ Microphone ] ---> [ Circular DMA Buffer ] ---> [ Fixed-Point STFT Filterbank ] |
|                                                               |                   |
|                                                               v                   |
|  [ Camera DVP ] ---> [ Double Ping-Pong DMA] ---> [ Quantized CNN Inference Engine ]
|                                                               |                   |
|                                                               v                   |
|  [ GPIO / Actuator ] <--- [ Outlier Detection ] <--- [ Memory Arena (<128 KB) ]  |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Model Architecture:** A custom quantized visual wake-word classifier and 1D temporal acoustic keyword spotter (< 250 KB Flash, < 80 KB peak SRAM consumption).
2. **Peripheral Pipeline:** Continuous DMA double-buffering capturing audio from an I2S/PDM digital microphone and video frames from an Omnivision DVP sensor, executing zero-copy handoffs to the tensor arena.
3. **Execution Runtime:** Custom static C runtime executing INT8 quantized inference with CMSIS-NN / RISC-V vector acceleration.

#### Verification & Acceptance Criteria
- **Inference Latency:** Complete single-frame inference latency must measure $< 100 \text{ ms}$ under continuous operation, clocked via hardware timer pins.
- **Energy Budget:** Average active system power consumption measured via physical current profiler (Nordic PPK2 or precision multimeter) must remain $< 50 \text{ mW}$ during continuous inference.
- **Robustness & Memory Integrity:** The system must process 500 consecutive test inference frames and acoustic streams without a single dropped frame, kernel panic, or stack-pointer collision.
- **Test Commands:**
  ```bash
  # Run host verification unit tests
  make test_tinyml_runtime
  # Run bit-exact simulation in QEMU ARM Cortex-M4
  qemu-system-arm -M lm3s6965evb -nographic -kernel build/tinyml_firmware.bin
  # Verify memory footprints
  arm-none-eabi-size build/tinyml_firmware.elf
  ```

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Assessment criteria go here.

## ➡️ Next Steps & Degree Pathway
- **Curriculum Hub:** [[Specializations Hub|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[Specialization A1|Block 26 - Specialization A1]] and Course 2 binds to [[Specialization A2|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[Specialization B1|Block 29 - Specialization B1]] and Course 2 binds to [[Specialization B2|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]]

- **Sequential Flow:** [[Track 6 - Computer Engineering|← Track 6 - Computer Engineering]] | [[00 - Dashboard|Dashboard]] | [[Track 8 - Rust for Systems Engineering and Formal Verification|Track 8 - Rust for Systems Engineering and Formal Verification →]]
