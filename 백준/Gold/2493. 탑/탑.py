# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
tower = list(map(int, input().split()))

stack = []
receive = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if stack[-1][0] > tower[i]:
            receive[i] = stack[-1][1]
            break
        else:
            stack.pop()

    stack.append((tower[i], i+1))

print(*receive)