# import sys
# sys.stdin = open('input.txt')

n = int(input())
dp = [1] * (n+10)

# 0은 상근, 1은 창영
dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4, n+1):
    if dp[i-3] != 0 or dp[i-1] != 0:
        dp[i] = 0

if dp[n] == 0:
    print("SK")
else:
    print("CY")