import sys
# sys.stdin = open("input.txt", "r")

N, H = map(int, input().split())
obsUp = []
obsDown = []

def binarySearchDown(obsList, x):
    left, right = 0, N // 2 - 1
    while(left <= right):
        mid = (left + right) // 2
        if(obsList[mid] <= x):
            left = mid + 1
        else:
            right = mid - 1
    return N // 2 - left

# Input
for i in range(N):
    barrier = int(input())
    if(i % 2 == 0):
        obsDown.append(barrier)
    else:
        obsUp.append(barrier)
obsUp.sort()
obsDown.sort()

def solve():
    obsMinNum = N
    obsMinCount = 0

    for h in range(1, H + 1):
        obsUpNum = binarySearchDown(obsUp, H - h)
        obsDownNum = binarySearchDown(obsDown, h - 1)
        obsTotalNum = obsUpNum + obsDownNum

        if(obsTotalNum < obsMinNum):
            obsMinNum = obsTotalNum
            obsMinCount = 1
        
        elif(obsTotalNum == obsMinNum):
            obsMinCount = obsMinCount + 1

    print(obsMinNum, obsMinCount)
solve()