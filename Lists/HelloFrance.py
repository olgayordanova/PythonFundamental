items = input ().split ( '|' )
budget = float ( input () )
new_prices = []
bought_items = []
profit = 0
new_budget = budget

for item in items:
    item = item.split ( "->" )
    y = float ( item[1] )
    x = item[0]
    if (x == 'Clothes' and y <= 50.0) or (x == 'Shoes' and y <= 35.0) or (x == "Accessories" and y <= 20.50):
        if (new_budget - y) >= 0:
            new_budget -= y
            bought_items.append ( y )
            y1 = f'{(y * 1.4):.2f}'
            new_prices.append ( str ( y1 ) )
profit = sum ( [float ( x ) for x in new_prices] ) - sum ( bought_items )

print ( *new_prices )
print ( f"Profit: {profit:.2f}" )
if (budget + profit) >= 150:
    print ( "Hello, France!" )
else:
    print ( "Time to go." )
