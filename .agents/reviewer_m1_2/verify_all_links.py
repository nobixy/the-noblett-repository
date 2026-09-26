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

def res(t):
    clean = t.split("#")[0].strip()
    if not clean:
        return True
    if clean.endswith("\\"):
        return False
    if clean in all_files or (clean + ".md") in all_files:
        return True
    tl = clean.lower()
    if tl in stems or tl in names:
        return True
    if (tl + ".md") in stems or (tl + ".md") in names:
        return True
    for f in all_files:
        if f.lower().endswith("/" + tl) or f.lower().endswith("/" + tl + ".md"):
            return True
    return False

wl_re = re.compile(r"\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]")

total_links = 0
broken = []
for f in sorted(all_files):
    if not f.endswith(".md"):
        continue
    text = (VAULT_ROOT / f).read_text(encoding="utf-8")
    # Strip fenced code
    text_clean = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for line_no, line in enumerate(text_clean.splitlines(), 1):
        # Strip inline code
        line_clean = re.sub(r"`[^`]*`", "", line)
        for m in wl_re.finditer(line_clean):
            target = m.group(1).strip()
            total_links += 1
            if not res(target):
                broken.append((f, line_no, target))

print(f"Total active wikilinks checked: {total_links}")
print(f"Total broken active wikilinks: {len(broken)}")
for b in broken:
    print(f"  BROKEN: {b[0]}:{b[1]} -> [[{b[2]}]]")
