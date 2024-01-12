T = int(input())

def spary_plus(y, x):
    global N, M, arr

    sum = arr[y][x]
    
    for i in range(M - 1):
        ny = y + i + 1
        py = y - i - 1

        if(ny < N):
            sum = sum + arr[ny][x]
        if(py >= 0):
            sum = sum + arr[py][x]

    for j in range(M - 1):
        nx = x + j + 1
        px = x - j - 1
        if(nx < N):
            sum = sum + arr[y][nx]
        if(px >= 0):    
            sum = sum + arr[y][px]

    return sum

def spary_cross(y, x):
    global N, M, arr

    sum = arr[y][x]
    
    for i in range(M - 1):
        ny = y + i + 1
        py = y - i - 1
        nx = x + i + 1
        px = x - i - 1

        if(nx < N):
            if(ny < N):
                sum = sum + arr[ny][nx]
            if(py >= 0):
                sum = sum + arr[py][nx]

        if(px >= 0):
            if(ny < N):
                sum = sum + arr[ny][px]
            if(py >= 0):
                sum = sum + arr[py][px]

    return sum

for t in range(T):
    N, M = map(int, input().split())
    maxSum = -1
    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            maxSum = max(maxSum, max(spary_plus(i, j), spary_cross(i, j)))

    print("#" + str(t + 1) + " " + str(maxSum))