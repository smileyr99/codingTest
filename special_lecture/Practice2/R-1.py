# 공포토 x 만큼 x 명의 인원이 필요 -> 최대로 만들 수 있는 그룹

# 방법1
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

result = 0
cnt = 0

for i in nums:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)

