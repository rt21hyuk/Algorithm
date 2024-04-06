def solution(N, number):
    dp = [[] for _ in range(9)]
    for l in range(1, 9):
        combSet = set()
        combSet.add(int(str(N)*l))
        for i in range(1, l):
            for n1 in dp[i]:
                for n2 in dp[l-i]:
                    plus = n1+n2
                    minus = n1-n2
                    mul = n1*n2
                    combSet.add(plus)
                    combSet.add(mul)
                    if n2 != 0:
                        div = n1//n2
                        combSet.add(div)
                    
                    if minus > 0:
                        combSet.add(minus)
                        
        if number in combSet:
            return l
        for num in combSet:
            dp[l].append(num)
    return -1