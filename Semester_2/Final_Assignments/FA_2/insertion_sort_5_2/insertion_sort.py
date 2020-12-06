array = [1, 2, 3, 4]
# array = [4, 2, 1, 3]


def ins_sort(arr):
    steps = 0
    for index in range(0, len(arr)):
        current_val = arr[index]
        current_pos = index
        steps += 1
        while current_pos > 0 and arr[current_pos - 1] > current_val:
            steps += 1
            arr[current_pos] = arr[current_pos - 1]
            current_pos -= 1
        arr[current_pos] = current_val

    print(steps)
    return arr

print(f"{ins_sort(array)}")

