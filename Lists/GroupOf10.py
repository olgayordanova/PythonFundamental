lst_numbers = input().split(', ')
numbers = list(map(lambda x: int(x),lst_numbers))
if max(numbers)%10==0:
    ten_s = max ( numbers ) // 10
else:
    ten_s = max(numbers)//10+1

for i in range (1, ten_s+1):
    current_tens = list((number for number in numbers if  (i-1)*10< number <= i*10 ))
    print(f"Group of {i*10}'s: {current_tens}")