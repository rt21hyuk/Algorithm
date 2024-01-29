# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(N, M, numList, iter):
    minVal, maxVal = 10000*100 + 1, -1

    for i in range(N - M + 1):
        sumVal = sum(numList[i:i+M])
        if maxVal < sumVal:
            maxVal = sumVal

        if sumVal < minVal:
            minVal = sumVal

    print(f"#{iter} {maxVal - minVal}")

for i in range(T):
    N, M = map(int, input().split())
    numberList = list(map(int, input().split()))
    solve(N, M, numberList, i + 1)