# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())

def comb(n, r):
    count = tmp = 1

    for i in range(n, n-r, -1):
        count = count * i
        count = count // tmp
        tmp += 1

    return count

for tc in range(t):
    n, m = map(int, input().split())
    print(comb(m, n))