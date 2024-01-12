def isTrue(y, x):
    global arr
    sum = 0

    for i in range(3):
        for j in range(3):
            sum = sum + arr[i + y][j + x]

    if (sum != 45):
        return False
    return True

def isTrue2():
    global arr
    for i in range(9):
        sum = 0
        for j in range(9):
            sum = sum + arr[i][j]

        if(sum != 45):
            return False

    for i in range(9):
        sum = 0
        for j in range(9):
            sum = sum + arr[j][i]

        if(sum != 45):
            return False
    return True

def isTrue3():
    global arr

    for i in range(9):
        for j in range(8):
            if(arr[i][j] == 5 and arr[i][j+1] == 5):
                return False
    return True
                
# arr = [[0 for j in range(9)] for i in range(9)]


T = int(input())

for t in range(T):
    flag = True
    arr = []
    for i in range(9):
        arr.append(list(map(int, input().split())))

        # temp = list(map(int, input().split()))
        # for j in range(9):
        #     arr[i][j] = temp[j]

    for i in range(3):
        for j in range(3):
            if(isTrue(3*i, 3*j) == False):
                flag = False
                break
    
    if(isTrue2() == False):
        flag = False
    
    if(isTrue3() == False):
        flag = False
        
    print("#" + str(t+1) + " " + str(int(flag)))
