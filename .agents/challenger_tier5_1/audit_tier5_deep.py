#!/usr/bin/env python3
"""
Deep Empirical Audit Script for Tier 5 Adversarial Coverage Hardening.
Audits all 84 markdown files in '/home/noblixy/The Noblett Repository'.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict, deque
import yaml

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository").resolve()

def get_vault_notes():
    notes = {}
    for p in sorted(VAULT_ROOT.rglob("*.md")):
        rel = p.relative_to(VAULT_ROOT)
        if str(rel).startswith(".agents"):
            continue
        notes[str(rel)] = p
    return notes

def parse_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                data = yaml.safe_load(parts[1])
                return data, parts[2]
            except Exception as e:
                return e, parts[2]
    return None, content

def run_deep_audit():
    notes = get_vault_notes()
    print(f"Auditing {len(notes)} notes in vault...")

    # Map stems and filenames
    filename_map = {}
    stem_map = {}
    for rel_path, full_path in notes.items():
        fname = full_path.name
        stem = full_path.stem
        filename_map[fname] = rel_path
        filename_map[stem] = rel_path
        stem_map[stem.lower()] = rel_path
        stem_map[fname.lower()] = rel_path

    findings = defaultdict(list)

    # 1. Wikilinks check (including anchor verification)
    wikilink_pattern = re.compile(r'(?<!`)(?:\[\[([^\]\n]+)\]\])')
    backticked_wikilink = re.compile(r'`\[\[([^\]\n]+)\]\]`')

    # Headings map for anchor resolution: rel_path -> set of normalized heading texts
    headings_map = defaultdict(set)
    for rel_path, full_path in notes.items():
        text = full_path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            m = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
            if m:
                h_text = m.group(2).strip()
                headings_map[rel_path].add(h_text)
                headings_map[rel_path].add(h_text.lower())
                # also add anchor normalized (remove non-alphanumeric except space/hyphen)
                norm_h = re.sub(r'[^\w\s-]', '', h_text).strip()
                headings_map[rel_path].add(norm_h)
                headings_map[rel_path].add(norm_h.lower())

    for rel_path, full_path in notes.items():
        is_template = rel_path.startswith("08 - Templates/")
        text = full_path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()

        # Check backticked wikilinks
        for idx, line in enumerate(lines, 1):
            for m in backticked_wikilink.finditer(line):
                findings["backticked_wikilink"].append((rel_path, idx, m.group(0)))

        # Strip code blocks before checking wikilinks in non-templates, or check code blocks
        in_code_fence = False
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue

            for m in wikilink_pattern.finditer(line):
                raw = m.group(1)
                # Split alias
                if "|" in raw:
                    target_part, alias_part = raw.split("|", 1)
                else:
                    target_part, alias_part = raw, raw

                # Check escaped pipe artifact
                if r"\|" in raw:
                    findings["escaped_pipe_in_wikilink"].append((rel_path, idx, raw))

                # Handle anchor: Target#Heading
                anchor = None
                if "#" in target_part:
                    target_file_part, anchor = target_part.split("#", 1)
                else:
                    target_file_part = target_part

                target_file_part = target_file_part.strip()
                if not target_file_part:
                    # Same page anchor: [[#Heading]]
                    resolved_file = rel_path
                else:
                    # Look up in filename_map / stem_map
                    resolved_file = filename_map.get(target_file_part)
                    if not resolved_file:
                        resolved_file = stem_map.get(target_file_part.lower())
                    if not resolved_file:
                        # Maybe full path or relative path
                        clean_p = target_file_part.lstrip("/")
                        if clean_p in notes:
                            resolved_file = clean_p
                        elif (clean_p + ".md") in notes:
                            resolved_file = clean_p + ".md"

                if not resolved_file:
                    if is_template:
                        findings["template_unresolved_link"].append((rel_path, idx, raw))
                    else:
                        findings["unresolved_wikilink"].append((rel_path, idx, raw))
                else:
                    # Target file found. If anchor exists, check anchor in target file
                    if anchor:
                        anchor_clean = anchor.strip()
                        # Some anchors might be block references ^abc or headings
                        if not anchor_clean.startswith("^"):
                            # Check if anchor is in headings
                            if anchor_clean not in headings_map[resolved_file] and anchor_clean.lower() not in headings_map[resolved_file]:
                                findings["unresolved_anchor"].append((rel_path, idx, raw, resolved_file, anchor_clean))

    # 2. Markdown Table Checks
    # Look for table blocks: lines starting with | or containing |
    # Check headers, separator row, column counts, escaped pipes
    for rel_path, full_path in notes.items():
        text = full_path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        in_code_fence = False
        table_lines = []
        table_start = 0

        def process_table(t_lines, start_lno):
            if len(t_lines) < 2:
                return
            header = t_lines[0]
            sep = t_lines[1]
            # Check separator format: |---|---| or :---:
            sep_cells = [c.strip() for c in sep.strip().strip("|").split("|")]
            valid_sep = all(re.match(r'^:?-+:?$', c) for c in sep_cells if c)
            if not valid_sep:
                findings["malformed_table_separator"].append((rel_path, start_lno + 1, sep))
                return

            expected_cols = len(sep_cells)
            for row_idx, row in enumerate(t_lines):
                # Count pipes, taking into account escaped pipes \|
                # But inside code `|` or wikilinks [[Target|Alias]]
                # Split row into cells carefully
                # A quick check: count unescaped pipes
                # Strip leading and trailing pipe
                r_clean = row.strip()
                if not (r_clean.startswith("|") and r_clean.endswith("|")):
                    findings["table_missing_bounding_pipe"].append((rel_path, start_lno + row_idx, row))
                # Split by unescaped pipe not inside ` ` or [[ ]]
                # Let's see how many cells
                # Simple cell splitting:
                cells = []
                cur = []
                in_code = False
                in_link = False
                escaped = False
                for ch in r_clean[1:-1]:
                    if escaped:
                        cur.append(ch)
                        escaped = False
                    elif ch == '\\':
                        escaped = True
                        cur.append(ch)
                    elif ch == '`':
                        in_code = not in_code
                        cur.append(ch)
                    elif ch == '[' and len(cur) > 0 and cur[-1] == '[':
                        in_link = True
                        cur.append(ch)
                    elif ch == ']' and len(cur) > 0 and cur[-1] == ']':
                        in_link = False
                        cur.append(ch)
                    elif ch == '|' and not in_code and not in_link:
                        cells.append("".join(cur).strip())
                        cur = []
                    else:
                        cur.append(ch)
                cells.append("".join(cur).strip())
                if len(cells) != expected_cols:
                    findings["table_column_mismatch"].append((rel_path, start_lno + row_idx, f"expected {expected_cols}, got {len(cells)}", row))

        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code_fence = not in_code_fence
                if table_lines:
                    process_table(table_lines, table_start)
                    table_lines = []
                continue
            if in_code_fence:
                continue

            stripped = line.strip()
            if stripped.startswith("|") and "|" in stripped[1:]:
                if not table_lines:
                    table_start = idx
                table_lines.append(line)
            else:
                if table_lines:
                    process_table(table_lines, table_start)
                    table_lines = []
        if table_lines:
            process_table(table_lines, table_start)

    # 3. List Indentation Checks
    # Even indentation (2 or 4 spaces)
    list_marker_pattern = re.compile(r'^(\s*)([-*+]|\d+\.)\s+')
    for rel_path, full_path in notes.items():
        text = full_path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        in_code_fence = False
        in_yaml = False
        if lines and lines[0].strip() == "---":
            in_yaml = True

        for idx, line in enumerate(lines, 1):
            if idx == 1 and in_yaml:
                continue
            if in_yaml:
                if line.strip() == "---":
                    in_yaml = False
                continue
            if line.strip().startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue

            m = list_marker_pattern.match(line)
            if m:
                indent_str = m.group(1)
                marker = m.group(2)
                # check tab characters
                if "\t" in indent_str:
                    findings["list_tab_indentation"].append((rel_path, idx, line))
                indent_len = len(indent_str)
                if indent_len % 2 != 0:
                    findings["list_odd_indentation"].append((rel_path, idx, indent_len, line))
                if marker in ("*", "+"):
                    findings["list_non_hyphen_marker"].append((rel_path, idx, marker, line))

    # 4. Code Fences Language Identifier
    for rel_path, full_path in notes.items():
        text = full_path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        in_code = False
        for idx, line in enumerate(lines, 1):
            s = line.strip()
            if s.startswith("```"):
                if not in_code:
                    in_code = True
                    tag = s[3:].strip()
                    if not tag:
                        findings["code_fence_missing_lang"].append((rel_path, idx, line))
                else:
                    in_code = False
        if in_code:
            findings["unclosed_code_fence"].append((rel_path, len(lines), "File ended inside open code fence"))

    # 5. LaTeX Math Environments Check
    for rel_path, full_path in notes.items():
        text = full_path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        in_code_fence = False
        in_display_math = False
        display_math_start = 0

        # Scan line by line for math
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue

            # Check display math delimiter $$
            # Count $$ on this line
            # Careful with escaped \$$
            pos = 0
            while True:
                p = line.find("$$", pos)
                if p == -1:
                    break
                if p > 0 and line[p-1] == '\\':
                    pos = p + 2
                    continue
                # toggle display math
                in_display_math = not in_display_math
                if in_display_math:
                    display_math_start = idx
                pos = p + 2

        if in_display_math:
            findings["unclosed_display_math"].append((rel_path, display_math_start, "Unclosed $$ display math fence"))

        # Check inline math $ on lines outside code fence and outside multi-line display math
        in_code_fence = False
        in_display_math = False
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue

            # Strip full display math $$...$$ on same line
            clean_l = re.sub(r'\$\$.*?\$\$', '', line)
            if "$$" in clean_l:
                # multi-line display math toggle
                in_display_math = not in_display_math
                continue
            if in_display_math:
                continue

            # Strip inline code `...`
            clean_l = re.sub(r'`[^`]*`', '', clean_l)

            # Check single $
            # Count unescaped $
            dollar_positions = [i for i, ch in enumerate(clean_l) if ch == '$' and (i == 0 or clean_l[i-1] != '\\')]
            if len(dollar_positions) % 2 != 0:
                findings["unmatched_inline_dollar"].append((rel_path, idx, len(dollar_positions), line))

        # Check LaTeX bracket balance inside math expressions
        # Find all $$...$$ and $...$
        # Strip code blocks
        clean_text = re.sub(r'```[\s\S]*?```', '', text)
        display_maths = re.findall(r'\$\$([\s\S]*?)\$\$', clean_text)
        for dm in display_maths:
            # check \left and \right balance
            lefts = len(re.findall(r'\\left[\[\(\{\|.]', dm))
            rights = len(re.findall(r'\\right[\]\)\}\|.]', dm))
            if lefts != rights:
                findings["latex_left_right_mismatch"].append((rel_path, f"left={lefts}, right={rights}", dm[:60]))
            # check braces balance (taking into account \{ and \})
            # rough brace check
            unbalanced_braces = 0
            escaped = False
            for ch in dm:
                if escaped:
                    escaped = False
                    continue
                if ch == '\\':
                    escaped = True
                    continue
                if ch == '{':
                    unbalanced_braces += 1
                elif ch == '}':
                    unbalanced_braces -= 1
                if unbalanced_braces < 0:
                    findings["latex_unbalanced_braces"].append((rel_path, "Extra closing brace", dm[:60]))
                    break
            if unbalanced_braces > 0:
                findings["latex_unbalanced_braces"].append((rel_path, "Unclosed opening brace", dm[:60]))

    # 6. Graph Reachability
    # Build graph of non-template notes
    adj = defaultdict(set)
    rev_adj = defaultdict(set)
    non_templates = [r for r in notes if not r.startswith("08 - Templates/")]

    for rel_path in non_templates:
        full_path = notes[rel_path]
        text = full_path.read_text(encoding="utf-8", errors="replace")
        for m in wikilink_pattern.finditer(text):
            raw = m.group(1).split("|")[0].split("#")[0].strip()
            target = filename_map.get(raw) or stem_map.get(raw.lower())
            if target and target in notes and not target.startswith("08 - Templates/"):
                adj[rel_path].add(target)
                rev_adj[target].add(rel_path)

    # BFS from 00 - Dashboard.md
    dashboard = "00 - Dashboard.md"
    visited = set()
    queue = deque([dashboard])
    if dashboard in notes:
        visited.add(dashboard)
        while queue:
            curr = queue.popleft()
            for nxt in adj[curr]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

    unreachable = set(non_templates) - visited
    if unreachable:
        findings["unreachable_from_dashboard"].extend(sorted(unreachable))

    # Check hubs, specializations, proofs, papers, bridges specifically
    specializations = [r for r in non_templates if "Specializations/Track" in r]
    for tr in specializations:
        if tr not in visited:
            findings["unreachable_specialization"].append(tr)

    bridges = [r for r in non_templates if "Bridge.md" in r]
    for br in bridges:
        if br not in visited:
            findings["unreachable_bridge"].append(br)

    # Check for sinks (out-degree == 0) among curriculum courses
    curriculum_courses = [r for r in non_templates if re.match(r'^01 - Curriculum/(?:Year \d|Phase)', r)]
    for cc in curriculum_courses:
        if len(adj[cc]) == 0:
            findings["curriculum_course_sink"].append(cc)

    # Check orphans (in-degree == 0)
    for nt in non_templates:
        if nt != dashboard and len(rev_adj[nt]) == 0:
            findings["orphan_note"].append(nt)

    # 7. Placeholder / TODO / TBD scan
    stub_pattern = re.compile(r'\b(TODO|TBD|TBA|FIXME|XXX)\b|\[(Insert|Outline|Draft)[^\]]*\]')
    for rel_path, full_path in notes.items():
        if rel_path.startswith("08 - Templates/"):
            continue
        text = full_path.read_text(encoding="utf-8", errors="replace")
        in_code_fence = False
        for idx, line in enumerate(text.splitlines(), 1):
            if line.strip().startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue
            m = stub_pattern.search(line)
            if m:
                findings["todo_placeholder_stub"].append((rel_path, idx, m.group(0), line.strip()[:80]))

    # Print summary of findings
    print("\n" + "="*80)
    print("                    DEEP EMPIRICAL AUDIT RESULTS")
    print("="*80)
    total_issues = sum(len(v) for v in findings.values())
    print(f"Total issue categories: {len(findings)}")
    print(f"Total anomalies detected: {total_issues}")
    print("-" * 80)

    for cat, items in sorted(findings.items()):
        print(f"\n[CATEGORY: {cat}] ({len(items)} occurrences)")
        for it in items[:10]:
            print(f"  - {it}")
        if len(items) > 10:
            print(f"  ... and {len(items)-10} more")

    if total_issues == 0:
        print("\nPERFECT PASS: ZERO DEFECTS DETECTED ACROSS ALL AUDITED CATEGORIES!")

if __name__ == "__main__":
    run_deep_audit()
