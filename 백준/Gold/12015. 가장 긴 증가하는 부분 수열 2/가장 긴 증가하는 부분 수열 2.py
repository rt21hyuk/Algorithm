# import sys
# sys.stdin = open('input.txt', 'r')

n = int(input())
numList = list(map(int, input().split()))
lisList = []

def binarySearch():
    for idx, num in enumerate(numList):
        if not lisList or lisList[-1] < num:
            lisList.append(num)
        else:
            left, right = 0, len(lisList)-1
            while left <= right:
                mid = (left + right) // 2
                if lisList[mid] >= numList[idx]:
                    right = mid - 1
                else:
                    left = mid + 1
            lisList[left] = num

def solve():
    binarySearch()
    print(len(lisList))

solve()