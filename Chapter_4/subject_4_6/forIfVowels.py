vowels = "aeiou"
string = "Guido van Rossum heeft programmeertaal Python bedacht."

for letter in string:
    if letter in vowels:
        print(letter)