import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

sum_arr = sum(arr)
res = 0
tmp = 0
for i in arr:
    tmp += i
    res += i * (sum_arr - tmp)

print(res % 1000000007)