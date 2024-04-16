# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
prices = sorted([int(input()) for _ in range(n)], reverse=True)

total = 0

for i in range(0, n//3):
    total += prices[3*i] + prices[3*i+1]

if n % 3 == 1:
    total += prices[-1]
elif n % 3 == 2:
    total += prices[-1] + prices[-2]

print(total)