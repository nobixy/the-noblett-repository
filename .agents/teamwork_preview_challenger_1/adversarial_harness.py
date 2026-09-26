#!/usr/bin/env python3
"""
Adversarial Stress Test Harness — Challenger 1 (Milestone 4)
===========================================================
Independent, empirical verification harness for:
1. Obsidian [[wikilink]] vault-wide integrity (including anchor/heading verification,
   escaped markdown table pipes, aliases, template placeholder isolation).
2. Comprehensive Prerequisite Directed Acyclic Graph (DAG) construction and cycle detection
   (using Tarjan's SCC, DFS cycle extraction, and Kahn's topological sort across both
   explicit frontmatter/body declarations and canonical academic sequences).
3. Negative Controls & Invalidation Proofs (asserting the detector detects induced cycles
   and induced broken links).
"""

import sys
import os
import re
import json
import time
from pathlib import Path
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple, Optional, Any

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository").resolve()

class VaultIndexer:
    def __init__(self, root: Path):
        self.root = root
        self.all_files: Set[str] = set()
        self.md_files: Dict[str, str] = {}  # rel_path -> content
        self.exact_map: Dict[str, str] = {}  # lower(rel_path) -> rel_path
        self.stem_map: Dict[str, List[str]] = defaultdict(list)
        self.name_map: Dict[str, List[str]] = defaultdict(list)
        self.headings_map: Dict[str, Set[str]] = defaultdict(set)  # rel_path -> set of lower(heading_text)
        self._index()

    def _index(self):
        for r, dirs, files in os.walk(self.root):
            # Ignore git, agent workspace, and obsidian internal caches
            if any(p in r for p in [".git", ".agents", ".obsidian"]):
                continue
            for f in files:
                p = Path(r) / f
                rel = str(p.relative_to(self.root))
                self.all_files.add(rel)
                self.exact_map[rel.lower().replace("\\", "/")] = rel
                self.stem_map[p.stem.lower()].append(rel)
                self.name_map[p.name.lower()].append(rel)

                if f.endswith(".md"):
                    try:
                        content = p.read_text(encoding="utf-8", errors="ignore")
                        self.md_files[rel] = content
                        for line in content.splitlines():
                            line_s = line.strip()
                            if line_s.startswith("#"):
                                m = re.match(r"^#{1,6}\s+(.*)$", line_s)
                                if m:
                                    # Normalize heading text for anchor matching
                                    h_text = m.group(1).strip().lower()
                                    self.headings_map[rel].add(h_text)
                    except Exception as e:
                        print(f"Warning: could not read {rel}: {e}", file=sys.stderr)

    def resolve_wikilink(self, raw_link: str, source_rel: str) -> Tuple[Optional[str], Optional[str], bool]:
        """
        Resolves a wikilink target according to Obsidian rules.
        Returns: (resolved_file_rel_path or None, anchor_text or None, is_template_var)
        """
        # Clean escaped pipes from markdown tables
        cleaned = raw_link.replace(r"\|", "|").strip()

        # Check for template variables
        if "{{" in cleaned and "}}" in cleaned:
            return None, None, True
        if cleaned.startswith("Related Note"):
            return None, None, True

        # Split alias
        if "|" in cleaned:
            target, _ = cleaned.split("|", 1)
        else:
            target = cleaned
        target = target.strip()

        # Split anchor (#heading or #^block)
        anchor = None
        if "#" in target:
            target, anchor = target.split("#", 1)
            target = target.strip()
            anchor = anchor.strip()

        # If target is empty, it refers to the source file itself
        if not target:
            return source_rel, anchor, False

        t_lower = target.lower().replace("\\", "/")

        # 1. Exact match relative path
        if t_lower in self.exact_map:
            return self.exact_map[t_lower], anchor, False
        if (t_lower + ".md") in self.exact_map:
            return self.exact_map[t_lower + ".md"], anchor, False

        # 2. Relative to current file folder
        src_parent = str(Path(source_rel).parent).replace("\\", "/")
        if src_parent != ".":
            cand = f"{src_parent}/{t_lower}"
            if cand in self.exact_map:
                return self.exact_map[cand], anchor, False
            if (cand + ".md") in self.exact_map:
                return self.exact_map[cand + ".md"], anchor, False

        # 3. Match stem or name
        target_name = Path(target).name.lower()
        target_stem = Path(target).stem.lower()
        if target_name in self.name_map:
            return self.name_map[target_name][0], anchor, False
        if target_stem in self.stem_map:
            return self.stem_map[target_stem][0], anchor, False

        # 4. Suffix match
        for f, real_rel in self.exact_map.items():
            if f.endswith("/" + t_lower) or f.endswith("/" + t_lower + ".md"):
                return real_rel, anchor, False

        return None, anchor, False


