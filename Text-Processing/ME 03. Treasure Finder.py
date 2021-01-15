import re
pattern_type = r'(&)([A-Za-z]+)\1'
pattern_coordinates =r'<([A-Za-z0-9]+)>'
key = (input().split(' '))

while True:
    text = input()
    if text == 'find':
        break
    new_str = ''
    for y in range (0, len(text), len(key)):
        k = y
        for i in range (0, len(key)):
            new_str+=chr(ord(text[k])-int(key[i]))
            if k < len(text)-1:
                k+=1
            else:
                break
        i=0
    type_of_treasure=re.search(pattern_type,new_str)
    coordinates = re.search(pattern_coordinates,new_str)
    type = type_of_treasure.group(2)
    coord = coordinates.group(1)

    print(f"Found {type} at {coord}")

