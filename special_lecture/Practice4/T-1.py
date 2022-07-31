import sys

n = int(sys.stdin.readline())
nlst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mlst = list(map(int, sys.stdin.readline().split()))

result = list()

for i in mlst:
    if i in nlst:
        result.append('yes')
    else:
        result.append('no')

print(*result)