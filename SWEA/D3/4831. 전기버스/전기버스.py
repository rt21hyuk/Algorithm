# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(K, N, M, stopList, iter):
    cur, curIdx, answer = 0, 0, 0
    next = cur

    while(cur + K < N):
        while(curIdx < M and cur < stopList[curIdx] <= cur + K):
            next = stopList[curIdx]
            curIdx = curIdx + 1
        answer = answer + 1

        if(cur == next):
            print(f"#{iter} {0}")
            return

        cur = next

    print(f"#{iter} {answer}")

for i in range(T):
    K, N, M = map(int, input().split())
    stopList = list(map(int, input().split()))
    solve(K, N, M, stopList, i + 1)