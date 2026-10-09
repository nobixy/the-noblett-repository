import os
import re

curriculum_dir = "01 - Curriculum"

canonical_metadata = {
    # Phase 0 & Foundations
    "Learning How to Learn.md": {"tier": "Tier 1 - Core", "prereqs": []},
    "The Deep Learner's Toolkit.md": {"tier": "Tier 1 - Core", "prereqs": []},
    "Tooling.md": {"tier": "Tier 1 - Core", "prereqs": []},
    "Bedrock English and Grammar.md": {"tier": "Tier 1 - Core", "prereqs": []},
    "Reading, Thinking, and Writing.md": {"tier": "Tier 1 - Core", "prereqs": ["Bedrock English and Grammar"]},
    "Bedrock Mathematics.md": {"tier": "Tier 1 - Core", "prereqs": []},
    "Math Prerequisites.md": {"tier": "Tier 1 - Core", "prereqs": ["Bedrock Mathematics"]},
    
    # Mathematics
    "Calculus I.md": {"tier": "Tier 1 - Core", "prereqs": ["Math Prerequisites"]},
    "Multivariable Calculus.md": {"tier": "Tier 1 - Core", "prereqs": ["Calculus I"]},
    "Linear Algebra.md": {"tier": "Tier 1 - Core", "prereqs": ["Multivariable Calculus"]},
    "Math for CS.md": {"tier": "Tier 1 - Core", "prereqs": ["Math Prerequisites"]},
    "Probability.md": {"tier": "Tier 1 - Core", "prereqs": ["Calculus I", "Math for CS"]},
    "Statistics.md": {"tier": "Tier 1 - Core", "prereqs": ["Probability", "Linear Algebra"]},
    "Differential Equations Bridge.md": {"tier": "Tier 2 - Support", "prereqs": ["Multivariable Calculus", "Linear Algebra"]},
    "Real Analysis.md": {"tier": "Tier 3 - Depth", "prereqs": ["Math Prerequisites", "Multivariable Calculus"]},
    "Convex Optimization.md": {"tier": "Tier 3 - Depth", "prereqs": ["Linear Algebra", "Multivariable Calculus"]},
    
    # Computer Science
    "Programming On-Ramp.md": {"tier": "Tier 2 - Support", "prereqs": []},
    "CS61A.md": {"tier": "Tier 1 - Core", "prereqs": ["Math Prerequisites"]},
    "SICP.md": {"tier": "Tier 3 - Depth", "prereqs": ["CS61A"]},
    "C Fluency.md": {"tier": "Tier 1 - Core", "prereqs": ["CS61A"]},
    "Algorithms I.md": {"tier": "Tier 1 - Core", "prereqs": ["C Fluency", "Math for CS"]},
    "Algorithms II.md": {"tier": "Tier 1 - Core", "prereqs": ["Algorithms I", "Probability"]},
    "Software Construction.md": {"tier": "Tier 1 - Core", "prereqs": ["CS61A", "C Fluency"]},
    "Interpreters.md": {"tier": "Tier 1 - Core", "prereqs": ["Software Construction", "Computer Systems"]},
    "Theory of Computation.md": {"tier": "Tier 1 - Core", "prereqs": ["Math for CS", "Algorithms I"]},
    "Information Theory.md": {"tier": "Tier 3 - Depth", "prereqs": ["Probability"]},
    
    # Computer Engineering & Systems
    "Nand2Tetris.md": {"tier": "Tier 1 - Core", "prereqs": ["CS61A"]},
    "Computer Systems.md": {"tier": "Tier 1 - Core", "prereqs": ["C Fluency", "Nand2Tetris"]},
    "Computer Architecture.md": {"tier": "Tier 2 - Support", "prereqs": ["Computer Systems"]},
    "Operating Systems.md": {"tier": "Tier 1 - Core", "prereqs": ["Computer Systems"]},
    "Networking.md": {"tier": "Tier 1 - Core", "prereqs": ["Operating Systems"]},
    
    # Software Engineering At Scale
    "Databases.md": {"tier": "Tier 1 - Core", "prereqs": ["Operating Systems", "Algorithms I"]},
    "Distributed Systems.md": {"tier": "Tier 1 - Core", "prereqs": ["Databases", "Networking"]},
    
    # Electrical Engineering
    "Physics I.md": {"tier": "Tier 1 - Core", "prereqs": ["Calculus I"]},
    "Physics II.md": {"tier": "Tier 1 - Core", "prereqs": ["Physics I", "Multivariable Calculus"]},
    "Circuits and Electronics Bridge.md": {"tier": "Tier 2 - Support", "prereqs": ["Physics II", "Differential Equations Bridge"]},
    "Signals and Systems Bridge.md": {"tier": "Tier 2 - Support", "prereqs": ["Circuits and Electronics Bridge", "Linear Algebra"]}
}

for root, dirs, files in os.walk(curriculum_dir):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            with open(path, "r") as file:
                content = file.read()
            
            if "type: hub" in content or "00 -" in f:
                continue
                
            tier = "Tier 3 - Depth"
            prereqs = []
            if f in canonical_metadata:
                tier = canonical_metadata[f]["tier"]
                prereqs = canonical_metadata[f]["prereqs"]
            
            yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if yaml_match:
                yaml_content = yaml_match.group(1)
                
                if "tier:" in yaml_content:
                    yaml_content = re.sub(r"tier:.*", f'tier: "{tier}"', yaml_content)
                else:
                    yaml_content += f'\ntier: "{tier}"'
                    
                prereq_str = "prerequisites:\n" + "\n".join([f'  - "{p}"' for p in prereqs])
                if not prereqs:
                    prereq_str = "prerequisites: []"
                
                yaml_content = re.sub(r"prerequisites:.*?(?=\n[a-z_]+:|\Z)", prereq_str, yaml_content, flags=re.DOTALL)
                
                new_content = content[:yaml_match.start()] + "---\n" + yaml_content + "\n---" + content[yaml_match.end():]
                
                if "## 📚 Curriculum Tier" not in new_content and f in canonical_metadata:
                    insert_idx = new_content.find("## 🎯 Why This Block Matters")
                    if insert_idx != -1:
                        tier_info = f"## 📚 Curriculum Tier: {tier}\n> **{tier}**: { 'Must complete before advancing.' if 'Tier 1' in tier else 'Strongly recommended for full understanding.' if 'Tier 2' in tier else 'Optional deep dive for specialized mastery.' }\n\n"
                        new_content = new_content[:insert_idx] + tier_info + new_content[insert_idx:]
                
                md_prereqs = "\n".join([f"- [[{p}]]" for p in prereqs])
                if not prereqs:
                    md_prereqs = "- *None. This is a foundational block.*"
                    
                new_content = re.sub(
                    r"## 🔗 Prerequisites\n\*What must you have mastered before starting this block\?\*\n(?:- \[\[.*?\]\]\n?|)*",
                    f"## 🔗 Prerequisites\n*What must you have mastered before starting this block?*\n{md_prereqs}\n\n",
                    new_content
                )
                
                with open(path, "w") as file:
                    file.write(new_content)
print("Curriculum metadata updated.")
