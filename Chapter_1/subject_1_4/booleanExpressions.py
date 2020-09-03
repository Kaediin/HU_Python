# SUBJECT 1_3!
# 1
a = 6
b = 7

# 2
c = sum([a, b]) / 2
print("Average of [{}, {}] = {}".format(a, b, c))

# 3
firstname = "Kaedin"
infix = "van de"
surname = "Schouten"

# 4
fullname = "{} {} {}".format(firstname, infix, surname)
print("My name is: {}".format(fullname))

# SUBJECT 1_4
# 1
comparisonNumber = 6.75
outcomeNumbers = a < comparisonNumber < b
print("The outcome is {}".format(outcomeNumbers))

# 2
fullnameLen = len(fullname)
sumOfLenNames = sum([len(firstname), len(surname)])
print("{} is equal to '{}' length = {}".format(fullnameLen, fullname, fullnameLen == sumOfLenNames))

# 3
is5xLargerThanC = fullnameLen > (c * 5)
print("{} is atleast 5x larger than {} = {}".format(fullnameLen, c, is5xLargerThanC))

# 4
isInfixInSurname = infix in surname
print("'{}' is in '{}' = {}".format(infix, surname, isInfixInSurname))