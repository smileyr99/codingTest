import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in array:
        if i > mid:
            total += (i - mid)
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < M:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답
        start = mid + 1

print(result)
