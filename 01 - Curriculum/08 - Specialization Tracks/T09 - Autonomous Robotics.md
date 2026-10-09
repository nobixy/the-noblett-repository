---
block_id: "Track 9"
track_id: "Track 9"
title: "Autonomous Robotics, Control and Cyber-Physical Systems"
category: "specialization"
subject: "Specialization"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "B04a - Differential Equations Bridge"
  - "B07 - Multivariable Calculus"
  - "B09 - Computer Systems"
  - "B11 - Linear Algebra"
  - "B15 - Probability"
  - "B15a - Signals and Systems Bridge"
target_profile: "Autonomous Systems Engineer, Robotics Software Architect, SLAM & Motion Planning Specialist"
aliases: [Track 11 - Autonomous Robotics and Cyber-Physical Systems, Track 11 - Autonomous Robotics and CPS, "Autonomous Robotics"]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
optional: true # specialization track not yet chosen (DR-001)
primary_resource: "Modern Robotics + MIT Underactuated + MIT Manipulation + ROS 2 (free)"
milestone: "Autonomous Indoor Navigation & Exploration System in ROS 2 / Gazebo"
date_started: ""
date_completed: ""
---

# Track 9 — Autonomous Robotics, Control and Cyber-Physical Systems

> [!INFO] Track Overview
> - **Track ID:** Track 9
> - **Prerequisites:** [[B04a - Differential Equations Bridge|Differential Equations Bridge]], [[B07 - Multivariable Calculus|Multivariable Calculus]], [[B09 - Computer Systems|Computer Systems]], [[B11 - Linear Algebra|Linear Algebra]], [[B15 - Probability|Probability]], [[B15a - Signals and Systems Bridge|Signals and Systems Bridge]]
> - **Target Profile:** Autonomous Systems Engineer, Robotics Software Architect, SLAM & Motion Planning Specialist
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Autonomous robotics represents the ultimate synthesis of cyber-physical engineering: physical hardware platforms operating under uncertain, dynamic real-world environments while executing real-time spatial perception, probabilistic state estimation, high-dimensional trajectory optimization, and closed-loop feedback control. From self-driving vehicles and automated warehouse logistics to humanoid manipulators and planetary rovers, autonomous systems must make high-stakes physical decisions in milliseconds without crashing or losing stability.

Building these systems requires far more than assembling pre-built ROS packages. High-assurance robotics engineering requires deep mathematical mastery of non-linear state estimation (Extended Kalman Filters, Lie group geometry $SE(3)$, factor graph optimization), spatial perception (point cloud processing, Visual-Inertial Odometry), sampling-based and trajectory optimization algorithms (RRT*, direct collocation, Model Predictive Control), and distributed real-time publish-subscribe architectures (ROS 2, DDS).

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B04a - Differential Equations Bridge|Differential Equations Bridge]]
- [[B07 - Multivariable Calculus|Multivariable Calculus]]
- [[B09 - Computer Systems|Computer Systems]]
- [[B11 - Linear Algebra|Linear Algebra]]
- [[B15 - Probability|Probability]]
- [[B15a - Signals and Systems Bridge|Signals and Systems Bridge]]




## 🌐 Real Courses (verified 2026-10-09, DR-004)
*The module plan below is the syllabus; these are the real, current courses that teach it. Do their assignments as the coursework.*
- **Course 1 → Estimation, SLAM and kinematics:** *Modern Robotics* (Lynch & Park, free book + videos): hades.mech.northwestern.edu/index.php/Modern_Robotics; Cyrill Stachniss's SLAM/estimation lectures (free): youtube.com/@CyrillStachniss.
- **Course 2 → Control and planning:** MIT *Underactuated Robotics* (free, current): underactuated.csail.mit.edu; MIT *Robotic Manipulation* (free): manipulation.csail.mit.edu; Steve Brunton's control lectures (free): youtube.com/@Eigensteve; classic control on OCW: 6.241J Dynamic Systems and Control.
- **Hardware-in-the-loop (merged from former Track 9):** ROS 2 (docs.ros.org/en/jazzy/), Renode (renode.io) for MCU emulation.

---

## 🔀 Merged In by DR-004
**Hardware-in-the-loop and digital twins (former Track 9)** is now part of this track. Its full module plan, labs and capstone are kept in [[Cut - T09 - Hardware-in-the-Loop Virtualization and Digital Twins]]; use its labs as optional extra labs here.

---

## 📚 Core Courses

### Course 1: Probabilistic State Estimation, SLAM & Spatial Perception

