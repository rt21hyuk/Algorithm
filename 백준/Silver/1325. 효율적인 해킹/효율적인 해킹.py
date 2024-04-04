import sys
input = sys.stdin.readline
from collections import deque
# sys.stdin = open("input.txt", "r")

def bfs(start):
    q = deque([start])
    visited[start] = 1
    cnt = 1

    while q:
        cur = q.popleft()
        for next in edge[cur]:
            if visited[next] == 0:
                visited[next] = 1
                q.append(next)
                cnt += 1
    return cnt

maxTotal = 0
comList = []
n, m = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    edge[node2].append(node1)

for i in range(1, n+1):
    visited = [0 for _ in range(n + 1)]
    curTotal = bfs(i)
    if maxTotal < curTotal:
        maxTotal = curTotal
        comList = [i]
    elif maxTotal == curTotal:
        comList.append(i)
comList.sort()
print(*comList)