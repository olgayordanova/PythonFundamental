import re

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

text = '\n'.join(lines)
pattern=r'(\d+)'

matches = re.findall(pattern, text, re.MULTILINE)
print(' '.join(matches))