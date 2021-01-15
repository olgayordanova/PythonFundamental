word= input()
charts = {}
char_lst = [char for char in word if char!=' ']
for char in char_lst:
    if char not in charts:
        charts[char] = 0
    charts[char] += 1

for key, value in charts.items():
    print(f"{key} -> {value}")

