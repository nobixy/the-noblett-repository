---
block_id: "Block 27a"
stage: "05 - Year 4"
title: "Drone Lab: Flight Stack, ROS 2 and SITL"
category: "core"
subject: "Robotics"
term: "Year 4 Spring"
status: not-started
prerequisites:
  - "B04a - Differential Equations Bridge"
  - "B15a - Signals and Systems Bridge"
  - "B16a - Maker Lab 4 - Raspberry Pi and Embedded Linux"
  - "B24a - Applied Cryptography and Protocol Security"
hours_estimate: 100
hours_actual: 0
primary_resource: "PX4 user guide (SITL + Gazebo + ROS 2) + Crazyswarm2 + MIT VNAV (free); one Crazyflie or DIY ESP-Drone"
milestone: "Your ROS 2 node flies PX4 SITL survey missions 10/10 (3 vehicles in sim); one real micro-drone flies a scripted indoor pattern; every failsafe triggered and logged"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 27a — Drone Lab: Flight Stack, ROS 2 and SITL

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Hardware Index|Hardware Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 Spring
> - **Estimated Hours:** ~100 hrs
> - **Status:** `not-started`
> - **Primary Resource:** PX4 user guide (SITL + Gazebo + ROS 2) + Crazyswarm2 + MIT VNAV (free); one Crazyflie or DIY ESP-Drone
> - **Key Milestone:** Your ROS 2 node flies PX4 SITL survey missions 10/10 (3 vehicles in sim); one real micro-drone flies a scripted indoor pattern; every failsafe triggered and logged
> - **Added by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
The last Maker Lab and the on-ramp to the capstone: an open-source flight stack, ROS 2, simulation, and one small real drone. Everything here is sim-first: PX4 and ArduPilot both run software-in-the-loop on your Arch PC, and Crazyswarm2 simulates Crazyflie swarms, so most of the learning is free.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B04a - Differential Equations Bridge|Differential Equations Bridge]]
- [[B15a - Signals and Systems Bridge|Signals and Systems Bridge]]
- [[B16a - Maker Lab 4 - Raspberry Pi and Embedded Linux|Maker Lab 4]]
- [[B24a - Applied Cryptography and Protocol Security|Applied Cryptography]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Quadrotor dynamics and cascaded control (rate → attitude → position); PID tuning from logs.
- [ ] State estimation: complementary filter → EKF; PX4's EKF2; IMU, barometer, optical flow, range sensors.
- [ ] PX4 architecture (uORB, modules), MAVLink, QGroundControl (ArduPilot SITL as a second stack is optional since DR-006).
- [ ] **Digital-twin primer (DR-006):** turn a real neighborhood into a Gazebo world from OpenStreetMap buildings + USGS 3DEP elevation; fly the survey mission there; plan around buildings with A* on a 3D grid. Optional: Unreal + Cesium for Unreal + Cosys-AirSim if your GPU can take it.
- [ ] **Failure injection (DR-006):** PX4 failure injection (`SYS_FAILURE_EN`) to switch off GPS or the data link in SITL and watch the failsafes.
- [ ] ROS 2 (Lyrical Luth LTS): nodes, topics, services, actions, tf2, launch files, rosbag; the PX4–ROS 2 bridge (uXRCE-DDS) and offboard control.
- [ ] Multi-vehicle SITL in Gazebo; Crazyswarm2 and CrazySim for Crazyflie swarms; gym-pybullet-drones for learning-based control.
- [ ] GPS-denied navigation basics: optical flow + ToF (Crazyflie Flow deck), visual-inertial odometry overview (MIT VNAV).
- [ ] Safety: geofence, data-link-loss and RC-loss failsafes, battery failsafe, kill switch, pre-flight checklist, LiPo charging and storage, prop safety, netted indoor flight area.
- [ ] Rules before any outdoor flight: pass the FAA TRUST test; see the Capstone's Regulations & Ethics section.

---

## 🛠️ Build Requirement
1. **SITL:** PX4 in Gazebo controlled by your ROS 2 node flies a lawn-mower survey pattern; then 3 vehicles at once.
2. **Real micro-drone:** one Crazyflie (or an ESP-Drone you build) flies a scripted hover → square → land indoors with optical flow; retune one PID loop from logged step responses.
3. **Digital-twin world:** the same SITL survey flown in your OSM + 3DEP Gazebo world, rerouting around one building you add mid-flight.
4. **Failsafes:** trigger every failsafe in SITL and the link-loss and low-battery ones on hardware; log each.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> 10/10 SITL missions; the real drone flies the scripted pattern 5 times in a row; step responses and failsafe logs in your notes; TRUST certificate in hand before any outdoor flight.

---

## 🎓 Coursera Plus companions (DR-006, 2026-10-09)
- *Introduction to Self-Driving Cars*, *State Estimation and Localization for Self-Driving Cars* and *Motion Planning for Self-Driving Cars* (University of Toronto; all included in Coursera Plus as of 2026-10-09). The estimation course is the best primer for EKF/GPS-denied work; the planning course covers A*, lattice and dynamic replanning. Take them in place of the optional ArduPilot second stack.
- Map data and simulators for the twin: openstreetmap.org/copyright (ODbL), apps.nationalmap.gov/downloader/ (USGS 3DEP, public domain), gazebosim.org/docs/latest/getstarted/, cosys-lab.github.io/Cosys-AirSim/, cesium.com/learn/unreal/, docs.px4.io/main/en/debug/failure_injection.html.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- PX4 user guide (free): docs.px4.io/main/en/; Gazebo SITL: …/sim_gazebo_gz/; multi-vehicle: …/simulation/multi-vehicle-simulation.html; ROS 2 guide: …/ros2/user_guide.html.
- ArduPilot SITL (free): ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html. QGroundControl (free): qgroundcontrol.com.
- ROS 2 docs (free): docs.ros.org.
- Crazyswarm2 (free): imrclab.github.io/crazyswarm2/; CrazySim (Crazyflie SITL in Gazebo): github.com/gtfactslab/CrazySim; Bitcraze getting started: bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/.
- gym-pybullet-drones (free): utiasdsl.github.io/gym-pybullet-drones/. MIT VNAV, Visual Navigation for Autonomous Vehicles (free materials): vnav.mit.edu. MIT Underactuated Robotics (free): underactuated.mit.edu.
- ESP-Drone (Espressif's open-source ESP32 drone): docs.espressif.com/projects/espressif-esp-drone/en/latest/.
- **Kit (💲, verified Oct 2026, store.bitcraze.io):** Crazyflie 2.1+ $240 alone; STEM drone bundle (Crazyflie 2.1+, Flow deck v2, Crazyradio 2.0) $320. Cheapest path: a DIY ESP-Drone from an ESP32-S3 board, coreless motors, a 1S LiPo and a printed frame ≈$40–70, or stay in SITL and buy hardware only for the Capstone.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Flight logs (PX4 ulog, Crazyflie logging) are the check; compare the tuned step response with your Block 4a/15a models.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- UPenn Aerial Robotics (Coursera) if it is open when you get here.
- ArduPilot instead of PX4 (both are fine; pick one for the Capstone).

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B27 - Intensive Cryptopals|← Cryptopals]] | [[00 - Start Here|Start Here]] | [[Specialization Branches|Specialization A, Course 2 →]]
