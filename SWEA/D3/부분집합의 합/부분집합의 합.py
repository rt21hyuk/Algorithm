# import sys
# sys.stdin = open('input.txt')
 
T = int(input())
 
def solve(N, K, mySet, iter):
    cnt = 0
    for i in range(1 << 12):
        total = len = 0
        for j in range(12):
            if i & (1 << j):
                total = total + mySet[j]
                len = len + 1
        if len == N and total == K:
            cnt = cnt + 1
 
    print(f"#{iter} {cnt}")
 
for i in range(T):
    N, K = map(int, input().split())
    mySet = [i for i in range(1, 13)]
    solve(N, K, mySet, i + 1)