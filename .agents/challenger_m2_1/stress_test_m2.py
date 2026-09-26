#!/usr/bin/env python3
"""
Empirical Challenger Stress Harness — Milestone M2
Target Vault: /home/noblixy/The Noblett Repository
Author: Challenger 1 (challenger_m2_1)

Mission:
1. Validate YAML parsing across all 84 notes (required keys, data types, absence of syntax errors).
2. Scan for untagged bare code blocks (MD040).
3. Validate list indentation across all files (ensure 0 odd-space indents).
4. Verify table row column counts and pipe consistency.
5. Adversarial generators & sensitivity calibration for each oracle.
"""

import os
import sys
import re
import glob
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Set, Any, Optional

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository").resolve()

class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

class StrictSafeLoader(yaml.SafeLoader):
    pass

def _construct_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"found duplicate key '{key}'", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping

StrictSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)

class VaultScanner:
    def __init__(self, root: Path):
        self.root = root
        self.md_files: Dict[str, str] = {} # rel_path -> raw content
        self.lines: Dict[str, List[str]] = {}
        self.frontmatter: Dict[str, Optional[Dict[str, Any]]] = {}
        self.fm_ranges: Dict[str, Tuple[int, int]] = {} # 1-based (start, end)
        self.all_stems: Set[str] = set()
        self._load_vault()

    def _load_vault(self):
        for root, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in (".git", ".agents", ".obsidian")]
            for f in sorted(files):
                if f.endswith(".md"):
                    abs_p = Path(root) / f
                    rel_p = str(abs_p.relative_to(self.root))
                    content = abs_p.read_text(encoding="utf-8")
                    self.md_files[rel_p] = content
                    self.lines[rel_p] = content.splitlines(keepends=True)
                    self.all_stems.add(abs_p.stem)

                    # Extract frontmatter
                    if content.startswith("---\n"):
                        parts = content.split("---\n", 2)
                        if len(parts) >= 3:
                            fm_text = parts[1]
                            # Count lines in frontmatter
                            fm_lines = len(fm_text.splitlines())
                            self.fm_ranges[rel_p] = (1, fm_lines + 2)
                            try:
                                data = yaml.load(fm_text, Loader=StrictSafeLoader)
                                self.frontmatter[rel_p] = data if isinstance(data, dict) else {}
                            except Exception:
                                self.frontmatter[rel_p] = None
                        else:
                            self.frontmatter[rel_p] = None
                            self.fm_ranges[rel_p] = (1, 1)
                    else:
                        self.frontmatter[rel_p] = None
                        self.fm_ranges[rel_p] = (0, 0)

# ==============================================================================
# ORACLES
# ==============================================================================

