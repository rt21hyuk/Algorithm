import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def dfs(node):
    visited[node] = 1

    if not edge[1]:
        return

    for idx in range(len(edge[node])):
        next = edge[node][idx]
        if visited[next] == 0:
            dfs(next)

numOfNode = int(input())
numOfEdge = int(input())
edge = [[] for _ in range(numOfNode+1)]
visited = [0 for _ in range(numOfNode+1)]
for _ in range(numOfEdge):
    node1, node2 = map(int, input().split())
    edge[node1].append(node2)
    edge[node2].append(node1)

dfs(1)
print(sum(visited)-1)