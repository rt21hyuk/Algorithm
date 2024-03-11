import sys
# input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def isVPS():
    answer = "NO"
    stack = []
    for char in myStr:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return "NO"

    if stack:
        return "NO"
    return "YES"

n = int(input())
for _ in range(n):
    myStr = input()
    print(isVPS())