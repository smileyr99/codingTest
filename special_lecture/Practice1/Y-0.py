# 제시한 숫자 사이에 'x' or '+'를 넣고 연산한 값중 가장 큰값 출력

import sys
s = list(map(int, sys.stdin.readline()))
result = s[0]

for i in s:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i
print(result)