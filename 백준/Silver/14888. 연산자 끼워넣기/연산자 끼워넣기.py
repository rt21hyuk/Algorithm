import sys
from itertools import permutations

# sys.stdin = open("input.txt", "r")
minVal = float('inf')
maxVal = float('-inf')

# Input
n = int(input())
arr = list(map(int, input().split()))
operator_num = list(map(int, input().split())) # +, -, *, -
operator_list = ['+', '-', '*', '/']
operator = []

for k in range(len(operator_num)):
    for i in range(operator_num[k]):
        operator.append(operator_list[k])

def Solve():
    global minVal, maxVal

    for case in permutations(operator, n - 1):
        result = arr[0]
        for r in range(1, n):
            if case[r - 1] == '+':
                result = result + arr[r]
            elif case[r - 1] == '-':
                result = result - arr[r]
            elif case[r - 1] == '*':
                result = result * arr[r]
            elif case[r - 1] == '/':
                if result < 0:
                    result = -(abs(result) // arr[r])
                else:
                    result = result // arr[r]

        if(minVal > result):
            minVal = result
        if(maxVal < result):
            maxVal = result

Solve()
print(maxVal)
print(minVal)

