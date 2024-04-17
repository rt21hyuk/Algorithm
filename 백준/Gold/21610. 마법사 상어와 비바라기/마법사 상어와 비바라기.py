import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

di = [0, -1, -1, -1, 0, 1, 1, 1] # ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 8방향 탐색
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

def moveClouds(dir, cnt):
    global movedClouds
    movedClouds = set() # 이동한 비구름 set를 초기화

    for cloud in clouds:
        ci, cj = cloud.split(',') # 'ci,cj'로 이루어진 cloud(문자열)에서 ci, cj를 뽑아냄
        ni, nj = int(ci) + di[dir]*cnt, int(cj) + dj[dir]*cnt # ni, nj를 계산

        # 좌표가 맵을 벗어나면 연결된 지점으로 이동
        while ni < 0:
            ni = n + ni
        while ni >= n:
            ni = ni - n
        while nj < 0:
            nj = n + nj
        while nj >= n:
            nj = nj - n

        movedClouds.add(str(ni)+','+str(nj)) # 이동한 비구름 set에 추가


def rain():
    for cloud in movedClouds: # 비구름이 있는 곳에 물++
        ci, cj = cloud.split(',')
        maps[int(ci)][int(cj)] += 1

def waterCopy():
    for cloud in movedClouds:
        cnt = 0
        ci, cj = cloud.split(',') # 현재 좌표
        for idx in range(1, 8, 2): # 대각선 인덱스
            ni, nj = int(ci) + di[idx], int(cj) + dj[idx] # ni, nj가 유효한 좌표이고, 대각선에 물이 있으면 물++
            if ni < 0 or nj < 0 or ni >=n or nj >= n:
                continue
            if maps[ni][nj] == 0:
                continue
            cnt += 1

        maps[int(ci)][int(cj)] += cnt # 해당 좌표에 물 복사


def createClouds():
    global clouds
    clouds = set()

    for i in range(n): # 비구름이 존재했던 곳이 아니고, 물 양이 2이상이라면 -> 물의 양 2를 빼고 구름을 생성
        for j in range(n):
            if maps[i][j] >= 2 and (str(i)+','+str(j)) not in movedClouds:
                clouds.add((str(i)+','+str(j)))
                maps[i][j] -= 2


def calculationWater(): # 물의 양의 합 계산
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += maps[i][j]
    return answer


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(m)]
clouds = set()
movedClouds = set()

for i in range(n-2, n): # 초기 비구름 (n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1) 생성
    clouds.add(str(i)+','+str(0))
    clouds.add(str(i)+','+str(1))

for idx in range(m):
    moveClouds(moves[idx][0]-1, moves[idx][1]) # 구름 이동
    rain() # 비 내리기
    waterCopy() # 물복사 마법
    createClouds() # 비구름 생성

print(calculationWater()) # 물의 양의 합 출력