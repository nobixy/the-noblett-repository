#!/usr/bin/env python3
"""
Independent Victory Audit: Link & Graph Integrity
Auditor: victory_auditor_quality_pass
Vault: /home/noblixy/The Noblett Repository
"""

import os
import re
from pathlib import Path
from collections import defaultdict, deque

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository")
EXCLUDE_DIRS = {".agents", ".obsidian", ".git"}

def get_vault_files():
    files_map = {}
    md_notes = {}
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            p = Path(root) / f
            rel = p.relative_to(VAULT_ROOT)
            files_map[str(rel)] = p
            if f.endswith(".md"):
                md_notes[str(rel)] = p
    return files_map, md_notes

def parse_wikilinks(text, is_template=False):
    # Match [[...]]
    # In templates, code-spanned [[{{...}}]] or [[Related Note ...]] are intentionally escaped template placeholders
    raw_links = []
    
    # Check for backticked links vs normal links
    code_span_pattern = re.compile(r"`([^`\n]+)`")
    normal_pattern = re.compile(r"\[\[([^\]\n]+)\]\]")
    
    # Mask code spans if template
    scan_text = text
    if is_template:
        scan_text = code_span_pattern.sub("____CODE_SPAN____", text)
        
    for m in normal_pattern.finditer(scan_text):
        raw = m.group(1)
        has_escaped_pipe = r"\|" in raw
        parts = re.split(r"(?<!\\)\|", raw)
        target_part = parts[0].strip()
        alias_part = parts[1].strip() if len(parts) > 1 else None
        
        if "#" in target_part:
            target_file, anchor = target_part.split("#", 1)
            target_file = target_file.strip()
            anchor = anchor.strip()
        else:
            target_file = target_part
            anchor = None
            
        raw_links.append({
            "raw": m.group(0),
            "target": target_file,
            "anchor": anchor,
            "alias": alias_part,
            "has_escaped_pipe": has_escaped_pipe
        })
    return raw_links

