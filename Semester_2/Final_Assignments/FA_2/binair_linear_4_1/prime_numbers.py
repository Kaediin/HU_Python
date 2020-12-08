from Semester_2.Final_Assignments.FA_2.binair_linear_4_1 import binary_search


def _input(message, in_type=str):
    while True:
        try:
            return in_type(input(message))
        except:
            pass


def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


number_of_items = int(input("Enter max number: "))
primes = [i for i in range(2, number_of_items + 1) if isPrime(i)]
target = 4
while not isPrime(target):
    target = _input("Pick a prime number as a target: ", int)

if target not in primes:
    print("The array is not large enough")
else:
    index = binary_search.search(primes, target)
    print(f"Target: {target} found at index {index}")
