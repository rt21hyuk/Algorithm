# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(cardList, iter):
    isBabyGin = "false"
    i = 0
    triNum, runNum = 0, 0

    while i < 10:
        if cardList[i] >= 3:
            cardList[i] = cardList[i] - 3
            triNum = triNum + 1
            continue

        if cardList[i] >= 1 and cardList[i+1] >= 1 and cardList[i+2] >= 1:
            cardList[i] = cardList[i] - 1
            cardList[i+1] = cardList[i+1] - 1
            cardList[i+2] = cardList[i+2] - 1
            runNum = runNum + 1
            continue

        i = i + 1

    if triNum + runNum == 2:
        isBabyGin = "true"

    print(f"#{iter} {isBabyGin}")

for i in range(T):
    N = int(input())
    cardList = [0] * 12

    for _ in range(6):
        cardList[N % 10] += 1
        N //= 10

    solve(cardList, i + 1)