# Opens the file in read mode (hence the "r")
file = open("pe_6_2_kaartnummers.txt", "r")

# Declares empty vars
lines = 0
highest_number = -1
highest_number_line = 0

# foreach line in file
for line in file:
    # increase lines var by 1
    lines += 1

    # splits the line by each ',' creating a list with [0] = id and [1] = name
    items = line.split(',')
    id = int(items[0])
    if id > highest_number:
        highest_number = id
        highest_number_line = lines





print('This file counts {} lines'.format(lines))
print('The highest number is {} on line {}'.format(highest_number, highest_number_line))