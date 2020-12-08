# import math
#
# def search(array, target):
#     n = len(array)
#     min_index = 0
#     max_index = n - 1
#     while True:
#         guess = math.ceil((min_index + max_index) / 2)
#         if array[guess] == target:
#             return guess
#         elif array[guess] < target:
#             # print(f"Guessed index wrong ({guess}). Going higher!")
#             min_index = guess + 1
#         else:
#             # print(f"Guessed index wrong ({guess}). Going lower!")
#             max_index = guess - 1
def search(array, target):
    min_index = 0
    max_index = len(array) - 1
    found = False
    while min_index <= max_index and not found:
        mid = (min_index + max_index) // 2
        print(mid)
        if array[mid] == target:
            found = mid
        else:
            if target < array[mid]:
                max_index = mid - 1
            else:
                min_index = mid + 1
    return found
