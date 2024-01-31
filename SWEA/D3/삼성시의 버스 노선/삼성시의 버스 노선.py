# import sys
# sys.stdin = open('input.txt')

T = int(input())

def solve(N, P, busRouteList, busStopList, iter):
    routeList = [0 for _ in range(P)]

    for busRoute in busRouteList:
        for i in range(P):
            if busRoute[0] <= busStopList[i] <= busRoute[1]:
                routeList[i] = routeList[i] + 1

    print(f"#{iter} {routeList[0]}", end="")
    for i in range(1, P):
        print(f" {routeList[i]}", end="")
    print()

for i in range(T):
    N = int(input())
    busRouteList = []
    for _ in range(N):
        busRouteList.append(list(map(int, input().split())))
    P = int(input())
    busStopList = []
    for _ in range(P):
        busStopList.append(int(input()))
    solve(N, P, busRouteList, busStopList, i + 1)