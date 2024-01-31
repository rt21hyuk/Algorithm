# import sys
# sys.stdin = open('input.txt')

T = int(input())

primeNum = [2, 3, 5, 7, 11]

def solve(N, iter):
    primeNumList = [0 for _ in range(5)]
    cur = 0

    while(N > 1):
        if(N % primeNum[cur] == 0):
            N = N // primeNum[cur]
            primeNumList[cur] = primeNumList[cur] + 1
        else:
            cur = cur + 1

    print(f"#{iter} {primeNumList[0]} {primeNumList[1]} {primeNumList[2]} {primeNumList[3]} {primeNumList[4]}")

for i in range(10):
    N = int(input())
    solve(N, i + 1)