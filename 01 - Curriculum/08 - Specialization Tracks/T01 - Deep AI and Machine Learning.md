---
block_id: "Track 1"
track_id: "Track 1"
title: "AI and Machine Learning"
category: "specialization"
subject: "Specialization"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "B01 - CS61A"
  - "B07 - Multivariable Calculus"
  - "B11 - Linear Algebra"
  - "B13 - Algorithms I"
  - "B15 - Probability"
  - "B25 - Convex Optimization"
target_profile: "Machine Learning Engineer, Research Scientist, Deep Learning Infrastructure Engineer"
aliases: [Track 1 - AI and Machine Learning, Track 1 - Artificial Intelligence and Machine Learning, "Deep AI and Machine Learning"]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
optional: true # specialization track not yet chosen (DR-001)
primary_resource: "Mathematical Machine Learning & Statistical Foundations (Stanford CS229 Equivalent) + Deep Learning Systems & Generative Architectures (CMU 10-414 / CS231n)"
milestone: "Production-Grade Autoregressive Transformer Training & Quantized Serving Engine"
date_started: ""
date_completed: ""
---

# Track 1 — AI and Machine Learning

> [!INFO] Track Overview
> - **Track ID:** Track 1
> - **Prerequisites:** [[B01 - CS61A|CS61A]], [[B07 - Multivariable Calculus|Multivariable Calculus]], [[B11 - Linear Algebra|Linear Algebra]], [[B13 - Algorithms I|Algorithms I]], [[B15 - Probability|Probability]], [[B25 - Convex Optimization|Convex Optimization]]
> - **Target Profile:** Machine Learning Engineer, Research Scientist, Deep Learning Infrastructure Engineer
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Modern Artificial Intelligence has transformed from heuristic expert systems into a foundational computational substrate spanning all of science and engineering. However, industry and academia are inundated with superficial practitioners who can only call black-box library APIs (`model.fit()`, HuggingFace pipelines) without understanding the underlying mathematical mechanics, computational bottlenecks, or statistical failure modes.

This track provides an elite, graduate-level mastery of both theoretical machine learning and scalable deep learning systems engineering. Students will master the rigorous statistical mechanics of generalization (Rademacher complexity, PAC bounds, VC dimension), convex and non-convex optimization, the calculus of automatic differentiation engines, high-throughput GPU kernel design for attention mechanisms, and distributed training systems across parallel worker clusters.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B01 - CS61A|CS61A]]
- [[B07 - Multivariable Calculus|Multivariable Calculus]]
- [[B11 - Linear Algebra|Linear Algebra]]
- [[B13 - Algorithms I|Algorithms I]]
- [[B15 - Probability|Probability]]
- [[B25 - Convex Optimization|Convex Optimization]]




## 📚 Core Courses

### Course 1: Mathematical Machine Learning & Statistical Foundations (Stanford CS229 Equivalent)

This course develops statistical learning theory, parametric and non-parametric estimation, optimization duality, and probabilistic models.

#### Module 1: Supervised Learning, Generalized Linear Models & Duality
- Maximum Likelihood Estimation (MLE) and Maximum A Posteriori (MAP) estimation.
- The Exponential Family: canonical response functions, sufficient statistics, and natural parameters.
- Derivation of Generalized Linear Models (GLMs): Ordinary Least Squares, Logistic Regression, Poisson Regression, and Softmax classification.
- Analytical derivation of the Normal Equations: $(X^T X)\theta = X^T y$ and geometric projection onto the column space $\text{col}(X)$.
- Regularization: $\ell_2$ Ridge regression (analytical solution), $\ell_1$ Lasso regression, and subgradient calculus.

#### Module 2: Kernel Methods & Support Vector Machines
- Constrained optimization: Lagrangian formulations, Karush-Kuhn-Tucker (KKT) conditions, and Slater's constraint qualification.
- Maximal margin hyperplanes: deriving the primal and dual SVM formulations.
- Mercer's Theorem and Reproducing Kernel Hilbert Spaces (RKHS): polynomial kernels, Gaussian Radial Basis Function (RBF) kernels, and the Representer Theorem.
- Support Vector Regression (SVR) with $\epsilon$-insensitive loss functions.

