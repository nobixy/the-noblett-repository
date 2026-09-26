#!/usr/bin/env python3
import os
import re
from pathlib import Path
from collections import defaultdict, deque

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository")
exclude = {"TEST_INFRA.md", "TEST_READY.md"}

all_files = set()
md_files = []
for r, d, fs in os.walk(VAULT_ROOT):
    parts = Path(r).relative_to(VAULT_ROOT).parts
    if any(p.startswith(".") for p in parts):
        continue
    for f in fs:
        rel = str((Path(r) / f).relative_to(VAULT_ROOT))
        if rel not in exclude:
            all_files.add(rel)
            if f.endswith(".md"):
                md_files.append(rel)

stems = defaultdict(list)
names = defaultdict(list)
for f in all_files:
    p = Path(f)
    stems[p.stem.lower()].append(f)
    names[p.name.lower()].append(f)

def res(t):
    clean = t.split("#")[0].strip()
    if not clean:
        return None
    if clean.endswith("\\"):
        return None
    if clean in all_files:
        return clean
    if (clean + ".md") in all_files:
        return clean + ".md"
    tl = clean.lower()
    if tl in stems:
        return stems[tl][0]
    if tl in names:
        return names[tl][0]
    for f in all_files:
        if f.lower().endswith("/" + tl) or f.lower().endswith("/" + tl + ".md"):
            return f
    return None

wl_re = re.compile(r"\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]")

adj = defaultdict(set)
in_degree = defaultdict(int)

for f in sorted(md_files):
    text = (VAULT_ROOT / f).read_text(encoding="utf-8")
    text_clean = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for line in text_clean.splitlines():
        line_clean = re.sub(r"`[^`]*`", "", line)
        for m in wl_re.finditer(line_clean):
            target = m.group(1).strip()
            resolved = res(target)
            if resolved and resolved in md_files and resolved != f:
                adj[f].add(resolved)

for src, tgts in adj.items():
    for t in tgts:
        in_degree[t] += 1

non_templates = [f for f in md_files if not f.startswith("08 - Templates/")]
templates = [f for f in md_files if f.startswith("08 - Templates/")]

print(f"Total MD files: {len(md_files)}")
print(f"Non-template MD files: {len(non_templates)}")
print(f"Template MD files: {len(templates)}")

orphans_all = [f for f in md_files if in_degree[f] == 0]
orphans_non_template = [f for f in non_templates if in_degree[f] == 0 and f != "00 - Dashboard.md"]

print(f"\nAll notes with in-degree 0 ({len(orphans_all)}):")
for o in sorted(orphans_all):
    is_tmpl = o.startswith("08 - Templates/")
    print(f"  {'[TEMPLATE]' if is_tmpl else '[NON-TEMPLATE ERROR]'} {o}")

print(f"\nNon-template orphans (excluding 00 - Dashboard.md): {len(orphans_non_template)}")

# Reachability and shortest path distances from 00 - Dashboard.md
start = "00 - Dashboard.md"
dist = {start: 0}
parent = {start: None}
queue = deque([start])

while queue:
    curr = queue.popleft()
    for neighbor in sorted(adj[curr]):
        if neighbor not in dist:
            dist[neighbor] = dist[curr] + 1
            parent[neighbor] = curr
            queue.append(neighbor)

unreachable_non_template = [f for f in non_templates if f not in dist]
print(f"\nUnreachable non-template notes from 00 - Dashboard.md: {len(unreachable_non_template)}")
for u in unreachable_non_template:
    print(f"  UNREACHABLE: {u}")

print(f"Reachability percentage: {len(dist.keys() & set(non_templates))} / {len(non_templates)} ({(len(dist.keys() & set(non_templates))/len(non_templates))*100:.2f}%)")

# Distance distribution
dist_counts = defaultdict(int)
for f in non_templates:
    if f in dist:
        dist_counts[dist[f]] += 1
print("\nHop distance distribution for non-template notes:")
for d in sorted(dist_counts):
    print(f"  {d} hops: {dist_counts[d]} notes")
