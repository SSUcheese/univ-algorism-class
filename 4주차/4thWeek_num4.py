red = 0
white = 1
blue = 2

nums = [2, 0, 2, 1, 1, 0]


def order(arr):
    for i in range(len(arr)):
        temp = arr[i]
        print(arr[i])
        for j in range(i + 1, len(arr)):
            if temp > arr[j]:
                arr[i] = arr[j]
                arr[j] = temp
            else:
                break
    return arr

print(nums)
print(order(nums))
