import sys


def dfs():
    # s리스트 안에 m개의 요소가 쌓였을 경우
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # s리스트 안에 m개의 요소가 쌓이지 않았을 경우
    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()

n, m = map(int, sys.stdin.readline().split())
s = []
visited = [False] * (n + 1)

dfs()
