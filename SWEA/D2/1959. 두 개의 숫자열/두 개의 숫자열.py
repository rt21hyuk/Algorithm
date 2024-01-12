T = int(input())

for t in range(T):
    max = -1

    N, M = map(int, input().split())
    
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    sum = 0
    if (N < M):
        for j in range(abs(M - N) + 1):
            sum = 0
            for i in range(N):
                sum = sum + arr1[i] * arr2[i+j]

            if(sum > max):
                max = sum
    else:
        for j in range(abs(M - N) + 1):
            sum = 0
            for i in range(M):
                sum = sum + arr1[i+j] * arr2[i]

            if(sum > max):
                max = sum

    print("#" + str(t+1) + " " + str(max))
