import re

with open('00 - Start Here.md', 'r') as f:
    text = f.read()

text = re.sub(
    r'TABLE WITHOUT ID regexreplace\(key, "\^.*/", ""\) AS Stage, length\(rows\) AS Blocks, length\(filter\(rows\.status, \(s\) => s = "done"\)\) AS Done, sum\(rows\.hours_actual\) AS "Hours logged", sum\(rows\.hours_estimate\) AS "Hours planned"\nFROM "01 - Curriculum"\nWHERE block_id AND optional != true\nGROUP BY file\.folder',
    'TABLE WITHOUT ID key AS Stage, length(rows) AS Blocks, length(filter(rows.status, (s) => s = "done")) AS Done, sum(rows.hours_actual) AS "Hours logged", sum(rows.hours_estimate) AS "Hours planned"\nFROM "01 - Curriculum"\nWHERE block_id AND optional != true\nGROUP BY stage',
    text
)

text = re.sub(
    r'TABLE WITHOUT ID regexreplace\(key, "\^.*/", ""\) AS Stage, length\(rows\) AS Blocks, sum\(rows\.hours_actual\) AS "Hours logged", sum\(rows\.hours_estimate\) AS "Hours planned"\nFROM "01 - Curriculum"\nWHERE block_id AND optional != true\nGROUP BY file\.folder',
    'TABLE WITHOUT ID key AS Stage, length(rows) AS Blocks, sum(rows.hours_actual) AS "Hours logged", sum(rows.hours_estimate) AS "Hours planned"\nFROM "01 - Curriculum"\nWHERE block_id AND optional != true\nGROUP BY stage',
    text
)

# Update README to reflect flat curriculum
with open('README.md', 'r') as f:
    readme = f.read()
readme = re.sub(r"- `01 - Curriculum/`: one folder per stage, in study order.*?\. ", "- `01 - Curriculum/`: flat folder of all block notes. ", readme)
with open('README.md', 'w') as f:
    f.write(readme)

with open('00 - Start Here.md', 'w') as f:
    f.write(text)
