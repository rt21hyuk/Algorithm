import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def dfs(depth, prev):
    if depth == m:
        print(*prev)
        return

    for i in range(n):
        if not prev or prev[-1] <= numList[i]:
            prev.append(numList[i])
            dfs(depth+1, prev)
            prev.pop()

n, m = map(int, input().split())
numList = list(set(map(int, input().split())))
n = len(numList)
numList.sort()
dfs(0, [])