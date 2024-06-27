import heapq as hq

# 유형 별 구분 함수
def solution(k, n, reqs):
    def peopleInfo(typeNum : int, peopleInfo : list) -> dict:
        info = {i : [] for i in range(0, typeNum)}
        
        for start, spend, consultType in peopleInfo:
            info[consultType-1].append((start,spend))
            
        return info
    
    # 대기시간 계산 함수
    def calTime(consultantNum : int, info : list) -> int:
        if len(info) <= consultantNum:
            return 0 # 상담사보다 리스트가 작거나 같으면 0 리턴
        else:
            waiting = 0
            timeList, remainConsultant = [], consultantNum
            
            for start, spend in info:
                if remainConsultant > 0:
                    hq.heappush(timeList, start+spend) # 힙에 종료시간을 넣음
                    remainConsultant += -1
                else:
                    nowTime = hq.heappop(timeList) # 시점 업데이트, 가장 빨리 종료되는 상담 시각
                    if nowTime - start > 0:
                        waiting += nowTime - start # 대기시간 업데이트
                        hq.heappush(timeList, nowTime+spend)
                    else:
                        hq.heappush(timeList, start+spend)
            return waiting
    
    # 대기시간 행렬
    infos = peopleInfo(k, reqs)
    timeInfo = [[0 for _ in range(n-k+2)] for _ in range(k)] # 대기시간 = timeInfo[유형][상담사 수]
    print(timeInfo)
    for typeNum in range(k):
        for consultantNum in range(1,n-k+2): # 1명부터 n-k+1명 일 때 대기큐 계산
            time = calTime(consultantNum, infos[typeNum])
            timeInfo[typeNum][consultantNum] = time
            if not time:
                break
    
    # 최적해 계산
    count = [1] * k
    while sum(count) < n:
        temp = []
        for i in range(k):
            temp.append(timeInfo[i][count[i]+1] - timeInfo[i][count[i]])
        minIdx = temp.index(min(temp))
        count[minIdx] += 1
        
    minTime = 0
    for typeNum, consultantNum in enumerate(count):
        minTime += timeInfo[typeNum][consultantNum]
    return minTime