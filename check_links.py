import os
import re

repo_dir = "/home/noblixy/The Noblett Repository"

# Find all markdown files
md_files = []
for root, dirs, files in os.walk(repo_dir):
    for f in files:
        if f.endswith(".md"):
            md_files.append(os.path.join(root, f))

# Collect all valid target names
# A wikilink [[Target]] or [[Target|Alias]] typically matches the basename of a file (without .md)
valid_targets = set()
for f in md_files:
    basename = os.path.basename(f)
    valid_targets.add(basename[:-3])
    valid_targets.add(basename) # sometimes .md is included

# Find and validate wikilinks
missing_links = []
wikilink_pattern = re.compile(r'\[\[(.*?)\]\]')

for f in md_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        links = wikilink_pattern.findall(content)
        for link in links:
            # Handle aliases: [[Target|Alias]]
            target = link.split('|')[0].strip()
            # Handle anchors: [[Target#Anchor]]
            target = target.split('#')[0].strip()
            
            if target not in valid_targets and target != "":
                missing_links.append((f, target))

if missing_links:
    for f, t in missing_links:
        print(f"Broken link in {os.path.relpath(f, repo_dir)}: {t}")
else:
    print("All wikilinks are valid.")

