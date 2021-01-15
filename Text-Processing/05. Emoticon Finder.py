string = input()
emot_symbol = ''
for i in range (0, len(string)):
    if string[i] == ":":
        emot_symbol = string[i]+string[i+1]
        print(emot_symbol)

