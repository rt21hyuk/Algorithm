# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(T):
    numbers = list(map(int, input().split()))
    max = -1

    for j in range(10):
        if(numbers[j] > max):
            max = numbers[j]

    print("#" + str(i+1) + " " + str(max))
