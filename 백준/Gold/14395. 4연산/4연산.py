def dfs(S,T,string):
    global result
    if result and len(string) >= len(result):
        return
    # print(S,string,result)
    if S == T:
        if not result:
            result = string
        elif len(string) < len(result):
                result = string
        return

    for w in '*+/':
        if w == '*' and S*S <= T and S > 1:
            dfs(S*S,T,string+w)
        elif w == '+' and S+S <= T:
            dfs(S+S,T,string+w)
        elif not string and w == '/':
            dfs(S//S,T,string+w)


s, t = map(int,input().split())
result = ''
if s == t:
    print(0)
elif t == 1:
    print('/')
else:
    dfs(s,t,'')
    if result:
        print(result)
    else:
        print(-1)