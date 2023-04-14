## template
import sys

def sum_beat(i, j):
  if j-1 < i:
    return 0
  rtn = 0
  for k in range(i-1, j-1):
    rtn += abs(arr[k] - arr[k+1])
  return rtn 
  
n,q = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(q):
  i, j = map(int, input().split())
  print(sum_beat(i, j))
  