def stress_test_wikilinks(indexer: VaultIndexer) -> Dict[str, Any]:
    print("\n" + "="*80)
    print("STRESS TEST 1: OBSIDIAN WIKILINK INTEGRITY AUDIT")
    print("="*80)

    wikilink_re = re.compile(r"!?\[\[([^\]]+)\]\]")
    total_links = 0
    valid_links = 0
    template_placeholders = 0
    broken_links = []
    broken_anchors = []

    for rel_path, content in indexer.md_files.items():
        is_template_file = "08 - Templates" in rel_path

        for line_no, line in enumerate(content.splitlines(), 1):
            for m in wikilink_re.finditer(line):
                total_links += 1
                raw_inner = m.group(1)

                resolved_rel, anchor, is_var = indexer.resolve_wikilink(raw_inner, rel_path)

                if is_var:
                    template_placeholders += 1
                    continue

                if not resolved_rel:
                    broken_links.append({
                        "file": rel_path,
                        "line": line_no,
                        "raw": raw_inner,
                        "reason": "Target file not found in vault"
                    })
                else:
                    valid_links += 1
                    # If anchor present, check heading existence
                    if anchor and not anchor.startswith("^"):
                        # Normalize anchor
                        anchor_norm = anchor.lower().replace("-", " ")
                        headings = indexer.headings_map.get(resolved_rel, set())
                        # Check partial or exact match in headings
                        matched = any(anchor_norm in h for h in headings)
                        if not matched:
                            broken_anchors.append({
                                "file": rel_path,
                                "line": line_no,
                                "raw": raw_inner,
                                "target_file": resolved_rel,
                                "anchor": anchor,
                                "available_headings": list(headings)[:5]
                            })

    print(f"Total wikilinks scanned:         {total_links}")
    print(f"Successfully resolved to files:  {valid_links}")
    print(f"Template variables / placeholders: {template_placeholders}")
    print(f"Broken file targets:             {len(broken_links)}")
    print(f"Broken heading anchors:          {len(broken_anchors)}")

    success = len(broken_links) == 0 and len(broken_anchors) == 0
    print(f"STATUS: {'PASS [0 Broken Links]' if success else 'FAIL'}")

    return {
        "pass": success,
        "total_links": total_links,
        "valid_links": valid_links,
        "template_placeholders": template_placeholders,
        "broken_links": broken_links,
        "broken_anchors": broken_anchors
    }


