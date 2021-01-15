import re
pattern=r'( |^)[a-zA-Z0-9]+((\.|\-|_)?[a-zA-Z0-9]+)*@([a-zA-Z]+(\-+[a-zA-Z]+)*)(\.([a-zA-Z]+(\-+[a-zA-Z]+)*)){1,}'
text = input()

matches = re.finditer(pattern, text)
for match in matches:
    print(match[0].strip())