#### Module 3: Statistical Learning Theory & Generalization Bounds
- The Probably Approximately Correct (PAC) learning framework; $\epsilon$-$\delta$ sample complexity bounds.
- Infinite hypothesis spaces: Shattering, Vapnik-Chervonenkis (VC) dimension, and Sauer-Shelah lemma.
- Rademacher complexity: empirical and population Rademacher complexity; deriving uniform generalization bounds via McDiarmid's bounded differences inequality.
- Structural Risk Minimization (SRM) and bias-variance decomposition.

#### Module 4: Probabilistic Graphical Models & Unsupervised Learning
- Directed Graphical Models (Bayesian Networks) and Undirected Graphical Models (Markov Random Fields); d-separation and conditional independence.
- Latent variable models and the Expectation-Maximization (EM) algorithm: Jensen's inequality and Evidence Lower Bound (ELBO) ascent.
- Gaussian Mixture Models (GMM) and Factor Analysis.
- Dimensionality reduction: Principal Component Analysis (PCA) spectral derivation via SVD; Kernel PCA; t-Distributed Stochastic Neighbor Embedding (t-SNE).

#### Module 5: Reinforcement Learning & Markov Decision Processes
- Markov Decision Processes (MDPs): state transitions, reward functions, and discount factor $\gamma$.
- The Bellman Expectation and Bellman Optimality Equations for $V(s)$ and $Q(s, a)$.
- Exact dynamic programming: Policy Iteration and Value Iteration with contraction mapping convergence proofs.
- Model-free algorithms: Temporal Difference learning (TD(0)), Q-Learning, and SARSA.
- Continuous action spaces and the Policy Gradient Theorem:
  $$\nabla_\theta J(\pi_\theta) = \mathbb{E}_{\tau \sim \pi_\theta}\left[\sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t|s_t) Q^{\pi_\theta}(s_t, a_t)\right]$$

---

### Course 2: Deep Learning Systems & Generative Architectures (CMU 10-414 / CS231n)

This course examines deep neural network microarchitectures, automatic differentiation runtimes, custom CUDA GPU acceleration, and distributed model parallelism.

#### Module 1: Deep Feedforward Networks & Optimization Dynamics
- Multilayer perceptrons: universal approximation theorems (Stone-Weierstrass and Hahn-Banach formulations).
- Non-linear activations: Sigmoid, Tanh, ReLU, LeakyReLU, GeLU, and SwiGLU; vanishing/exploding gradients.
- Weight initialization: Xavier/Glorot and He/Kaiming initialization variance proofs.
- Modern first-order stochastic optimizers: Momentum, RMSProp, Adam, and AdamW with decoupled weight decay; learning rate schedulers (cosine annealing with warmup).

#### Module 2: Computer Vision, Convolutions & Residual Connections
- Convolutional layers: cross-correlation, dilation, stride, and padding arithmetic; spatial receptive field growth.
- Residual Networks (ResNets): identity skip connections mitigating gradient attenuation ($F(x) + x$); degradation problem analysis.
- Batch Normalization, Layer Normalization, RMSNorm, and Group Normalization: internal covariate shift vs loss landscape smoothing.

#### Module 3: Sequence Modeling, Transformers & Self-Attention
- Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) cell gating mechanics.
- Scaled Dot-Product Attention:
  $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
- Multi-Head Attention (MHA), Multi-Query Attention (MQA), and Grouped-Query Attention (GQA).
- Positional encodings: absolute sinusoidal encodings, learned positional embeddings, and Rotary Position Embeddings (RoPE).
- Memory-efficient attention: FlashAttention algorithmic tiling (tiling $Q, K, V$ into SRAM to eliminate $\mathcal{O}(N^2)$ HBM read/write traffic).

