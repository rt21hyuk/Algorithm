# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
numList = list(map(int,input().split()))
result = [-1] * n
stack = []
for i in range(n-1, -1, -1):
    while stack:
        if stack[-1] > numList[i]:
            result[i] = stack[-1]
            break
        elif stack[-1] <= numList[i]:
            stack.pop()
    stack.append(numList[i])

print(*result)