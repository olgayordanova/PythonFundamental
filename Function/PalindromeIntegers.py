def palindrome(my_ls):
    output_ls = []
    for i in range ( len ( my_ls ) ):
        if int ( my_ls[i] ) == int ( reverse ( my_ls[i] ) ):
            output_ls.append ( True )
        else:
            output_ls.append ( False )
    return output_ls


def reverse(x):
    return x[::-1]


my_str = input ()
my_ls = my_str.split ( ', ' )

output_ls = palindrome ( my_ls )
print ( *output_ls, sep='\n' )
