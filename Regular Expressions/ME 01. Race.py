import re

name_pattern = r'[A-Za-z]+'
age_pattern = r'\d'
dict_participiants={}
age=0
participiants = input().split(', ')
for item in participiants:
    dict_participiants[item] = age

while True:
    line = input()
    if line == 'end of race':
        break
    name_symbols = re.findall ( name_pattern, line )
    name =''.join(name_symbols)
    if name in dict_participiants.keys():
        age_numbers = re.findall ( age_pattern, line )
        age = sum([int(n) for n in age_numbers])
        dict_participiants[name] +=age

sorted_dict_participiants = sorted(dict_participiants.items (), key=lambda x: (-x[1]))

print ( f"1st place: {sorted_dict_participiants[0][0]}")
print ( f"2nd place: {sorted_dict_participiants[1][0]}" )
print ( f"3rd place: {sorted_dict_participiants[2][0]}" )

