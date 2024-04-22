import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def dfs(row, col):
    global answer
    if row == n+1 and col == 1:
        answer += 1
        return

    if col == m:
        nRow = row + 1
        nCol = 1
    else:
        nRow = row
        nCol = col + 1

    dfs(nRow, nCol)

    if squares[row-1][col-1] == 0 or squares[row][col-1] == 0 or squares[row-1][col] == 0:
        squares[row][col] = 1
        dfs(nRow, nCol)
        squares[row][col] = 0


n, m = map(int, input().split())
squares = [[0 for _ in range(m+1)] for _ in range(n+1)]
answer = 0
dfs(1, 1)

print(answer)