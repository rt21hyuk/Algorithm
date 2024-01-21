import sys
# sys.stdin = open("input.txt", "r")

cards = input()
cardNum = [0 for i in range(9)]

def solve():
    for card in cards:
        cardIndex = int(card)

        if cardIndex == 9:
            cardIndex = 6

        cardNum[cardIndex] = cardNum[cardIndex] + 1

    cardNum[6] = cardNum[6] // 2 + cardNum[6] % 2
    print(max(cardNum))

solve()
