# import sys
# sys.stdin = open('input.txt')

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def check(ci, cj):
    cnt = 0
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if ni < 0 or nj < 0 or ni >= n or nj >= m:
            cnt += 1
        elif area[ni][nj] == ".":
            cnt += 1
    if cnt >= 3:
        sink.append([ci, cj])

n, m = map(int, input().split())
area = [list(input()) for _ in range(n)]
newArea = []
sink = []

for i in range(n):
    for j in range(m):
        if area[i][j] == "X":
            check(i, j)

if sink:
    for i, j in sink:
        area[i][j] = "."

x1, y1 = m-1, n-1
x2, y2 = 0, 0

# 지도 범위 구하기
for i in range(n):
    if 'X' in area[i]:
        y1 = min(y1, i)
        y2 = max(y2, i)

for j in range(m):
    for i in range(y1, y2+1):
        if area[i][j] == "X":
            x1 = min(x1, j)
            x2 = max(x2, j)
            break

# 정답 출력
for i in range(y1, y2+1):
    for j in range(x1, x2+1):
        print(area[i][j], end="")
    print()