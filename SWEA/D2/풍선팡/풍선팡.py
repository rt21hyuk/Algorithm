# import sys
# sys.stdin = open('input.txt')
 
T = int(input())
 
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
 
def solve(N, M, arr, iter):
    maxSum = -1
    for i in range(N):
        for j in range(M):
            curSum = arr[i][j]
            for k in range(4 * arr[i][j]):
                ci = i + di[k % 4] * ((k + 4) // 4)
                cj = j + dj[k % 4] * ((k + 4) // 4)
 
                if(ci>=0 and cj>=0 and ci<N and cj<M):
                    curSum = curSum + arr[ci][cj]
            maxSum = max(maxSum, curSum)
 
    print(f"#{iter} {maxSum}")
 
for i in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solve(N, M, arr, i + 1)