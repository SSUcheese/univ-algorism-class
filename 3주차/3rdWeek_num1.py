def lineMaker(num):
    numSet = num[1:len(num)]
    for i in range(1, len(num) + 1):
        if i < len(num) + 1:
            for j in range(i, i + 2):
                if num[i] < num[j]:
                    temp = num[j]
                    num[i] = temp
                    num[j] = num[i]


line = int(input("숫자를 넣으세요"))
numList = []
for i in range(1,line+1):
    if i >= 1:
        numList.append(int(input("숫자를 넣으세요")))


for i in range()