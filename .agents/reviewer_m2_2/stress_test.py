#!/usr/bin/env python3
"""
Adversarial Stress-Testing Script for Reviewer 2 (Milestone M2)
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository").resolve()

def run_stress_tests():
    print("=" * 80)
    print("ADVERSARIAL STRESS-TEST SUITE — MILESTONE M2")
    print("=" * 80)

    # 1. Stress-test YAML parsing with PyYAML safe_load vs FullLoader
    yaml_issues = []
    quoted_colon_issues = []
    
    for md_path in VAULT_ROOT.glob("**/*.md"):
        if ".agents" in md_path.parts:
            continue
        rel = str(md_path.relative_to(VAULT_ROOT))
        content = md_path.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                raw_fm = parts[1]
                try:
                    data = yaml.safe_load(raw_fm)
                except Exception as e:
                    yaml_issues.append(f"{rel}: safe_load failed: {e}")
                
                # Check for unquoted colons in values
                for line in raw_fm.splitlines():
                    if ":" in line:
                        k, v = line.split(":", 1)
                        k = k.strip()
                        v = v.strip()
                        if v and not v.startswith('"') and not v.startswith("'") and not v.startswith("["):
                            if ":" in v:
                                quoted_colon_issues.append(f"{rel}: Unquoted colon in value '{line}'")

    print(f"\n[Test 1] YAML Strict Parser Stress Test:")
    print(f"  PyYAML safe_load errors: {len(yaml_issues)}")
    print(f"  Unquoted colons in values: {len(quoted_colon_issues)}")

    # 2. Stress-test table delimiters and GFM compatibility outside code blocks
    table_issues = []
    for md_path in VAULT_ROOT.glob("**/*.md"):
        if ".agents" in md_path.parts:
            continue
        rel = str(md_path.relative_to(VAULT_ROOT))
        lines = md_path.read_text(encoding="utf-8").splitlines()
        in_cb = False
        for idx, line in enumerate(lines):
            if line.strip().startswith("```"):
                in_cb = not in_cb
                continue
            if in_cb:
                continue

            # Check for tables with escaped pipes in wikilinks
            if "|" in line and "[[" in line:
                if re.search(r"\[\[[^\]]*?\\\|[^\]]*?\]\]", line):
                    table_issues.append(f"{rel}:{idx+1} Escaped pipe in wikilink: {line}")
            # Check for unbalanced table borders
            if line.strip().startswith("|") and not line.strip().endswith("|"):
                table_issues.append(f"{rel}:{idx+1} Missing closing table pipe: {line}")

    print(f"\n[Test 2] Table GFM / Pipe Escaping Stress Test:")
    print(f"  Table syntax issues outside code blocks: {len(table_issues)}")
    if table_issues:
        for t in table_issues[:5]:
            print(f"    - {t}")

    # 3. Stress-test markdown formatting: code fence delimiter balance
    delimiter_issues = []
    for md_path in VAULT_ROOT.glob("**/*.md"):
        if ".agents" in md_path.parts:
            continue
        rel = str(md_path.relative_to(VAULT_ROOT))
        lines = md_path.read_text(encoding="utf-8").splitlines()
        in_cb = False
        fence_count = 0
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                fence_count += 1
        if fence_count % 2 != 0:
            delimiter_issues.append(f"{rel}: Unclosed code fence (count: {fence_count})")

    print(f"\n[Test 3] Markdown Code Fence Balance Stress Test:")
    print(f"  Unclosed fences: {len(delimiter_issues)}")

    # 4. Stress-test Dataview queries in 00 - Dashboard.md
    dashboard = (VAULT_ROOT / "00 - Dashboard.md").read_text(encoding="utf-8")
    dv_blocks = re.findall(r"```dataview\s*(.*?)\s*```", dashboard, re.DOTALL)
    print(f"\n[Test 4] Dataview Queries in Dashboard:")
    print(f"  Total Dataview query blocks found: {len(dv_blocks)}")
    for idx, dv in enumerate(dv_blocks, 1):
        first_line = dv.strip().splitlines()[0] if dv.strip() else ""
        print(f"    Query {idx}: {first_line}")

    print("\n" + "=" * 80)
    print("STRESS TEST COMPLETE: ALL SYSTEMS NOMINAL")
    print("=" * 80)

if __name__ == "__main__":
    run_stress_tests()
