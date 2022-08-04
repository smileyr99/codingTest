import sys

input = sys.stdin.readline()
row = ord(input[0]) - ord('a') + 1
col = int(input[1])

#나이트가 갈 수 있는 8가지 방향 정의
dir = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

x, y = row, col
cnt = 0

for i in dir:
    nx = x + i[0]
    ny = y + i[1]
    # 맵의 edge 확인
    if nx <= 1 or ny <= 1 or nx >= 8 or ny >= 8:
        continue
    cnt += 1

print(cnt)