#### Module 4: Deep Generative Modeling & Diffusion Processes
- Deep Autoencoders and Variational Autoencoders (VAEs): reparameterization trick, derivation of ELBO.
- Generative Adversarial Networks (GANs): minimax objective, Jensen-Shannon divergence minimization, Wasserstein GAN with gradient penalty (WGAN-GP).
- Diffusion models: forward Markovian noising process, reverse denoising diffusion probabilistic models (DDPM), and continuous-time score-based SDEs.

#### Module 5: Deep Learning Systems & Distributed Scaling
- Computational graphs: static vs dynamic graphs, reverse-mode automatic differentiation (Autograd) implementation.
- Distributed Data Parallel (DDP): gradient bucketing, all-reduce collective communication, and Ring AllReduce algorithm.
- Model parallelism: Tensor Parallelism (Megatron-LM column/row linear partitioning), Pipeline Parallelism (GPipe 1F1B schedule), and ZeRO (Zero Redundancy Optimizer stages 1, 2, 3 / FSDP).

---

## 📑 Seminal Papers & Advanced Textbooks

- **Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017).** *Attention Is All You Need*. Advances in Neural Information Processing Systems (NeurIPS 2017), 30, 5998–6008.
- **He, K., Zhang, X., Ren, S., & Sun, J. (2016).** *Deep Residual Learning for Image Recognition*. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2016), 770–778.
- **Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., & Bengio, Y. (2014).** *Generative Adversarial Nets*. Advances in Neural Information Processing Systems (NeurIPS 2014), 27, 2672–2680.
- **Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., & Poole, B. (2020).** *Score-Based Generative Modeling through Stochastic Differential Equations*. International Conference on Learning Representations (ICLR 2021).
- **Bishop, C. M., & Bishop, H. (2023).** *Deep Learning: Foundations and Concepts*. Springer.
- **Sutton, R. S., & Barto, A. G. (2018).** *Reinforcement Learning: An Introduction, 2nd Edition*. MIT Press.

---

## 🛠️ Progressive Labs

### Lab 1: Autograd Engine and Tensor Framework from Scratch
- **Objective:** Construct a lightweight PyTorch-like computational graph engine and reverse-mode automatic differentiation framework in C++ or Python (with NumPy / raw buffers).
- **Deliverables:**
  - Multi-dimensional `Tensor` class with strided memory layout, slicing, and broadcasting.
  - Dynamic reverse-mode DAG graph tracker computing exact adjoint gradients for addition, matrix multiplication, convolution, and non-linear activations.
- **Acceptance Criteria:**
  - Automated test suite executes backpropagation across 50 composite mathematical functions, asserting numerical gradient parity against finite-difference approximations:
    $$\left| \frac{\partial f}{\partial x}_{\text{analytical}} - \frac{f(x+\epsilon) - f(x-\epsilon)}{2\epsilon} \right| < 10^{-5}$$
  - Zero memory leaks during forward and backward execution passes, verified under Valgrind / AddressSanitizer.

### Lab 2: Multi-Head Self-Attention with Custom CUDA Kernel
- **Objective:** Write a custom CUDA C++ kernel executing scaled dot-product self-attention with shared memory tiling (FlashAttention style) to minimize high-bandwidth memory (HBM) bandwidth bottlenecks.
- **Deliverables:**
  - CUDA source module utilizing `__shared__` memory tiling and register-level accumulation.
  - Python PyTorch C++ extension wrapper benchmarking latency and memory consumption against standard PyTorch attention.
- **Acceptance Criteria:**
  - The custom CUDA kernel must achieve at least $2.5\times$ speedup over naive PyTorch attention on sequence lengths $N \ge 2048$ on an Nvidia GPU.
  - Peak memory usage during the forward pass must scale strictly as $\mathcal{O}(N)$ rather than $\mathcal{O}(N^2)$, passing bit-exact parity checks ($\ell_\infty \text{ error} < 10^{-4}$).

