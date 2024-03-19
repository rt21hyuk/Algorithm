# import sys
# sys.stdin = open("input.txt", "r")

from queue import PriorityQueue

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

tc = int(input())

for t in range(1, tc+1):
    n, m, k = map(int, input().split())
    area = [[0 for _ in range(m + 2*k + 3)] for _ in range(n + 2*k + 3)]
    cells = []
    pq = PriorityQueue()
    numOfActive = numOfDead = 0

    for i in range(n):
        cell = list(map(int, input().split()))
        for j in range(m):
            area[k+1+i][k+1+j] = cell[j]
            if cell[j] != 0:
                cells.append([cell[j], cell[j], k+1+i, k+1+j])

    numOfActive = len(cells)

    for hour in range(k):
        for i in range(numOfActive):
            cells[i][1] -= 1
            if cells[i][1] == -1:
                pq.put([-cells[i][0], cells[i][2], cells[i][3]])
            if cells[i][1] == -cells[i][0]:
                numOfDead += 1

        while not pq.empty():
            curCell = pq.get()

            for idx in range(4):
                ni, nj = curCell[1] + di[idx], curCell[2] + dj[idx]

                if area[ni][nj] == 0:
                    numOfActive += 1
                    area[ni][nj] = -curCell[0]
                    cells.append([-curCell[0], -curCell[0], ni, nj])

    print(f'#{t} {numOfActive - numOfDead}')