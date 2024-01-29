# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(N, cards, iter):
    numOfCards = [0 for _ in range(10)]

    for card in cards:
        numOfCards[int(card)] = numOfCards[int(card)] + 1

    maxVal = max(numOfCards)
    numOfCards.reverse()

    print(f"#{iter} {9 - numOfCards.index(maxVal)} {maxVal}")

for i in range(T):
    N = int(input())
    cards = input()
    solve(N, cards, i + 1)