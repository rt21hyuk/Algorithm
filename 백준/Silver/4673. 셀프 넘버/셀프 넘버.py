s = set(range(1,10001))
remove = set()

for num in s:
    for i in str(num):
        num+=int(i)
    remove.add(num)

result = s - remove
ans = list(sorted(result))
for i in ans:
    print(i)

