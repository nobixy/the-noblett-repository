import os
import re

def process_file(filepath):
    # Exclude hubs and indices
    filename = os.path.basename(filepath)
    if filename == "00 - Start Here.md" or filename.endswith("Hub.md") or filename.endswith("Index.md"):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        return
        
    yaml_content = yaml_match.group(1)
    
    # Check if we failed to extract prerequisites in the first pass
    # It might be in ## ➡️ Next Steps or ## 🧭 Navigation
    prev_block = None
    # We account for Optional spaces and ** around Sequential Flow
    nav_match = re.search(r'(?:## 🧭 Navigation|## ➡️ Next Steps).*?Sequential Flow:?\*?\*? \[\[(.*?)\|←.*?\]\]', content, re.DOTALL)
    
    if nav_match:
        prev_block = nav_match.group(1).strip()
    else:
        # sometimes it doesn't have the ← arrow but just [[Block Name]] as the first item before Dashboard?
        pass

    made_changes = False

    if prev_block:
        # If it has prerequisites: [] or prerequisites:\n  - "Something" where it should have the prev_block, update it
        # Actually, let's just make sure prerequisites contains it.
        # But wait, Calculus I already had it from the previous turn! Let's check if it's already there
        if "prerequisites:" in yaml_content and "[]" in yaml_content:
            yaml_content = yaml_content.replace("prerequisites: []", f'prerequisites:\n  - "{prev_block}"')
            made_changes = True

    # Also, we might have inserted `## 🔗 Prerequisites` with no block under it, but now we can add it.
    new_content = "---\n" + yaml_content + "\n---" + content[yaml_match.end():]
    
    if prev_block and "## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n\n" in new_content:
        new_content = new_content.replace(
            "## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n\n",
            f"## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n- [[{prev_block}]]\n\n"
        )
        made_changes = True

    if made_changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

curriculum_dir = "/home/noblixy/The Noblett Repository/01 - Curriculum"
for root, _, files in os.walk(curriculum_dir):
    for f in files:
        if f.endswith(".md"):
            process_file(os.path.join(root, f))
