import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def dfs(depth, ci, cj):
    global maxDepth
    if maxDepth < depth:
        maxDepth = depth

    visited[ord(area[ci][cj]) - ord('A')] = 1

    for idx in range(4):
        ni, nj = ci + di[idx], cj + dj[idx]

        if ni < 0 or nj < 0 or ni >= n or nj >= m:
            continue

        next = ord(area[ni][nj]) - ord('A')

        if visited[next] == 0:
            visited[next] = 1
            dfs(depth+1, ni, nj)
            visited[next] = 0

maxDepth = 0
n, m = map(int, input().split())
area = [list(input()) for _ in range(n)]
visited = [0 for _ in range(26)]
dfs(1, 0, 0)

print(maxDepth)