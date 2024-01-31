# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(N, numList, iter):
    minIdx, maxIdx = -1, -1
    minVal, maxVal = 100, -1

    for i, num in enumerate(numList):
        if num < minVal:
            minVal = num
            minIdx = i

        if maxVal <= num:
            maxVal = num
            maxIdx = i

    print(f"#{iter} {abs(maxIdx - minIdx)}")

for i in range(T):
    N = int(input())
    numList = list(map(int, input().split()))
    solve(N, numList, i + 1)