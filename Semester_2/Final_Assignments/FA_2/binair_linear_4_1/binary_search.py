def search(array, target):
    min_index = 0
    max_index = len(array) - 1
    found = False
    while min_index <= max_index and not found:
        mid = (min_index + max_index) // 2
        if array[mid] == target:
            found = mid
        elif target < array[mid]:
            max_index = mid - 1
        else:
            min_index = mid + 1
    return found
