import re
text = input()
list=[]
pattern=r'(^|(?<=\s))_([a-zA-Z0-9]+)($|(?=\s))'
matches = re.findall(pattern, text)

for match in matches:
    list.append(match[1])
print(','.join(list))

