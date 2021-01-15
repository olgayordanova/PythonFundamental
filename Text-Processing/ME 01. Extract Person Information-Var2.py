import re
n= int(input())

person = {}

name_pattern = r'(@)(?P<name>[A-Za-z]+)(\|)'
age_patern = r'(#)(?P<age>[0-9]+)(\*)'

for i in range (1, n+1):
    text = input ()
    name = re.search(name_pattern,text)
    age = re.search(age_patern,text)
    person[name.group (2)]=age.group(2)

for key, value in person.items():
    print(f"{key} is {value} years old.")
