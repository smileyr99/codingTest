# 각 행에서 가장 작은 값들중 가장 큰값 출력

import sys

n, m = map(int, sys.stdin.readline().split())
cards = list()
for _ in range(n):
    cards.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = list()
for i in range(n):
    result.append(min(cards[i]))

mx = max(result)

print(mx)
