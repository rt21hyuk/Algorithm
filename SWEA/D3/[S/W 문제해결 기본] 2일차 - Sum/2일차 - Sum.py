# import sys
# sys.stdin = open('input.txt')

T = 10
maxSum = -1

def maxCrossSum(arr):
    global maxSum
    curSum1 = 0
    curSum2 = 0
    for i in range(100):
        curSum1 = curSum1 + arr[i][i]
        curSum2 = curSum2 + arr[i][99-i]
    maxSum = max(maxSum, max(curSum1, curSum2))

def maxRowSum(arr):
    global maxSum
    for i in range(100):
        curSum = 0
        for j in range(100):
            curSum = curSum + arr[i][j]
        maxSum = max(maxSum, curSum)

def maxColumnSum(arr):
    global maxSum
    for i in range(100):
        curSum = 0
        for j in range(100):
            curSum = curSum + arr[j][i]
        maxSum = max(maxSum, curSum)

def solve(iter, arr):
    maxColumnSum(arr)
    maxRowSum(arr)
    maxCrossSum(arr)
    print(f"#{iter} {maxSum}")

for i in range(T):
    maxSum = -1
    iter = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    solve(iter, arr)