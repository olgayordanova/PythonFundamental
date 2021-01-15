import sys
def exchange(numbers, i):
    first_part = numbers[:i + 1]
    second_part = numbers[i + 1:]
    return second_part + first_part


def max_even_index(numbers, even):
    max_number_even = -sys.maxsize
    max_number_even_index = -1
    for i in range(len(numbers)):
        if numbers[i] % 2 == even and numbers[i] >= max_number_even:
            max_number_even = numbers[i]
            max_number_even_index = i

    if max_number_even_index == -1:
        return 'No matches'
    else:
        return max_number_even_index


def min_even_index(numbers, even):
    min_number_even = sys.maxsize
    max_number_even_index = -1
    for i in range(len(numbers)):
        if numbers[i] % 2 == even and numbers[i] <= min_number_even:
            min_number_even = numbers[i]
            max_number_even_index = i

    if max_number_even_index == -1:
        return 'No matches'
    else:
        return max_number_even_index


def first(numbers, event, counter):
    first_list_odd = []
    count = 0
    for number in numbers:
        if count == counter:
            break
        if number % 2 == event:
            first_list_odd.append(number)
            count += 1

    return first_list_odd


def last(numbers, even, counter):
    last_list_even = []
    count = 0
    for i in range(len(numbers) - 1, -1, -1):

        if count == counter:
            break

        if numbers[i] % 2 == even:
            last_list_even.append(numbers[i])
            count += 1

    return last_list_even[::-1]


numbers_list = input().split(' ')
numbers_list = [int(x) for x in numbers_list]

command_input = input().split(' ')
while command_input[0] != 'end':
    command = command_input[0]

    if command == 'exchange':
        index = int(command_input[1])
        if len(numbers_list) > index >= 0:
            numbers_list = exchange(numbers_list, index)
        else:
            print('Invalid index')
    elif command == 'max':
        criteria = command_input[1]
        res = max_even_index(numbers_list, 0 if criteria == "even" else 1)
        print(res)
    elif command == 'min':
        criteria = command_input[1]
        res = min_even_index(numbers_list, 0 if criteria == "even" else 1)
        print(res)
    elif command == 'first':
        criteria = command_input[2]
        index = int(command_input[1])
        if len(numbers_list) >= index >= -1:
            print(first(numbers_list, 0 if criteria == "even" else 1, index))
        else:
            print('Invalid count')
    elif command == 'last':
        criteria = command_input[2]
        index = int(command_input[1])
        if len(numbers_list) >= index >= -1:
            print(last(numbers_list, 0 if criteria == "even" else 1, index))
        else:
            print('Invalid count')

    command_input = input().split(' ')

print(numbers_list)