# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
dp = [-1 for _ in range(n+20)]

dp[3] = 1
dp[4] = -1
dp[5] = 1
dp[6] = 2
dp[7] = -1
dp[8] = 2
dp[9] = 3
dp[10] = 2
dp[11] = 3
dp[12] = 4


for i in range(13, n+1):
    dp[i] = dp[i-5] + 1

print(dp[n])
