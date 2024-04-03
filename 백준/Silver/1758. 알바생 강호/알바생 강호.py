# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
person = []
for i in range(n):
    person.append(int(input()))
person.sort(reverse=True)

total = 0

for i in range(n):
    if person[i] - i > 0:
        total = total + person[i] - i
    else:
        break

print(total)