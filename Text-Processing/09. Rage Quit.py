line = input ()
current_string = ''
current_number = ''
output_string = ''

i = 0
while i < len ( line ):
    ch = line[i]
    if ch.isdigit ():
        current_number = ch
        if i + 1 < len ( line ) and (line[i + 1]).isdigit ():
            current_number += line[i + 1]
            i += 1
        count = int ( current_number )
        output_string += current_string.upper() * count
        current_string = ''
    else:
        current_string += ch
    i += 1

unique_count = len(set(output_string))
print(f"Unique symbols used: {unique_count}")
print ( output_string )
