import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

nums = sorted(nums, reverse=True)

print(*nums)
