def get_winner(dict):
    win_points = []
    total_point =0
    win_names= []
    for key, value in dict.items ():
        name = key
        total_point = 0
        for i in range ( 0, len ( value ) ):
            total_point += int(value[i][1])
        win_names.append(name)
        win_points.append ( total_point )
    win_point = max(win_points )
    index_element = win_points.index ( win_point )
    win_name = win_names[index_element]

    return win_name, win_point

def output_view(dict):
    result = ''
    for key, value in dict.items ():
        result += f"{key}" + '\n'
        for i in range ( 0, len ( value ) ):
            current_value = value[i][0]
            current_point = value[i][1]
            result += f"#  {current_value} -> {current_point}" + '\n'
    return result


def get_values(name, sorted_submissions):
    my_list =[]
    for key, value in sorted_submissions.items ():
        if name in key:
            my_value = (value[0],value[2])
            my_list.append(my_value)
    return my_list

def is_valid_submissions(contests_name, contests_password, contests):
    for key, value in contests.items ():
        if key == contests_name and contests_password == value:
            return True
    return False


# Read Inputs
contests = {}
while True:
    command = input ()
    if command == 'end of contests':
        break
    contests_name, contests_password = command.split ( ':' )
    contests[contests_name] = contests_password

submissions = {}
# Правим ключа комбиниран от contests_name +'@'+user_name за да имаме уникална стойност в речника
while True:
    line = input ()
    if line == 'end of submissions':
        break
    contests_name, contests_password, user_name, point = line.split ( '=>' )
    if is_valid_submissions ( contests_name, contests_password, contests):
        # Проверка дали го има contests и дали съответства паролата
        # Ако го няма юзера го добавяме с точките, ако го има, проверяваме дали новите са повече от старите и правим промяна
        pattern = contests_name + '@' + user_name
        if pattern not in submissions.keys():
            submissions[pattern] = [contests_name, user_name, int ( point )]
        else:
            for key, value in submissions.items ():
                # pattern = contests_name + '@' + user_name
                if pattern == key:
                    if int(point) > value[2]:
                        value[2] = int(point)
                        # continue

# ------------Output---------------
# Сортираме submissions по име на състезание и вътре по брой точки на юзери в обратен ред - от най-високите към най ниските
sorted_submissions =  dict(sorted(submissions.items(),  key=lambda x:  (x[1][1], - x[1][2])))

# Печат на изхода
output_dict={}
user_list = sorted(set(el[1] for el in sorted_submissions.values()))
for name in user_list:
    output_dict[name]= get_values(name, sorted_submissions)

win_name, win_point = get_winner(output_dict)

print(f"Best candidate is {win_name} with total {win_point} points.")
print("Ranking:")
print(output_view(output_dict))




