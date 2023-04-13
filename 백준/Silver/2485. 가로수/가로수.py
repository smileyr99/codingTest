## template
import sys
import math

n = int(input())

a = int(input())

dis = []
for i in range(n-1):
  b = int(input())
  dis.append(b - a)
  a = b

g = dis[0]
for i in dis:
  g = math.gcd(g, i)

res = 0
for each in dis:
  res += each // g-1
  
print(res)
  

