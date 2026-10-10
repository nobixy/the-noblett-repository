#!/usr/bin/env python3
"""Read-only consistency check for the curriculum (see DR-002, DR-003, DR-005).

Run from anywhere: python3 verify_curriculum.py   (folder layout: DR-007)
Exit code 0 = clean, 1 = problems found. Never writes files.
Checks block notes (any note in 01 - Curriculum with a block_id):
  schema keys, category values, block_id format/uniqueness, title matches block_id,
  prerequisites resolve and match the body's Prerequisites section, standard headings,
  exactly one Sequential Flow line whose links resolve and whose prev/next pairs agree,
  stage folder and file-name prefix match block_id, subject set, job_ready in 1-5,
  every non-track block is linked from The Path in 00 - Start Here.
Vault-wide: every wikilink resolves to a note or file.
"""
import os, re, sys
try:
    import yaml
except ImportError:
    sys.exit("needs PyYAML: pip install pyyaml (or pacman -S python-yaml)")

ROOT = os.path.dirname(os.path.abspath(__file__))
CURR = os.path.join(ROOT, "01 - Curriculum")
SKIP_DIRS = {".obsidian", ".git", ".trash", "node_modules"}
REQUIRED = ["block_id", "title", "category", "term", "status", "prerequisites", "hours_estimate",
            "hours_actual", "primary_resource", "milestone", "date_started", "date_completed", "tier", "subject"]
CATEGORIES = {"core", "elective", "specialization"}
ID_RE = re.compile(r"^(B0|BM|BW|P[1-5]|Block \d+[a-z]?|E\d+|Track \d+)$")  # 8b, 15b etc. since DR-005
HEADINGS = ["## 🔗 Prerequisites", "## 🏁 Mastery Criteria & Assessments", "## ➡️ Next Steps"]
HUB = "00 - Start Here"

def stage_of(bid):
    """Stage folder under 01 - Curriculum for a block_id (DR-003)."""
    if bid in ("B0", "BM", "BW"): return "00 - Phase -1 Bedrock"
    if bid.startswith("P"): return "01 - Phase 0 Prerequisites"
    if bid.startswith("E"): return "07 - Optional Electives"
    if bid.startswith("Track"): return "08 - Specialization Tracks"
    n = int(re.findall(r"\d+", bid)[0])
    return ["02 - Year 1", "03 - Year 2", "04 - Year 3", "05 - Year 4", "06 - Year 5"][
        0 if n <= 8 else 1 if n <= 15 else 2 if n <= 22 else 3 if n <= 29 else 4]

def prefix(bid):
    m = re.match(r"Block (\d+)([a-z]?)$", bid)
    if m: return f"B{int(m.group(1)):02d}{m.group(2)}"
    m = re.match(r"Track (\d+)$", bid)
    if m: return f"T{int(m.group(1)):02d}"
    return bid

LINK_RE = re.compile(r"\[\[([^\]|#\\]*)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]")

problems = []
def bad(where, msg): problems.append(f"{where}: {msg}")

notes, files = {}, set()
for d, ds, fs in os.walk(ROOT):
    ds[:] = [x for x in ds if x not in SKIP_DIRS]
    for f in fs:
        files.add(f.lower())
        if f.endswith(".md"): notes[f[:-3]] = os.path.join(d, f)
lower = {k.lower() for k in notes}

def split(text):
    if not text.startswith("---\n"): return {}, text
    end = text.find("\n---\n", 4)
    if end < 0: return {}, text
    try: return (yaml.safe_load(text[4:end]) or {}), text[end + 5:]
    except yaml.YAMLError as e: return {"__error__": str(e)}, text[end + 5:]

def strip_code(t): return re.sub(r"```.*?```", "", t, flags=re.S)

# vault-wide links
for name, path in notes.items():
    rel = os.path.relpath(path, ROOT)
    if rel.startswith("04 - System"): continue
    for tgt in LINK_RE.findall(strip_code(open(path, encoding="utf-8").read())):
        base = tgt.strip().split("/")[-1]
        if base and base.lower() not in lower and base.lower() not in files:
            bad(rel, f"broken link [[{tgt}]]")

