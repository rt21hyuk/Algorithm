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
        # area[ci][cj] = "O"

n, m = map(int, input().split())
area = [list(input()) for _ in range(n)]
newArea = []
answer = 0
s, e = m, 0
sink = []

for i in range(n):
    for j in range(m):
        if area[i][j] == "X":
            check(i, j)
        # if j == m-1 and "X" in area[i]:
        #     newArea.append("".join(area[i]))

if sink:
    for i, j in sink:
        area[i][j] = "."

# for i in range(m):
#     for j in range(len(newArea)):
#         if newArea[j][i] == "X":
#             s = min(i, s)
#             e = max(i, e)
#             break
#
# for i in range(len(newArea)):
#     for j in range(s, e+1):
#         # if newArea[i][j] == "O":
#         #     print(".", end="")
#         # else:
#         print(newArea[i][j], end="")
#     print()

x1 = 0
y1 = m-1
x2 = 0
y2 = 0
# 지도 범위 구하기
for i in range(n):
    if 'X' in area[i]:
        x1 = i
        break
for i in range(n-1, -1, -1):
    if 'X' in area[i]:
        x2 = i
        break

for i in range(x1, x2+1):
    for j in range(m):
        if area[i][j] == 'X':
            y1 = min(y1, j)
            y2 = max(y2, j)

# 정답 출력하기
for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        print(area[i][j], end='')
    print()