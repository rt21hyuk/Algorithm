import sys
input = sys.stdin.readline

NUM_MAX = 1000000

n = int(input())
cntList = [0 for _ in range(NUM_MAX+1)]
numList = list(map(int, input().split()))

for num in numList:
    cntList[num] += 1

stack = []
NGFList = [-1] * n  # 결과 리스트를 미리 -1로 초기화

# 역순으로 탐색하며 오등큰수를 찾음
for i in range(n - 1, -1, -1):
    num = numList[i]

    # 스택이 비어있지 않고 현재 숫자의 등장횟수가 스택의 top보다 크거나 같으면 pop
    while stack and cntList[num] >= cntList[stack[-1]]:
        stack.pop()

    # 스택이 비어있지 않으면 해당 숫자는 오등큰수
    if stack:
        NGFList[i] = stack[-1]

    # 스택에 현재 숫자를 추가
    stack.append(num)

print(*NGFList)