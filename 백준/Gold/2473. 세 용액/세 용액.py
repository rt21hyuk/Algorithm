def search(potions):
    global ans, result
    for i in range(N - 2):
        start, end = i + 1, N - 1

        while start < end:
            SUM = potions[i] + potions[start] + potions[end]
            if abs(SUM) < ans:
                ans = abs(SUM)
                result = [potions[i], potions[start], potions[end]]

            if SUM == 0:
                return
            elif SUM < 0:
                start += 1
            elif SUM > 0:
                end -= 1

N = int(input())
potions = list(map(int,input().split()))
potions.sort()

ans = float('inf')
result = []

search(potions)
print(*result)