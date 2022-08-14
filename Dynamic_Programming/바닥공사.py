import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * 1002

d[1] = 1  # a_0 초기값
d[2] = 3  # a_1 초기값

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])
