import sys
input = sys.stdin.readline

NUM_MAX = 1000000

n = int(input())
cntList = [0 for _ in range(NUM_MAX+1)]
numList = list(map(int, input().split()))

for num in numList:
    cntList[num] += 1

stack = []
NGFList = []

for num in numList[::-1]:
    if not stack:
        NGFList.append(-1)
    else:
        while 1:
            if stack:
                if cntList[num] < cntList[stack[-1]]:
                    NGFList.append(stack[-1])
                    break
                else:
                    stack.pop()
            else:
                NGFList.append(-1)
                break
    stack.append(num)

print(*NGFList[::-1])