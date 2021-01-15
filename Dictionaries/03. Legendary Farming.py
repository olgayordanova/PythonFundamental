items = {'shards': 0, 'fragments': 0,'motes': 0}
junks = {}
needed_items = ['shards', 'fragments','motes']
legendary_item = {'shards': 'Shadowmourne', 'fragments': 'Valanyr','motes': 'Dragonwrath'}
flag =False

while True:
    input_lst = (input().split())
    my_list = [el.lower() for el in input_lst]
    for i in range (0, len(my_list),2):
        key = my_list[i+1]
        value = int(my_list[i])
        if key in needed_items:
            if key in items:
                items[key] += value
            if items[key] >= 250:
                items[key] -= 250
                flag = True
                break
        else:
            if key not in junks:
                junks[key] = value
            else:
                junks[key] += value
    if flag == True:
        break
sorted_items = dict(sorted(items.items(), key=lambda x: (-x[1],x[0])))
sorted_junks = dict(sorted(junks.items(), key=lambda x: x[0]))

print(f"{legendary_item[key]} obtained!")
for key, value in sorted_items.items():
    str = f"{key}: {value}"
    print (str)
for key, value in sorted_junks.items():
    str = f"{key}: {value}"
    print (str)

