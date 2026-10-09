import os
import re

curriculum_dir = "01 - Curriculum"
start_here_path = os.path.join(curriculum_dir, "00 - Start Here.md")

with open(start_here_path, "r") as f:
    start_here_content = f.read()

# Find all links like [[File Name]] or [[File Name|Alias]]
links = re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', start_here_content)

linked_files = set(link.strip() + ".md" for link in links)

all_md_files = set()
for root, dirs, files in os.walk(curriculum_dir):
    for file in files:
        if file.endswith(".md"):
            all_md_files.add(file)

start_here_itself = {"00 - Start Here.md"}

orphans = all_md_files - linked_files - start_here_itself
print("Orphaned files:")
for o in sorted(orphans):
    print(o)

