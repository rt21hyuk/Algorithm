import sys
input = sys.stdin.readline

maxVal = 0

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]

def dfs(depth, r, c, val):
    global maxVal
    if depth == 4:
        maxVal = max(maxVal, val)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nc < 0 or nr >= n or nc >= m:
            continue
        if visited[nr][nc]:
            continue
        visited[nr][nc] = 1
        dfs(depth+1, nr, nc, val+area[nr][nc])
        visited[nr][nc] = 0

def findRemain(r, c):
    global maxVal

    nearValList =  []

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nc < 0 or nr >= n or nc >= m:
            continue
        nearValList.append(area[nr][nc])
    length = len(nearValList)
    if length == 4:
        nearValList.sort(reverse=True)
        nearValList.pop()
        maxVal = max(maxVal, sum(nearValList)+area[r][c])
    elif length == 3:
        maxVal = max(maxVal, sum(nearValList)+area[r][c])
    return

for r in range(n):
    for c in range(m):
        visited[r][c] = 1
        dfs(1, r, c, area[r][c])
        findRemain(r, c)
        visited[r][c] = 0
print(maxVal)