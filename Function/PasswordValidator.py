def lends_pass(my_pass):
    if (len ( my_pass ) < 6) or (len ( my_pass ) > 10):
        return ( "Password must be between 6 and 10 characters" )


def number_char_pass(my_pass):
    flag = True
    if not my_pass.isalnum ():  # curses.isalnum ( my_pass ):
        flag = False
    if flag == False:
        return ( "Password must consist only of letters and digits" )


def number_digits_pass(my_pass):
    counter = 0
    for b in my_pass:
        if b.isdigit ():  # curses.isdigit ( b ):
            counter += 1
    if counter < 2:
        return ( "Password must have at least 2 digits" )


def validate(password):
    validators_list = [lends_pass, number_char_pass, number_digits_pass]
    validation_errors=[]
    for validator in validators_list:
        result = validator(password)
        if result is not None:
            validation_errors.append(result)
    if len(validation_errors)==0:
        return "Password is valid"
    else:
        return '\n'.join(validation_errors)


password = input ()
result = validate(password)
print(result)