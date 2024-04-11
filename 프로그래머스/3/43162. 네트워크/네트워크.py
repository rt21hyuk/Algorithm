from collections import deque

def bfs(start, computers, visited):
    q = deque([start])
    visited[start] = 1
    
    while q:
        cur = q.popleft()
        
        for idx in range(len(computers[cur])):

            if visited[idx]:
                continue
                
            if computers[cur][idx]:
                q.append(idx)
                visited[idx] = 1
    
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            bfs(i, computers, visited)
            answer += 1
            
    return answer