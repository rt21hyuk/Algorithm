# import sys
# sys.stdin = open("input.txt", "r")

def check(cur, next):
    if signs[cur] == '<' and arr[cur] < next:
        return True
    elif signs[cur] == '>' and arr[cur] > next:
        return True
    return False

def dfs(depth):
    global maxVal, minVal
    if depth == n:
        # print(''.join(map(str, arr)))
        maxVal = max(int(''.join(map(str, arr))), maxVal)
        minVal = min(int(''.join(map(str, arr))), minVal)
        return

    for next in range(10):
        if visited[next]:
            continue

        if check(depth, next):
            visited[next] = 1
            arr[depth+1] = next
            dfs(depth+1)
            visited[next] = 0

n = int(input())
signs = list(map(str, input().split()))

maxVal = float('-inf')
minVal = float('inf')

visited = [0 for i in range(10)]
arr = [-1 for _ in range(n+1)]

for i in range(10):
    arr[0] = i
    visited[i] = 1
    dfs(0)
    visited[i] = 0

if len(str(maxVal)) == n:
    print('0' + str(maxVal))
else:
    print(maxVal)

if len(str(minVal)) == n:
    print('0' + str(minVal))
else:
    print(minVal)