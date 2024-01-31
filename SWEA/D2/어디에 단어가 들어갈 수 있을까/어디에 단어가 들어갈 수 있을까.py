# import sys
# sys.stdin = open('input.txt')
 
T = int(input())
black = 0
white = 1
 
def calRow(N, K, arr):
    numOfWord = 0
    for i in range(N):
        for j in range(N-K+1):
            curVal = 0
            dj = 0
            if j-1 >= 0 and arr[i][j-1] == white:
                continue
 
            while(j + dj < N and arr[i][j+dj] == white):
                curVal = curVal + arr[i][j+dj]
                dj = dj + 1
 
            if curVal == K:
                numOfWord = numOfWord + 1
 
    return numOfWord
 
def calColumn(N, K, arr):
    numOfWord = 0
    for i in range(N):
        for j in range(N - K + 1):
            curVal = 0
            dj = 0
            if j - 1 >= 0 and arr[j - 1][i] == white:
                continue
 
            while (j + dj < N and arr[j + dj][i] == white):
                curVal = curVal + arr[j + dj][i]
                dj = dj + 1
 
            if curVal == K:
                numOfWord = numOfWord + 1
 
    return numOfWord
 
def solve(N, K, arr, iter):
    answer = calRow(N, K, arr) + calColumn(N, K, arr)
    print(f"#{iter} {answer}")
 
 
for i in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solve(N, K, arr, i + 1)