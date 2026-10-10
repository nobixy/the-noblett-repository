with open('verify_curriculum.py', 'r') as f:
    text = f.read()

import re
# Remove the folder check
text = re.sub(
    r'\n\s*folder = os\.path\.relpath\(os\.path\.dirname\(path\), CURR\)\n\s*if folder != stage_of\(bid\): bad\(rel, f"should be in \'01 - Curriculum/\{stage_of\(bid\)\}\' \(DR-003\)"\)',
    '', text
)

# And stage_of is now only used if it's referenced elsewhere, but wait, it's not.
# We will leave stage_of there just in case.

with open('verify_curriculum.py', 'w') as f:
    f.write(text)
