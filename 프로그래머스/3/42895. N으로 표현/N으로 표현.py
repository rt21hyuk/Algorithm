cal = {0:lambda x,y: x+y,
      1:lambda x,y: x-y,
      2:lambda x,y: x*y,
      3:lambda x,y: x//y}

def solution(N, number):
    dp = [[] for _ in range(9)]
    for i in range(1, 9):
        combSet = set()
        combSet.add(int(str(N)*i))
        for j in range(1, i):
            for n1 in dp[j]:
                for n2 in dp[i-j]:
                    for k in range(4):
                        if k!=3 or n2 != 0:
                            val = cal[k](n1, n2)
                        if val > 0:
                            combSet.add(val)
                        
        if number in combSet:
            return i
        for num in combSet:
            dp[i].append(num)
    return -1