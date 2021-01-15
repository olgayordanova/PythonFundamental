import re
text = input()
word = input()

pattern = '\\b('+ word+')\\b'
matches = re.findall(pattern, text, re.IGNORECASE)
lenght = len(matches)

print(lenght)
