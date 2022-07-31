import sys

N, M, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
nums.reverse()

mul = M // K
re = M % K
result = nums[0]*mul*K + nums[1]*re

print(result)

