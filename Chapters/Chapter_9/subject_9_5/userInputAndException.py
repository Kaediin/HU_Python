def askInfo(text):
    while True:
        try:
            info = float(input(text))
            return info
        except ValueError:
            print("This is not a number")
            continue

hourlyWage = float(askInfo('State your hourly wage: $'))
hoursWorked = float(askInfo('State your hours worked: '))


print('Working {} hours accumulates to ${}'.format(hoursWorked, (hourlyWage * hoursWorked)))
