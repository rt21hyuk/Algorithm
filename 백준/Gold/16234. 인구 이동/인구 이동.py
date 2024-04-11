# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bfs(ci, cj):
    q = deque([[ci, cj]])
    visited[ci][cj] = 1

    path = {(ci, cj)}
    total = area[ci][cj]

    while q:
        i, j = q.popleft()
        for idx in range(4):
            ni, nj = i + di[idx], j + dj[idx]

            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue

            if visited[ni][nj]:
                continue

            if l <= abs(area[ni][nj]-area[i][j]) <= r:
                path.add((ni, nj))
                visited[ni][nj] = 1
                q.append([ni, nj])
                total += area[ni][nj]

    for i, j in path:
        area[i][j] = total // len(path)


n, l, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
day = 0

while 1:
    prevArea = [arr[:] for arr in area]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)

    if prevArea == area:
        print(day)
        break

    day += 1