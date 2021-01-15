def test_last_symbol (result_string, symbol):
    if result_string[len(result_string)-1] == symbol:
        return True

string = input()
result_string = string[0]
for i in range (1, len(string)):
    if test_last_symbol (result_string, string[i] ):
        continue
    else:
        result_string +=string[i]

print(result_string)