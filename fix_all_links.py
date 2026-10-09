import os
import re

repo_dir = "/home/noblixy/The Noblett Repository"

# Find all markdown files
md_files = []
pdf_files = []
for root, dirs, files in os.walk(repo_dir):
    for f in files:
        if f.endswith(".md"):
            md_files.append(os.path.join(root, f))
        elif f.endswith(".pdf"):
            pdf_files.append(os.path.join(root, f))

# Replace broken links in specific files
changes = 0

def process_file(f, replacements):
    with open(f, 'r') as file:
        content = file.read()
    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)
    if new_content != content:
        with open(f, 'w') as file:
            file.write(new_content)

for f in md_files:
    if "Foundations" in f or "EECS Core" in f:
        process_file(f, [("[[Next Block]]", "Next Block")])
    if "Templates" in f:
        process_file(f, [
            ("[[Previous Block]]", "Previous Block"),
            ("[[Next Block]]", "Next Block"),
            ("[[{{associated_block}}]]", "{{associated_block}}"),
            ("[[Related Note 1]]", "Related Note 1"),
            ("[[Related Note 2]]", "Related Note 2")
        ])

