# import sys
# sys.stdin = open("input.txt", "r")

a, b = map(int, input().split())

def cal(num):
  if num % 4 == 0:
    return num
  elif num % 4 == 1:
    return 1
  elif num % 4 == 2:
    return num+1
  elif num % 4 == 3:
    return 0

print(cal(b) ^ cal(a-1))