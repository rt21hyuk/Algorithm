# import sys
# sys.stdin = open("input.txt", "r")

def dfs(depth, curVal):
    global answer

    if depth == n:
        return

    if curVal + numList[depth] == target:
        # print(visited)
        answer += 1

    # visited[depth] = 1
    dfs(depth+1, curVal + numList[depth])
    # visited[depth] = 0

    dfs(depth+1, curVal)


answer = 0
n, target = map(int, input().split())
numList = list(map(int, input().split()))
visited = [0]*n

dfs(0, 0)

print(answer)