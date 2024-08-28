import sys
from heapq import heappop, heappush
# sys.stdin = open('input.txt', 'r')

n, m, k = map(int, input().split())
graph = [{} for _ in range(n+1)]
start, end = 1, n

def dijkstra():
    q = []
    heappush(q, (0, start, 0))
    minCost = [[float('inf')] * (k+1) for _ in range(n+1)]
    minCost[start][0] = 0

    while q:
        curCost, cur, count = heappop(q)

        if minCost[cur][count] < curCost:
            continue

        for next in graph[cur]:
            nextCost = curCost + graph[cur][next]

            if nextCost < minCost[next][count]:
                minCost[next][count] = nextCost
                heappush(q, (nextCost, next, count))

            if count < k and curCost < minCost[next][count + 1]:
                minCost[next][count + 1] = curCost
                heappush(q, (curCost, next, count + 1))

    print(min(minCost[end]))

for _ in range(m):
    s, e, c = map(int, input().split())
    if e not in graph[s] or graph[s][e] > c:
        graph[s][e] = c
        graph[e][s] = c

dijkstra()
