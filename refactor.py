import os
import re

start_here_path = "01 - Curriculum/00 - Start Here.md"
with open(start_here_path, "r") as f:
    sh = f.read()

# Extract sequence from 00 - Start Here.md
sequence = []
for line in sh.splitlines():
    match = re.search(r'^\s*-\s*\[\[([^\]\|]+)\]\]', line)
    if match:
        course = match.group(1).strip()
        sequence.append(course)

print(f"Found {len(sequence)} courses in sequence.")

# Map course names to file paths
course_to_path = {}
for root, dirs, files in os.walk("01 - Curriculum"):
    for file in files:
        if file.endswith(".md"):
            name = file[:-3]
            course_to_path[name] = os.path.join(root, file)

for i, course in enumerate(sequence):
    if course not in course_to_path:
        print(f"Warning: {course} not found.")
        continue
    filepath = course_to_path[course]
    with open(filepath, "r") as f:
        content = f.read()

    block_id_val = f"Block {i+1}"
    
    # 1. Replace block_id in frontmatter
    # Handles both quoted and unquoted block_id values safely
    content = re.sub(r'(?m)^block_id:\s*".*?"\s*$', f'block_id: "{block_id_val}"', content)
    content = re.sub(r'(?m)^block_id:\s*(?!").*?\s*$', f'block_id: "{block_id_val}"', content)

    # If block_id is completely missing, inject it right after ---
    if 'block_id:' not in content:
        content = re.sub(r'^---\n', f'---\nblock_id: "{block_id_val}"\n', content)
    
    # 2. Replace Block number in the main H1 header
    # e.g., # Block 13 — Introduction to Algorithms -> # Block X — Introduction to Algorithms
    content = re.sub(r'(?m)^# (Block \w+|Block TBD) — ', f'# {block_id_val} — ', content)

    # 3. Next Steps link generation
    prev_c = sequence[i-1] if i > 0 else "Tooling"
    next_c = sequence[i+1] if i < len(sequence)-1 else "Dashboard"
    
    seq_flow = f"- **Sequential Flow:** "
    if i > 0:
        seq_flow += f"[[{prev_c}|← {prev_c}]] | "
    else:
        seq_flow += f"[[00 - Dashboard|← Dashboard]] | "
        
    seq_flow += "[[00 - Dashboard|Dashboard]] | "
    
    if i < len(sequence)-1:
        seq_flow += f"[[{next_c}|{next_c} →]]"
    else:
        seq_flow += f"[[00 - Dashboard|Dashboard →]]"

    # Replace the exact Sequential Flow line
    if "- **Sequential Flow:**" in content:
        content = re.sub(r'(?m)^-\s*\*\*Sequential Flow:\*\*.*$', seq_flow, content)
    else:
        # Fallback if Sequential flow doesn't exist but Next Steps does
        if "## ➡️ Next Steps" in content:
            content += f"\n{seq_flow}\n"
        else:
            # Complete missing Next Steps
            ns_text = f"\n## ➡️ Next Steps\n- **Topic Hub:** [[Topic Index|Topic Index]] | [[Checklist|Master Checklist]]\n{seq_flow}\n"
            content += ns_text

    with open(filepath, "w") as f:
        f.write(content)

print("Refactoring complete.")
