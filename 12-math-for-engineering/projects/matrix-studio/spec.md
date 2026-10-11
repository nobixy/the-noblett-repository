---
title: "Project: Matrix Studio"
id: "MOD12-PRJ-matrix-studio"
type: "project"
module: "12-math-for-engineering"
phase: "C"
order: 880
prerequisites: [MOD12-L1, MOD12-L2, MOD12-L3, MOD12-L4, MOD05-PRJ-vault-search]
units: "L1, L2, L3, L4"
artifact: "Image transformation with matrices (rotation, scaling, shear, homogeneous coordinates, interpolation); your own Gaussian elimination and least squares; PageRank of your vault's link graph by power iteration; SVD image compression"
deliverable: "Lab report: matrices at work on images, data, and your notes (with figures)"
---

# Project: Matrix Studio

| | |
| :-- | :-- |
| **Module** | 12 Math for Engineering (Units L1–L4) |
| **You build** | Tools that put linear algebra to work: transforming images with matrices; solving linear systems and fitting models by least squares with your own code; ranking the notes in your Obsidian vault by their links with eigenvectors; and compressing images with the singular value decomposition |
| **Deliverable** | A lab report with figures |

---

## Why this matters

Linear algebra is the most useful mathematics in modern computing: graphics, machine learning, search ranking, signal processing, robotics, and scientific simulation all run on matrices. Its ideas are geometric — a matrix *is* a transformation of space — and this project makes that literal, with images you can see.

---

## Milestones

### Milestone 1 — Transform images (Units L1–L2)

Work with images as arrays (read and write PPM — Heapsmith's visualiser format — or use Pillow only for loading and saving).

1. Write 2 × 2 matrices for: rotation by θ (M10 Part 7's formula — now you see it's a matrix), scaling, shear, and reflection. Compose them by **matrix multiplication**; check that the order matters [W].
2. Transform an image with **inverse mapping**: for each *output* pixel, apply the **inverse** matrix to find where it comes from in the input, and sample there. [W] Why map backwards instead of pushing each input pixel forwards? (Try forwards once and look at the holes.)
3. **Bilinear interpolation** for sampling between pixels; compare with nearest-neighbour.
4. **Homogeneous coordinates:** 3 × 3 matrices that include translation, so "rotate around the image centre" is one matrix (translate, rotate, translate back).
5. The **determinant** as area scaling: compute det for each transform and verify by counting how the area of a filled square changes.

### Milestone 2 — Solve and fit (Unit L3)

1. **Gaussian elimination with partial pivoting** and back substitution, yourself. Test against `numpy.linalg.solve` on random systems. Then on a nearly singular system: compare with and without pivoting and explain the difference [W].
2. **Least squares:** solve the normal equations AᵀA x = Aᵀb (and, better, with NumPy's `lstsq`, which uses a more stable method — note why).
3. Apply it:
   - **[Fare Detective](../../../00-foundations/math/projects/fare-detective/spec.md) data:** the true best-fit line, compared with your old two-point and brute-force fits.
   - **Your file-transfer timings (or Courier's, if Module 09 is already done — optional):** latency and bandwidth from many measurements.
   - **Your forgetting curve** from Study Deck's log: fit log(P(recall)) against days (linearised exponential).
4. **Geometry:** least squares is projecting b onto the column space of A. Draw it for a 3-point line fit [F].

### Milestone 3 — PageRank of your vault (Unit L4)

Your Obsidian vault is a **graph**: notes link to notes with `[[wikilinks]]` and Markdown links.
1. Parse the vault (reuse Vault Search's walker) into a directed graph.
2. Build the **transition matrix** of a random walker who follows a random link from each note (and, with probability 0.15, jumps to a random note — the "damping" that handles dead ends).
3. **Power iteration:** start with equal ranks; multiply by the matrix repeatedly until it stops changing. The result is the dominant **eigenvector** — the long-run fraction of time the walker spends on each note.
4. List your vault's top 15 notes. Do they match your sense of what's central?
5. **[W]** why does power iteration converge to the dominant eigenvector? (Write a matrix's action in its eigenvector basis; the largest eigenvalue's component wins after many multiplications.) How fast does it converge, and what decides it?

### Milestone 4 — Compress with the SVD (Unit L4)

1. Any matrix (a greyscale image) can be written as a sum of rank-one pieces ordered by importance: A = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + … (the **singular value decomposition**).
2. Compute the **first** singular vector pair yourself by power iteration on AᵀA; then use `numpy.linalg.svd` for the full decomposition (second witness: your first pair must match).
3. Reconstruct the image from the top k pieces for k = 1, 5, 20, 50, 100. Plot the error and the storage cost (k × (rows + cols + 1) numbers) against k. Show the images.
4. Plot the singular values: how quickly do they fall for a photo vs for random noise? [W] Why?

---

## Communication deliverable

**Lab report** (3–4 pages, E10): transformed images with their matrices; the pivoting experiment; the three least-squares fits with plots and interpretations; your vault's PageRank top 15 and convergence plot; the SVD compression figure and singular-value plot; three sentences explaining what an eigenvector is.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Rotation and homogeneous matrices from memory; elimination steps; power iteration |
| **F** | A matrix as a transformation; least squares as projection; eigenvectors via PageRank |
| **W** | Inverse mapping; order of composition; pivoting; damping; why power iteration converges; singular-value decay |
| **S** | Elimination and power iteration as labelled steps |
| **T** | The report |

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Transformations | All transforms, inverse mapping, bilinear, homogeneous, determinant check | Most | Few |
| Solving and fitting | Own elimination with pivoting experiment; three real fits | Two | One |
| PageRank | Vault graph, power iteration, convergence, interpretation | Works | Missing |
| SVD | Own first pair matches NumPy; compression plots | Plots only | Missing |
| Report | Clear figures and explanations | Complete | Missing |

**Done when:** every area at least 2.

## Connections

- **Back:** M10 (rotation), M09 (lines), Fare Detective, Study Deck, Vault Search, Courier/Lantern measurements.
- **Forward:** graphics, machine learning, and robotics tracks; Glimpse (transforms for a zoom feature).

> **Originality note:** the project's use of your own vault, data, and images was designed for this curriculum.
