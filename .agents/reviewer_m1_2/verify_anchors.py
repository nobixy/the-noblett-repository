#!/usr/bin/env python3
import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/home/noblixy/The Noblett Repository")
exclude = {"TEST_INFRA.md", "TEST_READY.md"}

all_files = set()
for r, d, fs in os.walk(VAULT_ROOT):
    parts = Path(r).relative_to(VAULT_ROOT).parts
    if any(p.startswith(".") for p in parts):
        continue
    for f in fs:
        rel = str((Path(r) / f).relative_to(VAULT_ROOT))
        if rel not in exclude:
            all_files.add(rel)

stems = defaultdict(list)
names = defaultdict(list)
for f in all_files:
    p = Path(f)
    stems[p.stem.lower()].append(f)
    names[p.name.lower()].append(f)

def resolve_file(t):
    clean = t.strip()
    if clean in all_files or (clean + ".md") in all_files:
        return clean if clean.endswith(".md") else (clean + ".md")
    tl = clean.lower()
    if tl in stems:
        return stems[tl][0]
    if tl in names:
        return names[tl][0]
    for f in all_files:
        if f.lower().endswith("/" + tl) or f.lower().endswith("/" + tl + ".md"):
            return f
    return None

anchor_re = re.compile(r"\[\[([^\]\|#]*)(?:#([^\]\|]+))(?:\|[^\]]+)?\]\]")

anchor_links = []
for f in sorted(all_files):
    if not f.endswith(".md"):
        continue
    text = (VAULT_ROOT / f).read_text(encoding="utf-8")
    clean = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for line_no, line in enumerate(clean.splitlines(), 1):
        line_no_inline = re.sub(r"`[^`]*`", "", line)
        for m in anchor_re.finditer(line_no_inline):
            file_part = m.group(1).strip()
            anchor_part = m.group(2).strip()
            anchor_links.append((f, line_no, file_part, anchor_part, m.group(0)))

print(f"Total wikilinks with heading anchors: {len(anchor_links)}")
for a in anchor_links:
    target_file = resolve_file(a[2]) if a[2] else a[0]
    print(f"  {a[0]}:{a[1]} -> target: {target_file} # {a[3]} (raw: {a[4]})")
