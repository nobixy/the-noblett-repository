#!/usr/bin/env python3
"""
Independent Victory Audit: Stubs, Agent Artifacts & Content Deduplication
Auditor: victory_auditor_quality_pass
Vault: /home/noblixy/The Noblett Repository
"""

import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository")
EXCLUDE_DIRS = {".agents", ".obsidian", ".git"}

def get_vault_notes():
    notes = {}
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if f.endswith(".md"):
                p = Path(root) / f
                rel = p.relative_to(VAULT_ROOT)
                notes[str(rel)] = p
    return notes

def scan_stubs_and_artifacts(notes):
    stub_patterns = [
        (r"\bTODO\b", "TODO marker"),
        (r"\bTBD\b", "TBD marker"),
        (r"\bFIXME\b", "FIXME marker"),
        (r"\bWIP\b", "WIP marker"),
        (r"\bplaceholder\b", "Placeholder keyword"),
        (r"\bstub\b", "Stub keyword"),
        (r"\bto be determined\b", "To be determined"),
        (r"\bto be implemented\b", "To be implemented"),
        (r"\bteamwork_preview_\w+\b", "Agent worker ID leak"),
        (r"\.agents/", "Agent directory path leak"),
    ]
    
    # Parenthetical directives that were typical placeholders in the original vault:
    # e.g. "*(Atomic notes, problem set proofs...)*"
    directive_pattern = re.compile(r"\*\([A-Z][^)]*(?:notes|proofs|explain|fill in|details)[^)]*\)\*", re.IGNORECASE)
    
    findings = []
    
    for rel, p in notes.items():
        is_template = "08 - Templates" in rel
        is_gap_analysis = "Baseline Gap Analysis" in rel
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
            
        lines = content.splitlines()
        for idx, line in enumerate(lines, 1):
            if not is_template:
                # Check directive stubs
                if directive_pattern.search(line):
                    findings.append((rel, idx, "Parenthetical directive stub", line.strip()))
                    
                # Check keywords
                for pat, label in stub_patterns:
                    if re.search(pat, line, re.IGNORECASE):
                        # Filter false positives:
                        # 1. Technical context for stub (RPC, client stub, etc.)
                        if pat == r"\bstub\b" and any(k in line.lower() for k in ["rpc", "client stub", "server stub", "stub compiler", "skeleton"]):
                            continue
                        # 2. Retrospective discussion in Baseline Gap Analysis describing what previous state lacked
                        if is_gap_analysis and ("flesh out placeholder" in line.lower() or "placeholder blocks" in line.lower()):
                            continue
                        findings.append((rel, idx, label, line.strip()))
            else:
                # Inside templates, check only for agent leaks
                for pat in [r"\bteamwork_preview_\w+\b", r"\.agents/"]:
                    if re.search(pat, line):
                        findings.append((rel, idx, "Agent leak in template", line.strip()))
                        
    return findings