This course focuses on non-linear filtering, 3D spatial transformations on Lie groups, Simultaneous Localization and Mapping (SLAM), and multi-modal sensor fusion.

#### Module 1: 3D Rigid Body Kinematics & Lie Algebra
- Coordinate representations: Euler angles, rotation matrices $SO(3)$, and unit quaternions $\mathbb{H}$; singularity and gimbal lock analysis.
- Special Euclidean group $SE(3)$ for 3D rigid poses: homogeneous transformation matrices.
- Lie theory for robotics: the Lie algebra $\mathfrak{so}(3)$ and $\mathfrak{se}(3)$, matrix exponential and logarithmic maps, tangent spaces, and computing Jacobians on manifolds.
- Forward and inverse kinematics for serial manipulators: Denavit-Hartenberg (D-H) parameterization and product of exponentials (PoE).

#### Module 2: Non-Linear Bayesian Filtering & Sensor Fusion
- Recursive Bayesian estimation: prior, prediction, likelihood, and posterior update cycles.
- The Extended Kalman Filter (EKF): first-order Taylor expansion linearization, covariance propagation, and innovation analysis.
- The Unscented Kalman Filter (UKF): deterministic sigma-point sampling, unscented transform, and avoiding analytical Jacobian computations.
- Non-parametric filtering: Particle Filtering (Sequential Monte Carlo) and Monte Carlo Localization (MCL) for non-Gaussian multimodal distributions.

#### Module 3: Graph-Based SLAM & Factor Graph Optimization
- The SLAM problem formulation: Full SLAM vs Online SLAM.
- Factor graphs and nonlinear least squares: variables (robot poses, landmark positions) and factor constraints (odometry, loop closures, GPS priors).
- Sparse Cholesky factorization and QR decomposition for solving normal equations ($J^T \Omega J \Delta x = -J^T \Omega r$).
- Optimization algorithms on manifolds: Gauss-Newton, Levenberg-Marquardt, and Powell's dogleg method using GTSAM / Ceres Solver.
- Loop closure detection: Bag of Visual Words (DBoW2), visual place recognition, and robust loss kernels (Huber, Cauchy) to reject false perceptual associations.

#### Module 4: Spatial Perception & Point Cloud Processing
- Sensor models: LiDAR (time-of-flight point clouds), stereo vision, structured light RGB-D, and IMU inertial measurement units.
- Point cloud filtering: voxel grid downsampling, pass-through filtering, and statistical outlier removal.
- Geometric registration: Point-to-Point and Point-to-Plane Iterative Closest Point (ICP), Normal Distributions Transform (NDT).
- 3D occupancy grid mapping: OctoMap hierarchical octree representations and probabilistic log-odds occupancy updates.

#### Module 5: Visual Odometry & Visual-Inertial Fusion (VIO)
- Monocular, stereo, and RGB-D visual odometry pipelines: feature extraction (ORB, SIFT), optical flow tracking (Lucas-Kanade), and epipolar geometry (essential matrix $E$, five-point algorithm).
- Visual-Inertial Odometry (VIO): tight vs loose coupling; pre-integration of high-rate IMU measurements on $SE(3)$ manifolds.
- Landmark triangulation, bundle adjustment, and keyframe selection mechanics.

---

### Course 2: Optimal Control, Motion Planning & Autonomous Navigation

This course covers path planning in continuous configuration spaces, trajectory optimization, model predictive control, and production robotics middleware.

#### Module 1: Configuration Space & Geometric Path Planning
- Configuration space ($\mathcal{C}$-space): obstacle transformation ($\mathcal{C}_{\text{obs}}$) and free space ($\mathcal{C}_{\text{free}}$) for rigid and articulated bodies.
- Search-based planning: A*, Dijkstra, Jump Point Search (JPS), and Anytime Repairing A* (ARA*).
- Sampling-based motion planning: Rapidly-exploring Random Trees (RRT), RRT-Connect, and probabilistic roadmaps (PRM).
- Asymptotic optimality: RRT* and informed RRT* with rewiring radius proofs ($r_n \propto (\frac{\log n}{n})^{1/d}$).

#### Module 2: Trajectory Optimization & Motion Generation
- Kinodynamic planning: incorporating velocity, acceleration, and jerk constraints.
- Polynomial splines: minimum-jerk and minimum-snap trajectory generation via quadratic programming (QP).
- Direct optimal control methods: shooting methods vs direct collocation; converting continuous-time optimal control problems into finite-dimensional non-linear programming (NLP) problems solved via IPOPT.

