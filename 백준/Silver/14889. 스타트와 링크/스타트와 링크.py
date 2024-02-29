import sys
input=sys.stdin.readline

N=int(input())
S=[]

for i in range(N):
    S.append(list(map(int,input().split())))

result=[]
temp=[]

def solution(n,s,count):
    global temp, result

    if n==count:
        start=0
        link=0
        for i in range(count):
            for j in range(count):
                if i in temp and j in temp:
                    start+=S[i][j]
                elif i not in temp and j not in temp:
                    link+=S[i][j]
        result.append(abs(start-link))
    else:
        for i in range(s,count):
            if i not in temp:
                temp.append(i)
                solution(n+2,i,count)
                temp.remove(i)
           
solution(0,0,N)
print(min(result))