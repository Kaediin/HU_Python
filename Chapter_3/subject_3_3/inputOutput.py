def askInfo(text):
    # While statement that runs infinitely unless a return or break statement is called
    while True:
        # Try-Catch statement for the float conversion. This will prevent a crash if occurs
        try:
            # Get value from input and convert to float
            info = float(input(text))
            # Return info
            return info
        # Catch the exception if thrown
        except ValueError:
            # Print message reminding user to enter a number
            print("This is not a number")
            continue

# Call function twice with different questions, gathering your info
hourlyWage = float(askInfo('State your hourly wage: $'))
hoursWorked = float(askInfo('State your hours worked: '))

# Print result
print('Working {} hours accumulates to ${}'.format(hoursWorked, (hourlyWage * hoursWorked)))
