# alpha = {chr(i): i-65 for i in range(65, 91)}
# print(alpha)

def solution(name):
    answer = 0
    minMove = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        minMove = min(minMove, 2*i + len(name) - next, i + 2*(len(name) - next))
            
    answer += minMove
    return answer
