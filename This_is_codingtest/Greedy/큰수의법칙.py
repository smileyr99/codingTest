import sys

N, M, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
nums.reverse()

mul = M // K    # 큰 수가 더해지는 횟수
re = M % K      # 다음 큰수가 더해지는 횟수
result = nums[0] * mul * K + nums[1] * re   # 결과 계산

print(result)
