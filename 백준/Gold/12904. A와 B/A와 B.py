import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

start = list(input().rstrip())
target = list(input().rstrip())

switch = False
while target:
    if target[-1] == 'A':
        target.pop()
    elif target[-1] == 'B':
        target.pop()
        target = target[::-1]
    if start == target:
        switch = True
        break

if switch:
    print(1)
else:
    print(0)