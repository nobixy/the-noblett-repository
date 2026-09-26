#!/usr/bin/env python3
"""
M1 Milestone Programmatic Verification Script:
1. Zero dead wikilinks across vault (with code-span awareness).
2. Zero orphaned notes (every non-template note has >=1 incoming link).
3. 100% reachability of non-template notes from 00 - Dashboard.md.
"""

import os
import re
from collections import defaultdict, deque

VAULT_ROOT = "/home/noblixy/The Noblett Repository"

def get_vault_files():
    all_files = []
    md_files = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in sorted(dirs) if not d.startswith('.')]
        for f in sorted(files):
            rel_path = os.path.relpath(os.path.join(root, f), VAULT_ROOT)
            all_files.append(rel_path)
            if f.endswith('.md'):
                md_files.append(rel_path)
    return all_files, md_files

def resolve_target(target, relpath_set, relpath_lower_map, no_ext_map, basename_map, src_rel):
    t = target.strip()
    if not t:
        return src_rel
    
    # 1. Exact relative path
    if t in relpath_set:
        return t
    if (t + '.md') in relpath_set:
        return t + '.md'
    
    # 2. Relative to src_rel
    rel_to_cur = os.path.normpath(os.path.join(os.path.dirname(src_rel), t))
    if rel_to_cur in relpath_set:
        return rel_to_cur
    if (rel_to_cur + '.md') in relpath_set:
        return rel_to_cur + '.md'
    
    # 3. Basename without ext
    if t in no_ext_map:
        return no_ext_map[t][0]
    if t in basename_map:
        return basename_map[t][0]
    
    # 4. Case-insensitive
    t_low = t.lower()
    if t_low in relpath_lower_map:
        return relpath_lower_map[t_low]
    if (t_low + '.md') in relpath_lower_map:
        return relpath_lower_map[t_low + '.md']
    for k, v in no_ext_map.items():
        if k.lower() == t_low:
            return v[0]
            
    return None

def main():
    all_files, md_files = get_vault_files()
    relpath_set = set(all_files)
    relpath_lower_map = {p.lower(): p for p in all_files}
    no_ext_map = defaultdict(list)
    basename_map = defaultdict(list)
    for p in all_files:
        bn = os.path.basename(p)
        basename_map[bn].append(p)
        ne = os.path.splitext(bn)[0]
        no_ext_map[ne].append(p)
        
    # Extract links excluding code spans
    # Regex to strip inline code `...` and fenced code ```...```
    wikilink_regex = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|([^\]]+))?\]\]')
    
    outgoing_links = defaultdict(set)
    incoming_links = defaultdict(set)
    broken_links = []
    total_active_wikilinks = 0
    
    for src in md_files:
        full_src = os.path.join(VAULT_ROOT, src)
        with open(full_src, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Strip fenced code blocks
        clean_content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        
        # Process line by line, stripping inline code spans
        for line_no, line in enumerate(clean_content.splitlines(), 1):
            # In markdown, `[[link]]` inside backticks is code, not a wikilink
            # Strip backticked code
            line_no_code = re.sub(r'`[^`]*`', '', line)
            
            for m in wikilink_regex.finditer(line_no_code):
                target = m.group(1).strip()
                alias = m.group(2)
                total_active_wikilinks += 1
                
                resolved = resolve_target(target, relpath_set, relpath_lower_map, no_ext_map, basename_map, src)
                if resolved:
                    if resolved.endswith('.md'):
                        outgoing_links[src].add(resolved)
                        incoming_links[resolved].add(src)
                else:
                    broken_links.append((src, line_no, target))
                    
    print(f"Total markdown files: {len(md_files)}")
    print(f"Total active wikilinks (outside code spans): {total_active_wikilinks}")
    print(f"Broken wikilinks: {len(broken_links)}")
    for b in broken_links:
        print(f"  FAILED: {b[0]}:{b[1]} -> [[{b[2]}]]")
        
    # Check non-template orphans
    non_template_md = [m for m in md_files if not m.startswith("08 - Templates")]
    template_md = [m for m in md_files if m.startswith("08 - Templates")]
    
    orphans = [m for m in md_files if len(incoming_links[m]) == 0]
    non_template_orphans = [m for m in non_template_md if len(incoming_links[m]) == 0]
    
    print(f"\nTotal notes with in-degree 0: {len(orphans)}")
    print(f"Non-template orphans (in-degree 0): {len(non_template_orphans)}")
    for o in non_template_orphans:
        print(f"  ORPHAN: {o}")
        
    print(f"\nTemplate notes in-degree count:")
    for t in template_md:
        print(f"  {t} <- incoming links: {len(incoming_links[t])} (from {list(incoming_links[t])})")
        
    # Check reachability from 00 - Dashboard.md
    start_node = "00 - Dashboard.md"
    visited = set()
    queue = deque([start_node])
    if start_node in relpath_set:
        visited.add(start_node)
        
    while queue:
        curr = queue.popleft()
        for neighbor in outgoing_links[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    unreachable_non_template = [m for m in non_template_md if m not in visited]
    unreachable_all = [m for m in md_files if m not in visited]
    
    reachability_pct = (len(visited.intersection(set(non_template_md))) / len(non_template_md)) * 100.0
    print(f"\n--- REACHABILITY FROM 00 - Dashboard.md ---")
    print(f"Reachable non-template notes: {len(visited.intersection(set(non_template_md)))} / {len(non_template_md)} ({reachability_pct:.2f}%)")
    print(f"Unreachable non-template notes: {len(unreachable_non_template)}")
    for u in unreachable_non_template:
        print(f"  UNREACHABLE: {u}")
        
    print(f"\nAll reachable vault notes (including templates): {len(visited)} / {len(md_files)}")
    if unreachable_all:
        print(f"Unreachable notes overall: {unreachable_all}")

if __name__ == "__main__":
    main()
