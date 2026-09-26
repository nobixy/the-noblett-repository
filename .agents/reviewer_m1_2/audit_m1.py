#!/usr/bin/env python3
import os
import re
from collections import defaultdict, deque

VAULT_ROOT = "/home/noblixy/The Noblett Repository"

def audit_vault(exclude_files=set()):
    all_files = []
    md_files = []
    for r, d, fs in os.walk(VAULT_ROOT):
        # Ignore hidden directories (.git, .agents, .obsidian)
        parts = r.split(os.sep)
        if any(p.startswith(".") and p != "." for p in parts):
            continue
        for f in fs:
            if not f.startswith("."):
                rel = os.path.relpath(os.path.join(r, f), VAULT_ROOT)
                if rel in exclude_files:
                    continue
                all_files.append(rel)
                if f.endswith(".md"):
                    md_files.append(rel)
    
    stem_map = defaultdict(list)
    file_map = defaultdict(list)
    for p in all_files:
        bn = os.path.basename(p)
        file_map[bn.lower()].append(p)
        stem = os.path.splitext(bn)[0]
        stem_map[stem.lower()].append(p)
        
    def resolve(target, src_file):
        clean = target.strip()
        if "#" in clean:
            clean = clean.split("#", 1)[0].strip()
        if not clean:
            return src_file
        if clean.endswith("\\"):
            return None # Escaped pipe artifact
        
        # 1. Exact relative path
        if clean in all_files:
            return clean
        if (clean + ".md") in all_files:
            return clean + ".md"
        clean_low = clean.lower()
        for p in all_files:
            if p.lower() == clean_low or p.lower() == clean_low + ".md":
                return p
        
        # 2. Match relative to src_file
        cur_dir = os.path.dirname(src_file)
        rel_cand = os.path.normpath(os.path.join(cur_dir, clean))
        if rel_cand in all_files:
            return rel_cand
        if (rel_cand + ".md") in all_files:
            return rel_cand + ".md"
        for p in all_files:
            if p.lower() == rel_cand.lower() or p.lower() == (rel_cand + ".md").lower():
                return p
                
        # 3. Match stem or basename
        if clean_low in stem_map:
            return stem_map[clean_low][0]
        if clean_low in file_map:
            return file_map[clean_low][0]
            
        # 4. Suffix match
        norm = clean_low.replace("\\", "/")
        for p in all_files:
            p_norm = p.lower().replace("\\", "/")
            if p_norm.endswith("/" + norm) or p_norm.endswith("/" + norm + ".md"):
                return p
        return None

    wikilink_re = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|([^\]]+))?\]\]")
    
    dead_links_active = []
    dead_links_all = []
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    adjacency = defaultdict(set)
    total_active_links = 0
    total_all_links = 0
    
    for mf in md_files:
        full_path = os.path.join(VAULT_ROOT, mf)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        lines = content.splitlines()
        # Find frontmatter
        fm_end = 0
        if content.startswith("---"):
            for idx in range(1, len(lines)):
                if lines[idx].strip() == "---":
                    fm_end = idx + 1
                    break
                    
        # Find fenced code blocks
        code_lines = set()
        in_fence = False
        for idx, line in enumerate(lines, 1):
            if idx <= fm_end:
                continue
            if line.strip().startswith("```"):
                code_lines.add(idx)
                in_fence = not in_fence
            elif in_fence:
                code_lines.add(idx)
                
        for idx, line in enumerate(lines, 1):
            if idx <= fm_end or idx in code_lines:
                continue
            # Strip inline code
            line_no_inline = re.sub(r"`[^`]*`", "", line)
            
            # Active links (outside code spans)
            for m in wikilink_re.finditer(line_no_inline):
                total_active_links += 1
                tgt = m.group(1).strip()
                res = resolve(tgt, mf)
                if res:
                    if res in md_files and res != mf:
                        adjacency[mf].add(res)
                else:
                    dead_links_active.append((mf, idx, tgt, m.group(0)))
                    
            # All links (including inside inline code)
            for m in wikilink_re.finditer(line):
                total_all_links += 1
                tgt = m.group(1).strip()
                res = resolve(tgt, mf)
                if not res:
                    dead_links_all.append((mf, idx, tgt, m.group(0)))
                    
    for src, tgts in adjacency.items():
        out_degree[src] = len(tgts)
        for t in tgts:
            in_degree[t] += 1
            
    non_templates = [m for m in md_files if not m.startswith("08 - Templates/")]
    orphans = [m for m in non_templates if in_degree[m] == 0 and m != "00 - Dashboard.md"]
    
    # BFS from Dashboard
    start = "00 - Dashboard.md"
    visited = set()
    queue = deque([start])
    if start in md_files:
        visited.add(start)
    while queue:
        c = queue.popleft()
        for n in adjacency[c]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
                
    unreachable_non_temp = [m for m in non_templates if m not in visited]
    
    print(f"Total MD Files: {len(md_files)}")
    print(f"Non-Template MD Files: {len(non_templates)}")
    print(f"Total Active Wikilinks: {total_active_links}")
    print(f"Active Dead Links: {len(dead_links_active)}")
    for d in dead_links_active:
        print(f"  FAIL DEAD ACTIVE: {d[0]}:{d[1]} -> {d[3]}")
    print(f"Total Wikilinks (inc inline code): {total_all_links}")
    print(f"Dead Links (inc inline code): {len(dead_links_all)}")
    for d in dead_links_all:
        print(f"  FAIL DEAD ALL: {d[0]}:{d[1]} -> {d[3]}")
    print(f"Non-Template Orphans (in-degree=0): {len(orphans)}")
    for o in orphans:
        print(f"  FAIL ORPHAN: {o}")
    print(f"Unreachable Non-Templates from Dashboard: {len(unreachable_non_temp)}")
    for u in unreachable_non_temp:
        print(f"  FAIL UNREACHABLE: {u}")
    pct = (len(visited.intersection(set(non_templates))) / len(non_templates)) * 100.0 if non_templates else 0
    print(f"Dashboard Reachability: {len(visited.intersection(set(non_templates)))} / {len(non_templates)} ({pct:.2f}%)")

if __name__ == "__main__":
    print("=" * 70)
    print("INDEPENDENT AUDIT 1: LIVE VAULT CURRENT STATE")
    print("=" * 70)
    audit_vault()

    print("\n" + "=" * 70)
    print("INDEPENDENT AUDIT 2: ISOLATING WORKER M1 DELIVERABLES (EXCLUDING TEST_*.md ROOT ARTIFACTS)")
    print("=" * 70)
    audit_vault(exclude_files={"TEST_INFRA.md", "TEST_READY.md"})