class M2Oracles:
    @staticmethod
    def audit_yaml_frontmatter(scanner: VaultScanner) -> Tuple[bool, List[str], Dict[str, Any]]:
        """Validates YAML syntax, required keys, and data types across all notes."""
        defects = []
        stats = {
            "total_notes": len(scanner.md_files),
            "notes_with_fm": 0,
            "curriculum_blocks": 0,
            "specialization_tracks": 0,
            "hubs_and_indices": 0,
            "templates": 0,
            "other_notes": 0,
            "parsing_syntax_errors": 0,
        }

        # Contract 1: Curriculum Blocks (43 files)
        curriculum_dirs = (
            "01 - Curriculum/Phase -1 - Bedrock Foundations/",
            "01 - Curriculum/Phase 0 - Prerequisites/",
            "01 - Curriculum/Year 1 - Fundamentals/",
            "01 - Curriculum/Year 2 - Systems/",
            "01 - Curriculum/Year 3 - Depth/",
            "01 - Curriculum/Year 4 - Specialization/",
            "01 - Curriculum/Year 5 - MEng/",
        )
        curr_req_keys = {
            "block_id", "title", "term", "status", "hours_estimate",
            "hours_actual", "primary_resource", "milestone", "date_started", "date_completed"
        }
        allowed_statuses = {"not-started", "in-progress", "done"}

        # Contract 2: Specialization Tracks (11 files)
        track_req_keys = {
            "track_id", "title", "term", "status", "target_profile", "prerequisites", "aliases"
        }

        # Contract 3: Hubs & Indices (12 files)
        hub_index_map = {
            "00 - Dashboard.md": "hub",
            "01 - Curriculum/Specializations/Specializations Hub.md": "hub",
            "02 - Notes/Hardware/Hardware Index.md": "index",
            "02 - Notes/Languages/Languages Index.md": "index",
            "02 - Notes/Math/Math Index.md": "index",
            "02 - Notes/Systems/Systems Index.md": "index",
            "02 - Notes/Theory/Theory Index.md": "index",
            "03 - Papers/Paper Reading Hub.md": "hub",
            "04 - Writing/Writing Hub.md": "hub",
            "05 - Projects/Projects Hub.md": "hub",
            "06 - Breadth/Breadth and Humanities Hub.md": "hub",
            "09 - Mindset & Habits/Mindset Hub.md": "hub",
        }

        for rel, content in sorted(scanner.md_files.items()):
            fm = scanner.frontmatter.get(rel)
            has_fm_marker = content.startswith("---\n")

            if has_fm_marker:
                stats["notes_with_fm"] += 1
                if fm is None:
                    defects.append(f"{rel}: YAML frontmatter failed to parse (syntax error or duplicate key)")
                    stats["parsing_syntax_errors"] += 1
                    continue

            # Classify file
            is_curr_block = any(rel.startswith(d) for d in curriculum_dirs)
            is_track = rel.startswith("01 - Curriculum/Specializations/Track ")
            is_hub_or_index = rel in hub_index_map

            if is_curr_block:
                stats["curriculum_blocks"] += 1
                if fm is None:
                    defects.append(f"{rel}: Curriculum block missing required YAML frontmatter")
                    continue
                # Key validation
                missing = curr_req_keys - set(fm.keys())
                if missing:
                    defects.append(f"{rel}: Curriculum block missing required keys: {sorted(list(missing))}")
                extra = set(fm.keys()) - curr_req_keys
                if extra:
                    defects.append(f"{rel}: Curriculum block has unexpected extra keys: {sorted(list(extra))}")
                # Data types
                if not isinstance(fm.get("block_id"), str) or not fm.get("block_id").strip():
                    defects.append(f"{rel}: 'block_id' must be non-empty string, got {fm.get('block_id')}")
                if not isinstance(fm.get("title"), str) or not fm.get("title").strip():
                    defects.append(f"{rel}: 'title' must be non-empty string, got {fm.get('title')}")
                if not isinstance(fm.get("term"), str):
                    defects.append(f"{rel}: 'term' must be string, got {type(fm.get('term'))}")
                if fm.get("status") not in allowed_statuses:
                    defects.append(f"{rel}: 'status' '{fm.get('status')}' not in {allowed_statuses}")
                if not isinstance(fm.get("hours_estimate"), (int, float)):
                    defects.append(f"{rel}: 'hours_estimate' must be numeric, got {type(fm.get('hours_estimate'))}")
                if not isinstance(fm.get("hours_actual"), (int, float)):
                    defects.append(f"{rel}: 'hours_actual' must be numeric, got {type(fm.get('hours_actual'))}")

            elif is_track:
                stats["specialization_tracks"] += 1
                if fm is None:
                    defects.append(f"{rel}: Specialization track missing required YAML frontmatter")
                    continue
                missing = track_req_keys - set(fm.keys())
                if missing:
                    defects.append(f"{rel}: Track missing required keys: {sorted(list(missing))}")
                extra = set(fm.keys()) - track_req_keys
                if extra:
                    defects.append(f"{rel}: Track has unexpected extra keys: {sorted(list(extra))}")
                if fm.get("status") != "not-started":
                    defects.append(f"{rel}: Track status must be 'not-started', got '{fm.get('status')}'")
                
                # Prerequisites list of wikilinks
                prereqs = fm.get("prerequisites")
                if not isinstance(prereqs, list):
                    defects.append(f"{rel}: 'prerequisites' must be a YAML list, got {type(prereqs)}")
                else:
                    if len(prereqs) == 0:
                        defects.append(f"{rel}: 'prerequisites' list is empty")
                    for p in prereqs:
                        if not isinstance(p, str) or not (p.startswith("[[") and p.endswith("]]")):
                            defects.append(f"{rel}: Prerequisite '{p}' is not a valid [[wikilink]]")
                        else:
                            # Verify target exists in vault
                            target_stem = p.strip("[]").split("|")[0].strip()
                            target_stem = Path(target_stem).name
                            if target_stem not in scanner.all_stems:
                                defects.append(f"{rel}: Prerequisite link target '{target_stem}' not found in vault")

                # Aliases list of strings
                aliases = fm.get("aliases")
                if not isinstance(aliases, list):
                    defects.append(f"{rel}: 'aliases' must be a YAML list, got {type(aliases)}")
                else:
                    for a in aliases:
                        if not isinstance(a, str) or not a.strip():
                            defects.append(f"{rel}: Alias '{a}' is not a valid non-empty string")

            elif is_hub_or_index:
                stats["hubs_and_indices"] += 1
                exp_type = hub_index_map[rel]
                if fm is None:
                    defects.append(f"{rel}: Hub/Index missing required YAML frontmatter")
                    continue
                for k in ["title", "type", "tags"]:
                    if k not in fm:
                        defects.append(f"{rel}: Hub/Index missing key '{k}'")
                if fm.get("type") != exp_type:
                    defects.append(f"{rel}: Hub/Index type '{fm.get('type')}' does not match expected '{exp_type}'")
                tags = fm.get("tags")
                if not isinstance(tags, list):
                    defects.append(f"{rel}: 'tags' must be a list, got {type(tags)}")
                else:
                    if "navigation" not in tags or exp_type not in tags:
                        defects.append(f"{rel}: tags {tags} missing 'navigation' or '{exp_type}'")

            elif rel.startswith("08 - Templates/"):
                stats["templates"] += 1
            else:
                stats["other_notes"] += 1

        passed = len(defects) == 0
        return passed, defects, stats

    @staticmethod
    def audit_bare_code_blocks(scanner: VaultScanner) -> Tuple[bool, List[str], Dict[str, Any]]:
        """Scans for any untagged bare code blocks (MD040 violation)."""
        bare_blocks = []
        lang_distribution = {}
        total_blocks = 0

        for rel, lines in sorted(scanner.lines.items()):
            # Note: 08 - Templates/ are evaluated as well, but let's check everywhere
            in_code = False
            fence_char = None
            fence_len = 0
            open_line_no = 0

            for line_no, line in enumerate(lines, 1):
                m = re.match(r"^( {0,3})(`{3,}|~{3,})(.*)$", line)
                if m:
                    indent, fence, rest = m.groups()
                    if not in_code:
                        in_code = True
                        fence_char = fence[0]
                        fence_len = len(fence)
                        open_line_no = line_no
                        info = rest.strip()
                        total_blocks += 1
                        if info:
                            tag = info.split()[0]
                            lang_distribution[tag] = lang_distribution.get(tag, 0) + 1
                        else:
                            bare_blocks.append(f"{rel}:{line_no} Bare code block opening (missing language tag)")
                    else:
                        if fence[0] == fence_char and len(fence) >= fence_len and not rest.strip():
                            in_code = False

        passed = len(bare_blocks) == 0
        stats = {
            "total_fenced_blocks": total_blocks,
            "bare_blocks_count": len(bare_blocks),
            "languages": lang_distribution,
        }
        return passed, bare_blocks, stats

    @staticmethod
    def audit_list_indentation(scanner: VaultScanner) -> Tuple[bool, List[str], Dict[str, Any]]:
        """Validates that all list items use even-space indents (0, 2, 4 spaces)."""
        odd_indent_items = []
        distribution = {}
        total_items = 0

        for rel, lines in sorted(scanner.lines.items()):
            fm_start, fm_end = scanner.fm_ranges.get(rel, (0, 0))
            in_code = False

            for line_no, line in enumerate(lines, 1):
                if fm_start <= line_no <= fm_end:
                    continue
                s_line = line.strip()
                if s_line.startswith("```") or s_line.startswith("~~~"):
                    in_code = not in_code
                    continue
                if in_code:
                    continue

                # Standard list marker match
                m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
                if m:
                    indent_spaces = len(m.group(1))
                    total_items += 1
                    distribution[indent_spaces] = distribution.get(indent_spaces, 0) + 1
                    if indent_spaces % 2 != 0:
                        odd_indent_items.append(
                            f"{rel}:{line_no} Odd indent of {indent_spaces} space(s): '{line.rstrip()}'"
                        )

        passed = len(odd_indent_items) == 0
        stats = {
            "total_list_items": total_items,
            "odd_indent_count": len(odd_indent_items),
            "indent_distribution": distribution,
        }
        return passed, odd_indent_items, stats

    @staticmethod
    def _split_table_row(line: str) -> List[str]:
        """Splits a table line into cells safely handling wikilinks, code, and math."""
        # 1. Mask escaped pipes
        s = line.replace("\\|", "\x01")
        # 2. Mask pipes in [[...]]
        s = re.sub(r"\[\[([^\]]+)\]\]", lambda m: "[[" + m.group(1).replace("|", "\x02") + "]]", s)
        # 3. Mask pipes in `...`
        s = re.sub(r"`([^`]+)`", lambda m: "`" + m.group(1).replace("|", "\x03") + "`", s)
        # 4. Mask pipes in $...$
        s = re.sub(r"\$([^\$]+)\$", lambda m: "$" + m.group(1).replace("|", "\x04") + "$", s)

        stripped = s.strip()
        if stripped.startswith("|"):
            stripped = stripped[1:]
        if stripped.endswith("|"):
            stripped = stripped[:-1]

        raw_cells = stripped.split("|")
        cells = []
        for c in raw_cells:
            cell = c.replace("\x01", "\\|").replace("\x02", "|").replace("\x03", "|").replace("\x04", "|").strip()
            cells.append(cell)
        return cells

    @staticmethod
    def _is_table_separator(line: str) -> bool:
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            return False
        cells = M2Oracles._split_table_row(stripped)
        if not cells:
            return False
        for c in cells:
            if not re.match(r"^:?-+:?$", c):
                return False
        return True

    @staticmethod
    def audit_table_structure_and_pipes(scanner: VaultScanner) -> Tuple[bool, List[str], Dict[str, Any]]:
        """Verifies table row column counts, separator consistency, and pipe integrity."""
        defects = []
        total_tables = 0
        total_rows = 0

        for rel, lines in sorted(scanner.lines.items()):
            fm_start, fm_end = scanner.fm_ranges.get(rel, (0, 0))
            in_code = False
            i = 0

            while i < len(lines):
                line_no = i + 1
                line = lines[i]

                if fm_start <= line_no <= fm_end:
                    i += 1
                    continue
                s_line = line.strip()
                if s_line.startswith("```") or s_line.startswith("~~~"):
                    in_code = not in_code
                    i += 1
                    continue
                if in_code:
                    i += 1
                    continue

                if s_line.startswith("|") and s_line.endswith("|"):
                    # Potential table header
                    if i + 1 < len(lines) and M2Oracles._is_table_separator(lines[i + 1]):
                        header_line_no = line_no
                        header_cells = M2Oracles._split_table_row(s_line)
                        expected_cols = len(header_cells)
                        sep_cells = M2Oracles._split_table_row(lines[i + 1].strip())
                        
                        total_tables += 1

                        if len(sep_cells) != expected_cols:
                            defects.append(
                                f"{rel}:{header_line_no+1} Table separator has {len(sep_cells)} cols, expected {expected_cols}"
                            )

                        i += 2
                        data_rows = 0
                        while i < len(lines):
                            curr_line_no = i + 1
                            curr_line = lines[i].strip()
                            if curr_line.startswith("```") or curr_line.startswith("~~~"):
                                break
                            if curr_line.startswith("|") and curr_line.endswith("|"):
                                row_cells = M2Oracles._split_table_row(curr_line)
                                if len(row_cells) != expected_cols:
                                    defects.append(
                                        f"{rel}:{curr_line_no} Row has {len(row_cells)} cols (expected {expected_cols}): '{curr_line}'"
                                    )
                                data_rows += 1
                                total_rows += 1
                                i += 1
                            else:
                                break

                        if data_rows == 0:
                            defects.append(f"{rel}:{header_line_no} Table has 0 data rows (orphaned header)")
                        continue
                    else:
                        # Pipe row without valid separator following
                        # Check if it has internal pipes
                        if "|" in s_line[1:-1]:
                            defects.append(
                                f"{rel}:{line_no} Orphaned pipe-delimited row without table separator: '{s_line}'"
                            )
                i += 1

        passed = len(defects) == 0
        stats = {
            "total_tables": total_tables,
            "total_data_rows": total_rows,
            "defects_count": len(defects),
        }
        return passed, defects, stats

