available_lockers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
filename = "fa_kluizen"

def displaymenu():
    print(
        "1: Ik wil weten hoeveel kluizen nog vrij zijn\n"
        "2: Ik wil een nieuwe kluis\n"
        "3: Ik wil even iets uit mijn kluis halen\n"
        "4: Ik geef mijn kluis terug\n"
    )
    while True:
        try:
            userChoice = int(input("Voer hier uw keuze in: "))
            if 1 <= userChoice <= 4:
                return userChoice
            else:
                print("Dat is geen geldige optie\n")
                continue
        except ValueError:
            print("Dat is geen geldige optie\n")
            continue


def check_availability():
    try:
        global available_lockers
        file = open(filename, mode="r")

        for line in file:
            items = line.split(";")
            available_lockers.remove(str(items[0]))

    except FileNotFoundError:
        return


def assign_locker():
    try:
        check_availability()
        file = open(filename, mode="a")
        locker_number = available_lockers[0]
        while True:
            password = str(input("Wachtwoord voor kluis {}. (Min 4 tekens): ".format(locker_number)))
            if len(password) > 4:
                break

        file.write("{};{}\n".format(locker_number, password))
        print('You have locker: {}'.format(locker_number))
    except IndexError:
        print('There are no available lockers :(')
        return


def open_locker():
    while True:
        try:
            lockerNumber = str(input("Enter your locker number: "))
            file = open(filename, mode="r")
            for line in file:
                items = line.split(";")
                if items[0] == lockerNumber:
                    password = str(input("Enter password for locker {}: ".format(lockerNumber)))
                    if str(password) == str(items[1].strip()):
                        print("Your locker is open!")
                        return
                    else:
                        print('Incorrect password...')
                else:
                    print('Locker not found. Please try again')

        except ValueError:
            print("Locker not found.")


def free_locker():
    while True:
        try:
            locker_number = str(input("Enter your locker number: "))
            file = open(filename, mode="w+")
            lines = file.readlines()
            for line in lines:
                items = line.split(";")
                if str(items[0]) == str(locker_number):
                    password = str(input("Enter password for locker {}: ".format(locker_number)))
                    if str(password) == str(items[1].strip()):
                        del lines[(int(locker_number) - 1)]
                        for new_line in lines:
                            file.write(new_line)
                        print("Your locker is free and your information has been deleted from our system.")
                        return
                    else:
                        print('Incorrect password...')
                else:
                    print('Locker not found. Please try again')

        except ValueError:
            print("Locker not found.")


choice = displaymenu()

if choice == 1:
    check_availability()
    print("Available lockers:")
    for locker in available_lockers:
        print("{}".format(locker))

elif choice == 2:
    assign_locker()
elif choice == 3:
    open_locker()
elif choice == 4:
    free_locker()

