import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def dfs(depth, cost, start, prev):
    global minCost

    if depth == n:
        if costs[prev][start]:
            cost += costs[prev][start]
            minCost = min(cost, minCost)
        return

    for idx in range(n):
        if visited[idx] == 0 and costs[prev][idx]:
            visited[idx] = 1
            dfs(depth+1, cost+costs[prev][idx], start, idx)
            visited[idx] = 0


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
minCost = float('inf')


for start in range(n):
    visited[start] = 1
    dfs(1, 0, start, start)
    visited[start] = 0

print(minCost)