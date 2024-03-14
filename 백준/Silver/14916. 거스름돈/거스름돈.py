# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
dp = [-1 for _ in range(n+10)]

dp[1] = -1
dp[2] = 1
dp[3] = -1
dp[4] = 2
dp[5] = 1
dp[6] = 3
dp[7] = 2
dp[8] = 4

for i in range(9, n+1):
    dp[i] = dp[i-5] + 1

print(dp[n])