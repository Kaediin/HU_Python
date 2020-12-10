def binary_recursive(arr, target):
    q = len(arr) // 2
    if len(arr) == 1:
        return True if arr[q] == target else False
    elif arr[q] == target:
        return True
    else:
        if arr[q] < target:
            return binary_recursive((arr[q:]), target)
        else:
            return binary_recursive((arr[:q]), target)
