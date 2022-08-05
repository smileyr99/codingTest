import sys

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료 (n,m 주의!!)
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우의 위치 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드에 대하여 탐색
cnt = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j):
            cnt += 1

print(cnt)
