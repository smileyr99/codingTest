import sys


def dfs():
    # s리스트 안에 m개의 요소가 쌓였을 경우
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # s리스트 안에 m개의 요소가 쌓이지 않았을 경우
    for i in range(1, n + 1):
        if visited[i]:  # i가 방문한 적이 있다면 -> true라면 contiune
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False


n, m = map(int, sys.stdin.readline().split())
s = []
visited = [False] * (n + 1)
dfs()
