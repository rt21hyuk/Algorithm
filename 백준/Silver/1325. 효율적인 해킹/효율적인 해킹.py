import sys
input = sys.stdin.readline
from collections import deque # bfs를 위한 deque
# sys.stdin = open("input.txt", "r")

def bfs(start):
    q = deque([start])
    visited[start] = 1
    cnt = 1 # 해킹할 수 있는 컴퓨터의 개수
    while q:
        cur = q.popleft()
        for next in edge[cur]: # cur를 신뢰하는 컴퓨터(next)를 순회
            if visited[next] == 0:
                visited[next] = 1
                q.append(next)
                cnt += 1
    return cnt # 해킹할 수 있는 컴퓨터의 개수 반환

maxTotal = 0 # 해킹 가능한 컴퓨터 최대값
comList = [] # 컴퓨터 번호 리스트
n, m = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    edge[node2].append(node1)

for i in range(1, n+1): # 1번 컴퓨터부터 n번 컴퓨터까지
    visited = [0 for _ in range(n+1)]
    curTotal = bfs(i)
    if maxTotal < curTotal: # 현재값이 최대값보다 크다면
        maxTotal = curTotal 
        comList = [i] # 컴퓨터 번호 리스트를 초기화
    elif maxTotal == curTotal: # 현재값이 최대값과 같다면
        comList.append(i) # 컴퓨터 번호 리스트에 추가

print(*comList) # 컴퓨터 번호를 출력