### Lab 3: Distributed Data Parallel (DDP) Training with Ring AllReduce
- **Objective:** Implement the Ring AllReduce collective communication algorithm from scratch using raw TCP/MPI sockets, and integrate it into a multi-process distributed training harness.
- **Deliverables:**
  - Python / C++ network daemon executing scatter-reduce followed by all-gather over a logical ring topology.
  - Distributed training script synchronizing gradients across 4 local processes without PyTorch DDP wrappers.
- **Acceptance Criteria:**
  - Total network communication volume per step must verify exactly $\frac{2(P-1)}{P} M$ bytes for model size $M$ across $P$ nodes.
  - 4-process distributed training of a CNN/transformer demonstrates scaling efficiency $\ge 88\%$ with bit-exact model parameter weights across all ranks at every epoch.

---

## 🏆 Capstone Build Deliverable

### Production-Grade Autoregressive Transformer Training & Quantized Serving Engine

An end-to-end, high-performance deep learning pipeline implementing a decoder-only generative transformer (GPT architecture, ~125M parameters), training it from raw text, and deploying it with an optimized low-latency inference server.

```text
+-----------------------------------------------------------------------------------+
|                        AI / MACHINE LEARNING PIPELINE                             |
|                                                                                   |
|  [ Raw Text Corpus ] ---> [ Byte-Pair Tokenizer ] ---> [ Sharded Data Loader ]    |
|                                                                    |              |
|                                                                    v              |
|  [ Distributed Ring AllReduce ] <--- [ Fused Transformer Block ] <----+           |
|            |                                                                      |
|            v                                                                      |
|  [ Checkpoint Loss < 1.8 ] ---> [ INT8 Post-Training Quant ] ---> [ KV-Cache Serv] |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Model Architecture:** Custom decoder-only autoregressive transformer with Rotary Position Embeddings (RoPE), SwiGLU activation functions, RMSNorm normalization, and FlashAttention execution.
2. **Data & Training Pipeline:** Custom Byte-Pair Encoding (BPE) tokenizer; multi-GPU distributed data-parallel training loop with mixed-precision FP16/BF16 AMP (Automatic Mixed Precision), gradient clipping, and cosine learning rate decay with warmup.
3. **Inference Serving Engine:** C++ inference server featuring key-value caching (KV-cache), continuous dynamic batching, and per-channel INT8 weight quantization.

#### Verification & Acceptance Criteria
- **Model Convergence:** Must train on a curated text dataset (e.g. TinyStories or a 10GB subset of OpenWebText), demonstrating monotonic cross-entropy loss reduction converging to a validation loss $< 1.8$.
- **Inference Throughput & Latency:** The C++ inference engine must serve autoregressive token generation with time-to-first-token (TTFT) $< 30 \text{ ms}$ and throughput $> 100 \text{ tokens/sec}$ on an Nvidia RTX/A-series GPU.
- **Test Commands:**
  ```bash
  # Execute unit tests for autograd and layer implementations
  pytest tests/test_transformer_layers.py -v
  # Launch distributed training run across available GPUs
  torchrun --nproc_per_node=2 train.py --config configs/gpt_125m.json
  # Benchmark inference server throughput and latency
  python3 scripts/benchmark_inference.py --model checkpoints/gpt_125m_final.pt --batch-size 8
  ```

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Assessment criteria go here.

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Use each course's own autograders and posted solutions when you reach this track.

---

## ➡️ Next Steps & Degree Pathway
- **Curriculum Hub:** [[Specialization Branches|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[Specialization Branches|Block 26 - Specialization A1]] and Course 2 binds to [[Specialization Branches|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[Specialization Branches|Block 29 - Specialization B1]] and Course 2 binds to [[Specialization Branches|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]]

- **Sequential Flow:** [[T05 - Advanced Programming Languages and Compilers|← Advanced Programming Languages and Compilers]] | [[00 - Start Here|Start Here]] | [[T04 - Advanced Graphics and Vision|Advanced Graphics and Vision →]]
