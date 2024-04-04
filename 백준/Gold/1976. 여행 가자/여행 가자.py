import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

for i in range(n):
    graph[i][i] = 1

def floydwarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
floydwarshall()

for i in range(1, m):
    if graph[plan[i-1]-1][plan[i]-1] != 1:
        print("NO")
        sys.exit()
print("YES")
