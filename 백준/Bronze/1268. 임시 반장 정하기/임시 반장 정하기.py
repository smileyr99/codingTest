## template
import sys

n = int(input())

arr = []
same = [0] * n
for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().split())))
  same[i] = [0] * n
  
for i in range(5):
  for j in range(n):
    for k in range(j+1, n):
      if arr[j][i] == arr[k][i]:
        same[j][k] = 1
        same[k][j] = 1


cnt = []
for c in same:
  cnt.append(c.count(1))
  
print(cnt.index(max(cnt)) + 1)


      
      
      
      
      
