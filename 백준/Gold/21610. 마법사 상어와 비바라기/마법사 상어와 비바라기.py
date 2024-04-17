import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

def moveClouds(dir, cnt):
    global movedClouds
    movedClouds = set()

    for cloud in clouds:
        ci, cj = cloud.split(',')
        ni, nj = int(ci) + di[dir]*cnt, int(cj) + dj[dir]*cnt

        while ni < 0:
            ni = n + ni
        while ni >= n:
            ni = ni - n
        while nj < 0:
            nj = n + nj
        while nj >= n:
            nj = nj - n

        movedClouds.add(str(ni)+','+str(nj))


def rain():
    for cloud in movedClouds:
        ci, cj = cloud.split(',')
        maps[int(ci)][int(cj)] += 1

def waterCopy():
    for cloud in movedClouds:
        cnt = 0
        ci, cj = cloud.split(',')
        for idx in range(1, 8, 2):
            ni, nj = int(ci) + di[idx], int(cj) + dj[idx]
            if ni < 0 or nj < 0 or ni >=n or nj >= n:
                continue
            if maps[ni][nj] == 0:
                continue
            cnt += 1

        maps[int(ci)][int(cj)] += cnt


def createClouds():
    global clouds
    clouds = set()

    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 2 and (str(i)+','+str(j)) not in movedClouds:
                clouds.add((str(i)+','+str(j)))
                maps[i][j] -= 2


def calculationWater():
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

for i in range(n-2, n):
    clouds.add(str(i)+','+str(0))
    clouds.add(str(i)+','+str(1))

for idx in range(m):
    moveClouds(moves[idx][0]-1, moves[idx][1])
    rain()
    waterCopy()
    createClouds()

print(calculationWater())