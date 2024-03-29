import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")

n = int(input())
connectList = [[] for _ in range(n+1)]

def dfs(node):
    for next in connectList[node]:
        if not visited[next]:
            visited[next] = node
            dfs(next)

for _ in range(n-1):
    n1, n2 = map(int, input().split())
    connectList[n1].append(n2)
    connectList[n2].append(n1)

root = 1
visited = [0] * (n+1)
visited[root] = root

dfs(root)

for idx in range(2, n+1):
    print(visited[idx])