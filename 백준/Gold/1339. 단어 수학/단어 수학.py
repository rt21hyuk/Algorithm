# import sys
# sys.stdin = open('input.txt')

N = int(input())
alphaList = [0 for i in range(26)]
alphaNum = 0
for _ in range(N):
    tempStr = input()
    tempStrLen = len(tempStr)

    for idx, char in enumerate(tempStr):
        alphaIdx = ord(char) - ord('A')
        alphaPower = tempStrLen - idx - 1
        alphaList[alphaIdx] = alphaList[alphaIdx] + pow(10, alphaPower)

for alpha in alphaList:
    if alpha != 0:
        alphaNum = alphaNum + 1

def solve():
    global alphaList
    total, cur = 0, 9
    for _ in range(alphaNum): # reverse 필요
        maxVal = max(alphaList)
        total = total + maxVal * cur
        alphaList.remove(maxVal)
        cur = cur - 1

    print(total)

solve()
