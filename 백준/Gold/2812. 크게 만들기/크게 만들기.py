import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
number = list(map(int, input().strip()))

stack = []

r = 0

for num in number:
    while r < k and stack:
        if stack[-1] < num:
            stack.pop()
            r += 1
        else:
            break
    stack.append(num)

while len(stack) > n-k:
    stack.pop()

print(''.join(list(map(str, stack))))