#### Module 3: Model Predictive Control (MPC) & Dynamic Tracking
- Classical state-space control: Linear Quadratic Regulator (LQR) and Riccati equation solutions.
- Linear and Non-Linear Model Predictive Control (NMPC): receding horizon optimization subject to state and input inequality constraints:
  $$\min_{u} \sum_{k=0}^{N-1} \left( x_k^T Q x_k + u_k^T R u_k \right) + x_N^T P x_N \quad \text{s.t.} \quad x_{k+1} = f(x_k, u_k), \, x \in \mathcal{X}, \, u \in \mathcal{U}$$
- Real-time iteration (RTI) schemes, warm-starting, and OSQP / acados fast solvers for microsecond-scale solve times.
- Dynamic obstacle avoidance via Control Barrier Functions (CBFs) ensuring forward set invariance.

#### Module 4: Non-Holonomic Vehicle Dynamics & Underactuated Systems
- Kinematic and dynamic models of mobile robots: differential drive, unicycle, and bicycle kinematic models.
- Underactuated robotics: cart-pole systems, acrobot, and quadrupedal contact dynamics.
- Zero-Moment Point (ZMP) and Divergent Component of Motion (DCM) for legged balance and locomotion planning.

#### Module 5: ROS 2 Architecture, DDS & Real-Time Middleware
- The Robot Operating System 2 (ROS 2): node lifecycle management, publishers, subscribers, services, and action servers.
- Data Distribution Service (DDS): Quality of Service (QoS) profiles (reliability, durability, liveliness, deadline).
- Real-time executor design: deterministic scheduling without dynamic memory allocation in the critical control loop.
- Physics simulation environments: Gazebo Garden / Harmonic, physics engines (ODE, Bullet, DART), and hardware-in-the-loop sensor emulation.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Thrun, S., Burgard, W., & Fox, D. (2005).** *Probabilistic Robotics*. MIT Press.
- **LaValle, S. M. (2006).** *Planning Algorithms*. Cambridge University Press.
- **Dellaert, F., & Kaess, M. (2006).** *Square Root SAM: Simultaneous Localization and Mapping via Square Root Information Smoothing*. The International Journal of Robotics Research, 25(12), 1181–1203.
- **Mur-Artal, R., Montiel, J. M. M., & Tardós, J. D. (2015).** *ORB-SLAM: A Versatile and Accurate Monocular SLAM System*. IEEE Transactions on Robotics, 31(5), 1147–1163.
- **Tedrake, R. (2023).** *Underactuated Robotics: Algorithms for Walking, Running, Swimming, Flying, and Manipulation*. Course Notes for MIT 6.832 (MIT Press).

---

## 🛠️ Progressive Labs

### Lab 1: Multi-Sensor EKF / UKF State Estimation in C++
- **Objective:** Implement a standalone C++ non-linear state estimation engine fusing high-rate IMU accelerometer and gyroscope data with noisy wheel encoder odometry and low-rate 2D LiDAR range measurements.
- **Deliverables:**
  - Modern C++ class implementing an Unscented Kalman Filter over the $SE(2)$ Lie group manifold without external linear algebra wrappers beyond Eigen.
  - Evaluation script validating estimation trajectory against ground-truth motion capture data.
- **Acceptance Criteria:**
  - Root Mean Square Error (RMSE) translation error must remain $< 0.05 \text{ m}$ and orientation error $< 1.0^\circ$ over a $100 \text{ meter}$ simulated trajectory under synthetic sensor noise.
  - Single filter prediction-update step latency must measure $< 500 \, \mu\text{s}$ on an embedded ARM CPU.

### Lab 2: Real-Time Graph-SLAM with Factor Graphs (GTSAM)
- **Objective:** Construct a pose-graph SLAM backend using GTSAM / Ceres Solver that optimizes robot trajectories from 2D LiDAR scan-matching odometry and loop-closure constraints.
- **Deliverables:**
  - C++ ROS 2 node subscribing to laser scan point clouds, computing Iterative Closest Point (ICP) scan-to-map matches, and inserting pose nodes into an incremental iSAM2 factor graph.
  - Robust loss function implementation (Huber kernel) rejecting spurious loop closures.
- **Acceptance Criteria:**
  - Successfully reconstruct a globally consistent 2D occupancy grid map of a public robotics benchmark dataset (e.g. Intel Lab or MIT Killian Court) with zero rotational drift.
  - The iSAM2 incremental update latency must benchmark $< 50 \text{ ms}$ per step at 10 Hz real-time processing speed.

