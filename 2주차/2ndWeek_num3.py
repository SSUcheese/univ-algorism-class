numRow = 5
a = []

for i in range(numRow):
    a.append([])
    a[i].append(1)

    for j in range(1, i):
        a[i].append(a[i-1][j-1] + a[i-1][j])

    if i > 0:
        a[i].append(1)

print(a)


