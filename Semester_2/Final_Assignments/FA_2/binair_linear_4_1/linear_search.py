def linear_search(arr, tar):
    for item in arr:
        print(f"Checking item: {item}")
        if item == tar:
            return True
    return False


mList = range(0, 20)
mTarget = int(input("Voer een getal in: "))
print(f"List does not contain target ({mTarget})") if not linear_search(mList, mTarget) else print(f"Found item {mTarget} in list!")
