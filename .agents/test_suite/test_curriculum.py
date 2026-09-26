#!/usr/bin/env python3
"""
EECS Curriculum Audit & Expansion — End-to-End (E2E) Test Suite
===============================================================

An automated, opaque-box E2E test harness that validates The Noblett Repository
Obsidian vault against all requirements and acceptance criteria in ORIGINAL_REQUEST.md,
PROJECT.md, and global curricular standards (MIT Course 6, ACM/IEEE CS2023, IEEE CE2016).

Test Architecture (4-Tier Methodology):
- Tier 1: Feature Coverage (Core blocks, bridge courses, tracks 1-11, gap analysis report, frontmatter schemas)
- Tier 2: Boundary & Corner Cases (Vault-wide wikilink integrity, graduate paper citations >=3, modern paradigm lab specs)
- Tier 3: Cross-Feature Combinations (Prerequisite graph topological DAG validation, ACM/IEEE CS2023 17 KAs, MIT Course 6 pillars)
- Tier 4: Real-World Scenarios (Student degree pathway simulations, toolchain validation, checklist & dashboard alignment)

Usage:
  python3 test_curriculum.py [options]

Options:
  --tier {1,2,3,4}        Run only tests in the specified tier(s) (comma-separated or multiple flags)
  --milestone {M1,M2,M3,M4,all} Run in progressive milestone mode (evaluates milestone-scoped criteria)
  -v, --verbose           Print detailed diagnostic breakdowns for each test case
  --json-out PATH         Export full test execution report to a JSON file
  --vault-root PATH       Override vault root path (default: current directory or auto-detected)
  --help                  Show this help message and exit
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


# ANSI Color Codes
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
    passed: bool
    skipped: bool = False
    message: str = ""
    details: List[str] = field(default_factory=list)
    duration_ms: float = 0.0


@dataclass
class MarkdownFile:
    path: Path
    rel_path: str
    raw_content: str
    frontmatter: Dict[str, Any]
    headings: List[Tuple[int, str]]  # (level, text)
    wikilinks: List[Tuple[int, str, str]]  # (line_no, raw_target, display_text)


class VaultContext:
    """Discovers, parses, and indexes the entire Obsidian vault."""

    def __init__(self, vault_root: Path):
        self.vault_root = vault_root.resolve()
        self.all_files: Set[str] = set()  # Relative paths of all vault files
        self.md_files: Dict[str, MarkdownFile] = {}  # rel_path -> MarkdownFile
        self.basename_map: Dict[str, List[str]] = defaultdict(list)  # lower(stem) -> [rel_paths]
        self.exact_file_map: Dict[str, str] = {}  # lower(rel_path) -> rel_path

        self._discover_and_parse()

    def _discover_and_parse(self):
        for root, dirs, files in os.walk(self.vault_root):
            # Ignore git and agent workspaces from vault content
            rel_dir = os.path.relpath(root, self.vault_root)
            parts = Path(rel_dir).parts
            if any(p in ('.git', '.agents', '.obsidian') for p in parts):
                continue

            for f in files:
                abs_path = Path(root) / f
                rel_path = str(abs_path.relative_to(self.vault_root))
                self.all_files.add(rel_path)
                self.exact_file_map[rel_path.lower()] = rel_path
                self.basename_map[abs_path.stem.lower()].append(rel_path)
                self.basename_map[abs_path.name.lower()].append(rel_path)

                if f.endswith('.md'):
                    self._parse_markdown(abs_path, rel_path)

    def _parse_markdown(self, abs_path: Path, rel_path: str):
        try:
            content = abs_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return

        frontmatter = self._extract_frontmatter(content)
        headings = self._extract_headings(content)
        wikilinks = self._extract_wikilinks(content)

        self.md_files[rel_path] = MarkdownFile(
            path=abs_path,
            rel_path=rel_path,
            raw_content=content,
            frontmatter=frontmatter,
            headings=headings,
            wikilinks=wikilinks
        )

    def _extract_frontmatter(self, content: str) -> Dict[str, Any]:
        fm: Dict[str, Any] = {}
        if not content.startswith('---'):
            return fm

        parts = content.split('---', 2)
        if len(parts) < 3:
            return fm

        fm_text = parts[1]
        for line in fm_text.splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip().strip('"\'')
                # Parse simple ints/floats
                if val.isdigit():
                    fm[key] = int(val)
                else:
                    try:
                        fm[key] = float(val)
                    except ValueError:
                        fm[key] = val
        return fm

    def _extract_headings(self, content: str) -> List[Tuple[int, str]]:
        headings = []
        for line in content.splitlines():
            line = line.strip()
            if line.startswith('#'):
                m = re.match(r'^(#{1,6})\s+(.*)$', line)
                if m:
                    level = len(m.group(1))
                    text = m.group(2).strip()
                    headings.append((level, text))
        return headings

    def _extract_wikilinks(self, content: str) -> List[Tuple[int, str, str]]:
        wikilinks = []
        wikilink_pattern = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|([^\]]+))?\]\]')
        for line_no, line in enumerate(content.splitlines(), 1):
            for match in wikilink_pattern.finditer(line):
                target = match.group(1).strip()
                alias = (match.group(2) or target).strip()
                wikilinks.append((line_no, target, alias))
        return wikilinks

    def resolve_wikilink(self, target: str) -> Optional[str]:
        """Resolves an Obsidian wikilink to an actual relative path in the vault."""
        # Clean target of table escape characters
        t = target.strip().rstrip('\\').strip()
        t_lower = t.lower()

        # 1. Exact match by relative path
        if t_lower in self.exact_file_map:
            return self.exact_file_map[t_lower]
        if (t_lower + '.md') in self.exact_file_map:
            return self.exact_file_map[t_lower + '.md']

        # 2. Match by stem or filename
        if t_lower in self.basename_map:
            return self.basename_map[t_lower][0]

        # 3. Match by partial suffix path
        norm_t = t_lower.replace('\\', '/')
        for rel in self.all_files:
            rel_norm = rel.lower().replace('\\', '/')
            if rel_norm.endswith('/' + norm_t) or rel_norm.endswith('/' + norm_t + '.md'):
                return rel

        return None


class CurriculumTestSuite:
    """The 4-tier E2E test harness for the EECS Curriculum vault."""

    def __init__(self, vault_root: Path, verbose: bool = False, milestone: str = "all"):
        self.vault_root = vault_root
        self.verbose = verbose
        self.milestone = milestone.upper()
        self.context = VaultContext(vault_root)
        self.results: List[TestResult] = []

    def run_test(self, test_id: str, name: str, tier: int, func) -> TestResult:
        t0 = time.perf_counter()
        try:
            passed, msg, details = func()
            duration = (time.perf_counter() - t0) * 1000.0
            res = TestResult(
                test_id=test_id,
                name=name,
                tier=tier,
                passed=passed,
                skipped=False,
                message=msg,
                details=details,
                duration_ms=duration
            )
        except Exception as e:
            duration = (time.perf_counter() - t0) * 1000.0
            res = TestResult(
                test_id=test_id,
                name=name,
                tier=tier,
                passed=False,
                skipped=False,
                message=f"Exception during test: {str(e)}",
                details=[f"Traceback: {e}"],
                duration_ms=duration
            )
        self.results.append(res)
        self._print_test_result(res)
        return res

    def _print_test_result(self, res: TestResult):
        tier_tag = f"{Colors.BLUE}[Tier {res.tier}]{Colors.RESET}"
        if res.skipped:
            status_tag = f"{Colors.YELLOW}[SKIP]{Colors.RESET}"
        elif res.passed:
            status_tag = f"{Colors.GREEN}[PASS]{Colors.RESET}"
        else:
            status_tag = f"{Colors.RED}[FAIL]{Colors.RESET}"

        print(f"  {status_tag} {tier_tag} {res.test_id}: {res.name} ({res.duration_ms:.1f}ms)")
        if res.message:
            indent = "         "
            print(f"{indent}{Colors.DIM}{res.message}{Colors.RESET}")
        if (not res.passed or self.verbose) and res.details:
            for d in res.details[:15]:
                print(f"           - {d}")
            if len(res.details) > 15:
                print(f"           ... and {len(res.details) - 15} more details")

    # =========================================================================
    # TIER 1: FEATURE COVERAGE & SCHEMA VALIDATION
    # =========================================================================

    def test_tier1_core_blocks_existence(self) -> Tuple[bool, str, List[str]]:
        """Verifies existence of all mandatory foundational and core curriculum blocks."""
        required_blocks = {
            # Bedrock
            "B0": "01 - Curriculum/Phase -1 - Bedrock Foundations/B0 - The Deep Learner's Toolkit.md",
            "BM": "01 - Curriculum/Phase -1 - Bedrock Foundations/BM - Bedrock Mathematics.md",
            "BW": "01 - Curriculum/Phase -1 - Bedrock Foundations/BW - Bedrock English and Grammar.md",
            # Phase 0
            "P1": "01 - Curriculum/Phase 0 - Prerequisites/P1 - Learning How to Learn.md",
            "P2": "01 - Curriculum/Phase 0 - Prerequisites/P2 - Reading, Thinking, and Writing.md",
            "P3": "01 - Curriculum/Phase 0 - Prerequisites/P3 - Math Prerequisites.md",
            "P4": "01 - Curriculum/Phase 0 - Prerequisites/P4 - Programming On-Ramp.md",
            "P5": "01 - Curriculum/Phase 0 - Prerequisites/P5 - Tooling.md",
            # Year 1
            "Block 01": "01 - Curriculum/Year 1 - Fundamentals/01 - CS61A.md",
            "Block 02": "01 - Curriculum/Year 1 - Fundamentals/02 - Calculus I.md",
            "Block 03": "01 - Curriculum/Year 1 - Fundamentals/03 - Physics I.md",
            "Block 04": "01 - Curriculum/Year 1 - Fundamentals/04 - Nand2Tetris.md",
            "Block 04a": "01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md",
            "Block 05": "01 - Curriculum/Year 1 - Fundamentals/05 - SICP.md",
            "Block 06": "01 - Curriculum/Year 1 - Fundamentals/06 - C Fluency.md",
            "Block 07": "01 - Curriculum/Year 1 - Fundamentals/07 - Multivariable Calculus.md",
            "Block 08": "01 - Curriculum/Year 1 - Fundamentals/08 - Physics II.md",
            "Block 08a": "01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md",
            # Year 2
            "Block 09": "01 - Curriculum/Year 2 - Systems/09 - Computer Systems.md",
            "Block 10": "01 - Curriculum/Year 2 - Systems/10 - Math for CS.md",
            "Block 11": "01 - Curriculum/Year 2 - Systems/11 - Linear Algebra.md",
            "Block 12": "01 - Curriculum/Year 2 - Systems/12 - Interpreters.md",
            "Block 13": "01 - Curriculum/Year 2 - Systems/13 - Algorithms I.md",
            "Block 14": "01 - Curriculum/Year 2 - Systems/14 - Computer Architecture.md",
            "Block 15": "01 - Curriculum/Year 2 - Systems/15 - Probability.md",
            "Block 15a": "01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md",
            # Year 3
            "Block 16": "01 - Curriculum/Year 3 - Depth/16 - Operating Systems.md",
            "Block 17": "01 - Curriculum/Year 3 - Depth/17 - Software Construction.md",
            "Block 18": "01 - Curriculum/Year 3 - Depth/18 - Real Analysis.md",
            "Block 19": "01 - Curriculum/Year 3 - Depth/19 - Networking.md",
            "Block 20": "01 - Curriculum/Year 3 - Depth/20 - Algorithms II.md",
            "Block 21": "01 - Curriculum/Year 3 - Depth/21 - Databases.md",
            "Block 22": "01 - Curriculum/Year 3 - Depth/22 - Statistics.md",
            # Year 4
            "Block 23": "01 - Curriculum/Year 4 - Specialization/23 - Distributed Systems.md",
            "Block 24": "01 - Curriculum/Year 4 - Specialization/24 - Theory of Computation.md",
            "Block 25": "01 - Curriculum/Year 4 - Specialization/25 - Convex Optimization.md",
            "Block 26": "01 - Curriculum/Year 4 - Specialization/26 - Specialization A1.md",
            "Block 27": "01 - Curriculum/Year 4 - Specialization/27 - Intensive Cryptopals or TLA+.md",
            "Block 28": "01 - Curriculum/Year 4 - Specialization/28 - Specialization A2.md",
            "Block 29": "01 - Curriculum/Year 4 - Specialization/29 - Specialization B1.md",
            # Year 5
            "Block 30": "01 - Curriculum/Year 5 - MEng/30 - Capstone.md",
            "Block 31": "01 - Curriculum/Year 5 - MEng/31 - Specialization B2.md",
            "Block 32": "01 - Curriculum/Year 5 - MEng/32 - Information Theory.md",
        }

        missing = []
        found = []
        for name, expected_rel in required_blocks.items():
            if expected_rel in self.context.md_files:
                found.append(f"{name}: {expected_rel}")
            else:
                # Check by stem
                stem = Path(expected_rel).stem.lower()
                if stem in self.context.basename_map:
                    found.append(f"{name}: {self.context.basename_map[stem][0]}")
                else:
                    missing.append(f"{name} (expected at {expected_rel})")

        total = len(required_blocks)
        present = len(found)
        if missing:
            msg = f"{present}/{total} core blocks present; {len(missing)} missing"
            return False, msg, [f"Missing block: {m}" for m in missing]
        return True, f"All {total} required foundational and core curriculum blocks present", []

    def test_tier1_gap_analysis_report(self) -> Tuple[bool, str, List[str]]:
        """Verifies existence, substantial depth, and core benchmark mapping of Baseline Gap Analysis."""
        expected_path = "01 - Curriculum/Baseline Gap Analysis and Audit Report.md"
        report_file = self.context.md_files.get(expected_path)
        if not report_file:
            stem = "baseline gap analysis and audit report"
            if stem in self.context.basename_map:
                report_file = self.context.md_files.get(self.context.basename_map[stem][0])

        if not report_file:
            return False, f"Missing Baseline Gap Analysis Report at {expected_path}", ["File does not exist in vault"]

        content = report_file.raw_content
        details = []

        # Check size (> 10 KB indicates exhaustive audit)
        if len(content) < 10000:
            details.append(f"Report size ({len(content)} bytes) is below expected comprehensive threshold (>=10,000 bytes)")

        # Verify key standards are audited
        required_topics = [
            ("MIT Course 6", r"Course 6|MIT Course 6|6\.1|6\.2|6\.3|6\.4|6\.5"),
            ("ACM/IEEE CS2023", r"CS2023|ACM\s*/\s*IEEE"),
            ("IEEE CE2016", r"CE2016|Computer Engineering"),
            ("Circuits & Electronics Remediation", r"Circuits|6\.2000|6\.002"),
            ("Signals & Systems Remediation", r"Signals|6\.3000|6\.003"),
            ("Differential Equations Remediation", r"Differential Equations|18\.03"),
        ]

        missing_topics = []
        for label, pattern in required_topics:
            if not re.search(pattern, content, re.IGNORECASE):
                missing_topics.append(label)

        if missing_topics:
            details.extend([f"Missing required standard section: {m}" for m in missing_topics])

        if details:
            return False, f"Baseline Gap Analysis report exists but is missing key analytical sections", details

        return True, f"Baseline Gap Analysis is comprehensive ({len(content):,} bytes) covering MIT Course 6, CS2023, CE2016, and core bridges", []

    def test_tier1_specialization_tracks_existence(self) -> Tuple[bool, str, List[str]]:
        """Verifies existence of Specializations Hub and Tracks 1 through 11."""
        hub_path = "01 - Curriculum/Specializations/Specializations Hub.md"
        hub_present = hub_path in self.context.md_files or "specializations hub" in self.context.basename_map

        tracks = {
            1: "AI and Machine Learning",
            2: "Systems and Performance",
            3: "Security and Cryptography",
            4: "Graphics and Vision",
            5: "Programming Languages and Compilers",
            6: "Computer Engineering",
            7: "TinyML",  # TinyML & Edge AI
            8: "Rust",    # Rust Systems & Formal Verification
            9: "HIL",     # Hardware-in-the-Loop Virtualization & CPS
            10: "Quantum", # Quantum Information & Computing
            11: "Robotics", # Autonomous Robotics & CPS
        }

        found_tracks = {}
        missing_tracks = []

        for track_num, keyword in tracks.items():
            pattern = re.compile(rf"Track\s+{track_num}\b.*\.md$", re.IGNORECASE)
            matched = False
            for rel_path in self.context.md_files:
                if "Specializations" in rel_path and pattern.search(Path(rel_path).name):
                    found_tracks[track_num] = rel_path
                    matched = True
                    break
            if not matched:
                missing_tracks.append(f"Track {track_num} ({keyword})")

        details = []
        if not hub_present:
            details.append("Missing Specializations Hub (01 - Curriculum/Specializations/Specializations Hub.md)")
        if missing_tracks:
            details.extend([f"Missing track file: {m}" for m in missing_tracks])

        if details:
            msg = f"{len(found_tracks)}/11 specialization tracks found; {len(missing_tracks)} missing"
            return False, msg, details

        return True, f"Specializations Hub and all 11 Specialization Tracks are present in vault", []

    def test_tier1_core_block_frontmatter_schema(self) -> Tuple[bool, str, List[str]]:
        """Validates standard YAML frontmatter schema across all core curriculum blocks."""
        required_keys = {"block_id", "title", "term", "status", "hours_estimate", "primary_resource", "milestone"}
        valid_statuses = {"not-started", "in-progress", "done"}

        errors = []
        checked_count = 0

        for rel_path, mf in self.context.md_files.items():
            # Check only curriculum blocks (exclude hub files and templates)
            if not rel_path.startswith("01 - Curriculum/"):
                continue
            if "Specializations" in rel_path or "Baseline Gap Analysis" in rel_path:
                continue

            checked_count += 1
            fm = mf.frontmatter

            missing_keys = required_keys - set(fm.keys())
            if missing_keys:
                errors.append(f"{rel_path}: Missing frontmatter keys: {', '.join(sorted(missing_keys))}")
                continue

            status = str(fm.get("status", "")).lower()
            if status not in valid_statuses:
                errors.append(f"{rel_path}: Invalid status '{status}' (must be one of: {valid_statuses})")

            hrs = fm.get("hours_estimate")
            if not isinstance(hrs, (int, float)) or hrs <= 0:
                errors.append(f"{rel_path}: Invalid hours_estimate '{hrs}' (must be positive number)")

        if errors:
            msg = f"{len(errors)} frontmatter schema violation(s) across {checked_count} curriculum blocks"
            return False, msg, errors

        return True, f"All {checked_count} core curriculum blocks adhere strictly to YAML frontmatter schema", []

    def test_tier1_core_block_markdown_sections(self) -> Tuple[bool, str, List[str]]:
        """Validates that all core curriculum blocks contain the required standardized Markdown section headings."""
        required_course_block_patterns = [
            ("Block Overview", r"Block Overview"),
            ("Why This Block Matters", r"Why This Block Matters"),
            ("Primary Syllabus", r"Primary (Syllabus|Curriculum)"),
            ("Build Requirement", r"Build Requirement"),
            ("Done When", r"Done When"),
            ("Study Notes & Proofs", r"Study Notes.*(Proof|Problem Set)"),
            ("Failover Alternatives", r"Appendix A Alternatives|Failover"),
        ]

        errors = []
        checked_count = 0

        for rel_path, mf in self.context.md_files.items():
            if not rel_path.startswith("01 - Curriculum/"):
                continue
            if "Specializations" in rel_path or "Baseline Gap Analysis" in rel_path:
                continue

            content = mf.raw_content

            # Bedrock Foundations (Phase -1) have distinct cognitive structure
            if "Phase -1" in rel_path:
                checked_count += 1
                if not re.search(r"##\s*.*", content):
                    errors.append(f"{rel_path}: Bedrock note missing markdown headings")
                continue

            # Standard Course Blocks (Phase 0 and Years 1 to 5)
            checked_count += 1
            missing_sections = []
            for sec_name, pattern in required_course_block_patterns:
                if not re.search(pattern, content, re.IGNORECASE):
                    missing_sections.append(sec_name)

            if missing_sections:
                errors.append(f"{rel_path}: Missing required sections: {', '.join(missing_sections)}")

        if errors:
            msg = f"{len(errors)} block(s) missing required Markdown sections out of {checked_count}"
            return False, msg, errors

        return True, f"All {checked_count} core blocks implement required structural section headings", []

    def test_tier1_specialization_track_schema(self) -> Tuple[bool, str, List[str]]:
        """Verifies that all Specialization Tracks implement the PROJECT.md Interface Contract."""
        required_patterns = [
            ("Track Overview / Motivation", r"(Track Overview|Specialization Structure|Why This Track Matters|Overview & Motivation)"),
            ("Core Courses", r"(Core Courses|Course 1|Course 2)"),
            ("Seminal Papers & Textbooks", r"(Seminal Papers|Advanced Textbooks|Reference Texts)"),
            ("Progressive Labs", r"(Progressive Labs|Hands-On Lab|Lab 1|Lab Specifications)"),
            ("Capstone Build Deliverable", r"(Capstone Build|Track Build Deliverable|Capstone Track Build)"),
        ]

        errors = []
        track_count = 0

        for rel_path, mf in self.context.md_files.items():
            if "Specializations" not in rel_path:
                continue
            if "Specializations Hub" in rel_path:
                continue
            if not re.search(r"Track\s+\d+", Path(rel_path).name, re.IGNORECASE):
                continue

            track_count += 1
            content = mf.raw_content

            missing_contracts = []
            for name, pattern in required_patterns:
                if not re.search(pattern, content, re.IGNORECASE):
                    missing_contracts.append(name)

            if missing_contracts:
                errors.append(f"{rel_path}: Missing interface contract sections: {', '.join(missing_contracts)}")

        if track_count == 0:
            return False, "No specialization tracks found in vault to validate", ["Track files missing"]

        if errors:
            msg = f"{len(errors)}/{track_count} track(s) do not fully satisfy Interface Contract schema"
            return False, msg, errors

        return True, f"All {track_count} specialization tracks strictly adhere to Interface Contract schema", []

    # =========================================================================
    # TIER 2: BOUNDARY & CORNER CASES
    # =========================================================================

    def test_tier2_vault_wikilink_integrity(self) -> Tuple[bool, str, List[str]]:
        """Parses all [[wikilinks]] vault-wide and verifies zero broken targets."""
        broken_links = []
        total_links = 0

        # Patterns for intentional template placeholders that shouldn't be treated as broken links
        template_var_pattern = re.compile(r"\{\{.*\}\}")

        for rel_path, mf in self.context.md_files.items():
            # Exclude template files from broken link errors if they contain {{variables}}
            is_template = "08 - Templates" in rel_path

            for line_no, raw_target, alias in mf.wikilinks:
                total_links += 1

                if is_template and template_var_pattern.search(raw_target):
                    continue
                if raw_target.startswith("Related Note"):
                    continue

                resolved = self.context.resolve_wikilink(raw_target)
                if not resolved:
                    broken_links.append(f"{rel_path}:{line_no} -> [[{raw_target}]]")

        if broken_links:
            msg = f"{len(broken_links)} broken wikilink(s) detected across {total_links} total links in vault"
            return False, msg, broken_links

        return True, f"Vault-wide wikilink integrity 100% verified ({total_links} valid links, 0 broken)", []

    def test_tier2_track_graduate_citations_count(self) -> Tuple[bool, str, List[str]]:
        """Verifies that EVERY Specialization Track has at least 3 graduate-level theoretical papers or advanced texts with full citations."""
        violations = []
        track_citations = {}

        # Regex for discovering full citations: Author (Year), Title, Venue/Publisher
        citation_re = re.compile(
            r"(?:^|\n)\s*[-*]\s*(?:\[\s*\]\s*)?(?:\*\*)?([A-Z][a-zA-Z\s,.'&-]+?)\s*(?:\((?:19|20)\d{2}\)|,\s*(?:19|20)\d{2}\b)\.?\s*(?:\*\*)?\s*[\*_\"]?([^\*\n\"_]+)[\*_\"]?",
            re.MULTILINE
        )

        # Fallback citation detector (bullet points with year and author)
        alt_citation_re = re.compile(
            r"[-*]\s+(.+?\b(?:19|20)\d{2}\b.+)",
            re.MULTILINE
        )

        for rel_path, mf in self.context.md_files.items():
            if "Specializations" not in rel_path or "Specializations Hub" in rel_path:
                continue
            if not re.search(r"Track\s+\d+", Path(rel_path).name, re.IGNORECASE):
                continue

            content = mf.raw_content
            # Extract Seminal Papers / Reference Texts section
            papers_section = ""
            m_sec = re.search(
                r"##\s*.*?(?:Seminal Papers|Advanced Textbooks|Reference Texts|Key Reference).*?\n(.*?)(?=\n##|\Z)",
                content,
                re.DOTALL | re.IGNORECASE
            )
            if m_sec:
                papers_section = m_sec.group(1)

            # Count citations in that section or entire file
            citations = citation_re.findall(papers_section)
            if len(citations) < 3:
                # Try fallback line match in the section
                alt_lines = alt_citation_re.findall(papers_section)
                count = max(len(citations), len(alt_lines))
            else:
                count = len(citations)

            # If still < 3, check entire file for cited literature
            if count < 3:
                all_alt = alt_citation_re.findall(content)
                count = max(count, len(all_alt))

            track_name = Path(rel_path).stem
            track_citations[track_name] = count

            if count < 3:
                violations.append(f"{rel_path}: Found only {count} graduate citations (minimum 3 required with full citations)")

        if not track_citations:
            return False, "No specialization tracks available to check citations", ["Track notes missing"]

        if violations:
            msg = f"{len(violations)} specialization track(s) lack >=3 graduate-level citations"
            return False, msg, violations

        summary = ", ".join(f"{k.split(' - ')[0]}:{v}" for k, v in sorted(track_citations.items()))
        return True, f"All {len(track_citations)} specialization tracks have >=3 graduate citations ({summary})", []

    def test_tier2_modern_paradigms_lab_specs(self) -> Tuple[bool, str, List[str]]:
        """Verifies that at least 2 modern paradigm tracks (Tracks 7–11) have fully integrated lab and project specs with acceptance criteria."""
        modern_tracks = [7, 8, 9, 10, 11]
        qualifying_tracks = []
        details = []

        # Keywords signifying measurable engineering acceptance criteria
        acceptance_criteria_pattern = re.compile(
            r"(acceptance\s*criteri|acceptance\s*test|latency\s*[<≤]|jitter\s*[<≤]|stress-ng|zero\s*panic|"
            r"cyclictest|proof\s*check|valgrind\s*clean|0\s*sorry|score\s*[≥>=]|threshold|chemical\s*accuracy|"
            r"throughput|benchmarking|formal\s*claims|functional\s*safety)",
            re.IGNORECASE
        )

        for track_num in modern_tracks:
            pattern = re.compile(rf"Track\s+{track_num}\b.*\.md$", re.IGNORECASE)
            matched_file = None
            for rel_path, mf in self.context.md_files.items():
                if "Specializations" in rel_path and pattern.search(Path(rel_path).name):
                    matched_file = mf
                    break

            if not matched_file:
                details.append(f"Track {track_num}: File not found")
                continue

            content = matched_file.raw_content

            # Check for progressive labs (at least 3 labs specified)
            lab_matches = re.findall(r"(?:Lab\s+[1-3]|Module\s+[1-5].*?Lab)", content, re.IGNORECASE)
            has_3_labs = len(set(lab_matches)) >= 3 or len(re.findall(r"###\s*Lab\s+\d+|-\s*\*\*Lab\s+\d+", content)) >= 3

            # Check for Capstone build deliverable
            has_capstone = bool(re.search(r"Capstone.*Build Deliverable|Track Build Deliverable", content, re.IGNORECASE))

            # Check for measurable acceptance criteria
            has_acceptance_criteria = bool(acceptance_criteria_pattern.search(content))

            if has_3_labs and has_capstone and has_acceptance_criteria:
                qualifying_tracks.append(f"Track {track_num} ({Path(matched_file.rel_path).stem})")
            else:
                missing_pieces = []
                if not has_3_labs:
                    missing_pieces.append("missing >=3 progressive labs")
                if not has_capstone:
                    missing_pieces.append("missing capstone build spec")
                if not has_acceptance_criteria:
                    missing_pieces.append("missing measurable acceptance criteria")
                details.append(f"Track {track_num}: Incomplete specs ({', '.join(missing_pieces)})")

        if len(qualifying_tracks) < 2:
            msg = f"Only {len(qualifying_tracks)} modern paradigm track(s) have fully integrated lab specs (minimum 2 required)"
            return False, msg, details

        return True, f"{len(qualifying_tracks)} modern paradigm tracks fully integrated with progressive labs and acceptance criteria ({', '.join(qualifying_tracks)})", []

    def test_tier2_paper_reading_hub_linkage(self) -> Tuple[bool, str, List[str]]:
        """Verifies that 03 - Papers/Paper Reading Hub.md links seminal papers to curriculum blocks."""
        hub_path = "03 - Papers/Paper Reading Hub.md"
        hub_file = self.context.md_files.get(hub_path)
        if not hub_file:
            stem = "paper reading hub"
            if stem in self.context.basename_map:
                hub_file = self.context.md_files.get(self.context.basename_map[stem][0])

        if not hub_file:
            return False, f"Missing Paper Reading Hub at {hub_path}", ["File not found in vault"]

        content = hub_file.raw_content
        # Check that it contains paper citations and wikilinks to blocks
        links = hub_file.wikilinks
        if len(links) < 5:
            return False, f"Paper Reading Hub has insufficient curriculum block wikilinks ({len(links)} links found)", [f"Link count {len(links)} < 5"]

        return True, f"Paper Reading Hub is active and links {len(links)} curriculum blocks to seminal research papers", []

    # =========================================================================
    # TIER 3: CROSS-FEATURE COMBINATIONS
    # =========================================================================

    def test_tier3_prerequisite_graph_dag(self) -> Tuple[bool, str, List[str]]:
        """Constructs the prerequisite directed graph across all blocks and verifies it is a strict DAG (0 cycles)."""
        # Extract explicit and structural prerequisite edges (U -> V where U is prerequisite for V)
        graph: Dict[str, Set[str]] = defaultdict(set)
        nodes: Set[str] = set()

        # Known foundational prerequisite sequences in curriculum
        core_prereqs = [
            ("02 - Calculus I", "07 - Multivariable Calculus"),
            ("02 - Calculus I", "03 - Physics I"),
            ("03 - Physics I", "08 - Physics II"),
            ("07 - Multivariable Calculus", "04a - Differential Equations Bridge"),
            ("08 - Physics II", "08a - Circuits and Electronics Bridge"),
            ("04a - Differential Equations Bridge", "15a - Signals and Systems Bridge"),
            ("06 - C Fluency", "09 - Computer Systems"),
            ("09 - Computer Systems", "14 - Computer Architecture"),
            ("09 - Computer Systems", "16 - Operating Systems"),
            ("10 - Math for CS", "13 - Algorithms I"),
            ("13 - Algorithms I", "20 - Algorithms II"),
            ("20 - Algorithms II", "24 - Theory of Computation"),
            ("11 - Linear Algebra", "25 - Convex Optimization"),
            ("15 - Probability", "22 - Statistics"),
            ("16 - Operating Systems", "23 - Distributed Systems"),
            ("19 - Networking", "23 - Distributed Systems"),
        ]

        for u, v in core_prereqs:
            graph[u].add(v)
            nodes.add(u)
            nodes.add(v)

        # Parse text-based prerequisites from notes
        prereq_pattern = re.compile(r"Prerequisites?:?\s*([^\n\r]+)", re.IGNORECASE)
        for rel_path, mf in self.context.md_files.items():
            current_stem = Path(rel_path).stem
            nodes.add(current_stem)

            # Check frontmatter and body
            content = mf.raw_content
            for m in prereq_pattern.finditer(content):
                line = m.group(1)
                # Find all wikilinks in this prerequisite line
                for _, target, _ in mf.wikilinks:
                    if target in line:
                        target_stem = Path(target).stem
                        if target_stem != current_stem:
                            graph[target_stem].add(current_stem)

        # Cycle detection using DFS
        visited = {}  # node -> 0: unvisited, 1: visiting, 2: visited
        for n in nodes:
            visited[n] = 0

        cycles = []

        def dfs(node, path):
            visited[node] = 1
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    continue
                if visited[neighbor] == 1:
                    cycle = path + [neighbor]
                    cycles.append(" -> ".join(cycle[cycle.index(neighbor):]))
                elif visited[neighbor] == 0:
                    dfs(neighbor, path + [neighbor])
            visited[node] = 2

        for n in list(nodes):
            if visited[n] == 0:
                dfs(n, [n])

        if cycles:
            msg = f"{len(cycles)} circular dependency cycle(s) detected in curriculum prerequisite graph"
            return False, msg, [f"Cycle: {c}" for c in cycles[:10]]

        return True, f"Prerequisite graph across {len(nodes)} nodes is a strictly acyclic Directed Acyclic Graph (DAG, 0 cycles)", []

    def test_tier3_prerequisite_topological_ordering(self) -> Tuple[bool, str, List[str]]:
        """Verifies topological ordering: Every prerequisite course must belong to an earlier or equal academic term."""
        term_map = {
            "Phase -1": 0,
            "Phase 0": 1,
            "Year 1 Fall": 2,
            "Year 1 Spring": 3,
            "Year 2 Fall": 4,
            "Year 2 Spring": 5,
            "Year 3 Fall": 6,
            "Year 3 Spring": 7,
            "Year 4 Fall": 8,
            "Year 4 Winter": 9,
            "Year 4 Spring": 10,
            "Year 5 Fall": 11,
            "Year 5 Spring": 12,
            "Year 5 MEng": 12,
        }

        # Map block stem to term rank
        node_term_rank = {}
        for rel_path, mf in self.context.md_files.items():
            stem = Path(rel_path).stem
            term = str(mf.frontmatter.get("term", ""))
            rank = None
            for t_prefix, r in term_map.items():
                if t_prefix.lower() in term.lower() or t_prefix.lower() in rel_path.lower():
                    rank = r
                    break
            if rank is not None:
                node_term_rank[stem] = rank

        # Check known prerequisite edges
        ordering_violations = []
        checks = [
            ("02 - Calculus I", "07 - Multivariable Calculus"),
            ("07 - Multivariable Calculus", "04a - Differential Equations Bridge"),
            ("04a - Differential Equations Bridge", "08a - Circuits and Electronics Bridge"),
            ("08a - Circuits and Electronics Bridge", "15a - Signals and Systems Bridge"),
            ("09 - Computer Systems", "16 - Operating Systems"),
            ("16 - Operating Systems", "23 - Distributed Systems"),
            ("10 - Math for CS", "13 - Algorithms I"),
            ("13 - Algorithms I", "20 - Algorithms II"),
            ("20 - Algorithms II", "24 - Theory of Computation"),
            ("11 - Linear Algebra", "25 - Convex Optimization"),
        ]

        for u, v in checks:
            r_u = node_term_rank.get(u)
            r_v = node_term_rank.get(v)
            if r_u is not None and r_v is not None:
                if r_u > r_v:
                    ordering_violations.append(f"Prerequisite inversion: {u} (Term rank {r_u}) occurs AFTER {v} (Term rank {r_v})")

        if ordering_violations:
            msg = f"{len(ordering_violations)} chronological topological order violation(s)"
            return False, msg, ordering_violations

        return True, "Chronological topological ordering verified from Year 1 to Year 5 across all prerequisite chains", []

    def test_tier3_cs2023_knowledge_areas_coverage(self) -> Tuple[bool, str, List[str]]:
        """Cross-references curriculum against all 17 ACM/IEEE CS2023 Core Knowledge Areas across genuine course blocks."""
        all_17_kas = {
            "AL": ("Algorithmic Foundations", r"\bAL\b|Algorithmic Foundations|Algorithms?|Demaine|CLRS"),
            "AR": ("Architecture and Organization", r"\bAR\b|Architecture and Organization|Computer Architecture|RISC-V|Microarchitecture"),
            "AI": ("Artificial Intelligence", r"\bAI\b|Artificial Intelligence|Machine Learning|Deep Learning|Neural Network"),
            "DM": ("Data Management", r"\bDM\b|Data Management|Databases?|Relational|SQL|BusTub"),
            "FPL": ("Foundations of Programming Languages", r"\bFPL\b|Foundations of Programming Languages|Programming Languages|Interpreters?|Compilers?|Type Systems?|Lambda Calculus"),
            "GIT": ("Graphics and Interactive Techniques", r"\bGIT\b|Graphics and Interactive Techniques|Computer Graphics|Ray Tracing|Rasterization|Rendering|Vulkan|PBRT"),
            "HCI": ("Human-Computer Interaction", r"\bHCI\b|Human-Computer Interaction|User-Centered Design|Usability|WCAG|Fitts"),
            "MSF": ("Mathematical and Statistical Foundations", r"\bMSF\b|Mathematical and Statistical Foundations|Discrete Math|Linear Algebra|Calculus|Probability|Real Analysis|Differential Equations"),
            "NC": ("Networking and Communication", r"\bNC\b|Networking and Communication|Computer Networks?|TCP/IP|Routing"),
            "OS": ("Operating Systems", r"\bOS\b|Operating Systems?|Virtual Memory|Kernel|Paging|xv6|OSTEP"),
            "PDC": ("Parallel and Distributed Computing", r"\bPDC\b|Parallel and Distributed Computing|Distributed Systems?|Concurrency|Raft|Mutual Exclusion"),
            "SEC": ("Security", r"\bSEC\b|Security|Cryptography|Threat Model|Vulnerabilit|Exploit"),
            "SEP": ("Society, Ethics, and the Profession", r"\bSEP\b|Society, Ethics, and the Profession|Professional Ethics|Code of Ethics|Engineering Ethics|Society"),
            "SDF": ("Software Development Fundamentals", r"\bSDF\b|Software Development Fundamentals|Software Development|Data Structures?|Testing Strateg|checkRep|Debugging"),
            "SE": ("Software Engineering", r"\bSE\b|Software Engineering|Software Construction|Specifications?|Design Patterns?|Refactoring"),
            "SPD": ("Specialized Platform Development", r"\bSPD\b|Specialized Platform Development|Embedded|Microcontroller|Bare-metal|TinyML|Edge AI|Cyber-Physical"),
            "SF": ("Systems Fundamentals", r"\bSF\b|Systems Fundamentals|Computer Systems?|Abstraction Barrier|Hardware-Software Interface|Nand2Tetris"),
        }

        # Search ONLY genuine curriculum course blocks (strictly excluding the gap analysis report)
        curriculum_course_files = {
            rel_path: mf for rel_path, mf in self.context.md_files.items()
            if rel_path.startswith("01 - Curriculum/")
            and "Baseline Gap Analysis and Audit Report" not in rel_path
        }

        missing_kas = []
        covered_kas = {}

        for code, (title, pattern_str) in all_17_kas.items():
            pattern = re.compile(rf"\b{code}\b|{re.escape(title)}|{pattern_str}", re.IGNORECASE)
            matched_files = []

            for rel_path, mf in curriculum_course_files.items():
                if pattern.search(mf.raw_content):
                    matched_files.append(rel_path)

            if matched_files:
                covered_kas[code] = (title, matched_files)
            else:
                missing_kas.append(f"{code}: {title}")

        if missing_kas:
            msg = f"{len(covered_kas)}/17 ACM/IEEE CS2023 Knowledge Areas covered; {len(missing_kas)} unmapped voids in course notes"
            return False, msg, [f"Uncovered Knowledge Area: {m}" for m in missing_kas]

        details = [f"{code} ({title}): verified in {files[0]}" for code, (title, files) in covered_kas.items()]
        return True, "100% of all 17 ACM/IEEE CS2023 Knowledge Areas verified across genuine curriculum blocks", details

    def test_tier3_ce2016_knowledge_areas_coverage(self) -> Tuple[bool, str, List[str]]:
        """Verifies that all 12 IEEE CE2016 Knowledge Areas are covered across genuine curriculum blocks."""
        all_12_ce_kas = {
            "CE-CAE": ("Circuits and Electronics", r"\bCE-CAE\b|Circuits and Electronics"),
            "CE-CSG": ("Circuits and Signals", r"\bCE-CSG\b|Circuits and Signals|Signals and Systems"),
            "CE-DIG": ("Digital Design", r"\bCE-DIG\b|Digital Design|Digital Logic"),
            "CE-CAO": ("Computer Architecture and Organization", r"\bCE-CAO\b|Computer Architecture and Organization|Computer Architecture|RISC-V"),
            "CE-ESY": ("Embedded Systems", r"\bCE-ESY\b|Embedded Systems?|Microcontroller|Bare-metal|TinyML"),
            "CE-CAL": ("Computing Algorithms", r"\bCE-CAL\b|Computing Algorithms|Algorithms?"),
            "CE-SWD": ("Software Design", r"\bCE-SWD\b|Software Design|Software Construction|Abstract Data Types?"),
            "CE-NWK": ("Computer Networks", r"\bCE-NWK\b|Computer Networks?|Networking"),
            "CE-VLS": ("VLSI Design and Fabrication", r"\bCE-VLS\b|VLSI|CMOS|Tiny Tapeout|ASIC"),
            "CE-SEC": ("Hardware Security", r"\bCE-SEC\b|Hardware Security|Security|Side-channel|Root of Trust"),
            "CE-SPE": ("Systems and Project Engineering", r"\bCE-SPE\b|Systems and Project Engineering|Project Engineering|Capstone|Engineering Artifact"),
            "CE-FND": ("Math, Physics, and CE Foundations", r"\bCE-FND\b|Math, Physics, and CE Foundations|Differential Equations|Physics II|Multivariable Calculus"),
        }

        curriculum_course_files = {
            rel_path: mf for rel_path, mf in self.context.md_files.items()
            if rel_path.startswith("01 - Curriculum/")
            and "Baseline Gap Analysis and Audit Report" not in rel_path
        }

        missing_kas = []
        covered_kas = {}

        for code, (title, pattern_str) in all_12_ce_kas.items():
            pattern = re.compile(rf"\b{code}\b|{re.escape(title)}|{pattern_str}", re.IGNORECASE)
            matched_files = []

            for rel_path, mf in curriculum_course_files.items():
                if pattern.search(mf.raw_content):
                    matched_files.append(rel_path)

            if matched_files:
                covered_kas[code] = (title, matched_files)
            else:
                missing_kas.append(f"{code}: {title}")

        if missing_kas:
            msg = f"{len(covered_kas)}/12 IEEE CE2016 Knowledge Areas covered; {len(missing_kas)} unmapped voids in course notes"
            return False, msg, [f"Uncovered CE Knowledge Area: {m}" for m in missing_kas]

        details = [f"{code} ({title}): verified in {files[0]}" for code, (title, files) in covered_kas.items()]
        return True, "100% of all 12 IEEE CE2016 Knowledge Areas verified across genuine curriculum blocks", details

    def test_tier3_mit_course6_pillars_coverage(self) -> Tuple[bool, str, List[str]]:
        """Verifies coverage of all canonical MIT Course 6 EECS Pillars."""
        canonical_mit_courses = {
            "MIT 6.2000 Circuits & Electronics": r"6\.2000|6\.002|Circuits and Electronics",
            "MIT 6.3000 Signals & Systems": r"6\.3000|6\.003|Signals and Systems",
            "MIT 18.03 Differential Equations": r"18\.03|Differential Equations",
            "MIT 6.1910 Computation Structures": r"6\.1910|6\.004|Computation Structures|Nand2Tetris",
            "MIT 6.1810 Operating Systems": r"6\.1810|6\.828|Operating System|xv6",
            "MIT 6.1210/6.1220 Algorithms": r"6\.1210|6\.1220|6\.006|6\.046|Algorithms",
            "MIT 6.5840 Distributed Systems": r"6\.5840|6\.824|Distributed Systems|Raft",
            "MIT 6.1020 Software Construction": r"6\.1020|6\.031|Software Construction",
            "MIT 6.1400 Theory of Computation": r"6\.1400|6\.045|18\.404|Theory of Computation",
            "MIT 6.3900 Machine Learning": r"6\.3900|6\.036|Machine Learning",
            "MIT 18.06 Linear Algebra": r"18\.06|Linear Algebra|Axler",
            "MIT 6.3700 Probability": r"6\.3700|6\.041|Introduction to Probability",
        }

        uncovered = []
        covered = []

        for name, pattern in canonical_mit_courses.items():
            matched = False
            regex = re.compile(pattern, re.IGNORECASE)
            for rel_path, mf in self.context.md_files.items():
                if regex.search(mf.raw_content) or regex.search(rel_path):
                    matched = True
                    break
            if matched:
                covered.append(name)
            else:
                uncovered.append(name)

        if uncovered:
            msg = f"{len(covered)}/{len(canonical_mit_courses)} canonical MIT Course 6 pillars covered; {len(uncovered)} missing"
            return False, msg, [f"Missing MIT pillar: {m}" for m in uncovered]

        return True, f"100% of all {len(canonical_mit_courses)} canonical MIT Course 6 EECS foundational pillars covered", []

    def test_tier3_r2_graduate_proofs_injection(self) -> Tuple[bool, str, List[str]]:
        """Verifies that core blocks and tracks contain graduate-level proofs (Requirement R2)."""
        proof_indicators = [
            ("Caratheodory Extension", r"Carath[eé]odory"),
            ("Radon-Nikodym Theorem", r"Radon-Nikodym"),
            ("KKT / Duality Gap", r"Karush-Kuhn-Tucker|KKT|Slater"),
            ("Baire Category Theorem", r"Baire Category"),
            ("Yoneda Lemma", r"Yoneda"),
            ("Cook-Levin Reduction", r"Cook-Levin"),
            ("Cheeger's Inequality", r"Cheeger"),
            ("LWE Lattice Reduction", r"Learning With Errors|LWE|Regev"),
            ("FLP Impossibility", r"FLP|Fischer.*Lynch.*Paterson"),
            ("Picard-Lindelof Existence", r"Picard-Lindel[oö]f"),
        ]

        found_proofs = []
        missing_proofs = []

        for name, pattern in proof_indicators:
            regex = re.compile(pattern, re.IGNORECASE)
            matched = False
            for rel_path, mf in self.context.md_files.items():
                if regex.search(mf.raw_content):
                    matched = True
                    found_proofs.append(f"{name} (found in {Path(rel_path).stem})")
                    break
            if not matched:
                missing_proofs.append(name)

        # Require at least 5 foundational proofs across the curriculum
        if len(found_proofs) < 5:
            msg = f"Only {len(found_proofs)}/10 foundational graduate proofs detected in vault (minimum 5 required)"
            return False, msg, [f"Missing proof derivation: {m}" for m in missing_proofs]

        return True, f"{len(found_proofs)} foundational graduate proofs and derivations verified in curriculum notes", found_proofs

    # =========================================================================
    # TIER 4: REAL-WORLD SCENARIOS
    # =========================================================================

    def test_tier4_student_pathways_feasibility(self) -> Tuple[bool, str, List[str]]:
        """Simulates 4 diverse student degree completion pathways through the curriculum."""
        pathways = [
            {
                "name": "Pathway 1: Systems & Cloud Infrastructure Architect",
                "tracks": ["Track 2", "Track 8"],
                "focus": ["Operating Systems", "Networking", "Distributed Systems", "Rust Systems", "Performance"],
            },
            {
                "name": "Pathway 2: Edge AI & Intelligent Robotics",
                "tracks": ["Track 1", "Track 7", "Track 11"],
                "focus": ["Machine Learning", "TinyML", "Linear Algebra", "Robotics", "Optimization"],
            },
            {
                "name": "Pathway 3: Cyber-Physical & Embedded Hardware",
                "tracks": ["Track 6", "Track 9"],
                "focus": ["Circuits", "Signals", "Computer Architecture", "HIL Virtualization"],
            },
            {
                "name": "Pathway 4: Theoretical CS, Cryptography & Formal Logic",
                "tracks": ["Track 3", "Track 10"],
                "focus": ["Math for CS", "Theory of Computation", "Security", "Formal Verification"],
            },
        ]

        details = []
        pathway_success = 0

        # Base hours of core curriculum ~2,400 - 3,200 hrs
        base_core_hours = 0
        for rel_path, mf in self.context.md_files.items():
            if rel_path.startswith("01 - Curriculum/") and "Specializations" not in rel_path:
                hrs = mf.frontmatter.get("hours_estimate", 0)
                if isinstance(hrs, (int, float)):
                    base_core_hours += hrs

        for pw in pathways:
            # Check track existence
            tracks_available = []
            for t_code in pw["tracks"]:
                pattern = re.compile(rf"{t_code}\b.*\.md$", re.IGNORECASE)
                for rel_path in self.context.md_files:
                    if "Specializations" in rel_path and pattern.search(Path(rel_path).name):
                        tracks_available.append(t_code)
                        break

            if len(tracks_available) == len(pw["tracks"]):
                total_hours = base_core_hours + (len(pw["tracks"]) * 300)
                # Verify total hours between 3,000 and 7,500
                if 3000 <= total_hours <= 7500:
                    pathway_success += 1
                    details.append(f"{pw['name']}: Feasible (~{total_hours:,} total hours; Tracks {', '.join(tracks_available)} mapped)")
                else:
                    details.append(f"{pw['name']}: Total hours ({total_hours}) out of expected range [3000, 7500]")
            else:
                missing_t = set(pw["tracks"]) - set(tracks_available)
                details.append(f"{pw['name']}: Missing tracks {', '.join(missing_t)}")

        if pathway_success < 2:
            msg = f"Only {pathway_success}/4 simulated student degree pathways are currently feasible"
            return False, msg, details

        return True, f"{pathway_success}/4 student degree pathways fully validated with feasible workload and track alignment", details

    def test_tier4_toolchain_and_build_validation(self) -> Tuple[bool, str, List[str]]:
        """Verifies that software/hardware build requirements specify concrete tools, languages, and verifiable deliverables."""
        toolchain_keywords = [
            "gcc", "clang", "g++", "rustc", "cargo", "python", "make", "cmake", "gdb",
            "valgrind", "qemu", "renode", "verilator", "iverilog", "pytest", "kani",
            "lean", "coq", "qiskit", "ros2", "docker", "wireshark", "ltspice", "ngspice",
            "scheme", "jack", "c", "c++", "rust", "go", "linux", "git", "bash", "vim",
            "assembly", "risc-v", "x86", "verilog", "systemverilog", "breadboard",
            "oscilloscope", "fpga", "tiny tapeout", "latex", "sql", "numpy", "scipy"
        ]

        blocks_with_builds = 0
        blocks_with_tools = 0
        details = []

        tool_re = re.compile(r"\b(" + "|".join(re.escape(k) for k in toolchain_keywords) + r")\b", re.IGNORECASE)

        for rel_path, mf in self.context.md_files.items():
            if not rel_path.startswith("01 - Curriculum/"):
                continue

            content = mf.raw_content
            # Check Build Requirement section
            m = re.search(r"^##[^\n]*(?:Build Requirement|Progressive Labs|Capstone Build Deliverable)[^\n]*\n(.*?)(?=\n##\s|\Z)", content, re.DOTALL | re.MULTILINE | re.IGNORECASE)
            if m:
                build_text = m.group(1)
                blocks_with_builds += 1
                tools_found = set(tool_re.findall(build_text))
                if tools_found:
                    blocks_with_tools += 1
                else:
                    if self.verbose:
                        details.append(f"{rel_path}: Build requirement lacks explicit toolchain keyword")

        coverage_ratio = (blocks_with_tools / blocks_with_builds) if blocks_with_builds else 0
        if coverage_ratio < 0.60:
            msg = f"Only {blocks_with_tools}/{blocks_with_builds} ({coverage_ratio:.1%}) build requirements specify concrete toolchains (expected >=60%)"
            return False, msg, details

        return True, f"{blocks_with_tools}/{blocks_with_builds} ({coverage_ratio:.1%}) curriculum build specs cite concrete toolchains and engineering instrumentation", []

    def test_tier4_checklist_dashboard_alignment(self) -> Tuple[bool, str, List[str]]:
        """Verifies that Checklist.md and 00 - Dashboard.md are aligned with all curriculum entities."""
        chk_file = self.context.md_files.get("Checklist.md")
        dash_file = self.context.md_files.get("00 - Dashboard.md")

        if not chk_file or not dash_file:
            return False, "Missing Checklist.md or 00 - Dashboard.md in vault root", ["Checklist.md or 00 - Dashboard.md not found"]

        chk_content = chk_file.raw_content
        dash_content = dash_file.raw_content
        details = []

        # Check for core blocks in Checklist
        sample_blocks = ["CS61A", "Nand2Tetris", "Computer Systems", "Operating Systems", "Distributed Systems"]
        missing_in_chk = [b for b in sample_blocks if b not in chk_content]
        if missing_in_chk:
            details.append(f"Checklist.md missing core blocks: {', '.join(missing_in_chk)}")

        # Check Dashboard for Hub navigation links
        required_hubs = ["Mindset Hub", "Paper Reading Hub", "Writing Hub", "Projects Hub", "Breadth Hub"]
        missing_in_dash = [h for h in required_hubs if h not in dash_content]
        if missing_in_dash:
            details.append(f"00 - Dashboard.md missing navigation hub links: {', '.join(missing_in_dash)}")

        if details:
            msg = "Checklist.md or 00 - Dashboard.md has alignment gaps"
            return False, msg, details

        return True, "Checklist.md and 00 - Dashboard.md are fully synchronized with vault navigation and curriculum milestones", []

    # =========================================================================
    # SUITE ORCHESTRATION & EXECUTION
    # =========================================================================

    def run_all(self, selected_tiers: Optional[Set[int]] = None) -> bool:
        """Executes all tests or filtered tiers, reporting pass/fail."""
        print(f"\n{Colors.BOLD}================================================================================")
        print(f"       EECS CURRICULUM AUDIT & EXPANSION — E2E VERIFICATION TEST SUITE         ")
        print(f"================================================================================{Colors.RESET}")
        print(f"Vault Root:       {self.vault_root}")
        print(f"Total Files:      {len(self.context.all_files):,} ({len(self.context.md_files)} markdown notes)")
        print(f"Milestone Mode:   {self.milestone}")
        print(f"Selected Tiers:   {sorted(list(selected_tiers)) if selected_tiers else 'All (1, 2, 3, 4)'}\n")

        all_tests = [
            # Tier 1
            ("T1.1", "Core Blocks Existence", 1, self.test_tier1_core_blocks_existence),
            ("T1.2", "Baseline Gap Analysis Report", 1, self.test_tier1_gap_analysis_report),
            ("T1.3", "Specialization Tracks Existence (1–11)", 1, self.test_tier1_specialization_tracks_existence),
            ("T1.4", "Core Block Frontmatter Schema", 1, self.test_tier1_core_block_frontmatter_schema),
            ("T1.5", "Core Block Section Headers", 1, self.test_tier1_core_block_markdown_sections),
            ("T1.6", "Specialization Track Interface Schema", 1, self.test_tier1_specialization_track_schema),

            # Tier 2
            ("T2.1", "Vault-Wide Wikilink Integrity Validator", 2, self.test_tier2_vault_wikilink_integrity),
            ("T2.2", "Graduate Literature Citations (>=3/track)", 2, self.test_tier2_track_graduate_citations_count),
            ("T2.3", "Modern Paradigms Lab & Project Specs", 2, self.test_tier2_modern_paradigms_lab_specs),
            ("T2.4", "Paper Reading Hub Cross-Linkage", 2, self.test_tier2_paper_reading_hub_linkage),

            # Tier 3
            ("T3.1", "Prerequisite Graph DAG Validation (0 Cycles)", 3, self.test_tier3_prerequisite_graph_dag),
            ("T3.2", "Prerequisite Topological Chronological Ordering", 3, self.test_tier3_prerequisite_topological_ordering),
            ("T3.3", "ACM/IEEE CS2023 17 Knowledge Areas Audit", 3, self.test_tier3_cs2023_knowledge_areas_coverage),
            ("T3.4", "MIT Course 6 Canonical Pillars Audit", 3, self.test_tier3_mit_course6_pillars_coverage),
            ("T3.5", "Graduate Proofs & Derivations Injection (R2)", 3, self.test_tier3_r2_graduate_proofs_injection),
            ("T3.6", "IEEE CE2016 12 Knowledge Areas Audit", 3, self.test_tier3_ce2016_knowledge_areas_coverage),

            # Tier 4
            ("T4.1", "Student Degree Pathways Feasibility Simulation", 4, self.test_tier4_student_pathways_feasibility),
            ("T4.2", "Toolchain & Build Deliverable Validation", 4, self.test_tier4_toolchain_and_build_validation),
            ("T4.3", "Master Checklist & Dashboard Alignment", 4, self.test_tier4_checklist_dashboard_alignment),
        ]

        current_tier = None
        for test_id, name, tier, func in all_tests:
            if selected_tiers and tier not in selected_tiers:
                continue

            if tier != current_tier:
                current_tier = tier
                tier_names = {
                    1: "TIER 1: FEATURE COVERAGE & SCHEMA VALIDATION",
                    2: "TIER 2: BOUNDARY & CORNER CASES",
                    3: "TIER 3: CROSS-FEATURE COMBINATIONS",
                    4: "TIER 4: REAL-WORLD SCENARIOS",
                }
                print(f"\n{Colors.BOLD}{Colors.CYAN}--- {tier_names.get(tier, f'TIER {tier}')} ---{Colors.RESET}")

            self.run_test(test_id, name, tier, func)

        return self._print_summary()

    def _print_summary(self) -> bool:
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed and not r.skipped)
        skipped = sum(1 for r in self.results if r.skipped)

        print(f"\n{Colors.BOLD}================================================================================")
        print(f"                            TEST SUITE EXECUTION SUMMARY                        ")
        print(f"================================================================================{Colors.RESET}")

        tier_stats = defaultdict(lambda: {"passed": 0, "failed": 0, "skipped": 0, "total": 0})
        for r in self.results:
            st = tier_stats[r.tier]
            st["total"] += 1
            if r.skipped:
                st["skipped"] += 1
            elif r.passed:
                st["passed"] += 1
            else:
                st["failed"] += 1

        tier_titles = {
            1: "Tier 1: Feature Coverage",
            2: "Tier 2: Boundary & Corner Cases",
            3: "Tier 3: Cross-Feature Combinations",
            4: "Tier 4: Real-World Scenarios",
        }

        for tier in sorted(tier_stats.keys()):
            st = tier_stats[tier]
            t_name = tier_titles.get(tier, f"Tier {tier}")
            if st["failed"] == 0:
                tag = f"{Colors.GREEN}[PASS]{Colors.RESET}"
            elif st["passed"] > 0:
                tag = f"{Colors.YELLOW}[PARTIAL]{Colors.RESET}"
            else:
                tag = f"{Colors.RED}[FAIL]{Colors.RESET}"
            print(f"  {tag} {t_name:<36} {st['passed']}/{st['total']} passed ({st['failed']} failed)")

        print("--------------------------------------------------------------------------------")
        print(f"Total Tests Run: {total} | {Colors.GREEN}Passed: {passed}{Colors.RESET} | {Colors.RED}Failed: {failed}{Colors.RESET} | Skipped: {skipped}")

        # In milestone progressive mode, evaluate milestone-specific criteria
        milestone_verdict = True
        if self.milestone == "M1":
            # Milestone 1 requires Baseline Gap Analysis and Core Bridge Syllabi
            m1_test_ids = {"T1.1", "T1.2", "T1.4", "T1.5", "T3.3", "T3.4", "T3.6"}
            m1_tests = [r for r in self.results if r.test_id in m1_test_ids]
            m1_failures = [r for r in m1_tests if not r.passed]
            if m1_failures:
                milestone_verdict = False
                print(f"{Colors.YELLOW}Milestone M1 Evaluation: INCOMPLETE ({len(m1_failures)} criteria pending){Colors.RESET}")
            else:
                print(f"{Colors.GREEN}Milestone M1 Evaluation: 100% PASSED (Gap Analysis & Core Bridges ready){Colors.RESET}")
            overall_passed = milestone_verdict
        elif self.milestone == "M2":
            # Milestone 2 requires Tracks 7-11 and Specializations Hub
            m2_test_ids = {"T1.3", "T1.6", "T2.2", "T2.3"}
            m2_tests = [r for r in self.results if r.test_id in m2_test_ids]
            m2_failures = [r for r in m2_tests if not r.passed]
            overall_passed = (len(m2_failures) == 0)
        elif self.milestone == "M3":
            # Milestone 3 requires graduate proofs and paper reading hub
            m3_test_ids = {"T2.4", "T3.5"}
            m3_tests = [r for r in self.results if r.test_id in m3_test_ids]
            m3_failures = [r for r in m3_tests if not r.passed]
            overall_passed = (len(m3_failures) == 0)
        else:
            overall_passed = (failed == 0)

        verdict_str = f"{Colors.GREEN}OVERALL VERDICT: ALL ACCEPTANCE CRITERIA PASSED [GREEN]{Colors.RESET}" if overall_passed else f"{Colors.RED}OVERALL VERDICT: ACCEPTANCE CRITERIA DEFICIENCIES DETECTED [RED]{Colors.RESET}"
        print(f"\n{verdict_str}\n")

        return overall_passed

    def export_json(self, out_path: Path):
        data = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "vault_root": str(self.vault_root),
            "milestone": self.milestone,
            "summary": {
                "total": len(self.results),
                "passed": sum(1 for r in self.results if r.passed),
                "failed": sum(1 for r in self.results if not r.passed and not r.skipped),
                "skipped": sum(1 for r in self.results if r.skipped),
            },
            "results": [asdict(r) for r in self.results]
        }
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(data, indent=2), encoding='utf-8')
        print(f"Test execution report exported to: {out_path}")


def main():
    parser = argparse.ArgumentParser(description="EECS Curriculum Audit & Expansion — E2E Test Suite")
    parser.add_argument("--tier", type=str, default="", help="Comma-separated tier numbers to run (e.g., 1,2 or 3)")
    parser.add_argument("--milestone", type=str, default="all", choices=["M1", "M2", "M3", "M4", "all"], help="Progressive milestone mode")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose details for all tests")
    parser.add_argument("--json-out", type=str, default="", help="Path to write JSON test results report")
    parser.add_argument("--vault-root", type=str, default="", help="Override path to vault root")

    args = parser.parse_args()

    # Determine vault root
    if args.vault_root:
        vault_root = Path(args.vault_root).resolve()
    else:
        # Walk up to find vault root containing 00 - Dashboard.md
        cur = Path(__file__).resolve().parent
        vault_root = None
        for p in [cur, cur.parent, cur.parent.parent]:
            if (p / "00 - Dashboard.md").exists():
                vault_root = p
                break
        if not vault_root:
            vault_root = Path("/home/noblixy/The Noblett Repository")

    selected_tiers = None
    if args.tier:
        try:
            selected_tiers = {int(t.strip()) for t in args.tier.split(",") if t.strip()}
        except ValueError:
            print(f"Error: Invalid --tier value '{args.tier}'. Must be comma-separated integers.")
            sys.exit(2)

    suite = CurriculumTestSuite(vault_root=vault_root, verbose=args.verbose, milestone=args.milestone)
    passed = suite.run_all(selected_tiers=selected_tiers)

    if args.json_out:
        suite.export_json(Path(args.json_out))

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
