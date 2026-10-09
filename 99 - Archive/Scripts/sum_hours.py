import os
import re

total_hours = 0
for root, dirs, files in os.walk("01 - Curriculum"):
    for file in files:
        if file.endswith(".md") and "Specializations" not in root and "00 -" not in file:
            with open(os.path.join(root, file), "r") as f:
                content = f.read()
                match = re.search(r'^hours_estimate:\s*(\d+)', content, re.MULTILINE)
                if match:
                    total_hours += int(match.group(1))

print(f"Total hours: {total_hours}")
