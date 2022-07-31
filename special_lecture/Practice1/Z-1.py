# 수직선상 두 점사이의 거리 최대값

import sys

n = int(sys.stdin.readline())
nums = list()

for i in range(n):
    tmp = int(sys.stdin.readline())
    nums.append(tmp)

mx = max(nums)
mn = min(nums)

result = mx - mn

print(result)