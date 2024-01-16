import sys
# sys.stdin = open("input.txt", "r")
maxVal = float('-inf')

n = int(input())
arr = list(map(int, input().split()))

dp = [-10000] * n

dp[0] = arr[0]
maxVal = dp[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
    maxVal = max(dp[i], maxVal)

print(maxVal)