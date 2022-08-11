import sys

N = int(sys.stdin.readline().rstrip())
# 집합 자료형으로 기록
N_array = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
M_array = list(map(int, sys.stdin.readline().split()))

for i in M_array:
    if i in N_array:
        print("yes", end=" ")
    else:
        print("no", end=" ")
