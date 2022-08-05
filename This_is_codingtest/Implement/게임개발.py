import sys

n, m = map(int, sys.stdin.readline().split())
x, y, dir = map(int, sys.stdin.readline().split())

# 방문처리맵
visit = [[0]*m for _ in range(n)]

# 시작점 방문 처리
visit[x][y] = 1

# 맵
Map = list()
for _ in range(n):
    Map.append(list(map(int, sys.stdin.readline().split())))

# 북, 서, 남, 동 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 함수
def turn_left():
    global dir
    dir -= 1
    if dir < 0:
        dir = 3

# 주의! 첫위치도 방문한 것으로 여기므로 cnt 초기값은 1
cnt = 1
turn_cnt = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 회전 후 정면이 안가본 육지일 경우
    if visit[nx][ny] == 0 and Map[nx][ny] == 0:
        visit[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 0
        continue
    # 회전 후 정면이 가본 육지일 경우
    else:
        turn_cnt += 1
    # 네방향 모두 갈 수 잆는 경우
    if turn_cnt == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있다면 이동하기
        if Map[nx][ny] == 0:
            x = nx
            y = ny
        #  뒤가 바다일 경우
        else:
            break
        turn_cnt = 0

print(cnt)







