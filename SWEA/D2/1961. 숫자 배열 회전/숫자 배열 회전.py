T = int(input())

for t in range(T):
    N = int(input())

    arr = [[0 for j in range(N)] for i in range(N)]
    arr90 = [[0 for j in range(N)] for i in range(N)]
    arr180 = [[0 for j in range(N)] for i in range(N)]
    arr270 = [[0 for j in range(N)] for i in range(N)]

    for i in range(N):
        temp = list(map(int, input().split()))
        
        for j in range(N):
            arr[i][j] = temp[j]

    for i in range(N):
        for j in range(N):
            arr90[j][N-i-1] = arr[i][j]
            arr180[N-i-1][N-j-1] = arr[i][j]
            arr270[N-j-1][i] = arr[i][j]

    print("#" + str(t+1))
        
    for i in range(N):
        for j in range(N):
            print(arr90[i][j], end="")
        print(" ", end="")
        for j in range(N):
            print(arr180[i][j], end="")
        print(" ", end="")
        for j in range(N):
            print(arr270[i][j], end="")
        print()