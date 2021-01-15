line = input ()
total_strength = 0

i = 0
while i < len ( line ):
    ch = line[i]
    if ch == ">":
        strength = int ( line[i + 1] )
        total_strength += strength
    else:
        if total_strength > 0:
            line = line[:i] + line[i + 1:]
            i -= 1
            total_strength -= 1
    i += 1
print ( line )
