import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

airPurifier = -1
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1] # 상 우 하 좌

def diffusion():
    global maps
    nextMaps = [[0 for _ in range(col)] for _ in range(row)] # 다음 격자판

    for r in range(row):
        for c in range(col):
            if maps[r][c] > 0: # 미세먼지가 있으면
                count, dust = 0, maps[r][c]

                for idx in range(4):
                    nr, nc = r + dr[idx], c + dc[idx]
                    if nr < 0 or nc < 0 or nr >= row or nc >= col:
                        continue
                    if maps[nr][nc] == airPurifier:
                        continue
                    nextMaps[nr][nc] += dust//5
                    count += 1

                nextMaps[r][c] += dust - dust//5 * count # 인덱스의 리스트의 개수만큼 확산

            if maps[r][c] == airPurifier: # 공기청정기일 경우
                nextMaps[r][c] = airPurifier
    maps = nextMaps # maps를 업데이트


def operateAirPurifier():
    r, c = airPurifierPoint[0], 1 # 공기청정기 위 -> 반시계방향 회전 우 상 좌 하
    idx = 1 # 우부터 시작
    temp = 0
    while 1:
        nr, nc = r + dr[idx], c + dc[idx]
        if nr < 0 or nc < 0 or nr >= row or nc >= col: # 벽에 닿으면
            idx = (idx-1) % 4 # 반시계방향
            continue
        if r == airPurifierPoint[0] and c == 0: # 공기청정기로 돌아오면
            break

        maps[r][c], temp = temp, maps[r][c]
        r, c = nr, nc # 다음 좌표

    r, c = airPurifierPoint[1], 1  # 공기청정기 아래 -> 시계방향 회전 우 하 좌 상
    idx = 1  # 우부터 시작
    temp = 0
    while 1:
        nr, nc = r + dr[idx], c + dc[idx]
        if nr < 0 or nc < 0 or nr >= row or nc >= col:  # 벽에 닿으면
            idx = (idx + 1) % 4 # 시계방향
            continue
        if r == airPurifierPoint[1] and c == 0:  # 공기청정기로 돌아오면
            break
        maps[r][c], temp = temp, maps[r][c]
        r, c = nr, nc # 다음 좌표


def getFineDust():
    answer = 0
    for r in range(row):
        for c in range(col):
            if maps[r][c] > 0:
                answer += maps[r][c]
    return answer


row, col, time = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(row)]
airPurifierPoint = []


# 공기청정기의 좌표를 저장함
for r in range(row):
    if maps[r][0] == airPurifier:
        airPurifierPoint.append(r)
        airPurifierPoint.append(r+1)
        break

# time만큼 시뮬레이션
for t in range(time):
    diffusion() # 미세먼지 확산
    operateAirPurifier() # 공기청정기 작동

print(getFineDust()) # 방에 남아있는 미세먼지 양 계산