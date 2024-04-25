di = [1,0,-1,0]
dj = [0,1,0,-1]
def dfs(i,j):
    global area, idx
    visited[i][j] = True
    area += 1
    # print(i,j)
    path[idx].append((i,j))
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj]:
            if MAP[i][j][d] == '1':
                continue
            dfs(ni,nj)

W, H = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(H)]
visited = [[False]*W for _ in range(H)]
cnt = 0
MAX_area = 0
idx = 0
for i in range(H):
    for j in range(W):
        MAP[i][j] = bin(MAP[i][j])[2:].zfill(4)

path = [[] for _ in range(2500)]
area_lst = []

for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        area = 0
        dfs(i,j)
        # MAX_area = max(MAX_area, area)
        area_lst.append(area)
        idx += 1
        cnt += 1

print(cnt)
print(max(area_lst))

wall_area = 0
for i in range(len(area_lst)-1):
    for j in range(i+1,len(area_lst)):
        for s in range(area_lst[i]):
            for e in range(area_lst[j]):
                if path[i][s][0] == path[j][e][0] and abs(path[i][s][1] - path[j][e][1]) == 1:
                    wall_area = max(wall_area, area_lst[i] + area_lst[j])
                if path[i][s][1] == path[j][e][1] and abs(path[i][s][0] - path[j][e][0]) == 1:
                    wall_area = max(wall_area, area_lst[i] + area_lst[j])

print(wall_area)