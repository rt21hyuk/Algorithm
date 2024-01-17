import sys
# sys.stdin = open("input.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N - 1
sumResult = abs(arr[left] + arr[right])
answer = [arr[left], arr[right]]

def binarySearch():
    global left, right, sumResult, answer

    while left < right:
        sumVal = arr[left] + arr[right]
    
        if abs(sumVal) < sumResult:
            sumResult = abs(sumVal)
            answer = [arr[left], arr[right]]

            if sumVal == 0:
                break

        if sumVal < 0:
            left = left + 1
        else:
            right = right - 1

def solve():
    binarySearch()
    print(answer[0], answer[1])

solve()