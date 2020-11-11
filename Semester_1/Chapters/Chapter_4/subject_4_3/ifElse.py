def isAllowedToVote(age):
    passport = input('Do you have a valid Dutch passport? (y/n): ')
    if passport.lower() == 'y' and age > 17:
        print('You are allowed to vote!')
    else:
        print('You are not allowed to vote :(')


age = int(input('State your age: '))
isAllowedToVote(age)
