def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser, equal, greater = [], [], []
    for i in arr:
        if i < pivot:
            lesser.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    return quick_sort(lesser) + equal + quick_sort(greater)


print(quick_sort([5, 7, 9, 0, 3, 1, 6, 2, 4, 8]))
