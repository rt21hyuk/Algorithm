import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
numList = list(map(int, input().split()))
modList = [0 for _ in range(m)]

def solve():
    prefixSum = 0
    for i in range(n):
        prefixSum += numList[i]
        modList[prefixSum % m] += 1

    count = modList[0]
    for i in range(m):
        count += modList[i] * (modList[i]-1) // 2

    print(count)

solve()