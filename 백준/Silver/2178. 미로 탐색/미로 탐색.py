import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

from collections import deque

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bfs():
    q = deque([[0, 0, 1]])
    visited[0][0] = 1
    while q:
        i, j, cnt = q.popleft()
        if i == n-1 and j == m-1:
            return cnt

        for idx in range(4):
            ni, nj = i + di[idx], j + dj[idx]
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if visited[ni][nj] or area[ni][nj] == '0':
                continue
            q.append([ni, nj, cnt+1])
            visited[ni][nj] = 1


n, m = map(int, input().split())
area = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
print(bfs())