def build_prerequisite_graph(indexer: VaultIndexer) -> Tuple[Dict[str, Set[str]], Dict[str, Dict[str, Any]]]:
    """
    Constructs an exhaustive prerequisite directed graph:
    u -> v means u is a prerequisite of v (u must be taken before v).
    """
    graph: Dict[str, Set[str]] = defaultdict(set)
    node_metadata: Dict[str, Dict[str, Any]] = {}

    # Term hierarchy mapping for chronological verification
    term_order = {
        "Phase -1": 0,
        "Phase 0": 1,
        "Year 1 Fall": 2,
        "Year 1 Spring": 3,
        "Year 2 Fall": 4,
        "Year 2 Spring": 5,
        "Year 3 Fall": 6,
        "Year 3 Spring": 7,
        "Year 4 Fall": 8,
        "Year 4 Spring": 9,
        "Year 5 (Two Semesters)": 10,
        "Year 5 Fall": 10,
        "Year 5 Spring": 11,
        "Year 5 MEng": 11,
    }

    # 1. Register all curriculum block nodes and their academic terms
    for rel_path, content in indexer.md_files.items():
        if not rel_path.startswith("01 - Curriculum/"):
            continue
        stem = Path(rel_path).stem

        # Extract frontmatter term
        term_val = None
        m_term = re.search(r"^term:\s*\"?([^\n\r\"]+)\"?", content, re.MULTILINE)
        if m_term:
            term_val = m_term.group(1).strip()
        elif "Phase -1" in rel_path:
            term_val = "Phase -1"
        elif "Phase 0" in rel_path:
            term_val = "Phase 0"

        node_metadata[stem] = {
            "rel_path": rel_path,
            "term": term_val,
            "term_rank": term_order.get(term_val, 99) if term_val else 99
        }

    # 2. Foundational canonical curricular prerequisite chains
    canonical_edges = [
        # Bedrock & Phase 0 to Year 1
        ("B0 - The Deep Learner's Toolkit", "P1 - Learning How to Learn"),
        ("BM - Bedrock Mathematics", "P3 - Math Prerequisites"),
        ("P3 - Math Prerequisites", "02 - Calculus I"),
        ("P3 - Math Prerequisites", "10 - Math for CS"),
        ("P4 - Programming On-Ramp", "01 - CS61A"),
        ("P4 - Programming On-Ramp", "06 - C Fluency"),
        ("P5 - Tooling", "06 - C Fluency"),
        ("P5 - Tooling", "09 - Computer Systems"),

        # Year 1 internal
        ("02 - Calculus I", "07 - Multivariable Calculus"),
        ("02 - Calculus I", "03 - Physics I"),
        ("03 - Physics I", "08 - Physics II"),
        ("07 - Multivariable Calculus", "04a - Differential Equations Bridge"),
        ("08 - Physics II", "08a - Circuits and Electronics Bridge"),
        ("01 - CS61A", "05 - SICP"),
        ("04 - Nand2Tetris", "09 - Computer Systems"),

        # Year 1 to Year 2
        ("04a - Differential Equations Bridge", "15a - Signals and Systems Bridge"),
        ("06 - C Fluency", "09 - Computer Systems"),
        ("06 - C Fluency", "12 - Interpreters"),
        ("06 - C Fluency", "13 - Algorithms I"),
        ("01 - CS61A", "12 - Interpreters"),
        ("07 - Multivariable Calculus", "11 - Linear Algebra"),
        ("10 - Math for CS", "13 - Algorithms I"),
        ("10 - Math for CS", "15 - Probability"),

        # Year 2 internal & Year 2 to Year 3
        ("09 - Computer Systems", "14 - Computer Architecture"),
        ("09 - Computer Systems", "16 - Operating Systems"),
        ("13 - Algorithms I", "20 - Algorithms II"),
        ("15 - Probability", "22 - Statistics"),
        ("09 - Computer Systems", "19 - Networking"),
        ("13 - Algorithms I", "21 - Databases"),
        ("09 - Computer Systems", "21 - Databases"),
        ("05 - SICP", "17 - Software Construction"),
        ("07 - Multivariable Calculus", "18 - Real Analysis"),

        # Year 3 to Year 4
        ("16 - Operating Systems", "23 - Distributed Systems"),
        ("19 - Networking", "23 - Distributed Systems"),
        ("20 - Algorithms II", "24 - Theory of Computation"),
        ("10 - Math for CS", "24 - Theory of Computation"),
        ("11 - Linear Algebra", "25 - Convex Optimization"),
        ("07 - Multivariable Calculus", "25 - Convex Optimization"),
        ("16 - Operating Systems", "27 - Intensive Cryptopals or TLA+"),

        # Year 4 to Year 5
        ("23 - Distributed Systems", "30 - Capstone"),
        ("26 - Specialization A1", "28 - Specialization A2"),
        ("29 - Specialization B1", "31 - Specialization B2"),
        ("28 - Specialization A2", "30 - Capstone"),
        ("31 - Specialization B2", "30 - Capstone"),
        ("15 - Probability", "32 - Information Theory"),
    ]

    for u, v in canonical_edges:
        if u in node_metadata and v in node_metadata:
            graph[u].add(v)

    # 3. Parse explicit frontmatter prerequisites and body prerequisites across all files
    wikilink_re = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|([^\]]+))?\]\]")

    for rel_path, content in indexer.md_files.items():
        if not rel_path.startswith("01 - Curriculum/"):
            continue
        v_stem = Path(rel_path).stem

        # Extract frontmatter prerequisites line
        fm_match = re.search(r"^prerequisites:\s*\"?([^\n\r\"]+)\"?", content, re.MULTILINE)
        if fm_match:
            prereq_line = fm_match.group(1)
            for m in wikilink_re.finditer(prereq_line):
                target = m.group(1).strip()
                resolved_rel, _, _ = indexer.resolve_wikilink(target, rel_path)
                if resolved_rel:
                    u_stem = Path(resolved_rel).stem
                    if u_stem != v_stem:
                        graph[u_stem].add(v_stem)

        # Extract body prerequisites (e.g., '> - **Prerequisites:** ...' or 'Prerequisites: ...')
        for line in content.splitlines():
            if re.search(r"\bprerequisites?:", line, re.IGNORECASE):
                for m in wikilink_re.finditer(line):
                    target = m.group(1).strip()
                    resolved_rel, _, _ = indexer.resolve_wikilink(target, rel_path)
                    if resolved_rel:
                        u_stem = Path(resolved_rel).stem
                        if u_stem != v_stem:
                            graph[u_stem].add(v_stem)

    return graph, node_metadata


