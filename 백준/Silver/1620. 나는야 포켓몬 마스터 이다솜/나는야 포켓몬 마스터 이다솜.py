# import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
pocketmons = {}
for i in range(1, n+1):
    pocketmon = input()
    pocketmons.update({pocketmon: i})
    pocketmons.update({i: pocketmon})

for _ in range(m):
    iter = input()
    if iter.isalpha():
        print(pocketmons.get(iter))
    else:
        print(pocketmons.get(int(iter)))
