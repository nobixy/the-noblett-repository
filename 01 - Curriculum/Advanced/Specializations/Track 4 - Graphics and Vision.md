---
track_id: "Track 4"
title: "Graphics and Vision"
category: "advanced"
term: "Years 4 & 5"
status: not-started
prerequisites: []
target_profile: "Computer Graphics Engineer, Rendering Pipeline Architect, Computer Vision Scientist"
aliases: [Track 4 - Graphics and Vision, Track 4 - Computer Graphics and Vision]
tier: "Tier 3 - Depth"
---

# Track 4: Graphics and Vision

> [!INFO] Track Overview
> - **Track ID:** Track 4
> - **Prerequisites:** [[C Fluency]], [[Multivariable Calculus]], [[Physics II]], [[Linear Algebra]], [[Algorithms I]]
> - **Target Profile:** Computer Graphics Engineer, Rendering Pipeline Architect, Computer Vision Scientist
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Visual computing is one of the most computationally demanding and mathematically elegant subfields of computer science. It sits at the intersection of electromagnetic radiative transfer physics, differential geometry, numerical Monte Carlo integration, and massively parallel GPU hardware architectures. From photorealistic movie visual effects and real-time interactive game engines to medical volume visualization, spatial computing, and autonomous vehicle vision, high-performance graphics and vision engineers build the engines that simulate light and reconstruct the physical 3D world.

This track guides students through the complete continuum of visual computing: from the mathematical foundations of affine projective geometry and hardware rasterization to physically based light transport (the Rendering Equation), microfacet reflection models, Monte Carlo path tracing, modern explicit GPU APIs (Vulkan, WebGPU), and modern differentiable neural radiance representations (NeRF, 3D Gaussian Splatting).

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- *None. This is a foundational block.*


## 📚 Core Courses

### Course 1: Mathematical Foundations of Computer Graphics (GAMES101 / Shirley Equivalent)

This course develops 3D geometric transformations, hardware rasterization algorithms, local illumination models, and fundamental ray tracing data structures.

#### Module 1: Transformations & Projective Geometry
- Coordinate frames: model, world, camera/view, and clip spaces.
- 3D affine transformations: 4x4 homogeneous transformation matrices, translation, scaling, shear, and Rodrigues' rotation formula.
- Perspective projection: viewing frustum, field of view (FOV), aspect ratio, near/far clipping planes, and perspective division.
- Quaternions for spatial rotations: SLERP (Spherical Linear Interpolation) and avoiding gimbal lock.

#### Module 2: The Hardware Rasterization Pipeline
- Triangle rasterization: edge function tests, barycentric coordinates, and perspective-correct attribute interpolation.
- Depth buffering ($z$-buffer) and visibility determination; early-$z$ rejection and occlusion culling.
- Anti-aliasing algorithms: Supersample Anti-Aliasing (SSAA), Multi-Sample Anti-Aliasing (MSAA), and temporal anti-aliasing (TAA) reprojection.
- Color spaces and gamma correction: sRGB, linear RGB, and HDR (High Dynamic Range) tone-mapping operators (Reinhard, ACES).

#### Module 3: Local Illumination & Shading Models
- Radiometric quantities: radiant energy, flux, irradiance, and radiance ($L = \frac{d^2\Phi}{dA \cos\theta d\omega}$).
- Classical empirical models: Lambertian diffuse, Phong reflection, and Blinn-Phong half-vector optimization.
- Shading frequencies: flat shading, Gouraud per-vertex shading, and Phong per-pixel shading.
- Texture mapping: UV parameterization, bilinear filtering, trilinear mipmapping, and anisotropic filtering to prevent aliasing.

#### Module 4: Spatial Acceleration Data Structures & Ray Tracing
- Ray-surface intersection mathematics: rays intersecting planes, spheres, axis-aligned bounding boxes (AABB), and triangles (Möller-Trumbore algorithm).
- Spatial partitioning trees: Bounding Volume Hierarchies (BVH), k-d trees, and Octrees.
- The Surface Area Heuristic (SAH) for optimal BVH spatial partitioning and fast ray traversal.

#### Module 5: Geometry Processing & Mesh Representations
- Polygon mesh data structures: indexed triangle meshes, winged-edge, and half-edge data structures.
- Surface differential geometry: normal vectors, principal curvatures, and discrete Laplace-Beltrami operators.
- Mesh simplification: Garland-Heckbert quadric error metrics (QEM) edge collapse.
- Subdivision surfaces: Catmull-Clark and Loop subdivision algorithms.

---

