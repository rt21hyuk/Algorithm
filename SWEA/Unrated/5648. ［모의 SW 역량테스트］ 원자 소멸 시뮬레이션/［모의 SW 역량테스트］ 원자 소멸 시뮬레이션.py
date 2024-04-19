# import sys
# sys.stdin = open("input.txt", "r")

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

def moveAtoms():
    global answer, remain

    atomsPoints = {} # 남은 원자들이 이동한 좌표
    atomsRemove = set() # 남아 있어 삭제해야할 원자 좌표

    for idx in range(n):
        live, cx, cy, dir, energy = atomsInfo[idx]

        if not live: # 이미 좌표 밖으로 넘어갔거나, 폭발했다면 넘어가기
            continue

        nx, ny = cx + dx[dir], cy + dy[dir]
        if nx < 0 or ny < 0 or nx >= 4000 or ny >= 4000: # 맵 밖으로 나가면 삭제
            remain -= 1
            atomsInfo[idx][0] = False
            continue

        atomsInfo[idx][1], atomsInfo[idx][2] = nx, ny

        if (nx, ny) in atomsPoints: # atomsPoints 위치에 원자가 있었다면
            prevAtomIdx = atomsPoints[(nx, ny)] # 이전에 있던 원자를 삭제
            answer += atomsInfo[prevAtomIdx][4]
            atomsInfo[prevAtomIdx][0] = False
            remain -= 1
            atomsRemove.add((nx, ny)) # 나중에 지우기 위해 atomsRemove에 이 좌표를 저장
            atomsPoints[(nx, ny)] = idx # atomsPoint 위치에 현재 원자의 idx를 저장
        else: # atomsPoints에 원자가 없으면
            atomsPoints[(nx, ny)] = idx

    for x, y in atomsRemove: # 모든 원자를 탐색하고 난 뒤, 원자가 충돌했다면 atomsRemove에 좌표가 저장됨
        atomIdx = atomsPoints[(x, y)] # 가장 마지막에 남아있던 원자 idx를 가져와서 삭제처리
        answer += atomsInfo[atomIdx][4]
        atomsInfo[atomIdx][0] = False
        remain -= 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    atomsInfo = []
    for _ in range(n):
        x, y, d, e = map(int, input().split())
        # 2차원 평면의 좌표가 -1000 <= x,y <= 1000, 오프셋(+1000)을 부여
        # 원자가 한 칸씩 이동하기 때문에 원자 좌표+1을 한다면, 충돌하지 않는 것처럼 계산됨 -> 좌표를 2배 키움 -> *2
        atomsInfo.append([True, x*2 + 2000, y*2 + 2000, d, e])
    remain, answer = n, 0 # 남아있는 원자 개수, 총 에너지 방출량

    while remain > 1: # 원자의 개수가 1개이하라면 더 이상 충돌할 수 없음
        moveAtoms()

    print(f'#{tc} {answer}')