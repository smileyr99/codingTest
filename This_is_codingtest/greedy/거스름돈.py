def solution(money):
   coin = [500, 100, 50, 10]
   N = money
   cnt = 0
   remain = N
   for i in coin :
       cnt += remain // i
       remain = remain % i
   print(cnt)