blocks, flows = {}, {}
for name, path in notes.items():
    if not path.startswith(CURR): continue
    rel = os.path.relpath(path, ROOT)
    text = open(path, encoding="utf-8").read()
    fm, body = split(text)
    if "__error__" in fm: bad(rel, "frontmatter does not parse: " + fm["__error__"]); continue
    if "block_id" not in fm: continue  # hubs and milestones
    for k in REQUIRED:
        if k not in fm: bad(rel, f"missing frontmatter key '{k}'")
    bid = str(fm.get("block_id", ""))
    if not ID_RE.match(bid): bad(rel, f"bad block_id '{bid}'")
    if bid in blocks: bad(rel, f"duplicate block_id '{bid}' (also {blocks[bid]})")
    blocks[bid] = name
    if fm.get("category") not in CATEGORIES: bad(rel, f"category '{fm.get('category')}' not in {sorted(CATEGORIES)}")
    if bid.startswith("Track") and fm.get("track_id") != bid: bad(rel, "track_id must equal block_id")
    if ID_RE.match(bid):
        if not name.startswith(prefix(bid) + " - "): bad(rel, f"file name should start '{prefix(bid)} - '")
    if not fm.get("subject"): bad(rel, "subject is empty")
    if "job_ready" in fm and fm["job_ready"] not in (1, 2, 3, 4, 5): bad(rel, "job_ready must be 1-5")
    h1 = next((l for l in body.splitlines() if l.startswith("# ")), "")
    if not h1.startswith(f"# {bid} — "): bad(rel, f"title '{h1[:50]}' should start '# {bid} — '")
    pre = fm.get("prerequisites") or []
    for p in pre:
        if p not in notes: bad(rel, f"prerequisite '{p}' is not a note name")
    m = re.search(r"## 🔗 Prerequisites\n(.*?)(?=\n## |\n---)", body, re.S)
    body_pre = re.findall(r"^- \[\[([^\]|#]+)", m.group(1), re.M) if m else []
    if set(body_pre) != set(pre): bad(rel, f"prerequisites differ: yaml {pre} vs body {body_pre}")
    for h in HEADINGS:
        if h not in body: bad(rel, f"missing heading '{h}'")
    fl = re.findall(r"^- \*\*Sequential Flow:\*\*(.*)$", body, re.M)
    if len(fl) != 1: bad(rel, f"{len(fl)} Sequential Flow lines (want 1)"); continue
    links = re.findall(r"\[\[([^\]|]+)\|([←→]?)[^\]]*?([→]?)\]\]", fl[0])
    prev = next((t for t, a, _ in links if a == "←"), None)
    nxt = next((t for t, _, b in links if b == "→"), None)
    flows[name] = (prev, nxt)

# chain consistency: if A says next is B (a block note), B must say prev is A
for a, (_, nxt) in flows.items():
    if nxt in flows and flows[nxt][0] != a:
        bad(a, f"Sequential Flow says next is '{nxt}', but '{nxt}' says previous is '{flows[nxt][0]}'")

# The Path in the hub must list every non-track block note
if HUB not in notes: bad(HUB, "hub note missing")
else:
    hubtext = open(notes[HUB], encoding="utf-8").read()
    m = re.search(r"\n## The Path\n(.*?)(?=\n## (?!#))", hubtext, re.S)
    if not m: bad(HUB, "no '## The Path' section")
    else:
        listed = {t.strip() for t in LINK_RE.findall(m.group(1))}
        for bid, name in blocks.items():
            if not bid.startswith("Track") and name not in listed: bad(HUB, f"The Path does not link {bid} ({name})")

planned = 0
for name, path in notes.items():
    if path.startswith(CURR):
        fm, _ = split(open(path, encoding="utf-8").read())
        if fm.get("block_id") and fm.get("optional") is not True: planned += int(fm.get("hours_estimate") or 0)

print(f"Block notes checked: {len(blocks)}   Planned hours (Start Here progress query): {planned}")
if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems: print("  -", p)
    sys.exit(1)
print("All checks passed.")
