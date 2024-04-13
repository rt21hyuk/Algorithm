# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
wines = [0 for _ in range(n+10)]
for i in range(1, n+1):
    wines[i] = int(input())
dp = [0 for _ in range(n+10)]

dp[1] = wines[1]
dp[2] = wines[1] + wines[2]
dp[3] = max(wines[1] + wines[2], wines[1] + wines[3], wines[2] + wines[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i])

print(dp[n])