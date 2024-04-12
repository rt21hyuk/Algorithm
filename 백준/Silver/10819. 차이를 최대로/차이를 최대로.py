import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def dfs(cur):
    global maxTotal

    if cur == n:
        total = 0
        for i in range(1, n):
            total += abs(arr[i] - arr[i-1])
        maxTotal = max(total, maxTotal)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        arr[cur] = numList[i]
        dfs(cur+1)
        visited[i] = 0
        # arr[cur] = 0

n = int(input())
numList = list(map(int, input().split()))
arr = [0 for _ in range(n)]
visited = [0 for _ in range(n)]
maxTotal = 0
dfs(0)
print(maxTotal)