import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):
    n = int(input())
    numbers = sorted([input() for _ in range(n)])
    answer = 'YES'

    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            answer = 'NO'
            break

    print(answer)