### Course 2: Physically Based Rendering & Real-Time GPU Architectures (PBRT / Pharr et al. / Vulkan)

This course covers global illumination, the physics of light transport, Monte Carlo integration, low-level Vulkan GPU programming, and 3D computer vision.

#### Module 1: The Rendering Equation & Light Transport Theory
- The Fredholm integral equation of the second kind (Kajiya's Rendering Equation):
  $$L_o(p, \omega_o) = L_e(p, \omega_o) + \int_{\Omega} f_r(p, \omega_i, \omega_o) L_i(p, \omega_i) (\omega_i \cdot n) d\omega_i$$
- Neumann series expansion and light transport path notation ($E[D|S]*L$).
- Bidirectional Scattering Distribution Functions (BSDF): reciprocity (Helmholtz reciprocity) and energy conservation invariants.

#### Module 2: Monte Carlo Integration & Importance Sampling
- Probability Theory on the hemisphere: probability density functions (PDFs), solid angle measures ($d\omega = \sin\theta d\theta d\phi$), and cumulative distribution functions (CDFs).
- Monte Carlo estimator variance and convergence rate ($\mathcal{O}(1/\sqrt{N})$).
- Importance sampling: cosine-weighted hemisphere sampling and sampling microfacet distribution functions.
- Multiple Importance Sampling (MIS) and the balance heuristic (Veach & Guibas).

#### Module 3: Microfacet Surface Theory & Volumetric Scattering
- Microfacet theory: Cook-Torrance reflection model ($f_r = \frac{D(\omega_h) F(\omega_o, \omega_h) G(\omega_i, \omega_o, \omega_h)}{4 (\omega_i \cdot n)(\omega_o \cdot n)}$).
- Normal distribution functions: GGX (Trowbridge-Reitz) and Beckmann distributions; masking-shadowing functions (Smith $G$).
- Dielectrics vs conductors: Fresnel equations and complex index of refraction ($\tilde{n} = n + ik$).
- Participating media: radiative transfer equation (RTE), absorption, out-scattering, and phase functions (Henyey-Greenstein).

#### Module 4: Explicit Real-Time GPU Architecture (Vulkan / WebGPU)
- Modern explicit graphics APIs: Vulkan, DirectX 12, and WebGPU.
- GPU resource management: physical devices, logical queues, memory heaps (device-local vs host-visible), and synchronization barriers (pipeline barriers, semaphores, fences).
- Real-time rendering pipelines: deferred shading, G-buffer layout, clustered forward shading, and screen-space ambient occlusion (SSAO).
- Hardware ray tracing (Vulkan RT / DXR): Top-Level Acceleration Structures (TLAS), Bottom-Level Acceleration Structures (BLAS), and ray-generation/closest-hit shaders.

#### Module 5: Neural Rendering, NeRFs & Spatial Vision
- Multi-view geometry: epipolar geometry, fundamental matrix $F$, essential matrix $E$, and structure-from-motion (SfM).
- Differentiable rendering: continuous volume rendering equations and ray marching.
- Neural Radiance Fields (NeRF): coordinate-based MLPs, positional encoding, and volume density integration.
- 3D Gaussian Splatting: real-time radiance field rendering via rasterization of anisotropic 3D Gaussians.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Kajiya, J. T. (1986).** *The Rendering Equation*. Proceedings of the 13th Annual Conference on Computer Graphics and Interactive Techniques (SIGGRAPH '86), 143–150.
- **Pharr, M., Jakob, W., & Humphreys, G. (2023).** *Physically Based Rendering: From Theory to Implementation, 4th Edition*. MIT Press.
- **Szeliski, R. (2022).** *Computer Vision: Algorithms and Applications, 2nd Edition*. Springer.
- **Mildenhall, B., Srinivasan, P. P., Tancik, M., Barron, J. T., Ramamoorthi, R., & Ng, R. (2020).** *NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis*. European Conference on Computer Vision (ECCV 2020), 405–421.
- **Hartley, R., & Zisserman, A. (2004).** *Multiple View Geometry in Computer Vision, 2nd Edition*. Cambridge University Press.

---

## 🛠️ Progressive Labs

### Lab 1: Multi-Threaded BVH Accelerator and Ray-Surface Intersection Engine
- **Objective:** Construct a high-performance C++ ray-primitive intersection engine implementing a Bounding Volume Hierarchy built using the Surface Area Heuristic (SAH).
- **Deliverables:**
  - Fast BVH builder featuring spatial binning and SIMD-accelerated AABB box intersection tests.
  - Multi-threaded traversal engine testing rays against dense geometric triangle meshes (e.g. Stanford Bunny, Lucy).
- **Acceptance Criteria:**
  - The traversal engine must sustain at least $10,000,000 \text{ rays/sec}$ on an 8-core CPU across a mesh containing $> 100,000$ triangles.
  - Verification tests confirm 100% ray-triangle intersection parity against an exhaustive brute-force reference tracer.

### Lab 2: Microfacet BSDF Implementation & Multiple Importance Sampling (MIS)
- **Objective:** Implement a physically plausible Cook-Torrance microfacet material model (GGX distribution, Smith masking-shadowing, Fresnel) with Multiple Importance Sampling.
- **Deliverables:**
  - Material evaluation and sampling routine implemented in a unidirectional path tracer.
  - Veach MIS power heuristic combining light source sampling and BSDF sampling.
- **Acceptance Criteria:**
  - Automated test compares rendered radiance against an analytic furnace test (integrating over a uniform white ambient environment); energy conservation error must verify $< 0.1\%$.
  - MIS implementation eliminates firefly noise artifacts on rough metallic surfaces within 64 samples per pixel.

### Lab 3: Real-Time Deferred Shading Pipeline in Vulkan / WebGPU
- **Objective:** Engineer a production-grade real-time deferred shading renderer in Vulkan or WebGPU.
- **Deliverables:**
  - Multi-pass rendering pipeline: G-Buffer pass (albedo, world normal, roughness, metallic, depth) followed by a lighting compute/fragment pass.
  - Dynamic descriptor sets, push constants, and synchronization pipeline barriers.
- **Acceptance Criteria:**
  - The renderer must sustain at least $60 \text{ FPS}$ at $3840 \times 2160$ (4K) resolution with 1,000 dynamic point lights on a modern GPU.
  - Zero validation layer warnings or errors under Vulkan Validation Layers (`VK_LAYER_KHRONOS_validation`).

---

## 🏆 Capstone Build Deliverable

### Spectral Monte Carlo Path Tracer with Volumetric Scattering and Neural Denoising

An industrial-grade physically based offline path tracer written in modern C++ (or Rust) implementing volumetric light transport, bidirectional importance sampling, and integration with an AI-accelerated denoiser (Intel Open Image Denoise / OptiX).

```text
+-----------------------------------------------------------------------------------+
|                        PHYSICALLY BASED PATH TRACER                               |
|                                                                                   |
|  [ Wavefront Ray Queue ] ---> [ BVH Traversal (AVX2/Embree) ]                     |
|                                         |                                         |
|                                         v                                         |
|  [ Multiple Importance Sampling ] <--- [ Radiative Transfer Phase Function (RTE) ]|
|                 |                                                                 |
|                 v                                                                 |
|  [ High-Dynamic-Range Framebuffer ] ---> [ OIDN / OptiX Neural Denoiser ]         |
|                                                        |                          |
|                                                        v                          |
|  [ Tonemapped Image (ACES) ] <-------------------------+                          |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Light Transport Simulation:** Unidirectional spectral Monte Carlo path tracing with Russian roulette path termination, next-event estimation (direct light sampling), and Multiple Importance Sampling.
2. **Volumetric Media:** Homogeneous and heterogeneous participating media simulation via delta tracking (Woodcock tracking) with Henyey-Greenstein anisotropic scattering phase functions.
3. **High-Performance Architecture:** Wavefront ray-tracing execution pattern sorting rays by material to maximize SIMD cache locality, utilizing AVX-512 / AVX2 vectorization.
4. **Post-Processing & Denoising:** Deep-learning neural reconstruction pass utilizing Intel Open Image Denoise (OIDN), incorporating albedo and normal feature guide buffers to produce noise-free images at low sample counts.

#### Verification & Acceptance Criteria
- **Physical Correctness & Convergence:** The path tracer must render standard academic benchmark scenes (Cornell Box, Veach MIS test, Living Room) demonstrating convergence to ground-truth reference renders with Mean Squared Error (MSE) $< 0.001$.
- **Energy Conservation:** Passes white furnace tests across all implemented smooth dielectric, rough conductor, and subsurface scattering materials.
- **Test Commands:**
  ```bash
  # Run unit tests for vector math, ray intersection, and BSDF sampling
  ctest --test-dir build --output-on-failure
  # Render benchmark Cornell Box scene at 256 samples per pixel
  ./build/bin/pathtracer --scene scenes/cornell_box.json --spp 256 --out output.exr
  # Verify image MSE against reference ground truth
  python3 scripts/compare_images.py --test output.exr --ref reference/cornell_box_ref.exr --max-mse 0.001
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
