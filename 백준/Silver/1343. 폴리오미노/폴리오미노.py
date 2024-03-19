# import sys
# sys.stdin = open('input.txt')

board = input()
newBoard = board.replace("XXXX", "AAAA")
newBoard = newBoard.replace("XX", "BB")

if newBoard.count("X") > 0:
    print(-1)
else:
    print(newBoard)