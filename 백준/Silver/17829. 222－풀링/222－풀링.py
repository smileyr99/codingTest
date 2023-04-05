
import sys


def solution():
    n = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    while len(board[-1]) != 1:
        new = []
        for i in range(0, len(board), 2):
            tmp = []
            for j in range(0, len(board), 2):
                calc = sorted([board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]], reverse=True)
                tmp.append(calc[1])
            new.append(tmp)
        board = new
    print(board[0][0])


solution()