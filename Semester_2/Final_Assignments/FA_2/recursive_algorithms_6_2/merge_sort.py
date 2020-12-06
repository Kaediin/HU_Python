array = [14, 7, 3, 1, 9, 11, 6, 2]


def merge_sort(arr):
    if len(arr) > 1:
        # Divide
        q = len(arr) // 2

        p = arr[:q]

        r = arr[q:]

        merge_sort(p)

        merge_sort(r)

        i, j, k = 0, 0, 0

        # Combine
        while i < len(p) and j < len(r):
            if p[i] < r[j]:
                arr[k] = p[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(p):
            arr[k] = p[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    return arr


print(merge_sort(array))
