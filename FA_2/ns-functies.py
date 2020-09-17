import random

def standaardprijs(afstandKM):
    vasteKosten = 0
    centPerKm = 0.8
    if afstandKM <= 0:
        return 0

    if afstandKM > 50:
        centPerKm = 0.6
        vasteKosten = 15

    return (centPerKm * afstandKM) + vasteKosten

def ritprijs(leeftijd, weekendrit, afstandKM):
    sp = standaardprijs(afstandKM)
    korting = 1

    if leeftijd < 12 or leeftijd >= 65:
        korting -= 0.3
        if weekendrit:
            korting -= 0.05
    elif weekendrit:
        korting -= 0.4

    return round(korting * sp, 2)

try:
    leeftijd = int(input('Wat is uw leeftijd?(getal): '))
    afstand = float(input('Wat is uw afstand in km?(getal): '))
    weekend = str(input('Is het weekend?(y/n): '))

    if weekend.lower() == 'y':
        weekend = True
    elif weekend.lower() == 'n':
        weekend = False
    else:
        raise ValueError

    print('Uw kosten zijn €{:,.2f} voor de totale rit'.format(ritprijs(leeftijd, weekend, afstand)))

except ValueError:
    print('Voer alleen geldige antwoorden in aub.')

# def testIterations(numIterations):
#     for i in range(numIterations):
#         leeftijd = random.randint(1, 100)
#         weekend = random.randint(0, 1)
#         afstandKM = random.randint(0, 100)
#         kosten = ritprijs(leeftijd, weekend, afstandKM)
#         print(
#               "ITERATIE {}\n"
#               "Leeftijd = {}\n"
#               "Weekend = {}\n"
#               "Afstand = {}KM\n"
#               "Heeft als kosten: €{:,.2f}\n"
#               .format(i+1, leeftijd, bool(weekend), afstandKM, kosten)
#               )

# def hcTestcases():
#     print('€{:,.2f}'.format(ritprijs(11, 0, 40)))
#     print('€{:,.2f}'.format(ritprijs(12, 0, 40)))
#     print('€{:,.2f}'.format(ritprijs(64, 0, 40)))
#     print('€{:,.2f}\n'.format(ritprijs(65, 0, 40)))
#
#     print('€{:,.2f}'.format(ritprijs(11, 1, 40)))
#     print('€{:,.2f}'.format(ritprijs(12, 1, 40)))
#     print('€{:,.2f}'.format(ritprijs(64, 1, 40)))
#     print('€{:,.2f}\n'.format(ritprijs(65, 1, 40)))
#
#     print('€{:,.2f}'.format(ritprijs(11, 0, 80)))
#     print('€{:,.2f}'.format(ritprijs(12, 0, 80)))
#     print('€{:,.2f}'.format(ritprijs(64, 0, 80)))
#     print('€{:,.2f}\n'.format(ritprijs(65, 0, 80)))
#
#     print('€{:,.2f}'.format(ritprijs(11, 1, 80)))
#     print('€{:,.2f}'.format(ritprijs(12, 1, 80)))
#     print('€{:,.2f}'.format(ritprijs(64, 1, 80)))
#     print('€{:,.2f}\n'.format(ritprijs(65, 1, 80)))
#
#     print('€{:,.2f}'.format(ritprijs(11, 0, 0)))
#     print('€{:,.2f}'.format(ritprijs(12, 0, 0)))
#     print('€{:,.2f}'.format(ritprijs(64, 0, 0)))
#     print('€{:,.2f}\n'.format(ritprijs(65, 0, 0)))
#
#     print('€{:,.2f}'.format(ritprijs(11, 1, 0)))
#     print('€{:,.2f}'.format(ritprijs(12, 1, 0)))
#     print('€{:,.2f}'.format(ritprijs(64, 1, 0)))
#     print('€{:,.2f}\n'.format(ritprijs(65, 1, 0)))

# hcTestcases()
# testIterations(24)
