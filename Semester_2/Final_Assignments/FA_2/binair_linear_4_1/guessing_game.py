from random import randint
from binair_linear_4_1 import binary_search
guessed = False
min = 0
max = 100
numbers = [i for i in range(min, max)]
target = int(input(f"Choose a number between {min} and {max}: "))

print(binary_search.search(numbers, target))