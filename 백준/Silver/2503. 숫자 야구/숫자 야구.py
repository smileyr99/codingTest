## template
import sys

from itertools import permutations
T = int(input())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nums = list(permutations(data, 3))

for _ in range(T):
  n, s, b = map(int, sys.stdin.readline().split())
  n = list(str(n))
  cnt = 0
  for i in range(len(nums)):
    st = ba = 0
    i -= cnt
    for j in range(3):
      if nums[i][j] == n[j]:
        st += 1
      elif n[j] in nums[i]:
        ba += 1
      
    if st != s or ba != b:
      nums.remove(nums[i])
      cnt += 1

print(len(nums))
    
    
  