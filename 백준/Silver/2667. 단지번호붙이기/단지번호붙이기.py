# import sys
# sys.stdin = open("input.txt", "r")

di, dj = [-1, 0, 1, 0], [0, -1, 0, 1]

def dfs(ci, cj):
    global cnt

    visited[ci][cj] = 1 # 방문처리
    cnt += 1 # 집의 개수

    for idx in range(4):
        ni, nj = ci + di[idx], cj + dj[idx]

        if ni < 0 or nj < 0 or ni >= n or nj >= n: # 영역 밖이면 continue
            continue
        if visited[ni][nj] or maps[ni][nj] == '0': # 방문했거나 집이 없으면 continue
            continue

        dfs(ni, nj) # ni, nj 탐색


n = int(input())
maps = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cntList = []


for i in range(n):
    for j in range(n):
        if maps[i][j] == '1' and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            cntList.append(cnt)


print(len(cntList))
for cnt in sorted(cntList):
    print(cnt)