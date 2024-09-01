import sys
# sys.stdin = open('input.txt', 'r')

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] # 파이프의 끝 개수

def solve():
    dp[0][0][1] = 1
    for i in range(2, n):
        if area[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]
    for r in range(1, n):
        for c in range(1, n):
            if area[r][c] == 0 and area[r][c-1] == 0 and area[r-1][c] == 0:
                dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

            if area[r][c] == 0:
                dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
                dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]
    print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])

solve()
