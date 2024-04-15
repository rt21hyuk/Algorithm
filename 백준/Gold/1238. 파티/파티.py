# import sys
# sys.stdin = open("input.txt", "r")

import heapq

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

def dijkstra(start, end):
  minCost = [float('inf') for _ in range(n+1)]
  minCost[start] = 0

  q = []
  heapq.heappush(q, [0, start])

  while q:
    cost, cur = heapq.heappop(q)

    if cur == end:
      return cost

    if minCost[cur] < cost:
      continue

    for next, nextCost in graph[cur]:
      if cost + nextCost < minCost[next]:
        minCost[next] = cost + nextCost
        heapq.heappush(q, [minCost[next], next])

for _ in range(m):
  start, end, time = map(int, input().split())
  graph[start].append([end, time])


maxCost = 0
for cur in range(1, n+1):
  maxCost = max(dijkstra(cur, x) + dijkstra(x, cur), maxCost)

print(maxCost)