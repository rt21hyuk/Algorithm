N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x:x[1],reverse=True)

t = lst[0][1]
for i in range(N):
    if t >= lst[i][1]:
        t = lst[i][1]
    t = t - lst[i][0]
    if t < 0:
        t = -1
        break
        
print(t)