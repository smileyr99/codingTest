import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 101

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = nums[0]  # a_0 초기값
d[1] = max(nums[0], nums[1])  # a_1 초기값
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + nums[i])

print(d[n - 1])
