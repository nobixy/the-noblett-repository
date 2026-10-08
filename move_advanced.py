import os
import shutil

source_dir = "01 - Curriculum/Advanced/Specializations"
target_dir = "01 - Curriculum/EECS Core/Advanced"

os.makedirs(target_dir, exist_ok=True)

rename_map = {
    "Track 1 - AI and Machine Learning.md": "Deep AI and Machine Learning.md",
    "Track 2 - Systems and Performance.md": "Advanced Systems and Performance.md",
    "Track 3 - Security and Cryptography.md": "Advanced Security and Cryptography.md",
    "Track 4 - Graphics and Vision.md": "Advanced Graphics and Vision.md",
    "Track 5 - Programming Languages and Compilers.md": "Advanced Programming Languages and Compilers.md",
    "Track 6 - Computer Engineering.md": "Advanced Computer Engineering.md",
    "Track 7 - TinyML and Edge AI.md": "TinyML and Edge AI.md",
    "Track 8 - Rust for Systems Engineering and Formal Verification.md": "Rust for Systems Engineering.md",
    "Track 9 - Hardware-in-the-Loop Virtualization, Digital Twins and CPS.md": "Hardware-in-the-Loop Virtualization and Digital Twins.md",
    "Track 10 - Quantum Information and Computing.md": "Quantum Information and Computing.md",
    "Track 11 - Autonomous Robotics and Cyber-Physical Systems.md": "Autonomous Robotics.md",
    "Track 12 - Computational Biology.md": "Computational Biology and Bioinformatics.md",
    "Track 12 - Computational Biology and Bioinformatics.md": "Computational Biology and Bioinformatics.md",
    "Track 13 - Systems Formal Verification.md": "Systems Formal Verification.md",
    "Track 14 - Advanced Pure Mathematics.md": "Advanced Pure Mathematics.md",
    "Intensive Cryptopals or TLA+.md": "Intensive Cryptopals.md",
    "Capstone.md": "Magnum Opus Capstone.md"
}

for old_name, new_name in rename_map.items():
    old_path = os.path.join(source_dir, old_name)
    new_path = os.path.join(target_dir, new_name)
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"Moved {old_name} -> {new_name}")
    else:
        print(f"Skipped {old_name} (not found)")

if os.path.exists(os.path.join(source_dir, "Specializations Hub.md")):
    os.remove(os.path.join(source_dir, "Specializations Hub.md"))
    print("Deleted Specializations Hub.md")

# Remove directory if empty
try:
    os.rmdir(source_dir)
    print("Removed old specializations directory.")
except OSError:
    print("Could not remove old specializations directory (not empty).")
