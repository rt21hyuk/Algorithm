# import sys
# sys.stdin = open('input.txt')

T = 10

def solve(N, boxList, iter):
    minVal, maxVal = 0, 0
    answer = 0

    while(N > 0):
        minVal, maxVal = min(boxList), max(boxList)
        minIdx = boxList.index(minVal)
        maxIdx = boxList.index(maxVal)
        boxList[minIdx] = boxList[minIdx] + 1
        boxList[maxIdx] = boxList[maxIdx] - 1
        N = N - 1

    answer = max(boxList) - min(boxList)
    print(f"#{iter} {answer}")

for i in range(10):
    N = int(input())
    boxList = list(map(int, input().split()))
    solve(N, boxList, i + 1)