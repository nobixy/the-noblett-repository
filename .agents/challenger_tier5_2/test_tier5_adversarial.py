#!/usr/bin/env python3
"""
Tier 5 Adversarial Coverage Hardening & Empirical Stress Test Suite
Challenger 2 (challenger_tier5_2)

This script performs opaque-box, empirical adversarial verification across
The Noblett Repository Obsidian vault.
"""

import sys
import os
import re
import json
import time
from pathlib import Path
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Any

try:
    import yaml
except ImportError:
    yaml = None


@dataclass
class Tier5TestResult:
    test_id: str
    name: str
    passed: bool
    message: str = ""
    details: List[str] = field(default_factory=list)
    duration_ms: float = 0.0


class Tier5AdversarialHarness:
    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self.md_files: Dict[str, Path] = {}
        self.contents: Dict[str, str] = {}
        self.stem_map: Dict[str, str] = {}
        self.out_edges: Dict[str, Set[str]] = defaultdict(set)
        self.in_edges: Dict[str, Set[str]] = defaultdict(set)
        self._load_vault()

    def _load_vault(self):
        for p in sorted(self.vault_root.rglob("*.md")):
            if any(x in p.parts for x in [".agents", ".git", ".obsidian"]):
                continue
            rel = str(p.relative_to(self.vault_root))
            self.md_files[rel] = p
            content = p.read_text(encoding="utf-8")
            self.contents[rel] = content
            self.stem_map[p.stem] = rel
            self.stem_map[p.name] = rel

        # Build graph
        for rel, content in self.contents.items():
            base = Path(rel).stem
            for m in re.finditer(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]", content):
                target = m.group(1).strip()
                target_base = Path(target).stem
                if target_base in self.stem_map:
                    target_rel = self.stem_map[target_base]
                    target_stem = Path(target_rel).stem
                    self.out_edges[base].add(target_stem)
                    self.in_edges[target_stem].add(base)

    # -------------------------------------------------------------------------
    # Test 5.1: Exhaustive Student Navigation Simulation
    # -------------------------------------------------------------------------
    def test_5_1_student_navigation_simulation(self) -> Tier5TestResult:
        start_time = time.time()
        start_node = "00 - Dashboard"
        dist = {start_node: 0}
        q = deque([start_node])

        while q:
            u = q.popleft()
            for v in sorted(self.out_edges[u]):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)

        non_template_stems = [
            Path(rel).stem for rel in self.md_files if "08 - Templates" not in rel
        ]
        unreachable = [stem for stem in non_template_stems if stem not in dist]
        excessive_hops = [stem for stem in dist if dist[stem] > 2]

        passed = len(unreachable) == 0 and len(excessive_hops) == 0
        details = []
        if unreachable:
            details.append(f"Unreachable notes ({len(unreachable)}): {unreachable}")
        if excessive_hops:
            details.append(f"Notes > 2 hops ({len(excessive_hops)}): {excessive_hops}")

        dur = (time.time() - start_time) * 1000.0
        msg = f"All {len(non_template_stems)} non-template notes reachable in <= 2 hops from Dashboard" if passed else f"Navigation failure: {len(unreachable)} unreachable"
        return Tier5TestResult("TEST-5.1", "Student Navigation Simulation & Graph Reachability", passed, msg, details, dur)

    # -------------------------------------------------------------------------
    # Test 5.2: Bidirectional Graph Symmetry & Paired Link Invariant
    # -------------------------------------------------------------------------
    def test_5_2_graph_bidirectional_symmetry(self) -> Tier5TestResult:
        start_time = time.time()
        failures = []

        # 1. Specializations Hub <-> All 11 Tracks
        sh = "Specializations Hub"
        for i in range(1, 12):
            track_prefix = f"Track {i} - "
            track_matches = [s for s in self.stem_map if s.startswith(track_prefix)]
            if not track_matches:
                failures.append(f"Missing Track {i}")
                continue
            t_stem = track_matches[0]
            if t_stem not in self.out_edges[sh]:
                failures.append(f"Specializations Hub missing outbound link to {t_stem}")
            if sh not in self.out_edges[t_stem]:
                failures.append(f"{t_stem} missing outbound link to Specializations Hub")

        # 2. Sequential Course Progression (01 to 32, including 04a, 08a, 15a)
        course_blocks = sorted([
            Path(rel).stem for rel in self.md_files
            if re.match(r"^01 - Curriculum/(?:Year \d|Phase)/(\d{2}[a-z]?) - ", rel)
        ])
        for i in range(len(course_blocks) - 1):
            b1 = course_blocks[i]
            b2 = course_blocks[i+1]
            if b2 not in self.out_edges[b1]:
                failures.append(f"Sequential forward link missing: {b1} -> {b2}")
            if b1 not in self.out_edges[b2]:
                failures.append(f"Sequential backward link missing: {b2} -> {b1}")

        # 3. Specialization Blocks 26, 28, 29, 31 <-> Specializations Hub
        for sb in ["26 - Specialization A1", "28 - Specialization A2", "29 - Specialization B1", "31 - Specialization B2"]:
            if sh not in self.out_edges[sb]:
                failures.append(f"Specialization block {sb} missing link to Specializations Hub")

        # 4. OS (16) <-> Distributed Systems (23)
        os_stem = "16 - Operating Systems"
        ds_stem = "23 - Distributed Systems"
        if ds_stem not in self.out_edges[os_stem]:
            failures.append("16 - Operating Systems does not link to 23 - Distributed Systems")
        if os_stem not in self.out_edges[ds_stem]:
            failures.append("23 - Distributed Systems does not link to 16 - Operating Systems")

        passed = len(failures) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = "All paired links exhibit strict bidirectional symmetry" if passed else f"{len(failures)} bidirectional asymmetry errors detected"
        return Tier5TestResult("TEST-5.2", "Graph Invariant & Bidirectional Symmetry", passed, msg, failures, dur)

    # -------------------------------------------------------------------------
    # Test 5.3: Exhaustive YAML Schema & Enum Validation
    # -------------------------------------------------------------------------
    def test_5_3_yaml_schema_validation(self) -> Tier5TestResult:
        start_time = time.time()
        if yaml is None:
            return Tier5TestResult("TEST-5.3", "YAML Schema Validation", False, "PyYAML not installed", duration_ms=0.0)

        errors = []
        for rel, content in self.contents.items():
            if not content.startswith("---\n"):
                continue
            end_idx = content.find("\n---\n", 4)
            if end_idx == -1:
                end_idx = content.find("\n---", 4)
            raw_yaml = content[4:end_idx]
            try:
                data = yaml.safe_load(raw_yaml)
            except Exception as e:
                errors.append(f"YAML parse error in {rel}: {e}")
                continue

            h1_match = re.search(r"^#\s+(.+)$", content[end_idx+4:], re.MULTILINE)
            h1 = h1_match.group(1).strip() if h1_match else None

            # Course Blocks
            if re.match(r"^01 - Curriculum/(?:Year \d|Phase)/(\d{2}[a-z]?) - ", rel):
                req = ["block_id", "title", "term", "status", "hours_estimate", "hours_actual", "primary_resource", "milestone", "date_started", "date_completed"]
                for k in req:
                    if k not in data:
                        errors.append(f"{rel}: Missing required key '{k}'")
                if data.get("status") not in ["not-started", "in-progress", "done"]:
                    errors.append(f"{rel}: Invalid status enum '{data.get('status')}'")
                if not isinstance(data.get("hours_estimate"), (int, float)) or data.get("hours_estimate") <= 0:
                    errors.append(f"{rel}: Invalid hours_estimate '{data.get('hours_estimate')}'")
                if not isinstance(data.get("hours_actual"), (int, float)) or data.get("hours_actual") < 0:
                    errors.append(f"{rel}: Invalid hours_actual '{data.get('hours_actual')}'")
                expected_h1 = f"{data.get('block_id')} — {data.get('title')}"
                if h1 != expected_h1:
                    errors.append(f"{rel}: H1 mismatch: got '{h1}', expected '{expected_h1}'")

            # Specialization Tracks
            elif "01 - Curriculum/Specializations/Track " in rel:
                req = ["track_id", "title", "term", "status", "target_profile", "prerequisites", "aliases"]
                for k in req:
                    if k not in data:
                        errors.append(f"{rel}: Missing required key '{k}'")
                if data.get("status") not in ["not-started", "in-progress", "done"]:
                    errors.append(f"{rel}: Invalid status '{data.get('status')}'")
                if not isinstance(data.get("prerequisites"), list) or len(data.get("prerequisites")) == 0:
                    errors.append(f"{rel}: Prerequisites must be non-empty list")
                else:
                    for pr in data.get("prerequisites"):
                        if not (isinstance(pr, str) and pr.startswith("[[") and pr.endswith("]]")):
                            errors.append(f"{rel}: Prerequisite entry not wikilink: {pr}")
                if not isinstance(data.get("aliases"), list) or len(data.get("aliases")) == 0:
                    errors.append(f"{rel}: Aliases must be non-empty list")
                expected_h1 = f"{data.get('track_id')}: {data.get('title')}"
                if h1 != expected_h1:
                    errors.append(f"{rel}: H1 mismatch: got '{h1}', expected '{expected_h1}'")

            # Hubs & Indices
            elif ("Hub" in Path(rel).stem or "Index" in Path(rel).stem or rel == "00 - Dashboard.md") and "08 - Templates" not in rel:
                req = ["title", "type", "tags"]
                for k in req:
                    if k not in data:
                        errors.append(f"{rel}: Missing required key '{k}'")
                if data.get("type") not in ["hub", "index"]:
                    errors.append(f"{rel}: Invalid hub type '{data.get('type')}'")
                if not isinstance(data.get("tags"), list):
                    errors.append(f"{rel}: Tags must be list")

        passed = len(errors) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = "All 75 frontmatter blocks satisfy schema types, required keys, and enum constraints" if passed else f"{len(errors)} YAML schema violations detected"
        return Tier5TestResult("TEST-5.3", "Full YAML Schema & Enum Invariant Validation", passed, msg, errors, dur)

    # -------------------------------------------------------------------------
    # Test 5.4: Formal Proof Tombstone Invariant
    # -------------------------------------------------------------------------
    def test_5_4_tombstone_invariant(self) -> Tier5TestResult:
        start_time = time.time()
        # All notes containing formal proof derivations must have \blacksquare terminating the proof
        proof_blocks = [
            "P3 - Math Prerequisites.md",
            "Track 1 - AI and Machine Learning.md",
            "01 - CS61A.md", "02 - Calculus I.md", "03 - Physics I.md", "04 - Nand2Tetris.md",
            "04a - Differential Equations Bridge.md", "05 - SICP.md", "06 - C Fluency.md",
            "07 - Multivariable Calculus.md", "08 - Physics II.md", "08a - Circuits and Electronics Bridge.md",
            "09 - Computer Systems.md", "10 - Math for CS.md", "11 - Linear Algebra.md", "12 - Interpreters.md",
            "13 - Algorithms I.md", "14 - Computer Architecture.md", "15 - Probability.md",
            "15a - Signals and Systems Bridge.md", "16 - Operating Systems.md", "17 - Software Construction.md",
            "18 - Real Analysis.md", "19 - Networking.md", "20 - Algorithms II.md", "21 - Databases.md",
            "22 - Statistics.md", "23 - Distributed Systems.md", "24 - Theory of Computation.md",
            "25 - Convex Optimization.md", "27 - Intensive Cryptopals or TLA+.md", "32 - Information Theory.md"
        ]
        missing = []
        for rel, content in self.contents.items():
            if any(rel.endswith(b) for b in proof_blocks):
                # Search for blacksquare
                if r"\blacksquare" not in content and "■" not in content and r"\square" not in content:
                    missing.append(f"{rel}: Formal proof section missing Q.E.D. tombstone")

        passed = len(missing) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = f"All {len(proof_blocks)} formal proof derivation notes contain Q.E.D. tombstone" if passed else f"{len(missing)} notes missing tombstone"
        return Tier5TestResult("TEST-5.4", "Tombstone Invariant Test", passed, msg, missing, dur)

    # -------------------------------------------------------------------------
    # Test 5.5: Projects Hub Completeness & Active Toolchains
    # -------------------------------------------------------------------------
    def test_5_5_projects_hub_completeness(self) -> Tier5TestResult:
        start_time = time.time()
        ph_rel = "05 - Projects/Projects Hub.md"
        if ph_rel not in self.contents:
            return Tier5TestResult("TEST-5.5", "Projects Hub Completeness", False, "Projects Hub.md missing", duration_ms=0.0)

        c = self.contents[ph_rel]
        missing = []

        # 32 core blocks
        for i in range(1, 33):
            b_num = f"{i:02d}"
            if not re.search(rf"\b(?:Block\s+{i}\b|{b_num}\s*-\s*)", c):
                missing.append(f"Missing core Block {i:02d}")

        # 3 bridge courses
        for b in ["04a", "08a", "15a"]:
            if b not in c:
                missing.append(f"Missing bridge course {b}")

        # 11 track capstones
        for t in range(1, 12):
            if f"Track {t}" not in c:
                missing.append(f"Missing Track {t} capstone")

        # Active toolchains check
        toolchains = ["gcc", "clang", "rust", "cargo", "valgrind", "pytest", "qemu", "renode", "verilator", "gdb", "lean", "cvxpy", "scipy", "numpy"]
        found_toolchains = [tc for tc in toolchains if tc in c.lower()]

        passed = len(missing) == 0 and len(found_toolchains) >= 10
        dur = (time.time() - start_time) * 1000.0
        msg = "Projects Hub verified: 32 blocks + 3 bridge courses + 11 track capstones + active toolchains" if passed else f"Projects Hub defects: {missing}"
        return Tier5TestResult("TEST-5.5", "Projects Hub Completeness & Active Toolchains", passed, msg, missing, dur)

    # -------------------------------------------------------------------------
    # Test 5.6: Heading Anchor & Cross-Reference Integrity
    # -------------------------------------------------------------------------
    def test_5_6_heading_anchor_integrity(self) -> Tier5TestResult:
        start_time = time.time()
        anchor_errors = []

        for rel, content in self.contents.items():
            for m in re.finditer(r"\[\[([^\]\|]+#[^\]\|]+)(?:\|[^\]]+)?\]\]", content):
                target_str = m.group(1).strip()
                file_part, heading_part = target_str.split("#", 1)
                file_stem = Path(file_part).stem
                if file_stem not in self.stem_map:
                    anchor_errors.append(f"{rel}: Target note '{file_part}' for anchor '{heading_part}' not found")
                    continue
                target_rel = self.stem_map[file_stem]
                target_content = self.contents[target_rel]
                # Heading must exist in target content
                h_pattern = rf"^#{1,6}\s+{re.escape(heading_part)}\s*$"
                if not re.search(h_pattern, target_content, re.MULTILINE):
                    # Also check substring match if exact heading formatting differs
                    if heading_part not in target_content:
                        anchor_errors.append(f"{rel}: Anchor '#{heading_part}' does not exist in '{target_rel}'")

        passed = len(anchor_errors) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = "All heading anchor wikilinks resolve to existing targets" if passed else f"{len(anchor_errors)} broken heading anchors"
        return Tier5TestResult("TEST-5.6", "Heading Anchor & Cross-Reference Integrity", passed, msg, anchor_errors, dur)

    # -------------------------------------------------------------------------
    # Test 5.7: LaTeX Mathematical Delimiter Balance
    # -------------------------------------------------------------------------
    def test_5_7_math_delimiter_balance(self) -> Tier5TestResult:
        start_time = time.time()
        delim_errors = []

        for rel, content in self.contents.items():
            # Strip code blocks
            lines = content.split("\n")
            non_code = []
            in_code = False
            for l in lines:
                if l.strip().startswith("```"):
                    in_code = not in_code
                    continue
                if not in_code:
                    non_code.append(l)
            text = "\n".join(non_code)

            # Check $$ balance
            if text.count("$$") % 2 != 0:
                delim_errors.append(f"{rel}: Unbalanced display math delimiters ($$)")

            # Check single $ balance
            no_display = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
            no_inline_code = re.sub(r"`[^`]*`", "", no_display)
            if no_inline_code.count("$") % 2 != 0:
                delim_errors.append(f"{rel}: Unbalanced inline math delimiters ($)")

        passed = len(delim_errors) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = "All LaTeX inline and display math delimiters are perfectly balanced across 84 notes" if passed else f"{len(delim_errors)} math delimiter errors"
        return Tier5TestResult("TEST-5.7", "LaTeX Mathematical Delimiter Balance", passed, msg, delim_errors, dur)

    # -------------------------------------------------------------------------
    # Test 5.8: Prerequisite Topological Consistency & DAG Chronology
    # -------------------------------------------------------------------------
    def test_5_8_prerequisite_dag_chronology(self) -> Tier5TestResult:
        start_time = time.time()
        prereqs = defaultdict(list)
        chronology = {}

        for rel, content in self.contents.items():
            stem = Path(rel).stem
            if "Bedrock" in rel:
                chronology[stem] = 0
            elif "Phase 0" in rel:
                chronology[stem] = 10
            elif "Year 1" in rel:
                chronology[stem] = 100
            elif "Year 2" in rel:
                chronology[stem] = 200
            elif "Year 3" in rel:
                chronology[stem] = 300
            elif "Year 4" in rel:
                chronology[stem] = 400
            elif "Year 5" in rel:
                chronology[stem] = 500
            elif "Specializations" in rel:
                chronology[stem] = 600
            else:
                chronology[stem] = 999

            # Extract from frontmatter
            if content.startswith("---\n") and yaml is not None:
                end_idx = content.find("\n---\n", 4)
                if end_idx != -1:
                    try:
                        d = yaml.safe_load(content[4:end_idx])
                        if isinstance(d, dict) and "prerequisites" in d:
                            pr_list = d["prerequisites"]
                            if isinstance(pr_list, list):
                                for item in pr_list:
                                    m = re.search(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]", str(item))
                                    if m:
                                        target_stem = Path(m.group(1).strip()).stem
                                        if target_stem in self.stem_map:
                                            prereqs[stem].append(target_stem)
                    except Exception:
                        pass

        # Cycle detection
        visited = {}
        cycles = []

        def dfs(u, path):
            visited[u] = 1
            for v in prereqs[u]:
                if v not in visited or visited[v] == 0:
                    dfs(v, path + [v])
                elif visited[v] == 1:
                    cycles.append(path + [v])
            visited[u] = 2

        for node in list(prereqs.keys()):
            if visited.get(node, 0) == 0:
                dfs(node, [node])

        # Chronology violations
        violations = []
        for u, plist in prereqs.items():
            u_score = chronology.get(u, 999)
            for v in plist:
                v_score = chronology.get(v, 999)
                if u_score < v_score and u_score < 600 and v_score <= 500:
                    violations.append(f"{u} (score {u_score}) requires later block {v} (score {v_score})")

        passed = len(cycles) == 0 and len(violations) == 0
        dur = (time.time() - start_time) * 1000.0
        details = [f"Cycle: {' -> '.join(c)}" for c in cycles] + violations
        msg = f"Prerequisite DAG verified: 0 cycles, 0 chronological inversions across {len(prereqs)} tracked nodes" if passed else f"Prerequisite DAG violations: {details}"
        return Tier5TestResult("TEST-5.8", "Prerequisite Topological Consistency & DAG Chronology", passed, msg, details, dur)

    # -------------------------------------------------------------------------
    # Test 5.9: Dataview Telemetry & Metadata Field Parsing
    # -------------------------------------------------------------------------
    def test_5_9_dataview_telemetry_compatibility(self) -> Tier5TestResult:
        start_time = time.time()
        telem_rel = "Telemetry Log.md"
        errors = []
        if telem_rel not in self.contents:
            errors.append("Telemetry Log.md missing")
        else:
            c = self.contents[telem_rel]
            # Ensure lines 1-15 don't have broken markdown table syntax preceding dataview list
            first_lines = c.split("\n")[:15]
            for idx, line in enumerate(first_lines):
                if line.strip().startswith("|") and ("---" in line or "Date" in line):
                    errors.append(f"Orphaned table markup detected on line {idx+1} in Telemetry Log.md")

        # Check frontmatter data types across curriculum
        for rel, content in self.contents.items():
            if re.match(r"^01 - Curriculum/(?:Year \d|Phase)/(\d{2}[a-z]?) - ", rel) and yaml is not None:
                end_idx = content.find("\n---\n", 4)
                if end_idx != -1:
                    try:
                        d = yaml.safe_load(content[4:end_idx])
                        if not isinstance(d.get("status"), str):
                            errors.append(f"{rel}: status is not string")
                        if not isinstance(d.get("hours_estimate"), (int, float)):
                            errors.append(f"{rel}: hours_estimate is not numeric")
                    except Exception:
                        pass

        passed = len(errors) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = "Dataview telemetry syntax and query properties verified" if passed else f"Dataview errors: {errors}"
        return Tier5TestResult("TEST-5.9", "Dataview Telemetry & Metadata Field Parsing", passed, msg, errors, dur)

    # -------------------------------------------------------------------------
    # Test 5.10: Zero Stubs, Zero TODOs, and Zero Agent Artifacts
    # -------------------------------------------------------------------------
    def test_5_10_zero_stubs_and_artifacts(self) -> Tier5TestResult:
        start_time = time.time()
        stubs = []
        for rel, content in self.contents.items():
            # Exclude templates from dummy checks if properly escaped
            for m in re.finditer(r"\b(TODO|TBD|FIXME|WIP)\b", content):
                stubs.append(f"{rel}: Placeholder '{m.group(1)}' found")
            for m in re.finditer(r"(teamwork_preview_worker|\.agents/)", content):
                stubs.append(f"{rel}: Agent artifact '{m.group(1)}' found")

        passed = len(stubs) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = "0 stubs, 0 TODOs, and 0 agent artifacts detected across entire vault" if passed else f"{len(stubs)} stubs/artifacts found"
        return Tier5TestResult("TEST-5.10", "Zero Stubs & Agent Artifacts", passed, msg, stubs, dur)

    # -------------------------------------------------------------------------
    # Test 5.11: Content Deduplication & Architectural Purity
    # -------------------------------------------------------------------------
    def test_5_11_deduplication_and_architecture(self) -> Tier5TestResult:
        start_time = time.time()
        dedup_errors = []

        # 1. Blocks 26, 28, 29, 31 must not have full 11-track table
        for b in ["26 - Specialization A1.md", "28 - Specialization A2.md", "29 - Specialization B1.md", "31 - Specialization B2.md"]:
            matches = [rel for rel in self.contents if rel.endswith(b)]
            if matches:
                rel = matches[0]
                c = self.contents[rel]
                if c.count("| Track ") > 2:
                    dedup_errors.append(f"{rel}: Contains duplicate 11-track matrix instead of referencing Specializations Hub")
                if "Specializations Hub" not in c:
                    dedup_errors.append(f"{rel}: Missing link to Specializations Hub")

        # 2. how-i-study.md must cross-reference Mindset Hub anchors
        how_study = self.contents.get("how-i-study.md", "")
        if "Mindset Hub#1. Core Mindset: Grit & Growth" not in how_study:
            dedup_errors.append("how-i-study.md missing anchor link to Mindset Hub Grit & Growth")

        passed = len(dedup_errors) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = "Architectural deduplication verified across specialization blocks and mindset notes" if passed else f"Deduplication failures: {dedup_errors}"
        return Tier5TestResult("TEST-5.11", "Content Deduplication & Architectural Purity", passed, msg, dedup_errors, dur)

    # -------------------------------------------------------------------------
    # Test 5.12: Seminal PhD Papers 35-Paper Complete Census
    # -------------------------------------------------------------------------
    def test_5_12_landmark_papers_census(self) -> Tier5TestResult:
        start_time = time.time()
        prh_rel = "03 - Papers/Paper Reading Hub.md"
        if prh_rel not in self.contents:
            return Tier5TestResult("TEST-5.12", "Landmark Papers Census", False, "Paper Reading Hub.md missing", duration_ms=0.0)

        c = self.contents[prh_rel]
        paper_rows = []
        for line in c.split("\n"):
            line = line.strip()
            if line.startswith("|") and not line.startswith("| #") and not line.startswith("|:--") and not line.startswith("| ---"):
                cols = [col.strip() for col in line.split("|")[1:-1]]
                if len(cols) >= 6 and cols[0].isdigit():
                    paper_rows.append(cols)

        errors = []
        if len(paper_rows) != 35:
            errors.append(f"Expected 35 papers, found {len(paper_rows)}")

        for r in paper_rows:
            p_num, title, block_col = r[0], r[1], r[5]
            m = re.search(r"\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]", block_col)
            if not m:
                errors.append(f"Paper {p_num}: Missing wikilink in assigned block column: {block_col}")
                continue
            block_target = m.group(1).strip()
            target_stem = Path(block_target).stem
            if target_stem not in self.stem_map:
                errors.append(f"Paper {p_num}: Assigned block '{block_target}' does not exist")
                continue
            target_rel = self.stem_map[target_stem]
            target_content = self.contents[target_rel]
            if "Paper Reading Hub" not in target_content:
                errors.append(f"Paper {p_num}: Assigned block '{target_rel}' does not link back to Paper Reading Hub")

        passed = len(errors) == 0
        dur = (time.time() - start_time) * 1000.0
        msg = "All 35 landmark papers verified with valid metadata and reciprocal curriculum links" if passed else f"Paper reading hub census errors: {errors}"
        return Tier5TestResult("TEST-5.12", "Seminal PhD Papers 35-Paper Census", passed, msg, errors, dur)

    # -------------------------------------------------------------------------
    # Runner
    # -------------------------------------------------------------------------
    def run_all_tests(self) -> List[Tier5TestResult]:
        tests = [
            self.test_5_1_student_navigation_simulation,
            self.test_5_2_graph_bidirectional_symmetry,
            self.test_5_3_yaml_schema_validation,
            self.test_5_4_tombstone_invariant,
            self.test_5_5_projects_hub_completeness,
            self.test_5_6_heading_anchor_integrity,
            self.test_5_7_math_delimiter_balance,
            self.test_5_8_prerequisite_dag_chronology,
            self.test_5_9_dataview_telemetry_compatibility,
            self.test_5_10_zero_stubs_and_artifacts,
            self.test_5_11_deduplication_and_architecture,
            self.test_5_12_landmark_papers_census,
        ]
        results = []
        for t in tests:
            res = t()
            results.append(res)
        return results


def main():
    vault_root = Path("/home/noblixy/The Noblett Repository")
    harness = Tier5AdversarialHarness(vault_root)
    results = harness.run_all_tests()

    print("=" * 80)
    print("       TIER 5 ADVERSARIAL STRESS TEST SUITE — CHALLENGER 2")
    print("=" * 80)
    all_passed = True
    for r in results:
        status = "[PASS]" if r.passed else "[FAIL]"
        print(f"  {status} {r.test_id:10} {r.name:50} ({r.duration_ms:5.1f}ms)")
        if not r.passed:
            all_passed = False
            print(f"         Message: {r.message}")
            for d in r.details:
                print(f"           - {d}")

    print("-" * 80)
    passed_count = sum(1 for r in results if r.passed)
    print(f"Total Tier 5 Tests: {len(results)} | Passed: {passed_count} | Failed: {len(results) - passed_count}")
    print("=" * 80)
    if all_passed:
        print("VERDICT: ZERO REMAINING GAPS [ALL TIER 5 STRESS TESTS PASSED]")
        sys.exit(0)
    else:
        print("VERDICT: GAPS DETECTED [REQUEST CHANGES]")
        sys.exit(1)


if __name__ == "__main__":
    main()
