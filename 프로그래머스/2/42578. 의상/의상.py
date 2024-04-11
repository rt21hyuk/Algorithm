def solution(clothes):
    answer = 1
    types = [y for x, y in clothes]
    counts = [types.count(type) for type in set(types)]
    for c in counts:
        answer *= c + 1 # 옷 종류별 개수 + 안 고르는 경우
    
    return answer - 1 # 아무것도 안 고르는 경우