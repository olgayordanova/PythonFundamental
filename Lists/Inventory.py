def participate(my_string,my_list):
    if my_string in my_list:
        return True


items = input().split(', ')
while True:
    command = input()
    if command == 'Craft!':
        break
    action, item = command.split(' - ')
    if action == 'Collect':
        if participate ( item, items ) != True:
            items.append(item)
    elif action == 'Drop':
        if participate ( item, items ) == True:
            items.remove(item)
    elif action == 'Combine Items':
        item_old, item_new = item.split(':')
        if participate ( item_old, items ) == True:
            i = items.index (item_old)
            items.insert ( i+1, item_new )
    elif action == 'Renew':
        if participate(item, items) == True:
            items.remove ( item )
            items.append ( item )

print(', '.join(items))


