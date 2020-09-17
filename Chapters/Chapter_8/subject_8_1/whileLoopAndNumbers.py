number = -1
total = 0
counter = 0

# While loop that continues for as long as var 'number' is not 0
while number != 0:
    number = int(input('Enter a number: '))

    # the number is added up to the total var
    total += number

    # Only update the counter if the while loop will still continue (when number is not 0)
    if number != 0:
        counter += 1
print('There have been {} numbers entered, the sum is: {}'.format(counter, total))