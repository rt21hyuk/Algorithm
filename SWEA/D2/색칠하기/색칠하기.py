# import sys
# sys.stdin = open('input.txt')
 
T = int(input())
 
purple = 3
 
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
 
def paint(shape, arr):
    for i in range(shape[0], shape[2] + 1):
        for j in range(shape[1], shape[3] + 1):
            arr[i][j] = arr[i][j] + shape[4]
 
def calPurple(arr):
    total = 0
    for i in range(10):
        for j in range(10):
           if arr[i][j] == purple:
               total = total + 1
    return total
 
def solve(N, shapes, arr, iter):
    for i in range(N):
        paint(shapes[i], arr)
    answer = calPurple(arr)
    print(f"#{iter} {answer}")
 
for i in range(T):
    N = int(input())
    shapes = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0 for _ in range(10)] for _ in range(10)]
    solve(N, shapes, arr, i + 1)