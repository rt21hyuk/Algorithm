# import sys
# sys.stdin = open("input.txt", "r")

def calTime(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

left = {"q": (0,0), "w": (0,1), "e": (0,2), "r": (0,3), "t": (0,4),
       "a": (1,0), "s": (1,1), "d": (1,2), "f": (1,3), "g": (1,4),
        "z": (2,0), "x": (2,1), "c": (2,2), "v": (2,3)}

right = {"y": (0,5), "u": (0,6), "i": (0,7), "o": (0,8), "p": (0,9),
         "h": (1,5), "j": (1,6), "k": (1,7), "l": (1,8),
         "b": (2,4), "n": (2,5), "m": (2,6)}

answer = 0
startLeft, startRight = map(str, input().split())
leftPoint, rightPoint = left[startLeft], right[startRight]

target = input()

for char in target:
    if char in left:
        charPoint = left[char]
        answer += calTime(leftPoint[1], leftPoint[0], charPoint[1], charPoint[0])
        leftPoint = charPoint
    else:
        charPoint = right[char]
        answer += calTime(rightPoint[1], rightPoint[0], charPoint[1], charPoint[0])
        rightPoint = charPoint
    answer += 1

print(answer)