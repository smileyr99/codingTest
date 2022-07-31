# A 작업을 시작할 수 있는 최소 역량값
# B 작업 후 얻게 되는 역량 증가값

import sys

# 방법1
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
tmp = list()
lst = list()

for i in range(0, len(nums), 2):
    A = nums[i]
    B = nums[i+1]
    tmp.append(A)
    tmp.append(B)
    lst.append(tmp)
    tmp = []
lst.sort()

result = 0

for i in range(n):
    if result >= lst[i][0]:
        result += lst[i][1]

print(result)

'''
# 방법2
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
mx = max(nums)
index = [0 for i in range(mx*2)]

for i in range(0, n*2, 2):
    index[nums[i]] += nums[i+1]

print(index)
result = index[0]
for i in range(len(index)):
    if index[i] != 0 and result >= i+1:
       result += index[i]
       print(result)

print(result)
'''
