# import sys
# sys.stdin = open('input.txt')

nPole = 0
sPole = 1
clockWise = 1
counterClockWise = -1
upIdx = 0
rightIdx = 2
downIdx = 4
leftIdx = 6

gear = []
for _ in range(4):
    gear.append(list(input()))
K = int(input())
rotationList = []
doClockWise = [0, 0, 0, 0]
doCounterClockWise = [0, 0, 0, 0]
for _ in range(K):
    rotationList.append(list(map(int, input().split())))

def rotationClockWise(idx):
    temp = gear[idx].pop()
    gear[idx].insert(0, temp)

def rotationCounterClockWise(idx):
    temp = gear[idx].pop(0)
    gear[idx].append(temp)

def calPoint():
    total = 0
    for i in range(4):
        total = total + int(gear[i][0]) * pow(2, i)
    print(total)

def solve():
    iter = 0
    for elem in rotationList:
        iter = iter + 1
        doClockWise = [0, 0, 0, 0]
        doCounterClockWise = [0, 0, 0, 0]
        numOfGear = elem[0] - 1
        rotation = elem[1]
        if numOfGear == 0 or numOfGear == 3:
            curNumOfGear = numOfGear
            for i in range(numOfGear, 3 - numOfGear, pow(-1, numOfGear)):
                leftGearIdx = min(i, i + pow(-1, numOfGear))
                rightGearIdx = max(i, i + pow(-1, numOfGear))
                if(gear[leftGearIdx][rightIdx] != gear[rightGearIdx][leftIdx]):
                    if rotation == clockWise:
                        doClockWise[curNumOfGear] = 1
                        doCounterClockWise[curNumOfGear + pow(-1, numOfGear)] = 1
                    else:
                        doCounterClockWise[curNumOfGear] = 1
                        doClockWise[curNumOfGear + pow(-1, numOfGear)] = 1
                else:
                    if rotation == clockWise:
                        doClockWise[curNumOfGear] = 1
                    else:
                        doCounterClockWise[curNumOfGear] = 1
                    break
                curNumOfGear = curNumOfGear + pow(-1, numOfGear)
                rotation *= -1
        else:
            leftGearIdx = min(numOfGear, numOfGear + pow(-1, numOfGear))
            rightGearIdx = max(numOfGear, numOfGear + pow(-1, numOfGear))

            if (gear[leftGearIdx][rightIdx] != gear[rightGearIdx][leftIdx]):
                if rotation == clockWise:
                    doClockWise[numOfGear] = 1
                    doCounterClockWise[numOfGear + pow(-1, numOfGear)] = 1
                else:
                    doCounterClockWise[numOfGear] = 1
                    doClockWise[numOfGear + pow(-1, numOfGear)] = 1

            curNumOfGear = numOfGear
            for i in range(numOfGear, 2 + pow(-1, numOfGear+1) * numOfGear, pow(-1, numOfGear+1)):
                leftGearIdx = min(i, i + pow(-1, numOfGear+1))
                rightGearIdx = max(i, i + pow(-1, numOfGear+1))
                if(gear[leftGearIdx][rightIdx] != gear[rightGearIdx][leftIdx]):
                    if rotation == clockWise:
                        doClockWise[curNumOfGear] = 1
                        doCounterClockWise[curNumOfGear + pow(-1, numOfGear+1)] = 1
                    else:
                        doCounterClockWise[curNumOfGear] = 1
                        doClockWise[curNumOfGear + pow(-1, numOfGear+1)] = 1
                else:
                    if rotation == clockWise:
                        doClockWise[curNumOfGear] = 1
                    else:
                        doCounterClockWise[curNumOfGear] = 1
                    break
                curNumOfGear = curNumOfGear + pow(-1, numOfGear+1)
                rotation *= -1
        for i in range(4):
            if doClockWise[i] == 1:
                rotationClockWise(i)
            if doCounterClockWise[i] == 1:
                rotationCounterClockWise(i)
solve()
calPoint()