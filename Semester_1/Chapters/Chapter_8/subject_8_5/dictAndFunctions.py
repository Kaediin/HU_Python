
# Declare empty dictionary
dict = {}

def names():
    name = 'placeholder'
    while name != '':
        name = str(input('Enter a name here: '))
        if name != '':

            # if name is not '' add it to the dict
            # make sure the value is the previous value + 1, to keep track of the amount of people with those names
            # if there isnt a value it will be by default (hence the '(name, 0)')
            dict[name] = dict.get(name, 0) +1

# call the function
names()

# for loop through all the items in the dictionary
for k, v in dict.items():

    # Use right grammar...
    if v > 1:
        print('There are {} students with the name {}'.format(v, k))
    else:
        print('There is {} student with the name {}'.format(v, k))