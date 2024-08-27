import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

n = m = 0
edges = [[] for _ in range(n)]
redges = [[] for _ in range(n)]

def dijkstra(start, dest, edges):
    q = []
    heappush(q, (0, start))
    minCost = [float('inf') for _ in range(n)]
    minCost[start] = 0

    while q:
        curCost, curNode = heappop(q)
        if curNode == dest:
            break
        if minCost[curNode] < curCost:
            continue
        for nextNode in edges[curNode]:
            edge, cost = nextNode[0], nextNode[1]
            if cost + curCost < minCost[edge]:
                minCost[edge] = cost + curCost
                heappush(q, (cost+curCost, edge))
    return minCost

def bfs(minCost):
    global redges
    q = deque([dest])

    while q:
        cur = q.popleft()
        # if cur == start:
        #     return
        for idx in range(len(redges[cur])-1, -1, -1):
            prev, cost = redges[cur][idx]
            if minCost[prev] + cost == minCost[cur]:
                q.append(prev)
                del redges[cur][idx]

def solve():
    global n, m, start, dest, edges, redges
    while 1:
        n, m = map(int, input().split())
        edges = [[] for _ in range(n)]
        redges = [[] for _ in range(n)]
        if n == 0 and m == 0:
            return
        start, dest = map(int, input().split())
        for _ in range(m):
            u, v, p = map(int, input().split())
            edges[u].append((v, p))
            redges[v].append((u, p))
        minCost = dijkstra(start, dest, edges)
        if minCost[dest] == float('inf'):
            print(-1)
            continue
        bfs(minCost)
        minCost = dijkstra(dest, start, redges)
        print(minCost[start] if minCost[start] < float('inf') else -1)

solve()