def tarjan_scc(graph: Dict[str, Set[str]], all_nodes: Set[str]) -> List[List[str]]:
    """Finds all strongly connected components using Tarjan's algorithm."""
    index = 0
    indices: Dict[str, int] = {}
    lowlinks: Dict[str, int] = {}
    on_stack: Set[str] = set()
    stack: List[str] = []
    sccs: List[List[str]] = []

    def strongconnect(v: str):
        nonlocal index
        indices[v] = index
        lowlinks[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        for w in graph.get(v, []):
            if w not in indices:
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in on_stack:
                lowlinks[v] = min(lowlinks[v], indices[w])

        if lowlinks[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for node in sorted(all_nodes):
        if node not in indices:
            strongconnect(node)

    return sccs


def find_elementary_cycles(graph: Dict[str, Set[str]], all_nodes: Set[str]) -> List[List[str]]:
    """Extracts all elementary directed cycles via DFS 3-coloring."""
    visited: Dict[str, int] = {n: 0 for n in all_nodes}  # 0: white, 1: gray, 2: black
    cycles: List[List[str]] = []

    def dfs(node: str, path: List[str]):
        visited[node] = 1
        for nxt in sorted(graph.get(node, [])):
            if visited[nxt] == 1:
                # Cycle found
                cycle = path + [nxt]
                cycle_from = cycle[cycle.index(nxt):]
                cycles.append(cycle_from)
            elif visited[nxt] == 0:
                dfs(nxt, path + [nxt])
        visited[node] = 2

    for n in sorted(all_nodes):
        if visited[n] == 0:
            dfs(n, [n])

    return cycles


def kahn_topological_sort(graph: Dict[str, Set[str]], all_nodes: Set[str]) -> Tuple[List[str], bool]:
    """Performs topological sort using Kahn's algorithm."""
    in_degree: Dict[str, int] = {n: 0 for n in all_nodes}
    for u in all_nodes:
        for v in graph.get(u, []):
            if v in in_degree:
                in_degree[v] += 1

    queue = deque([n for n in all_nodes if in_degree[n] == 0])
    order: List[str] = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v in in_degree:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    is_dag = len(order) == len(all_nodes)
    return order, is_dag


def stress_test_dag(indexer: VaultIndexer) -> Dict[str, Any]:
    print("\n" + "="*80)
    print("STRESS TEST 2: PREREQUISITE GRAPH DAG & CYCLE DETECTION AUDIT")
    print("="*80)

    graph, node_metadata = build_prerequisite_graph(indexer)
    all_nodes = set(node_metadata.keys()) | set(graph.keys())
    for u in list(graph.keys()):
        all_nodes.update(graph[u])

    edge_count = sum(len(neighbors) for neighbors in graph.values())
    print(f"Total curriculum nodes in graph:  {len(all_nodes)}")
    print(f"Total directed prerequisite edges: {edge_count}")

    # 1. Tarjan's SCC
    sccs = tarjan_scc(graph, all_nodes)
    cyclic_sccs = [scc for scc in sccs if len(scc) > 1 or (len(scc) == 1 and scc[0] in graph.get(scc[0], set()))]
    print(f"Tarjan SCC count:                  {len(sccs)}")
    print(f"Cyclic SCCs detected:              {len(cyclic_sccs)}")

    # 2. Elementary cycles via DFS
    cycles = find_elementary_cycles(graph, all_nodes)
    print(f"Elementary cycles detected:        {len(cycles)}")

    # 3. Kahn's Topological Sort
    topo_order, is_dag = kahn_topological_sort(graph, all_nodes)
    print(f"Kahn topological sort valid:       {is_dag}")
    print(f"Topologically ordered nodes count: {len(topo_order)} / {len(all_nodes)}")

    # 4. Temporal Chronology Audit: Verify no prerequisite requires a course from a later term
    temporal_violations = []
    for u, neighbors in graph.items():
        u_meta = node_metadata.get(u)
        u_rank = u_meta["term_rank"] if u_meta else None
        if u_rank is None or u_rank == 99:
            continue
        for v in neighbors:
            v_meta = node_metadata.get(v)
            v_rank = v_meta["term_rank"] if v_meta else None
            if v_rank is None or v_rank == 99:
                continue
            # If u is prerequisite for v, then u's term must be <= v's term
            if u_rank > v_rank:
                temporal_violations.append({
                    "prerequisite": u,
                    "prereq_term": u_meta["term"],
                    "prereq_rank": u_rank,
                    "target": v,
                    "target_term": v_meta["term"],
                    "target_rank": v_rank,
                    "reason": f"Prerequisite '{u}' ({u_meta['term']}) occurs AFTER target '{v}' ({v_meta['term']})"
                })

    print(f"Temporal causality violations:    {len(temporal_violations)}")
    for tv in temporal_violations[:5]:
        print(f"  VIOLATION: {tv['reason']}")

    success = (len(cyclic_sccs) == 0) and (len(cycles) == 0) and is_dag and (len(temporal_violations) == 0)
    print(f"STATUS: {'PASS [Strict DAG, 0 Cycles, 0 Chronology Violations]' if success else 'FAIL'}")

    return {
        "pass": success,
        "node_count": len(all_nodes),
        "edge_count": edge_count,
        "cyclic_sccs": cyclic_sccs,
        "cycles": [" -> ".join(c) for c in cycles],
        "is_dag": is_dag,
        "topological_sample": topo_order[:10],
        "temporal_violations": temporal_violations
    }


def negative_control_tests(indexer: VaultIndexer) -> Dict[str, Any]:
    print("\n" + "="*80)
    print("STRESS TEST 3: NEGATIVE CONTROLS (ORACLE INVALIDATION PROOFS)")
    print("="*80)

    # 1. Induced cycle test: inject cycle into a synthetic graph
    graph, node_meta = build_prerequisite_graph(indexer)
    all_nodes = set(node_meta.keys()) | set(graph.keys())
    for u in list(graph.keys()):
        all_nodes.update(graph[u])

    cloned_graph = {u: set(graph.get(u, set())) for u in all_nodes}
    # Inject cycle: 09 - Computer Systems -> 16 - Operating Systems -> 23 - Distributed Systems -> 09 - Computer Systems
    cloned_graph["23 - Distributed Systems"].add("09 - Computer Systems")

    injected_cycles = find_elementary_cycles(cloned_graph, all_nodes)
    _, injected_is_dag = kahn_topological_sort(cloned_graph, all_nodes)

    cycle_detected_properly = (len(injected_cycles) > 0) and (not injected_is_dag)
    print(f"Negative Control 1 (Injected Cycle Detection): {'PASS (Cycle correctly caught)' if cycle_detected_properly else 'FAIL'}")
    if cycle_detected_properly:
        print(f"  Caught cycle: {' -> '.join(injected_cycles[0])}")

    # 2. Induced broken link test: test resolver on deliberate nonsense
    nonsense_link = "NonExistentCourse_99999"
    res_file, _, _ = indexer.resolve_wikilink(nonsense_link, "00 - Dashboard.md")
    broken_link_properly_rejected = (res_file is None)
    print(f"Negative Control 2 (Broken Link Rejection):   {'PASS (Non-existent link rejected)' if broken_link_properly_rejected else 'FAIL'}")

    success = cycle_detected_properly and broken_link_properly_rejected
    return {
        "pass": success,
        "injected_cycle_detected": cycle_detected_properly,
        "broken_link_rejected": broken_link_properly_rejected
    }


def main():
    print(f"Initializing Vault Indexer at: {VAULT_ROOT}")
    t0 = time.perf_counter()
    indexer = VaultIndexer(VAULT_ROOT)
    t_idx = (time.perf_counter() - t0) * 1000.0
    print(f"Vault indexed in {t_idx:.2f}ms ({len(indexer.all_files)} total files, {len(indexer.md_files)} markdown notes)")

    t1 = time.perf_counter()
    wikilink_res = stress_test_wikilinks(indexer)
    t_wiki = (time.perf_counter() - t1) * 1000.0

    t2 = time.perf_counter()
    dag_res = stress_test_dag(indexer)
    t_dag = (time.perf_counter() - t2) * 1000.0

    t3 = time.perf_counter()
    neg_res = negative_control_tests(indexer)
    t_neg = (time.perf_counter() - t3) * 1000.0

    overall_pass = wikilink_res["pass"] and dag_res["pass"] and neg_res["pass"]

    print("\n" + "="*80)
    print("CHALLENGER 1 ADVERSARIAL STRESS TEST SUMMARY")
    print("="*80)
    print(f"Wikilink Integrity:   {'PASS' if wikilink_res['pass'] else 'FAIL'} ({t_wiki:.1f}ms)")
    print(f"DAG Acyclicity:       {'PASS' if dag_res['pass'] else 'FAIL'} ({t_dag:.1f}ms)")
    print(f"Negative Controls:    {'PASS' if neg_res['pass'] else 'FAIL'} ({t_neg:.1f}ms)")
    print(f"OVERALL STRESS RESULT:{'PASS [GREEN]' if overall_pass else 'FAIL [RED]'}")

    out_path = Path("/home/noblixy/The Noblett Repository/.agents/teamwork_preview_challenger_1/adversarial_results.json")
    full_report = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "overall_pass": overall_pass,
        "verdict": "APPROVE" if overall_pass else "REQUEST_CHANGES",
        "wikilinks": wikilink_res,
        "dag": dag_res,
        "negative_controls": neg_res,
        "benchmarks_ms": {
            "indexing": t_idx,
            "wikilinks": t_wiki,
            "dag": t_dag,
            "negative_controls": t_neg
        }
    }
    out_path.write_text(json.dumps(full_report, indent=2))
    print(f"\nFull stress test report exported to: {out_path}")

    return 0 if overall_pass else 1

if __name__ == "__main__":
    sys.exit(main())
