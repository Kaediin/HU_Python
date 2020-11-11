stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']


def inlezen_beginstation(stations):
    while True:
        station = str(input('Geef hier uw beginstation aan: '))
        if station in stations:
            return station
        else:
            print('Dit station komt niet voor op dit traject.')


def inlezen_eindstation(beginstation, stations):
    while True:
        station = str(input('Geef hier uw eindstation aan: '))
        indexBegin = stations.index(beginstation)
        if station in stations:
            indexEind = stations.index(station)
            if indexEind > indexBegin:
                return station
            else:
                print('Station: {} komt niet na uw beginstation'.format(station))
        else:
            print('Dit station komt niet voor op dit traject.')


def omroepen_reis(stations, beginstation, eindstation):
    indexBegin = stations.index(beginstation) + 1
    indexEind = stations.index(eindstation) + 1
    tussenstations = indexEind - indexBegin
    kosten = tussenstations * 5

    print(
        '\nHet beginstation {} is het {}e station in het traject. \nHet eindstation {} is het {}e station in het traject. \nDe afstand bedraagt {} station(s). \nDe prijs van het kaartje is {} euro.\n'.format(
            beginstation, indexBegin, eindstation, indexEind, tussenstations, kosten))
    print('Jij stapt in de trein in: {} - {} \nJij stapt uit in: {}'.format(beginstation, stations[
        stations.index(beginstation) + 1], eindstation))


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(beginstation, stations)
omroepen_reis(stations, beginstation, eindstation)
