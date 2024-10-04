import sys
input = sys.stdin.readline

from collections import deque

sideIdx = {'F': 0, 'D': 1, 'U': 2, 'L': 3, 'R': 4, 'B': 5}

"""
               [2]
               WWW            
               WWW
               WWW
          [3]  [0]  [4]  [5]
          GGG  RRR  BBB  OOO
          GGG  RRR  BBB  OOO
          GGG  RRR  BBB  OOO
               [1]
               YYY
               YYY
               YYY  
"""

def rotateSide(cube, side):
    # for _ in range(2):
    index = sideIdx[side]

    temp = [row[:] for row in cube[index]]

    cube[index][0][0] = temp[2][0]
    cube[index][0][1] = temp[1][0]
    cube[index][0][2] = temp[0][0]
    cube[index][1][0] = temp[2][1]
    cube[index][1][2] = temp[0][1]
    cube[index][2][0] = temp[2][2]
    cube[index][2][1] = temp[1][2]
    cube[index][2][2] = temp[0][2]

def simulate(cube, side):
    if side == 'U':
        temp = cube[0][0]
        cube[0][0] = cube[4][0]
        cube[4][0] = cube[5][0]
        cube[5][0] = cube[3][0]
        cube[3][0] = temp

    elif side == 'D':
        temp = cube[0][2]
        cube[0][2] = cube[3][2]
        cube[3][2] = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = temp

    elif side == 'F':
        temp = cube[2][2]
        cube[2][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[1][0]
        cube[1][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp

    elif side == 'B':
        temp = cube[2][0]
        cube[2][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][2]
        cube[1][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = temp

    elif side == 'L':
        temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp

    elif side == 'R':
        temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp
    rotateSide(cube, side)

def printUpSide(cube):
    for i in range(3):
        print("".join(cube[2][i]), end="\n")


def doCommand(cube, cmd):
    side, direction = cmd
    cnt = 1 if direction == '+' else 3
    for _ in range(cnt):
        simulate(cube, side)

n = int(input())

for _ in range(n):
    cnt, cmdList = int(input()), deque(map(str, input().split()))
    cube = [[] for _ in range(6)]
    for _ in range(3):
        cube[0].append(['r', 'r', 'r'])
        cube[1].append(['y', 'y', 'y'])
        cube[2].append(['w', 'w', 'w'])
        cube[3].append(['g', 'g', 'g'])
        cube[4].append(['b', 'b', 'b'])
        cube[5].append(['o', 'o', 'o'])
    cntIdx = 1

    while cmdList:
        doCommand(cube, cmdList.popleft())
    printUpSide(cube)