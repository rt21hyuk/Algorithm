# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    hexList = input()
    numList = []
    hexSet = set()

    for r in range(n//4): # 회전
        tempHexList = hexList[n-1:] + hexList[:n-1]

        for i in range(0, n, n//4):
            hexSet.add(tempHexList[i:i+n//4])
        hexList = tempHexList

    for num in hexSet:
        numList.append(int(num, 16))
    numList.sort(reverse=True)

    print(f'#{tc} {numList[k-1]}')