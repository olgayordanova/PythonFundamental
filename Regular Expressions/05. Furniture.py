import re
pattern=r'([A-Za-z]+)<<(\d+(.\d+)?)!(\d+)'

product=[]
total_sum=0.0
while True:
    line = input ()
    if line == 'Purchase':
        break
    if not 'Invalid' in line:
        match_obj = re.findall(pattern,line)
        for match in match_obj:
            product.append ( match[0] )
            total_sum+=float(match[1])*int(match[3])

print ( "Bought furniture:" )
for el in product:
    print ( el)
print ( f'Total money spend: {total_sum:.2f}')





