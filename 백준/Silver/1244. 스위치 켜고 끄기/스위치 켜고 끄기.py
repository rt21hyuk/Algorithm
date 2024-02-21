# import sys
# sys.stdin = open("input.txt", "r")

boy = 1
girl = 2

def solve():
    for gender, idx in studentInfo:
        cur = idx-1

        if gender == boy:
            for i in range(cur, numOfSwitch, idx):
                switchList[i] = (switchList[i]+1) % 2
        else:
            i=1
            switchList[cur] = (switchList[cur]+1) % 2
            while cur-i >= 0 and cur+i < numOfSwitch:
                if switchList[cur-i] == switchList[cur+i]:
                    switchList[cur-i] = (switchList[cur-i]+1) % 2
                    switchList[cur+i] = (switchList[cur+i]+1) % 2
                    i=i+1
                else:
                    break

    for i in range(1, numOfSwitch+1):
        print(switchList[i-1], end=" ")
        if i % 20 == 0:
            print()

numOfSwitch = int(input())
switchList = list(map(int, input().split()))
numOfStudent = int(input())
studentInfo = [map(int, input().split()) for _ in range(numOfStudent)]
solve()