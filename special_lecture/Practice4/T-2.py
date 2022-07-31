import sys

n, x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in nums:
    if i == x:
        cnt += 1

if cnt == 0:
    print(-1)
else:
    print(cnt)