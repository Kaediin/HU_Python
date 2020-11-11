berichten = ['Hello', 'World', 'This', 'Is', 'Python', 'But', 'I', 'like', 'Java', 'Better']
woordenEnStatus = {}
for bericht in berichten:
    hasFeedback = False
    while not hasFeedback:
        print('Bericht: {}'.format(bericht))
        feedback = input('Is dit bericht goed gekeurd?(y/n): ')
        if feedback == 'y':
            woordenEnStatus[bericht] = 'goedgekeurd'
            hasFeedback = True
        elif feedback == 'n':
            woordenEnStatus[bericht] = 'afgekeurd'
            hasFeedback = True
        else:
            print('Geef een geldig antwoord (y/n)')
            continue

for k, v in woordenEnStatus.items():
    print('Bericht: {} is {}'.format(k, v))