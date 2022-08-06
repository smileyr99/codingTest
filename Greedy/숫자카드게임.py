import sys

N, M = map(int, sys.stdin.readline().split())
result = list()

for i in range(N): #행만큼 반복
    nums = list(map(int, sys.stdin.readline().split()))
    result.append(min(nums)) # 행에서 가장 작은 수 리스트에 저장

result = max(result) #리스트에 저장된 가장 작은 수 중 가장 큰 수 출력

print(result)
