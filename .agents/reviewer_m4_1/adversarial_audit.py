import re
import sys
from pathlib import Path

vault_root = Path("/home/noblixy/The Noblett Repository")

target_f27 = [
    "01 - Curriculum/Year 1 - Fundamentals/01 - CS61A.md",
    "01 - Curriculum/Year 1 - Fundamentals/02 - Calculus I.md",
    "01 - Curriculum/Year 1 - Fundamentals/03 - Physics I.md",
    "01 - Curriculum/Year 1 - Fundamentals/04 - Nand2Tetris.md",
    "01 - Curriculum/Year 1 - Fundamentals/05 - SICP.md",
    "01 - Curriculum/Year 1 - Fundamentals/06 - C Fluency.md",
    "01 - Curriculum/Year 1 - Fundamentals/07 - Multivariable Calculus.md",
    "01 - Curriculum/Year 1 - Fundamentals/08 - Physics II.md",
    "01 - Curriculum/Year 2 - Systems/09 - Computer Systems.md",
    "01 - Curriculum/Year 2 - Systems/12 - Interpreters.md",
    "01 - Curriculum/Year 2 - Systems/14 - Computer Architecture.md",
    "01 - Curriculum/Year 3 - Depth/19 - Networking.md",
    "01 - Curriculum/Year 4 - Specialization/27 - Intensive Cryptopals or TLA+.md"
]

target_f28 = [
    "01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md",
    "01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md",
    "01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md"
]

target_f29 = [
    "01 - Curriculum/Year 4 - Specialization/24 - Theory of Computation.md"
]

all_targets = target_f27 + target_f28 + target_f29

print("=== STARTING ADVERSARIAL AUDIT FOR M4 DELIVERABLES ===")
failures = []

for rel in all_targets:
    p = vault_root / rel
    if not p.exists():
        failures.append(f"MISSING FILE: {rel}")
        continue
    content = p.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    # 1. Unclosed $$
    dd_count = content.count("$$")
    if dd_count % 2 != 0:
        failures.append(f"{rel}: Odd number of $$ markers ({dd_count}), unclosed math environment!")
        
    # 2. Check for leftover placeholder patterns
    stubs = re.findall(r"\*(?:\(Atomic notes.*?\)|TODO|TBD|Placeholder)\*", content, re.IGNORECASE)
    if stubs:
        failures.append(f"{rel}: Leftover stubs found: {stubs}")
        
    # 3. Check for tombstone in Study Notes section
    study_notes = re.search(r"## 📝 Study Notes[^\n]*\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if not study_notes:
        failures.append(f"{rel}: Missing Study Notes section!")
    else:
        sn_text = study_notes.group(1)
        if r"\blacksquare" not in sn_text and "■" not in sn_text:
            failures.append(f"{rel}: Missing tombstone \\blacksquare in Study Notes!")
            
    # Track code fence lines
    in_code = False
    code_lines = set()
    for l_no, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            code_lines.add(l_no)
        elif in_code:
            code_lines.add(l_no)

    # 4. Check for odd-space list indentation
    for line_idx, line in enumerate(lines, start=1):
        if line_idx in code_lines:
            continue
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if m:
            indent = len(m.group(1))
            if indent % 2 != 0:
                failures.append(f"{rel}:{line_idx}: Odd-space indentation ({indent} spaces): '{line.strip()}'")

# Landmark research papers check
landmark_blocks = {
    "01 - Curriculum/Year 2 - Systems/09 - Computer Systems.md": ["Lampson", "Gharachorloo"],
    "01 - Curriculum/Year 2 - Systems/14 - Computer Architecture.md": ["Patterson", "Jouppi", "Tullsen"],
    "01 - Curriculum/Year 3 - Depth/19 - Networking.md": ["Clark"],
    "01 - Curriculum/Year 4 - Specialization/27 - Intensive Cryptopals or TLA+.md": ["Regev"]
}

for rel, expected_authors in landmark_blocks.items():
    p = vault_root / rel
    content = p.read_text(encoding="utf-8")
    if "### 📄 Landmark Research Papers" not in content:
        failures.append(f"{rel}: Missing '### 📄 Landmark Research Papers' header!")
    for author in expected_authors:
        if author not in content:
            failures.append(f"{rel}: Missing expected landmark paper author '{author}'!")

# Bridge block proofs check (must have 3 proofs each)
bridge_expected = {
    "01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md": [
        "Abel's Theorem", "Matrix Exponential", "Picard-Lindelöf"
    ],
    "01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md": [
        "Thévenin-Norton", "KCL/KVL", "RLC"
    ],
    "01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md": [
        "DTFT Convolution-Multiplication Duality", "Nyquist-Shannon", "Z-Transform"
    ]
}

for rel, proofs in bridge_expected.items():
    p = vault_root / rel
    content = p.read_text(encoding="utf-8")
    sn = re.search(r"## 📝 Study Notes[^\n]*\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if not sn:
        failures.append(f"{rel}: Missing study notes")
        continue
    sn_text = sn.group(1)
    # count tombstones in bridge block
    tombstones = sn_text.count(r"\blacksquare") + sn_text.count("■")
    if tombstones < 3:
        failures.append(f"{rel}: Has only {tombstones} tombstones (expected 3)!")
    for prf in proofs:
        if prf.lower() not in sn_text.lower():
            failures.append(f"{rel}: Missing expected proof '{prf}'!")

print(f"Audit completed. Failures detected: {len(failures)}")
for f in failures:
    print(f"  FAIL: {f}")
if not failures:
    print("ALL 17 FILES PASSED ADVERSARIAL SYNTAX, INDENTATION, MATH, AND LANDMARK INTEGRITY CHECKS!")
