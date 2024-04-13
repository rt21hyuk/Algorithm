# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
steps = [0 for _ in range(n+10)]
for i in range(1, n+1):
    steps[i] = int(input())
dp = [0 for _ in range(n+10)]

dp[1] = steps[1]
dp[2] = steps[1] + steps[2]
dp[3] = max(steps[1] + steps[3], steps[2] + steps[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-2] + steps[i], dp[i-3] + steps[i-1] + steps[i])

print(dp[n])