from random import randint

# OPDRACHT 1a
def pyramide_half():
    n = None
    while n is None:
        try:
            n = int(input('Hoe groot? '))
        except ValueError:
            print('Voer aub een getal in.')
    for stars in range(1, n + 1):
        star_str = ''
        for star in range(0, stars):
            star_str += '*'
        print(star_str)

    pyramide_vol(n)

# OPDRACHT 1b
def pyramide_vol(n):
    for stars in range(1, n + 1, 1):
        star_str = ''
        n -= 1
        for star in range(n + 1, 1, -1):
            star_str += '*'
        print(star_str)

# OPDRACHT 2
def tekstcheck():
    sentence_1 = input('Geef een string: ')
    sentence_2 = input('Geef een string: ')

    if sentence_1 == sentence_2:
        print('Er zijn verschillen tussen de 2 zinnen.')
        return

    max_length = min(len(sentence_1), len(sentence_2))

    for i in range(0, max_length):
        if sentence_1[i] == sentence_2[i]:
            continue
        print(f'Het verschil zit op index: {i}')
        return

    print(f'Het verschil zit op index: {max_length - 1}')

# OPDRACHT 3a
def lijstcheck_count(lst, target):
    n = 0
    for item in lst:
        if item == target:
            n += 1
    return n

# OPDRACHT 3b
def lijstcheck_verschil(lst):
    getal_1 = lst[0]
    try:
        getal_2 = lst[1]
        if getal_1 == getal_2:
            print(0)
        print(getal_1 - getal_2 if getal_1 > getal_2 else getal_2 - getal_1)
        return lijstcheck_verschil(lst[2:])
    except IndexError:
        print(f'0. Getal 1 (waarde = {getal_1}) heeft geen buur.')
        return

# OPDRACHT 3c
def lijstcheck_eisen(lst):
    return True if lijstcheck_count(lst, 1) > lijstcheck_count(lst, 0) and lijstcheck_count(lst, 0) < 13 else False

# OPDRACHT 4
def isPalindroom(word):
    return word == word[::-1]

# OPDRACHT 5
def sorteren(lst):
    # Insertion
    # result = [lst[0]]
    # del lst[0]
    #
    # for item in lst:
    #     inserted = False
    #     for c in range(0, len(result)):
    #         if item < result[c]:
    #             result.insert(c, item)
    #             inserted = True
    #             break
    #     if not inserted:
    #         result.append(item)
    # return result

    # Merge recursive
    if len(lst) > 1:
        # Divide
        q = len(lst) // 2
        p = lst[:q]
        r = lst[q:]
        sorteren(p)
        sorteren(r)
        i, j, k = 0, 0, 0

        # Combine
        while i < len(p) and j < len(r):
            if p[i] < r[j]:
                lst[k] = p[i]
                i += 1
            else:
                lst[k] = r[j]
                j += 1
            k += 1
        while i < len(p):
            lst[k] = p[i]
            i += 1
            k += 1
        while j < len(r):
            lst[k] = r[j]
            j += 1
            k += 1
    return lst

# OPDRACHT 6
def gem_berekenen(lst):
    total = 0
    for item in lst:
        total += item
    return 0 if len(lst) == 0 else total / len(lst)

# OPDRACHT 7
def random_getal_spel():
    threshold = None
    while threshold is None:
        try:
            threshold = int(input('Grens? '))
        except ValueError:
            print('Voer aub een getal in.')
    n = randint(1, threshold)
    while True:
        guess = None
        while guess is None:
            try:
                guess = int(input('Voer een getal in: '))
            except ValueError:
                print('Voer aub een getal in.')

        if n == guess:
            print(f'u heeft het getal {guess} geraden!')
            return

        print('Lager!') if n < guess else print('Hoger!')


# OPDRACHT 8
def lijst_compressie(file):
    new_file = open('compressed_file.txt', 'a')
    with open(file, 'r') as given_file:
        for line in given_file:
            stripped_line = line.strip()
            new_file.write(stripped_line)
    new_file.close()
    return new_file


# OPDRACHT 8 HELPER CODE
# with open('text.txt', 'a') as f:
#     f.write('\nDit een zin!')
#     f.write('Nog een zinnetje!')
#     f.write('dit is een halve \n\nzin!')
#     f.close()
#     lijst_compressie('text.txt')


# OPDRACHT 9
def cyclisch_verschuiven(ch, n):
    if n == 0:
        return ch
    return ch[n:] + ch[:n] if n > 0 else ch[n:] + ch[:n]

# OPDRACHT 10
def fibonaci_reeks(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci_reeks(n - 1) + fibonaci_reeks(n - 2)

# OPDRACHT 11
def caesarcijfer():
    tekst = input(str('Geef een tekst: '))
    new_tekst = ''
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    rot = None
    while rot is None:
        try:
            rot = int(input('Geef een rotatie: '))
        except ValueError:
            print('Voer aub een geldig nummer in')

    for karakter in tekst:
        if karakter.lower() in alfabet:
            n_index = alfabet.index(karakter.lower()) + rot % len(alfabet)
            new_tekst += alfabet[n_index].upper() if karakter.isupper() else alfabet[n_index]
        else:
            new_tekst += karakter
    return new_tekst

# OPDRACHT 12
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('fizzbuzz')
            continue
        if i % 3 == 0:
            print('fizz')
            continue
        if i % 5 == 0:
            print('buzz')
            continue
        print(i)
