import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def push(n):
    stack.append(n)

def pop():
    if stack:
        return stack.pop()
    return -1

def size():
    return len(stack)

def empty():
    if stack:
        return 0
    return 1

def top():
    if stack:
        return stack[-1]
    else:
        return -1

n = int(input())

stack = []

for _ in range(n):
    command, *n = map(str, input().split())
    if n:
        n = int(n[0])

    if command == 'push':
        push(n)
    elif command == 'pop':
        print(pop())
    elif command == 'top':
        print(top())
    elif command == 'empty':
        print(empty())
    else:
        print(size())