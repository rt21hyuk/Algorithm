# import sys
# sys.stdin = open("input.txt", "r")

stack = []
res = 1
result = 0
bracket = list(input())

for i in range(len(bracket)):
    if bracket[i] == '(':
        res *= 2
        stack.append(bracket[i])
    if bracket[i] == '[':
        res *= 3
        stack.append(bracket[i])
    if bracket[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if bracket[i-1] == '(':
            result += res
        res //= 2
        stack.pop()
    if bracket[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if bracket[i-1] == '[':
            result += res
        res //= 3
        stack.pop()

if stack:
    result = 0

print(result)