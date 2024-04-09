def dfs(S,T,string,cnt):
    global result
    if len(string) > len(result) and result:
        return
    # print(S,string,result)
    if S == T:
        if not result:
            result = string
        else:
            if len(string) < len(result):
                result = string
            elif len(string) == len(result):
                if string < result:
                    result = string
        return

    for w in '*+/':
        if w == '*' and S*S <= T and S > 1:
            dfs(S*S,T,string+w,cnt)
        elif w == '+' and S+S <= T:
            dfs(S+S,T,string+w,cnt)
        elif w == '/' and cnt == 0:
            dfs(S//S,T,string+w,cnt+1)


s, t = map(int,input().split())
result = ''
if s == t:
    print(0)
elif s == 0:
    print(-1)
elif t == 1:
    print('/')
elif t == 0:
    print('-')
else:
    dfs(s,t,'',0)
    if result:
        print(result)
    else:
        print(-1)