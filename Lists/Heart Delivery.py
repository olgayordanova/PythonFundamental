def update_list (index, new_data, my_list):
    output_list =[]
    for i in range(0, len(my_list)):
        if i == index:
            output_list.append(new_data)
        else:
            output_list.append( my_list[i] )
    return output_list


number_lst = list(map(int,input().split('@')))
current_index =0
sucsses_mision = [0 for i in number_lst ]
sucsses_mision[0]=1

while True:
    s_command = input()
    if s_command == 'Love!':
        break
    command, jump_index = s_command.split(' ')
    current_index =current_index+int(jump_index)

    if current_index>len(number_lst)-1:
        current_index =0

    sucsses_mision[current_index] = 1
    old_heards = number_lst[current_index]

    if old_heards ==0:
        print(f"Place {current_index} already had Valentine's day.")
        new_heards =0
    elif old_heards==2:
        print ( f"Place {current_index} has Valentine's day." )
        new_heards = 0
    else:
        new_heards = number_lst[current_index] - 2

    number_lst = update_list(current_index, new_heards,number_lst)

print(f"Cupid's last position was {current_index}.")

l = [x for x in number_lst if x ==0]
visited_places = len(l)

if visited_places < len(number_lst):
    houseCount = sum(x for x in sucsses_mision)
    print(f"Cupid has failed {len(number_lst)-visited_places} places.")
else:
    print(f"Mission was successful.")


