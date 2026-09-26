#!/usr/bin/env python3
"""
Independent Audit and Adversarial Verification Script for Milestone M2
Reviewer 2: /home/noblixy/The Noblett Repository/.agents/reviewer_m2_2
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from collections import defaultdict, deque
import yaml

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository").resolve()

def get_vault_files() -> Tuple[Dict[str, Path], Set[str]]:
    md_files = {}
    all_files = set()
    for root, dirs, files in os.walk(VAULT_ROOT):
        # Skip agent and dot directories
        parts = Path(root).relative_to(VAULT_ROOT).parts
        if any(p.startswith(".") for p in parts):
            continue
        for f in files:
            abs_p = Path(root) / f
            rel_p = str(abs_p.relative_to(VAULT_ROOT))
            all_files.add(rel_p)
            if f.endswith(".md"):
                md_files[rel_p] = abs_p
    return md_files, all_files

def check_root_cleanliness(all_files: Set[str]) -> List[str]:
    violations = []
    root_files = [f for f in all_files if "/" not in f]
    allowed_root_md = {
        "00 - Dashboard.md",
        "Checklist.md",
        "how-i-study.md",
        "log.md",
        "Telemetry Log.md",
        "Your Shelf.md",
    }
    for f in root_files:
        # Ignore dotfiles like .gitignore
        if f.startswith("."):
            continue
        if f not in allowed_root_md:
            violations.append(f"Unexpected file at vault root: {f}")
    return violations

def check_frontmatter(md_files: Dict[str, Path]) -> Dict[str, List[str]]:
    results = defaultdict(list)
    
    # Curriculum notes required keys
    curr_req_keys = {
        "block_id", "title", "term", "status", "hours_estimate",
        "hours_actual", "primary_resource", "milestone", "date_started", "date_completed"
    }
    
    # Track required keys
    track_req_keys = {
        "track_id", "title", "term", "status", "target_profile", "prerequisites", "aliases"
    }
    
    hub_and_indices = {
        "00 - Dashboard.md",
        "01 - Curriculum/Specializations/Specializations Hub.md",
        "03 - Papers/Paper Reading Hub.md",
        "04 - Writing/Writing Hub.md",
        "05 - Projects/Projects Hub.md",
        "06 - Breadth/Breadth and Humanities Hub.md",
        "09 - Mindset & Habits/Mindset Hub.md",
        "02 - Notes/Hardware/Hardware Index.md",
        "02 - Notes/Languages/Languages Index.md",
        "02 - Notes/Math/Math Index.md",
        "02 - Notes/Systems/Systems Index.md",
        "02 - Notes/Theory/Theory Index.md"
    }

    for rel_p, abs_p in sorted(md_files.items()):
        text = abs_p.read_text(encoding="utf-8")
        if text.startswith("---"):
            # Extract frontmatter
            parts = text.split("---", 2)
            if len(parts) >= 3:
                fm_raw = parts[1]
                try:
                    fm = yaml.safe_load(fm_raw)
                    if not isinstance(fm, dict):
                        results["yaml_error"].append(f"{rel_p}: Frontmatter is not a dictionary")
                        continue
                except Exception as e:
                    results["yaml_error"].append(f"{rel_p}: YAML parse error: {e}")
                    continue
            else:
                fm = {}
                results["yaml_error"].append(f"{rel_p}: Unclosed frontmatter --- delimiter")
        else:
            fm = {}
            if rel_p in hub_and_indices or rel_p.startswith("01 - Curriculum/"):
                if not rel_p.endswith("Baseline Gap Analysis and Audit Report.md"):
                    results["missing_frontmatter"].append(f"{rel_p}: No YAML frontmatter found")

        # Check curriculum notes (core 32 blocks + 3 bridge blocks + bedrock + prerequisites)
        if rel_p.startswith("01 - Curriculum/") and not rel_p.startswith("01 - Curriculum/Specializations/") and not rel_p.endswith("Baseline Gap Analysis and Audit Report.md"):
            missing = curr_req_keys - set(fm.keys())
            if missing:
                results["curriculum_missing_keys"].append(f"{rel_p}: missing {missing}")
            # Check status
            st = fm.get("status")
            if st not in ("not-started", "in-progress", "done"):
                results["curriculum_invalid_status"].append(f"{rel_p}: status='{st}'")
            # Check hours_estimate
            he = fm.get("hours_estimate")
            if not isinstance(he, (int, float)) or he <= 0:
                results["curriculum_invalid_hours"].append(f"{rel_p}: hours_estimate='{he}'")

        # Check Specialization Tracks
        if rel_p.startswith("01 - Curriculum/Specializations/Track "):
            missing = track_req_keys - set(fm.keys())
            if missing:
                results["track_missing_keys"].append(f"{rel_p}: missing {missing}")
            # Check status
            st = fm.get("status")
            if st != "not-started":
                results["track_invalid_status"].append(f"{rel_p}: status='{st}' (expected 'not-started')")
            # Check prerequisites is list
            prereqs = fm.get("prerequisites")
            if not isinstance(prereqs, list) or len(prereqs) == 0:
                results["track_invalid_prereqs"].append(f"{rel_p}: prerequisites is not a non-empty list: {prereqs}")
            # Check aliases is list
            aliases = fm.get("aliases")
            if not isinstance(aliases, list):
                results["track_invalid_aliases"].append(f"{rel_p}: aliases is not a list: {aliases}")

        # Check Hubs and Indices
        if rel_p in hub_and_indices:
            if "title" not in fm:
                results["hub_missing_title"].append(f"{rel_p}: missing 'title'")
            if "type" not in fm or fm["type"] not in ("hub", "index"):
                results["hub_invalid_type"].append(f"{rel_p}: invalid 'type'='{fm.get('type')}'")
            if "tags" not in fm:
                results["hub_missing_tags"].append(f"{rel_p}: missing 'tags'")

    return results

def check_h1_and_headings(md_files: Dict[str, Path]) -> Dict[str, List[str]]:
    results = defaultdict(list)
    for rel_p, abs_p in sorted(md_files.items()):
        if rel_p.startswith("08 - Templates/"):
            continue
        text = abs_p.read_text(encoding="utf-8")
        lines = text.splitlines()
        
        # Strip frontmatter
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                body_lines = parts[2].splitlines()
            else:
                body_lines = lines
        else:
            body_lines = lines

        headings = []
        in_cb = False
        for idx, line in enumerate(body_lines, 1):
            if line.strip().startswith("```"):
                in_cb = not in_cb
                continue
            if in_cb:
                continue
            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            if m:
                level = len(m.group(1))
                htext = m.group(2).strip()
                headings.append((level, htext, idx))

        h1s = [h for h in headings if h[0] == 1]
        if len(h1s) == 0:
            results["missing_h1"].append(rel_p)
        elif len(h1s) > 1:
            results["multiple_h1"].append(f"{rel_p}: {len(h1s)} H1s on lines {[h[2] for h in h1s]}")

        # Check heading level continuity
        prev_level = 0
        for level, htext, idx in headings:
            if prev_level > 0 and level > prev_level + 1:
                results["heading_level_skip"].append(f"{rel_p}:{idx} H{prev_level} -> H{level} ('{htext}')")
            prev_level = level

        # Check Blocks 31 and 32 specifically
        if rel_p == "01 - Curriculum/Year 5 - MEng/31 - Specialization B2.md":
            if not h1s or not h1s[0][1].startswith("Block 31 —"):
                results["blocks_31_32_desync"].append(f"Block 31 H1 is '{h1s[0][1] if h1s else 'NONE'}'")
        if rel_p == "01 - Curriculum/Year 5 - MEng/32 - Information Theory.md":
            if not h1s or not h1s[0][1].startswith("Block 32 —"):
                results["blocks_31_32_desync"].append(f"Block 32 H1 is '{h1s[0][1] if h1s else 'NONE'}'")

        # Check Specialization Track H1s
        if rel_p.startswith("01 - Curriculum/Specializations/Track "):
            m_track = re.search(r"Track (\d+)", rel_p)
            if m_track:
                tnum = m_track.group(1)
                expected_prefix = f"Track {tnum}:"
                if not h1s or not h1s[0][1].startswith(expected_prefix):
                    results["track_h1_mismatch"].append(f"{rel_p}: H1 is '{h1s[0][1] if h1s else 'NONE'}', expected '{expected_prefix} ...'")

    return results

def check_wikilinks_and_graph(md_files: Dict[str, Path], all_files: Set[str]) -> Dict[str, Any]:
    results = defaultdict(list)
    
    # Basename lookup across all_files
    stem_map = defaultdict(list)
    name_map = defaultdict(list)
    for rel_p in all_files:
        stem_map[Path(rel_p).stem.lower()].append(rel_p)
        name_map[Path(rel_p).name.lower()].append(rel_p)

    def resolve(target: str) -> bool:
        t = target.strip()
        if not t:
            return False
        # Remove anchor if present
        if "#" in t:
            t = t.split("#", 1)[0].strip()
        if not t:
            return True # pure anchor in same file
        # Check direct path
        if t in all_files or t.lower() in [f.lower() for f in all_files]:
            return True
        if (t + ".md") in all_files or (t.lower() + ".md") in [f.lower() for f in all_files]:
            return True
        t_stem = Path(t).stem.lower()
        if t_stem in stem_map:
            return True
        t_name = Path(t).name.lower()
        if t_name in name_map:
            return True
        return False

    adjacency = defaultdict(set)
    in_degree = defaultdict(int)

    backticked_links = []
    broken_links = []
    escaped_pipe_links = []

    for rel_p, abs_p in sorted(md_files.items()):
        text = abs_p.read_text(encoding="utf-8")
        is_template = rel_p.startswith("08 - Templates/")
        
        # Check for backticked wikilinks: `[[...]]`
        bt_matches = re.finditer(r"`\[\[(.*?)\]\]`", text)
        for m in bt_matches:
            if not is_template:
                backticked_links.append(f"{rel_p}: `[[{m.group(1)}]]`")

        # Find all wikilinks outside code fences
        lines = text.splitlines()
        in_cb = False
        for line_no, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_cb = not in_cb
                continue
            if in_cb:
                continue

            # Check escaped pipes in tables
            if r"\|" in line and "[[" in line:
                for pm in re.finditer(r"\[\[([^\]]*?\\\|[^\]]*?)\]\]", line):
                    escaped_pipe_links.append(f"{rel_p}:{line_no} -> {pm.group(0)}")

            # Extract all wikilinks
            for m in re.finditer(r"(?<!`)\[\[([^\]]+)\]\](?!`)", line):
                raw = m.group(1)
                # target | alias
                if "|" in raw:
                    target, alias = raw.split("|", 1)
                else:
                    target, alias = raw, ""
                target = target.strip()
                if not is_template:
                    if not resolve(target):
                        broken_links.append(f"{rel_p}:{line_no} -> [[{raw}]] (target: '{target}')")
                    else:
                        # find resolved target rel_path in md_files
                        t_clean = target.split("#", 1)[0].strip()
                        if t_clean:
                            t_stem = Path(t_clean).stem.lower()
                            if t_stem in stem_map:
                                resolved_list = [r for r in stem_map[t_stem] if r.endswith(".md")]
                                if resolved_list:
                                    adjacency[rel_p].add(resolved_list[0])

    # In-degree computation for non-templates
    non_templates = [r for r in md_files if not r.startswith("08 - Templates/")]
    for u in non_templates:
        for v in adjacency[u]:
            in_degree[v] += 1

    orphans = [r for r in non_templates if r != "00 - Dashboard.md" and in_degree[r] == 0]

    # Reachability from 00 - Dashboard.md
    reachable = set()
    queue = deque(["00 - Dashboard.md"])
    reachable.add("00 - Dashboard.md")
    while queue:
        curr = queue.popleft()
        for nxt in adjacency.get(curr, []):
            if nxt not in reachable:
                reachable.add(nxt)
                queue.append(nxt)

    unreachable = [r for r in non_templates if r not in reachable]

    results["backticked_links"] = backticked_links
    results["broken_links"] = broken_links
    results["escaped_pipe_links"] = escaped_pipe_links
    results["orphans"] = orphans
    results["unreachable"] = unreachable
    results["total_non_templates"] = len(non_templates)
    results["reachable_count"] = len(reachable)
    return results

def check_tables_and_html(md_files: Dict[str, Path]) -> Dict[str, List[str]]:
    results = defaultdict(list)
    html_tag_re = re.compile(r"<(br|div|span|table|tr|td|th|p|b|i|font)\b[^>]*>", re.IGNORECASE)

    for rel_p, abs_p in sorted(md_files.items()):
        text = abs_p.read_text(encoding="utf-8")
        lines = text.splitlines()

        # Check raw HTML tags outside code fences and outside inline code
        in_cb = False
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_cb = not in_cb
                continue
            if in_cb:
                continue
            # Strip inline code
            line_no_code = re.sub(r"`[^`]*`", "", line)
            for m in html_tag_re.finditer(line_no_code):
                results["raw_html"].append(f"{rel_p}:{idx} found tag '{m.group(0)}'")

        # Parse tables
        in_cb = False
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.strip().startswith("```"):
                in_cb = not in_cb
                i += 1
                continue
            if in_cb:
                i += 1
                continue

            # Potential table header
            if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+:?\s*(\|:?-+:?\s*)+\|?\s*$", lines[i+1]):
                header_line = line
                delim_line = lines[i+1]
                def split_row(r):
                    masked = re.sub(r"\[\[([^\]]+)\]\]", lambda m: "[[" + m.group(1).replace("|", "\x00") + "]]", r)
                    cells = [c.replace("\x00", "|").strip() for c in masked.strip("|").split("|")]
                    return cells

                headers = split_row(header_line)
                num_cols = len(headers)
                t_start = i + 1
                i += 2
                # Process table rows
                row_idx = 0
                while i < len(lines) and "|" in lines[i] and lines[i].strip():
                    row_cells = split_row(lines[i])
                    if len(row_cells) != num_cols:
                        results["invalid_table_row"].append(
                            f"{rel_p}:{i+1} Table starting at {t_start}: expected {num_cols} cols, got {len(row_cells)}: '{lines[i]}'"
                        )
                    row_idx += 1
                    i += 1
                continue
            i += 1

    # Check Telemetry Log specifically
    tlog_p = VAULT_ROOT / "Telemetry Log.md"
    if tlog_p.exists():
        tlog_text = tlog_p.read_text(encoding="utf-8")
        if "| Date | Time | Event | Data |" in tlog_text:
            results["telemetry_log_error"].append("Orphaned table header still present in Telemetry Log.md")

    return results

def check_code_blocks_and_lists(md_files: Dict[str, Path]) -> Dict[str, List[str]]:
    results = defaultdict(list)

    for rel_p, abs_p in sorted(md_files.items()):
        is_template = rel_p.startswith("08 - Templates/")
        text = abs_p.read_text(encoding="utf-8")
        lines = text.splitlines()

        # Check code fence balance and language tagging
        in_cb = False
        cb_start = 0
        cb_lang = ""
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                if not in_cb:
                    in_cb = True
                    cb_start = idx
                    cb_lang = line.strip()[3:].strip()
                    if not is_template and not cb_lang:
                        results["bare_code_block"].append(f"{rel_p}:{idx} Bare code block without language tag")
                else:
                    in_cb = False
                    cb_start = 0
                    cb_lang = ""

        if in_cb:
            results["unclosed_code_fence"].append(f"{rel_p}: Unclosed code fence starting at line {cb_start}")

        # Check display math balance $$
        outside_lines = []
        in_cb = False
        for line in lines:
            if line.strip().startswith("```"):
                in_cb = not in_cb
                continue
            if not in_cb:
                outside_lines.append(line)
        math_count = len(re.findall(r"\$\$", "\n".join(outside_lines)))
        if math_count % 2 != 0:
            results["unclosed_math_fence"].append(f"{rel_p}: Unbalanced $$ display math delimiter count ({math_count})")

        # Check list indentation and bullet markers
        in_cb = False
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_cb = not in_cb
                continue
            if in_cb:
                continue

            m = re.match(r"^(\s*)([-*+])\s+(.*)$", line)
            if m:
                indent_str = m.group(1)
                marker = m.group(2)
                item_text = m.group(3)
                indent_len = len(indent_str.replace("\t", "    "))
                
                # Check bullet marker
                if marker in ("*", "+"):
                    results["non_standard_bullet"].append(f"{rel_p}:{idx} Marker '{marker}' used")

                # Check odd indent
                if indent_len % 2 != 0:
                    results["odd_space_indent"].append(f"{rel_p}:{idx} Odd indent of {indent_len} spaces")

    return results

def check_qed_tombstones(md_files: Dict[str, Path]) -> Dict[str, List[str]]:
    results = defaultdict(list)
    proof_blocks = [
        "10 - Math for CS.md", "11 - Linear Algebra.md", "13 - Algorithms I.md",
        "15 - Probability.md", "18 - Real Analysis.md", "20 - Algorithms II.md",
        "22 - Statistics.md", "24 - Theory of Computation.md", "25 - Convex Optimization.md",
        "32 - Information Theory.md"
    ]
    for rel_p, abs_p in sorted(md_files.items()):
        if any(rel_p.endswith(b) for b in proof_blocks):
            text = abs_p.read_text(encoding="utf-8")
            # Look for study notes / proofs section
            m = re.search(r"## 📝 Study Notes[^\n]*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
            if m:
                sec_text = m.group(1)
                if r"\blacksquare" not in sec_text and "■" not in sec_text and r"\square" not in sec_text:
                    results["missing_qed"].append(rel_p)
    return results

def check_block_note_template() -> List[str]:
    violations = []
    p = VAULT_ROOT / "08 - Templates/Block Note Template.md"
    if not p.exists():
        return ["08 - Templates/Block Note Template.md does not exist"]
    text = p.read_text(encoding="utf-8")
    if "## 📖 Primary Syllabus & Core Content" not in text:
        violations.append("Block Note Template missing '## 📖 Primary Syllabus & Core Content'")
    if "## 📝 Study Notes, Psets & Proofs" not in text:
        violations.append("Block Note Template missing '## 📝 Study Notes, Psets & Proofs'")
    return violations

def main():
    print("=" * 80)
    print("INDEPENDENT ADVERSARIAL AUDIT - MILESTONE M2")
    print("Reviewer 2: /home/noblixy/The Noblett Repository/.agents/reviewer_m2_2")
    print("=" * 80)

    md_files, all_files = get_vault_files()
    print(f"Total vault markdown files discovered: {len(md_files)}")
    print(f"Total vault non-agent files: {len(all_files)}")

    clean_errors = check_root_cleanliness(all_files)
    fm_errors = check_frontmatter(md_files)
    h1_errors = check_h1_and_headings(md_files)
    wiki_results = check_wikilinks_and_graph(md_files, all_files)
    table_errors = check_tables_and_html(md_files)
    fmt_errors = check_code_blocks_and_lists(md_files)
    qed_errors = check_qed_tombstones(md_files)
    template_errors = check_block_note_template()

    print("\n--- ROOT CLEANLINESS & ARTIFACTS ---")
    if clean_errors:
        print(f"[FAIL] {len(clean_errors)} root cleanliness violations:")
        for e in clean_errors:
            print(f"  - {e}")
    else:
        print("[PASS] Vault root is clean. No orphan/temporary test files at root.")

    print("\n--- YAML FRONTMATTER AUDIT ---")
    total_fm_errs = sum(len(v) for v in fm_errors.values())
    if total_fm_errs > 0:
        print(f"[FAIL] {total_fm_errs} frontmatter errors:")
        for k, v in fm_errors.items():
            print(f"  {k} ({len(v)}):")
            for item in v[:5]:
                print(f"    - {item}")
    else:
        print("[PASS] 100% of required YAML frontmatters are valid and adhere to schemas.")

    print("\n--- HEADINGS & H1 CONVENTIONS (F08) ---")
    total_h1_errs = sum(len(v) for v in h1_errors.values())
    if total_h1_errs > 0:
        print(f"[FAIL] {total_h1_errs} heading errors:")
        for k, v in h1_errors.items():
            print(f"  {k} ({len(v)}):")
            for item in v:
                print(f"    - {item}")
    else:
        print("[PASS] All notes have exactly 1 H1, valid continuity, and Blocks 31/32 H1 synced.")

    print("\n--- WIKILINKS & M1 REGRESSION CHECK (F01, F02, F05, F07, F09) ---")
    print(f"  Backticked wikilinks: {len(wiki_results['backticked_links'])}")
    print(f"  Broken wikilinks:     {len(wiki_results['broken_links'])}")
    print(f"  Escaped pipe links:   {len(wiki_results['escaped_pipe_links'])}")
    print(f"  Orphan notes:         {len(wiki_results['orphans'])}")
    print(f"  Dashboard reachability: {wiki_results['reachable_count']}/{wiki_results['total_non_templates']} reachable")

    wiki_pass = (
        len(wiki_results['backticked_links']) == 0 and
        len(wiki_results['broken_links']) == 0 and
        len(wiki_results['escaped_pipe_links']) == 0 and
        len(wiki_results['orphans']) == 0 and
        len(wiki_results['unreachable']) == 0
    )
    if wiki_pass:
        print("[PASS] ZERO M1 regressions. 0 broken links, 0 orphans, 100% reachable, 0 backticked links.")
    else:
        print("[FAIL] M1 regression detected!")
        if wiki_results['backticked_links']:
            print("  Backticked links sample:", wiki_results['backticked_links'][:5])
        if wiki_results['broken_links']:
            print("  Broken links sample:", wiki_results['broken_links'][:5])
        if wiki_results['orphans']:
            print("  Orphans:", wiki_results['orphans'])
        if wiki_results['unreachable']:
            print("  Unreachable:", wiki_results['unreachable'])

    print("\n--- TABLES & RAW HTML (F11, F14) ---")
    total_tbl_errs = sum(len(v) for v in table_errors.values())
    if total_tbl_errs > 0:
        print(f"[FAIL] {total_tbl_errs} table/html errors:")
        for k, v in table_errors.items():
            print(f"  {k} ({len(v)}):")
            for item in v:
                print(f"    - {item}")
    else:
        print("[PASS] All markdown tables structurally valid. Telemetry Log clean. Zero raw HTML tags.")

    print("\n--- CODE BLOCKS & LIST INDENTATION (F13, F15) ---")
    total_fmt_errs = sum(len(v) for v in fmt_errors.values())
    if total_fmt_errs > 0:
        print(f"[FAIL] {total_fmt_errs} formatting errors:")
        for k, v in fmt_errors.items():
            print(f"  {k} ({len(v)}):")
            for item in v[:5]:
                print(f"    - {item}")
    else:
        print("[PASS] All code blocks tagged with language. No unclosed fences. No odd-space indents. Strict '-' bullets.")

    print("\n--- Q.E.D. PROOF TOMBSTONES (F16) ---")
    if qed_errors["missing_qed"]:
        print(f"[FAIL] Proof sections missing tombstone: {qed_errors['missing_qed']}")
    else:
        print("[PASS] All formal proof sections terminate with standard Q.E.D. tombstone.")

    print("\n--- BLOCK NOTE TEMPLATE (F10) ---")
    if template_errors:
        print(f"[FAIL] Block note template errors: {template_errors}")
    else:
        print("[PASS] Block note template H2 headings synchronized.")

    all_passed = (
        len(clean_errors) == 0 and
        total_fm_errs == 0 and
        total_h1_errs == 0 and
        wiki_pass and
        total_tbl_errs == 0 and
        total_fmt_errs == 0 and
        len(qed_errors["missing_qed"]) == 0 and
        len(template_errors) == 0
    )
    print("\n" + "=" * 80)
    print(f"OVERALL INDEPENDENT VERIFICATION VERDICT: {'ALL CRITERIA SATISFIED [APPROVE]' if all_passed else 'FAILURES DETECTED [REQUEST_CHANGES]'}")
    print("=" * 80)
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
