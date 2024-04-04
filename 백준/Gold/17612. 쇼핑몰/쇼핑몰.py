from collections import deque
import heapq
import sys
input = sys.stdin.readline
N,k = map(int,input().split()) # N -> 손님 수 k -> 계산대 수

shopping = deque()
heap = []
for i in range(k):
    heapq.heappush(heap,[0,i,0])
tmp = 0
cnt = 1
ans = 0
for _ in range(N):
    id_num,w = map(int,input().split())
    time,buy_num,crt_id = heapq.heappop(heap)
    if time != 0:
        if time == tmp:
            pass
        else:
            while shopping:
                crt = shopping.popleft()
                ans += crt*cnt
                cnt = cnt+1

            tmp = time
        shopping.appendleft(crt_id)
    heapq.heappush(heap,[time+w,buy_num,id_num])

for i in range(k):
    time, buy_num, crt_id = heapq.heappop(heap)
    if time != 0:
        if time == tmp:
            pass
        else:
            while shopping:
                crt = shopping.popleft()
                ans += crt*cnt
                cnt = cnt+1

            tmp = time
        shopping.appendleft(crt_id)

for crt in shopping:
    ans += crt*cnt
    cnt = cnt+1
print(ans)
