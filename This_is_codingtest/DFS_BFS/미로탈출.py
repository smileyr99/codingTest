import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, input())) for _ in range(n)]

# 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    # 큐가 빌 떄까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재위치를 기준으로 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 해당 위치에 괴물이 있을 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문한 경우
            if graph[nx][ny] == 1:
                # 방문한 노드에 +1를 하여 방문한 노드 개수 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
    return graph[n - 1][m - 1]


result = bfs(0, 0)
print(result)
