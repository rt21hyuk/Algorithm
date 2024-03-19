# import sys
# sys.stdin = open('input.txt')

blackHole = -1
blank = 0

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
direction = {"u": 0, "r": 1, "d": 2, "l": 3}

# go[blockNum][공이 오는 방향]으로 튕기는 방향 알 수 있음
go = [[],
      ["r", "u", "d", "l"],
      ["u", "d", "r", "l"],
      ["u", "r", "l", "d"],
      ["l", "r", "d", "u"],
      ["u", "r", "d", "l"]]

def bounce(blockNum, bi, bj, pi, pj):
    if bj == pj:
        if bi > pi: # 공이 위에서
            return go[blockNum][0]
        elif bi < pi: # 공이 아래에서
            return go[blockNum][2]
    if bi == pi:
        if bj < pj: # 공이 왼쪽에서
            return go[blockNum][1]
        elif bj > pj: # 공이 오른쪽에서
            return go[blockNum][3]

def warf(ci, cj):
    for idx in range(len(warfList)):
        if warfList[idx][0][0] == ci and warfList[idx][0][1] == cj:
            return warfList[idx][1][0], warfList[idx][1][1]
        elif warfList[idx][1][0] == ci and warfList[idx][1][1] == cj:
            return warfList[idx][0][0], warfList[idx][0][1]

def play(ci, cj, dir):
    global maxScore
    si, sj = ci, cj
    score = 0
    while(1):
        ni, nj = ci + di[dir], cj + dj[dir]

        if ni < 0 or nj < 0 or ni >= n or nj >= n: # 벽이면
            dir = direction[bounce(5, ni, nj, ci, cj)]
            score += 1
            ci, cj = ni, nj
            continue

        if area[ni][nj] == blackHole or (ni == si and nj == sj): # blackHole이거나 돌아오면
            maxScore = max(score, maxScore)
            return

        if area[ni][nj] == blank: # blank 면
            ci, cj = ni, nj
            continue

        if 1 <= area[ni][nj] <= 5: # block이면
            dir = direction[bounce(area[ni][nj], ni, nj, ci, cj)]
            ci, cj = ni, nj
            score += 1
            continue

        if 6 <= area[ni][nj] <= 10: # wormHole이면
            ci, cj = warf(ni, nj)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    maxScore = 0
    warfList = [[] for _ in range(5)]

    for i in range(n):
        for j in range(n):
            if 6 <= area[i][j] <= 10:
                warfList[area[i][j]-6].append([i, j])

    for i in range(n):
        for j in range(n):
            for dir in range(4):
                if area[i][j] == blank:
                    play(i, j, dir)

    print(f"#{tc} {maxScore}")