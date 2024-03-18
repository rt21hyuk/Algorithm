# import sys
# sys.stdin = open('input.txt')

from collections import deque

def dfs(node):
    print(f"{node}", end=" ")
    visited1[node] = 1

    for next in edge[node]:
        if visited1[next] == 0:
            dfs(next)

def bfs(node):
    q = deque([node])
    visited2[node] = 1

    while q:
        cur = q.popleft()
        print(f"{cur}", end=" ")
        for next in edge[cur]:
            if visited2[next] == 0:
                q.append(next)
                visited2[next] = 1


n, m, s = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

for i in range(n+1):
    edge[i].sort()

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)
dfs(s)
print()
bfs(s)