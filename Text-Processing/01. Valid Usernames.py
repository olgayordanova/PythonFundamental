def lenght(user_name):
    if 3<= len(user_name)<=16:
        return True


def type_dig(user_name):
    for char in user_name:
        if not (char.isalnum() or char =='-' or char =='_'):
            return False
    return True


def redundant(user_name):
    for char in user_name:
        if char==' ':
            return False
    return True


def user_name_validation(user_name):
    if lenght(user_name) and type_dig(user_name) and redundant(user_name):
        return True


user_names = input().split(', ')

for user_name in user_names:
    if user_name_validation(user_name):
        print(user_name)