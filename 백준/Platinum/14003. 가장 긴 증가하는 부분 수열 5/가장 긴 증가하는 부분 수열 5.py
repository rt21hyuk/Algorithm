# import sys
# sys.stdin = open('input.txt', 'r')

n = int(input())
numList = list(map(int, input().split()))
lisList = []
idxList = [0 for _ in range(n)]

def binarySearch():
    for idx, num in enumerate(numList):
        if not lisList or lisList[-1] < num:
            lisList.append(num)
            idxList[idx] = len(lisList)-1
        else:
            left, right = 0, len(lisList)-1
            while left <= right:
                mid = (left + right) // 2
                if lisList[mid] >= numList[idx]:
                    right = mid - 1
                else:
                    left = mid + 1
            lisList[left] = num
            idxList[idx] = left

def findLIS():
    idx = len(lisList) - 1
    answer = []
    for i in range(n-1, -1, -1):
        if idxList[i] == idx:
            idx -= 1
            answer.append(numList[i])
    return answer[::-1]

def solve():
    binarySearch()
    print(len(lisList))
    print(*findLIS())

solve()