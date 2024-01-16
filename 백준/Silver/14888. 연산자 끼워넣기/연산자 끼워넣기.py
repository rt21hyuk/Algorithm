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

def dfs(depth, result, plus, minus, multiply, divide):
    global minVal, maxVal, operator_num

    if depth == n:
        maxVal = max(result, maxVal)
        minVal = min(result, minVal)
        return
    
    if plus > 0:
        dfs(depth + 1, result + arr[depth], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(depth + 1, result - arr[depth], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(depth + 1, result * arr[depth], plus, minus, multiply - 1, divide)
    if divide > 0:
        if result < 0:
            dfs(depth + 1, - (abs(result) // arr[depth]), plus, minus, multiply, divide - 1) # - abs(result) // arr[depth] -> (X)
        else:
            dfs(depth + 1, result // arr[depth], plus, minus, multiply, divide - 1)

dfs(1, arr[0], operator_num[0], operator_num[1], operator_num[2], operator_num[3])
print(maxVal)
print(minVal)

# import sys
# from itertools import permutations

# # sys.stdin = open("input.txt", "r")
# minVal = float('inf')
# maxVal = float('-inf')

# # Input
# n = int(input())
# arr = list(map(int, input().split()))
# operator_num = list(map(int, input().split())) # +, -, *, -
# operator_list = ['+', '-', '*', '/']
# operator = []

# for k in range(len(operator_num)):
#     for i in range(operator_num[k]):
#         operator.append(operator_list[k])

# def Solve():
#     global minVal, maxVal

#     for case in permutations(operator, n - 1):
#         result = arr[0]
#         for r in range(1, n):
#             if case[r - 1] == '+':
#                 result = result + arr[r]
#             elif case[r - 1] == '-':
#                 result = result - arr[r]
#             elif case[r - 1] == '*':
#                 result = result * arr[r]
#             elif case[r - 1] == '/':
#                 if result < 0:
#                     result = -(abs(result) // arr[r])
#                 else:
#                     result = result // arr[r]

#         if(minVal > result):
#             minVal = result
#         if(maxVal < result):
#             maxVal = result

# Solve()
# print(maxVal)
# print(minVal)
