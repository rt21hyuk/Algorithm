T = int(input())

for i in range(T):
    numbers = list(map(int, input().split()))
    sum = 0

    for j in range(10):
        if(numbers[j] % 2 == 1):
            sum = sum + numbers[j]

    print("#" + str(i+1) + " " + str(sum))
