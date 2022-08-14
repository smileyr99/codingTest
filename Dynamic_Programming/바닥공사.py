import sys

n = int(sys.stdin.readline().rstrip())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1002

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[1] = 1  # a_0 초기값
d[2] = 3  # a_1 초기값
for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])
