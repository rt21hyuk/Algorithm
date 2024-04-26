N = int(input())
potions = list(map(int,input().split()))
potions.sort()

start, end = 0, N-1
SUM_abs = abs(potions[start] + potions[end])
result = [potions[start],potions[end]]
while start < end:
    SUM = potions[start] + potions[end]

    if abs(SUM) < SUM_abs:
        SUM_abs = abs(SUM)
        result = [potions[start],potions[end]]

    if SUM == 0:
        break
    elif SUM < 0:
        start += 1
    elif SUM > 0:
        end -= 1

print(*result)