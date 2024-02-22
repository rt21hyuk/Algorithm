import sys
# sys.stdin = open("input.txt")

import copy
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

n, m = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
year = 0

def bfs(ci, cj):
    q = deque([[ci, cj]])
    visited[ci][cj] = 1

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if visited[ni][nj] == 1 or area[ni][nj] == 0:
                continue
            q.append([ni, nj])
            visited[ni][nj] = 1

def nextYear():
    global area
    nextArea = copy.deepcopy(area)

    for i in range(n):
        for j in range(m):
            if area[i][j] != 0:
                sea = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if ni < 0 or nj < 0 or ni >= n or nj >= m:
                        continue
                    if area[ni][nj] == 0:
                       sea = sea + 1
                if area[i][j] - sea > 0:
                    nextArea[i][j] = area[i][j] - sea
                else:
                    nextArea[i][j] = 0
    area = nextArea

while 1:
    cnt = 0
    visited = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and area[i][j] != 0:
                bfs(i, j)
                cnt = cnt + 1

    if cnt == 0:
        print(0)
        break
    elif cnt > 1:
        print(year)
        break
    nextYear()
    year = year + 1