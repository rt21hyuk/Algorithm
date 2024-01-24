import sys
# sys.stdin = open("input.txt", "r")

N, target = map(int, input().split())
numArr = list(map(int, input().split()))

def solve():
    left, right = 0, 0
    sum = 0
    minLen = sys.maxsize
    
    while(True):
        if sum >= target:
            minLen = min(minLen, right - left)
            sum = sum - numArr[left]
            left = left + 1
        
        elif right == N:
            break
        
        elif sum < target:
            sum = sum + numArr[right]
            right = right + 1

    if minLen == sys.maxsize:
        print(0)
    else:
        print(minLen)
solve()