#!/usr/bin/env python3
"""
Comprehensive Independent Victory Audit Runner
Auditor: victory_auditor_quality_pass
Vault: /home/noblixy/The Noblett Repository
"""

import sys
import subprocess
import time

def run_suite(name, script_path):
    print(f"\n========================================================")
    print(f"RUNNING INDEPENDENT AUDIT SUITE: {name}")
    print(f"========================================================")
    start = time.time()
    res = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    dur = time.time() - start
    print(res.stdout)
    if res.stderr:
        print("STDERR:\n", res.stderr)
    print(f"Exit code: {res.returncode} | Duration: {dur:.2f}s")
    return res.returncode == 0

def main():
    print("STARTING INDEPENDENT VICTORY AUDIT SUITE EXECUTION...")
    suites = [
        ("Link & Graph Integrity", ".agents/victory_auditor_quality_pass/audit_links_and_graph.py"),
        ("Formatting, Frontmatter & Structural Consistency", ".agents/victory_auditor_quality_pass/audit_formatting.py"),
        ("Stubs, Placeholders, Agent Artifacts & Deduplication", ".agents/victory_auditor_quality_pass/audit_stubs_and_duplicates.py"),
    ]
    
    results = {}
    for name, path in suites:
        success = run_suite(name, path)
        results[name] = success
        
    print("\n========================================================")
    print("INDEPENDENT AUDIT SUMMARY")
    print("========================================================")
    all_passed = True
    for name, success in results.items():
        status = "PASS" if success else "FAIL"
        if not success:
            all_passed = False
        print(f"  [{status}] {name}")
        
    print("--------------------------------------------------------")
    overall = "VICTORY CONFIRMED" if all_passed else "VICTORY REJECTED"
    print(f"OVERALL INDEPENDENT VERDICT: {overall}")
    print("========================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
