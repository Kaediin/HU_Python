word = ''

while len(word) != 4:
    word = str(input('Enter a string that consist of 4 letters: '))
    if len(word) != 4:
        print('{} has {} letters...'.format(word, len(word)))

print('The word {} is accepted!'.format(word))