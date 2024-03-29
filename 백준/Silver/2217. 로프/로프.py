import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

n = int(input())
rope = [0] * n

for i in range(n):
    rope[i] = int(input())
rope.sort()

maxWeight = float('-inf')

for numOfRope in range(1, n+1):
    curWeight = rope[n-numOfRope] * numOfRope
    maxWeight = max(curWeight, maxWeight)

print(maxWeight)