import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

operators = {"+": lambda x,y: x+y,
       "-": lambda x,y: x-y,
       "*": lambda x,y: x*y,
        "/": lambda x,y: x/y}

def calPostfix():
    numStack = []
    for char in expression:
        if (char.isalpha()):
            numStack.append(alpha.get(char))
        elif (char in operators):
            operand2 = numStack.pop()
            operand1 = numStack.pop()
            result = operators[char](operand1, operand2)
            numStack.append(result)
    return numStack[-1]

NIL = -1
alpha = {chr(i): NIL for i in range(65, 91)}

n = int(input())
expression = input()

for i in range(n):
    alpha[chr(i+65)] = int(input())

# print(alpha)

print(f'{calPostfix():.2f}')