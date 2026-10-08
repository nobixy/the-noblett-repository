import os
import yaml
import glob
import re

curriculum_dir = "/home/noblixy/The Noblett Repository/01 - Curriculum"
files = glob.glob(os.path.join(curriculum_dir, "**", "*.md"), recursive=True)

missing_category = []
missing_prereqs_yaml = []
missing_prereqs_header = []
missing_mastery_header = []
missing_next_steps = []

def parse_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]), parts[2]
            except Exception as e:
                return None, content
    return None, content

for f in files:
    if os.path.basename(f) in ["00 - Start Here.md", "Specializations Hub.md"]:
        continue
    with open(f, 'r') as fp:
        content = fp.read()
    
    fm, body = parse_frontmatter(content)
    if not fm:
        fm = {}
    
    if "category" not in fm:
        missing_category.append(f)
    if "prerequisites" not in fm:
        missing_prereqs_yaml.append(f)
        
    if "## 🔗 Prerequisites" not in body:
        missing_prereqs_header.append(f)
    if "## 🏁 Mastery Criteria & Assessments" not in body:
        missing_mastery_header.append(f)
    if "## ➡️ Next Steps" not in body:
        missing_next_steps.append(f)

print("Missing category:", len(missing_category))
if missing_category: print(missing_category)
print("Missing prerequisites YAML:", len(missing_prereqs_yaml))
if missing_prereqs_yaml: print(missing_prereqs_yaml)
print("Missing prerequisites Header:", len(missing_prereqs_header))
if missing_prereqs_header: print(missing_prereqs_header)
print("Missing mastery Header:", len(missing_mastery_header))
if missing_mastery_header: print(missing_mastery_header)
print("Missing next steps Header:", len(missing_next_steps))
if missing_next_steps: print(missing_next_steps)
