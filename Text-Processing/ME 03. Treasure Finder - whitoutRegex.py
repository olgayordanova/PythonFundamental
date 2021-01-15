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

    type_of_treasure=new_str
    coordinates = new_str

    start_index_type=0
    end_index_type=0
    start_index_coordinates=0
    end_index_coordinates =0
    for ch in new_str:
        if ch=='&':
            start_index_type = new_str.index(ch)
            end_index_type = new_str.find('&', start_index_type+1 )
        elif ch=='<':
            start_index_coordinates =new_str.index(ch)
            end_index_coordinates =new_str.find('>', start_index_coordinates+1 )

    type_of_treasure = new_str[start_index_type+1:end_index_type]
    coordinate = new_str[start_index_coordinates + 1:end_index_coordinates]

    print(f"Found {type_of_treasure} at {coordinate}")

