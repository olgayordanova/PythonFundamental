count_electons = int(input())
shelds=0
distributed_list = []
current_electron_count=count_electons
while True:
    shelds+=1
    if current_electron_count -2*(shelds**2) > 0:
        current_electron_count -= 2*(shelds**2)
        distributed_list.append(2*(shelds**2))
    else:
        distributed_list.append(current_electron_count)
        break
print (distributed_list)


