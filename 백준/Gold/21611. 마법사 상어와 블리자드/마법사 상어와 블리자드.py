# import sys
# sys.stdin = open('input.txt', 'r')

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
areaNum = [[0 for _ in range(n)] for _ in range(n)]
actions = [list(map(int, input().split())) for _ in range(m)]
delete = [False for _ in range(n*n)]
coords = []
shark = (n//2, n//2)
score = [0, 0, 0, 0]

def changeDir(dir):
    if dir == 1: return 3
    if dir == 2: return 4
    if dir == 3: return 2
    if dir == 4: return 1

def makeArea():
    r, c = shark
    moveCnt = 1
    num = 0
    dir = 3

    areaNum[r][c] = num
    coords.append(shark)
    num += 1

    while 1:
        for _ in range(2):
            for _ in range(moveCnt):
                r += dr[dir]
                c += dc[dir]
                areaNum[r][c] = num
                coords.append((r, c))
                num += 1
            dir = changeDir(dir)
        moveCnt += 1

        if moveCnt == n:
            for _ in range(moveCnt):
                r += dr[dir]
                c += dc[dir]
                areaNum[r][c] = num
                coords.append((r, c))
                num += 1
            break

def blizzardMagic(idx):
    global delete
    delete = [False for _ in range(n * n)]

    dir = actions[idx][0]
    dist = actions[idx][1]

    r, c = shark
    for _ in range(dist):
        r += dr[dir]
        c += dc[dir]
        # print(areaNum[r][c])
        delete[areaNum[r][c]] = True

def moveMarble():
    flag = False
    cnt = 0
    for i in range(1, n*n):
        if delete[i] == True:
            flag = True
            cnt += 1
        else:
            if area[coords[i][0]][coords[i][1]] == 0:
                for j in range(1, cnt+1):
                    area[coords[i-j][0]][coords[i-j][1]] = 0
                flag = False
                break
            else:
                area[coords[i-cnt][0]][coords[i-cnt][1]] = area[coords[i][0]][coords[i][1]]

    if flag == True:
        i = n*n - 1
        for j in range(cnt):
            area[coords[i][0]][coords[i][1]] = 0
            i -= 1

def explodeMarble():
    global delete
    delete = [False for _ in range(n * n)]

    flag = False
    curMarble = area[coords[1][0]][coords[1][1]]
    seqCnt = 1
    startNum = 1

    for num in range(2, n*n):
        nextMarble = area[coords[num][0]][coords[num][1]]

        if nextMarble == 0:
            break

        if curMarble == nextMarble:
            seqCnt += 1
        else:
            if seqCnt >= 4:
                flag = True
                for i in range(startNum, num):
                    delete[i] = True
                score[curMarble] += seqCnt

            curMarble = nextMarble
            seqCnt = 1
            startNum = num

    if seqCnt >= 4:
        flag = True
        for i in range(startNum, n*n):
            delete[i] = True
        score[curMarble] += seqCnt

    return flag

def remakeArea():
    newArea = [[0 for _ in range(n)] for _ in range(n)]
    curMarble = area[coords[1][0]][coords[1][1]]
    cnt = 1
    posNum = 1
    flag = True

    for num in range(2, n*n):
        if posNum >= n*n:
            flag = False
            break

        nextMarble = area[coords[num][0]][coords[num][1]]
        if nextMarble == 0:
            break
        if curMarble == nextMarble:
            cnt += 1
        else:
            newArea[coords[posNum][0]][coords[posNum][1]] = cnt
            newArea[coords[posNum+1][0]][coords[posNum+1][1]] = curMarble
            curMarble = nextMarble
            cnt = 1
            posNum += 2

    if flag == True:
        if posNum != 1:
            newArea[coords[posNum][0]][coords[posNum][1]] = cnt
            newArea[coords[posNum+1][0]][coords[posNum+1][1]] = curMarble

    for i in range(n):
        for j in range(n):
            area[i][j] = newArea[i][j]

def solve():
    makeArea()
    for idx in range(m):
        blizzardMagic(idx)
        moveMarble()
        while(1):
            if explodeMarble() == False:
                break
            moveMarble()
        remakeArea()
    print(score[1] + 2*score[2] + 3*score[3])

solve()