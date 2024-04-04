import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def dfs(depth, prev):
    if depth == m: # 최대 길이에 도달하면 출력
        print(*prev)
        return

    for i in range(n):
        if not prev or prev[-1] <= numList[i]: # prev 리스트가 없거나(처음) or 가장 최근 값보다 크거나 같을 경우
            prev.append(numList[i]) # prev에 현재 값을 저장
            dfs(depth+1, prev)
            prev.pop() # prev에 현재 값을 삭제

n, m = map(int, input().split()) # n과 수열의 길이가 최대 8
numList = list(set(map(int, input().split()))) # 중복이 제거된 자연수 리스트
n = len(numList) # n을 중복 제거한 리스트 길이로 갱신
numList.sort() # 백트래킹을 위해 정렬
dfs(0, []) # n과 수열의 길이가 최대 8이고, 메모리 제한이 512MB이므로, 리스트를 Argument로 넣어도 메모리 제한이 발생하지 않는다고 판단했습니다.