### Lab 3: Model Predictive Control (MPC) Trajectory Tracking in ROS 2
- **Objective:** Design and implement a real-time Non-Linear Model Predictive Controller in C++ (interfacing OSQP / CasADi / acados) that drives a non-holonomic mobile robot along complex trajectories while respecting dynamic acceleration limits.
- **Deliverables:**
  - C++ ROS 2 controller node publishing geometry velocity commands (`geometry_msgs/Twist`) given reference trajectory waypoints.
  - Linearized kinematic bicycle model formulation with state and control constraint boundaries.
- **Acceptance Criteria:**
  - The vehicle must track a high-speed figure-8 trajectory in simulation, keeping maximum cross-track error $< 0.1 \text{ m}$ at speeds up to $2.0 \text{ m/s}$.
  - The quadratic programming solver must converge deterministically with solve times $< 10 \text{ ms}$ across 1,000 consecutive control cycles (100 Hz update loop).

---

## 🏆 Capstone Build Deliverable

### Autonomous Indoor Navigation & Exploration System in ROS 2 / Gazebo

A complete, production-grade autonomous navigation, frontier exploration, and obstacle avoidance software stack deployed to a differential-drive / Ackermann autonomous ground vehicle operating within high-fidelity Gazebo simulation.

```text
+-----------------------------------------------------------------------------------+
|                         AUTONOMOUS ROBOTICS STACK                                 |
|                                                                                   |
|  [ 2D/3D LiDAR & RGB-D ] ---> [ Point Cloud Filter ] ---> [ Cartographer / iSAM2 ]|
|                                                                    |              |
|                                                                    v              |
|  [ Global Costmap 2D ] <--- [ Frontier Explorer ] <--- [ 3D Pose on SE(3) ]       |
|            |                                                       |              |
|            v                                                       v              |
|  [ RRT* Global Planner ] ---> [ Local Costmap ] ---> [ NMPC Controller Engine ]   |
|                                                                    |              |
|                                                                    v              |
|  [ Gazebo Physics Sim ] <--- [ Actuator Commands ] <--- [ Control Barrier Filter ]|
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Sensory & Perception Pipeline:** Multi-beam 3D LiDAR point cloud processing, voxel grid downsampling, and ground-plane removal; continuous 6-DOF odometry estimation via GTSAM factor graph optimization.
2. **Autonomous Exploration:** Frontier exploration planner identifying boundaries between known free space and unmapped territory, computing optimal exploration inspection tours via traveling salesperson TSP heuristics.
3. **Planning & Control:** Asymptotically optimal global path planning via Informed RRT*, coupled with a real-time Model Predictive Controller enforcing Control Barrier Functions (CBFs) to guarantee collision-free trajectory tracking around unforeseen dynamic obstacles.

#### Verification & Acceptance Criteria
- **Autonomous Mapping:** The autonomous vehicle must autonomously navigate and map an unknown $500 \text{ m}^2$ multi-room indoor facility in Gazebo simulation, discovering $> 95\%$ of all traversable space without human teleoperation intervention.
- **Dynamic Obstacle Avoidance:** Under sudden insertion of moving obstacles (e.g. simulated pedestrians walking at $1.2 \text{ m/s}$ across the robot's planned path), the MPC controller must replan with reaction latency $< 20 \text{ ms}$ and maneuver safely around the obstacles.
- **Robustness:** Across 50 independent Monte Carlo evaluation trials with randomized initial robot poses and obstacle placements, the navigation stack must achieve a 100% collision-free record (zero collisions).
- **Test Commands:**
  ```bash
  # Build the complete ROS 2 robotics workspace
  colcon build --symlink-install --packages-select autonomous_nav_stack
  source install/setup.bash
  # Launch Gazebo world with autonomous vehicle and sensors
  ros2 launch autonomous_nav_stack simulation.launch.py world:=indoor_facility
  # Execute automated navigation and obstacle avoidance test suite
  python3 src/autonomous_nav_stack/tests/test_navigation_evaluation.py --trials 50
  ```

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Assessment criteria go here.

## ➡️ Next Steps & Degree Pathway
- **Curriculum Hub:** [[Specialization Branches|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[Specialization Branches|Block 26 - Specialization A1]] and Course 2 binds to [[Specialization Branches|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[Specialization Branches|Block 29 - Specialization B1]] and Course 2 binds to [[Specialization Branches|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]]

- **Sequential Flow:** [[T08 - Quantum Information and Computing|← Quantum Information and Computing]] | [[00 - Start Here|Start Here]] | [[T10 - Full-Stack and Product Engineering|Full-Stack and Product Engineering →]]
