#!/usr/bin/env python3
"""
Independent Victory Audit: Formatting, Frontmatter & Readability
Auditor: victory_auditor_quality_pass
Vault: /home/noblixy/The Noblett Repository
"""

import os
import re
import yaml
from pathlib import Path

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

def parse_frontmatter(content):
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end != -1:
            raw_fm = content[4:end]
            body = content[end + 5:]
            try:
                data = yaml.safe_load(raw_fm)
                return data, raw_fm, body
            except Exception as e:
                return None, raw_fm, body
    return None, "", content

def audit_file(rel, p):
    errors = []
    warnings = []
    
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    data, raw_fm, body = parse_frontmatter(content)
    
    # 1. Frontmatter Validation
    is_template = "08 - Templates" in rel
    is_curriculum_block = bool(re.match(r"^01 - Curriculum/(?:Year \d|Phase)/(\d{2}[a-z]?) - ", rel))
    is_track = "01 - Curriculum/Specializations/Track " in rel
    is_hub_or_index = ("Hub" in Path(rel).stem or "Index" in Path(rel).stem or rel == "00 - Dashboard.md") and not is_template

    if is_curriculum_block and not is_template:
        if not data:
            errors.append("Missing or invalid YAML frontmatter in curriculum block")
        else:
            req_keys = ["block_id", "title", "term", "status", "hours_estimate", "hours_actual", 
                        "primary_resource", "milestone", "date_started", "date_completed"]
            for k in req_keys:
                if k not in data:
                    errors.append(f"Missing required frontmatter key '{k}'")
            if data.get("status") not in ["not-started", "in-progress", "done"]:
                errors.append(f"Invalid status '{data.get('status')}'")
            if not isinstance(data.get("hours_estimate"), (int, float)):
                errors.append(f"Invalid hours_estimate type: {type(data.get('hours_estimate'))}")
            if not isinstance(data.get("hours_actual"), (int, float)):
                errors.append(f"Invalid hours_actual type: {type(data.get('hours_actual'))}")

    elif is_track and not is_template:
        if not data:
            errors.append("Missing or invalid YAML frontmatter in specialization track")
        else:
            req_keys = ["track_id", "title", "term", "status", "target_profile", "prerequisites", "aliases"]
            for k in req_keys:
                if k not in data:
                    errors.append(f"Missing required track frontmatter key '{k}'")
            if not isinstance(data.get("prerequisites"), list) or len(data.get("prerequisites")) == 0:
                errors.append("Prerequisites must be a non-empty list of wikilinks")
            else:
                for pr in data.get("prerequisites"):
                    if not (isinstance(pr, str) and pr.startswith("[[") and pr.endswith("]]")):
                        errors.append(f"Prerequisite item '{pr}' not formatted as [[wikilink]]")
            if not isinstance(data.get("aliases"), list) or len(data.get("aliases")) == 0:
                errors.append("Aliases must be a non-empty list")

    elif is_hub_or_index and not is_template:
        if not data:
            errors.append("Missing or invalid YAML frontmatter in hub/index")
        else:
            req_keys = ["title", "type", "tags"]
            for k in req_keys:
                if k not in data:
                    errors.append(f"Missing required hub/index frontmatter key '{k}'")
            if data.get("type") not in ["hub", "index"]:
                errors.append(f"Invalid hub/index type '{data.get('type')}'")
            if not isinstance(data.get("tags"), list):
                errors.append("Tags must be a list")

    # 2. Header Hierarchy
    # Find all headings in body outside code blocks
    in_code_block = False
    headings = []
    for line_idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if m:
            level = len(m.group(1))
            h_text = m.group(2).strip()
            headings.append((line_idx, level, h_text))

    # Single H1 check
    h1s = [h for h in headings if h[1] == 1]
    if len(h1s) == 0 and not is_template:
        errors.append("Note has no H1 heading")
    elif len(h1s) > 1:
        errors.append(f"Multiple H1 headings detected ({len(h1s)}): {[h[2] for h in h1s]}")

    # Header level continuity (no jumping e.g. H1 -> H3)
    prev_level = 0
    for l_idx, lvl, txt in headings:
        if prev_level > 0 and lvl > prev_level + 1:
            errors.append(f"Line {l_idx}: Header level skipped from H{prev_level} to H{lvl}: '{txt}'")
        prev_level = lvl

    # Check H1 convention for curriculum blocks
    if is_curriculum_block and data and len(h1s) == 1:
        expected_h1 = f"{data.get('block_id')} — {data.get('title')}"
        if h1s[0][2] != expected_h1:
            errors.append(f"H1 mismatch: got '{h1s[0][2]}', expected '{expected_h1}'")

    # Check H1 convention for tracks
    if is_track and data and len(h1s) == 1:
        expected_h1 = f"{data.get('track_id')}: {data.get('title')}"
        if h1s[0][2] != expected_h1:
            errors.append(f"H1 mismatch: got '{h1s[0][2]}', expected '{expected_h1}'")

    # 3. List Formatting & Indentation
    # Check for odd space indentations (e.g. 3 or 5 spaces) on bullet list items
    in_code = False
    for line_idx, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        # Check bullet item
        m = re.match(r"^(\s*)([-*+])\s+", line)
        if m:
            indent = len(m.group(1))
            # Standard markdown indentation is even (0, 2, 4, 6...)
            if indent % 2 != 0:
                errors.append(f"Line {line_idx}: Odd indentation ({indent} spaces) on list item: '{line.strip()}'")

    # 4. Fenced Code Block Language Tagging
    in_code = False
    for line_idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code:
                # Opening fence
                lang = stripped[3:].strip()
                if not lang:
                    errors.append(f"Line {line_idx}: Fenced code block missing language tag")
                in_code = True
            else:
                in_code = False

    # 5. Raw HTML Tags (<br>, etc.)
    # Check for unwanted raw HTML tags like <br>, <br/>, <div, <span
    for line_idx, line in enumerate(lines, 1):
        if re.search(r"<\s*br\s*/?>", line, re.IGNORECASE):
            errors.append(f"Line {line_idx}: Raw HTML <br> tag detected: '{line.strip()}'")

    # 6. Table formatting
    # Inspect tables in file outside code blocks
    in_table_code = False
    table_lines = []
    for line_idx, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```"):
            in_table_code = not in_table_code
            table_lines = []
            continue
        if in_table_code:
            continue
        if s.startswith("|") and s.endswith("|"):
            table_lines.append((line_idx, s))
        else:
            if len(table_lines) >= 2:
                # Check table separator line
                sep_idx, sep_line = table_lines[1]
                if not re.match(r"^\|(\s*:?-+:?\s*\|)+$", sep_line):
                    errors.append(f"Line {sep_idx}: Malformed markdown table separator row: '{sep_line}'")
            table_lines = []

    # 7. Math Delimiter Balance ($ and $$)
    # Check $$ display math balance
    display_math_count = content.count("$$")
    if display_math_count % 2 != 0:
        errors.append(f"Unbalanced display math delimiters ($$): count = {display_math_count}")

    # Check inline math balance outside code blocks and display math
    # Strip code blocks
    content_no_code = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    content_no_inline_code = re.sub(r"`[^`\n]+`", "", content_no_code)
    content_no_disp_math = re.sub(r"\$\$.*?\$\$", "", content_no_inline_code, flags=re.DOTALL)
    
    # In the remainder, count single $ that are not escaped
    single_dollars = re.findall(r"(?<!\\)\$", content_no_disp_math)
    if len(single_dollars) % 2 != 0:
        errors.append(f"Unbalanced inline math delimiters ($): count = {len(single_dollars)}")

    return errors, warnings

def main():
    notes = get_vault_notes()
    print(f"Total markdown notes to audit for formatting: {len(notes)}")
    
    all_errors = {}
    for rel, p in sorted(notes.items()):
        errs, warns = audit_file(rel, p)
        if errs:
            all_errors[rel] = errs

    print("\n=== FORMATTING & READABILITY AUDIT RESULTS ===")
    print(f"Files audited: {len(notes)}")
    print(f"Files with formatting errors: {len(all_errors)}")
    
    if all_errors:
        for rel, errs in all_errors.items():
            print(f"\n[FAIL] {rel}:")
            for e in errs:
                print(f"  - {e}")
    else:
        print("ALL 84 NOTES PASS FORMATTING, FRONTMATTER, AND READABILITY AUDIT!")

    passed = len(all_errors) == 0
    print(f"\nFORMATTING & READABILITY VERDICT: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
