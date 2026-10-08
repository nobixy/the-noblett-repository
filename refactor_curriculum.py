import os
import re

curriculum_dir = "/home/noblixy/The Noblett Repository/01 - Curriculum"
template_path = "/home/noblixy/The Noblett Repository/08 - Templates/Block Note Template.md"

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip hub files
    if "type: hub" in content or "00 - Start Here" in filepath or not content.startswith('---'):
        return

    # Skip files that don't look like blocks
    if "block_id:" not in content:
        return

    # Extract sequential flow to find prerequisites and next steps
    prev_block = None
    next_block = None
    nav_match = re.search(r'\*\*Sequential Flow:\*\*\s*\[\[(.*?)\]\].*?\[\[(.*?)\]\]', content)
    if nav_match:
        pass
    
    # Let's extract the actual links from the navigation section
    nav_section = re.search(r'## 🧭 Navigation\n.*?- \*\*Sequential Flow:\*\*\s*\[\[(.*?)\]\].*?\[\[00 - Dashboard\|Dashboard\]\]\s*\|\s*\[\[(.*?)\]\]', content, re.DOTALL)
    if nav_section:
        prev_raw = nav_section.group(1)
        next_raw = nav_section.group(2)
        # e.g. "Math for CS|← 10 - Math for CS"
        prev_block = prev_raw.split('|')[0].strip()
        next_block = next_raw.split('|')[0].strip()

    # We also need to map the headers. Let's do a smart regex replacement.
    
    # 1. Frontmatter
    # Add 'category: "core"' if missing
    if 'category:' not in content:
        content = re.sub(r'(title: ".*?")', r'\1\ncategory: "core"', content, count=1)
    
    # Remove 'milestone:' from frontmatter? The template doesn't have it.
    content = re.sub(r'milestone: ".*?"\n', '', content)
    
    # Remove the block overview blockquote if we want, or adjust it?
    # The template has:
    # > [!INFO] README / Overview
    # > **Estimated Hours:** {{hours_estimate}} hrs
    # > **Status:** `{{status}}`
    
    # Let's just fix the headers for now.
    
    # ## 🎯 Why This Block Matters -> ## 🎯 Why This Matters
    content = content.replace("## 🎯 Why This Block Matters", "## 🎯 Why This Matters")
    
    # Insert ## 🔗 Prerequisites after Why This Matters section
    # Find the next header after Why This Matters
    why_matters_end = re.search(r'(## 🎯 Why This Matters.*?\n)(?=## )', content, re.DOTALL)
    if why_matters_end:
        why_text = why_matters_end.group(1)
        prereq_text = f"\n## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n"
        if prev_block:
            prereq_text += f"- [[{prev_block}]]\n"
        else:
            prereq_text += f"- \n"
        
        prereq_text += f"\n## 🧠 Learning Objectives\n*What will you understand by the end of this block?*\n"
        
        content = content.replace(why_text, why_text + prereq_text)
        
    # ## 📖 Primary Syllabus & Core Content OR ## 📖 Primary Syllabus -> ## 📖 Core Resources
    content = re.sub(r'## 📖 Primary Syllabus(?: & Core Content)?(?: & Actions)?', '## 📖 Core Resources', content)
    
    # ## 🛠️ Build Requirement -> ## 🛠️ Execution
    content = content.replace("## 🛠️ Build Requirement", "## 🛠️ Execution\n### Exercises & Problem Sets\n\n### Labs & Projects")
    
    # ## 🏁 Done When -> ## 🏁 Mastery Criteria & Assessments
    done_when_match = re.search(r'## 🏁 Done When\n> \[!IMPORTANT\]\n> (.*?)\n', content, re.DOTALL)
    if done_when_match:
        milestone_text = done_when_match.group(1).strip()
        new_done_when = f"## 🏁 Mastery Criteria & Assessments\n> [!IMPORTANT]\n> A block is done when you can independently satisfy these criteria. Not before.\n- [ ] {milestone_text}\n"
        content = re.sub(r'## 🏁 Done When\n> \[!IMPORTANT\]\n> .*?\n', new_done_when, content, flags=re.DOTALL)
    
    # ## 📝 Study Notes, Psets & Proofs -> ## 📝 Study Notes & Proofs
    content = content.replace("## 📝 Study Notes, Psets & Proofs", "## 📝 Study Notes & Proofs")
    
    # Replace ## 🧭 Navigation with ## ➡️ Next Steps
    if "## 🧭 Navigation" in content:
        nav_full = re.search(r'## 🧭 Navigation\n.*', content, re.DOTALL)
        if nav_full:
            next_step_text = "## ➡️ Next Steps\n*Why does the next subject come next?*\n"
            if next_block:
                next_step_text += f"- [[{next_block}]]\n"
            else:
                next_step_text += "- \n"
            content = content.replace(nav_full.group(0), next_step_text)
            
    with open(filepath, 'w') as f:
        f.write(content)

changes = 0
for root, _, files in os.walk(curriculum_dir):
    for f in files:
        if f.endswith('.md'):
            process_file(os.path.join(root, f))
            changes += 1

print(f"Processed {changes} files.")
