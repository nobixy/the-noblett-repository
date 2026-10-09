import os
import glob
import re

tracks_dir = "01 - Curriculum/Advanced/Specializations"
track_files = glob.glob(os.path.join(tracks_dir, "Track*.md"))
track_files.append(os.path.join(tracks_dir, "Intensive Cryptopals or TLA+.md"))

for path in track_files:
    if not os.path.exists(path):
        continue
    
    with open(path, "r") as f:
        content = f.read()

    # Find prerequisites in the > - **Prerequisites:** line
    prereq_match = re.search(r"> -\s*\*\*Prerequisites:\*\*\s*(.*)", content)
    prereqs = []
    if prereq_match:
        # Extract [[Course]] elements
        raw_prereqs = prereq_match.group(1)
        prereqs = re.findall(r"\[\[(.*?)\]\]", raw_prereqs)
    
    # Extract YAML frontmatter
    yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not yaml_match:
        continue
        
    yaml_content = yaml_match.group(1)
    
    # Update prerequisites array in YAML
    if prereqs:
        prereq_str = "prerequisites:\n" + "\n".join([f'  - "{p}"' for p in prereqs])
        yaml_content = re.sub(r"prerequisites:.*?(?=\n[a-z_]+:|\Z)", prereq_str, yaml_content, flags=re.DOTALL)
    
    # Add hours_estimate and hours_actual if missing
    if "hours_estimate" not in yaml_content:
        yaml_content += "\nhours_estimate: 400"
    if "hours_actual" not in yaml_content:
        yaml_content += "\nhours_actual: 0"
        
    new_content = content[:yaml_match.start()] + "---\n" + yaml_content + "\n---" + content[yaml_match.end():]
    
    # Fix the markdown Prerequisites section
    if prereqs:
        md_prereqs = "\n".join([f"- [[{p}]]" for p in prereqs])
        new_content = re.sub(
            r"## 🔗 Prerequisites\n\*What must you have mastered before starting this block\?\*\n(?:- \*None\. This is a foundational block\.\*|- \[\[.*?\]\]\n?|)*",
            f"## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n{md_prereqs}\n\n",
            new_content
        )
    
    with open(path, "w") as f:
        f.write(new_content)

print("Track metadata updated successfully.")