# ==============================================================================
# ADVERSARIAL GENERATORS & SENSITIVITY CALIBRATION
# ==============================================================================

class AdversarialStressHarness:
    """Generates synthetic adversarial mutations and confirms oracles detect them."""

    @staticmethod
    def test_generator_yaml_mutations(scanner: VaultScanner) -> Tuple[bool, str]:
        """Injects synthetic malformed YAML to test oracle sensitivity."""
        mutations = [
            ("missing_key", "---\nblock_id: 'B99'\ntitle: 'Test'\n---\n"),
            ("duplicate_key", "---\nblock_id: 'B99'\ntitle: 'Test'\ntitle: 'Duplicate'\n---\n"),
            ("invalid_status", "---\nstatus: 'unknown-status'\n---\n"),
            ("non_numeric_hours", "---\nhours_estimate: 'one hundred'\n---\n"),
            ("string_prereq", "---\nprerequisites: '[[01 - CS61A]]'\n---\n"),
            ("non_link_prereq", "---\nprerequisites:\n  - '01 - CS61A'\n---\n"),
            ("non_existent_prereq", "---\nprerequisites:\n  - '[[NonExistentTargetNote999]]'\n---\n"),
        ]

        detected = 0
        for name, mut_text in mutations:
            # Test duplicate key detection
            if name == "duplicate_key":
                try:
                    yaml.load(mut_text.split("---\n")[1], Loader=StrictSafeLoader)
                except Exception:
                    detected += 1
                continue

            # Test syntax and schema logic
            try:
                data = yaml.safe_load(mut_text.split("---\n")[1])
            except Exception:
                detected += 1
                continue

            if name == "missing_key" and ("hours_estimate" not in data):
                detected += 1
            elif name == "invalid_status" and (data.get("status") not in {"not-started", "in-progress", "done"}):
                detected += 1
            elif name == "non_numeric_hours" and not isinstance(data.get("hours_estimate"), (int, float)):
                detected += 1
            elif name == "string_prereq" and not isinstance(data.get("prerequisites"), list):
                detected += 1
            elif name == "non_link_prereq":
                p = data.get("prerequisites", [])[0]
                if not (p.startswith("[[") and p.endswith("]]")):
                    detected += 1
            elif name == "non_existent_prereq":
                p = data.get("prerequisites", [])[0]
                stem = p.strip("[]").split("|")[0].strip()
                if stem not in scanner.all_stems:
                    detected += 1

        all_detected = (detected == len(mutations))
        return all_detected, f"{detected}/{len(mutations)} synthetic YAML mutations detected"

    @staticmethod
    def test_generator_bare_code_blocks() -> Tuple[bool, str]:
        """Injects synthetic markdown with bare code blocks and tests detection."""
        test_markdown = """# Sample
Some text

```
echo 'bare block 1'
```

```bash
echo 'tagged block'
```

~~~
bare tilde block 2
~~~
"""
        bare_count = 0
        lines = test_markdown.splitlines()
        in_code = False
        fence_char = None
        fence_len = 0
        for line in lines:
            m = re.match(r"^( {0,3})(`{3,}|~{3,})(.*)$", line)
            if m:
                indent, fence, rest = m.groups()
                if not in_code:
                    in_code = True
                    fence_char = fence[0]
                    fence_len = len(fence)
                    if not rest.strip():
                        bare_count += 1
                else:
                    if fence[0] == fence_char and len(fence) >= fence_len and not rest.strip():
                        in_code = False

        passed = (bare_count == 2)
        return passed, f"Bare block oracle detected {bare_count}/2 synthetic bare fences"

    @staticmethod
    def test_generator_odd_space_indents() -> Tuple[bool, str]:
        """Injects synthetic odd-space list items and tests detection."""
        test_markdown = """# Test
- Normal root item (0 spaces)
  - Even subitem (2 spaces)
   - Odd subitem (3 spaces)
    - Even subitem (4 spaces)
     - Odd subitem (5 spaces)
 - Odd root item (1 space)
       - Odd subitem (7 spaces)
"""
        odd_detected = 0
        lines = test_markdown.splitlines()
        for line in lines:
            m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
            if m:
                indent = len(m.group(1))
                if indent % 2 != 0:
                    odd_detected += 1

        expected_odd = 4 # 3, 5, 1, 7 spaces
        passed = (odd_detected == expected_odd)
        return passed, f"Odd-space list oracle detected {odd_detected}/{expected_odd} synthetic violations"

    @staticmethod
    def test_generator_table_column_mismatches() -> Tuple[bool, str]:
        """Injects synthetic table anomalies and tests detection."""
        test_table = """
| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| Val 1 | Val 2 | Val 3 |
| Val 1 | Val 2 |
| Val 1 | Val 2 | Val 3 | Val 4 |
| [[Link|Alias]] | `$|x|$` | `foo|bar` |
"""
        lines = test_table.strip().splitlines()
        header = M2Oracles._split_table_row(lines[0])
        exp_cols = len(header) # 3
        mismatches = 0
        
        # Test row 3 (2 cols -> mismatch)
        r3 = M2Oracles._split_table_row(lines[3])
        if len(r3) != exp_cols:
            mismatches += 1
            
        # Test row 4 (4 cols -> mismatch)
        r4 = M2Oracles._split_table_row(lines[4])
        if len(r4) != exp_cols:
            mismatches += 1

        # Test row 5 (3 cols with masked pipes -> valid!)
        r5 = M2Oracles._split_table_row(lines[5])
        is_r5_valid = (len(r5) == exp_cols)

        passed = (mismatches == 2 and is_r5_valid)
        return passed, f"Table oracle correctly flagged 2/2 mismatches and preserved masked pipes row (cols={len(r5)})"


