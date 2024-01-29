# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(N, numList, iter):
    min, max = 10000000, -1
    for i in range(N):
        if max < numList[i]:
            max = numList[i]
        if numList[i] < min:
            min = numList[i]

    print(f"#{iter} {max - min}")

for i in range(T):
    N = int(input())
    numberList = list(map(int, input().split()))
    solve(N, numberList, i + 1)