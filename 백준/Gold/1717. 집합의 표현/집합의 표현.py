import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# sys.stdin = open('input.txt')

sumCommand = 0
printCommand = 1
n, commandNum = map(int, input().split())
parentList = [i for i in range(n + 1)]

def findParent(n):
    if parentList[n] != n:
        parentList[n] = findParent(parentList[n])
    return parentList[n]

def union(n1, n2):
    n1 = findParent(n1)
    n2 = findParent(n2)

    if n1 < n2:
        parentList[n2] = n1
    else:
        parentList[n1] = n2

def solve():
    for i in range(commandNum):
        command, num1, num2 = map(int, input().split())
        if command == sumCommand:
            union(num1, num2)
        else:
            if findParent(num1) == findParent(num2):
                print("YES")
            else:
                print("NO")
solve()
