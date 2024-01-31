# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(N, M, arr, iter):
    maxSum = -1

    for i in range(N-M+1):
        for j in range(N-M+1):
            curSum = 0
            for di in range(M):
                for dj in range(M):
                    curSum = curSum + arr[i+di][j+dj]
            maxSum = max(maxSum, curSum)
            
    print(f"#{iter} {maxSum}")

for i in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solve(N, M, arr, i + 1)