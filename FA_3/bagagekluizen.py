available_lockers = ["0"]
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
            choice = int(input("Voer hier uw keuze in: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Dat is geen geldige optie\n")
                continue
        except ValueError:
            print("Dat is geen geldige optie\n")
            continue

def check_availablilty():
    try:
        global available_lockers
        file = open(filename, mode="r")
        available_lockers.clear()

        for line in file:
            items = line.split(";")
            id = int(items[0])

            available_lockers.append(id)
    except FileNotFoundError:

        available_lockers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        print("Available lockers:")
        for locker in available_lockers:
            print("{}".format(locker))

def assign_locker():
    try:
        file = open(filename, mode="a")
        locker_number = available_lockers[0]
        while True:
            password = str(input("Wachtwoord voor kluis {}. Min 4 tekens): ".format(locker_number)))
            if len(password) > 4:
                break

        file.write("{};{}\n".format(locker_number, password))
    except IndexError:
        return


def open_locker():
    while True:
        try:
            locker = str(input("Enter your locker number: "))
            file = open(filename, mode="r")
            for line in file:
                items = line.split(";")
                if items[0] == locker:
                    password = str(input("Enter your locker password: "))
                    if str(password) == str(items[1].strip()):
                        print("Your locker is open!")
                        return
                    else:
                        print("Pass is {}, entered pass is {}".format(items[1].strip(), password))

        except ValueError:
            print("Locker not found.")



choice = displaymenu()

if choice == 1:
    check_availablilty()
elif choice == 2:
    assign_locker()
elif choice == 3:
    open_locker()
else:
    free_locker()

