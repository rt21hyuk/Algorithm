import sys
# sys.stdin = open("input.txt", "r")

startNum, targetNum = map(int, input().split())
minDepth = int(1e10)
flag = False

def DFS(num, depth):
    global minDepth, flag
    
    if(num == targetNum):
        minDepth = min(depth, minDepth)
        return

    if(num > targetNum):
        return

    nextNum1 = int(str(num) + '1')
    nextNum2 = num * 2

    DFS(nextNum1, depth + 1)
    DFS(nextNum2, depth + 1)
    
def solve():
    global minDepth

    if(startNum == targetNum):
        minDepth = 1
        print(minDepth)

    DFS(startNum, 1)

solve()

if(minDepth == 1e10):
    print(-1)
else:
    print(minDepth)