import os
import re
import glob

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
    
    # Determine category
    category = "core"
    if "Advanced/" in filepath:
        category = "advanced"
    elif "Optional/" in filepath:
        category = "optional"
        
    if "category:" not in yaml_content:
        # Insert category after title or block_id
        yaml_content = re.sub(r'(title: ".*?")', r'\1\ncategory: "' + category + '"', yaml_content)

    # Extract previous block from navigation if it exists
    prev_block = None
    nav_match = re.search(r'## 🧭 Navigation.*?Sequential Flow: \[\[(.*?)\|←.*?\]\]', content, re.DOTALL)
    if not nav_match:
        nav_match = re.search(r'## ➡️ Next Steps.*?Sequential Flow: \[\[(.*?)\|←.*?\]\]', content, re.DOTALL)
    
    if nav_match:
        prev_block = nav_match.group(1).strip()
    
    if "prerequisites:" not in yaml_content:
        # Insert prerequisites after status or category
        prereq_str = "prerequisites:\n  - \"" + prev_block + "\"" if prev_block else "prerequisites: []"
        
        if "status:" in yaml_content:
            yaml_content = re.sub(r'(status: .*?)\n', r'\1\n' + prereq_str + '\n', yaml_content)
        else:
            yaml_content += "\n" + prereq_str
            
    # Reconstruct YAML
    new_content = "---\n" + yaml_content + "\n---" + content[yaml_match.end():]
    
    # Map headers
    new_content = new_content.replace("## 🏁 Done When", "## 🏁 Mastery Criteria & Assessments")
    new_content = new_content.replace("## 🧭 Navigation", "## ➡️ Next Steps")
    
    # Ensure Prerequisites header in body
    if "## 🔗 Prerequisites" not in new_content:
        prereq_body = "## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n"
        if prev_block:
            prereq_body += f"- [[{prev_block}]]\n\n"
        else:
            prereq_body += "\n"
        
        # Insert before ## 📖 Primary Syllabus or ## 📖 Core Resources
        if "## 📖 Primary Syllabus" in new_content:
            new_content = new_content.replace("## 📖 Primary Syllabus", prereq_body + "## 📖 Primary Syllabus")
        elif "## 📖 Core Resources" in new_content:
            new_content = new_content.replace("## 📖 Core Resources", prereq_body + "## 📖 Core Resources")
        else:
            # Fallback: after Why This Block Matters
            if "## 🎯 Why This Block Matters" in new_content:
                # Find end of Why section (next ##)
                match = re.search(r'## 🎯 Why This Block Matters.*?(\n## )', new_content, re.DOTALL)
                if match:
                    new_content = new_content.replace(match.group(1), "\n\n" + prereq_body + match.group(1))
                    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {filename}")

curriculum_dir = "/home/noblixy/The Noblett Repository/01 - Curriculum"
for root, _, files in os.walk(curriculum_dir):
    for f in files:
        if f.endswith(".md"):
            process_file(os.path.join(root, f))
