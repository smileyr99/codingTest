## template
import sys

tc = int(input())

def sol():
  global n, ans
  n = int(input())
  ans = []
  recur(2,'1')
  print()
  
def recur(now, tmp):
  if now == n+1:
    calc(tmp)
    return
  
  recur(now+1, tmp+' '+str(now))
  recur(now+1, tmp+'+'+str(now))
  recur(now+1, tmp+'-'+str(now))
  
  
def calc(ans):
  tmp = ans.replace(' ', '')
  if eval(tmp) == 0:
    print(ans)

for _ in range(tc):
  sol()
  
  
    