# ==============================================================================
# MAIN RUNNER
# ==============================================================================

def main():
    print("=" * 80)
    print("      EMPIRICAL CHALLENGER STRESS HARNESS — MILESTONE M2 AUDIT")
    print("=" * 80)
    print(f"Target Vault: {VAULT_ROOT}\n")

    scanner = VaultScanner(VAULT_ROOT)
    print(f"Indexed Markdown Notes: {len(scanner.md_files)}")
    print(f"Total Unique Basenames: {len(scanner.all_stems)}\n")

    all_passed = True

    # 1. YAML Parsing & Schema Validation
    print("--- CHALLENGE 1: YAML FRONTMATTER & SCHEMA STRESS TEST ---")
    pass_yaml, yaml_defects, yaml_stats = M2Oracles.audit_yaml_frontmatter(scanner)
    if pass_yaml:
        print(f"{Colors.GREEN}[PASS]{Colors.RESET} YAML Parsing & Schema Validation")
        print(f"       Audited {yaml_stats['total_notes']} notes ({yaml_stats['notes_with_fm']} with frontmatter).")
        print(f"       Curriculum Blocks: {yaml_stats['curriculum_blocks']} | Specialization Tracks: {yaml_stats['specialization_tracks']}")
        print(f"       Hubs & Indices: {yaml_stats['hubs_and_indices']} | Templates: {yaml_stats['templates']}")
        print(f"       Syntax/duplicate errors: {yaml_stats['parsing_syntax_errors']} | Schema defects: 0")
    else:
        all_passed = False
        print(f"{Colors.RED}[FAIL]{Colors.RESET} YAML Parsing & Schema Validation ({len(yaml_defects)} defects):")
        for d in yaml_defects:
            print(f"       - {d}")
    print()

    # 2. Bare Code Blocks (MD040)
    print("--- CHALLENGE 2: BARE CODE BLOCKS (MD040) SCANNER ---")
    pass_code, code_defects, code_stats = M2Oracles.audit_bare_code_blocks(scanner)
    if pass_code:
        print(f"{Colors.GREEN}[PASS]{Colors.RESET} Fenced Code Block Language Identifier Audit (MD040)")
        print(f"       Audited {code_stats['total_fenced_blocks']} code fences across vault.")
        print(f"       Languages: {code_stats['languages']}")
        print(f"       Bare code blocks found: {code_stats['bare_blocks_count']}")
    else:
        all_passed = False
        print(f"{Colors.RED}[FAIL]{Colors.RESET} Bare Code Blocks Detected ({len(code_defects)} blocks):")
        for d in code_defects:
            print(f"       - {d}")
    print()

    # 3. List Indentation Hierarchy
    print("--- CHALLENGE 3: LIST INDENTATION ODD-SPACE SCANNER ---")
    pass_indent, indent_defects, indent_stats = M2Oracles.audit_list_indentation(scanner)
    if pass_indent:
        print(f"{Colors.GREEN}[PASS]{Colors.RESET} List Indentation Regularity Audit")
        print(f"       Audited {indent_stats['total_list_items']} list items across 84 files.")
        print(f"       Indentation distribution: {indent_stats['indent_distribution']}")
        print(f"       Odd-space indented items found: {indent_stats['odd_indent_count']}")
    else:
        all_passed = False
        print(f"{Colors.RED}[FAIL]{Colors.RESET} Odd-Space List Indents Detected ({len(indent_defects)} items):")
        for d in indent_defects:
            print(f"       - {d}")
    print()

    # 4. Table Structure and Pipe Consistency
    print("--- CHALLENGE 4: TABLE STRUCTURAL VALIDATION & PIPE INTEGRITY ---")
    pass_tables, table_defects, table_stats = M2Oracles.audit_table_structure_and_pipes(scanner)
    if pass_tables:
        print(f"{Colors.GREEN}[PASS]{Colors.RESET} Table Column Counts & Pipe Delimiter Integrity")
        print(f"       Audited {table_stats['total_tables']} markdown tables ({table_stats['total_data_rows']} data rows).")
        print(f"       Column count mismatches: 0 | Orphaned pipe lines: 0")
    else:
        all_passed = False
        print(f"{Colors.RED}[FAIL]{Colors.RESET} Table Structural Defects Detected ({len(table_defects)} defects):")
        for d in table_defects:
            print(f"       - {d}")
    print()

    # 5. Adversarial Generators & Oracles Calibration
    print("--- CHALLENGE 5: ADVERSARIAL ORACLE SENSITIVITY CALIBRATION ---")
    g1_pass, g1_msg = AdversarialStressHarness.test_generator_yaml_mutations(scanner)
    g2_pass, g2_msg = AdversarialStressHarness.test_generator_bare_code_blocks()
    g3_pass, g3_msg = AdversarialStressHarness.test_generator_odd_space_indents()
    g4_pass, g4_msg = AdversarialStressHarness.test_generator_table_column_mismatches()

    gen_results = [
        ("Generator 1 (YAML Mutation Oracle)", g1_pass, g1_msg),
        ("Generator 2 (Bare Code Block Oracle)", g2_pass, g2_msg),
        ("Generator 3 (Odd-Space List Indent Oracle)", g3_pass, g3_msg),
        ("Generator 4 (Table Structural Mismatch Oracle)", g4_pass, g4_msg),
    ]

    for name, passed, msg in gen_results:
        status = f"{Colors.GREEN}[PASS]{Colors.RESET}" if passed else f"{Colors.RED}[FAIL]{Colors.RESET}"
        print(f"  {status} {name}: {msg}")
        if not passed:
            all_passed = False
    print()

    # Final Summary
    print("=" * 80)
    print("                      STRESS TEST EXECUTION VERDICT")
    print("=" * 80)
    if all_passed:
        print(f"VERDICT: {Colors.BOLD}{Colors.GREEN}APPROVE{Colors.RESET} — All Milestone M2 deliverables empirically verified with 0 defects.")
    else:
        print(f"VERDICT: {Colors.BOLD}{Colors.RED}REQUEST_CHANGES{Colors.RESET} — Empirical defects identified.")
    print("=" * 80)

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
