import re
pattern=r'(www.[A-Za-z0-9\-]*(\.([A-Za-z]+))+)'
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

for elenent in lines:
    matches = re.findall(pattern, elenent)
    for match in matches:
        print ( (match[0]), end= '\n' )


