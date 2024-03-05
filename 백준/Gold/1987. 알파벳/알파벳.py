def dfs(x, y, visited, count):
    global max_count

    # 현재 위치의 알파벳 방문 표시
    visited[ord(board[x][y]) - ord('A')] = True

    # 현재까지 이동한 칸의 수 갱신
    count += 1

    # 상하좌우 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 다음 위치가 보드 내에 있고, 아직 방문하지 않은 알파벳인 경우
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny]) - ord('A')]:
            dfs(nx, ny, visited, count)

    # 이동이 끝난 후, 최대 칸 수 갱신
    max_count = max(max_count, count)

    # 현재 위치의 알파벳 방문 표시 해제
    visited[ord(board[x][y]) - ord('A')] = False

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

# 상하좌우 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 방문한 알파벳을 저장하기 위한 배열
visited = [False] * 26

# 최대 칸 수 초기화
max_count = 0

# 시작 위치에서 DFS 시작
dfs(0, 0, visited, 0)

print(max_count)
