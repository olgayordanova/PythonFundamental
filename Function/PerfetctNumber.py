def perfect_number (n):
    iterator = n
    sum=0
    while True:
        if n%2==0:
            n=n//2
        else:
            n=n//2+1
        sum+=n
        if n<=1:
            break
    if sum == iterator:
        output_flag = True
    else:
        output_flag = False

    return output_flag


a = int(input())
result = perfect_number(a)
if result == True:
    print("We have a perfect number!")
else:
    print ( "It's not so perfect." )