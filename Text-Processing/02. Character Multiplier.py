def prepare_lists(str1, str2):
    n=len(str1)
    for char1 in str1:
        l_str1.append(ord(char1))
    for char2 in str2:
        l_str2.append ( ord ( char2 ) )
    for i in range (len(str2)-1, n):
        l_str2.append(1)
    return l_str1, l_str2

str1, str2 = input().split()
total_sum = 0
l_str1=[]
l_str2=[]

if len(str1)>=len(str2):
    l_str1, l_str2 = prepare_lists(str1, str2)
else:
    k=str1
    str1 = str2
    str2 = k
    l_str1, l_str2 = prepare_lists ( str1, str2 )

for i in range (0, len(l_str1)):
    total_sum+=l_str1[i]*l_str2[i]

print(total_sum)

line = input ().split ()



# recursia
# def multiply(word, required_length, counter):
#     if len ( word ) * counter == required_length:
#         return word * counter
#     counter += 1
#     return multiply ( word, required_length, counter )
#
#
# result = ""
#
# for w in line:
#     length_to_exceed = len ( w * len ( w ) )
#     result += multiply ( w, length_to_exceed, 1 )
#
# print ( result )

