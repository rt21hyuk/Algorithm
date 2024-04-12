import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def dfs(depth, prev):
    if depth == k:
        print(*prev)
        return

    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth+1, prev + str(i))
            visited[i] = 0

n, k = map(int, input().split())
visited = [0 for _ in range(n+1)]

dfs(0, "")