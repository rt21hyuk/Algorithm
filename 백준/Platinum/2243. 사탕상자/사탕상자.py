import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

n = int(input())
tree = [0] * (4*10**6)

def putCandy(left, right, node, rank, cnt):
    tree[node] += cnt
    if left == right:
        return
    mid = (left+right) // 2
    if rank <= mid:
        putCandy(left, mid, node*2, rank, cnt)
    else:
        putCandy(mid+1, right, node*2+1, rank, cnt)

def findCandy(left, right, node, rank):
    tree[node] -= 1
    if left == right:
        return left
    mid = (left+right) // 2
    if tree[node*2] >= rank:
        return findCandy(left, mid, node*2, rank)
    else:
        return findCandy(mid+1, right, node*2+1, rank-tree[node*2])

for _ in range(n):
    command = list(map(int, input().rstrip().split()))
    if len(command) == 2:
        rank = command[1]
        print(findCandy(1, 10**6, 1, rank))
    else:
        _, rank, cnt = command
        putCandy(1, 10**6, 1, rank, cnt)