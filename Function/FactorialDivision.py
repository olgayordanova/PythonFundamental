def factorial (x):
    result = 1
    for i in range(2,x+1):
        result=result*i
    return result

a=int(input())
b=int(input())

result = factorial(a)/factorial(b)
print(f"{result:.2f}")