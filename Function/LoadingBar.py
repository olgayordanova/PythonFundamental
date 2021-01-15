number=int(input())

x=number//10
if x==10:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
else:
    str = x*"%"
    str1 = (10-x)*"."
    print(f"{number}% [{str}{str1}]")
    print("Still loading...")
