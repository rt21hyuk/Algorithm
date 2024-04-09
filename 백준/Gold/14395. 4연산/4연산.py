def dfs(S, T, string):
    global result
    # print(S, string)
    if result and len(string) >= len(result):
        return
    if S == T:
        if not result:
            result = string
        elif len(string) < len(result):
            result = string
        return

    if S * S <= T and S > 1:
        dfs(S*S, T, string + '*')
    if S + S <= T:
        dfs(S+S, T, string + '+')
    if not string:
        dfs(S//S, T, string + '/')

S, T = map(int,input().split())
result = ''
if S == T :
    print(0)
elif T == 1:
    print('/')
else:
    dfs(S, T, '')
    if result:
        print(result)
    else:
        print(-1)