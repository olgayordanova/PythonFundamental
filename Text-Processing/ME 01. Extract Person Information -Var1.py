n= int(input())

for i in range (1, n+1):
    text = input ()
    start_index_name=0
    end_index_name=0
    start_index_age=0
    end_index_age =0
    for ch in text:
        if ch=='@':
            start_index_name = text.index(ch)
        elif ch=='|':
            end_index_name = text.index ( ch )
        elif ch=='#':
            start_index_age =text.index(ch)
        elif ch == '*':
            end_index_age = text.index ( ch )

    name = text[start_index_name+1:end_index_name]
    age = text[start_index_age + 1:end_index_age]
    print ( f"{name} is {age} years old." )
