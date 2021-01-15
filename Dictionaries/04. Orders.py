shops = {}

while True:
    command = input()
    if command == 'buy':
        break
    name, * data = command.split ()
    if name not in shops:
        shops[name] = (data)
        price = float(shops[name][0])
        quantity = int(shops[name][1])
        shops[name][0]= price
        shops[name][1]=quantity
    else:
        shops[name][0] = float(data[0])
        shops[name][1]+=int(data[1])

for name in shops.keys():
    total_price = shops[name][0]*shops[name][1]
    print(f"{name} -> {total_price:.2f}")
