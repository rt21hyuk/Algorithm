import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

from collections import deque

# 명령어를 수행하기 위한, dict와 lambda 함수 결합
# func[command](argument)로 함수 실행

func = {"push": lambda q,x: q.append(x),
           "front": lambda q:print(q[0]) if q else print(-1),
           "back": lambda q:print(q[-1]) if q else print(-1),
           "size": lambda q:print(len(q)),
           "pop": lambda q:print(q.popleft()) if q else print(-1),
           "empty": lambda q:print(1) if not q else print(0),
        }

n = int(input())

q = deque() # popleft를 위해, deque으로 큐를 구현

for i in range(n):
    command, *num = map(str, input().split()) # command에는 push, pop 같은 명령어
    # num에는 pop, size 같이 숫자가 안 올 수도 있어서 -> *num으로 선언 -> num이 있는 경우는 push 밖에 없음
    if num:
        func[command](q, int(num[0])) # push
    else:
        func[command](q)
