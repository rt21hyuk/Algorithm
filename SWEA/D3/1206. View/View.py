#import sys

# sys.stdin = open('input.txt')

T = 10
dx = [-2, -1, 1, 2]

def solve(N, buildings, iter):
    total = 0
    for i in range(2, N - 2):
        minVal = 10000

        for j in range(4):
            curVal = buildings[i] - buildings[i + dx[j]]

            if curVal <= 0:
                minVal = 10000
                break

            if(curVal < minVal):
                minVal = curVal

        if(minVal != 10000):
            total = total + minVal

    print(f"#{iter} {total}")

for i in range(T):
    N = int(input())
    buildingList = list(map(int, input().split()))
    solve(N, buildingList, i + 1)