# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
numList = []
for _ in range(n):
    numList.append(int(input()))
numList.sort()

total = 0

def calMinus():
    global total
    for i in range(0, n-1, 2):
        # print(i, i + 1)
        if numList[i] <= 0 and numList[i + 1] <= 0:
            total += numList[i] * numList[i + 1]
        elif numList[i] <= 0 and numList[i + 1] > 0:
            total += numList[i]
            return
        elif numList[i] > 0:
            return

    if n % 2 == 1 and numList[n-1] < 0:
        total += numList[n-1]

def calPlus():
    global total

    for i in range(n-1, 0, -2):
        # print(i-1, i)
        if numList[i-1] > 1 and numList[i] > 1:
            total += numList[i-1] * numList[i]
        elif numList[i-1] >= 0 and numList[i] >= 0:
            total += numList[i-1] + numList[i]
        elif numList[i-1] < 0 and numList[i] >= 0:
            total += numList[i]
            return
        elif numList[i] < 0:
            return

    if n % 2 == 1 and numList[0] > 0:
        total += numList[0]

calMinus()
# print(total)

calPlus()
print(total)
