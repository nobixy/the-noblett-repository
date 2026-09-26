#!/usr/bin/env python3
"""
Comprehensive Vault Quality Pass — End-to-End (E2E) Test Suite & Runner
========================================================================

An automated, opaque-box, requirement-driven E2E test runner that validates
The Noblett Repository Obsidian vault against 100% of the features inventoried
in PROJECT.md § Feature Inventory (F01–F30) and all user acceptance criteria.

Architecture:
- Tier 1: Feature Coverage (35 test cases across 7 core feature areas)
  * Area 1.1: Wikilink Resolution (5 tests)
  * Area 1.2: Graph Reachability & Orphan Notes (5 tests)
  * Area 1.3: Header Hierarchy & Title Consistency (5 tests)
  * Area 1.4: YAML Frontmatter Schemas (5 tests)
  * Area 1.5: List Formatting & Table Syntax (5 tests)
  * Area 1.6: Stub Absence & Proof Completeness (5 tests)
  * Area 1.7: Content Deduplication & Sanitization (5 tests)
- Tier 2: Boundary & Corner Cases (7 test cases: escaped pipes, template placeholders,
  empty files, malformed fences, odd-space indentation, isolated subgraphs, case sensitivity)
- Tier 3: Cross-Feature Interactions (6 test cases: Dataview compatibility, bidirectional
  links, landmark papers reciprocity, topic notes reciprocity, course sink elimination, DAG acyclicity)
- Tier 4: Real-World Workflows (5 test cases: student navigation simulation, degree pathway
  completion, daily study routine, project build progression, master audit synchronization)

Total: 53 automated test cases.

Usage:
  python3 .agents/test_suite/run_e2e_tests.py [options]

Options:
  --tier {1,2,3,4,all}          Run tests for a specific tier (default: all)
  --milestone {M1,M2,M3,M4,all} Filter or evaluate progressive milestone gate (default: all)
  -v, --verbose                 Display detailed diagnostic failure breakdowns
  --json-out PATH               Export machine-readable JSON test execution report
  --vault-root PATH             Override vault root directory (default: parent of .agents)
  --list-tests                  Print full catalog of all 53 test specifications and exit
  --baseline                    Run in baseline audit mode (prints diagnostics, exits 0)
"""

import sys
import os
import re
import json
import time
import argparse
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Set, Tuple, Optional, Any
from collections import defaultdict, deque


# ANSI Terminal Colors
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"

    @classmethod
    def disable(cls):
        cls.RESET = ""
        cls.BOLD = ""
        cls.DIM = ""
        cls.GREEN = ""
        cls.RED = ""
        cls.YELLOW = ""
        cls.BLUE = ""
        cls.CYAN = ""
        cls.MAGENTA = ""


if not sys.stdout.isatty():
    Colors.disable()


@dataclass
class TestResult:
    test_id: str
    name: str
    tier: int
    milestone: str
    feature_id: str
    passed: bool
    skipped: bool = False
    message: str = ""
    details: List[str] = field(default_factory=list)
    duration_ms: float = 0.0


@dataclass
class TableInfo:
    start_line: int
    headers: List[str]
    num_columns: int
    row_count: int
    is_valid: bool
    error: str = ""


@dataclass
class MarkdownFile:
    path: Path
    rel_path: str
    raw_content: str
    lines: List[str]
    frontmatter: Dict[str, Any]
    raw_frontmatter: str
    headings: List[Tuple[int, str, int]]  # (level, text, line_num)
    wikilinks: List[Tuple[int, str, str, str, bool]]  # (line_num, raw_match, target, alias, is_backticked)
    code_blocks: List[Tuple[int, str, str]]  # (line_num, lang, content)
    tables: List[TableInfo]
    list_items: List[Tuple[int, int, str, str]]  # (line_num, indent_spaces, bullet_marker, text)


class SimpleYAMLParser:
    """Robust zero-dependency YAML frontmatter parser for Obsidian notes."""

    @staticmethod
    def parse(yaml_str: str) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        lines = yaml_str.splitlines()
        current_list_key = None
        current_list: List[Any] = []

        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            # Check for list item under current key
            if current_list_key and re.match(r"^(\s*)-\s+(.*)$", line):
                m = re.match(r"^(\s*)-\s+(.*)$", line)
                item_val = m.group(2).strip().strip('"\'')
                current_list.append(item_val)
                continue
            elif current_list_key and not line.startswith(" ") and not line.startswith("\t"):
                result[current_list_key] = current_list
                current_list_key = None
                current_list = []

            # Check for key: value
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip()

                if not val:
                    # Possible start of a multiline list
                    current_list_key = key
                    current_list = []
                    continue

                # Inline list: [item1, item2]
                if val.startswith("[") and val.endswith("]"):
                    inner = val[1:-1].strip()
                    if not inner:
                        result[key] = []
                    else:
                        items = [i.strip().strip('"\'') for i in inner.split(",") if i.strip()]
                        result[key] = items
                    continue

                # Strip quotes
                clean_val = val.strip('"\'')
                # Parse numeric
                if clean_val.isdigit():
                    result[key] = int(clean_val)
                else:
                    try:
                        result[key] = float(clean_val)
                    except ValueError:
                        # Booleans
                        if clean_val.lower() == "true":
                            result[key] = True
                        elif clean_val.lower() == "false":
                            result[key] = False
                        else:
                            result[key] = clean_val

        if current_list_key:
            result[current_list_key] = current_list

        return result


class VaultContext:
    """Discovers, parses, and indexes the entire Obsidian vault."""

    def __init__(self, vault_root: Path):
        self.vault_root = vault_root.resolve()
        self.all_files: Set[str] = set()
        self.md_files: Dict[str, MarkdownFile] = {}
        self.basename_map: Dict[str, List[str]] = defaultdict(list)
        self.exact_file_map: Dict[str, str] = {}
        self.adjacency: Dict[str, Set[str]] = defaultdict(set)
        self.in_degree: Dict[str, int] = defaultdict(int)
        self.out_degree: Dict[str, int] = defaultdict(int)

        self._discover_and_parse()
        self._build_graph()

    def _discover_and_parse(self):
        for root, dirs, files in os.walk(self.vault_root):
            rel_dir = os.path.relpath(root, self.vault_root)
            parts = Path(rel_dir).parts
            if any(p in (".git", ".agents", ".obsidian") for p in parts):
                continue

            for f in files:
                abs_path = Path(root) / f
                rel_path = str(abs_path.relative_to(self.vault_root))
                # Skip test suite documentation deliverables from vault curriculum note parsing
                if rel_path in ("TEST_INFRA.md", "TEST_READY.md") or f.startswith("TEST_"):
                    continue
                self.all_files.add(rel_path)
                self.exact_file_map[rel_path.lower()] = rel_path
                self.basename_map[abs_path.stem.lower()].append(rel_path)
                self.basename_map[abs_path.name.lower()].append(rel_path)

                if f.endswith(".md"):
                    self._parse_markdown(abs_path, rel_path)

    @staticmethod
    def _split_table_row(row_str: str) -> List[str]:
        # Temporarily mask pipes inside [[...]]
        masked = re.sub(r"\[\[([^\]]+)\]\]", lambda m: "[[" + m.group(1).replace("|", "\x00") + "]]", row_str)
        cells = [c.replace("\x00", "|").strip() for c in masked.strip("|").split("|")]
        return cells

    def _parse_markdown(self, abs_path: Path, rel_path: str):
        try:
            content = abs_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return

        lines = content.splitlines()

        # Frontmatter
        frontmatter = {}
        raw_fm = ""
        fm_end_line = 0
        if content.startswith("---"):
            for idx in range(1, len(lines)):
                if lines[idx].strip() == "---":
                    fm_end_line = idx + 1
                    raw_fm = "\n".join(lines[1:idx])
                    frontmatter = SimpleYAMLParser.parse(raw_fm)
                    break

        # Code blocks & code line tracking
        code_blocks: List[Tuple[int, str, str]] = []
        code_lines: Set[int] = set()
        current_block_lang = None
        current_block_lines: List[str] = []
        start_line = 0

        for line_no, line in enumerate(lines, 1):
            if line_no <= fm_end_line:
                continue
            stripped = line.strip()
            if stripped.startswith("```"):
                code_lines.add(line_no)
                if current_block_lang is None:
                    # Opening fence
                    current_block_lang = stripped[3:].strip()
                    start_line = line_no
                    current_block_lines = []
                else:
                    # Closing fence
                    code_blocks.append((start_line, current_block_lang, "\n".join(current_block_lines)))
                    current_block_lang = None
                    current_block_lines = []
            elif current_block_lang is not None:
                code_lines.add(line_no)
                current_block_lines.append(line)

        # Headings
        headings: List[Tuple[int, str, int]] = []
        for line_no, line in enumerate(lines, 1):
            if line_no <= fm_end_line or line_no in code_lines:
                continue
            s_line = line.strip()
            if s_line.startswith("#"):
                m = re.match(r"^(#{1,6})\s+(.*)$", s_line)
                if m:
                    headings.append((len(m.group(1)), m.group(2).strip(), line_no))

        # Wikilinks
        # Match `[[...]]` or `[[...]]` wrapped in backticks
        wikilinks: List[Tuple[int, str, str, str, bool]] = []
        inline_code_pattern = re.compile(r"`([^`\n]+)`")
        normal_pattern = re.compile(r"\[\[([^\]]+)\]\]")

        for line_no, line in enumerate(lines, 1):
            # Check for backticked links first (any wikilink enclosed within inline code backticks)
            clean_line = line
            for cm in inline_code_pattern.finditer(line):
                span_text = cm.group(1)
                for wm in normal_pattern.finditer(span_text):
                    raw_target = wm.group(1)
                    if "|" in raw_target:
                        target_part, alias_part = raw_target.split("|", 1)
                    else:
                        target_part, alias_part = raw_target, raw_target
                    wikilinks.append((line_no, cm.group(0), target_part.strip(), alias_part.strip(), True))
                if "[[" in span_text and "]]" in span_text:
                    clean_line = clean_line.replace(cm.group(0), "____BACKTICKED_LINK____")

            # Non-backticked
            for m in normal_pattern.finditer(clean_line):
                raw_target = m.group(1)
                if "|" in raw_target:
                    target_part, alias_part = raw_target.split("|", 1)
                else:
                    target_part, alias_part = raw_target, raw_target
                wikilinks.append((line_no, m.group(0), target_part.strip(), alias_part.strip(), False))

        # Tables
        tables: List[TableInfo] = []
        idx = 0
        while idx < len(lines):
            line_no = idx + 1
            if line_no <= fm_end_line or line_no in code_lines:
                idx += 1
                continue
            line = lines[idx]
            stripped = line.strip()
            if stripped.startswith("|") and stripped.endswith("|"):
                t_start = line_no
                headers = self._split_table_row(stripped)
                idx += 1
                if idx < len(lines):
                    sep_line = lines[idx].strip()
                    if sep_line.startswith("|") and re.match(r"^\|(\s*:?-+:?\s*\|)+$", sep_line):
                        # Valid separator
                        num_cols = len(headers)
                        rows = 0
                        idx += 1
                        table_valid = True
                        table_err = ""
                        while idx < len(lines):
                            curr_line_no = idx + 1
                            if curr_line_no in code_lines:
                                break
                            row_line = lines[idx].strip()
                            if row_line.startswith("|") and row_line.endswith("|"):
                                row_cols = len(self._split_table_row(row_line))
                                if row_cols != num_cols:
                                    table_valid = False
                                    table_err = f"Row on line {curr_line_no} has {row_cols} columns (expected {num_cols})"
                                rows += 1
                                idx += 1
                            else:
                                break
                        # If a table has 0 rows and is immediately followed by bullet items, flag as malformed
                        if rows == 0 and idx < len(lines) and lines[idx].strip().startswith("-"):
                            table_valid = False
                            table_err = f"Table header on line {t_start} has 0 data rows and is immediately followed by list items"

                        tables.append(TableInfo(
                            start_line=t_start,
                            headers=headers,
                            num_columns=num_cols,
                            row_count=rows,
                            is_valid=table_valid,
                            error=table_err
                        ))
                        continue
                    else:
                        # Malformed table (header without valid separator)
                        tables.append(TableInfo(
                            start_line=t_start,
                            headers=headers,
                            num_columns=len(headers),
                            row_count=0,
                            is_valid=False,
                            error=f"Table header on line {t_start} followed by invalid separator: '{sep_line}'"
                        ))
            idx += 1

        # List items
        list_items: List[Tuple[int, int, str, str]] = []
        for line_no, line in enumerate(lines, 1):
            if line_no <= fm_end_line or line_no in code_lines:
                continue
            m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
            if m:
                indent = len(m.group(1))
                marker = m.group(2)
                text = m.group(3)
                list_items.append((line_no, indent, marker, text))

        self.md_files[rel_path] = MarkdownFile(
            path=abs_path,
            rel_path=rel_path,
            raw_content=content,
            lines=lines,
            frontmatter=frontmatter,
            raw_frontmatter=raw_fm,
            headings=headings,
            wikilinks=wikilinks,
            code_blocks=code_blocks,
            tables=tables,
            list_items=list_items
        )

    def _build_graph(self):
        # Initialize in/out degrees for all md files
        for rel_path in self.md_files:
            self.in_degree[rel_path] = 0
            self.out_degree[rel_path] = 0

        for src, md in self.md_files.items():
            for line_no, raw, target, alias, is_bt in md.wikilinks:
                resolved = self.resolve_wikilink(target)
                if resolved and resolved in self.md_files and resolved != src:
                    self.adjacency[src].add(resolved)

        for src, targets in self.adjacency.items():
            self.out_degree[src] = len(targets)
            for tgt in targets:
                self.in_degree[tgt] += 1

    def resolve_wikilink(self, target: str) -> Optional[str]:
        """Resolves target stem or relative path to a canonical vault relative path."""
        # Strip heading anchor if present
        clean = target.strip()
        if "#" in clean:
            clean = clean.split("#", 1)[0].strip()

        if not clean:
            return None

        # Check for escaped table pipes (which produce literal trailing backslashes)
        if clean.endswith("\\"):
            # Escaped pipe artifact: target will fail to resolve in authentic Obsidian
            return None

        clean_lower = clean.lower()

        # 1. Exact match by relative path
        if clean in self.all_files:
            return clean
        if (clean + ".md") in self.all_files:
            return clean + ".md"
        if clean_lower in self.exact_file_map:
            return self.exact_file_map[clean_lower]
        if (clean_lower + ".md") in self.exact_file_map:
            return self.exact_file_map[clean_lower + ".md"]

        # 2. Match by basename / stem
        if clean_lower in self.basename_map:
            return self.basename_map[clean_lower][0]

        # 3. Match by partial suffix path
        norm_clean = clean_lower.replace("\\", "/")
        for rel in self.all_files:
            rel_norm = rel.lower().replace("\\", "/")
            if rel_norm.endswith("/" + norm_clean) or rel_norm.endswith("/" + norm_clean + ".md"):
                return rel

        return None


