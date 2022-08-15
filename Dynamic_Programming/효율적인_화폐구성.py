import sys

n, m = map(int, sys.stdin.readline().split())

nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
# n개의 화폐 단위에 대하여
for i in range(n):
    # price를 만들기 위한 최소 화폐 개수 구하기
    for j in range(nums[i], m + 1):
        # (price - 화폐단위)를 만드는 방법이 있으면
        d[j] = min(d[j], d[j - nums[i]] + 1)


# 최종적으로 M원을 만드는 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
