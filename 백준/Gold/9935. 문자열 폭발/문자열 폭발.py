# import sys
# sys.stdin = open("input.txt", "r")

myStr = input()
bombStr = input()

stack = []
tempStack = []

for i in range(len(myStr)):
    stack.append(myStr[i])
    if myStr[i] == bombStr[-1] and len(stack) >= len(bombStr):
        temp = ""
        for j in range(len(bombStr)):
            temp = stack.pop() + temp
        if temp != bombStr:
            for i in range(len(bombStr)):
                stack.append(temp[i])

if not stack:
    print("FRULA")
else:
    for char in stack:
        print(char, end="")