# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(N, numList, iter):
    maxLen, curLen = 0, 0
    flag = False

    for i in range(N):
        if flag == False:
            if numList[i] == "1":
                flag = True
                curLen = curLen + 1
        else:
            if numList[i] == "0":
                flag = False
                curLen = 0

            elif numList[i] == "1":
                curLen = curLen + 1

        maxLen = max(curLen, maxLen)

    print(f"#{iter} {maxLen}")

for i in range(T):
    N = int(input())
    numList = input()
    solve(N, numList, i + 1)