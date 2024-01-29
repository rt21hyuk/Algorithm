# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(N, boxesHeight, iter):
    answer = 0
    for i in range(N):
        cnt = 0
        for j in range(i + 1, N):
            if(boxesHeight[i] - boxesHeight[j] > 0):
                cnt = cnt + 1

        if(answer < cnt):
            answer = cnt

    print(f"#{iter} {answer}")

for i in range(T):
    N = int(input())
    boxesList = list(map(int, input().split()))
    solve(N, boxesList, i + 1)