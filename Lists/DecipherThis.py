def change_letter(word):
    new_word_list = [char for char in word]
    new_word_list[1], new_word_list[len(new_word_list) -1] = new_word_list[len(new_word_list) -1],new_word_list[1]
    new_word_list = ''.join(new_word_list)
    return new_word_list


decifer_list = list(input().split(' '))

decifer_list_new=[]
for i in range (0, len(decifer_list)):
    flag = 0
    num = []
    for char in decifer_list[i]:
        if 48 <= ord ( char ) <= 57:
            num.append ( char )
            flag += 1
        curent_num = int ( ''.join ( [n for n in num] ) )
    curent_letter = chr ( curent_num )
    new_word = curent_letter+decifer_list[i][flag:]
    new_word= change_letter(new_word)
    decifer_list_new.append(new_word)
print(' '.join(decifer_list_new))