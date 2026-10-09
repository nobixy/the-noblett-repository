import os

def process_file(filepath):
    # Exclude hubs and indices
    filename = os.path.basename(filepath)
    if filename == "00 - Start Here.md" or filename.endswith("Hub.md") or filename.endswith("Index.md"):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    made_changes = False
    
    if "## ➡️ Next Steps" not in content:
        content += "\n---\n\n## ➡️ Next Steps\n*Why does the next subject come next?*\n- [[Next Block]]\n"
        made_changes = True

    if made_changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Next Steps to {filename}")

curriculum_dir = "/home/noblixy/The Noblett Repository/01 - Curriculum"
for root, _, files in os.walk(curriculum_dir):
    for f in files:
        if f.endswith(".md"):
            process_file(os.path.join(root, f))
