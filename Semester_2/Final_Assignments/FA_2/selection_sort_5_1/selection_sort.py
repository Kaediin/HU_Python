array = [1, 13, 19, 18, 4, 10]


def sel_sort(arr):
    for i in range(len(arr)):

        index = i
        for j in range(i + 1, len(arr)):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]

    return arr


print(sel_sort(array))