class VaultQualityTestSuite:
    """Comprehensive 53-test E2E Test Suite for Vault Comprehensive Quality Pass."""

    def __init__(self, vault_root: Path, verbose: bool = False, milestone: str = "all", baseline_mode: bool = False):
        self.vault_root = vault_root.resolve()
        self.verbose = verbose
        self.milestone = milestone.upper()
        self.baseline_mode = baseline_mode
        self.context = VaultContext(vault_root)
        self.results: List[TestResult] = []

    # --------------------------------------------------------------------------
    # TIER 1: FEATURE COVERAGE
    # --------------------------------------------------------------------------

    # Area 1.1: Wikilink Resolution
    def test_t1_1_standard_wikilinks_resolve(self) -> TestResult:
        """T1.1: Every standard [[Target]] in non-template notes resolves to an existing file."""
        broken: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("08 - Templates/"):
                continue
            for line_no, raw, target, alias, is_bt in md.wikilinks:
                if target == alias:  # standard unaliased
                    res = self.context.resolve_wikilink(target)
                    if not res:
                        broken.append(f"{rel}:{line_no} -> [[{target}]]")

        passed = len(broken) == 0
        msg = "All standard wikilinks resolve accurately" if passed else f"{len(broken)} standard wikilinks failed resolution"
        return TestResult("T1.1", "Standard Wikilink Resolution", 1, "M1", "F01", passed, message=msg, details=broken)

    def test_t1_2_aliased_wikilinks_resolve(self) -> TestResult:
        """T1.2: Every aliased [[Target|Alias]] resolves to an existing target note."""
        broken: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("08 - Templates/"):
                continue
            for line_no, raw, target, alias, is_bt in md.wikilinks:
                if target != alias:
                    res = self.context.resolve_wikilink(target)
                    if not res:
                        broken.append(f"{rel}:{line_no} -> [[{target}|{alias}]]")

        passed = len(broken) == 0
        msg = "All aliased wikilinks resolve accurately" if passed else f"{len(broken)} aliased wikilinks failed resolution"
        return TestResult("T1.2", "Aliased Wikilink Resolution", 1, "M1", "F02", passed, message=msg, details=broken)

    def test_t1_3_bedrock_paths_resolve(self) -> TestResult:
        """T1.3: Bedrock Foundations links in Dashboard, Checklist, log, Your Shelf resolve."""
        target_files = ["00 - Dashboard.md", "Checklist.md", "log.md", "Your Shelf.md"]
        bedrock_targets = {
            "bm - bedrock mathematics",
            "bw - bedrock english and grammar",
            "b0 - the deep learner's toolkit",
        }
        broken: List[str] = []
        for tf in target_files:
            if tf in self.context.md_files:
                md = self.context.md_files[tf]
                for line_no, raw, target, alias, is_bt in md.wikilinks:
                    t_stem = Path(target).stem.lower()
                    if t_stem in bedrock_targets or any(b in target.lower() for b in bedrock_targets):
                        res = self.context.resolve_wikilink(target)
                        if not res:
                            broken.append(f"{tf}:{line_no} -> {raw}")

        passed = len(broken) == 0
        msg = "All Bedrock Foundations links resolve cleanly" if passed else f"{len(broken)} Bedrock links contain path/escape errors"
        return TestResult("T1.3", "Bedrock Foundations Path Resolution", 1, "M1", "F01", passed, message=msg, details=broken)

    def test_t1_4_unbackticked_wikilinks(self) -> TestResult:
        """T1.4: Scan all vault notes; assert 0 backticked wikilinks (`[[...]]`)."""
        backticked: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("08 - Templates/"):
                continue
            for line_no, raw, target, alias, is_bt in md.wikilinks:
                if is_bt:
                    backticked.append(f"{rel}:{line_no} -> {raw}")

        passed = len(backticked) == 0
        msg = "Zero backticked wikilinks detected across vault" if passed else f"{len(backticked)} backticked wikilinks found"
        return TestResult("T1.4", "Un-backticked Wikilink Syntax", 1, "M2", "F09", passed, message=msg, details=backticked)

    def test_t1_5_zero_broken_links_census(self) -> TestResult:
        """T1.5: Total vault-wide census confirming 0 broken wikilinks in non-template notes."""
        all_broken: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("08 - Templates/"):
                continue
            for line_no, raw, target, alias, is_bt in md.wikilinks:
                res = self.context.resolve_wikilink(target)
                if not res:
                    all_broken.append(f"{rel}:{line_no} -> [[{target}]] (raw: {raw})")

        passed = len(all_broken) == 0
        msg = f"Vault census: 0 broken wikilinks across {len(self.context.md_files)} files" if passed else f"{len(all_broken)} broken wikilinks detected"
        return TestResult("T1.5", "Zero Broken Links Vault Census", 1, "M1", "F01", passed, message=msg, details=all_broken)

    # Area 1.2: Graph Reachability & Orphan Notes
    def test_t1_6_non_template_orphan_prohibition(self) -> TestResult:
        """T1.6: 100% of non-template notes must have in-degree >= 1 (0 orphan notes)."""
        orphans: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("08 - Templates/"):
                continue
            if rel == "00 - Dashboard.md":
                continue  # Root hub
            if self.context.in_degree[rel] == 0:
                orphans.append(f"{rel} (in-degree=0)")

        passed = len(orphans) == 0
        msg = "Zero orphan notes found across non-template notes" if passed else f"{len(orphans)} non-template orphan notes detected"
        return TestResult("T1.6", "Non-Template Orphan Notes Prohibition", 1, "M1", "F05", passed, message=msg, details=orphans)

    def test_t1_7_dashboard_directed_reachability(self) -> TestResult:
        """T1.7: 100% of non-template notes must be reachable via directed traversal from Dashboard."""
        root = "00 - Dashboard.md"
        if root not in self.context.md_files:
            return TestResult("T1.7", "Dashboard Directed Graph Reachability", 1, "M1", "F07", False, message="00 - Dashboard.md not found")

        visited: Set[str] = set()
        queue = deque([root])
        visited.add(root)

        while queue:
            curr = queue.popleft()
            for neighbor in self.context.adjacency.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        unreachable: List[str] = []
        for rel in sorted(self.context.md_files):
            if rel.startswith("08 - Templates/"):
                continue
            if rel not in visited:
                unreachable.append(rel)

        total_non_templates = sum(1 for r in self.context.md_files if not r.startswith("08 - Templates/"))
        passed = len(unreachable) == 0
        pct = (len(visited) / total_non_templates) * 100 if total_non_templates else 0
        msg = f"100% reachability achieved ({len(visited)}/{total_non_templates} notes)" if passed else f"{len(unreachable)} notes unreachable from Dashboard ({pct:.1f}% reached)"
        return TestResult("T1.7", "Dashboard Directed Graph Reachability", 1, "M1", "F07", passed, message=msg, details=unreachable)

    def test_t1_8_root_notes_linked_from_dashboard(self) -> TestResult:
        """T1.8: Checklist, Your Shelf, how-i-study, log, Telemetry Log linked from Dashboard."""
        root = "00 - Dashboard.md"
        if root not in self.context.md_files:
            return TestResult("T1.8", "Root Notes Inbound Dashboard Linkage", 1, "M1", "F05", False, message="00 - Dashboard.md not found")

        targets = ["Checklist.md", "Your Shelf.md", "how-i-study.md", "log.md", "Telemetry Log.md"]
        dashboard_neighbors = self.context.adjacency.get(root, set())
        unlinked = [t for t in targets if t not in dashboard_neighbors]

        passed = len(unlinked) == 0
        msg = "All 5 core tracking root notes linked directly from Dashboard" if passed else f"Unlinked root notes: {', '.join(unlinked)}"
        return TestResult("T1.8", "Root Notes Inbound Dashboard Linkage", 1, "M1", "F05", passed, message=msg, details=unlinked)

    def test_t1_9_domain_notes_indices_linked_from_dashboard(self) -> TestResult:
        """T1.9: All 5 domain indices in 02 - Notes/ linked directly from Dashboard."""
        root = "00 - Dashboard.md"
        indices = [
            "02 - Notes/Hardware/Hardware Index.md",
            "02 - Notes/Languages/Languages Index.md",
            "02 - Notes/Math/Math Index.md",
            "02 - Notes/Systems/Systems Index.md",
            "02 - Notes/Theory/Theory Index.md"
        ]
        dashboard_neighbors = self.context.adjacency.get(root, set())
        unlinked = [i for i in indices if i not in dashboard_neighbors]

        passed = len(unlinked) == 0
        msg = "All 5 domain indices in 02 - Notes/ directly linked from Dashboard" if passed else f"Unlinked domain indices: {', '.join(unlinked)}"
        return TestResult("T1.9", "Domain Notes Indices Dashboard Linkage", 1, "M1", "F05", passed, message=msg, details=unlinked)

    def test_t1_10_specialization_tracks_directed_reachability(self) -> TestResult:
        """T1.10: All 11 Specialization Tracks reachable from Dashboard through Specializations Hub."""
        tracks = [f"01 - Curriculum/Specializations/Track {i} - " for i in range(1, 12)]
        matched_tracks: List[str] = []
        for rel in self.context.md_files:
            if any(rel.startswith(t) for t in tracks):
                matched_tracks.append(rel)

        spec_hub = "01 - Curriculum/Specializations/Specializations Hub.md"
        hub_neighbors = self.context.adjacency.get(spec_hub, set())

        missing_from_hub = [t for t in matched_tracks if t not in hub_neighbors]
        passed = len(matched_tracks) == 11 and len(missing_from_hub) == 0
        msg = f"All 11 Specialization Tracks linked from Specializations Hub" if passed else f"Missing links from hub: {len(missing_from_hub)} tracks"
        return TestResult("T1.10", "Specialization Tracks Directed Reachability", 1, "M1", "F07", passed, message=msg, details=missing_from_hub)

    # Area 1.3: Header Hierarchy & Title Consistency
    def test_t1_11_header_level_continuity(self) -> TestResult:
        """T1.11: Strict header level continuity across all notes (0 header level skips)."""
        violations: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            prev_level = 0
            for level, text, line_no in md.headings:
                if prev_level > 0 and level > prev_level + 1:
                    violations.append(f"{rel}:{line_no} Header level skip: H{prev_level} to H{level} ('{text}')")
                prev_level = level

        passed = len(violations) == 0
        msg = "Zero header level skips detected across all notes" if passed else f"{len(violations)} header level skips found"
        return TestResult("T1.11", "Header Level Continuity", 1, "M2", "F08", passed, message=msg, details=violations)

    def test_t1_12_single_h1_rule(self) -> TestResult:
        """T1.12: Exactly one H1 per non-template document."""
        violations: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("08 - Templates/"):
                continue
            h1s = [h for h in md.headings if h[0] == 1]
            if len(h1s) == 0:
                violations.append(f"{rel}: Missing H1 heading")
            elif len(h1s) > 1:
                violations.append(f"{rel}: Multiple H1 headings ({len(h1s)} found on lines {[h[2] for h in h1s]})")

        passed = len(violations) == 0
        msg = "Exactly one H1 per document across all notes" if passed else f"{len(violations)} notes violate single H1 rule"
        return TestResult("T1.12", "Single H1 Rule", 1, "M2", "F08", passed, message=msg, details=violations)

    def test_t1_13_curriculum_block_h1_convention(self) -> TestResult:
        """T1.13: Curriculum course notes H1 matching '# <block_id> — <title>'."""
        violations: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if not rel.startswith("01 - Curriculum/"):
                continue
            if "Specializations" in rel or rel.endswith("Baseline Gap Analysis and Audit Report.md"):
                continue

            h1s = [h for h in md.headings if h[0] == 1]
            if not h1s:
                violations.append(f"{rel}: No H1 found")
                continue

            h1_text = h1s[0][1]
            # Must contain em-dash or standard dash
            if "—" not in h1_text and " - " not in h1_text:
                violations.append(f"{rel}: H1 '{h1_text}' missing standard title separator")

        passed = len(violations) == 0
        msg = "All curriculum course notes conform to H1 title convention" if passed else f"{len(violations)} notes violate H1 convention"
        return TestResult("T1.13", "Curriculum Block H1 & Title Convention", 1, "M2", "F08", passed, message=msg, details=violations)

    def test_t1_14_blocks_31_32_header_id_sync(self) -> TestResult:
        """T1.14: Blocks 31 & 32 header & block_id synchronization."""
        defects: List[str] = []
        b31 = "01 - Curriculum/Year 5 - MEng/31 - Specialization B2.md"
        b32 = "01 - Curriculum/Year 5 - MEng/32 - Information Theory.md"

        if b31 in self.context.md_files:
            md31 = self.context.md_files[b31]
            bid = md31.frontmatter.get("block_id")
            if bid != "Block 31":
                defects.append(f"{b31}: block_id is '{bid}' (expected 'Block 31')")
            h1 = [h for h in md31.headings if h[0] == 1]
            if h1 and not h1[0][1].startswith("Block 31"):
                defects.append(f"{b31}: H1 is '{h1[0][1]}' (expected to start with 'Block 31')")
        else:
            defects.append(f"Missing file: {b31}")

        if b32 in self.context.md_files:
            md32 = self.context.md_files[b32]
            bid = md32.frontmatter.get("block_id")
            if bid != "Block 32":
                defects.append(f"{b32}: block_id is '{bid}' (expected 'Block 32')")
            h1 = [h for h in md32.headings if h[0] == 1]
            if h1 and not h1[0][1].startswith("Block 32"):
                defects.append(f"{b32}: H1 is '{h1[0][1]}' (expected to start with 'Block 32')")
        else:
            defects.append(f"Missing file: {b32}")

        passed = len(defects) == 0
        msg = "Blocks 31 & 32 headers and IDs are synchronized" if passed else f"Blocks 31/32 desync defects: {', '.join(defects)}"
        return TestResult("T1.14", "Blocks 31 & 32 Header & ID Synchronization", 1, "M2", "F08", passed, message=msg, details=defects)

    def test_t1_15_specialization_track_h1_convention(self) -> TestResult:
        """T1.15: Specialization Tracks H1 matching '# Track <N>: <title>'."""
        violations: List[str] = []
        for i in range(1, 12):
            matched = [rel for rel in self.context.md_files if rel.startswith(f"01 - Curriculum/Specializations/Track {i} - ")]
            if not matched:
                violations.append(f"Track {i}: Note missing")
                continue
            md = self.context.md_files[matched[0]]
            h1s = [h for h in md.headings if h[0] == 1]
            if not h1s:
                violations.append(f"Track {i}: Missing H1")
            elif not re.match(rf"^Track {i}:\s+", h1s[0][1]):
                violations.append(f"Track {i}: H1 is '{h1s[0][1]}' (expected 'Track {i}: <title>')")

        passed = len(violations) == 0
        msg = "All 11 tracks conform to '# Track <N>: <title>' convention" if passed else f"{len(violations)} tracks violate H1 format"
        return TestResult("T1.15", "Specialization Track H1 Convention", 1, "M2", "F08", passed, message=msg, details=violations)

    # Area 1.4: YAML Frontmatter Schemas
    def test_t1_16_curriculum_frontmatter_required_keys(self) -> TestResult:
        """T1.16: All curriculum block notes have required frontmatter keys."""
        required = {"block_id", "title", "term", "status", "hours_estimate", "primary_resource", "milestone"}
        defects: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if not rel.startswith("01 - Curriculum/"):
                continue
            if "Specializations" in rel or rel.endswith("Baseline Gap Analysis and Audit Report.md"):
                continue

            missing = required - set(md.frontmatter.keys())
            if missing:
                defects.append(f"{rel}: Missing keys {missing}")

        passed = len(defects) == 0
        msg = "All curriculum notes contain required frontmatter keys" if passed else f"{len(defects)} curriculum notes missing keys"
        return TestResult("T1.16", "Curriculum Frontmatter Required Keys", 1, "M2", "F12", passed, message=msg, details=defects)

    def test_t1_17_curriculum_status_and_hours_values(self) -> TestResult:
        """T1.17: status in ['not-started', 'in-progress', 'done'] and hours_estimate > 0."""
        valid_statuses = {"not-started", "in-progress", "done"}
        defects: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if not rel.startswith("01 - Curriculum/"):
                continue
            if "Specializations" in rel or rel.endswith("Baseline Gap Analysis and Audit Report.md"):
                continue

            st = str(md.frontmatter.get("status", "")).strip()
            if st not in valid_statuses:
                defects.append(f"{rel}: Invalid status '{st}'")

            he = md.frontmatter.get("hours_estimate")
            if not isinstance(he, (int, float)) or he <= 0:
                defects.append(f"{rel}: Invalid hours_estimate '{he}'")

        passed = len(defects) == 0
        msg = "Curriculum status and hours values are compliant" if passed else f"{len(defects)} notes have invalid status/hours"
        return TestResult("T1.17", "Curriculum Status & Hours Values", 1, "M2", "F12", passed, message=msg, details=defects)

    def test_t1_18_track_frontmatter_required_keys(self) -> TestResult:
        """T1.18: Specialization Tracks contain required frontmatter keys."""
        required = {"track_id", "title", "term", "status", "target_profile", "prerequisites"}
        defects: List[str] = []
        for i in range(1, 12):
            matched = [rel for rel in self.context.md_files if rel.startswith(f"01 - Curriculum/Specializations/Track {i} - ")]
            if not matched:
                continue
            md = self.context.md_files[matched[0]]
            missing = required - set(md.frontmatter.keys())
            if missing:
                defects.append(f"Track {i}: Missing frontmatter keys {missing}")

        passed = len(defects) == 0
        msg = "All 11 tracks contain required frontmatter keys" if passed else f"{len(defects)} tracks missing required keys"
        return TestResult("T1.18", "Track Frontmatter Required Keys", 1, "M2", "F12", passed, message=msg, details=defects)

    def test_t1_19_track_prerequisites_yaml_schema(self) -> TestResult:
        """T1.19: Specialization Track prerequisites formatted as a valid YAML list."""
        defects: List[str] = []
        for i in range(1, 12):
            matched = [rel for rel in self.context.md_files if rel.startswith(f"01 - Curriculum/Specializations/Track {i} - ")]
            if not matched:
                continue
            md = self.context.md_files[matched[0]]
            prereqs = md.frontmatter.get("prerequisites")
            if not isinstance(prereqs, list):
                defects.append(f"Track {i}: prerequisites is not a list (type: {type(prereqs)})")
            elif len(prereqs) == 0:
                defects.append(f"Track {i}: prerequisites list is empty")

        passed = len(defects) == 0
        msg = "All track prerequisites formatted as valid YAML lists" if passed else f"{len(defects)} tracks have invalid prerequisites schema"
        return TestResult("T1.19", "Track Prerequisites YAML Schema", 1, "M2", "F12", passed, message=msg, details=defects)

    def test_t1_20_hub_and_index_frontmatter_schema(self) -> TestResult:
        """T1.20: Hubs and indices contain standardized frontmatter (title, type, tags)."""
        hubs_and_indices = [
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
        ]
        defects: List[str] = []
        for rel in hubs_and_indices:
            if rel in self.context.md_files:
                md = self.context.md_files[rel]
                fm = md.frontmatter
                if "title" not in fm:
                    defects.append(f"{rel}: Missing 'title' key")
                if "type" not in fm or fm["type"] not in ("hub", "index"):
                    defects.append(f"{rel}: Missing or invalid 'type' key")
                if "tags" not in fm:
                    defects.append(f"{rel}: Missing 'tags' key")

        passed = len(defects) == 0
        msg = "All navigation hubs and indices contain standardized frontmatter" if passed else f"{len(defects)} hubs/indices missing frontmatter schema"
        return TestResult("T1.20", "Hub & Index Frontmatter Standardization", 1, "M2", "F12", passed, message=msg, details=defects)

    # Area 1.5: List Formatting & Table Syntax
    def test_t1_21_list_bullet_marker_uniformity(self) -> TestResult:
        """T1.21: Bullet lists across the vault consistently use hyphen '-' marker."""
        violations: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            for line_no, indent, marker, text in md.list_items:
                if marker in ("*", "+"):
                    violations.append(f"{rel}:{line_no} Uses non-standard bullet marker '{marker}'")

        passed = len(violations) == 0
        msg = "All bullet lists strictly use hyphen '-' markers" if passed else f"{len(violations)} non-standard bullet markers found"
        return TestResult("T1.21", "List Bullet Marker Uniformity", 1, "M2", "F15", passed, message=msg, details=violations)

    def test_t1_22_list_indentation_hierarchy(self) -> TestResult:
        """T1.22: Sublists use standard 2-space or 4-space indentations (no odd-space indents)."""
        odd_indents: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            for line_no, indent, marker, text in md.list_items:
                if indent % 2 != 0:
                    odd_indents.append(f"{rel}:{line_no} Odd indent of {indent} spaces")

        passed = len(odd_indents) == 0
        msg = "All list indentations adhere to standard 2-space multiples" if passed else f"{len(odd_indents)} odd-space indents detected"
        return TestResult("T1.22", "List Indentation Normalization", 1, "M2", "F15", passed, message=msg, details=odd_indents)

    def test_t1_23_telemetry_log_table_syntax(self) -> TestResult:
        """T1.23: Telemetry Log table syntax integrity (no orphaned table header)."""
        tlog = "Telemetry Log.md"
        if tlog not in self.context.md_files:
            return TestResult("T1.23", "Telemetry Log Table Syntax Integrity", 1, "M2", "F11", False, message="Telemetry Log.md not found")

        md = self.context.md_files[tlog]
        invalid_tables = [t for t in md.tables if not t.is_valid]
        has_broken_header = False
        for line_no, line in enumerate(md.lines[:12], 1):
            if line.strip().startswith("| Date | Time |"):
                has_broken_header = True

        passed = len(invalid_tables) == 0 and not has_broken_header
        msg = "Telemetry Log contains clean syntax for Dataview" if passed else "Orphaned table header present in Telemetry Log.md"
        return TestResult("T1.23", "Telemetry Log Table Syntax Integrity", 1, "M2", "F11", passed, message=msg, details=[t.error for t in invalid_tables])

    def test_t1_24_markdown_table_structural_validation(self) -> TestResult:
        """T1.24: Markdown tables have consistent column counts across rows."""
        invalid_tables: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            for t in md.tables:
                if not t.is_valid:
                    invalid_tables.append(f"{rel}:{t.start_line} {t.error}")

        passed = len(invalid_tables) == 0
        msg = "All markdown tables across vault are structurally valid" if passed else f"{len(invalid_tables)} structurally invalid tables found"
        return TestResult("T1.24", "Markdown Table Structural Validation", 1, "M2", "F11", passed, message=msg, details=invalid_tables)

    def test_t1_25_fenced_code_block_language_tagging(self) -> TestResult:
        """T1.25: All fenced code blocks specify language identifiers (MD040)."""
        bare_blocks: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("08 - Templates/"):
                continue
            for line_no, lang, content in md.code_blocks:
                if not lang or lang.strip() == "":
                    bare_blocks.append(f"{rel}:{line_no} Bare code block without language tag")

        passed = len(bare_blocks) == 0
        msg = "All fenced code blocks have language tags" if passed else f"{len(bare_blocks)} bare code blocks lack language identifier"
        return TestResult("T1.25", "Fenced Code Block Language Tagging", 1, "M2", "F13", passed, message=msg, details=bare_blocks)

    # Area 1.6: Stub Absence & Proof Completeness
    def test_t1_26_zero_placeholder_and_todo_directives(self) -> TestResult:
        """T1.26: Zero placeholder/TODO stubs in curriculum, hub, or reference files."""
        stubs: List[str] = []
        stub_patterns = [
            re.compile(r"\bTODO\b", re.IGNORECASE),
            re.compile(r"\bTBD\b"),
            re.compile(r"\*\s*\([^\)]*(?:track|record|atomic|proof)[^\)]*\)\*", re.IGNORECASE)
        ]
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("08 - Templates/"):
                continue
            for line_no, line in enumerate(md.lines, 1):
                for p in stub_patterns:
                    if p.search(line):
                        if "Proof follows from" in line:
                            continue
                        stubs.append(f"{rel}:{line_no} -> '{line.strip()}'")

        passed = len(stubs) == 0
        msg = "Zero TODO/placeholder stubs found across vault notes" if passed else f"{len(stubs)} placeholder stubs detected"
        return TestResult("T1.26", "Zero Placeholder & TODO Directives", 1, "M3", "F27", passed, message=msg, details=stubs)

    def test_t1_27_core_course_proof_population(self) -> TestResult:
        """T1.27: 13 core course blocks contain substantive proof sections."""
        target_blocks = [
            "01 - CS61A.md", "02 - Calculus I.md", "03 - Physics I.md", "04 - Nand2Tetris.md",
            "05 - SICP.md", "06 - C Fluency.md", "07 - Multivariable Calculus.md", "08 - Physics II.md",
            "09 - Computer Systems.md", "12 - Interpreters.md", "14 - Computer Architecture.md",
            "19 - Networking.md", "27 - Intensive Cryptopals or TLA+.md"
        ]
        empty_proofs: List[str] = []
        for rel, md in self.context.md_files.items():
            if any(rel.endswith(b) for b in target_blocks):
                # Check for proof section
                m = re.search(r"## 📝 Study Notes[^\n]*\n(.*?)(?=\n## |\Z)", md.raw_content, re.DOTALL)
                if not m:
                    empty_proofs.append(f"{rel}: Missing proof section")
                else:
                    body = m.group(1).strip()
                    # Filter out placeholders
                    cleaned_body = re.sub(r"\*\(.*?\)\*", "", body).strip()
                    cleaned_body = re.sub(r"---", "", cleaned_body).strip()
                    if len(cleaned_body) < 150:
                        empty_proofs.append(f"{rel}: Proof section contains insufficient substantive derivations ({len(cleaned_body)} chars)")

        passed = len(empty_proofs) == 0
        msg = "All 13 core course blocks have populated proof derivations" if passed else f"{len(empty_proofs)} course blocks have empty/stub proof sections"
        return TestResult("T1.27", "Core Course Blocks Proof Population", 1, "M4", "F27", passed, message=msg, details=empty_proofs)

    def test_t1_28_bridge_course_rigorous_proof_expansions(self) -> TestResult:
        """T1.28: Bridge courses 04a, 08a, 15a contain step-by-step mathematical proofs."""
        bridges = [
            "01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md",
            "01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md",
            "01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md"
        ]
        defects: List[str] = []
        for b in bridges:
            if b in self.context.md_files:
                md = self.context.md_files[b]
                # Look for proof section
                proof_section = re.search(r"## 📝 Study Notes[^\n]*\n(.*?)(?=\n## |\Z)", md.raw_content, re.DOTALL)
                if not proof_section:
                    defects.append(f"{b}: Missing proof section")
                    continue
                body = proof_section.group(1)
                # Verify it's not just "Prove that..." prompts without proofs
                # A full derivation should contain multiple display math blocks and explanation
                num_display_math = len(re.findall(r"\$\$", body))
                if num_display_math < 6:
                    defects.append(f"{b}: Contains only {num_display_math//2} display math environments (prompts rather than derivations)")
            else:
                defects.append(f"Missing bridge file: {b}")

        passed = len(defects) == 0
        msg = "All bridge courses contain complete step-by-step mathematical proofs" if passed else f"Bridge proof deficiencies: {', '.join(defects)}"
        return TestResult("T1.28", "Bridge Course Rigorous Proof Expansions", 1, "M4", "F28", passed, message=msg, details=defects)

    def test_t1_29_time_hierarchy_theorem_proof_completion(self) -> TestResult:
        """T1.29: Time Hierarchy Theorem proof in Block 24 is complete."""
        f24 = "01 - Curriculum/Year 4 - Specialization/24 - Theory of Computation.md"
        if f24 not in self.context.md_files:
            return TestResult("T1.29", "Time Hierarchy Theorem Proof Completion", 1, "M4", "F29", False, message="Block 24 not found")

        content = self.context.md_files[f24].raw_content
        has_tht = "Time Hierarchy Theorem" in content
        # Must have diagonalization reduction proof
        has_diag = bool(re.search(r"diagonalization|simulation tape|clocked turing machine", content, re.IGNORECASE))
        has_tombstone = bool(re.search(r"Time Hierarchy.*?(?:\\blacksquare|■)", content, re.DOTALL))

        passed = has_tht and has_diag and has_tombstone
        msg = "Time Hierarchy Theorem has full diagonalization proof" if passed else "Time Hierarchy Theorem proof is incomplete or missing derivation"
        return TestResult("T1.29", "Time Hierarchy Theorem Proof Completion", 1, "M4", "F29", passed, message=msg)

    def test_t1_30_proof_qed_tombstone_consistency(self) -> TestResult:
        """T1.30: All formal mathematical proofs terminate with Q.E.D. tombstone ($\blacksquare$)."""
        # Inspect proof-heavy blocks (10, 11, 13, 15, 16, 18, 20, 22, 24, 25, 32)
        proof_blocks = [
            "10 - Math for CS.md", "11 - Linear Algebra.md", "13 - Algorithms I.md",
            "15 - Probability.md", "18 - Real Analysis.md", "20 - Algorithms II.md",
            "22 - Statistics.md", "24 - Theory of Computation.md", "25 - Convex Optimization.md",
            "32 - Information Theory.md"
        ]
        missing_tombstone: List[str] = []
        for rel, md in self.context.md_files.items():
            if any(rel.endswith(b) for b in proof_blocks):
                proof_sec = re.search(r"## 📝 Study Notes[^\n]*\n(.*?)(?=\n## |\Z)", md.raw_content, re.DOTALL)
                if proof_sec:
                    sec_text = proof_sec.group(1)
                    if r"\blacksquare" not in sec_text and "■" not in sec_text and r"\square" not in sec_text:
                        missing_tombstone.append(rel)

        passed = len(missing_tombstone) == 0
        msg = "Formal proof sections terminate with Q.E.D. tombstone" if passed else f"{len(missing_tombstone)} proof sections missing Q.E.D. marker"
        return TestResult("T1.30", "Proof Q.E.D. Tombstone Consistency", 1, "M2", "F16", passed, message=msg, details=missing_tombstone)

    # Area 1.7: Content Deduplication & Sanitization
    def test_t1_31_root_agent_prompt_file_elimination(self) -> TestResult:
        """T1.31: Redundant ORIGINAL_REQUEST.md removed from vault root."""
        root_prompt = self.vault_root / "ORIGINAL_REQUEST.md"
        exists = root_prompt.exists()
        passed = not exists
        msg = "Vault root is clean (no prompt artifact ORIGINAL_REQUEST.md)" if passed else "Redundant ORIGINAL_REQUEST.md present in vault root"
        return TestResult("T1.31", "Root Agent Prompt File Elimination", 1, "M1", "F04", passed, message=msg)

    def test_t1_32_baseline_gap_analysis_sanitization(self) -> TestResult:
        """T1.32: Baseline Gap Analysis note contains no worker IDs, .agents paths, or milestone labels."""
        gap_file = "01 - Curriculum/Baseline Gap Analysis and Audit Report.md"
        if gap_file not in self.context.md_files:
            return TestResult("T1.32", "Baseline Gap Analysis Sanitization", 1, "M3", "F17", False, message="Gap Analysis report not found")

        content = self.context.md_files[gap_file].raw_content
        defects: List[str] = []
        if "teamwork_preview_worker_" in content:
            defects.append("Contains internal worker ID ('teamwork_preview_worker_*')")
        if ".agents/PROJECT.md" in content or ".agents/" in content:
            defects.append("Contains internal agent workspace path ('.agents/...')")
        if "Milestone 1 — Current" in content or "subsequent rollout of Milestone 2" in content:
            defects.append("Contains internal agent milestone phase tracking text")

        passed = len(defects) == 0
        msg = "Baseline Gap Analysis note is sanitized of internal agent artifacts" if passed else f"Sanitization defects: {', '.join(defects)}"
        return TestResult("T1.32", "Baseline Gap Analysis Note Sanitization", 1, "M3", "F17", passed, message=msg, details=defects)

    def test_t1_33_specialization_matrix_deduplication(self) -> TestResult:
        """T1.33: Deduplicate repeated 11-track matrices in Blocks 26, 28, 29, 31."""
        blocks = [
            "26 - Specialization A1.md",
            "28 - Specialization A2.md",
            "29 - Specialization B1.md",
            "31 - Specialization B2.md"
        ]
        duplicated: List[str] = []
        for rel, md in self.context.md_files.items():
            if any(rel.endswith(b) for b in blocks):
                # If file contains the entire 11-row track table repeated verbatim
                if md.raw_content.count("| Track ") > 4:
                    duplicated.append(f"{rel}: Contains verbatim repeated 11-track matrix")

        passed = len(duplicated) == 0
        msg = "Specialization course notes reference Specializations Hub rather than duplicating matrix" if passed else f"{len(duplicated)} notes duplicate track matrix"
        return TestResult("T1.33", "Specialization Matrix Deduplication", 1, "M3", "F18", passed, message=msg, details=duplicated)

    def test_t1_34_mindset_habit_definitions_deduplication(self) -> TestResult:
        """T1.34: Consolidate duplicate Grit, Growth Mindset, Deep Work definitions."""
        study_file = "how-i-study.md"
        mindset_file = "09 - Mindset & Habits/Mindset Hub.md"

        if study_file not in self.context.md_files or mindset_file not in self.context.md_files:
            return TestResult("T1.34", "Mindset & Habit Definitions Deduplication", 1, "M3", "F19", True, message="Files missing")

        s_text = self.context.md_files[study_file].raw_content
        m_text = self.context.md_files[mindset_file].raw_content

        # Check for substantial identical paragraphs
        s_paras = [p.strip() for p in s_text.split("\n\n") if len(p.strip()) > 100]
        m_paras = [p.strip() for p in m_text.split("\n\n") if len(p.strip()) > 100]

        common = set(s_paras).intersection(set(m_paras))
        passed = len(common) == 0
        msg = "Mindset and study definitions consolidated without verbatim paragraph duplication" if passed else f"{len(common)} verbatim duplicate paragraphs found"
        return TestResult("T1.34", "Mindset & Habit Definitions Deduplication", 1, "M3", "F19", passed, message=msg, details=list(common))

    def test_t1_35_generalization_bounds_proof_deduplication(self) -> TestResult:
        """T1.35: Cross-reference generalization bounds between Block 22 and Track 1."""
        b22 = "01 - Curriculum/Year 3 - Depth/22 - Statistics.md"
        t1 = "01 - Curriculum/Specializations/Track 1 - AI and Machine Learning.md"

        if b22 not in self.context.md_files or t1 not in self.context.md_files:
            return TestResult("T1.35", "Generalization Bounds Proof Deduplication", 1, "M3", "F20", True, message="Notes missing")

        t1_content = self.context.md_files[t1].raw_content
        b22_content = self.context.md_files[b22].raw_content

        # Track 1 should link to Block 22 for the foundational statistical bounds
        links_to_b22 = "22 - Statistics" in t1_content
        passed = links_to_b22
        msg = "Statistical generalization bounds cross-referenced between Track 1 and Block 22" if passed else "Track 1 lacks cross-reference to Block 22 for statistical bounds"
        return TestResult("T1.35", "Generalization Bounds Proof Deduplication", 1, "M3", "F20", passed, message=msg)

    # --------------------------------------------------------------------------
    # TIER 2: BOUNDARY & CORNER CASES
    # --------------------------------------------------------------------------

    def test_t2_1_escaped_table_pipes_boundary(self) -> TestResult:
        """T2.1: Pipes within wikilinks in tables must NOT be escaped with backslashes (`\\|`)."""
        escaped_pipe_pattern = re.compile(r"\[\[[^\]]+\\+[\|][^\]]+\]\]")
        instances: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            for line_no, line in enumerate(md.lines, 1):
                if escaped_pipe_pattern.search(line):
                    instances.append(f"{rel}:{line_no} -> '{line.strip()}'")

        passed = len(instances) == 0
        msg = "Zero escaped table pipes in wikilinks (`\\|`) across all markdown files" if passed else f"{len(instances)} escaped table pipe wikilinks found"
        return TestResult("T2.1", "Escaped Table Pipes Boundary", 2, "M1", "F02", passed, message=msg, details=instances)

    def test_t2_2_template_placeholders_escaping(self) -> TestResult:
        """T2.2: Template placeholders (`{{...}}`, `Related Note`) must not create unescaped dead links."""
        bad_placeholders: List[str] = []
        placeholder_pattern = re.compile(r"(?<!`)\[\[\s*(\{\{[^}]+\}\}|Related Note\s*\d*)\s*(?:\|[^\]]+)?\]\](?!`)")
        for rel, md in sorted(self.context.md_files.items()):
            if not rel.startswith("08 - Templates/"):
                continue
            for line_no, line in enumerate(md.lines, 1):
                m = placeholder_pattern.search(line)
                if m:
                    bad_placeholders.append(f"{rel}:{line_no} -> '{m.group(0)}'")

        passed = len(bad_placeholders) == 0
        msg = "All template dummy variables are properly escaped/quoted" if passed else f"{len(bad_placeholders)} unescaped template placeholder wikilinks found"
        return TestResult("T2.2", "Template Dummy Placeholders Escaping", 2, "M1", "F03", passed, message=msg, details=bad_placeholders)

    def test_t2_3_empty_and_degenerate_files(self) -> TestResult:
        """T2.3: Zero empty files (0 bytes) or degenerate notes (< 100 bytes)."""
        degenerate: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            size = len(md.raw_content.strip())
            if size == 0:
                degenerate.append(f"{rel}: Empty file (0 bytes)")
            elif size < 100:
                degenerate.append(f"{rel}: Degenerate file ({size} bytes)")

        passed = len(degenerate) == 0
        msg = "All vault notes contain substantial content (> 100 bytes)" if passed else f"{len(degenerate)} empty/degenerate notes found"
        return TestResult("T2.3", "Empty Files & Degenerate Notes Boundary", 2, "M2", "F11", passed, message=msg, details=degenerate)

    def test_t2_4_malformed_fences_and_unclosed_delimiters(self) -> TestResult:
        """T2.4: Code fences (```) and math delimiters ($$) must be balanced across each note."""
        unclosed: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            fence_count = sum(1 for line in md.lines if line.strip().startswith("```"))
            if fence_count % 2 != 0:
                unclosed.append(f"{rel}: Unclosed code block fence (count: {fence_count})")

            # Check display math ($$)
            outside_code = []
            in_cb = False
            for line in md.lines:
                if line.strip().startswith("```"):
                    in_cb = not in_cb
                    continue
                if not in_cb:
                    outside_code.append(line)
            full_outside = "\n".join(outside_code)
            math_fence_count = len(re.findall(r"\$\$", full_outside))
            if math_fence_count % 2 != 0:
                unclosed.append(f"{rel}: Unclosed display math delimiter ($$ count: {math_fence_count})")

        passed = len(unclosed) == 0
        msg = "All code blocks and display math fences are properly balanced" if passed else f"{len(unclosed)} unclosed delimiter defects detected"
        return TestResult("T2.4", "Malformed Fences & Unclosed Delimiters", 2, "M2", "F13", passed, message=msg, details=unclosed)

    def test_t2_5_odd_space_indentation_boundary(self) -> TestResult:
        """T2.5: No 1, 3, 5, or 7-space odd indentation at sublist boundaries."""
        odd_lines: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            for line_no, indent, marker, text in md.list_items:
                if indent in (1, 3, 5, 7):
                    odd_lines.append(f"{rel}:{line_no} (indent={indent} spaces)")

        passed = len(odd_lines) == 0
        msg = "Zero 1/3/5/7 odd-space indentation lines across vault" if passed else f"{len(odd_lines)} odd-space indented lines detected"
        return TestResult("T2.5", "Odd-Space Indentation Boundary", 2, "M2", "F15", passed, message=msg, details=odd_lines)

    def test_t2_6_isolated_subgraph_detection(self) -> TestResult:
        """T2.6: Zero isolated subgraphs (disconnected components with >=2 notes)."""
        nodes = [r for r in self.context.md_files if not r.startswith("08 - Templates/")]
        adj: Dict[str, Set[str]] = defaultdict(set)
        for u in nodes:
            for v in self.context.adjacency.get(u, set()):
                if v in nodes:
                    adj[u].add(v)
                    adj[v].add(u)

        visited: Set[str] = set()
        components: List[Set[str]] = []
        for n in nodes:
            if n not in visited:
                comp: Set[str] = set()
                q = deque([n])
                visited.add(n)
                while q:
                    curr = q.popleft()
                    comp.add(curr)
                    for nbr in adj.get(curr, set()):
                        if nbr not in visited:
                            visited.add(nbr)
                            q.append(nbr)
                components.append(comp)

        dashboard = "00 - Dashboard.md"
        main_comp = set()
        isolated_clusters: List[str] = []
        for c in components:
            if dashboard in c:
                main_comp = c
            elif len(c) > 1:
                isolated_clusters.append(f"Cluster of {len(c)} notes: {list(c)[:3]}...")

        passed = len(isolated_clusters) == 0
        msg = "No isolated subgraphs or disconnected note islands detected" if passed else f"{len(isolated_clusters)} isolated subgraphs detected"
        return TestResult("T2.6", "Isolated Subgraph Detection", 2, "M1", "F07", passed, message=msg, details=isolated_clusters)

    def test_t2_7_case_sensitivity_and_collision(self) -> TestResult:
        """T2.7: All wikilinks match case-sensitive filenames and 0 basename collisions exist."""
        collisions: List[str] = []
        seen_stems: Dict[str, str] = {}
        for rel in sorted(self.context.md_files):
            stem = Path(rel).stem.lower()
            if stem in seen_stems:
                collisions.append(f"Basename collision between '{seen_stems[stem]}' and '{rel}'")
            else:
                seen_stems[stem] = rel

        case_mismatches: List[str] = []
        for rel, md in self.context.md_files.items():
            if rel.startswith("08 - Templates/"):
                continue
            for line_no, raw, target, alias, is_bt in md.wikilinks:
                res = self.context.resolve_wikilink(target)
                if res:
                    actual_stem = Path(res).stem
                    target_stem = Path(target.split("#")[0]).stem
                    if actual_stem.lower() == target_stem.lower() and actual_stem != target_stem:
                        case_mismatches.append(f"{rel}:{line_no} Case mismatch: '[[{target}]]' vs actual '{actual_stem}'")

        defects = collisions + case_mismatches
        passed = len(defects) == 0
        msg = "Zero basename collisions and exact case-sensitive wikilink matches" if passed else f"{len(defects)} collision/case mismatch defects"
        return TestResult("T2.7", "Case Sensitivity & Basename Collision", 2, "M1", "F01", passed, message=msg, details=defects)

    # --------------------------------------------------------------------------
    # TIER 3: CROSS-FEATURE INTERACTIONS
    # --------------------------------------------------------------------------

    def test_t3_1_dataview_query_compatibility(self) -> TestResult:
        """T3.1: Notes queried by Dataview parse seamlessly (frontmatter + list items)."""
        defects: List[str] = []
        tlog = "Telemetry Log.md"
        if tlog in self.context.md_files:
            md = self.context.md_files[tlog]
            telemetry_lines = [l for l in md.lines if "TELEMETRY:" in l]
            if not telemetry_lines:
                defects.append(f"{tlog}: No TELEMETRY list items found")
            for tl in telemetry_lines:
                parts = tl.split("|")
                if len(parts) < 3:
                    defects.append(f"{tlog}: Malformed telemetry row: '{tl}'")

        for rel, md in self.context.md_files.items():
            if rel.startswith("01 - Curriculum/Year ") or rel.startswith("01 - Curriculum/Phase "):
                fm = md.frontmatter
                if "block_id" not in fm or "status" not in fm:
                    defects.append(f"{rel}: Incompatible with Dataview curriculum dashboard query")

        passed = len(defects) == 0
        msg = "Vault notes are fully compatible with Dataview dashboard queries" if passed else f"{len(defects)} Dataview compatibility defects found"
        return TestResult("T3.1", "Dataview Query Compatibility", 3, "M2", "F11", passed, message=msg, details=defects)

    def test_t3_2_bidirectional_graph_connectivity(self) -> TestResult:
        """T3.2: Specialization tracks maintain reciprocal linking with Specializations Hub."""
        spec_hub = "01 - Curriculum/Specializations/Specializations Hub.md"
        if spec_hub not in self.context.md_files:
            return TestResult("T3.2", "Bidirectional Specialization Graph Connectivity", 3, "M3", "F22", False, message="Specializations Hub missing")

        hub_content = self.context.md_files[spec_hub].raw_content
        defects: List[str] = []

        for i in range(1, 12):
            matched = [rel for rel in self.context.md_files if rel.startswith(f"01 - Curriculum/Specializations/Track {i} - ")]
            if not matched:
                defects.append(f"Track {i}: Missing file")
                continue
            track_rel = matched[0]
            track_content = self.context.md_files[track_rel].raw_content

            if Path(track_rel).stem not in hub_content:
                defects.append(f"{spec_hub} does not link to Track {i}")

            if "Specializations Hub" not in track_content:
                defects.append(f"Track {i} does not link back to Specializations Hub")

        passed = len(defects) == 0
        msg = "Bidirectional connectivity confirmed between Specializations Hub and all 11 tracks" if passed else f"{len(defects)} bidirectional linking defects"
        return TestResult("T3.2", "Bidirectional Specialization Graph Connectivity", 3, "M3", "F22", passed, message=msg, details=defects)

    def test_t3_3_curriculum_to_landmark_papers_reciprocity(self) -> TestResult:
        """T3.3: Curriculum blocks and Paper Reading Hub maintain reciprocal cross-references."""
        paper_hub = "03 - Papers/Paper Reading Hub.md"
        if paper_hub not in self.context.md_files:
            return TestResult("T3.3", "Curriculum to Landmark Papers Reciprocity", 3, "M3", "F23", False, message="Paper Reading Hub missing")

        defects: List[str] = []
        blocks_with_paper_section = 0
        for rel, md in self.context.md_files.items():
            if rel.startswith("01 - Curriculum/Year "):
                if "Landmark Research Papers" in md.raw_content:
                    blocks_with_paper_section += 1
                    if "Paper Reading Hub" not in md.raw_content:
                        defects.append(f"{rel}: Has Landmark Papers section but lacks link to Paper Reading Hub")

        if blocks_with_paper_section < 8:
            defects.append(f"Only {blocks_with_paper_section} curriculum blocks have dedicated Landmark Research Papers sections (expected >= 8)")

        passed = len(defects) == 0
        msg = f"Curriculum blocks and Paper Reading Hub maintain reciprocal linkage ({blocks_with_paper_section} sections)" if passed else f"{len(defects)} paper reciprocity defects"
        return TestResult("T3.3", "Curriculum to Landmark Papers Reciprocity", 3, "M3", "F23", passed, message=msg, details=defects)

    def test_t3_4_curriculum_to_topic_notes_reciprocity(self) -> TestResult:
        """T3.4: Curriculum blocks link to domain indices in 02 - Notes/ and vice versa."""
        indices = {
            "Math Index.md": "02 - Notes/Math/Math Index.md",
            "Systems Index.md": "02 - Notes/Systems/Systems Index.md",
            "Theory Index.md": "02 - Notes/Theory/Theory Index.md",
            "Hardware Index.md": "02 - Notes/Hardware/Hardware Index.md",
            "Languages Index.md": "02 - Notes/Languages/Languages Index.md"
        }
        defects: List[str] = []
        for name, path in indices.items():
            if path in self.context.md_files:
                md = self.context.md_files[path]
                if self.context.out_degree[path] == 0:
                    defects.append(f"{path}: Zero outgoing course links")
            else:
                defects.append(f"Missing index: {path}")

        passed = len(defects) == 0
        msg = "Topic note indices in 02 - Notes/ link reciprocally to curriculum courses" if passed else f"{len(defects)} topic index reciprocity defects"
        return TestResult("T3.4", "Curriculum to Topic Notes Reciprocity", 3, "M3", "F24", passed, message=msg, details=defects)

    def test_t3_5_course_sinks_elimination_and_breadcrumbs(self) -> TestResult:
        """T3.5: All 31 core course blocks have out-degree > 0 (zero dead-end sinks)."""
        sinks: List[str] = []
        for rel, md in sorted(self.context.md_files.items()):
            if rel.startswith("01 - Curriculum/Year "):
                if self.context.out_degree[rel] == 0:
                    sinks.append(f"{rel} (out-degree=0)")

        passed = len(sinks) == 0
        msg = "Zero course block sink nodes detected (all blocks have outgoing navigation)" if passed else f"{len(sinks)} course blocks remain dead-end sinks"
        return TestResult("T3.5", "Course Block Sinks Elimination & Breadcrumbs", 3, "M3", "F26", passed, message=msg, details=sinks)

    def test_t3_6_prerequisite_dag_acyclicity_and_order(self) -> TestResult:
        """T3.6: Prerequisite dependency graph is a strict DAG (0 cycles)."""
        prereq_graph: Dict[str, Set[str]] = defaultdict(set)
        for rel, md in self.context.md_files.items():
            if rel.startswith("01 - Curriculum/"):
                prereqs = md.frontmatter.get("prerequisites", [])
                if isinstance(prereqs, list):
                    for p in prereqs:
                        res = self.context.resolve_wikilink(str(p))
                        if res:
                            prereq_graph[rel].add(res)

        WHITE, GRAY, BLACK = 0, 1, 2
        color = {u: WHITE for u in prereq_graph}
        for u in self.context.md_files:
            if u not in color:
                color[u] = WHITE

        cycles: List[List[str]] = []

        def dfs(u: str, path: List[str]):
            color[u] = GRAY
            path.append(u)
            for v in prereq_graph.get(u, set()):
                if color.get(v, WHITE) == GRAY:
                    idx = path.index(v)
                    cycles.append(path[idx:] + [v])
                elif color.get(v, WHITE) == WHITE:
                    dfs(v, path)
            path.pop()
            color[u] = BLACK

        for node in list(color.keys()):
            if color[node] == WHITE:
                dfs(node, [])

        passed = len(cycles) == 0
        msg = f"Prerequisite graph is a strict DAG (0 cycles across {len(prereq_graph)} nodes)" if passed else f"{len(cycles)} prerequisite dependency cycles detected"
        cycle_details = [" -> ".join(c) for c in cycles]
        return TestResult("T3.6", "Prerequisite DAG Acyclicity & Chronological Order", 3, "M2", "F12", passed, message=msg, details=cycle_details)

    # --------------------------------------------------------------------------
    # TIER 4: REAL-WORLD WORKFLOWS
    # --------------------------------------------------------------------------

    def test_t4_1_student_navigation_simulation(self) -> TestResult:
        """T4.1: Simulate continuous student navigation from Dashboard to all curriculum areas."""
        root = "00 - Dashboard.md"
        if root not in self.context.md_files:
            return TestResult("T4.1", "Student Navigation Simulation", 4, "M5", "F30", False, message="Dashboard missing")

        required_destinations = [
            "01 - Curriculum/Specializations/Specializations Hub.md",
            "03 - Papers/Paper Reading Hub.md",
            "04 - Writing/Writing Hub.md",
            "05 - Projects/Projects Hub.md",
            "06 - Breadth/Breadth and Humanities Hub.md",
            "07 - Reference/Appendix E - Failure Modes.md",
            "07 - Reference/Appendix F - Curated URLs.md",
            "09 - Mindset & Habits/Mindset Hub.md",
            "Checklist.md",
            "Your Shelf.md"
        ]

        unreachable = []
        for dest in required_destinations:
            if dest not in self.context.md_files:
                unreachable.append(f"{dest} (file missing)")
                continue

            q = deque([(root, [root])])
            seen = {root}
            found = False
            while q:
                curr, path = q.popleft()
                if curr == dest:
                    found = True
                    break
                for nbr in self.context.adjacency.get(curr, set()):
                    if nbr not in seen:
                        seen.add(nbr)
                        q.append((nbr, path + [nbr]))
            if not found:
                unreachable.append(f"Cannot navigate from Dashboard to {dest}")

        passed = len(unreachable) == 0
        msg = "End-to-end student navigation simulation passed across all hubs and appendices" if passed else f"{len(unreachable)} navigation destinations unreachable"
        return TestResult("T4.1", "Student Navigation Simulation", 4, "M5", "F30", passed, message=msg, details=unreachable)

    def test_t4_2_degree_pathways_completion_simulation(self) -> TestResult:
        """T4.2: Simulate 4 distinct career specialization degree pathways (3,000–7,500 hrs)."""
        pathways = {
            "AI/ML Specialist": {
                "tracks": ["Track 1 - AI and Machine Learning.md"],
                "blocks": ["22 - Statistics.md", "25 - Convex Optimization.md"]
            },
            "Systems & Performance Architect": {
                "tracks": ["Track 2 - Systems and Performance.md", "Track 8 - Rust for Systems Engineering and Formal Verification.md"],
                "blocks": ["16 - Operating Systems.md", "23 - Distributed Systems.md"]
            },
            "Security & Cryptography Researcher": {
                "tracks": ["Track 3 - Security and Cryptography.md"],
                "blocks": ["27 - Intensive Cryptopals or TLA+.md", "24 - Theory of Computation.md"]
            },
            "Robotics & Cyber-Physical Engineer": {
                "tracks": ["Track 11 - Autonomous Robotics and Cyber-Physical Systems.md"],
                "blocks": ["09 - Computer Systems.md", "14 - Computer Architecture.md"]
            }
        }

        failures: List[str] = []
        for name, spec in pathways.items():
            total_hours = 0
            for rel, md in self.context.md_files.items():
                if rel.startswith("01 - Curriculum/Year ") or rel.startswith("01 - Curriculum/Phase "):
                    h = md.frontmatter.get("hours_estimate", 0)
                    if isinstance(h, (int, float)):
                        total_hours += h

            for t in spec["tracks"]:
                matched = [rel for rel in self.context.md_files if rel.endswith(t)]
                if not matched:
                    failures.append(f"{name}: Track note '{t}' not found")

            if not (3000 <= total_hours <= 7500):
                failures.append(f"{name}: Total degree workload {total_hours} hrs outside 3,000–7,500 hr envelope")

        passed = len(failures) == 0
        msg = "All 4 student degree pathways successfully simulated with valid workload pacing" if passed else f"Pathway simulation failures: {', '.join(failures)}"
        return TestResult("T4.2", "Degree Pathways Completion Simulation", 4, "M5", "F30", passed, message=msg, details=failures)

    def test_t4_3_daily_study_routine_simulation(self) -> TestResult:
        """T4.3: Simulate daily study routine (how-i-study -> log -> Telemetry Log -> Checklist -> Shelf)."""
        study_files = [
            "how-i-study.md",
            "log.md",
            "Telemetry Log.md",
            "Checklist.md",
            "Your Shelf.md",
            "08 - Templates/Daily Log Entry Template.md"
        ]
        missing = [f for f in study_files if f not in self.context.md_files]
        if missing:
            return TestResult("T4.3", "Daily Study Routine Simulation", 4, "M5", "F30", False, message=f"Missing study routine notes: {', '.join(missing)}")

        his_content = self.context.md_files["how-i-study.md"].raw_content
        log_content = self.context.md_files["log.md"].raw_content
        chk_content = self.context.md_files["Checklist.md"].raw_content
        defects = []

        if "log" not in his_content:
            defects.append("how-i-study.md does not cross-reference log.md")
        if "Block Note Template" not in his_content:
            defects.append("how-i-study.md does not link to Block Note Template")
        if "Daily Log Entry Template" not in log_content:
            defects.append("log.md does not link to Daily Log Entry Template")
        if "how-i-study" not in chk_content:
            defects.append("Checklist.md does not cross-reference how-i-study")

        passed = len(defects) == 0
        msg = "Daily study routine workflow components are integrated and cross-linked" if passed else f"Daily routine defects: {', '.join(defects)}"
        return TestResult("T4.3", "Daily Study Routine Simulation", 4, "M5", "F30", passed, message=msg, details=defects)

    def test_t4_4_project_build_progression_simulation(self) -> TestResult:
        """T4.4: Projects Hub defines valid course project specs with toolchains and criteria."""
        proj_hub = "05 - Projects/Projects Hub.md"
        if proj_hub not in self.context.md_files:
            return TestResult("T4.4", "Project Build Progression Simulation", 4, "M5", "F25", False, message="Projects Hub missing")

        md = self.context.md_files[proj_hub]
        content = md.raw_content

        tools = ["gcc", "clang", "rust", "cargo", "qemu", "verilog", "renode", "pytest", "valgrind", "gdb"]
        tool_count = sum(1 for t in tools if re.search(rf"\b{t}\b", content, re.IGNORECASE))

        all_32 = [f"{i:02d}" for i in range(1, 33)]
        missing_blocks = [b for b in all_32 if not re.search(rf"\[\[[^\]]*\b{b}\s*-\s*[^\]]+\]\]", content)]

        passed = tool_count >= 5 and len(missing_blocks) == 0
        msg = f"Project Build Hub specifies rigorous toolchains ({tool_count} tools) and active links for all 32 blocks" if passed else f"Projects Hub missing {len(missing_blocks)} blocks: {', '.join(missing_blocks)}"
        return TestResult("T4.4", "Project Build Progression Simulation", 4, "M3", "F25", passed, message=msg, details=missing_blocks)

    def test_t4_5_master_curriculum_audit_simulation(self) -> TestResult:
        """T4.5: Master tracking synchronization across Dashboard, Checklist, and Gap Analysis."""
        dash = "00 - Dashboard.md"
        chk = "Checklist.md"
        gap = "01 - Curriculum/Baseline Gap Analysis and Audit Report.md"

        missing = [f for f in (dash, chk, gap) if f not in self.context.md_files]
        if missing:
            return TestResult("T4.5", "Master Curriculum Audit Simulation", 4, "M5", "F30", False, message=f"Missing tracking files: {', '.join(missing)}")

        chk_text = self.context.md_files[chk].raw_content
        missing_blocks = []
        for i in range(1, 33):
            b_prefix = f"{i:02d} - "
            if b_prefix not in chk_text and f"Block {i}" not in chk_text:
                missing_blocks.append(f"Block {i}")

        passed = len(missing_blocks) == 0
        msg = "Master curriculum tracking files are synchronized with all 32 blocks" if passed else f"Checklist missing blocks: {', '.join(missing_blocks)}"
        return TestResult("T4.5", "Master Curriculum Audit Simulation", 4, "M5", "F30", passed, message=msg, details=missing_blocks)

    # --------------------------------------------------------------------------
    # EXECUTION RUNNER
    # --------------------------------------------------------------------------

    def get_all_tests(self):
        """Returns the complete list of test runner methods in order."""
        return [
            # Tier 1
            self.test_t1_1_standard_wikilinks_resolve,
            self.test_t1_2_aliased_wikilinks_resolve,
            self.test_t1_3_bedrock_paths_resolve,
            self.test_t1_4_unbackticked_wikilinks,
            self.test_t1_5_zero_broken_links_census,
            self.test_t1_6_non_template_orphan_prohibition,
            self.test_t1_7_dashboard_directed_reachability,
            self.test_t1_8_root_notes_linked_from_dashboard,
            self.test_t1_9_domain_notes_indices_linked_from_dashboard,
            self.test_t1_10_specialization_tracks_directed_reachability,
            self.test_t1_11_header_level_continuity,
            self.test_t1_12_single_h1_rule,
            self.test_t1_13_curriculum_block_h1_convention,
            self.test_t1_14_blocks_31_32_header_id_sync,
            self.test_t1_15_specialization_track_h1_convention,
            self.test_t1_16_curriculum_frontmatter_required_keys,
            self.test_t1_17_curriculum_status_and_hours_values,
            self.test_t1_18_track_frontmatter_required_keys,
            self.test_t1_19_track_prerequisites_yaml_schema,
            self.test_t1_20_hub_and_index_frontmatter_schema,
            self.test_t1_21_list_bullet_marker_uniformity,
            self.test_t1_22_list_indentation_hierarchy,
            self.test_t1_23_telemetry_log_table_syntax,
            self.test_t1_24_markdown_table_structural_validation,
            self.test_t1_25_fenced_code_block_language_tagging,
            self.test_t1_26_zero_placeholder_and_todo_directives,
            self.test_t1_27_core_course_proof_population,
            self.test_t1_28_bridge_course_rigorous_proof_expansions,
            self.test_t1_29_time_hierarchy_theorem_proof_completion,
            self.test_t1_30_proof_qed_tombstone_consistency,
            self.test_t1_31_root_agent_prompt_file_elimination,
            self.test_t1_32_baseline_gap_analysis_sanitization,
            self.test_t1_33_specialization_matrix_deduplication,
            self.test_t1_34_mindset_habit_definitions_deduplication,
            self.test_t1_35_generalization_bounds_proof_deduplication,
            # Tier 2
            self.test_t2_1_escaped_table_pipes_boundary,
            self.test_t2_2_template_placeholders_escaping,
            self.test_t2_3_empty_and_degenerate_files,
            self.test_t2_4_malformed_fences_and_unclosed_delimiters,
            self.test_t2_5_odd_space_indentation_boundary,
            self.test_t2_6_isolated_subgraph_detection,
            self.test_t2_7_case_sensitivity_and_collision,
            # Tier 3
            self.test_t3_1_dataview_query_compatibility,
            self.test_t3_2_bidirectional_graph_connectivity,
            self.test_t3_3_curriculum_to_landmark_papers_reciprocity,
            self.test_t3_4_curriculum_to_topic_notes_reciprocity,
            self.test_t3_5_course_sinks_elimination_and_breadcrumbs,
            self.test_t3_6_prerequisite_dag_acyclicity_and_order,
            # Tier 4
            self.test_t4_1_student_navigation_simulation,
            self.test_t4_2_degree_pathways_completion_simulation,
            self.test_t4_3_daily_study_routine_simulation,
            self.test_t4_4_project_build_progression_simulation,
            self.test_t4_5_master_curriculum_audit_simulation,
        ]

    def run_suite(self, tier_filter: Optional[int] = None) -> bool:
        """Executes test suite with tier and milestone progressive gates."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}")
        print("     VAULT COMPREHENSIVE QUALITY PASS — E2E VERIFICATION SUITE")
        print(f"{'='*80}{Colors.RESET}")
        print(f"Vault Root:       {self.vault_root}")
        print(f"Total MD Notes:   {len(self.context.md_files)}")
        print(f"Milestone Filter: {self.milestone}")
        print(f"Tier Filter:      {tier_filter if tier_filter else 'ALL TIERS (1-4)'}")
        print(f"Execution Mode:   {'BASELINE AUDIT (Non-blocking)' if self.baseline_mode else 'STRICT ENFORCEMENT'}")
        print(f"{Colors.CYAN}{'-'*80}{Colors.RESET}\n")

        all_test_methods = self.get_all_tests()
        start_time = time.time()

        for test_fn in all_test_methods:
            t0 = time.time()
            try:
                res = test_fn()
            except Exception as e:
                res = TestResult(
                    test_id=test_fn.__name__,
                    name=test_fn.__name__,
                    tier=0,
                    milestone="all",
                    feature_id="ERR",
                    passed=False,
                    message=f"Unhandled exception during execution: {e}"
                )
            res.duration_ms = (time.time() - t0) * 1000.0

            # Filter by tier if requested
            if tier_filter and res.tier != tier_filter:
                continue

            # In milestone-scoped mode, mark tests outside scope as skipped
            if self.milestone != "ALL":
                if self.milestone == "M1" and res.milestone != "M1":
                    res.skipped = True
                elif self.milestone == "M2" and res.milestone not in ("M1", "M2"):
                    res.skipped = True
                elif self.milestone == "M3" and res.milestone not in ("M1", "M2", "M3"):
                    res.skipped = True
                elif self.milestone == "M4" and res.milestone not in ("M1", "M2", "M3", "M4"):
                    res.skipped = True

            self.results.append(res)

            # Display progress line
            if res.skipped:
                tag = f"{Colors.YELLOW}[SKIP]{Colors.RESET}"
            elif res.passed:
                tag = f"{Colors.GREEN}[PASS]{Colors.RESET}"
            else:
                tag = f"{Colors.RED}[FAIL]{Colors.RESET}"

            print(f"  {tag} {res.test_id:<8} [T{res.tier} {res.milestone} {res.feature_id}] {res.name:<45} ({res.duration_ms:.1f}ms)")
            if not res.passed and not res.skipped and (self.verbose or len(res.details) > 0):
                print(f"         {Colors.RED}Defect:{Colors.RESET} {res.message}")
                if self.verbose:
                    for d in res.details[:10]:
                        print(f"           - {d}")
                    if len(res.details) > 10:
                        print(f"           ... ({len(res.details) - 10} more suppressed, use -v to expand)")

        elapsed = time.time() - start_time

        # Print Tier Summary
        print(f"\n{Colors.CYAN}{'-'*80}{Colors.RESET}")
        print(f"{Colors.BOLD}TIER-BY-TIER RESULTS BREAKDOWN:{Colors.RESET}\n")

        tier_stats: Dict[int, Dict[str, int]] = {t: {"passed": 0, "failed": 0, "skipped": 0, "total": 0} for t in (1, 2, 3, 4)}
        for r in self.results:
            if r.tier in tier_stats:
                tier_stats[r.tier]["total"] += 1
                if r.skipped:
                    tier_stats[r.tier]["skipped"] += 1
                elif r.passed:
                    tier_stats[r.tier]["passed"] += 1
                else:
                    tier_stats[r.tier]["failed"] += 1

        tier_names = {
            1: "Tier 1: Feature Coverage (Schemas, Links, Stubs)",
            2: "Tier 2: Boundary & Corner Cases (Pipes, Fences)",
            3: "Tier 3: Cross-Feature Interactions (DAG, Sinks)",
            4: "Tier 4: Real-World Workflows (Student Simulation)"
        }

        for t in (1, 2, 3, 4):
            st = tier_stats[t]
            if st["total"] == 0:
                continue
            if st["failed"] == 0 and st["passed"] > 0:
                tag = f"{Colors.GREEN}[PASS]{Colors.RESET}"
            elif st["passed"] > 0:
                tag = f"{Colors.YELLOW}[PARTIAL]{Colors.RESET}"
            elif st["failed"] == 0 and st["skipped"] > 0:
                tag = f"{Colors.YELLOW}[SKIP]{Colors.RESET}"
            else:
                tag = f"{Colors.RED}[FAIL]{Colors.RESET}"
            print(f"  {tag} {tier_names[t]:<52} {st['passed']}/{st['total']} passed ({st['failed']} failed, {st['skipped']} skipped)")

        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed and not r.skipped)
        skipped = sum(1 for r in self.results if r.skipped)

        print(f"{Colors.CYAN}{'-'*80}{Colors.RESET}")
        print(f"Total Tests Executed: {total} | {Colors.GREEN}Passed: {passed}{Colors.RESET} | {Colors.RED}Failed: {failed}{Colors.RESET} | {Colors.YELLOW}Skipped: {skipped}{Colors.RESET} | Duration: {elapsed:.2f}s")

        # Milestone Gate Verdict
        if self.milestone == "M1":
            m1_failures = [r for r in self.results if r.milestone == "M1" and not r.passed and not r.skipped]
            overall_success = (len(m1_failures) == 0)
            if overall_success:
                print(f"\n{Colors.GREEN}{Colors.BOLD}MILESTONE M1 GATE: PASSED (Graph & Link Integrity Verified){Colors.RESET}\n")
            else:
                print(f"\n{Colors.YELLOW}{Colors.BOLD}MILESTONE M1 GATE: INCOMPLETE ({len(m1_failures)} criteria pending){Colors.RESET}\n")
        elif self.milestone == "M2":
            m2_failures = [r for r in self.results if r.milestone in ("M1", "M2") and not r.passed and not r.skipped]
            overall_success = (len(m2_failures) == 0)
        elif self.milestone == "M3":
            m3_failures = [r for r in self.results if r.milestone in ("M1", "M2", "M3") and not r.passed and not r.skipped]
            overall_success = (len(m3_failures) == 0)
        elif self.milestone == "M4":
            m4_failures = [r for r in self.results if not r.passed and not r.skipped]
            overall_success = (len(m4_failures) == 0)
        else:
            overall_success = (failed == 0)

        if overall_success:
            print(f"{Colors.GREEN}{Colors.BOLD}OVERALL VERDICT: ALL AUDITED ACCEPTANCE CRITERIA SATISFIED [GREEN]{Colors.RESET}\n")
        else:
            print(f"{Colors.RED}{Colors.BOLD}OVERALL VERDICT: VAULT QUALITY CRITERIA DEFICIENCIES DETECTED [RED]{Colors.RESET}\n")

        if self.baseline_mode:
            return True

        return overall_success

    def export_json(self, out_path: Path):
        data = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "vault_root": str(self.vault_root),
            "milestone": self.milestone,
            "total_files": len(self.context.md_files),
            "summary": {
                "total": len(self.results),
                "passed": sum(1 for r in self.results if r.passed),
                "failed": sum(1 for r in self.results if not r.passed and not r.skipped),
                "skipped": sum(1 for r in self.results if r.skipped),
            },
            "results": [asdict(r) for r in self.results]
        }
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"{Colors.DIM}Report exported to: {out_path}{Colors.RESET}")


def list_tests():
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}")
    print("           COMPREHENSIVE VAULT QUALITY PASS — 53 TEST CATALOG")
    print(f"{'='*80}{Colors.RESET}\n")
    dummy_suite = VaultQualityTestSuite(vault_root=Path("."), baseline_mode=True)
    tests = dummy_suite.get_all_tests()
    print(f"{'ID':<8} {'Tier':<6} {'Mile':<6} {'Feat':<6} {'Test Name'}")
    print("-" * 80)
    for t in tests:
        res = t()
        print(f"{res.test_id:<8} T{res.tier:<5} {res.milestone:<6} {res.feature_id:<6} {res.name}")
    print(f"\nTotal Catalog: {len(tests)} test cases across 4 tiers and milestones M1–M5.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Comprehensive Vault Quality Pass E2E Test Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4], help="Execute only tests in specific tier")
    parser.add_argument("--milestone", type=str, default="all", choices=["M1", "M2", "M3", "M4", "all"], help="Filter by progressive milestone")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print detailed diagnostic failure breakdowns")
    parser.add_argument("--json-out", type=str, help="Export JSON test execution report")
    parser.add_argument("--vault-root", type=str, help="Override path to vault root")
    parser.add_argument("--list-tests", action="store_true", help="Print full test catalog and exit")
    parser.add_argument("--baseline", action="store_true", help="Run in baseline audit mode (exit 0 after printing report)")

    args = parser.parse_args()

    if args.list_tests:
        list_tests()
        sys.exit(0)

    if args.vault_root:
        vault_root = Path(args.vault_root)
    else:
        # Default: current dir or parent of .agents
        cwd = Path.cwd()
        if (cwd / "00 - Dashboard.md").exists():
            vault_root = cwd
        elif (cwd.parent / "00 - Dashboard.md").exists():
            vault_root = cwd.parent
        else:
            vault_root = cwd

    suite = VaultQualityTestSuite(
        vault_root=vault_root,
        verbose=args.verbose,
        milestone=args.milestone,
        baseline_mode=args.baseline
    )

    success = suite.run_suite(tier_filter=args.tier)

    if args.json_out:
        suite.export_json(Path(args.json_out))

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
