def sumator(start_letter, end_letter, number ):
    sum =0.0
    if 65<=ord(start_letter)<=90:
        sum += number/(ord(start_letter)-64)
    elif 97<=ord(start_letter)<=122:
        sum += number * (ord ( start_letter ) -96)
    if 65<=ord(end_letter)<=90:
        sum -= (ord ( end_letter ) - 64)
    elif 97<=ord(end_letter)<=122:
        sum += (ord ( end_letter ) - 96)
    return sum

line = input ()
total_sum = 0

words = line.split()

for word in words:
    lenght = len(word)
    start_letter = word[0]
    end_letter = word[lenght-1]
    number = int(word[1:lenght-1])
    current_sum = sumator(start_letter, end_letter, number )
    total_sum+=current_sum

print (f"{total_sum:.2f}")