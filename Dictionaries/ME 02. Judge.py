contests = {}

while True:
    line = input ()
    if line == 'no more time':
        break
    tokens = line.split ( ' -> ' )
    username = tokens[0]
    contest = tokens[1]
    points = int ( tokens[2] )
    if contest not in contests:
        contests[contest] = {username: 0}
        if username in contests[contest]:
            if contests[contest][username] < points:
                contests[contest][username] = points
        else:
            contests[contest][username] = points
    else:
        if username in contests[contest]:
            if contests[contest][username] < points:
                contests[contest][username] = points
        else:
            contests[contest][username] = points

for key, value in contests.items ():
    print ( f'{key}: {len ( value )} participants' )
    position = 1
    for k, v in sorted ( value.items (), key=lambda x: (-x[1], x[0]) ):
        print ( f'{position}. {k} <::> {v}' )
        position += 1

print ( 'Individual standings:' )
individual = {}
for value in contests.values ():
    for k, v in value.items ():
        if k not in individual:
            individual[k] = 0
        individual[k] += v
position = 1
for key, value in sorted ( individual.items (), key=lambda x: (-x[1], x[0]) ):
    print ( f'{position}. {key} -> {value}' )
    position += 1