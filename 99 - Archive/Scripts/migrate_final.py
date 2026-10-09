import os
import re

def process_file(filepath):
    # Exclude hubs and indices
    filename = os.path.basename(filepath)
    if filename == "00 - Start Here.md" or filename.endswith("Hub.md") or filename.endswith("Index.md"):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    made_changes = False
    
    # 1. Add ## 🔗 Prerequisites if missing
    if "## 🔗 Prerequisites" not in content:
        made_changes = True
        prereq_body = "## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n\n"
        
        # Try finding a place to insert
        if "## 📚 Core Courses" in content:
            content = content.replace("## 📚 Core Courses", prereq_body + "## 📚 Core Courses")
        elif "## 📖 Primary Resources & Texts" in content:
            content = content.replace("## 📖 Primary Resources & Texts", prereq_body + "## 📖 Primary Resources & Texts")
        elif "## 🎯 Why This Track Matters" in content:
            match = re.search(r'## 🎯 Why This Track Matters.*?(\n## )', content, re.DOTALL)
            if match:
                content = content.replace(match.group(1), "\n\n" + prereq_body + match.group(1))
            else:
                # Append after YAML
                content = re.sub(r'(^---\n.*?\n---\n+)', r'\1' + prereq_body, content, flags=re.DOTALL)
        else:
            # Append after YAML
            content = re.sub(r'(^---\n.*?\n---\n+)', r'\1' + prereq_body, content, flags=re.DOTALL)

    # 2. Add ## 🏁 Mastery Criteria & Assessments if missing
    if "## 🏁 Mastery Criteria" not in content:
        made_changes = True
        mastery_body = "## 🏁 Mastery Criteria & Assessments\n> [!IMPORTANT]\n> Assessment criteria go here.\n\n"
        
        if "## 📝 Study Notes, Psets & Proofs" in content:
            content = content.replace("## 📝 Study Notes, Psets & Proofs", mastery_body + "## 📝 Study Notes, Psets & Proofs")
        elif "## ➡️ Next Steps" in content:
            content = content.replace("## ➡️ Next Steps", mastery_body + "## ➡️ Next Steps")
        else:
            content += "\n" + mastery_body

    if made_changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")

curriculum_dir = "/home/noblixy/The Noblett Repository/01 - Curriculum"
for root, _, files in os.walk(curriculum_dir):
    for f in files:
        if f.endswith(".md"):
            process_file(os.path.join(root, f))
