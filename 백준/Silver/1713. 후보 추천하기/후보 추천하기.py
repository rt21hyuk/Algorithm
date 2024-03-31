import sys
#sys.stdin = open("input.txt", "r")

from heapq import *

n = int(input())
student_num = int(input())
student_list = list(map(int, input().split()))
pic_heap = list()

for idx, num in enumerate(student_list):
    tmp_heap = list()
    flg = 0

    while pic_heap:
        cnt, old_idx, std_num = heappop(pic_heap)
        if std_num == num:
            cnt += 1

        heappush(tmp_heap, (cnt, old_idx, std_num))
        flg += std_num == num

    if not flg and len(tmp_heap) >= n:
        heappop(tmp_heap)

    if not flg:
        heappush(tmp_heap, (0, idx, num))
    pic_heap = tmp_heap

answer_list = [x[-1] for x in pic_heap]
answer_list.sort()

print(*answer_list)