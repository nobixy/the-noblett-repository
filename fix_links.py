import os
import re

repo_dir = "/home/noblixy/The Noblett Repository"

# Find all markdown files
md_files = []
for root, dirs, files in os.walk(repo_dir):
    for f in files:
        if f.endswith(".md"):
            md_files.append(os.path.join(root, f))

wikilink_pattern = re.compile(r'\[\[(.*?)\]\]')
changes = 0

for f in md_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    def replace_link(match):
        inner = match.group(1)
        # Split by alias if present
        parts = inner.split('|', 1)
        target = parts[0].strip()
        alias = parts[1].strip() if len(parts) > 1 else None
        
        # Split by anchor if present
        target_parts = target.split('#', 1)
        path = target_parts[0]
        anchor = f"#{target_parts[1]}" if len(target_parts) > 1 else ""
        
        # If the path contains a slash, it's a directory path. We want just the basename.
        if '/' in path:
            basename = path.split('/')[-1]
            if alias:
                return f"[[{basename}{anchor}|{alias}]]"
            else:
                return f"[[{basename}{anchor}]]"
        return match.group(0)

    new_content = wikilink_pattern.sub(replace_link, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        changes += 1

print(f"Updated wikilinks in {changes} files.")