def scan_content_duplication(notes):
    """
    Check pairwise substantive text overlap across non-template notes.
    Extract substantive paragraphs (>= 30 words) outside navigation footers.
    """
    paragraph_map = defaultdict(list)
    
    for rel, p in notes.items():
        if "08 - Templates" in rel:
            continue
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Strip frontmatter
        if content.startswith("---\n"):
            end = content.find("\n---\n", 4)
            if end != -1:
                content = content[end + 5:]
                
        # Split into paragraphs and strip navigation footers
        paras = re.split(r"\n\s*\n", content)
        for para in paras:
            # Skip navigation sections
            if "## 🧭 Navigation" in para or "## 🧭 Navigation & Degree Pathway" in para:
                continue
            if "Curriculum Hub:" in para and "Degree Assignment:" in para:
                continue
            # Clean paragraph
            cleaned = re.sub(r"[#*`>|\[\]\$-]", " ", para)
            words = [w.lower() for w in re.findall(r"\b[a-zA-Z]{3,}\b", cleaned)]
            if len(words) >= 30:
                fingerprint = " ".join(words[:25])
                paragraph_map[fingerprint].append((rel, " ".join(words[:15]) + "..."))
                
    duplicate_paras = {k: v for k, v in paragraph_map.items() if len(v) > 1}
    
    # Also verify specific M3 deduplication milestones:
    # 1. Blocks 26, 28, 29, 31 specialization matrix deduplication
    spec_matrix_duplicates = []
    matrix_notes = [
        "01 - Curriculum/Year 4 - Specialization/26 - Specialization A1.md",
        "01 - Curriculum/Year 4 - Specialization/28 - Specialization A2.md",
        "01 - Curriculum/Year 4 - Specialization/29 - Specialization B1.md",
        "01 - Curriculum/Year 5 - MEng/31 - Specialization B2.md"
    ]
    for mn in matrix_notes:
        with open(notes[mn], "r", encoding="utf-8") as f:
            c = f.read()
        # Should link to Specializations Hub and NOT have a giant table duplicating all 11 tracks
        if "[[Specializations Hub]]" not in c and "[[01 - Curriculum/Specializations/Specializations Hub|Specializations Hub]]" not in c:
            spec_matrix_duplicates.append(f"{mn} missing link to Specializations Hub")
        if c.count("Track 1") > 2 and c.count("Track 11") > 2:
            spec_matrix_duplicates.append(f"{mn} appears to retain duplicate 11-track full table")
            
    # 2. Mindset deduplication (how-i-study.md vs Mindset Hub.md)
    mindset_issues = []
    with open(notes["how-i-study.md"], "r", encoding="utf-8") as f:
        his = f.read()
    if "[[09 - Mindset & Habits/Mindset Hub|Mindset Hub]]" not in his and "[[Mindset Hub]]" not in his:
        mindset_issues.append("how-i-study.md does not cross-reference Mindset Hub")
        
    return duplicate_paras, spec_matrix_duplicates, mindset_issues

def main():
    notes = get_vault_notes()
    print(f"Total markdown notes: {len(notes)}")
    
    print("\n--- 1. Stub and Agent Artifact Census ---")
    stubs = scan_stubs_and_artifacts(notes)
    print(f"Total stubs/artifacts found: {len(stubs)}")
    if stubs:
        for rel, line_no, label, line in stubs:
            print(f"  [FAIL] {rel}:{line_no} [{label}]: {line[:80]}")
    else:
        print("  PASS: 0 placeholder, TODO, directive stubs, or agent artifacts found across all notes!")
        
    print("\n--- 2. Content Deduplication Audit ---")
    dup_paras, spec_mat, mindset = scan_content_duplication(notes)
    
    # Filter duplicate paras: if duplicates are standard navigation or license/disclaimers
    substantive_dups = []
    for fp, occurrences in dup_paras.items():
        files = {o[0] for o in occurrences}
        if len(files) > 1:
            substantive_dups.append((files, occurrences[0][1]))
            
    print(f"Duplicate substantive paragraphs across different files: {len(substantive_dups)}")
    if substantive_dups:
        for files, sample in substantive_dups:
            print(f"  [FAIL] Duplicate text between {files}: '{sample}'")
    else:
        print("  PASS: 0 duplicate substantive paragraphs detected across different notes!")
        
    if spec_mat:
        print(f"  [FAIL] Specialization matrix issues: {spec_mat}")
    else:
        print("  PASS: Specialization matrices cleanly consolidated into Specializations Hub!")
        
    if mindset:
        print(f"  [FAIL] Mindset issues: {mindset}")
    else:
        print("  PASS: Mindset and study guidelines cleanly consolidated and cross-referenced!")
        
    passed = len(stubs) == 0 and len(substantive_dups) == 0 and len(spec_mat) == 0 and len(mindset) == 0
    print(f"\nSTUBS & DEDUPLICATION AUDIT VERDICT: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
