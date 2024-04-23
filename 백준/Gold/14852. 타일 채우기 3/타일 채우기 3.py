# import sys
# sys.stdin = open("input.txt", "r")

modConst = 1000000007

n = int(input())

dp = [0 for _ in range(n+10)]
dp[1] = 2 # |, :
dp[2] = 7 # ||, ::, |:, :|, =, ㅛ, ㅠ
dp[3] = 22 # |||, :::, ||:, |:|, :||, ::|, |::, :|:, =|, |=, =:, :=, ㅛ|, ㅛ:, :ㅛ, |ㅛ, ㅠ|, ㅠ:, |ㅠ, :ㅠ, ∸⨪, ⨪∸

for i in range(4, n+1):
    dp[i] = (3*dp[i-1] + dp[i-2] - dp[i-3]) % modConst
print(dp[n])