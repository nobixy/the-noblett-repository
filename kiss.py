import os, re, shutil, json

def read_file(p):
    with open(p, 'r') as f: return f.read()

def write_file(p, c):
    with open(p, 'w') as f: f.write(c)

def stage_of(bid):
    if bid in ("B0", "BM", "BW"): return "00 - Phase -1 Bedrock"
    if bid.startswith("P"): return "01 - Phase 0 Prerequisites"
    if bid.startswith("E"): return "07 - Optional Electives"
    if bid.startswith("Track"): return "08 - Specialization Tracks"
    n = int(re.findall(r"\d+", bid)[0])
    return ["02 - Year 1", "03 - Year 2", "04 - Year 3", "05 - Year 4", "06 - Year 5"][
        0 if n <= 8 else 1 if n <= 15 else 2 if n <= 22 else 3 if n <= 29 else 4]

curr_dir = "01 - Curriculum"
for root, dirs, files in os.walk(curr_dir):
    for f in files:
        if not f.endswith(".md"): continue
        path = os.path.join(root, f)
        text = read_file(path)
        if "block_id:" in text:
            # It's a block note
            bid_match = re.search(r'block_id:\s*"?([^"\n]+)"?', text)
            if bid_match:
                bid = bid_match.group(1)
                stage = stage_of(bid)
                # insert stage: "..." into frontmatter
                if "stage:" not in text:
                    text = re.sub(r'(block_id:.*?)\n', r'\1\nstage: "' + stage + r'"\n', text, count=1)
                
                new_path = os.path.join(curr_dir, f)
                if path != new_path:
                    write_file(path, text)
                    os.rename(path, new_path)

