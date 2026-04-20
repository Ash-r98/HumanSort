def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lower = []
    higher = []
    for item in arr[1:]:
        if item < pivot:
            lower.append(item)
        else:
            higher.append(item)
    return quickSort(lower) + [pivot] + quickSort(higher)