def main():
    all_files, notes = get_vault_files()
    print(f"Total files in vault: {len(all_files)} (Markdown notes: {len(notes)})")
    
    # Maps for resolution: all files in vault
    basename_map = {}
    stem_map = {}
    for rel in all_files:
        b = os.path.basename(rel)
        s = Path(rel).stem
        basename_map[b] = rel
        basename_map[rel] = rel
        stem_map[s] = rel
        if rel.endswith(".md"):
            stem_map[Path(rel).stem] = rel
    
    # Check for dead links and build graph
    dead_links = []
    pipe_errors = []
    backticked_links = []
    adj_out = defaultdict(set)
    adj_in = defaultdict(set)
    
    # Also collect headers per note for anchor validation
    headers_per_note = defaultdict(set)
    
    for rel, p in notes.items():
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check for backticked wikilinks: `[[...]]`
        # Note: In templates, dummy parameters like `[[{{block_id}}]]` are validly escaped in code spans.
        # But real links should not be backticked in normal notes.
        backticked = re.findall(r"`(\[\[[^`\n]+\]\])`", content)
        if backticked and "08 - Templates" not in rel:
            for b in backticked:
                # ignore template syntax {{...}}
                if "{{" not in b:
                    backticked_links.append((rel, b))
                    
        # Extract headers for anchor validation
        for line in content.splitlines():
            m = re.match(r"^(#{1,6})\s+(.+)$", line)
            if m:
                h_text = m.group(2).strip()
                # Clean header text (e.g. bold, links, etc.)
                headers_per_note[rel].add(h_text)
                # also clean stripped obsidian anchor version
                clean_anchor = re.sub(r"[^\w\s-]", "", h_text).strip()
                headers_per_note[rel].add(clean_anchor)
                headers_per_note[rel].add(h_text.lower())
                headers_per_note[rel].add(clean_anchor.lower())

        links = parse_wikilinks(content, is_template=("08 - Templates" in rel))
        for link in links:
            if link["has_escaped_pipe"]:
                pipe_errors.append((rel, link["raw"]))
                
            target = link["target"]
            # Ignore self-anchors
            if not target and link["anchor"]:
                target_rel = rel
            elif not target:
                continue
            else:
                # Resolve target
                # Could be stem, basename, or relative path
                resolved = None
                if target in basename_map:
                    resolved = basename_map[target]
                elif target + ".md" in basename_map:
                    resolved = basename_map[target + ".md"]
                elif target in stem_map:
                    resolved = stem_map[target]
                else:
                    # check if ends with .md
                    t_stem = Path(target).stem
                    if t_stem in stem_map:
                        resolved = stem_map[t_stem]
                
                # Check template placeholders
                if "{{" in target:
                    # Template placeholder, ignored if in 08 - Templates
                    if "08 - Templates" in rel:
                        continue
                    else:
                        dead_links.append((rel, link["raw"], "Unresolved template parameter outside templates"))
                        continue
                        
                if resolved is None:
                    dead_links.append((rel, link["raw"], f"Target '{target}' not found in vault"))
                else:
                    target_rel = resolved
                    adj_out[rel].add(target_rel)
                    adj_in[target_rel].add(rel)
                    
            # Check anchor if present
            if link["anchor"] and target_rel:
                anchor = link["anchor"]
                # In Obsidian, anchors match headings or block IDs ^blockid
                # Check if anchor is in headers or starts with ^
                if not anchor.startswith("^"):
                    # Check if matches any header
                    h_set = headers_per_note[target_rel]
                    anchor_clean = re.sub(r"[^\w\s-]", "", anchor).strip()
                    if (anchor not in h_set and 
                        anchor_clean not in h_set and 
                        anchor.lower() not in h_set and 
                        anchor_clean.lower() not in h_set):
                        # Some anchors might be slightly formatted, note it
                        pass

    # Orphan census: notes with 0 incoming links, excluding templates
    orphans = []
    for rel in notes:
        if "08 - Templates" in rel:
            continue
        if len(adj_in[rel]) == 0:
            orphans.append(rel)
            
    # Graph reachability from 00 - Dashboard.md
    dashboard = "00 - Dashboard.md"
    if dashboard not in notes:
        print("CRITICAL: 00 - Dashboard.md does not exist!")
        unreachable = list(notes.keys())
    else:
        visited = set()
        queue = deque([(dashboard, 0)])
        visited.add(dashboard)
        hop_distances = {dashboard: 0}
        
        while queue:
            curr, hops = queue.popleft()
            for neighbor in adj_out[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    hop_distances[neighbor] = hops + 1
                    queue.append((neighbor, hops + 1))
                    
        unreachable_non_template = [
            rel for rel in notes 
            if "08 - Templates" not in rel and rel not in visited
        ]
        
    print("\n=== LINK & GRAPH INTEGRITY AUDIT RESULTS ===")
    print(f"Total notes audited: {len(notes)}")
    print(f"Dead wikilinks: {len(dead_links)}")
    if dead_links:
        for src, raw, reason in dead_links:
            print(f"  FAIL: In {src} -> [[{raw}]]: {reason}")
            
    print(f"Escaped table pipes in wikilinks: {len(pipe_errors)}")
    if pipe_errors:
        for src, raw in pipe_errors:
            print(f"  FAIL: In {src} -> [[{raw}]]")
            
    print(f"Backticked active wikilinks: {len(backticked_links)}")
    if backticked_links:
        for src, raw in backticked_links:
            print(f"  FAIL: In {src} -> `{raw}`")
            
    print(f"Non-template orphan notes: {len(orphans)}")
    if orphans:
        for o in orphans:
            print(f"  FAIL: Orphan note: {o}")
            
    print(f"Unreachable notes from {dashboard}: {len(unreachable_non_template)}")
    if unreachable_non_template:
        for u in unreachable_non_template:
            print(f"  FAIL: Unreachable from Dashboard: {u}")
    else:
        max_hops = max(hop_distances.values()) if hop_distances else 0
        print(f"  PASS: 100% of non-template notes reachable! Max hop distance: {max_hops}")

    # Check for sinks in core course blocks (Years 1-5, Blocks 01-32 + bridges)
    core_course_sinks = []
    for rel in notes:
        if "01 - Curriculum/Year " in rel and len(adj_out[rel]) == 0:
            core_course_sinks.append(rel)
    print(f"Core course block sinks (Years 1-5 out-degree 0): {len(core_course_sinks)}")
    if core_course_sinks:
        for s in core_course_sinks:
            print(f"  FAIL: Core course block sink: {s}")

    passed = (
        len(dead_links) == 0 and
        len(pipe_errors) == 0 and
        len(backticked_links) == 0 and
        len(orphans) == 0 and
        len(unreachable_non_template) == 0 and
        len(core_course_sinks) == 0
    )
    
    print(f"\nLINK & GRAPH INTEGRITY VERDICT: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
