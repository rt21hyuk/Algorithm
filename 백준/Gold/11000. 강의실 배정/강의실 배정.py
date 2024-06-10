import sys, heapq
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort(key=lambda x: (x[0], x[1]))
# print(classes)

pq = [classes[0][1]]
# print(pq)

for i in range(1, n):
    if pq[0] <= classes[i][0]:
        heapq.heappop(pq)
    heapq.heappush(pq, classes[i][1])
    # print(pq)

print(len(pq))
