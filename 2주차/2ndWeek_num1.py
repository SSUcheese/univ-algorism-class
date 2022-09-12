def permutation(level):
    if level >= N:
        arr_list.append(arr.copy())
        return

    for i in range(N):
        if visited[i]: continue
        visited[i] = 1 # 사용 중
        arr[level] = a[i]
        permutation(level+1)
        arr[level] = 0
        visited[i] = 0 # 사용 해지


a = list(map(int, input().split()))

N = len(a)
visited = [0] * N
arr = [0] * N
arr_list = []

permutation(0)
print(arr_list)