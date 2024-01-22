import sys
#sys.stdin = open("input.txt", "r")

n = int(input())
answer = 0
queen = [0 for _ in range(n)]

def check(x):
    for i in range(x): # n까지 아님
        if queen[i] == queen[x]:
            return False
        
        if abs(queen[i] - queen[x]) == abs(i - x):
            return False
        
    return True

def DFS(x):
    global answer
    if x == n:
        answer = answer + 1
    else:
        for i in range(n):
            queen[x] = i
            if check(x) == True:
                DFS(x + 1)

def solve():
    DFS(0)
    print(answer)

solve()