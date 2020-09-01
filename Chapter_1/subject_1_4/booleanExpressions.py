from subject1_3 import statements

# 1
comparisonNumber = 6.75
outcomeNumbers = statements.a < comparisonNumber < statements.b
print("The outcome is {}".format(outcomeNumbers))

# 2
fullnameLen = len(statements.fullname)
sumOfLenNames = sum([len(statements.firstname), len(statements.surname)])
print("{} is equal to '{}' length = {}".format(fullnameLen, statements.fullname, fullnameLen == sumOfLenNames))

# 3
is5xLargerThanC = fullnameLen > (statements.c * 5)
print("{} is atleast 5x larger than {} = {}".format(fullnameLen, statements.c, is5xLargerThanC))

# 4
isInfixInSurname = statements.infix in statements.surname
print("'{}' is in '{}' = {}".format(statements.infix, statements.surname, isInfixInSurname))