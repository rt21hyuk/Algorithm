import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

from collections import deque

di, dj = [-1, 0, 1, 0], [0, -1, 0, 1]

def bfs(ci, cj):
    q = deque([[ci, cj]])
    visited[ci][cj] = 1

    while q:
        i, j = q.popleft()

        for idx in range(4):
            ni, nj = i + di[idx], j + dj[idx]

            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue

            if visited[ni][nj] or maps[ni][nj] == 0:
                continue

            q.append([ni, nj])
            visited[ni][nj] = 1


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    maps = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        r, c = map(int, input().split())
        maps[r][c] = 1

    answer = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                answer += 1

    print(answer)
