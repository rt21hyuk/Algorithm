# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

n = int(input())
card = deque(i for i in range(1, n+1))

while len(card) > 1:
    if  card:
        card.popleft()

    if card:
        temp = card.popleft()
        card.append(temp)

print(card[0])