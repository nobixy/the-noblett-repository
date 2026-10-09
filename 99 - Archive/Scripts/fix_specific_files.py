import os
import re

curriculum_dir = "/home/noblixy/The Noblett Repository/01 - Curriculum"

updates = {
    "Reading, Thinking, and Writing.md": {
        "category": "support",
        "prereqs": []
    },
    "Calculus I.md": {
        "category": "core",
        "prereqs": ["Math Prerequisites"]
    },
    "Math for CS.md": {
        "category": "core",
        "prereqs": ["Calculus I"]
    },
    "Linear Algebra.md": {
        "category": "core",
        "prereqs": ["Calculus I"]
    },
    "Algorithms I.md": {
        "category": "core",
        "prereqs": ["Math for CS", "CS61A"]
    },
    "CS61A.md": {
        "category": "core",
        "prereqs": ["Programming On-Ramp"]
    }
}

def update_file(filename, data):
    # Find the file
    filepath = None
    for root, _, files in os.walk(curriculum_dir):
        if filename in files:
            filepath = os.path.join(root, filename)
            break
            
    if not filepath:
        print(f"File {filename} not found.")
        return

    with open(filepath, 'r') as f:
        content = f.read()
        
    # Update Frontmatter
    if 'category:' not in content:
        content = re.sub(r'(title: ".*?")', r'\1\ncategory: "' + data["category"] + '"', content, count=1)
    if 'prerequisites:' not in content:
        prereqs_yaml = "prerequisites:\n" + "".join([f"  - \"{p}\"\n" for p in data["prereqs"]])
        if not data["prereqs"]:
            prereqs_yaml = "prerequisites: []\n"
        content = re.sub(r'(status: .*?)', r'\1\n' + prereqs_yaml.rstrip(), content, count=1)
        
    # Update Body (Add Prerequisites header if missing)
    if "## 🔗 Prerequisites" not in content:
        why_matters_match = re.search(r'(## 🎯 Why This Block Matters.*?\n)(?=## |---)', content, re.DOTALL)
        if why_matters_match:
            why_text = why_matters_match.group(1)
            prereq_text = "\n## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n"
            if data["prereqs"]:
                for p in data["prereqs"]:
                    prereq_text += f"- [[{p}]]\n"
            else:
                prereq_text += "- None.\n"
            content = content.replace(why_text, why_text + prereq_text)
            
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated {filename}")

for filename, data in updates.items():
    update_file(filename, data)
