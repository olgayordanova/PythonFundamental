import re
customer_pattern = r'(%)([A-Z][a-z]+)\1' #2
product_pattern = r'<(\w+)>'#1
count_pattern = r'(\|)(\d+)\1' #2
price_pattern = r'((\d+)(\.\d+)?)\$' #1

total_sum = 0.0
while True:
    line = input()
    if line == 'end of shift':
        break
    try:
        customer_name = re.search(customer_pattern,line).group(2)
        product = re.search(product_pattern,line).group(1)
        count = int(re.search(count_pattern,line).group(2))
        price = float(re.search(price_pattern,line).group(1))

        total_sum+=count*price
        print(f"{customer_name}: {product} - {(count*price):.2f}")
    except:
        continue

print(f'Total income: {total_sum:.2f}')