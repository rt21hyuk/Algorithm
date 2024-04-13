mineralDict = {"diamond": 0, "iron": 1, "stone": 2}

def solution(picks, minerals):
    n = min(sum(picks), len(minerals)//5+1)
    
    cost = [[0, 0, 0] for _ in range(n)]
    
    idx = 0
    for i in range(1, len(minerals)+1):
        mineralIdx = mineralDict[minerals[i-1]]
        cost[idx][mineralIdx] += 1
    
        if i % 5 == 0:
            idx += 1
        
        if idx == n:
            break
    
    cost.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    
    pickIdx = cur = answer = 0
    
    while cur < n:
        if picks[pickIdx]:
            if pickIdx == 0:
                answer += cost[cur][0] + cost[cur][1] + cost[cur][2]
            elif pickIdx == 1:
                answer += 5 * cost[cur][0] + cost[cur][1] + cost[cur][2]
            else:
                answer += 25 * cost[cur][0] + 5 * cost[cur][1] + cost[cur][2]
            cur += 1
            picks[pickIdx] -= 1
            
        else:
            pickIdx += 1
        
    return answer