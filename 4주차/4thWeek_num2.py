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


arr = [3,2,1,5,6,4]
order = 2

print(quick_sort(arr))

print(quick_sort(arr)[len(quick_sort(arr)) - order])