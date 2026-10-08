import os
import re

curriculum_dir = "/home/noblixy/The Noblett Repository/01 - Curriculum"
files_to_fix = [
    "Reading, Thinking, and Writing.md",
    "Calculus I.md",
    "Math for CS.md",
    "Linear Algebra.md",
    "Algorithms I.md",
    "CS61A.md"
]

for filename in files_to_fix:
    filepath = None
    for root, _, files in os.walk(curriculum_dir):
        if filename in files:
            filepath = os.path.join(root, filename)
            break
            
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Fix the status line
    content = re.sub(r'status: \nprerequisites:\n(.*?)not-started', r'status: not-started\nprerequisites:\n\1', content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)
