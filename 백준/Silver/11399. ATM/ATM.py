# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
person = sorted(list(map(int, input().split())))

total = 0
for i in range(n):
    total += person[i] + (n-i-1)*person[i]
print(total)