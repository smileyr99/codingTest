import sys

n = int(sys.stdin.readline())
dir_list = list(sys.stdin.readline().split())

# 시작 위치
x, y = 1, 1

# L R U D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for dir in dir_list:
    for i in range(len(move_types)):
        if dir == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행(현재 위치에서 다음 위치로 선언)
    x, y = nx, ny

print(x, y)
